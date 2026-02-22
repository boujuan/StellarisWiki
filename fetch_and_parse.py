#!/usr/bin/env python3
"""
Fetch Stellaris Wiki pages as HTML and convert to Markdown.

This script uses MediaWiki's action=parse API to get server-rendered HTML,
then converts it to clean Markdown optimized for LLM consumption.
"""

import argparse
import json
import re
import sys
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import unquote

import cloudscraper
from bs4 import BeautifulSoup, Tag
from tqdm import tqdm

from html_to_markdown import HTMLToMarkdown
from config import cfg

# Known error patterns in wiki-rendered content
CONTENT_ERROR_PATTERNS = [
    (re.compile(r'Failed to parse \(SVG.*?\)'), "Math render error"),
    (re.compile(r'{\s*\\displaystyle'), "Raw LaTeX not rendered"),
]


def check_content_errors(title: str, markdown: str) -> list[str]:
    """Check converted markdown for known content errors.

    Returns list of warning strings (empty if no errors).
    """
    warnings = []
    for pattern, label in CONTENT_ERROR_PATTERNS:
        matches = pattern.findall(markdown)
        if matches:
            warnings.append(f"{title}: {label} ({len(matches)} occurrence{'s' if len(matches) > 1 else ''})")
    return warnings

# Backward-compatible alias (analyze_wiki_pages.py imports this)
PAGES_TO_FETCH = cfg.pages_to_fetch


def create_session():
    """Create a cloudscraper session to bypass Cloudflare."""
    session = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "linux", "desktop": True}
    )
    session.headers.update({
        "User-Agent": "StellarisWikiScraper/1.0 (Educational/Research purposes)"
    })
    return session


def fetch_page_html(session, title: str, max_retries: int = 5) -> dict | None:
    """Fetch single page as rendered HTML using action=parse.

    Args:
        session: The cloudscraper session
        title: Page title to fetch
        max_retries: Maximum retry attempts

    Returns:
        Dict with page data or None if failed
    """
    params = {
        "action": "parse",
        "page": title,
        "prop": "text|sections|categories|displaytitle",
        "disabletoc": "true",
        "disableeditsection": "true",
        "format": "json",
    }

    for attempt in range(max_retries):
        try:
            response = session.get(cfg.wiki.api_url, params=params, timeout=30)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "application/json" not in content_type:
                if attempt < max_retries - 1:
                    wait_time = 2.0 * (2 ** attempt)
                    print(f"\nNon-JSON response for '{title}', retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    continue
                return None

            data = response.json()

            if "error" in data:
                error_msg = data["error"].get("info", "Unknown error")
                print(f"\nAPI error for '{title}': {error_msg}")
                return None

            parse_data = data.get("parse", {})

            return {
                "title": parse_data.get("displaytitle", title),
                "pageid": parse_data.get("pageid"),
                "html": parse_data.get("text", {}).get("*", ""),
                "sections": parse_data.get("sections", []),
                "categories": [c["*"] for c in parse_data.get("categories", [])]
            }

        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2.0 * (2 ** attempt)
                print(f"\nError fetching '{title}': {e}. Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"\nFailed to fetch '{title}' after {max_retries} attempts: {e}")
                return None

    return None


def sanitize_filename(title: str) -> str:
    """Convert page title to safe filename."""
    safe = re.sub(r'[<>:"/\\|?*]', "_", title)
    safe = safe.replace(" ", "_")
    if len(safe) > 200:
        safe = safe[:200]
    return safe



def strip_html_from_title(title: str) -> str:
    """Strip HTML tags from title."""
    if '<' in title:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(title, 'lxml')
        return soup.get_text(strip=True)
    return title


def create_yaml_frontmatter(title: str, categories: list[str]) -> str:
    """Create YAML frontmatter for markdown file."""
    # Strip HTML and escape quotes in title
    clean_title = strip_html_from_title(title)
    safe_title = clean_title.replace('"', '\\"')
    # Format categories as YAML list
    cat_str = json.dumps(categories)
    return f'---\ntitle: "{safe_title}"\ncategories: {cat_str}\n---\n\n'


def process_single_page(session, converter: HTMLToMarkdown, title: str,
                        output_dir: Path, delay: float = 0.5) -> tuple[str, bool]:
    """Process a single page: fetch and convert to Markdown.

    Args:
        session: The cloudscraper session
        converter: HTMLToMarkdown instance
        title: Page title
        output_dir: Directory for output files
        delay: Delay between requests

    Returns:
        Tuple of (markdown_content, success)
    """
    # Rate limiting
    time.sleep(delay)

    # Fetch HTML
    data = fetch_page_html(session, title)
    if not data or not data.get("html"):
        return "", False

    # Convert to Markdown
    markdown = converter.convert(data["html"], data["title"])

    # Add frontmatter
    frontmatter = create_yaml_frontmatter(data["title"], data["categories"])
    full_md = frontmatter + markdown

    # Save individual file
    filename = sanitize_filename(title) + ".md"
    output_path = output_dir / filename
    output_path.write_text(full_md, encoding="utf-8")

    return full_md, True


def _fetch_and_convert(title: str, pages_dir: Path) -> tuple[str, str, bool, list[str]]:
    """Fetch and convert a single page (for use in thread pool).

    Each thread creates its own session to avoid sharing state.

    Returns:
        Tuple of (title, markdown_content, success, warnings)
    """
    session = create_session()
    converter = HTMLToMarkdown()

    data = fetch_page_html(session, title)
    if not data or not data.get("html"):
        return title, "", False, []

    markdown = converter.convert(data["html"], data["title"])
    frontmatter = create_yaml_frontmatter(data["title"], data["categories"])
    full_md = frontmatter + markdown

    filename = sanitize_filename(title) + ".md"
    output_path = pages_dir / filename
    output_path.write_text(full_md, encoding="utf-8")

    warnings = check_content_errors(title, full_md)
    return title, full_md, True, warnings


def extract_event_subpage_links(html: str) -> list[tuple[str, list[str]]]:
    """Extract event sub-page links from the Events page HTML.

    Parses the stellaris-outliner divs to find categorized event chain links.

    Returns:
        List of (category_name, [page_titles]) tuples
    """
    soup = BeautifulSoup(html, 'lxml')
    categories = []

    for outliner in soup.find_all('div', class_='stellaris-outliner'):
        header_div = outliner.find('div', class_='stellaris-outliner-header')
        if not header_div:
            continue
        header_text = header_div.get_text(strip=True)

        # Skip the version/status box
        if 'version' in header_text.lower() or 'article' in header_text.lower():
            continue

        content_div = outliner.find('div', class_='stellaris-outliner-content')
        if not content_div:
            continue

        page_titles = []
        for row in content_div.find_all('div', class_='infobox-row-single'):
            for a in row.find_all('a'):
                href = a.get('href', '')
                if not href.startswith('/'):
                    continue
                # Extract page title from href (e.g., "/Horizon_Signal" -> "Horizon Signal")
                page_title = unquote(href.lstrip('/').replace('_', ' '))
                # Skip self-reference and DLC pages
                if page_title == 'Events' or not page_title:
                    continue
                if page_title not in page_titles:
                    page_titles.append(page_title)

        if page_titles:
            categories.append((header_text, page_titles))

    return categories


def extract_astral_rift_subpage_links(html: str) -> list[tuple[str, list[str]]]:
    """Extract astral rift sub-page links from the Astral rift page HTML.

    Finds all "(see full rift details)" links pointing to individual rift pages.

    Returns:
        List of (category_name, [page_titles]) tuples
    """
    soup = BeautifulSoup(html, 'lxml')
    subpages = []

    for a in soup.find_all('a'):
        if 'full rift details' in a.get_text():
            href = a.get('href', '').lstrip('/')
            if href:
                title = unquote(href.replace('_', ' '))
                if title not in subpages:
                    subpages.append(title)

    if subpages:
        return [("Astral Rift Details", subpages)]
    return []


# Map config function-name strings to actual callables
_COMPOSITE_EXTRACTORS = {
    "extract_event_subpage_links": extract_event_subpage_links,
    "extract_astral_rift_subpage_links": extract_astral_rift_subpage_links,
}

# Pages that are index pages — their sub-page links are extracted from HTML
# and each sub-page's content is appended to the parent page's markdown.
COMPOSITE_PAGES = {}
for _title, _func_name in cfg.composite_pages.items():
    if _func_name not in _COMPOSITE_EXTRACTORS:
        raise ValueError(
            f"Unknown composite extractor '{_func_name}' for page '{_title}'. "
            f"Available: {list(_COMPOSITE_EXTRACTORS.keys())}"
        )
    COMPOSITE_PAGES[_title] = _COMPOSITE_EXTRACTORS[_func_name]


def _fetch_and_convert_body(title: str) -> tuple[str, str, bool]:
    """Fetch a page and return only the markdown body (no frontmatter, no file write).

    Used for sub-pages that will be appended to a composite page.
    """
    session = create_session()
    converter = HTMLToMarkdown()

    data = fetch_page_html(session, title)
    if not data or not data.get("html"):
        return title, "", False

    markdown = converter.convert(data["html"], data["title"])
    return title, markdown, True


def process_composite_page(title: str, pages_dir: Path,
                           workers: int = 4) -> tuple[str, bool]:
    """Process a composite page: fetch main page + all sub-pages, combine into one file.

    Args:
        title: Main page title (e.g., "Events")
        pages_dir: Directory for output files
        workers: Number of parallel workers for sub-page fetching

    Returns:
        Tuple of (full_markdown_content, success)
    """
    print(f"\n  Fetching composite page: {title}")

    # Step 1: Fetch the main page
    session = create_session()
    data = fetch_page_html(session, title)
    if not data or not data.get("html"):
        return "", False

    # Step 2: Convert main page to markdown
    converter = HTMLToMarkdown()
    main_markdown = converter.convert(data["html"], data["title"])

    # Step 3: Extract sub-page links from the raw HTML
    extract_fn = COMPOSITE_PAGES[title]
    categories = extract_fn(data["html"])

    # Collect all unique sub-page titles
    all_subpages = []
    for _, page_titles in categories:
        for pt in page_titles:
            if pt not in all_subpages:
                all_subpages.append(pt)

    print(f"  Found {len(all_subpages)} sub-pages across {len(categories)} categories")

    # Step 4: Fetch all sub-pages in parallel
    subpage_content = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(_fetch_and_convert_body, pt): pt
            for pt in all_subpages
        }
        with tqdm(total=len(all_subpages), desc=f"  Sub-pages", unit=" pages",
                  leave=False) as pbar:
            for future in as_completed(futures):
                pt, md, success = future.result()
                if success:
                    subpage_content[pt] = md
                else:
                    print(f"\n  Warning: Failed to fetch sub-page '{pt}'")
                pbar.update(1)

    print(f"  Fetched {len(subpage_content)}/{len(all_subpages)} sub-pages")

    # Step 5: Build the combined markdown
    parts = [main_markdown]

    for category_name, page_titles in categories:
        parts.append(f"\n\n---\n\n## {category_name}\n")
        for pt in page_titles:
            if pt in subpage_content:
                parts.append(f"\n{subpage_content[pt]}\n")

    combined_md = "\n".join(parts)

    # Step 6: Add frontmatter and save
    frontmatter = create_yaml_frontmatter(data["title"], data["categories"])
    full_md = frontmatter + combined_md

    filename = sanitize_filename(title) + ".md"
    output_path = pages_dir / filename
    output_path.write_text(full_md, encoding="utf-8")

    size_kb = output_path.stat().st_size / 1024
    print(f"  Saved {filename} ({size_kb:.1f} KB)")

    return full_md, True


def process_all_pages(page_titles: list[str], output_dir: Path,
                      delay: float = 0.5, workers: int = 1):
    """Fetch and convert all pages to Markdown.

    Args:
        page_titles: List of page titles to process
        output_dir: Directory for output files
        delay: Delay between requests in seconds (used in sequential mode)
        workers: Number of parallel workers (1 = sequential)
    """
    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    # Dict to preserve page order for combined file
    results = {}
    successful = 0
    failed = 0
    all_warnings = []

    print(f"\nProcessing {len(page_titles)} pages (workers={workers})...")
    print(f"Output directory: {output_dir}")
    print("-" * 60)

    # Separate composite pages from regular pages
    composite_titles = [t for t in page_titles if t in COMPOSITE_PAGES]
    regular_titles = [t for t in page_titles if t not in COMPOSITE_PAGES]

    # Process regular pages
    if regular_titles:
        if workers > 1:
            with ThreadPoolExecutor(max_workers=workers) as executor:
                futures = {
                    executor.submit(_fetch_and_convert, title, pages_dir): title
                    for title in regular_titles
                }
                with tqdm(total=len(regular_titles), desc="Regular pages",
                          unit=" pages") as pbar:
                    for future in as_completed(futures):
                        title, full_md, success, page_warnings = future.result()
                        if success:
                            results[title] = full_md
                            successful += 1
                            all_warnings.extend(page_warnings)
                        else:
                            failed += 1
                        pbar.update(1)
        else:
            session = create_session()
            converter = HTMLToMarkdown()
            for title in tqdm(regular_titles, desc="Regular pages", unit=" pages"):
                full_md, success = process_single_page(
                    session, converter, title, pages_dir, delay
                )
                if success:
                    results[title] = full_md
                    successful += 1
                    all_warnings.extend(check_content_errors(title, full_md))
                else:
                    failed += 1

    # Process composite pages (these handle their own parallelism)
    for title in composite_titles:
        full_md, success = process_composite_page(title, pages_dir, workers)
        if success:
            results[title] = full_md
            successful += 1
            all_warnings.extend(check_content_errors(title, full_md))
        else:
            failed += 1

    # Save combined file in original page order
    if results:
        ordered_markdown = [results[t] for t in page_titles if t in results]
        combined = "\n\n---\n\n".join(ordered_markdown)
        combined_path = output_dir / cfg.combined_filename
        combined_path.write_text(combined, encoding="utf-8")
        combined_size = combined_path.stat().st_size

        print("\n" + "=" * 60)
        print("Conversion Complete!")
        print("=" * 60)
        print(f"Pages processed: {successful} successful, {failed} failed")
        print(f"Individual files: {pages_dir}")
        print(f"Combined file: {combined_path}")
        print(f"Combined size: {combined_size / 1024 / 1024:.2f} MB")

        total_size = sum(f.stat().st_size for f in pages_dir.glob("*.md"))
        print(f"Total individual files size: {total_size / 1024 / 1024:.2f} MB")

        zip_path = create_zip(pages_dir, output_dir)
        print(f"Zip archive: {zip_path} ({zip_path.stat().st_size / 1024 / 1024:.2f} MB)")

        if all_warnings:
            print(f"\n⚠ Content warnings ({len(all_warnings)}):")
            for w in all_warnings:
                print(f"  - {w}")
        else:
            print("\nNo content warnings.")


def create_zip(pages_dir: Path, output_dir: Path):
    """Create a zip archive of all markdown files."""
    zip_path = output_dir / "stellaris_wiki_pages.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for md_file in sorted(pages_dir.glob("*.md")):
            zf.write(md_file, f"pages/{md_file.name}")
        combined = output_dir / cfg.combined_filename
        if combined.exists():
            zf.write(combined, combined.name)
    return zip_path


def test_single_page(title: str, output_dir: Path):
    """Test processing of a single page.

    Args:
        title: Page title to test
        output_dir: Directory for output files
    """
    session = create_session()
    converter = HTMLToMarkdown()

    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    print(f"Testing single page: {title}")
    print("-" * 60)

    full_md, success = process_single_page(session, converter, title, pages_dir)

    if success:
        filename = sanitize_filename(title) + ".md"
        output_path = pages_dir / filename
        print(f"Success! Output saved to: {output_path}")
        print(f"File size: {output_path.stat().st_size / 1024:.2f} KB")

        warnings = check_content_errors(title, full_md)
        if warnings:
            print(f"\n⚠ Content warnings:")
            for w in warnings:
                print(f"  - {w}")

        print("\nFirst 2000 characters of output:")
        print("-" * 60)
        print(full_md[:2000])
        if len(full_md) > 2000:
            print(f"\n... ({len(full_md) - 2000} more characters)")
    else:
        print("Failed to process page!")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch Stellaris Wiki pages and convert to Markdown"
    )
    parser.add_argument(
        "--page",
        type=str,
        help="Process a single page (for testing)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode (with --page)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=cfg.defaults.output_dir,
        help=f"Output directory (default: {cfg.defaults.output_dir})"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=cfg.defaults.delay,
        help=f"Delay between API requests in seconds (default: {cfg.defaults.delay}, sequential mode only)"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=cfg.defaults.workers,
        help=f"Number of parallel workers (default: {cfg.defaults.workers}, use 1 for sequential)"
    )
    args = parser.parse_args()

    output_dir = Path(__file__).parent / args.output

    if args.page and args.test:
        if args.page in COMPOSITE_PAGES:
            pages_dir = output_dir / "pages"
            pages_dir.mkdir(parents=True, exist_ok=True)
            full_md, success = process_composite_page(
                args.page, pages_dir, args.workers
            )
            if success:
                filename = sanitize_filename(args.page) + ".md"
                output_path = pages_dir / filename
                print(f"Success! Output saved to: {output_path}")
                print(f"File size: {output_path.stat().st_size / 1024:.2f} KB")

                warnings = check_content_errors(args.page, full_md)
                if warnings:
                    print(f"\n⚠ Content warnings:")
                    for w in warnings:
                        print(f"  - {w}")

                print("\nFirst 2000 characters of output:")
                print("-" * 60)
                print(full_md[:2000])
                if len(full_md) > 2000:
                    print(f"\n... ({len(full_md) - 2000} more characters)")
            else:
                print("Failed to process composite page!")
                sys.exit(1)
        else:
            test_single_page(args.page, output_dir)
    elif args.page:
        pages_dir = output_dir / "pages"
        pages_dir.mkdir(parents=True, exist_ok=True)
        if args.page in COMPOSITE_PAGES:
            full_md, success = process_composite_page(
                args.page, pages_dir, args.workers
            )
        else:
            session = create_session()
            converter = HTMLToMarkdown()
            full_md, success = process_single_page(
                session, converter, args.page, pages_dir, args.delay
            )
        if success:
            print(f"Processed: {args.page}")
        else:
            print(f"Failed: {args.page}")
            sys.exit(1)
    else:
        page_titles = cfg.pages_to_fetch
        print(f"Processing {len(page_titles)} pages")
        process_all_pages(page_titles, output_dir, args.delay, args.workers)


if __name__ == "__main__":
    main()
