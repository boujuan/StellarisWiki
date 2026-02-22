#!/usr/bin/env python3
"""
StellarisWikiMCP - MCP server for querying Stellaris Wiki data.

Provides tools to search, browse, and read Stellaris game wiki pages
that have been converted to Markdown.
"""

import json
import re
from pathlib import Path

from fastmcp import FastMCP

from config import cfg

# Path to markdown pages
PAGES_DIR = Path(__file__).parent / cfg.defaults.output_dir / "pages"

# In-memory store for wiki pages
wiki_pages: dict[str, dict] = {}


def load_pages():
    """Load all markdown pages into memory at startup."""
    if not PAGES_DIR.exists():
        return

    for md_file in PAGES_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")

        # Parse YAML frontmatter
        title = md_file.stem.replace("_", " ")
        categories = []

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2].strip()

                # Extract title
                title_match = re.search(r'title:\s*"(.+?)"', frontmatter)
                if title_match:
                    title = title_match.group(1)

                # Extract categories
                cat_match = re.search(r'categories:\s*(\[.+?\])', frontmatter)
                if cat_match:
                    try:
                        categories = json.loads(cat_match.group(1))
                    except json.JSONDecodeError:
                        pass
            else:
                body = content
        else:
            body = content

        wiki_pages[md_file.stem] = {
            "title": title,
            "categories": categories,
            "content": body,
            "filename": md_file.name,
        }


# Load pages at import time
load_pages()

# Create MCP server
mcp = FastMCP(
    "StellarisWikiMCP",
    instructions=(
        "This server provides access to Stellaris game wiki data. "
        "Use search_wiki to find information about game mechanics, "
        "get_page to read a full wiki page, and list_pages to see "
        "all available pages."
    ),
)


@mcp.tool()
def list_pages() -> str:
    """List all available Stellaris wiki pages with their categories.

    Returns a formatted list of all pages that can be queried.
    """
    lines = []
    for key in sorted(wiki_pages.keys()):
        page = wiki_pages[key]
        cats = ", ".join(page["categories"]) if page["categories"] else ""
        lines.append(f"- {page['title']}" + (f" [{cats}]" if cats else ""))

    return f"Available pages ({len(wiki_pages)}):\n\n" + "\n".join(lines)


@mcp.tool()
def get_page(page_name: str) -> str:
    """Get the full content of a specific Stellaris wiki page.

    Args:
        page_name: The page name to look up. Case-insensitive, supports
                   partial matching. E.g. "machine traits", "civics",
                   "corporate civics".

    Returns:
        The full Markdown content of the matching page.
    """
    query = page_name.lower().replace(" ", "_")

    # Exact match first
    for key, page in wiki_pages.items():
        if key.lower() == query:
            return f"# {page['title']}\n\n{page['content']}"

    # Partial match
    matches = []
    for key, page in wiki_pages.items():
        if query in key.lower() or query in page["title"].lower():
            matches.append((key, page))

    if len(matches) == 1:
        key, page = matches[0]
        return f"# {page['title']}\n\n{page['content']}"
    elif len(matches) > 1:
        names = "\n".join(f"- {p['title']}" for _, p in matches)
        return f"Multiple pages match '{page_name}':\n\n{names}\n\nPlease be more specific."

    return f"No page found matching '{page_name}'. Use list_pages() to see available pages."


@mcp.tool()
def search_wiki(query: str, max_results: int = 5) -> str:
    """Search across all Stellaris wiki pages for information.

    Performs case-insensitive search across all page content and returns
    relevant snippets with context.

    Args:
        query: The search term or phrase. E.g. "Efficient Processors",
               "habitability bonus", "federation types".
        max_results: Maximum number of results to return (default 5).

    Returns:
        Matching snippets from wiki pages with context.
    """
    query_lower = query.lower()
    results = []

    for key, page in wiki_pages.items():
        content_lower = page["content"].lower()

        if query_lower not in content_lower:
            continue

        # Find all occurrences and extract snippets
        snippets = []
        lines = page["content"].split("\n")

        for i, line in enumerate(lines):
            if query_lower in line.lower():
                # Get context: 1 line before, matching line, 2 lines after
                start = max(0, i - 1)
                end = min(len(lines), i + 3)
                snippet = "\n".join(lines[start:end]).strip()
                if snippet and snippet not in snippets:
                    snippets.append(snippet)

                if len(snippets) >= 2:
                    break

        if snippets:
            results.append({
                "page": page["title"],
                "snippets": snippets,
            })

        if len(results) >= max_results:
            break

    if not results:
        return f"No results found for '{query}'."

    output_parts = [f"Found {len(results)} page(s) matching '{query}':\n"]

    for r in results:
        output_parts.append(f"## {r['page']}\n")
        for snippet in r["snippets"]:
            output_parts.append(f"{snippet}\n")
        output_parts.append("")

    return "\n".join(output_parts)


if __name__ == "__main__":
    mcp.run(transport="stdio")
