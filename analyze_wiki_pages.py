#!/usr/bin/env python3
"""
Analyze ALL pages on the Stellaris wiki to distinguish real content pages
from redirects, then cross-reference with the pages we already fetch.

Produces an interactive HTML report (default) or markdown report.

Usage:
    python analyze_wiki_pages.py                    # HTML report (default)
    python analyze_wiki_pages.py --format md        # Markdown report
    python analyze_wiki_pages.py --workers 8        # More parallel workers
"""

import argparse
import html as html_module
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote

import cloudscraper
from tqdm import tqdm

# ---------------------------------------------------------------------------
# Shared config + imports from fetch_and_parse.py
# ---------------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from config import cfg
from fetch_and_parse import (
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
        "cllimit": "50",
    }
    data = api_get(session, params)
    partial = {}
    if data is None:
        return partial
    for page_info in data.get("query", {}).get("pages", {}).values():
        title = page_info.get("title", "")
        cats = [c.get("title", "").replace("Category:", "")
                for c in page_info.get("categories", [])]
        partial[title] = cats
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
    """Classify a page: 'mod', 'dlc', 'patch', 'modding', or 'game_content'."""
    title_lower = title.lower()
    for prefix in cfg.classification.mod_prefixes:
        if title_lower.startswith(prefix.lower()):
            return "mod"
    if VERSION_PATTERN.match(title.strip()):
        return "patch"
    if PATCH_PATTERN.match(title.strip()):
        return "patch"
    if "Patches" in wiki_categories:
        return "patch"
    if title_lower.strip() in cfg.classification.dlc_titles:
        return "dlc"
    if "DLC" in wiki_categories:
        return "dlc"
    if "modding" in title_lower or "moddable" in title_lower:
        return "modding"
    if "Modding" in wiki_categories:
        return "modding"
    return "game_content"


def get_content_categories(wiki_categories: list[str]) -> list[str]:
    """Filter out version numbers and wiki maintenance tags from categories."""
    return [c.strip() for c in wiki_categories
            if not VERSION_PATTERN.match(c.strip())
            and c.strip() not in cfg.classification.wiki_maintenance_categories]


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
        fetched_pages_info.append({
            "title": t,
            "source": source,
            "file_exists": normalize_title(t) in existing_files,
            "url": page_url(t),
        })

    not_fetched = {t for t in content_titles_set if normalize_title(t) not in all_fetched}

    # Classify
    classified = {"game_content": [], "mod": [], "dlc": [], "patch": [], "modding": []}
    for title in sorted(not_fetched):
        wiki_cats = categories_map.get(title, [])
        classified[classify_page(title, wiki_cats)].append(title)

    # Group game content by wiki category (each page in ONE primary category only)
    game_by_category = {}
    game_uncategorized = []
    for title in classified["game_content"]:
        content_cats = get_content_categories(categories_map.get(title, []))
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

    # Group mods by prefix (case-insensitive)
    mod_groups = {}
    for t in classified["mod"]:
        matched = False
        for mp in cfg.classification.mod_prefixes:
            if t.lower().startswith(mp.lower()):
                mod_groups.setdefault(mp, []).append(t)
                matched = True
                break
        if not matched:
            mod_groups.setdefault("Other mods", []).append(t)

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
        "fetched_with_files": sum(1 for p in fetched_pages_info if p["file_exists"]),
        "fetched_without_files": sum(1 for p in fetched_pages_info if not p["file_exists"]),
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
    w(f"- **Currently fetched:** {len(d['all_fetched'])} pages")
    w(f"- **Files on disk:** {d['fetched_with_files']} present, {d['fetched_without_files']} missing")
    w(f"- **Content pages NOT fetched:** {len(d['not_fetched']):,}")
    w("")

    w("### Not-fetched breakdown\n")
    w("| Classification | Count |")
    w("|---------------|-------|")
    for key, label in [("game_content", "Game content"), ("dlc", "DLC"),
                        ("patch", "Patch notes"), ("modding", "Modding"), ("mod", "Mods")]:
        w(f"| {label} | {len(d['classified'][key])} |")
    w("")

    # Fetched pages
    w(f"## Fetched Pages ({len(d['fetched_pages_info'])})\n")
    w("| # | Page | Source | File |")
    w("|---|------|--------|------|")
    for i, p in enumerate(d["fetched_pages_info"], 1):
        status = "yes" if p["file_exists"] else "**MISSING**"
        w(f"| {i} | [{p['title']}]({p['url']}) | {p['source']} | {status} |")
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
    for t in sorted(d["classified"]["dlc"]):
        w(f"- [{t}]({page_url(t)})")
    w("")

    # Patches
    w(f"## Patch Notes ({len(d['classified']['patch'])})\n")
    if d["classified"]["patch"]:
        w(", ".join(sorted(d["classified"]["patch"])))
    w("")

    # Modding
    w(f"## Modding ({len(d['classified']['modding'])})\n")
    for t in sorted(d["classified"]["modding"]):
        w(f"- [{t}]({page_url(t)})")
    w("")

    # Mods (individual pages)
    w(f"## Total-Conversion Mods ({len(d['classified']['mod'])})\n")
    for mod_name, pages in sorted(d["mod_groups"].items(), key=lambda x: -len(x[1])):
        w(f"### {mod_name} ({len(pages)} pages)\n")
        for t in sorted(pages):
            w(f"- [{t}]({page_url(t)})")
        w("")

    # Redirects
    w(f"## Redirects to Fetched Pages ({len(d['relevant_redirects'])})\n")
    if d["relevant_redirects"]:
        w("| Redirect | Target |")
        w("|----------|--------|")
        for src, tgt, frag in d["relevant_redirects"]:
            target_display = f"{tgt} > {frag}" if frag else tgt
            w(f"| {src} | [{target_display}]({page_url(tgt, frag)}) |")
    w("")

    report = "\n".join(lines)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return report


# ---------------------------------------------------------------------------
# HTML Report Generator
# ---------------------------------------------------------------------------

def _esc(text):
    """HTML-escape a string."""
    return html_module.escape(str(text))


def _html_head(data):
    """Generate HTML head with embedded CSS."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Stellaris Wiki Analysis</title>
<style>
:root {{
    --bg: #f8fafc; --text: #1e293b; --border: #e2e8f0; --card-bg: #fff;
    --nav-bg: #1e293b; --nav-text: #f1f5f9; --link: #2563eb;
    --green: #22c55e; --red: #ef4444; --yellow: #eab308;
    --blue: #3b82f6; --purple: #8b5cf6; --orange: #f59e0b; --teal: #14b8a6;
}}
@media (prefers-color-scheme: dark) {{
    :root {{
        --bg: #0f172a; --text: #e2e8f0; --border: #334155; --card-bg: #1e293b;
        --link: #60a5fa;
    }}
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
       background: var(--bg); color: var(--text); line-height: 1.5; padding-top: 56px; }}
a {{ color: var(--link); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

.nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 100;
        background: var(--nav-bg); color: var(--nav-text); padding: 0 1rem;
        display: flex; align-items: center; height: 56px; gap: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,.15); }}
.nav-brand {{ font-weight: 700; font-size: 1.1rem; white-space: nowrap; }}
.nav-links {{ display: flex; gap: 0.25rem; flex-wrap: wrap; flex: 1; }}
.nav-links a {{ color: var(--nav-text); padding: 0.25rem 0.5rem; border-radius: 4px;
               font-size: 0.85rem; white-space: nowrap; }}
.nav-links a:hover {{ background: rgba(255,255,255,.15); text-decoration: none; }}
.nav-stats {{ font-size: 0.8rem; opacity: 0.8; white-space: nowrap; }}

.container {{ max-width: 1200px; margin: 0 auto; padding: 1.5rem; }}
.dashboard {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
              gap: 1rem; margin: 1rem 0; }}
.card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 8px;
         padding: 1rem; text-align: center; }}
.card .number {{ font-size: 2rem; font-weight: 700; }}
.card .label {{ font-size: 0.85rem; opacity: 0.7; margin-top: 0.25rem; }}
.card.green .number {{ color: var(--green); }}
.card.red .number {{ color: var(--red); }}
.card.blue .number {{ color: var(--blue); }}

.breakdown {{ display: flex; align-items: center; gap: 2rem; margin: 1.5rem 0;
              flex-wrap: wrap; }}
.pie-chart {{ width: 140px; height: 140px; border-radius: 50%; flex-shrink: 0; }}
.pie-legend {{ font-size: 0.9rem; }}
.pie-legend div {{ display: flex; align-items: center; gap: 0.5rem; margin: 0.25rem 0; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }}

.section {{ margin: 2rem 0; }}
.section-header {{ display: flex; align-items: center; gap: 0.5rem; cursor: pointer;
                   padding: 0.75rem 1rem; background: var(--card-bg); border: 1px solid var(--border);
                   border-radius: 8px; user-select: none; }}
.section-header:hover {{ background: var(--border); }}
.section-header h2, .section-header h3 {{ font-size: 1.1rem; }}
.chevron {{ display: inline-block; transition: transform 0.2s; font-size: 0.8rem; }}
.section-body {{ display: none; padding: 1rem 0; }}
.section-body.open {{ display: block; }}
.sub-section {{ margin: 0.75rem 0; }}
.sub-header {{ padding: 0.5rem 0.75rem; border-left: 3px solid var(--blue); cursor: pointer;
               display: flex; align-items: center; gap: 0.5rem; }}
.sub-header:hover {{ background: var(--border); }}
.sub-header h3 {{ font-size: 0.95rem; font-weight: 600; }}

.filter-input {{ width: 100%; padding: 0.5rem 0.75rem; border: 1px solid var(--border);
                 border-radius: 6px; font-size: 0.9rem; margin-bottom: 0.75rem;
                 background: var(--card-bg); color: var(--text); }}
table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
th {{ text-align: left; padding: 0.5rem; border-bottom: 2px solid var(--border);
     cursor: pointer; white-space: nowrap; user-select: none; }}
th:hover {{ background: var(--border); }}
th.sort-asc::after {{ content: " \\25B2"; font-size: 0.7rem; }}
th.sort-desc::after {{ content: " \\25BC"; font-size: 0.7rem; }}
td {{ padding: 0.4rem 0.5rem; border-bottom: 1px solid var(--border); }}
tr:hover {{ background: rgba(59,130,246,.05); }}
.status-ok {{ color: var(--green); font-weight: 700; text-align: center; }}
.status-missing {{ color: var(--red); font-weight: 700; text-align: center; }}
.tag {{ display: inline-block; padding: 0.1rem 0.4rem; border-radius: 4px; font-size: 0.75rem;
        background: var(--border); margin: 1px; white-space: nowrap; }}
.generated {{ text-align: center; padding: 2rem; opacity: 0.5; font-size: 0.85rem; }}
.count {{ font-size: 0.85rem; opacity: 0.7; font-weight: normal; }}
</style>
</head>
<body>'''


def _html_nav(data):
    """Generate sticky navigation bar."""
    d = data
    gc = len(d["classified"]["game_content"])
    dlc = len(d["classified"]["dlc"])
    patch = len(d["classified"]["patch"])
    modding = len(d["classified"]["modding"])
    mods = len(d["classified"]["mod"])
    redir = len(d["relevant_redirects"])
    fetched = len(d["fetched_pages_info"])
    return f'''
<nav class="nav">
    <div class="nav-brand">Stellaris Wiki Analysis</div>
    <div class="nav-links">
        <a href="#dashboard">Dashboard</a>
        <a href="#fetched">Fetched ({fetched})</a>
        <a href="#game-content">Game Content ({gc})</a>
        <a href="#dlc">DLC ({dlc})</a>
        <a href="#patches">Patches ({patch})</a>
        <a href="#modding">Modding ({modding})</a>
        <a href="#mods">Mods ({mods})</a>
        <a href="#redirects">Redirects ({redir})</a>
    </div>
    <div class="nav-stats">{d["total_pages"]:,} pages | {fetched} fetched</div>
</nav>
<div class="container">'''


def _html_dashboard(data):
    """Generate summary dashboard with stat cards and pie chart."""
    d = data
    cl = d["classified"]
    total_nf = len(d["not_fetched"])

    # Pie chart angles
    def pct_to_deg(n):
        return (n / total_nf * 360) if total_nf > 0 else 0

    gc_deg = pct_to_deg(len(cl["game_content"]))
    dlc_deg = gc_deg + pct_to_deg(len(cl["dlc"]))
    patch_deg = dlc_deg + pct_to_deg(len(cl["patch"]))
    modding_deg = patch_deg + pct_to_deg(len(cl["modding"]))

    return f'''
<section id="dashboard" class="section">
    <h2 style="margin-bottom:1rem;">Summary Dashboard</h2>
    <div class="dashboard">
        <div class="card"><div class="number">{d["total_pages"]:,}</div><div class="label">Total Wiki Pages</div></div>
        <div class="card"><div class="number">{d["num_content"]:,}</div><div class="label">Content Pages</div></div>
        <div class="card"><div class="number">{d["num_redirects"]:,}</div><div class="label">Redirects ({d["redirect_pct"]:.0f}%)</div></div>
        <div class="card green"><div class="number">{len(d["fetched_pages_info"])}</div><div class="label">Currently Fetched</div></div>
        <div class="card blue"><div class="number">{d["fetched_with_files"]}</div><div class="label">Files on Disk</div></div>
        <div class="card red"><div class="number">{d["fetched_without_files"]}</div><div class="label">Missing Files</div></div>
    </div>
    <div class="breakdown">
        <div class="pie-chart" style="background: conic-gradient(
            var(--blue) 0deg {gc_deg:.1f}deg,
            var(--orange) {gc_deg:.1f}deg {dlc_deg:.1f}deg,
            var(--teal) {dlc_deg:.1f}deg {patch_deg:.1f}deg,
            var(--purple) {patch_deg:.1f}deg {modding_deg:.1f}deg,
            var(--red) {modding_deg:.1f}deg 360deg
        );"></div>
        <div class="pie-legend">
            <h3>Not-Fetched Breakdown ({total_nf} pages)</h3>
            <div><span class="dot" style="background:var(--blue)"></span> Game Content ({len(cl["game_content"])})</div>
            <div><span class="dot" style="background:var(--orange)"></span> DLC ({len(cl["dlc"])})</div>
            <div><span class="dot" style="background:var(--teal)"></span> Patches ({len(cl["patch"])})</div>
            <div><span class="dot" style="background:var(--purple)"></span> Modding ({len(cl["modding"])})</div>
            <div><span class="dot" style="background:var(--red)"></span> Total-conversion Mods ({len(cl["mod"])})</div>
        </div>
    </div>
    <p class="generated">Generated on {d["generated_at"]}</p>
</section>'''


def _html_fetched_table(data):
    """Generate fetched pages table with file-exists status."""
    rows = []
    for i, p in enumerate(data["fetched_pages_info"], 1):
        cls = "status-ok" if p["file_exists"] else "status-missing"
        sym = "&#10003;" if p["file_exists"] else "&#10007;"
        rows.append(
            f'<tr><td>{i}</td>'
            f'<td><a href="{_esc(p["url"])}" target="_blank">{_esc(p["title"])}</a></td>'
            f'<td>{_esc(p["source"])}</td>'
            f'<td class="{cls}">{sym}</td></tr>'
        )
    tbody = "\n".join(rows)
    n = len(data["fetched_pages_info"])
    return f'''
<section id="fetched" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Fetched Pages <span class="count">({n})</span></h2>
    </div>
    <div class="section-body open">
        <input type="text" class="filter-input" placeholder="Filter fetched pages..."
               oninput="filterTable(this, 'fetched-table')">
        <table id="fetched-table">
            <thead><tr>
                <th onclick="sortTable('fetched-table',0)" style="width:3rem">#</th>
                <th onclick="sortTable('fetched-table',1)">Page Title</th>
                <th onclick="sortTable('fetched-table',2)">Source</th>
                <th onclick="sortTable('fetched-table',3)" style="width:4rem">File</th>
            </tr></thead>
            <tbody>{tbody}</tbody>
        </table>
    </div>
</section>'''


def _html_game_content(data):
    """Generate game content section with collapsible categories."""
    gc_count = len(data["classified"]["game_content"])
    parts = [f'''
<section id="game-content" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Game Content — Not Fetched <span class="count">({gc_count} pages)</span></h2>
    </div>
    <div class="section-body open">
        <p style="margin-bottom:0.75rem">Stellaris game content pages not in <code>PAGES_TO_FETCH</code>. Each page shows all its wiki categories.</p>
        <input type="text" class="filter-input" placeholder="Search all game content pages..."
               oninput="filterAllSubtables(this, 'game-content')">''']

    for cat_name, titles in data["game_by_category"]:
        rows = []
        for t in sorted(titles):
            cats_html = " ".join(
                f'<span class="tag">{_esc(c)}</span>'
                for c in data["categories_map"].get(t, [])
            ) or '<span style="opacity:0.4">none</span>'
            rows.append(
                f'<tr><td><a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a></td>'
                f'<td>{cats_html}</td></tr>'
            )
        tbody = "\n".join(rows)
        parts.append(f'''
        <div class="sub-section">
            <div class="sub-header" onclick="toggleSection(this)">
                <span class="chevron">&#9656;</span>
                <h3>{_esc(cat_name)} <span class="count">({len(titles)})</span></h3>
            </div>
            <div class="section-body open">
                <table><thead><tr>
                    <th>Page</th><th>Wiki Categories</th>
                </tr></thead><tbody>{tbody}</tbody></table>
            </div>
        </div>''')

    if data["game_uncategorized"]:
        rows = []
        for t in sorted(data["game_uncategorized"]):
            rows.append(
                f'<tr><td><a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a></td></tr>'
            )
        tbody = "\n".join(rows)
        parts.append(f'''
        <div class="sub-section">
            <div class="sub-header" onclick="toggleSection(this)">
                <span class="chevron">&#9656;</span>
                <h3>No wiki categories <span class="count">({len(data["game_uncategorized"])})</span></h3>
            </div>
            <div class="section-body open">
                <table><thead><tr><th>Page</th></tr></thead><tbody>{tbody}</tbody></table>
            </div>
        </div>''')

    parts.append("    </div>\n</section>")
    return "\n".join(parts)


def _html_dlc_section(data):
    """Generate DLC pages section (collapsed by default)."""
    pages = data["classified"]["dlc"]
    if not pages:
        return ""
    rows = []
    for t in sorted(pages):
        cats_html = " ".join(
            f'<span class="tag">{_esc(c)}</span>'
            for c in data["categories_map"].get(t, [])
        ) or ""
        rows.append(
            f'<tr><td><a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a></td>'
            f'<td>{cats_html}</td></tr>'
        )
    tbody = "\n".join(rows)
    return f'''
<section id="dlc" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>DLC Pages <span class="count">({len(pages)})</span></h2>
    </div>
    <div class="section-body">
        <table><thead><tr><th>Page</th><th>Wiki Categories</th></tr></thead>
        <tbody>{tbody}</tbody></table>
    </div>
</section>'''


def _html_patches_section(data):
    """Generate patch notes section (collapsed by default)."""
    pages = data["classified"]["patch"]
    if not pages:
        return ""
    items = ", ".join(f'<a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a>'
                      for t in sorted(pages))
    return f'''
<section id="patches" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Patch Notes / Version Pages <span class="count">({len(pages)})</span></h2>
    </div>
    <div class="section-body">
        <p>{items}</p>
    </div>
</section>'''


def _html_modding_section(data):
    """Generate modding docs section (collapsed by default)."""
    pages = data["classified"]["modding"]
    if not pages:
        return ""
    rows = "\n".join(
        f'<tr><td><a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a></td></tr>'
        for t in sorted(pages)
    )
    return f'''
<section id="modding" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Modding Documentation <span class="count">({len(pages)})</span></h2>
    </div>
    <div class="section-body">
        <table><thead><tr><th>Page</th></tr></thead><tbody>{rows}</tbody></table>
    </div>
</section>'''


def _html_mods_section(data):
    """Generate total-conversion mods section with collapsible mod groups."""
    mod_pages = data["classified"]["mod"]
    if not mod_pages:
        return ""
    parts = [f'''
<section id="mods" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Total-Conversion Mod Pages <span class="count">({len(mod_pages)})</span></h2>
    </div>
    <div class="section-body">
        <p style="margin-bottom:0.75rem">Pages for mods like ST NewHorizons, Star Trek New Civilisations, etc.</p>
        <input type="text" class="filter-input" placeholder="Search mod pages..."
               oninput="filterAllSubtables(this, 'mods')">''']

    for mod_name, pages in sorted(data["mod_groups"].items(), key=lambda x: -len(x[1])):
        rows = "\n".join(
            f'<tr><td><a href="{_esc(page_url(t))}" target="_blank">{_esc(t)}</a></td></tr>'
            for t in sorted(pages)
        )
        parts.append(f'''
        <div class="sub-section">
            <div class="sub-header" onclick="toggleSection(this)">
                <span class="chevron">&#9656;</span>
                <h3>{_esc(mod_name)} <span class="count">({len(pages)})</span></h3>
            </div>
            <div class="section-body">
                <table><thead><tr><th>Page</th></tr></thead><tbody>{rows}</tbody></table>
            </div>
        </div>''')

    parts.append("    </div>\n</section>")
    return "\n".join(parts)


def _html_redirects_section(data):
    """Generate redirects section (collapsed by default), with section anchors."""
    redirects = data["relevant_redirects"]
    if not redirects:
        return ""
    row_parts = []
    for src, tgt, frag in redirects:
        display = f"{tgt} &raquo; {_esc(frag)}" if frag else _esc(tgt)
        url = page_url(tgt, frag)
        row_parts.append(
            f'<tr><td>{_esc(src)}</td><td><a href="{_esc(url)}" target="_blank">{display}</a></td></tr>'
        )
    rows = "\n".join(row_parts)
    return f'''
<section id="redirects" class="section">
    <div class="section-header" onclick="toggleSection(this)">
        <span class="chevron">&#9656;</span>
        <h2>Redirects to Fetched Pages <span class="count">({len(redirects)})</span></h2>
    </div>
    <div class="section-body">
        <p style="margin-bottom:0.75rem">These redirect to pages you already fetch — no action needed.</p>
        <input type="text" class="filter-input" placeholder="Filter redirects..."
               oninput="filterTable(this, 'redirects-table')">
        <table id="redirects-table">
            <thead><tr>
                <th onclick="sortTable('redirects-table',0)">Redirect</th>
                <th onclick="sortTable('redirects-table',1)">Target</th>
            </tr></thead>
            <tbody>{rows}</tbody>
        </table>
    </div>
</section>'''


def _html_scripts():
    """Generate JavaScript for interactivity."""
    return '''
<script>
function toggleSection(header) {
    const body = header.nextElementSibling;
    const chevron = header.querySelector('.chevron');
    if (!body || !body.classList.contains('section-body')) return;
    if (body.classList.contains('open')) {
        body.classList.remove('open');
        if (chevron) chevron.style.transform = 'rotate(0deg)';
    } else {
        body.classList.add('open');
        if (chevron) chevron.style.transform = 'rotate(90deg)';
    }
}

function filterTable(input, tableId) {
    const filter = input.value.toLowerCase();
    const table = document.getElementById(tableId);
    if (!table) return;
    table.querySelectorAll('tbody tr').forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
    });
}

function filterAllSubtables(input, sectionId) {
    const filter = input.value.toLowerCase();
    const section = document.getElementById(sectionId);
    if (!section) return;
    section.querySelectorAll('tbody tr').forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
    });
    section.querySelectorAll('.sub-section').forEach(sub => {
        const visible = sub.querySelectorAll('tbody tr:not([style*="display: none"])');
        sub.style.display = visible.length > 0 ? '' : 'none';
    });
}

function sortTable(tableId, colIndex) {
    const table = document.getElementById(tableId);
    if (!table) return;
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const th = table.querySelectorAll('th')[colIndex];
    const dir = th.dataset.sortDir === 'asc' ? 'desc' : 'asc';
    table.querySelectorAll('th').forEach(h => {
        h.classList.remove('sort-asc', 'sort-desc');
        h.dataset.sortDir = 'none';
    });
    th.dataset.sortDir = dir;
    th.classList.add('sort-' + dir);
    rows.sort((a, b) => {
        let av = a.cells[colIndex]?.textContent.trim() || '';
        let bv = b.cells[colIndex]?.textContent.trim() || '';
        const an = parseFloat(av), bn = parseFloat(bv);
        if (!isNaN(an) && !isNaN(bn)) return dir === 'asc' ? an - bn : bn - an;
        return dir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av);
    });
    rows.forEach(row => tbody.appendChild(row));
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.section-body.open').forEach(body => {
        const chevron = body.previousElementSibling?.querySelector('.chevron');
        if (chevron) chevron.style.transform = 'rotate(90deg)';
    });
});
</script>
</div>
</body>
</html>'''


def generate_html_report(data: dict, output_path: Path) -> str:
    """Generate a self-contained interactive HTML analysis report."""
    parts = [
        _html_head(data),
        _html_nav(data),
        _html_dashboard(data),
        _html_fetched_table(data),
        _html_game_content(data),
        _html_dlc_section(data),
        _html_patches_section(data),
        _html_modding_section(data),
        _html_mods_section(data),
        _html_redirects_section(data),
        _html_scripts(),
    ]
    html_str = "\n".join(parts)
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

def main():
    parser = argparse.ArgumentParser(
        description="Analyze Stellaris wiki pages and generate an interactive report."
    )
    parser.add_argument(
        "--format", choices=["html", "md"], default="html",
        help="Output format: html (interactive, default) or md (markdown)"
    )
    parser.add_argument(
        "--workers", type=int, default=cfg.defaults.workers,
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

    session = create_session()
    output_dir = Path(script_dir) / cfg.defaults.output_dir
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

    # 7. Fetch categories (PARALLEL)
    categories_map = fetch_categories_parallel(not_fetched, workers=args.workers)

    # 8. Scan existing files
    pages_dir = Path(script_dir) / cfg.defaults.output_dir / "pages"
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
        all_pages_path = Path(script_dir) / "all_pages.md"
        generate_all_pages_md(
            content_pages, redirect_pages, data["all_fetched"],
            composite_subpages, all_pages_path,
        )

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
    print(f"Total wiki pages: {data['total_pages']:,}")
    print(f"  Content: {data['num_content']:,} | Redirects: {data['num_redirects']:,}")
    print(f"Fetched: {len(data['all_fetched'])} | Files on disk: {data['files_on_disk']}")
    print(f"Not fetched: {len(data['not_fetched']):,}")


if __name__ == "__main__":
    main()
