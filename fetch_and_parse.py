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
from pathlib import Path

import cloudscraper
from tqdm import tqdm

from html_to_markdown import HTMLToMarkdown


API_URL = "https://stellaris.paradoxwikis.com/api.php"

PAGES_TO_FETCH = [
    # Empire Setup
    "Origin",
    "Government",
    "Ethics",
    "Civics",
    "Corporate civics",
    "Hive mind civics",
    "Machine intelligence civics",
    "Empire",
    # Governance
    "Council",
    "Policies",
    "Edicts",
    "Factions",
    "Traditions",
    "Ascension_perks",
    "Situations",
    "Crisis_empire",
    # Species
    "Species",
    "Species_traits",
    "Biological_traits",
    "Machine_traits",
    "Population",
    "Species_rights",
    # Leaders
    "Leaders",
    "Common_leader_traits",
    "Commander_traits",
    "Scientist_traits",
    "Official_traits",
    "Paragons",
    # Economy & Buildings
    "Resources",
    "Planetary_management",
    "Jobs",
    "Districts",
    "Designation",
    "Holdings",
    "Planet_capital",
    "Unique_buildings",
    "Megastructures",
    "Colonization",
    # Technology
    "Technology",
    "Physics_research",
    "Society_research",
    "Engineering_research",
    # Ships & Components
    "Ship",
    "Ship_designer",
    "Core_components",
    "Weapon_components",
    "Utility_components",
    "Mutations",
    "Offensive mutations",
    # Military
    "Warfare",
    "Space_warfare",
    "Land warfare",
    "Starbase",
    # Exploration & Discovery
    "Exploration",
    "FTL travel",
    "Discovery",
    "Anomaly",
    "Archaeological site",
    "Astral rift",
    "Celestial_object",
    "Planet_modifiers",
    "Planetary_features",
    "Unique_systems",
    "Relics",
    "Collection",
    "L-Cluster",
    "The_Shroud",
    # Diplomacy & Relations
    "Diplomacy",
    "Relations",
    "Galactic Community",
    "Federation",
    "Subject empire",
    "Intelligence",
    "AI personalities",
    # NPCs & Encounters
    "Fallen empire",
    "Spaceborne aliens",
    "Pre-FTL species",
    "Enclaves",
    "Guardians",
    "Marauders",
    "Caravaneers",
    # Modifiers & Events
    "Empire_modifiers",
    "Stat_modifiers",
    "Events",
    # Reference & Other
    "Achievements",
    "Crisis",
    "Galaxy settings",
    "Beginner's guide",
    "Hotkeys",
    "Jargon",
    "User interface",
    "Console_commands",
    "Easter eggs",
    "AI players",
    "Preset empires",
    "Modding",
]


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
            response = session.get(API_URL, params=params, timeout=30)
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


def process_all_pages(page_titles: list[str], output_dir: Path, delay: float = 0.5):
    """Fetch and convert all pages to Markdown.

    Args:
        page_titles: List of page titles to process
        output_dir: Directory for output files
        delay: Delay between requests in seconds
    """
    session = create_session()
    converter = HTMLToMarkdown()

    # Create output directory
    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    all_markdown = []
    successful = 0
    failed = 0

    print(f"\nProcessing {len(page_titles)} pages...")
    print(f"Output directory: {output_dir}")
    print("-" * 60)

    for title in tqdm(page_titles, desc="Converting", unit=" pages"):
        full_md, success = process_single_page(
            session, converter, title, pages_dir, delay
        )

        if success:
            all_markdown.append(full_md)
            successful += 1
        else:
            failed += 1

    # Save combined file
    if all_markdown:
        combined = "\n\n---\n\n".join(all_markdown)
        combined_path = output_dir / "stellaris_4.2_combined.md"
        combined_path.write_text(combined, encoding="utf-8")
        combined_size = combined_path.stat().st_size

        print("\n" + "=" * 60)
        print("Conversion Complete!")
        print("=" * 60)
        print(f"Pages processed: {successful} successful, {failed} failed")
        print(f"Individual files: {pages_dir}")
        print(f"Combined file: {combined_path}")
        print(f"Combined size: {combined_size / 1024 / 1024:.2f} MB")

        # Calculate total individual file sizes
        total_size = sum(f.stat().st_size for f in pages_dir.glob("*.md"))
        print(f"Total individual files size: {total_size / 1024 / 1024:.2f} MB")


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
        default="output_markdown",
        help="Output directory (default: output_markdown)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between API requests in seconds (default: 0.5)"
    )
    args = parser.parse_args()

    output_dir = Path(__file__).parent / args.output

    if args.page and args.test:
        test_single_page(args.page, output_dir)
    elif args.page:
        # Process single page without test output
        session = create_session()
        converter = HTMLToMarkdown()
        pages_dir = output_dir / "pages"
        pages_dir.mkdir(parents=True, exist_ok=True)
        full_md, success = process_single_page(
            session, converter, args.page, pages_dir, args.delay
        )
        if success:
            print(f"Processed: {args.page}")
        else:
            print(f"Failed: {args.page}")
            sys.exit(1)
    else:
        page_titles = PAGES_TO_FETCH
        print(f"Processing {len(page_titles)} pages")
        process_all_pages(page_titles, output_dir, args.delay)


if __name__ == "__main__":
    main()
