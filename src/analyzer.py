#!/usr/bin/env python3
"""
Analyze ALL pages on the Stellaris wiki to distinguish real content pages
from redirects, then cross-reference with the pages we already fetch.

Produces an interactive HTML report (default) or markdown report.

Usage:
    python stellariswiki.py analyze                  # HTML report (default)
    python stellariswiki.py analyze --format md      # Markdown report
    python stellariswiki.py analyze --workers 8      # More parallel workers
"""

import argparse
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote

import cloudscraper
from tqdm import tqdm

from src import PROJECT_ROOT, CONFIG_PATH, OUTPUT_DIR
from src.config import cfg
from src.fetcher import (
    COMPOSITE_PAGES,
    fetch_page_html,
    create_session as fp_create_session,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize_title(title: str) -> str:
    """Normalize a page title for comparison (underscores -> spaces)."""
    return title.replace("_", " ").strip()


def create_session():
    """Create a cloudscraper session."""
    session = cloudscraper.create_scraper(
        browser={"browser": "chrome", "platform": "linux", "desktop": True}
    )
    session.headers.update({
        "User-Agent": "StellarisWikiAnalyzer/1.0 (Educational/Research purposes)"
    })
    return session


def api_get(session, params, max_retries=None):
    """Make an API GET request with retries and exponential backoff."""
    if max_retries is None:
        max_retries = cfg.defaults.max_retries
    params["format"] = "json"
    for attempt in range(max_retries):
        try:
            resp = session.get(cfg.wiki.api_url, params=params, timeout=30)
            resp.raise_for_status()
            ct = resp.headers.get("Content-Type", "")
            if "application/json" not in ct:
                if attempt < max_retries - 1:
                    wait = 2.0 * (2 ** attempt)
                    time.sleep(wait)
                    continue
                return None
            return resp.json()
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 2.0 * (2 ** attempt)
                time.sleep(wait)
            else:
                print(f"  Failed after {max_retries} attempts: {e}")
                return None
    return None


def page_url(title, fragment=""):
    """Build a URL for a wiki page, optionally with a section anchor."""
    url = f"https://stellaris.paradoxwikis.com/{quote(title.replace(' ', '_'))}"
    if fragment:
        url += f"#{quote(fragment.replace(' ', '_'))}"
    return url


def sanitize_filename(title: str) -> str:
    """Convert page title to safe filename (mirrors fetch_and_parse.sanitize_filename)."""
    safe = re.sub(r'[<>:"/\\|?*]', "_", title)
    safe = safe.replace(" ", "_")
    return safe[:200] if len(safe) > 200 else safe


# ---------------------------------------------------------------------------
# Data Gathering
# ---------------------------------------------------------------------------

def fetch_all_pages(session, filter_redir="nonredirects"):
    """Fetch all page titles using allpages with pagination (sequential)."""
    pages = []
    params = {
        "action": "query",
        "list": "allpages",
        "apfilterredir": filter_redir,
        "aplimit": "500",
        "apnamespace": "0",
    }
    label = "content" if filter_redir == "nonredirects" else "redirect"
    print(f"Fetching {label} pages from wiki...")

    while True:
        time.sleep(cfg.defaults.request_delay)
        data = api_get(session, dict(params))
        if data is None:
            print("  ERROR: failed to fetch page list, aborting.")
            break
        batch = data.get("query", {}).get("allpages", [])
        pages.extend(batch)
        cont = data.get("continue")
        if cont and "apcontinue" in cont:
            params["apcontinue"] = cont["apcontinue"]
        else:
            break

    print(f"  Total {label} pages: {len(pages)}")
    return pages


def _resolve_redirect_batch(batch: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    """Worker: resolve one batch of up to 50 redirect titles.
    Returns (targets, fragments) where fragments maps source->section anchor."""
    session = create_session()
    params = {
        "action": "query",
        "titles": "|".join(batch),
        "redirects": "",
    }
    data = api_get(session, params)
    targets = {}
    fragments = {}
    if data is None:
        for title in batch:
            targets[title] = "(unresolved)"
        return targets, fragments

    for r in data.get("query", {}).get("redirects", []):
        targets[r["from"]] = r["to"]
        frag = r.get("tofragment", "")
        if frag:
            fragments[r["from"]] = frag
    for title in batch:
        if title not in targets:
            targets[title] = "(unresolved)"
    return targets, fragments


def resolve_redirects_parallel(redirect_titles: list[str], workers: int = 4) -> tuple[dict[str, str], dict[str, str]]:
    """Resolve redirect targets in parallel batches of 50.
    Returns (redirect_map, redirect_fragments)."""
    batches = [redirect_titles[i:i+50] for i in range(0, len(redirect_titles), 50)]
    redirect_map = {}
    redirect_fragments = {}

    print(f"Resolving {len(redirect_titles)} redirects in {len(batches)} batches ({workers} workers)...")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_resolve_redirect_batch, b): b for b in batches}
        for future in tqdm(as_completed(futures), total=len(batches),
                           desc="Resolving redirects", unit=" batch"):
            targets, frags = future.result()
            redirect_map.update(targets)
            redirect_fragments.update(frags)

    return redirect_map, redirect_fragments


def resolve_redirect_chains(redirect_map, redirect_fragments, content_pages_set):
    """Follow redirect chains to find the final target and fragment.
    Returns (resolved_map, resolved_fragments)."""
    resolved = {}
    resolved_frags = {}
    for source, target in redirect_map.items():
        chain = [source]
        current = target
        # Track the last fragment seen in the chain
        last_frag = redirect_fragments.get(source, "")
        max_depth = 10
        while current in redirect_map and current not in content_pages_set and max_depth > 0:
            if current in chain:
                current = f"{current} (circular)"
                break
            chain.append(current)
            if current in redirect_fragments:
                last_frag = redirect_fragments[current]
            current = redirect_map[current]
            max_depth -= 1
        resolved[source] = current
        if last_frag:
            resolved_frags[source] = last_frag
    return resolved, resolved_frags


def resolve_composite_subpages(session):
    """For each composite page, fetch HTML and extract sub-page titles."""
    composite_subpages = {}
    for title, extract_fn in COMPOSITE_PAGES.items():
        print(f"  Fetching composite page '{title}'...")
        time.sleep(cfg.defaults.request_delay)
        data = fetch_page_html(session, title)
        if not data or not data.get("html"):
            composite_subpages[title] = []
            continue
        categories = extract_fn(data["html"])
        subpages = []
        for _, page_titles in categories:
            for pt in page_titles:
                if pt not in subpages:
                    subpages.append(pt)
        # Merge extra_subpages from config
        page_config = cfg.composite_pages.get(title)
        if page_config and page_config.extra_subpages:
            for pt in page_config.extra_subpages:
                if pt not in subpages:
                    subpages.append(pt)
        composite_subpages[title] = subpages
        print(f"    Found {len(subpages)} sub-pages for '{title}'")
    return composite_subpages


def _fetch_categories_batch(batch: list[str]) -> dict[str, list[str]]:
    """Worker: fetch categories for one batch of up to 50 pages."""
    session = create_session()
    params = {
        "action": "query",
        "titles": "|".join(batch),
        "prop": "categories",
        "cllimit": "max",
        "format": "json",
    }
    partial: dict[str, list[str]] = {}
    # Handle continuation — cllimit="max" returns up to 500 results per
    # response; if there are more we need to follow the "continue" token.
    while True:
        data = api_get(session, params)
        if data is None:
            break
        for page_info in data.get("query", {}).get("pages", {}).values():
            title = page_info.get("title", "")
            cats = [c.get("title", "").replace("Category:", "")
                    for c in page_info.get("categories", [])]
            if title in partial:
                partial[title].extend(cats)
            else:
                partial[title] = cats
        if "continue" in data:
            params.update(data["continue"])
        else:
            break
    return partial


def fetch_categories_parallel(page_titles, workers: int = 4) -> dict[str, list[str]]:
    """Fetch categories for pages in parallel batches of 50."""
    titles_list = list(page_titles)
    batches = [titles_list[i:i+50] for i in range(0, len(titles_list), 50)]
    categories = {}

    print(f"Fetching categories for {len(titles_list)} pages in {len(batches)} batches ({workers} workers)...")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_fetch_categories_batch, b): b for b in batches}
        for future in tqdm(as_completed(futures), total=len(batches),
                           desc="Fetching categories", unit=" batch"):
            categories.update(future.result())

    return categories


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

VERSION_PATTERN = re.compile(r"^(\d+\.\d+(\.\d+)*([a-z])?)$", re.IGNORECASE)
PATCH_PATTERN = re.compile(r"^(Patch\s+\d|Dev diary|Developer diary)", re.IGNORECASE)


def classify_page(title: str, wiki_categories: list[str]) -> str:
    """Classify a page into: 'mod', 'disambiguation', 'patch', 'dlc', 'modding', or 'game_content'."""
    title_lower = title.lower()
    wiki_cats_set = set(wiki_categories)

    # 1. Mod: title prefix
    for prefix in cfg.classification.mod_prefixes:
        if title_lower.startswith(prefix.lower()):
            return "mod"
    # 2. Mod: wiki category
    if wiki_cats_set & cfg.classification.mod_categories:
        return "mod"

    # 3. Disambiguation
    if wiki_cats_set & cfg.classification.disambiguation_categories:
        return "disambiguation"

    # 4. Patch/version
    if VERSION_PATTERN.match(title.strip()):
        return "patch"
    if PATCH_PATTERN.match(title.strip()):
        return "patch"
    if "Patches" in wiki_cats_set:
        return "patch"

    # 5. DLC
    if title_lower.strip() in cfg.classification.dlc_titles:
        return "dlc"
    if "DLC" in wiki_cats_set:
        return "dlc"

    # 6. Modding
    if "modding" in title_lower or "moddable" in title_lower:
        return "modding"
    if "Modding" in wiki_cats_set:
        return "modding"

    return "game_content"


def get_content_categories(wiki_categories: list[str]) -> list[str]:
    """Filter out version numbers, wiki maintenance, and irrelevant categories."""
    result = []
    for c in wiki_categories:
        cs = c.strip()
        if not cs:
            continue
        if VERSION_PATTERN.match(cs):
            continue
        if cs in cfg.classification.wiki_maintenance_categories:
            continue
        if any(cs.startswith(pfx) for pfx in cfg.classification.wiki_maintenance_prefixes):
            continue
        result.append(cs)
    return result


def get_display_categories(wiki_categories: list[str]) -> list[str]:
    """Return all categories for display (no filtering)."""
    return [c.strip() for c in wiki_categories if c.strip()]


# ---------------------------------------------------------------------------
# Dynamic file detection
# ---------------------------------------------------------------------------

def scan_existing_files(pages_dir: Path) -> set[str]:
    """Scan output/pages/ for existing .md files.
    Returns set of normalized page titles that have files on disk."""
    existing = set()
    if not pages_dir.is_dir():
        return existing
    for md_file in pages_dir.glob("*.md"):
        existing.add(md_file.stem.replace("_", " "))
    return existing


# ---------------------------------------------------------------------------
# Data Preparation (shared by both report generators)
# ---------------------------------------------------------------------------

def prepare_report_data(
    content_pages, redirect_pages, redirect_map_resolved, redirect_fragments_resolved,
    fetched_titles, composite_subpages, categories_map, existing_files,
) -> dict:
    """Prepare all computed data needed by report generators."""
    total_pages = len(content_pages) + len(redirect_pages)
    num_redirects = len(redirect_pages)
    num_content = len(content_pages)
    redirect_pct = (num_redirects / total_pages * 100) if total_pages else 0

    # Build full fetched set (normalized)
    all_fetched = set(normalize_title(t) for t in fetched_titles)
    for subs in composite_subpages.values():
        for s in subs:
            all_fetched.add(normalize_title(s))

    content_titles_set = {p["title"] for p in content_pages}

    # Fetched pages info with file-exists status (include ALL configured pages)
    fetched_pages_info = []
    for t in sorted(all_fetched):
        source = "PAGES_TO_FETCH"
        for parent, subs in composite_subpages.items():
            if normalize_title(t) in {normalize_title(s) for s in subs}:
                if normalize_title(t) not in {normalize_title(x) for x in fetched_titles}:
                    source = f"Sub-page of {parent}"
                break
        # Look up categories (try both space and underscore variants)
        cats = categories_map.get(t, []) or categories_map.get(t.replace(" ", "_"), [])
        fetched_pages_info.append({
            "title": t,
            "source": source,
            "file_exists": normalize_title(t) in existing_files,
            "url": page_url(t),
            "categories": get_display_categories(cats),
        })

    not_fetched = {t for t in content_titles_set if normalize_title(t) not in all_fetched}

    # Classify
    classified = {"game_content": [], "mod": [], "dlc": [], "patch": [],
                  "modding": [], "disambiguation": []}
    for title in sorted(not_fetched):
        wiki_cats = categories_map.get(title, [])
        classified[classify_page(title, wiki_cats)].append(title)

    # Group game content by wiki category (each page in ONE primary category only)
    game_by_category = {}
    game_uncategorized = []
    for title in classified["game_content"]:
        content_cats = get_content_categories(categories_map.get(title, []))
        if not content_cats:
            # Fall back: skip versions + prefix-matched maintenance, then
            # also skip known maintenance categories if something remains.
            fallback = []
            for c in get_display_categories(categories_map.get(title, [])):
                if VERSION_PATTERN.match(c):
                    continue
                if any(c.startswith(pfx) for pfx in cfg.classification.wiki_maintenance_prefixes):
                    continue
                fallback.append(c)
            # Prefer non-maintenance categories in fallback
            non_maint = [c for c in fallback
                         if c not in cfg.classification.wiki_maintenance_categories]
            content_cats = non_maint if non_maint else fallback
        if content_cats:
            # Assign to first meaningful category only to avoid duplication
            game_by_category.setdefault(content_cats[0], []).append(title)
        else:
            game_uncategorized.append(title)

    sorted_game_cats = sorted(game_by_category.items(), key=lambda x: -len(x[1]))

    # Relevant redirects (include section fragment)
    relevant_redirects = sorted([
        (src, tgt, redirect_fragments_resolved.get(src, ""))
        for src, tgt in redirect_map_resolved.items()
        if normalize_title(tgt) in all_fetched
    ])

    # Group mods by prefix or wiki category
    mod_groups = {}
    for t in classified["mod"]:
        matched = False
        for mp in cfg.classification.mod_prefixes:
            if t.lower().startswith(mp.lower()):
                mod_groups.setdefault(mp, []).append(t)
                matched = True
                break
        if not matched:
            # Try grouping by mod-specific wiki category
            page_cats = set(categories_map.get(t, []))
            mod_cat_match = page_cats & cfg.classification.mod_categories
            mod_cat_match.discard("Mods")  # Too generic for grouping
            if mod_cat_match:
                group_name = sorted(mod_cat_match)[0]
                mod_groups.setdefault(group_name, []).append(t)
            else:
                mod_groups.setdefault("Other mods", []).append(t)

    # Collect all unique categories across ALL pages (keep everything except versions)
    all_categories = set()
    for cats in categories_map.values():
        all_categories.update(get_display_categories(cats))
    for p in fetched_pages_info:
        all_categories.update(p["categories"])
    # Track whether any page has no categories
    has_uncategorized = any(not p["categories"] for p in fetched_pages_info)
    if not has_uncategorized:
        for cats in categories_map.values():
            if not get_display_categories(cats):
                has_uncategorized = True
                break

    # Compute main vs sub-page breakdown
    main_pages = [p for p in fetched_pages_info if p["source"] == "PAGES_TO_FETCH"]
    sub_pages = [p for p in fetched_pages_info if p["source"] != "PAGES_TO_FETCH"]
    # Only main pages are expected to have individual files on disk;
    # sub-pages are embedded in composite parent files.
    main_missing = [p for p in main_pages if not p["file_exists"]]

    # Fetched breakdown for pie chart
    n_composite_parents = len(composite_subpages)
    fetched_breakdown = [
        {"label": "Main pages", "value": len(main_pages) - n_composite_parents},
        {"label": "Composite parents", "value": n_composite_parents},
    ] + [
        {"label": f"{parent} sub-pages", "value": len(subs)}
        for parent, subs in sorted(composite_subpages.items())
    ]

    return {
        "generated_at": time.strftime('%Y-%m-%d %H:%M:%S'),
        "total_pages": total_pages,
        "num_redirects": num_redirects,
        "num_content": num_content,
        "redirect_pct": redirect_pct,
        "all_fetched": all_fetched,
        "fetched_pages_info": fetched_pages_info,
        "not_fetched": not_fetched,
        "classified": classified,
        "game_by_category": sorted_game_cats,
        "game_uncategorized": game_uncategorized,
        "relevant_redirects": relevant_redirects,
        "mod_groups": mod_groups,
        "categories_map": categories_map,
        "composite_subpages": composite_subpages,
        "files_on_disk": len(existing_files),
        "n_main_pages": len(main_pages),
        "n_sub_pages": len(sub_pages),
        "main_missing": len(main_missing),
        "fetched_breakdown": fetched_breakdown,
        "all_categories": sorted(all_categories),
        "has_uncategorized": has_uncategorized,
    }


# ---------------------------------------------------------------------------
# Markdown Report Generator
# ---------------------------------------------------------------------------

def generate_markdown_report(data: dict, output_path: Path) -> str:
    """Generate the markdown analysis report from prepared data."""
    lines = []
    w = lines.append
    d = data

    w("# Stellaris Wiki Page Analysis\n")
    w(f"_Generated on {d['generated_at']}_\n")

    w("## Summary\n")
    w(f"- **Total wiki pages (namespace 0):** {d['total_pages']:,}")
    w(f"- **Redirect pages:** {d['num_redirects']:,} ({d['redirect_pct']:.1f}%)")
    w(f"- **Unique content pages:** {d['num_content']:,}")
    w(f"- **Currently fetched:** {len(d['all_fetched'])} pages ({d['n_main_pages']} main + {d['n_sub_pages']} sub-pages)")
    w(f"- **Files on disk:** {d['files_on_disk']}")
    if d['main_missing'] > 0:
        w(f"- **Missing files:** {d['main_missing']} main pages without a file on disk")
    w(f"- **Content pages NOT fetched:** {len(d['not_fetched']):,}")
    w("")

    w("### Fetched breakdown\n")
    w("| Component | Count |")
    w("|-----------|-------|")
    for seg in d["fetched_breakdown"]:
        w(f"| {seg['label']} | {seg['value']} |")
    w("")

    w("### Not-fetched breakdown\n")
    w("| Classification | Count |")
    w("|---------------|-------|")
    for key, label in [("game_content", "Game content"), ("dlc", "DLC"),
                        ("patch", "Patch notes"), ("disambiguation", "Disambiguation"),
                        ("modding", "Modding"), ("mod", "Mods")]:
        w(f"| {label} | {len(d['classified'][key])} |")
    w("")

    # Fetched pages
    w(f"## Fetched Pages ({len(d['fetched_pages_info'])})\n")
    w("| # | Page | Source | File | Categories |")
    w("|---|------|--------|------|------------|")
    for i, p in enumerate(d["fetched_pages_info"], 1):
        status = "yes" if p["file_exists"] else "**MISSING**"
        file_md = f" ([md](pages/{sanitize_filename(p['title'])}.md))" if p["file_exists"] else ""
        cats = ", ".join(p["categories"]) if p["categories"] else "_(none)_"
        w(f"| {i} | [{p['title']}]({p['url']}){file_md} | {p['source']} | {status} | {cats} |")
    w("")

    # Game content
    w(f"## Game Content — Not Fetched ({len(d['classified']['game_content'])} pages)\n")
    for cat_name, titles in d["game_by_category"]:
        w(f"### {cat_name} ({len(titles)} pages)\n")
        w("| Page | Wiki categories | URL |")
        w("|------|----------------|-----|")
        for t in sorted(titles):
            cats = ", ".join(d["categories_map"].get(t, [])) or "_(none)_"
            w(f"| {t} | {cats} | [link]({page_url(t)}) |")
        w("")

    if d["game_uncategorized"]:
        w(f"### Uncategorized ({len(d['game_uncategorized'])} pages)\n")
        w("| Page | URL |")
        w("|------|-----|")
        for t in sorted(d["game_uncategorized"]):
            w(f"| {t} | [link]({page_url(t)}) |")
        w("")

    # DLC
    w(f"## DLC Pages ({len(d['classified']['dlc'])})\n")
    w("| Page | Categories |")
    w("|------|------------|")
    for t in sorted(d["classified"]["dlc"]):
        cats = ", ".join(get_display_categories(d["categories_map"].get(t, []))) or "_(none)_"
        w(f"| [{t}]({page_url(t)}) | {cats} |")
    w("")

    # Patches
    w(f"## Patch Notes ({len(d['classified']['patch'])})\n")
    if d["classified"]["patch"]:
        w(", ".join(sorted(d["classified"]["patch"])))
    w("")

    # Disambiguation
    if d["classified"]["disambiguation"]:
        w(f"## Disambiguation Pages ({len(d['classified']['disambiguation'])})\n")
        w(", ".join(sorted(d["classified"]["disambiguation"])))
        w("")

    # Modding
    w(f"## Modding ({len(d['classified']['modding'])})\n")
    w("| Page | Categories |")
    w("|------|------------|")
    for t in sorted(d["classified"]["modding"]):
        cats = ", ".join(get_display_categories(d["categories_map"].get(t, []))) or "_(none)_"
        w(f"| [{t}]({page_url(t)}) | {cats} |")
    w("")

    # Mods (individual pages)
    w(f"## Total-Conversion Mods ({len(d['classified']['mod'])})\n")
    for mod_name, pages in sorted(d["mod_groups"].items(), key=lambda x: -len(x[1])):
        w(f"### {mod_name} ({len(pages)} pages)\n")
        w("| Page | Categories |")
        w("|------|------------|")
        for t in sorted(pages):
            cats = ", ".join(get_display_categories(d["categories_map"].get(t, []))) or "_(none)_"
            w(f"| [{t}]({page_url(t)}) | {cats} |")
        w("")

    # Redirects
    w(f"## Redirects to Fetched Pages ({len(d['relevant_redirects'])})\n")
    if d["relevant_redirects"]:
        w("| Redirect | Target | Categories |")
        w("|----------|--------|------------|")
        for src, tgt, frag in d["relevant_redirects"]:
            target_display = f"{tgt} > {frag}" if frag else tgt
            cats = ", ".join(get_display_categories(d["categories_map"].get(tgt, []))) or "_(none)_"
            w(f"| {src} | [{target_display}]({page_url(tgt, frag)}) | {cats} |")
    w("")

    report = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report


# ---------------------------------------------------------------------------
# HTML Report Generator
# ---------------------------------------------------------------------------


_STELLARIS_FAVICON_B64 = "AAABAAEAEBAAAAAAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAAD///8B////AUCe/wlAnv8hQJ7/Ef///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BQJ7/BUCe/zdAnv91QJ7/ezeH2mcAAABXAAAAiwAAALMAAACzAAAAiwAAAFcAAAAX////Af///wH///8B////AUCe/w9Anv+TQJ7/gQ0gM0EUFhTJQDcU23JgH+2agSX7tZcp+7ycJ+1/ahvbHxoHxwAAADf///8B////Af///wFAnv8FSqr/bVCl37EiJyPRTUEe62tZIP9zXh//fWgh/5R6Jf+8nSr/5b4w/7eZJ+s6MA7NAAAAN////wH///8B////ASllojdHldHzUIGh91xYOP9BNxf/XHcy/0I/Fv9VSxj/gmsg/7CRJ//guzD/u5on6xsWB8cAAAAX////Af///wEAAABXQ2mD612u5P9Ofp3/NTIf/z09Gf9WcDD/Xn01/09EGP+DbCD/pYom/9OvLf9zYBnbAAAAV////wH///8BAAAAi4F6VO9mlrP/WK3k/z9qgv9CTyb/RVMl/1NtLf8uKQ//RDkT/3VgHv+qjCf/p4sl7QAAAIv///8B////AQAAALO8rnz7n5Vl/02FqP9Xr+j/RYGj/0JVM/86Phv/Jx8P/0xbKP9NQxv/dWEf/62PKPsAAACz////Af///wEAAACz5tqv+76sdP9mZUz/SIOr/1i17/9MndH/P19l/0RRL/9SZjT/U1Ep/2NTH/91YSX7AAAAs////wH///8BAAAAi7mwje3czpn/koFP/1FMNv9KjK//YsD1/5jW+P9/tNH/VImm/y9AR/8YFgv/LicP9QAAAIv///8B////AQAAAFd6dV7b5tuv/83Ai/+EdEP/UVE8/1yYtP/D6v3/0+/+/1d3jf9OWWP/rKyr/w0LBPcAAABX////Af///wEAAAAXExgMx1R2M+twnUT/hJtN/4V0Pf9waUL/p9Tt/3SEjf9cZGr/rKup/09NR/0JBwTfAAAAF////wH///8B////AQAAADckLhfNU3Yy63GeRf+qomD/l4NC/0FRT/9SXGL/4+Da/9XV1f+sq6n/AAAAzQAAAAP///8B////Af///wH///8BAAAANx0bE8d2cFbbtKyG7bCeZPsgHRD/3NnU/01LRvnZ19P/rayr/09PT9MAAABx////Af///wH///8B////Af///wEAAAAXAAAAVwAAAIsAAACzAAAA1QAAAOMAAAChAAAAxU9PT9PEwbz/AAAAvwAAAAP///8B////Af///wH///8B////Af///wH///8B////Af///wEAAAAD////AQAAAAMAAABxAAAAvwAAAHH///8BAAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//w=="

_NOTEBOOKLM_SVG = '<svg style="width:14px;height:14px;vertical-align:middle" viewBox="0 1.14 174.56 127.99"><path fill="currentColor" d="M87.27,1.14C39.07,1.14,0,39.88,0,87.69v41.44h16.09v-4.13c0-19.39,15.84-35.11,35.39-35.11s35.39,15.72,35.39,35.11v4.13h16.09v-4.13c0-28.2-23.05-51.05-51.48-51.05-11.07,0-21.32,3.46-29.72,9.37,8.79-17.32,26.88-29.21,47.77-29.21,29.51,0,53.44,23.74,53.44,53v22.02h16.09v-22.02c0-38.08-31.13-68.96-69.53-68.96-17.27,0-33.06,6.24-45.22,16.58,11.94-22.39,35.65-37.64,62.97-37.64,39.32,0,71.19,31.61,71.19,70.6v41.44h16.09v-41.44C174.55,39.88,135.48,1.14,87.27,1.14Z"/></svg>'


def _strip_markdown(text: str) -> str:
    """Strip markdown formatting for search indexing."""
    text = re.sub(r"\|[-:]+\|", " ", text)    # table separator rows
    text = re.sub(r"[|*#>_`\[\]]", " ", text)  # formatting chars
    text = re.sub(r"\(https?://[^\)]+\)", " ", text)  # markdown link URLs
    text = re.sub(r"\s+", " ", text)            # collapse whitespace
    return text.strip()


def _build_search_index(pages_dir: Path) -> list[list[str]]:
    """Build section-level search index from fetched markdown files.

    Returns list of [page_title, section_heading, searchable_text] tuples.
    Text is capped at 500 chars per section for size control.
    """
    index = []
    for md_file in sorted(pages_dir.glob("*.md")):
        title = md_file.stem.replace("_", " ")
        content = md_file.read_text(encoding="utf-8")
        # Strip YAML frontmatter
        content = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)
        # Split into sections by headings
        current_heading = title
        section_lines: list[str] = []
        for line in content.split("\n"):
            m = re.match(r"^#{1,4}\s+(.+)", line)
            if m:
                # Flush previous section
                if section_lines:
                    text = _strip_markdown(" ".join(section_lines))
                    if len(text) > 30:
                        index.append([title, current_heading, text[:500]])
                current_heading = m.group(1).strip()
                section_lines = []
            elif line.strip():
                section_lines.append(line.strip())
        # Flush last section
        if section_lines:
            text = _strip_markdown(" ".join(section_lines))
            if len(text) > 30:
                index.append([title, current_heading, text[:500]])
    return index




def generate_html_report(data: dict, output_path: Path) -> str:
    """Generate a self-contained interactive HTML analysis report using Jinja2 templates."""
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    from urllib.parse import quote

    # Build search index from fetched markdown files
    pages_dir = cfg.output_path / "pages"
    data["search_index"] = _build_search_index(pages_dir) if pages_dir.exists() else []

    # Add data needed by templates
    data["pages_to_fetch"] = list(cfg.pages_to_fetch)
    config_path = CONFIG_PATH
    data["config_yaml"] = config_path.read_text(encoding="utf-8") if config_path.exists() else ""

    # Pre-compute pie chart data for dashboard template
    cl = data["classified"]
    n_fetched = len(data["fetched_pages_info"])
    n_redir_fetched = len(data["relevant_redirects"])
    n_not_fetched = len(data["not_fetched"])
    n_redir_other = data["num_redirects"] - n_redir_fetched

    data["wiki_structure_data"] = [
        {"label": "Main pages fetched", "value": data["n_main_pages"], "color": "#22c55e"},
        {"label": "Sub-pages fetched", "value": data["n_sub_pages"], "color": "#14b8a6"},
        {"label": "Redirects to fetched", "value": n_redir_fetched, "color": "#3b82f6"},
        {"label": "Not fetched", "value": n_not_fetched, "color": "#f97316"},
        {"label": "Other redirects", "value": n_redir_other, "color": "#64748b"},
    ]

    data["not_fetched_data"] = [
        {"label": "Game Content", "value": len(cl["game_content"]), "color": "#3b82f6"},
        {"label": "DLC", "value": len(cl["dlc"]), "color": "#f97316"},
        {"label": "Patches", "value": len(cl["patch"]), "color": "#14b8a6"},
        {"label": "Disambiguation", "value": len(cl["disambiguation"]), "color": "#eab308"},
        {"label": "Modding", "value": len(cl["modding"]), "color": "#a855f7"},
        {"label": "Total-conversion Mods", "value": len(cl["mod"]), "color": "#ef4444"},
    ]

    fb_colors = ["#22c55e", "#0ea5e9", "#f97316", "#a855f7", "#ef4444", "#eab308", "#14b8a6"]
    data["fetched_breakdown_data"] = [
        {"label": seg["label"], "value": seg["value"], "color": fb_colors[i % len(fb_colors)]}
        for i, seg in enumerate(data["fetched_breakdown"])
    ]

    # Sort mod_groups by descending page count for template
    data["mod_groups"] = dict(
        sorted(data["mod_groups"].items(), key=lambda x: -len(x[1]))
    )

    # Template constants
    data["favicon_b64"] = _STELLARIS_FAVICON_B64
    data["notebooklm_svg"] = _NOTEBOOKLM_SVG

    # Set up Jinja2
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(["html"]),
    )

    # Custom filters
    def _page_url_filter(title):
        return f"https://stellaris.paradoxwikis.com/{quote(title.replace(' ', '_'))}"

    def _page_url_with_fragment(title, fragment=""):
        url = f"https://stellaris.paradoxwikis.com/{quote(title.replace(' ', '_'))}"
        if fragment:
            url += f"#{quote(fragment.replace(' ', '_'))}"
        return url

    env.filters["page_url"] = _page_url_filter
    env.filters["page_url_with_fragment"] = _page_url_with_fragment
    env.filters["sanitize_filename"] = sanitize_filename
    env.filters["display_categories"] = get_display_categories

    template = env.get_template("report.html")
    html_str = template.render(**data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_str, encoding="utf-8")
    return html_str


# ---------------------------------------------------------------------------
# All Pages Markdown Generator
# ---------------------------------------------------------------------------

def generate_all_pages_md(content_pages, redirect_pages, all_fetched, composite_subpages, output_path: Path):
    """Generate all_pages.md listing every wiki page with fetch status."""
    # Combine all page titles (content + redirects)
    all_titles = sorted(
        {p["title"] for p in content_pages} | {p["title"] for p in redirect_pages}
    )
    all_fetched_normalized = {normalize_title(t) for t in all_fetched}

    # Count sub-pages
    n_main = len(cfg.pages_to_fetch)
    n_sub = len(all_fetched_normalized) - n_main
    n_fetched = len(all_fetched_normalized)
    total = len(all_titles)

    lines = []
    w = lines.append
    w("# All Stellaris Wiki Pages\n")
    w(f"Total pages in wiki: {total}")
    w(f"Currently fetched: {n_fetched} pages ({n_main} main + {n_sub} composite sub-pages)")
    w(f"Not fetched: {total - n_fetched} pages\n")
    w("## All Pages\n")
    w("| # | Page | Fetched | URL |")
    w("|---|------|---------|-----|")

    for i, title in enumerate(all_titles, 1):
        fetched = "✓" if normalize_title(title) in all_fetched_normalized else ""
        url = page_url(title)
        w(f"| {i} | {title} | {fetched} | {url} |")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {output_path} ({len(all_titles)} pages listed)")


# ---------------------------------------------------------------------------
# CLI & Main
# ---------------------------------------------------------------------------

def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser(
            description="Analyze Stellaris wiki pages and generate an interactive report."
        )
        parser.add_argument(
            "--format", choices=["html", "md"], default="html",
            help="Output format: html (interactive, default) or md (markdown)"
        )
        parser.add_argument(
            "--workers", type=int, default=None,
            help=f"Number of parallel workers for API calls (default: {cfg.defaults.workers})"
        )
        parser.add_argument(
            "--output", type=str, default=None,
            help=f"Output file path (default: {cfg.defaults.output_dir}/wiki_analysis.{{html|md}})"
        )
        parser.add_argument(
            "--no-all-pages", action="store_true",
            help="Skip generating all_pages.md"
        )
        args = parser.parse_args()

    # Apply defaults from config for unset values
    if not hasattr(args, 'format') or args.format is None:
        args.format = "html"
    args.workers = args.workers if args.workers is not None else cfg.defaults.workers
    if not hasattr(args, 'no_all_pages'):
        args.no_all_pages = False

    session = create_session()
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    ext = "html" if args.format == "html" else "md"
    output_path = Path(args.output) if args.output else output_dir / f"wiki_analysis.{ext}"

    # 1-2. Fetch all content + redirect pages (sequential, paginated)
    content_pages = fetch_all_pages(session, "nonredirects")
    redirect_pages = fetch_all_pages(session, "redirects")

    # 3. Resolve redirects (PARALLEL)
    redirect_titles = [p["title"] for p in redirect_pages]
    redirect_map, redirect_fragments = resolve_redirects_parallel(redirect_titles, workers=args.workers)
    content_titles_set = {p["title"] for p in content_pages}
    redirect_map_resolved, redirect_fragments_resolved = resolve_redirect_chains(
        redirect_map, redirect_fragments, content_titles_set
    )

    # 4. Composite sub-pages
    print("\nResolving composite page sub-pages...")
    composite_subpages = resolve_composite_subpages(fp_create_session())

    # 5. Build fetched set
    fetched_titles = set(normalize_title(t) for t in cfg.pages_to_fetch)

    # 6. Not-fetched pages
    all_fetched = set(fetched_titles)
    for subs in composite_subpages.values():
        for s in subs:
            all_fetched.add(normalize_title(s))
    not_fetched = {t for t in content_titles_set if normalize_title(t) not in all_fetched}

    # 7. Fetch categories for ALL content pages (PARALLEL)
    categories_map = fetch_categories_parallel(content_titles_set, workers=args.workers)

    # 8. Scan existing files
    pages_dir = OUTPUT_DIR / "pages"
    existing_files = scan_existing_files(pages_dir)
    print(f"Files on disk: {len(existing_files)}")

    # 9. Prepare report data
    print("\nPreparing report data...")
    data = prepare_report_data(
        content_pages, redirect_pages, redirect_map_resolved, redirect_fragments_resolved,
        fetched_titles, composite_subpages, categories_map, existing_files,
    )

    # 10. Generate report
    print(f"Generating {args.format.upper()} report...")
    if args.format == "html":
        generate_html_report(data, output_path)
    else:
        generate_markdown_report(data, output_path)

    size_kb = output_path.stat().st_size / 1024
    print(f"\nReport saved to: {output_path} ({size_kb:.1f} KB)")

    # 11. Generate all_pages.md (unless disabled)
    if cfg.defaults.generate_all_pages and not args.no_all_pages:
        all_pages_path = output_dir / "all_pages.md"
        generate_all_pages_md(
            content_pages, redirect_pages, data["all_fetched"],
            composite_subpages, all_pages_path,
        )

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Total wiki pages: {data['total_pages']:,}")
    print(f"  Content: {data['num_content']:,} | Redirects: {data['num_redirects']:,}")
    print(f"Fetched: {len(data['all_fetched'])} ({data['n_main_pages']} main + {data['n_sub_pages']} sub-pages)")
    print(f"Files on disk: {data['files_on_disk']}", end="")
    if data['main_missing'] > 0:
        print(f" | Missing: {data['main_missing']}", end="")
    print(f"\nNot fetched: {len(data['not_fetched']):,}")

    return output_path


if __name__ == "__main__":
    # Allow standalone execution: python src/analyzer.py
    import sys as _sys
    from pathlib import Path as _Path
    _root = str(_Path(__file__).resolve().parent.parent)
    if _root not in _sys.path:
        _sys.path.insert(0, _root)
    main()
