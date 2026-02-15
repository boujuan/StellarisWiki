# Stellaris Wiki Scraper

A tool for fetching and converting Stellaris Wiki pages into clean, token-efficient Markdown optimized for LLM consumption.

## Overview

This project fetches game data from the [Stellaris Wiki](https://stellaris.paradoxwikis.com/) and converts it to clean Markdown format. It uses MediaWiki's `action=parse` API to get server-rendered HTML (with all templates expanded), then converts that HTML to structured Markdown.

### Why This Approach?

| Approach | Output Size | Issues |
|----------|-------------|--------|
| Raw wikitext | ~4.3 MB | Templates not expanded, hard to parse |
| Parsed to JSON | ~11 MB | JSON overhead, template artifacts |
| **HTML to Markdown** | **~3.1 MB** | Clean, structured, token-efficient |

The HTML-to-Markdown approach produces output that is **~70% smaller** than the JSON approach while maintaining all the important game data in a clean, readable format.

## Features

- Fetches 95 game concept pages using MediaWiki's `action=parse` API (server expands all templates)
- Converts HTML tables to proper Markdown tables
- Preserves section hierarchy with Markdown headers
- Removes navigation boxes, edit links, and other wiki chrome
- Outputs individual `.md` files per page plus a single combined file
- YAML frontmatter with title and categories
- Rate limiting to respect the wiki's servers
- Retry logic with exponential backoff

## Installation

### Prerequisites

- Python 3.11+
- micromamba, conda, or pip

### Using micromamba (recommended)

```bash
# Create environment from environment.yml
micromamba create -f environment.yml
micromamba run -n stellaris-scraper pip install cloudscraper

# Or manually
micromamba create -n stellaris-scraper python=3.11 tqdm beautifulsoup4 lxml -c conda-forge
micromamba run -n stellaris-scraper pip install cloudscraper
```

### Using pip

```bash
pip install -r requirements.txt
```

### Dependencies

```
cloudscraper>=1.2.71    # Bypass Cloudflare protection
tqdm>=4.66.0            # Progress bars
beautifulsoup4>=4.11.0  # HTML parsing
lxml>=4.9.0             # Fast HTML parser backend
```

## Usage

### Fetch and Convert All Pages to Markdown

```bash
# Using micromamba
micromamba run -n stellaris-scraper python fetch_and_parse.py

# Or if environment is activated
python fetch_and_parse.py
```

This will:
1. Fetch all 95 predefined game pages from the wiki
2. Convert each to Markdown
3. Save individual files to `output_markdown/pages/`
4. Create a combined file at `output_markdown/stellaris_4.2_combined.md`

### Test Single Page

```bash
# Test mode shows first 2000 characters of output
python fetch_and_parse.py --page "Machine_traits" --test

# Process single page without test output
python fetch_and_parse.py --page "Civics"
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--page TITLE` | Process a single page by title | (all pages) |
| `--test` | Run in test mode (use with `--page`) | false |
| `--output DIR` | Output directory | `output_markdown` |
| `--delay SECONDS` | Delay between API requests | `0.5` |

### Examples

```bash
# Fetch all pages with default settings
python fetch_and_parse.py

# Faster fetching (be nice to the wiki!)
python fetch_and_parse.py --delay 0.3

# Custom output directory
python fetch_and_parse.py --output my_wiki_data

# Test a specific page
python fetch_and_parse.py --page "Technology" --test
```

## Output Format

### Individual Markdown Files

Each page is saved as `output_markdown/pages/{Page_Title}.md`:

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

All pages are concatenated into `output_markdown/stellaris_4.2_combined.md`, separated by `---` dividers.

## Project Structure

```
stellaris_wiki_scraper/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── environment.yml           # Conda/micromamba environment
│
├── fetch_and_parse.py        # Main script: fetch HTML → convert to Markdown
├── html_to_markdown.py       # HTML to Markdown converter class
│
├── fetch_specific_pages.py   # Fetch raw wikitext (legacy)
├── scraper.py                # Full wiki scraper (legacy)
├── parser.py                 # Wikitext parser (legacy)
├── template_resolver.py      # Template mappings (legacy)
│
└── output_markdown/          # Markdown output (generated)
    ├── pages/                # Individual .md files (95 pages)
    │   ├── Machine_traits.md
    │   ├── Civics.md
    │   ├── Corporate_civics.md
    │   └── ...
    └── stellaris_4.2_combined.md  # Single combined file
```

## Pages Fetched

The tool fetches 95 game concept pages covering:

| Category | Pages |
|----------|-------|
| **Empire Setup** | Origin, Government, Authorities, Ethics, Civics, Corporate civics, Hive mind civics, Machine intelligence civics, Empire |
| **Governance** | Council, Agendas, Policies, Edicts, Factions, Traditions, Ascension perks, Situations, Crisis empire |
| **Species** | Species traits, Biological traits, Machine traits, Population, Species rights |
| **Leaders** | Leaders, Common leader traits, Commander traits, Scientist traits, Official traits, Paragons |
| **Economy** | Resources, Trade, Planetary management, Jobs, Districts, Designation, Holdings, Megastructures, Colonization, Terraforming |
| **Buildings** | Planet capital, Unique buildings, Holdings |
| **Technology** | Technology, Physics research, Society research, Engineering research |
| **Ships** | Ship, Ship designer, Fleet, Core components, Weapon components, Utility components, Mutations, Offensive mutations |
| **Military** | Warfare, Space warfare, Land warfare, Army, Bombardment, Starbase |
| **Exploration** | Exploration, FTL, Discovery, Anomaly, Archaeological site, Astral rift, Relics, Collection, Unique systems, L-Cluster |
| **Diplomacy** | Diplomacy, Relations, Galactic community, Federations, Subject empire, Intelligence, Espionage, AI personalities |
| **NPCs** | Fallen empire, Spaceborne aliens, Pre-FTL species, Enclaves, Guardians, Marauders, Caravaneers |
| **Other** | Empire modifiers, Stat modifiers, Events, The Shroud, Console commands, Easter eggs, AI players, Preset empires |

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

- Default delay: 0.5 seconds between requests
- Exponential backoff on errors (2s, 4s, 8s, 16s, 32s)
- Maximum 5 retries per page

## HTML to Markdown Conversion

The `HTMLToMarkdown` class handles conversion with these features:

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

### Elements Removed

- Navigation boxes (`.navbox`)
- Edit section links (`.mw-editsection`)
- Table of contents (`.toc`)
- References section
- Images
- Stellaris outliner boxes
- Infoboxes (navigation type)

## Troubleshooting

### Cloudflare Blocking

The tool uses `cloudscraper` to bypass Cloudflare protection. If you get blocked:

1. Increase the delay: `--delay 1.0`
2. Wait a few minutes and try again
3. Check if the wiki is accessible in your browser

### Empty Output

If pages have very little content:

1. Check if the page exists on the wiki
2. Verify your internet connection
3. Run with `--test` to see raw output

### Missing Tables

Some complex wiki tables with colspan/rowspan may not convert perfectly. The converter handles basic colspan but complex nested tables may be simplified.

## Contributing

To add new pages to fetch, edit the `PAGES_TO_FETCH` list in `fetch_and_parse.py`:

```python
PAGES_TO_FETCH = [
    "Origin",
    "Traditions",
    # Add new pages here
    "New_Page_Title",
]
```

## License

This tool is for educational and research purposes. All wiki content is owned by Paradox Interactive and wiki contributors under their respective licenses.

## Version Compatibility

- **Wiki Version**: 4.2 (Stellaris game version)
- **Python**: 3.11+
- **Last Updated**: February 2025
