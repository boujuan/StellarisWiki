#!/usr/bin/env python3
"""
Stellaris Wiki Parser - Transform wikitext to structured JSON.

Converts raw wikitext from Stellaris Wiki pages into clean, structured JSON
optimized for LLM consumption. Handles tables, templates, and wiki markup.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

import wikitextparser as wtp

from template_resolver import resolve_template, clean_wiki_markup


class WikiParser:
    """Parser for Stellaris Wiki wikitext content."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def parse_page(self, content: str) -> dict[str, Any]:
        """
        Parse wikitext content into structured data.

        Args:
            content: Raw wikitext string

        Returns:
            Dictionary with sections, tables, and plain_text
        """
        parsed = wtp.parse(content)

        return {
            "sections": self._extract_sections(parsed),
            "tables": self._extract_tables(parsed),
            "plain_text": self._get_plain_text(content),
        }

    def _extract_sections(self, parsed: wtp.WikiText) -> dict[str, Any]:
        """
        Extract sections organized by header level.

        Returns a dictionary where keys are section titles and values contain:
        - level: Header level (2 for ==, 3 for ===, etc.)
        - content: Cleaned text content of the section
        - tables: Tables found within this section
        """
        sections = {}

        for section in parsed.sections:
            # Skip the lead section (no title)
            if not section.title:
                # Store lead content separately
                lead_content = self._clean_text(section.contents)
                if lead_content.strip():
                    sections["_lead"] = {
                        "level": 0,
                        "content": lead_content,
                        "tables": self._extract_section_tables(section),
                    }
                continue

            title = self._clean_text(section.title).strip()
            if not title:
                continue

            # Get section content excluding subsections
            # The section.contents includes subsections, so we need to be careful
            section_content = self._get_section_own_content(section)

            sections[title] = {
                "level": section.level,
                "content": self._clean_text(section_content),
                "tables": self._extract_section_tables(section),
            }

        return sections

    def _get_section_own_content(self, section: wtp.Section) -> str:
        """Get section content excluding nested subsections."""
        full_content = section.contents

        # Remove nested section headers and their content
        # This is a simplified approach - just get content before first subsection
        parsed = wtp.parse(full_content)
        subsections = [s for s in parsed.sections if s.level > 0 and s.title]

        if not subsections:
            return full_content

        # Find the first subsection and cut there
        first_sub = subsections[0]
        first_sub_str = str(first_sub)
        idx = full_content.find(first_sub_str)
        if idx > 0:
            return full_content[:idx]

        return full_content

    def _extract_section_tables(self, section: wtp.Section) -> list[dict]:
        """Extract tables from a specific section."""
        parsed = wtp.parse(section.contents if hasattr(section, 'contents') else str(section))
        return self._extract_tables_from_parsed(parsed)

    def _extract_tables(self, parsed: wtp.WikiText) -> list[dict[str, Any]]:
        """
        Extract all tables from the parsed wikitext.

        Returns a list of table dictionaries with:
        - headers: List of column header names
        - rows: List of dictionaries (header -> cell value)
        """
        return self._extract_tables_from_parsed(parsed)

    def _extract_tables_from_parsed(self, parsed: wtp.WikiText) -> list[dict[str, Any]]:
        """Extract tables from a parsed wikitext object."""
        tables = []

        for table in parsed.tables:
            try:
                table_data = self._parse_table(table)
                if table_data:
                    tables.append(table_data)
            except Exception as e:
                if self.verbose:
                    print(f"Warning: Failed to parse table: {e}", file=sys.stderr)
                continue

        return tables

    def _parse_table(self, table: wtp.Table) -> Optional[dict[str, Any]]:
        """
        Parse a single wiki table into structured data.

        Returns dictionary with headers and rows, or None if table is empty.
        """
        try:
            data = table.data()
        except Exception:
            # Some tables have malformed syntax
            return None

        if not data or len(data) == 0:
            return None

        # First row is typically headers
        raw_headers = data[0] if data else []
        headers = [self._clean_text(str(h)).strip() for h in raw_headers]

        # Handle empty or all-empty headers
        if not headers or all(not h for h in headers):
            # Generate column names
            if len(data) > 1:
                headers = [f"col_{i}" for i in range(len(data[1]))]
            else:
                return None

        # Process data rows
        rows = []
        for row_data in data[1:]:
            # Skip separator rows (often empty or just formatting)
            if not row_data or all(not str(cell).strip() for cell in row_data):
                continue

            row_dict = {}
            for i, cell in enumerate(row_data):
                # Use header name or generate column name
                key = headers[i] if i < len(headers) else f"col_{i}"
                # Skip empty header columns
                if not key:
                    key = f"col_{i}"
                row_dict[key] = self._clean_text(str(cell)).strip()

            # Only add non-empty rows
            if any(v for v in row_dict.values()):
                rows.append(row_dict)

        if not rows:
            return None

        return {
            "headers": headers,
            "rows": rows,
        }

    def _extract_lists(self, parsed: wtp.WikiText) -> list[list[str]]:
        """Extract bullet/numbered lists from parsed content."""
        lists = []
        for wikilist in parsed.get_lists():
            items = []
            for item in wikilist.items:
                cleaned = self._clean_text(item)
                if cleaned.strip():
                    items.append(cleaned.strip())
            if items:
                lists.append(items)
        return lists

    def _get_plain_text(self, content: str) -> str:
        """
        Convert wikitext to plain text, removing all markup.

        This is useful for full-text search and simple display.
        """
        return self._clean_text(content)

    def _clean_text(self, text: str) -> str:
        """
        Clean wikitext by resolving templates and removing markup.

        Args:
            text: Raw wikitext string

        Returns:
            Cleaned plain text
        """
        if not text:
            return ""

        # Parse the text to find templates
        parsed = wtp.parse(text)

        # Resolve templates from innermost to outermost
        result = text
        for template in reversed(parsed.templates):
            try:
                resolved = resolve_template(template)
                result = result.replace(str(template), resolved, 1)
            except Exception:
                # If resolution fails, just remove the template
                result = result.replace(str(template), "", 1)

        # Clean remaining wiki markup
        result = clean_wiki_markup(result)

        # Clean up table syntax remnants
        result = re.sub(r'\{\|[^}]*$', '', result, flags=re.MULTILINE)
        result = re.sub(r'^\|\}', '', result, flags=re.MULTILINE)
        result = re.sub(r'^\|-.*$', '', result, flags=re.MULTILINE)
        result = re.sub(r'^!.*$', '', result, flags=re.MULTILINE)
        result = re.sub(r'^\|.*$', '', result, flags=re.MULTILINE)

        # Clean up whitespace
        result = re.sub(r'\n{3,}', '\n\n', result)
        result = re.sub(r' +', ' ', result)
        result = re.sub(r'^\s+', '', result, flags=re.MULTILINE)

        return result.strip()


def process_single_page(
    input_file: Path,
    output_file: Optional[Path] = None,
    verbose: bool = False,
) -> dict[str, Any]:
    """
    Process a single wiki page JSON file.

    Args:
        input_file: Path to input JSON file
        output_file: Optional path for output JSON file
        verbose: Print progress information

    Returns:
        Parsed page data dictionary
    """
    parser = WikiParser(verbose=verbose)

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if verbose:
        print(f"Parsing: {data.get('title', input_file.name)}")

    # Parse the content
    parsed_content = parser.parse_page(data.get("content", ""))

    # Build result with metadata
    result = {
        "title": data.get("title", ""),
        "pageid": data.get("pageid"),
        "timestamp": data.get("timestamp"),
        "categories": data.get("categories", []),
        **parsed_content,
    }

    # Write output if specified
    if output_file:
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        if verbose:
            print(f"  -> {output_file}")

    return result


def process_all_pages(
    input_dir: Path,
    output_dir: Path,
    verbose: bool = False,
) -> list[dict[str, Any]]:
    """
    Process all wiki page JSON files in a directory.

    Args:
        input_dir: Directory containing input JSON files
        output_dir: Directory for output JSON files
        verbose: Print progress information

    Returns:
        List of all parsed page data dictionaries
    """
    input_pages_dir = input_dir / "pages"
    output_pages_dir = output_dir / "pages"
    output_pages_dir.mkdir(parents=True, exist_ok=True)

    all_parsed = []
    json_files = list(input_pages_dir.glob("*.json"))

    if verbose:
        print(f"Found {len(json_files)} pages to process")

    for json_file in sorted(json_files):
        output_file = output_pages_dir / json_file.name
        try:
            result = process_single_page(json_file, output_file, verbose=verbose)
            all_parsed.append(result)
        except Exception as e:
            print(f"Error processing {json_file.name}: {e}", file=sys.stderr)
            continue

    # Write combined JSONL file
    jsonl_output = output_dir / "stellaris_4.2_parsed.jsonl"
    with open(jsonl_output, "w", encoding="utf-8") as f:
        for page in all_parsed:
            f.write(json.dumps(page, ensure_ascii=False) + "\n")

    if verbose:
        print(f"\nProcessed {len(all_parsed)} pages")
        print(f"Output directory: {output_dir}")
        print(f"Combined JSONL: {jsonl_output}")

    return all_parsed


def main():
    """Main entry point for the parser."""
    argparser = argparse.ArgumentParser(
        description="Parse Stellaris Wiki wikitext into structured JSON",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse all pages in output_4.2
  python parser.py --input ./output_4.2 --output ./output_parsed

  # Parse a single page for testing
  python parser.py --input ./output_4.2/pages/Machine_traits.json --test

  # Verbose output
  python parser.py --input ./output_4.2 --output ./output_parsed -v
        """,
    )

    argparser.add_argument(
        "--input", "-i",
        type=Path,
        required=True,
        help="Input directory (containing pages/) or single JSON file",
    )
    argparser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("output_parsed"),
        help="Output directory (default: output_parsed)",
    )
    argparser.add_argument(
        "--test", "-t",
        action="store_true",
        help="Test mode: parse single file and print to stdout",
    )
    argparser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output",
    )

    args = argparser.parse_args()

    if args.test:
        # Test mode: parse single file and print result
        if args.input.is_file():
            result = process_single_page(args.input, verbose=args.verbose)
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(f"Error: {args.input} is not a file", file=sys.stderr)
            sys.exit(1)
    else:
        # Normal mode: process all pages
        if not args.input.exists():
            print(f"Error: Input path does not exist: {args.input}", file=sys.stderr)
            sys.exit(1)

        if args.input.is_file():
            # Single file
            output_file = args.output / args.input.name
            process_single_page(args.input, output_file, verbose=args.verbose)
        else:
            # Directory
            process_all_pages(args.input, args.output, verbose=args.verbose)

    print("\nDone!", file=sys.stderr if not args.test else sys.stdout)


if __name__ == "__main__":
    main()
