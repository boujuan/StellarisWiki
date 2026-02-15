#!/usr/bin/env python3
"""
HTML to Markdown converter for MediaWiki content.

This module converts MediaWiki's rendered HTML output to clean Markdown,
optimized for LLM consumption.
"""

import re
from bs4 import BeautifulSoup, NavigableString, Tag


class HTMLToMarkdown:
    """Convert MediaWiki HTML to clean Markdown."""

    def __init__(self):
        # Elements to completely remove
        self.remove_selectors = [
            '.mw-editsection',       # Edit section links
            '.navbox',               # Navigation boxes
            '.references',           # Reference sections
            '.toc',                  # Table of contents
            '.noprint',              # Non-printable elements
            '.mw-empty-elt',         # Empty elements
            '.reference',            # Inline reference markers
            'script',                # Scripts
            'style',                 # Styles
            'sup.reference',         # Reference superscripts
            '.magnify',              # Image magnify buttons
            '.thumbcaption',         # Image captions (often noise)
            '.metadata',             # Metadata boxes
            '.ambox',                # Article message boxes
            '.sistersitebox',        # Sister site boxes
            '.mbox-small',           # Small message boxes
            '.vertical-navbox',      # Vertical navigation
            '.infobox-navbox-below', # Infobox nav
            'noscript',              # Noscript content
            '.stellaris-outliner',   # Stellaris wiki outliner boxes
            '.infobox',              # Infoboxes (navigation)
            '.mw-headline-anchor',   # Headline anchors
            'table.navbox',          # Navigation boxes in table format
            '.navbox-inner',         # Inner navbox content
            '.collapsible',          # Collapsible navbox elements
        ]

        # Table classes to skip (these are navigation, not data)
        self.skip_table_classes = {
            'navbox', 'navbox-inner', 'collapsible', 'autocollapse',
            'mw-collapsible', 'navbox-columns-table'
        }

    def convert(self, html: str, title: str) -> str:
        """Convert full page HTML to Markdown.

        Args:
            html: The HTML content from MediaWiki action=parse API
            title: The page title

        Returns:
            Clean Markdown string
        """
        soup = BeautifulSoup(html, 'lxml')

        # Remove unwanted elements
        self._remove_unwanted(soup)

        # Clean title (remove HTML tags)
        clean_title = self._strip_html(title)

        # Build markdown content
        md_parts = [f"# {clean_title}\n"]

        # Find the main content container
        content = soup.find('div', class_='mw-parser-output')
        if not content:
            # Fallback to body or entire soup
            content = soup.find('body') or soup

        # Process all content elements
        stop_processing = False
        for element in content.children:
            if isinstance(element, Tag):
                # Stop at References section (typically just navigation after this)
                if element.name in ['h2', 'h3'] and self._get_text(element).lower() in ['references', 'see also', 'external links']:
                    stop_processing = True
                    break
                md = self._convert_element(element)
                if md:
                    md_parts.append(md)

        result = '\n'.join(filter(None, md_parts))

        # Clean up excessive whitespace
        result = re.sub(r'\n{4,}', '\n\n\n', result)
        result = re.sub(r' +', ' ', result)

        return result.strip()

    def _strip_html(self, text: str) -> str:
        """Strip HTML tags from text."""
        if '<' in text:
            soup = BeautifulSoup(text, 'lxml')
            return soup.get_text(strip=True)
        return text

    def _remove_unwanted(self, soup: BeautifulSoup) -> None:
        """Remove navigation, edit links, references, etc."""
        for selector in self.remove_selectors:
            for el in soup.select(selector):
                el.decompose()

        # Remove image elements (keep alt text if processing text)
        for img in soup.find_all('img'):
            # Just remove images entirely for cleaner output
            img.decompose()

        # Remove audio/video
        for el in soup.find_all(['audio', 'video', 'source']):
            el.decompose()

    def _convert_element(self, el: Tag) -> str:
        """Convert single HTML element to Markdown."""
        if not isinstance(el, Tag):
            return ''

        tag_name = el.name

        if tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            return self._convert_header(el)
        elif tag_name == 'p':
            return self._convert_paragraph(el)
        elif tag_name in ['ul', 'ol']:
            return self._convert_list(el)
        elif tag_name == 'table':
            return self._convert_table(el)
        elif tag_name == 'dl':
            return self._convert_definition_list(el)
        elif tag_name == 'div':
            return self._convert_div(el)
        elif tag_name == 'pre':
            return self._convert_preformatted(el)
        elif tag_name == 'blockquote':
            return self._convert_blockquote(el)
        elif tag_name == 'hr':
            return '\n---\n'

        return ''

    def _convert_header(self, el: Tag) -> str:
        """Convert h1-h6 to Markdown headers."""
        level = int(el.name[1])  # h2 -> 2
        text = self._get_text(el)
        if not text.strip():
            return ''
        return f"\n{'#' * level} {text}\n"

    def _convert_paragraph(self, el: Tag) -> str:
        """Convert paragraph to Markdown."""
        text = self._get_text(el)
        if not text.strip():
            return ''
        return f"\n{text}\n"

    def _convert_table(self, table: Tag) -> str:
        """Convert HTML table to Markdown table."""
        # Skip navbox tables
        classes = table.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()
        if any(c in self.skip_table_classes for c in classes):
            return ''

        rows = table.find_all('tr')
        if not rows:
            return ''

        # Try to find header row
        header_row = rows[0]
        headers = []
        header_cells = header_row.find_all(['th', 'td'])

        for cell in header_cells:
            # Handle colspan
            colspan = int(cell.get('colspan', 1))
            text = self._get_cell_text(cell)
            headers.append(text)
            # Add empty columns for colspan
            for _ in range(colspan - 1):
                headers.append('')

        if not headers:
            return ''

        # Check if first row is actually headers (has th elements or is different style)
        has_th = len(header_row.find_all('th')) > 0
        data_start = 1 if has_th else 0

        # If no th elements, use first row as header anyway
        if not has_th and len(rows) > 0:
            data_start = 1

        # Build markdown table
        md_lines = []

        # Header row
        md_lines.append('| ' + ' | '.join(headers) + ' |')
        md_lines.append('|' + '|'.join(['---'] * len(headers)) + '|')

        # Data rows
        for row in rows[data_start:]:
            cells = row.find_all(['td', 'th'])
            values = []

            for cell in cells:
                colspan = int(cell.get('colspan', 1))
                text = self._get_cell_text(cell)
                values.append(text)
                for _ in range(colspan - 1):
                    values.append('')

            # Pad or trim to match header count
            while len(values) < len(headers):
                values.append('')
            values = values[:len(headers)]

            md_lines.append('| ' + ' | '.join(values) + ' |')

        return '\n' + '\n'.join(md_lines) + '\n'

    def _convert_list(self, el: Tag, indent: int = 0) -> str:
        """Convert ul/ol to Markdown list."""
        items = []
        prefix = '  ' * indent

        for i, li in enumerate(el.find_all('li', recursive=False)):
            marker = '-' if el.name == 'ul' else f'{i+1}.'

            # Get direct text content (not from nested lists)
            text_parts = []
            nested_lists = []

            for child in li.children:
                if isinstance(child, Tag) and child.name in ['ul', 'ol']:
                    nested_lists.append(child)
                elif isinstance(child, Tag):
                    text_parts.append(self._get_text(child))
                elif isinstance(child, NavigableString):
                    text_parts.append(str(child).strip())

            text = ' '.join(filter(None, text_parts))
            text = re.sub(r'\s+', ' ', text).strip()

            if text:
                items.append(f"{prefix}{marker} {text}")

            # Process nested lists
            for nested in nested_lists:
                nested_md = self._convert_list(nested, indent + 1)
                if nested_md:
                    items.append(nested_md)

        return '\n'.join(items) + '\n' if items else ''

    def _convert_definition_list(self, el: Tag) -> str:
        """Convert dl/dt/dd to Markdown."""
        items = []

        for child in el.children:
            if isinstance(child, Tag):
                if child.name == 'dt':
                    text = self._get_text(child)
                    if text:
                        items.append(f"**{text}**")
                elif child.name == 'dd':
                    text = self._get_text(child)
                    if text:
                        items.append(f": {text}")

        return '\n'.join(items) + '\n' if items else ''

    def _convert_div(self, el: Tag) -> str:
        """Convert div by processing its children."""
        # Check for special div classes that should be skipped entirely
        classes = el.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()

        # Classes to skip entirely (don't process children)
        skip_entirely = {
            'navbox', 'toc', 'stellaris-outliner', 'infobox',
            'mw-references-wrap', 'catlinks', 'printfooter'
        }
        if any(c in skip_entirely for c in classes):
            return ''

        # Process children
        md_parts = []
        for child in el.children:
            if isinstance(child, Tag):
                md = self._convert_element(child)
                if md:
                    md_parts.append(md)

        return '\n'.join(md_parts)

    def _convert_preformatted(self, el: Tag) -> str:
        """Convert pre/code blocks."""
        text = el.get_text()
        return f"\n```\n{text}\n```\n"

    def _convert_blockquote(self, el: Tag) -> str:
        """Convert blockquote to Markdown."""
        text = self._get_text(el)
        if not text:
            return ''
        lines = text.split('\n')
        quoted = '\n'.join(f'> {line}' for line in lines)
        return f"\n{quoted}\n"

    def _get_text(self, el: Tag) -> str:
        """Get clean text from element, preserving inline formatting."""
        if el is None:
            return ''

        # Get text with space separator
        text = el.get_text(separator=' ', strip=True)

        # Clean up whitespace
        text = re.sub(r'\s+', ' ', text)

        return text.strip()

    def _get_cell_text(self, el: Tag) -> str:
        """Get text for table cell, handling special formatting."""
        text = self._get_text(el)

        # Escape pipe characters in table cells
        text = text.replace('|', '\\|')

        # Replace newlines with spaces
        text = text.replace('\n', ' ')

        # Clean up multiple spaces
        text = re.sub(r'\s+', ' ', text)

        return text.strip()


def convert_html_to_markdown(html: str, title: str) -> str:
    """Convenience function to convert HTML to Markdown.

    Args:
        html: HTML content from MediaWiki
        title: Page title

    Returns:
        Markdown string
    """
    converter = HTMLToMarkdown()
    return converter.convert(html, title)


if __name__ == '__main__':
    # Simple test
    test_html = """
    <div class="mw-parser-output">
        <p>This is a test paragraph.</p>
        <h2>Section One</h2>
        <p>Some content here.</p>
        <table>
            <tr><th>Name</th><th>Value</th></tr>
            <tr><td>Foo</td><td>10</td></tr>
            <tr><td>Bar</td><td>20</td></tr>
        </table>
        <h2>Section Two</h2>
        <ul>
            <li>Item one</li>
            <li>Item two</li>
        </ul>
    </div>
    """

    result = convert_html_to_markdown(test_html, "Test Page")
    print(result)
