#!/usr/bin/env python3
"""
HTML to Markdown converter for MediaWiki content.

This module converts MediaWiki's rendered HTML output to clean Markdown,
optimized for LLM consumption.
"""

import re
from bs4 import BeautifulSoup, NavigableString, Tag


def _extract_brace_group(s: str) -> tuple[str | None, str]:
    """Extract content of a {...} group from the start of string s.

    Returns (content, remainder) or (None, s) if no group found.
    """
    s = s.lstrip()
    if not s or s[0] != '{':
        return None, s
    depth = 0
    for i, c in enumerate(s):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[1:i], s[i+1:]
    return None, s


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
            '.infobox',              # Infoboxes (navigation)
            '.mw-headline-anchor',   # Headline anchors
            'table.navbox',          # Navigation boxes in table format
            '.navbox-inner',         # Inner navbox content
            '.tooltiptext',          # CSS hover tooltip popups
        ]

        # Table classes to skip (these are navigation, not data)
        self.skip_table_classes = {
            'navbox', 'navbox-inner', 'navbox-columns-table'
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

        # Pre-process component icons before images are stripped
        self._preprocess_component_icons(soup)

        # Flatten tabbed content into sequential sections
        self._preprocess_tabber(soup)

        # Convert math/LaTeX elements to plain text
        self._preprocess_math(soup)

        # Remove unwanted elements
        self._remove_unwanted(soup)

        # Preserve bold formatting in markdown
        self._preprocess_formatting(soup)

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
        result = re.sub(r'\n{3,}', '\n\n', result)
        result = re.sub(r' +', ' ', result)

        return result.strip()

    def _strip_html(self, text: str) -> str:
        """Strip HTML tags from text."""
        if '<' in text:
            soup = BeautifulSoup(text, 'lxml')
            return soup.get_text(strip=True)
        return text

    def _preprocess_component_icons(self, soup: BeautifulSoup) -> None:
        """Replace {{component}} template grid spans with plain text names.

        The wiki's {{component}} template renders as a 3-layer CSS grid of
        overlapping images. Since images are stripped later, we extract the
        component name and replace the entire grid span with text.
        """
        # Collect all grid spans and extract names before modifying tree
        grid_spans = []
        grid_span_set = set()
        for span in soup.find_all('span', style=True):
            style = span.get('style', '').replace(' ', '')
            if 'display:inlinegrid' in style:
                grid_spans.append(span)
                grid_span_set.add(id(span))

        # First pass: extract names and determine if decorative (before any replacements)
        replacements = []
        for span in grid_spans:
            component_name = None

            for a_tag in span.find_all('a'):
                title = a_tag.get('title')
                if title and 'File:' not in title:
                    component_name = title
                    break
            if not component_name:
                for img in span.find_all('img'):
                    alt = img.get('alt', '')
                    if alt and not alt.endswith('.png') and not alt.endswith('.jpg'):
                        component_name = alt
                        break
            if not component_name:
                for a_tag in span.find_all('a'):
                    href = a_tag.get('href', '')
                    if '#' in href and 'File:' not in href:
                        component_name = href.split('#')[-1].replace('_', ' ')
                        break

            # Check adjacent non-grid text to decide if decorative
            is_decorative = False
            if component_name:
                next_text = ''
                for sib in span.next_siblings:
                    if isinstance(sib, NavigableString):
                        text = str(sib).strip()
                        if text:
                            next_text = text
                            break
                    elif isinstance(sib, Tag) and id(sib) not in grid_span_set:
                        next_text = sib.get_text(strip=True)
                        break
                prev_text = ''
                for sib in span.previous_siblings:
                    if isinstance(sib, NavigableString):
                        text = str(sib).strip()
                        if text:
                            prev_text = text
                            break
                    elif isinstance(sib, Tag) and id(sib) not in grid_span_set:
                        prev_text = sib.get_text(strip=True)
                        break

                name_words = [w for w in component_name.lower().split() if len(w) > 2]
                adjacent = (prev_text + ' ' + next_text).lower()
                if name_words and all(w in adjacent for w in name_words):
                    is_decorative = True

            replacements.append((span, component_name, is_decorative))

        # Second pass: do all replacements
        for span, name, is_decorative in replacements:
            if is_decorative:
                span.replace_with(NavigableString(' '))
            elif name:
                span.replace_with(NavigableString(f'{name}, '))
            else:
                span.replace_with(NavigableString(''))

    def _preprocess_tabber(self, soup: BeautifulSoup) -> None:
        """Flatten tabbed content (MediaWiki Tabber extension) into sequential sections.

        Tabber renders as:
          <div class="tabber">
            <header class="tabber__header">...</header>
            <section class="tabber__section">
              <article class="tabber__panel" data-title="Tab1">...content...</article>
              <article class="tabber__panel" data-title="Tab2">...content...</article>
            </section>
          </div>

        We replace each tabber with the contents of all panels in sequence,
        with a bold label for each tab's title.
        """
        for tabber in list(soup.find_all('div', class_='tabber')):
            # Remove the JS-required header
            header = tabber.find('header', class_='tabber__header')
            if header:
                header.decompose()

            # Extract all tab panels
            panels = tabber.find_all('article', class_='tabber__panel')
            if not panels:
                continue

            # Replace the tabber div with the sequential panel contents
            # We'll build replacement nodes and insert them before the tabber
            for panel in panels:
                title = panel.get('data-title', '')

                # Add a bold label for the tab if there are multiple panels
                if title and len(panels) > 1:
                    label_tag = soup.new_tag('p')
                    label_tag.string = f'**{title}**'
                    tabber.insert_before(label_tag)

                # Move all children of the panel before the tabber
                for child in list(panel.children):
                    tabber.insert_before(child)

            tabber.decompose()

    def _preprocess_math(self, soup: BeautifulSoup) -> None:
        """Convert LaTeX math elements to readable plain text.

        MediaWiki's math extension renders <math> tags as SVG/MathML.
        When the renderer fails, error messages with raw LaTeX leak through.
        Even when it succeeds, the MathML/SVG is not useful in markdown.

        This handles two HTML patterns:
        1. Successful render: <span class="mwe-math-element"> with <annotation>
        2. Failed render: <strong class="error texerror">Failed to parse...{\displaystyle ...}
        """
        # Pattern 1: Successfully rendered math elements (inline <span> or block <div>)
        for el in list(soup.find_all(class_='mwe-math-element')):
            # Try to get LaTeX from <annotation> tag first
            ann = el.find('annotation', encoding='application/x-tex')
            if ann and ann.string:
                latex = ann.string.strip()
            else:
                # Fallback: extract from alt attribute on the fallback <img>
                img = el.find('img', class_='mwe-math-fallback-image-inline')
                if img and img.get('alt'):
                    latex = img['alt'].strip()
                else:
                    # Last resort: get raw text and try to find LaTeX
                    text = el.get_text()
                    match = re.search(r'\{\\displaystyle\s+(.*)\}', text)
                    if match:
                        latex = match.group(0)
                    else:
                        continue

            plain = self._latex_to_plain(latex)
            # Block-level math (div) needs wrapping in <p> so the converter
            # picks it up; inline math (span) can stay as NavigableString
            if el.name == 'div':
                p_tag = soup.new_tag('p')
                p_tag.string = plain
                el.replace_with(p_tag)
            else:
                el.replace_with(NavigableString(plain))

        # Pattern 2: Failed math renders — error messages with embedded LaTeX
        for el in list(soup.find_all('strong', class_='error')):
            text = el.get_text()
            if 'Failed to parse' not in text:
                continue
            match = re.search(r'(\{\\displaystyle\s+.*\})\s*$', text)
            if match:
                latex = match.group(1)
                plain = self._latex_to_plain(latex)
                el.replace_with(NavigableString(plain))

    def _latex_to_plain(self, latex: str) -> str:
        """Convert a LaTeX math expression to readable plain text.

        Handles the subset of LaTeX used on the Stellaris wiki:
        fractions, text labels, operators, superscripts, subscripts.
        """
        s = latex

        # Strip outer \displaystyle wrapper
        s = re.sub(r'^\{\\displaystyle\s*', '', s)
        s = re.sub(r'\}$', '', s)

        # Strip aligned/array environments — flatten to single line
        s = re.sub(r'\\begin\{aligned\}', '', s)
        s = re.sub(r'\\end\{aligned\}', '', s)
        s = re.sub(r'\\begin\{array\}(\{[^}]*\})?', '', s)
        s = re.sub(r'\\end\{array\}', '', s)
        # Alignment markers: & = column separator, \\ = row separator
        s = re.sub(r'\\\\', ' ; ', s)
        s = s.replace('&', ' ')

        # \text{...} -> contents
        s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
        # \textbf{...} -> contents
        s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)

        # Process \frac iteratively (may appear multiple times)
        while r'\frac' in s:
            pos = s.find(r'\frac')
            rest = s[pos + len(r'\frac'):]
            num, after_num = _extract_brace_group(rest)
            den, after_den = _extract_brace_group(after_num)
            if num is not None and den is not None:
                num_plain = self._latex_to_plain('{' + num + '}')
                den_plain = self._latex_to_plain('{' + den + '}')
                num_simple = not any(c in num_plain for c in '+-')
                den_simple = not any(c in den_plain for c in '+-')
                num_str = num_plain if num_simple else f'({num_plain})'
                den_str = den_plain if den_simple else f'({den_plain})'
                s = s[:pos] + num_str + ' / ' + den_str + after_den
            else:
                break

        # \tfrac same as \frac
        while r'\tfrac' in s:
            pos = s.find(r'\tfrac')
            rest = s[pos + len(r'\tfrac'):]
            num, after_num = _extract_brace_group(rest)
            den, after_den = _extract_brace_group(after_num)
            if num is not None and den is not None:
                num_plain = self._latex_to_plain('{' + num + '}')
                den_plain = self._latex_to_plain('{' + den + '}')
                num_simple = not any(c in num_plain for c in '+-')
                den_simple = not any(c in den_plain for c in '+-')
                num_str = num_plain if num_simple else f'({num_plain})'
                den_str = den_plain if den_simple else f'({den_plain})'
                s = s[:pos] + num_str + ' / ' + den_str + after_den
            else:
                break

        # Operators
        s = s.replace(r'\cdot', ' * ')
        s = s.replace(r'\times', ' * ')
        s = s.replace(r'\div', ' / ')
        s = s.replace(r'\pm', ' +/- ')
        s = s.replace(r'\leq', ' <= ')
        s = s.replace(r'\geq', ' >= ')
        s = s.replace(r'\neq', ' != ')
        s = s.replace(r'\approx', ' ~ ')
        s = s.replace(r'\sum', 'Sum')

        # Spacing commands
        s = s.replace(r'\,', ' ')
        s = s.replace(r'\;', ' ')
        s = s.replace(r'\:', ' ')
        s = s.replace(r'\!', '')
        s = s.replace(r'\quad', '  ')
        s = s.replace(r'\qquad', '   ')
        s = s.replace(r'\ ', ' ')

        # Delimiters
        s = s.replace(r'\left(', '(')
        s = s.replace(r'\right)', ')')
        s = s.replace(r'\left[', '[')
        s = s.replace(r'\right]', ']')
        s = s.replace(r'\left\{', '{')
        s = s.replace(r'\right\}', '}')
        s = s.replace(r'\left.', '')
        s = s.replace(r'\right.', '')

        # Escaped characters
        s = s.replace(r'\%', '%')
        s = s.replace(r'\_', '_')
        s = s.replace(r'\&', '&')

        # Superscripts: ^{...} -> ^(...)
        s = re.sub(r'\^\{([^}]*)\}', r'^(\1)', s)
        # Simple superscript: ^x (single char)
        # (leave as-is, e.g. n^2 is readable)

        # Subscripts: _{...} -> _text
        s = re.sub(r'_\{([^}]*)\}', r'_\1', s)

        # Remaining braces used for grouping — remove them
        s = re.sub(r'(?<!\\)\{', '', s)
        s = re.sub(r'(?<!\\)\}', '', s)

        # Any remaining backslash commands we missed — strip the backslash
        s = re.sub(r'\\([a-zA-Z]+)', r'\1', s)

        # Normalize spacing around operators
        s = re.sub(r'\s*=\s*', ' = ', s)
        s = re.sub(r'\s*(?<![(\[,])\+\s*', ' + ', s)
        s = re.sub(r'\s*(?<![(\[,])-\s*', ' - ', s)

        # Clean up whitespace
        s = re.sub(r'\s+', ' ', s).strip()

        return s

    def _preprocess_formatting(self, soup: BeautifulSoup) -> None:
        """Preserve bold formatting from HTML as markdown **bold** markers.

        Handles three patterns:
        1. Elements with font-size:larger + font-weight:bold (civic/item names)
        2. <div> with font-weight:bold only (tradition/building names)
        3. <b> and <strong> tags (labels, inline bold text)

        Skips <span> with font-weight:bold (modifier values like "+10%").
        """
        # 1 & 2. Styled bold elements
        for el in list(soup.find_all(style=True)):
            style = el.get('style', '').replace(' ', '').lower()
            if 'font-weight:bold' not in style:
                continue
            text = el.get_text(strip=True)
            if not text or len(text) > 200:
                continue
            # font-size:larger items (any tag) — civic/item names
            if 'font-size:larger' in style:
                el.clear()
                el.append(NavigableString(f'**{text}**'))
            # <div> with font-weight:bold — tradition/building names
            # Skip short numeric/modifier values
            elif el.name == 'div' and len(text) > 2 and not text.lstrip('−+-').replace('.', '').replace('%', '').isdigit():
                el.clear()
                el.append(NavigableString(f'**{text}**'))

        # 3. <b> and <strong> tags
        for tag in list(soup.find_all(['b', 'strong'])):
            text = tag.get_text(strip=True)
            if text:
                tag.replace_with(NavigableString(f'**{text}**'))
            else:
                tag.decompose()

    def _remove_unwanted(self, soup: BeautifulSoup) -> None:
        """Remove navigation, edit links, references, etc."""
        for selector in self.remove_selectors:
            for el in soup.select(selector):
                el.decompose()

        # Remove navigation footers (inline-styled divs with border, no class)
        # These are "Game concepts", "Modding", and "Stellaris" nav bars
        for div in list(soup.find_all('div', style=True)):
            if not div.attrs:
                continue
            style = div.get('style', '')
            if 'border: 1px solid #aaa' in style and 'text-align: center' in style:
                div.decompose()

        # Unwrap tooltip wrapper divs — they're inline containers whose
        # popup content (tooltiptext) was already stripped above
        for tooltip in list(soup.find_all('div', class_='tooltip')):
            tooltip.unwrap()

        # Process images: replace with alt text when it carries meaning,
        # strip decorative icons that duplicate adjacent text
        for img in list(soup.find_all('img')):
            alt = img.get('alt', '')

            # Always strip decorative/background images
            if not alt or any(skip in alt.lower() for skip in [
                'slot bg', 'slot_bg', 'slot frame', 'slot_frame',
                'menu icon', 'event button', 'leader trait bg',
                'pm frame', 'pm_frame',
            ]):
                img.decompose()
                continue

            # Clean alt text
            label = re.sub(r'\.(png|jpg|gif)$', '', alt, flags=re.IGNORECASE)
            label = label.replace('_', ' ').strip()

            if not label:
                img.decompose()
                continue

            # Check if image is inside a link that has nearby text context
            parent_a = img.find_parent('a')
            if parent_a:
                # If the <a> has a title or adjacent text, the icon is decorative
                if parent_a.get('title'):
                    img.decompose()
                    continue
                # Check if parent element already has text that covers this
                parent_el = parent_a.parent
                if parent_el:
                    sibling_text = ''
                    for sib in parent_el.children:
                        if isinstance(sib, NavigableString):
                            sibling_text += str(sib)
                        elif isinstance(sib, Tag) and sib != parent_a:
                            sibling_text += sib.get_text()
                    if sibling_text.strip():
                        img.decompose()
                        continue

            # Replace with text — this image carries unique meaning
            img.replace_with(NavigableString(label))

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
        classes = table.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()

        # Skip navbox tables
        if any(c in self.skip_table_classes for c in classes):
            return ''

        # If this table contains event outliner boxes (mildtable layout),
        # extract and convert the events instead of rendering as a table
        event_outliners = table.find_all('div', class_='stellaris-outliner')
        if event_outliners:
            parts = []
            for outliner in event_outliners:
                md = self._convert_stellaris_outliner(outliner)
                if md:
                    parts.append(md)
            return '\n'.join(parts)

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
        classes = el.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()

        # Classes to skip entirely (don't process children)
        skip_entirely = {
            'navbox', 'toc', 'infobox',
            'mw-references-wrap', 'catlinks', 'printfooter'
        }
        if any(c in skip_entirely for c in classes):
            return ''

        # Handle stellaris-outliner: version/nav boxes are skipped, event boxes are kept
        if 'stellaris-outliner' in classes:
            return self._convert_stellaris_outliner(el)

        # Check if div has any block-level children
        block_tags = {
            'p', 'div', 'table', 'ul', 'ol', 'dl',
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'pre', 'blockquote', 'hr',
        }
        has_block_children = any(
            isinstance(child, Tag) and child.name in block_tags
            for child in el.children
        )

        if not has_block_children:
            # Inline-only div — treat as a paragraph
            text = self._get_text(el)
            if text.strip():
                return f"\n{text}\n"
            return ''

        # Has block-level children — process them, but also capture
        # inline content that appears between block elements
        md_parts = []
        inline_buffer = []

        for child in el.children:
            if isinstance(child, Tag) and child.name in block_tags:
                # Flush any accumulated inline content first
                if inline_buffer:
                    inline_text = ' '.join(filter(None, inline_buffer))
                    inline_text = re.sub(r'\s+', ' ', inline_text).strip()
                    if inline_text:
                        md_parts.append(f"\n{inline_text}\n")
                    inline_buffer = []
                # Process block element
                md = self._convert_element(child)
                if md:
                    md_parts.append(md)
            elif isinstance(child, Tag):
                # Inline tag — buffer its text
                text = self._get_text(child)
                if text:
                    inline_buffer.append(text)
            elif isinstance(child, NavigableString):
                text = str(child).strip()
                if text:
                    inline_buffer.append(text)

        # Flush remaining inline content
        if inline_buffer:
            inline_text = ' '.join(filter(None, inline_buffer))
            inline_text = re.sub(r'\s+', ' ', inline_text).strip()
            if inline_text:
                md_parts.append(f"\n{inline_text}\n")

        return '\n'.join(md_parts)

    def _convert_stellaris_outliner(self, el: Tag) -> str:
        """Convert a stellaris-outliner div, distinguishing navigation from event content."""
        header_div = el.find('div', class_='stellaris-outliner-header')
        header_text = header_div.get_text(strip=True) if header_div else ''

        # Skip version/status boxes
        if header_text.lower() in ('version', ''):
            return ''

        # Skip navigation infoboxes (they contain infobox-row elements)
        if el.find('div', class_='infobox-row'):
            return ''

        # This is an event content box — convert it
        return self._convert_event_box(el, header_text)

    def _convert_event_box(self, el: Tag, event_name: str) -> str:
        """Convert an event content box to structured Markdown."""
        parts = [f"\n### Event: {event_name}\n"]

        content_div = el.find('div', class_='stellaris-outliner-content')
        if not content_div:
            return ''

        # Extract event flavor text (plain divs before the hr/collapsible)
        for child in content_div.children:
            if isinstance(child, Tag):
                if child.name == 'hr':
                    continue
                if 'mw-collapsible' in child.get('class', []):
                    # Extract trigger conditions and options from the collapsible
                    parts.append(self._convert_event_details(child))
                    continue
                # Plain div with event text
                text = self._get_text(child)
                if text:
                    parts.append(f"\n{text}\n")

        return '\n'.join(filter(None, parts))

    def _convert_event_details(self, collapsible: Tag) -> str:
        """Extract trigger conditions, MTTH, and options from an event's collapsible section."""
        content = collapsible.find('div', class_='mw-collapsible-content')
        if not content:
            content = collapsible

        table = content.find('table')
        if not table:
            text = self._get_text(content)
            return f"\n{text}\n" if text else ''

        parts = []

        # Extract trigger conditions and MTTH from subheading spans
        for subheading in table.find_all('span', class_='subheading'):
            label = subheading.get_text(strip=True)
            # Get the parent cell and extract content after the subheading
            cell = subheading.find_parent('td')
            if not cell:
                continue
            # Collect text from siblings after the subheading
            detail_parts = []
            for sibling in subheading.find_next_siblings():
                if sibling.name == 'span' and 'subheading' in sibling.get('class', []):
                    break
                text = self._get_text(sibling)
                if text:
                    detail_parts.append(text)
            detail = ' '.join(detail_parts)
            if label and detail:
                parts.append(f"\n**{label}** {detail}\n")
            elif label:
                parts.append(f"\n**{label}**\n")

        # Also handle subheading in div form (some events use <div class="subheading">)
        for subheading_div in table.find_all('div', class_='subheading'):
            text = subheading_div.get_text(strip=True)
            if text and not any(text in p for p in parts):
                parts.append(f"\n**{text}**\n")

        # Extract options: div.option_title contains the choice text,
        # followed by <ul> with effects
        for option_title in table.find_all('div', class_='option_title'):
            choice_text = self._get_text(option_title)
            if not choice_text:
                continue

            option_parts = [f"- **Option:** {choice_text}"]

            # Check for "Enabled if:" condition before this option
            # Walk backwards from the option's parent div to find a preceding <p> with conditions
            option_wrapper = option_title.find_parent('div', style=True)
            if option_wrapper:
                # Check for condition <p> before the wrapper or its parent margin div
                container = option_wrapper.parent
                if container and container.get('style', '').startswith('margin'):
                    # Look for <p> with "Enabled if:" before this container
                    prev = container.find_previous_sibling('p')
                    if prev:
                        cond_text = self._get_text(prev)
                        if 'Enabled if:' in cond_text:
                            option_parts.append(f"  - *Condition:* {cond_text}")

                # Collect effect <ul> elements after the option div
                for sibling in option_wrapper.find_next_siblings():
                    if isinstance(sibling, Tag):
                        if sibling.name == 'ul':
                            effects = self._convert_effect_list(sibling)
                            if effects:
                                option_parts.append(effects)
                        elif sibling.name == 'hr':
                            break
                        elif sibling.name == 'div' and 'option_button' in ' '.join(sibling.get('class', [])):
                            break
                        elif sibling.name == 'div' and sibling.find('div', class_='option_title'):
                            break
                        elif sibling.name == 'p':
                            text = self._get_text(sibling)
                            if text:
                                option_parts.append(f"  - {text}")

            parts.append('\n'.join(option_parts))

        # Fallback: if no options or subheadings found, extract all text
        if not parts:
            for row in table.find_all('tr'):
                for cell in row.find_all(['td', 'th']):
                    text = self._get_text(cell)
                    if text:
                        parts.append(f"\n{text}\n")

        return '\n'.join(filter(None, parts))

    def _convert_effect_list(self, ul: Tag, indent: int = 1) -> str:
        """Convert a <ul> of effects to indented markdown list."""
        items = []
        prefix = '  ' * indent
        for li in ul.find_all('li', recursive=False):
            # Get direct text (not from nested lists)
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
                items.append(f"{prefix}- {text}")
            for nested in nested_lists:
                nested_md = self._convert_effect_list(nested, indent + 1)
                if nested_md:
                    items.append(nested_md)
        return '\n'.join(items)

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

        # Clean up trailing comma from component icon preprocessing
        text = text.strip().rstrip(',').strip()

        return text

    def _get_cell_text(self, el: Tag) -> str:
        """Get text for table cell, preserving list structure with <br> separators."""
        # Check if cell contains any list elements
        lists = el.find_all(['ul', 'ol'])

        if not lists:
            # No lists — use standard text extraction
            text = self._get_text(el)
            text = text.replace('|', '\\|')
            text = text.replace('\n', ' ')
            text = re.sub(r'\s+', ' ', text)
            return text.strip()

        # Cell contains lists — process preserving structure
        parts = []
        for child in el.children:
            if isinstance(child, Tag) and child.name in ['ul', 'ol']:
                items = self._get_list_items_for_cell(child)
                parts.extend(items)
            elif isinstance(child, Tag):
                # Check if wrapper contains a list
                inner_lists = child.find_all(['ul', 'ol'])
                if inner_lists:
                    for inner_child in child.children:
                        if isinstance(inner_child, Tag) and inner_child.name in ['ul', 'ol']:
                            parts.extend(self._get_list_items_for_cell(inner_child))
                        elif isinstance(inner_child, Tag):
                            text = self._get_text(inner_child)
                            if text.strip():
                                parts.append(text.strip())
                        elif isinstance(inner_child, NavigableString):
                            text = str(inner_child).strip()
                            if text:
                                parts.append(text)
                else:
                    text = self._get_text(child)
                    if text.strip():
                        parts.append(text.strip())
            elif isinstance(child, NavigableString):
                text = str(child).strip()
                if text:
                    parts.append(text)

        result = '<br>'.join(parts)
        result = result.replace('|', '\\|')
        result = re.sub(r' +', ' ', result)
        return result.strip()

    def _get_list_items_for_cell(self, list_el: Tag, indent: int = 0) -> list:
        """Extract list items for use in table cells with <br> separators."""
        items = []
        indent_prefix = '\u00a0\u00a0' * indent  # Non-breaking spaces for indent

        for i, li in enumerate(list_el.find_all('li', recursive=False)):
            marker = '-' if list_el.name == 'ul' else f'{i+1}.'

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
                items.append(f"{indent_prefix}{marker} {text}")

            for nested in nested_lists:
                items.extend(self._get_list_items_for_cell(nested, indent + 1))

        return items


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
