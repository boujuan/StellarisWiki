#!/usr/bin/env python3
"""
Fetch specific Stellaris Wiki pages.

This script fetches a predefined list of pages from the Stellaris Wiki.
"""

import json
import os
import re
import time
from pathlib import Path

import cloudscraper
from tqdm import tqdm


# Pages to fetch (deduplicated)
PAGES_TO_FETCH = [
    "Origin",
    "Traditions",
    "Technology",
    "Empire_modifiers",
    "Ascension_perks",
    "Crisis_empire",
    "Government",
    "Council",
    "Civics",
    "Events",
    "Policies",
    "Edicts",
    "Factions",
    "Situations",
    "Resources",
    "Planetary_management",
    "Jobs",
    "Designation",
    "Warfare",
    "Starbase",
    "Ship",
    "Stat_modifiers",
    "Exploration",
    "Celestial_object",
    "Population",
    "Leaders",
    "Ethics",
    "Species_traits",
    "Species_rights",
    "Empire",
    "Biological_traits",
    "Machine_traits",
    "Discovery",
    "Anomaly",
    "Planet_modifiers",
    "Planetary_features",
    "Colonization",
    "Unique_systems",
    "Common_leader_traits",
    "Commander_traits",
    "Scientist_traits",
    "Official_traits",
    "Paragons",
    "Districts",
    "Megastructures",
    "Planet_capital",
    "Unique_buildings",
    "Ship_designer",
    "Core_components",
    "Weapon_components",
    "Utility_components",
    "Physics_research",
    "Society_research",
    "Engineering_research",
    "Space_warfare",
    "The_Shroud",
]

API_URL = "https://stellaris.paradoxwikis.com/api.php"


def create_session():
    """Create a cloudscraper session."""
    session = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "linux", "desktop": True}
    )
    session.headers.update(
        {"User-Agent": "StellarisWikiScraper/1.0 (Educational/Research purposes)"}
    )
    return session


def fetch_pages_batch(session, titles, delay=1.0, max_retries=5):
    """Fetch multiple pages in a single API request."""
    params = {
        "action": "query",
        "titles": "|".join(titles),
        "prop": "revisions|categories",
        "rvprop": "content|timestamp",
        "rvslots": "main",
        "cllimit": "max",
        "format": "json",
    }

    for attempt in range(max_retries):
        try:
            time.sleep(delay)
            response = session.get(API_URL, params=params, timeout=30)
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "application/json" not in content_type:
                if attempt < max_retries - 1:
                    wait_time = 2.0 * (2**attempt)
                    print(f"\nNon-JSON response, retrying in {wait_time:.1f}s...")
                    time.sleep(wait_time)
                    continue
                return []

            data = response.json()
            if "query" not in data or "pages" not in data["query"]:
                return []

            results = []
            for page_id, page_data in data["query"]["pages"].items():
                if "missing" in page_data:
                    print(f"\nWarning: Page '{page_data.get('title', 'Unknown')}' not found")
                    continue

                content = ""
                timestamp = ""
                if "revisions" in page_data and page_data["revisions"]:
                    rev = page_data["revisions"][0]
                    timestamp = rev.get("timestamp", "")
                    if "slots" in rev and "main" in rev["slots"]:
                        content = rev["slots"]["main"].get("*", "")

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

        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2.0 * (2**attempt)
                print(f"\nError: {e}. Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"\nFailed after {max_retries} attempts: {e}")
                return []

    return []


def sanitize_filename(title):
    """Convert page title to safe filename."""
    safe = re.sub(r'[<>:"/\\|?*]', "_", title)
    safe = safe.replace(" ", "_")
    if len(safe) > 200:
        safe = safe[:200]
    return safe


def main():
    output_dir = Path("./output_4.2")
    pages_dir = output_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Stellaris Wiki - Specific Pages Fetcher")
    print("=" * 60)
    print(f"Pages to fetch: {len(PAGES_TO_FETCH)}")
    print(f"Output directory: {output_dir}")
    print("=" * 60)

    session = create_session()
    all_pages = []
    batch_size = 10  # Smaller batches to be safe

    print(f"\nFetching {len(PAGES_TO_FETCH)} pages...")

    with tqdm(total=len(PAGES_TO_FETCH), desc="Fetching", unit=" pages") as pbar:
        for i in range(0, len(PAGES_TO_FETCH), batch_size):
            batch_titles = PAGES_TO_FETCH[i : i + batch_size]
            batch_data = fetch_pages_batch(session, batch_titles)

            for page_data in batch_data:
                # Save individual JSON file
                filename = sanitize_filename(page_data["title"]) + ".json"
                filepath = pages_dir / filename
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump(page_data, f, ensure_ascii=False, indent=2)

                all_pages.append(page_data)

            pbar.update(len(batch_titles))

    # Save combined JSONL file
    jsonl_path = output_dir / "stellaris_4.2_pages.jsonl"
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for page in all_pages:
            f.write(json.dumps(page, ensure_ascii=False) + "\n")

    print(f"\nFetched {len(all_pages)} pages successfully!")
    print(f"Individual JSON files: {pages_dir}")
    print(f"Combined JSONL: {jsonl_path}")

    # Print summary of timestamps
    print("\nPage timestamps (showing wiki is on 4.2.x):")
    for page in sorted(all_pages, key=lambda x: x["timestamp"], reverse=True)[:5]:
        print(f"  {page['title']}: {page['timestamp']}")


if __name__ == "__main__":
    main()
