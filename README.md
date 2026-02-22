# Stellaris Wiki Scraper

A tool for fetching and converting Stellaris Wiki pages into clean, token-efficient Markdown optimized for LLM consumption.

> **[Ask any question about Stellaris using the NotebookLM with all parsed wiki docs loaded](https://notebooklm.google.com/notebook/ae857011-2ba6-4312-ad22-a6b8b6c891a3)**
>
> **[Browse the interactive Wiki Analysis Dashboard](https://boujuan.github.io/StellarisWiki/)**

## Overview

This project fetches game data from the [Stellaris Wiki](https://stellaris.paradoxwikis.com/) and converts it to clean Markdown format. It uses MediaWiki's `action=parse` API to get server-rendered HTML (with all templates expanded), then converts that HTML to structured Markdown.

### Why This Approach?

| Approach | Output Size | Issues |
|----------|-------------|--------|
| Raw wikitext | ~4.3 MB | Templates not expanded, hard to parse |
| Parsed to JSON | ~11 MB | JSON overhead, template artifacts |
| **HTML to Markdown** | **~4.9 MB** | Clean, structured, token-efficient |

The HTML-to-Markdown approach produces output that is **~55% smaller** than the JSON approach while maintaining all the important game data in a clean, readable format.

## Features

- Fetches 101 game concept pages (+ 99 event/rift sub-pages) using MediaWiki's `action=parse` API
- Parallel fetching with configurable worker count (default: 4 workers)
- **Composite pages**: Events and Astral rift pages aggregate sub-page content
- Converts HTML tables to proper Markdown tables (with list-in-cell support via `<br>`)
- Preserves section hierarchy with Markdown headers
- **Bold formatting** for civic names, tradition names, and building names
- **LaTeX math formulas** converted to readable plain text
- **Tabbed content** (MediaWiki Tabber extension) flattened into sequential sections
- Removes navigation boxes, edit links, tooltips, and other wiki chrome
- Outputs individual `.md` files per page plus a single combined file
- YAML frontmatter with title and categories
- Content error detection (math render failures, raw LaTeX)
- Rate limiting and retry logic with exponential backoff
- **Interactive HTML dashboard** with wiki coverage analysis, category filters, and expand/collapse all sections
- **Page management buttons**: +/- buttons per page to add/remove from `config.yaml` (downloads modified config)
- **Zip download**: all fetched pages bundled as `stellaris_wiki_pages.zip` (locally after fetch + GitHub Release)
- **External links**: Stellaris Wiki and NotebookLM links with favicons in the dashboard nav bar

## Installation

### Prerequisites

- Python 3.11+

### Install (recommended)

```bash
# Clone and install as editable package
git clone https://github.com/boujuan/StellarisWiki.git
cd StellarisWiki
pip install -e .

# With MCP server support (for Claude Desktop integration)
pip install -e ".[mcp]"
```

This installs the `stellariswiki` command globally in your environment.

### Using micromamba

```bash
micromamba create -f environment.yml
micromamba activate stellaris-scraper
pip install -e ".[mcp]"
```

### Dependencies

Core dependencies (installed automatically via `pip install`):

```
cloudscraper>=1.2.71    # Bypass Cloudflare protection
tqdm>=4.66.0            # Progress bars
beautifulsoup4>=4.11.0  # HTML parsing
lxml>=4.9.0             # Fast HTML parser backend
PyYAML>=6.0             # Config parsing
```

Optional (for MCP server — `pip install -e ".[mcp]"`):

```
fastmcp>=2.0.0          # MCP server framework
```

## Usage

After installation, use the `stellariswiki` command (or `python stellariswiki.py`):

```bash
stellariswiki --help       # Show all commands and examples
stellariswiki --version    # Show version
```

### Fetch and Convert All Pages to Markdown

```bash
stellariswiki fetch
```

This will:
1. Fetch all 101 predefined game pages from the wiki
2. Fetch sub-pages for composite pages (87 event chains + 12 astral rifts)
3. Convert each to Markdown
4. Save individual files to `output/pages/`
5. Create a combined file at `output/stellaris_4.2_combined.md`
6. Print content warnings (if any math render errors remain)

### Test Single Page

```bash
# Test mode shows first 2000 characters of output
stellariswiki fetch --page "Machine_traits" --test

# Process single page without test output
stellariswiki fetch --page "Civics"

# Test a composite page (fetches all sub-pages)
stellariswiki fetch --page "Astral rift" --test
```

### Analyze Wiki Coverage

```bash
# Generate interactive HTML dashboard
stellariswiki analyze

# Generate Markdown report
stellariswiki analyze --format md

# Skip all_pages.md generation
stellariswiki analyze --no-all-pages
```

### Command Line Options

**`stellariswiki fetch`**

| Option | Description | Default |
|--------|-------------|---------|
| `--page TITLE` | Process a single page by title | (all pages) |
| `--test` | Test mode: print first 2000 chars (use with `--page`) | false |
| `--output DIR` | Output directory | `output` |
| `--delay SEC` | Delay between API requests (sequential mode) | `0.5` |
| `--workers N` | Number of parallel workers | `4` |

**`stellariswiki analyze`**

| Option | Description | Default |
|--------|-------------|---------|
| `--format {html,md}` | Output format | `html` |
| `--workers N` | Number of parallel workers for API calls | `4` |
| `--output PATH` | Output file path | `output/wiki_analysis.{html,md}` |
| `--no-all-pages` | Skip generating all_pages.md | false |

**`stellariswiki serve`**

| Option | Description | Default |
|--------|-------------|---------|
| `--transport {stdio,sse}` | MCP transport protocol | `stdio` |

### Examples

```bash
# Fetch all pages with default settings (4 parallel workers)
stellariswiki fetch

# Sequential fetching (gentler on the wiki)
stellariswiki fetch --workers 1 --delay 1.0

# Custom output directory
stellariswiki fetch --output my_wiki_data

# Test a specific page
stellariswiki fetch --page "Technology" --test

# Generate HTML dashboard + all_pages.md
stellariswiki analyze

# Start MCP server for Claude Desktop
stellariswiki serve
```

## MCP Server (StellarisWikiMCP)

An MCP (Model Context Protocol) server is included, allowing Claude Desktop to query the wiki data directly.

### Setup

1. Install with MCP support:

```bash
pip install -e ".[mcp]"
```

2. Add to Claude Desktop config (`~/.config/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "StellarisWikiMCP": {
      "command": "stellariswiki",
      "args": ["serve"]
    }
  }
}
```

3. Restart Claude Desktop. The server will appear in the tools list.

### Available Tools

| Tool | Description | Example |
|------|-------------|---------|
| `list_pages` | List all available wiki pages | "What Stellaris wiki pages are available?" |
| `get_page` | Get full content of a page (fuzzy matching) | "Get the Machine traits page" |
| `search_wiki` | Search across all pages, returns snippets | "Search for Efficient Processors" |

### Testing

```bash
# Test the server with the MCP inspector
micromamba run -n stellaris-scraper fastmcp dev src/mcp_server.py
```

## Output Format

### Individual Markdown Files

Each page is saved as `output/pages/{Page_Title}.md`:

```markdown
---
title: "Machine traits"
categories: ["4.2", "Game_concepts"]
---

# Machine traits

Machine traits are available to species with the Machine and Mechanical
primary traits...

## Climate preference traits

Each species has a climate preference trait that determines their base
Habitability on the various types of planets...

| Preference | Dry | Wet | Cold | Volcanic | Other | Source |
|---|---|---|---|---|---|---|
| Dry | 75% | 50% | 50% | 25% | | Empire creation Machine modification |
| Wet | 50% | 75% | 50% | 25% | | |
...
```

### Combined File

All pages are concatenated into `output/stellaris_4.2_combined.md`, separated by `---` dividers.

## Project Structure

```
stellaris_wiki_scraper/
├── stellariswiki.py          # Script entry point (python stellariswiki.py ...)
├── pyproject.toml            # Package metadata, dependencies, console_scripts
├── config/
│   └── config.yaml           # Pages to fetch + classification rules
├── src/
│   ├── __init__.py           # Package version + path constants
│   ├── cli.py                # CLI argument parser + command dispatch
│   ├── config.py             # Config loader (dataclasses), singleton cfg
│   ├── fetcher.py            # Fetch wiki HTML → convert to Markdown
│   ├── converter.py          # HTML to Markdown converter class
│   ├── analyzer.py           # Wiki coverage analysis + HTML dashboard
│   └── mcp_server.py         # MCP server for Claude Desktop
├── .github/workflows/
│   ├── pages.yml             # Deploy dashboard to GitHub Pages
│   └── release.yml           # Upload zip as GitHub Release
│
└── output/                   # All generated output
    ├── pages/                # Individual .md files (108+ pages)
    │   ├── Machine_traits.md
    │   ├── Civics.md
    │   ├── Events.md         # Composite: main + 91 event sub-pages
    │   ├── Astral_rift.md    # Composite: main + 22 rift sub-pages
    │   └── ...
    ├── stellaris_4.2_combined.md   # Single combined file (~4.9 MB)
    ├── stellaris_wiki_pages.zip    # Zip of all pages (generated, not in git)
    ├── all_pages.md                # Complete list of all 4994 wiki pages
    ├── index.html                  # Redirect → wiki_analysis.html
    └── wiki_analysis.html          # Interactive analysis dashboard
```

## Pages Fetched

The tool fetches 101 game concept pages covering:

| Category | Pages |
|----------|-------|
| **Empire Setup** | Origin, Government, Ethics, Civics, Corporate civics, Hive mind civics, Machine intelligence civics, Empire |
| **Governance** | Council, Policies, Edicts, Factions, Traditions, Ascension perks, Situations, Crisis empire |
| **Species** | Species, Species traits, Biological traits, Machine traits, Population, Species rights |
| **Leaders** | Leaders, Common leader traits, Commander traits, Scientist traits, Official traits, Paragons |
| **Economy & Buildings** | Resources, Planetary management, Jobs, Districts, Designation, Holdings, Planet capital, Buildings, Unique buildings, Megastructures, Colonization |
| **Technology** | Technology, Physics research, Society research, Engineering research |
| **Ships & Components** | Ship, Ship designer, Core components, Weapon components, Utility components, Mutations, Offensive mutations |
| **Military** | Warfare, Space warfare, Land warfare, Starbase |
| **Exploration** | Exploration, FTL travel, Discovery, Anomaly, Archaeological site, Astral rift (+12 sub-pages), Celestial object, Planet modifiers, Planetary features, Unique systems, Relics, Collection, L-Cluster, The Shroud |
| **Diplomacy** | Diplomacy, Relations, Galactic Community, Federation, Subject empire, Intelligence, AI personalities |
| **NPCs** | Fallen empire, Spaceborne aliens, Pre-FTL species, Enclaves, Guardians, Marauders, Caravaneers |
| **Modifiers & Events** | Empire modifiers, Stat modifiers, Events (+87 event chain sub-pages) |
| **Crisis** | Crisis, Prethoryn Scourge, Extradimensional Invaders, Contingency, The Synthetic Queen |
| **Reference** | Achievements, Effects, Galaxy settings, Beginner's guide, Hotkeys, Jargon, User interface, Console commands, Easter eggs, AI players, Preset empires, Modding |

See [`all_pages.md`](output/all_pages.md) for the complete list of all 4994 wiki pages (with checkmarks showing which are currently fetched).

## Adding New Pages

To add new pages, edit the `pages_to_fetch` list in `config/config.yaml`:

```yaml
pages_to_fetch:
  # ...existing pages...
  - "New_Page_Title"  # Use the exact wiki page title
```

Page titles must match the wiki URL (e.g., `https://stellaris.paradoxwikis.com/Achievements` → `"Achievements"`). Pages with spaces in the title work too (e.g., `"Beginner's guide"`).

Then re-run the fetch:

```bash
stellariswiki fetch
```

## HTML to Markdown Conversion

The `HTMLToMarkdown` class handles conversion with these features:

### Preprocessing Pipeline

1. **Component icons** — CSS grid spans replaced with text names
2. **Tabbed content** — MediaWiki Tabber extension flattened to sequential sections
3. **Math/LaTeX** — Formulas converted to readable plain text (e.g., `\frac{a}{b}` → `a / b`)
4. **Navigation removal** — Navboxes, footers, tooltips, infoboxes stripped
5. **Bold formatting** — Civic/tradition/building names preserved as `**bold**`
6. **Image handling** — Semantic alt text kept, decorative icons stripped

### Elements Converted

| HTML | Markdown |
|------|----------|
| `<h2>`, `<h3>`, etc. | `##`, `###`, etc. |
| `<p>` | Paragraph text |
| `<table>` | Markdown table |
| `<ul>`, `<ol>` | `-` or `1.` lists |
| `<dl>` | Bold terms with descriptions |
| `<pre>` | Code blocks |
| `<blockquote>` | `>` quoted text |
| `<div>` (inline content) | Paragraph text |
| `<math>` / LaTeX | Plain text formulas |
| `<tabber>` | Sequential sections with labels |

### Elements Removed

- Navigation boxes (`.navbox`)
- Navigation footers (Game concepts, Modding, Stellaris bars)
- Edit section links (`.mw-editsection`)
- Table of contents (`.toc`)
- References section
- Tooltip popups (`.tooltiptext`)
- Decorative images (icons duplicating adjacent text)
- Infoboxes (navigation type)

## API Details

### MediaWiki Parse API

The tool uses the MediaWiki `action=parse` endpoint:

```
GET https://stellaris.paradoxwikis.com/api.php
?action=parse
&page={title}
&prop=text|sections|categories|displaytitle
&disabletoc=true
&disableeditsection=true
&format=json
```

This returns server-rendered HTML with all templates expanded, which is then converted to Markdown.

### Rate Limiting

- Parallel mode: 4 concurrent workers (configurable with `--workers`)
- Sequential mode: configurable delay between requests (default: 0.5s)
- Exponential backoff on errors (2s, 4s, 8s, 16s, 32s)
- Maximum 5 retries per page

## Troubleshooting

### Cloudflare Blocking

The tool uses `cloudscraper` to bypass Cloudflare protection. If you get blocked:

1. Reduce workers: `--workers 1`
2. Wait a few minutes and try again
3. Check if the wiki is accessible in your browser

### Content Warnings

After processing, the tool reports content warnings for any remaining issues (e.g., math render failures). These are informational — the page is still saved, but some formulas may not have converted cleanly.

### Missing Tables

Some complex wiki tables with colspan/rowspan may not convert perfectly. The converter handles basic colspan but complex nested tables may be simplified.

## License

This tool is for educational and research purposes. All wiki content is owned by Paradox Interactive and wiki contributors under their respective licenses.

## Version Compatibility

- **Package Version**: 1.0.0
- **Wiki Version**: 4.2 (Stellaris game version)
- **Python**: 3.11+
- **Last Updated**: February 2026
