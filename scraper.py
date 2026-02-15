#!/usr/bin/env python3
"""
Stellaris Wiki Scraper

Scrapes all content from https://stellaris.paradoxwikis.com/ using the MediaWiki API.
Uses cloudscraper to bypass JavaScript challenge protection.

Usage:
    python scraper.py --output ./wiki_data                    # Full scrape
    python scraper.py --test --output ./wiki_data             # Test mode (first 10 pages)
    python scraper.py --namespace 0 --output ./wiki_data      # Main articles only
    python scraper.py --resume --output ./wiki_data           # Resume interrupted scrape
"""

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import cloudscraper
from tqdm import tqdm


class WikiScraper:
    """Scraper for Stellaris Paradox Wiki using MediaWiki API."""

    BASE_URL = "https://stellaris.paradoxwikis.com"
    API_URL = f"{BASE_URL}/api.php"

    # Namespace IDs: 0=Main, 6=File, 10=Template, 14=Category
    NAMESPACES = {
        0: "Main",
        6: "File",
        10: "Template",
        14: "Category",
    }

    def __init__(
        self,
        output_dir: str,
        delay: float = 1.0,
        batch_size: int = 50,
        namespaces: Optional[list[int]] = None,
    ):
        """
        Initialize the scraper.

        Args:
            output_dir: Directory to save scraped content
            delay: Delay between requests in seconds
            batch_size: Number of pages to fetch per batch request
            namespaces: List of namespace IDs to scrape (default: [0] for main articles)
        """
        self.output_dir = Path(output_dir)
        self.pages_dir = self.output_dir / "pages"
        self.delay = delay
        self.batch_size = min(batch_size, 50)  # API limit is 50
        self.namespaces = namespaces if namespaces is not None else [0]

        # Create output directories
        self.pages_dir.mkdir(parents=True, exist_ok=True)

        # Create cloudscraper session
        self.session = cloudscraper.create_scraper(
            browser={
                "browser": "chrome",
                "platform": "linux",
                "desktop": True,
            }
        )
        self.session.headers.update(
            {
                "User-Agent": "StellarisWikiScraper/1.0 (Educational/Research purposes)",
            }
        )

        # Progress tracking file
        self.progress_file = self.output_dir / "progress.json"
        self.scraped_pages: set[str] = set()
        self._load_progress()

    def _load_progress(self) -> None:
        """Load progress from previous run."""
        if self.progress_file.exists():
            with open(self.progress_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.scraped_pages = set(data.get("scraped_pages", []))

    def _save_progress(self) -> None:
        """Save current progress."""
        with open(self.progress_file, "w", encoding="utf-8") as f:
            json.dump({"scraped_pages": list(self.scraped_pages)}, f)

    def _api_request(
        self, params: dict, max_retries: int = 5, base_delay: float = 2.0
    ) -> Optional[dict]:
        """
        Make an API request with exponential backoff retry.

        Args:
            params: API parameters
            max_retries: Maximum number of retries
            base_delay: Base delay for exponential backoff

        Returns:
            JSON response or None on failure
        """
        params["format"] = "json"

        for attempt in range(max_retries):
            try:
                time.sleep(self.delay)
                response = self.session.get(self.API_URL, params=params, timeout=30)

                # Check for Retry-After header
                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", base_delay))
                    print(f"\nRate limited. Waiting {retry_after} seconds...")
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()

                # Check if response is JSON
                content_type = response.headers.get("Content-Type", "")
                if "application/json" not in content_type:
                    # Might be a challenge page
                    if attempt < max_retries - 1:
                        wait_time = base_delay * (2**attempt)
                        print(
                            f"\nGot non-JSON response, retrying in {wait_time:.1f}s..."
                        )
                        time.sleep(wait_time)
                        continue
                    else:
                        print(f"\nFailed to get JSON response after {max_retries} attempts")
                        return None

                return response.json()

            except Exception as e:
                if attempt < max_retries - 1:
                    wait_time = base_delay * (2**attempt)
                    print(f"\nError: {e}. Retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                else:
                    print(f"\nFailed after {max_retries} attempts: {e}")
                    return None

        return None

    def get_all_pages(self, namespace: int = 0) -> list[dict]:
        """
        Get all page titles in a namespace using list=allpages.

        Args:
            namespace: Namespace ID to enumerate

        Returns:
            List of page info dicts with 'pageid', 'ns', 'title'
        """
        pages = []
        apcontinue = None

        print(f"Fetching page list for namespace {namespace} ({self.NAMESPACES.get(namespace, 'Unknown')})...")

        with tqdm(desc="Listing pages", unit=" pages") as pbar:
            while True:
                params = {
                    "action": "query",
                    "list": "allpages",
                    "apnamespace": namespace,
                    "aplimit": 500,  # Maximum allowed
                }
                if apcontinue:
                    params["apcontinue"] = apcontinue

                data = self._api_request(params)
                if not data:
                    break

                if "query" in data and "allpages" in data["query"]:
                    batch = data["query"]["allpages"]
                    pages.extend(batch)
                    pbar.update(len(batch))

                # Check for continuation
                if "continue" in data and "apcontinue" in data["continue"]:
                    apcontinue = data["continue"]["apcontinue"]
                else:
                    break

        print(f"Found {len(pages)} pages in namespace {namespace}")
        return pages

    def get_page_content_batch(self, titles: list[str]) -> list[dict]:
        """
        Fetch content for multiple pages in a single request.

        Args:
            titles: List of page titles (max 50)

        Returns:
            List of page data dicts
        """
        if not titles:
            return []

        # Join titles with pipe, properly encoded
        titles_param = "|".join(titles)

        params = {
            "action": "query",
            "titles": titles_param,
            "prop": "revisions|categories",
            "rvprop": "content|timestamp",
            "rvslots": "main",
            "cllimit": "max",
        }

        data = self._api_request(params)
        if not data or "query" not in data or "pages" not in data["query"]:
            return []

        results = []
        for page_id, page_data in data["query"]["pages"].items():
            # Skip missing pages
            if "missing" in page_data:
                continue

            # Extract content from revision
            content = ""
            timestamp = ""
            if "revisions" in page_data and page_data["revisions"]:
                rev = page_data["revisions"][0]
                timestamp = rev.get("timestamp", "")
                if "slots" in rev and "main" in rev["slots"]:
                    content = rev["slots"]["main"].get("*", "")

            # Extract categories
            categories = []
            if "categories" in page_data:
                categories = [
                    cat["title"].replace("Category:", "")
                    for cat in page_data["categories"]
                ]

            results.append(
                {
                    "title": page_data.get("title", ""),
                    "pageid": int(page_id) if page_id.lstrip("-").isdigit() else 0,
                    "ns": page_data.get("ns", 0),
                    "timestamp": timestamp,
                    "categories": categories,
                    "content": content,
                }
            )

        return results

    def _sanitize_filename(self, title: str) -> str:
        """Convert page title to safe filename."""
        # Replace problematic characters
        safe = re.sub(r'[<>:"/\\|?*]', "_", title)
        safe = safe.replace(" ", "_")
        # Limit length
        if len(safe) > 200:
            safe = safe[:200]
        return safe

    def save_page(self, page_data: dict) -> None:
        """Save page data to individual JSON file."""
        filename = self._sanitize_filename(page_data["title"]) + ".json"
        filepath = self.pages_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)

    def save_jsonl(self, pages: list[dict], filename: str = "wiki_dump.jsonl") -> None:
        """Save all pages to a single JSONL file."""
        filepath = self.output_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            for page in pages:
                f.write(json.dumps(page, ensure_ascii=False) + "\n")

        print(f"Saved {len(pages)} pages to {filepath}")

    def scrape_all(
        self, test_mode: bool = False, resume: bool = False, limit: int = 10
    ) -> list[dict]:
        """
        Main scraping loop.

        Args:
            test_mode: If True, only scrape first `limit` pages
            resume: If True, skip already scraped pages
            limit: Number of pages to scrape in test mode

        Returns:
            List of all scraped page data
        """
        all_pages_info = []

        # Get page lists for all requested namespaces
        for ns in self.namespaces:
            pages = self.get_all_pages(namespace=ns)
            all_pages_info.extend(pages)

        if not all_pages_info:
            print("No pages found!")
            return []

        # Filter out already scraped pages if resuming
        if resume and self.scraped_pages:
            original_count = len(all_pages_info)
            all_pages_info = [
                p for p in all_pages_info if p["title"] not in self.scraped_pages
            ]
            print(
                f"Resuming: {original_count - len(all_pages_info)} pages already scraped, {len(all_pages_info)} remaining"
            )

        # Limit pages in test mode
        if test_mode:
            all_pages_info = all_pages_info[:limit]
            print(f"Test mode: limiting to {len(all_pages_info)} pages")

        all_scraped = []

        # Process in batches
        print(f"\nScraping {len(all_pages_info)} pages...")
        with tqdm(total=len(all_pages_info), desc="Scraping", unit=" pages") as pbar:
            for i in range(0, len(all_pages_info), self.batch_size):
                batch_info = all_pages_info[i : i + self.batch_size]
                titles = [p["title"] for p in batch_info]

                # Fetch batch
                batch_data = self.get_page_content_batch(titles)

                # Save each page
                for page_data in batch_data:
                    self.save_page(page_data)
                    self.scraped_pages.add(page_data["title"])
                    all_scraped.append(page_data)

                pbar.update(len(batch_info))

                # Save progress periodically
                if len(all_scraped) % 100 == 0:
                    self._save_progress()

        # Final progress save
        self._save_progress()

        # Save combined JSONL dump
        if all_scraped:
            self.save_jsonl(all_scraped)

        print(f"\nScraping complete! {len(all_scraped)} pages saved to {self.output_dir}")
        return all_scraped


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Stellaris Wiki content using MediaWiki API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scraper.py --output ./wiki_data                    # Full scrape (main articles)
  python scraper.py --test --output ./wiki_data             # Test mode (first 10 pages)
  python scraper.py --namespace 0 14 --output ./wiki_data   # Main articles and categories
  python scraper.py --resume --output ./wiki_data           # Resume interrupted scrape
  python scraper.py --delay 2.0 --output ./wiki_data        # Slower scraping (2s delay)
        """,
    )

    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="./output",
        help="Output directory for scraped content (default: ./output)",
    )
    parser.add_argument(
        "--test",
        "-t",
        action="store_true",
        help="Test mode: only scrape first 10 pages",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=10,
        help="Number of pages to scrape in test mode (default: 10)",
    )
    parser.add_argument(
        "--resume",
        "-r",
        action="store_true",
        help="Resume from previous scrape (skip already downloaded pages)",
    )
    parser.add_argument(
        "--namespace",
        "-n",
        type=int,
        nargs="+",
        default=[0],
        help="Namespace IDs to scrape (default: 0 for main articles). "
        "Common namespaces: 0=Main, 6=File, 10=Template, 14=Category",
    )
    parser.add_argument(
        "--delay",
        "-d",
        type=float,
        default=1.0,
        help="Delay between API requests in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--batch-size",
        "-b",
        type=int,
        default=50,
        help="Number of pages per batch request (default: 50, max: 50)",
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Stellaris Wiki Scraper")
    print("=" * 60)
    print(f"Output directory: {args.output}")
    print(f"Namespaces: {args.namespace}")
    print(f"Delay: {args.delay}s")
    print(f"Batch size: {args.batch_size}")
    print(f"Test mode: {args.test}")
    print(f"Resume mode: {args.resume}")
    print("=" * 60)

    scraper = WikiScraper(
        output_dir=args.output,
        delay=args.delay,
        batch_size=args.batch_size,
        namespaces=args.namespace,
    )

    scraper.scrape_all(test_mode=args.test, resume=args.resume, limit=args.limit)


if __name__ == "__main__":
    main()
