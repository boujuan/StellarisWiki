"""
Template resolver for Stellaris Wiki wikitext.

Maps wiki templates to clean, readable text for LLM consumption.
"""

from typing import Callable, Optional
import re


# Template mappings: template_name -> function(params) -> clean_text
# params is a list of positional arguments from the template

TEMPLATE_MAPPINGS: dict[str, Callable[[list[str]], str]] = {
    # Icon templates - convert to bracketed text or just the name
    "icon": lambda p: f"[{p[0]}]" if p else "",
    "iconify": lambda p: p[0] if p else "",
    "multi icon": lambda p: "[" + ", ".join(p) + "]" if p else "",
    "icon link": lambda p: f"[{p[1] if len(p) > 1 else p[0]}]" if p else "",

    # Color formatting - just extract the text value
    "green": lambda p: p[0] if p else "",
    "red": lambda p: p[0] if p else "",
    "yellow": lambda p: p[0] if p else "",
    "blue": lambda p: p[0] if p else "",
    "grey": lambda p: p[0] if p else "",
    "gray": lambda p: p[0] if p else "",
    "white": lambda p: p[0] if p else "",
    "orange": lambda p: p[0] if p else "",

    # Description/formatting templates
    "desc small": lambda p: p[0] if p else "",
    "desc": lambda p: p[0] if p else "",
    "tooltip": lambda p: p[0] if p else "",  # Show main text, ignore hover
    "abbr": lambda p: p[0] if p else "",
    "small": lambda p: p[0] if p else "",
    "nowrap": lambda p: p[0] if p else "",

    # DLC/Expansion markers
    "expansion": lambda p: f"[{p[0].upper()} DLC]" if p else "",

    # Version and navigation templates - strip completely
    "version": lambda p: "",
    "traitnav": lambda p: "",
    "conceptsnavbox": lambda p: "",
    "navbox": lambda p: "",
    "main": lambda p: "",
    "see also": lambda p: "",
    "stub": lambda p: "",
    "outdated": lambda p: "",
    "todo": lambda p: "",
    "verify": lambda p: "",
    "clarify": lambda p: "",
    "citation needed": lambda p: "",

    # Trait template - extracts trait name and optionally icon
    "trait": lambda p: f"[{p[0]}]" if p else "",

    # Tradition template
    "tradition": lambda p: f"[{p[0]}]" if p else "",

    # Collapse list - extract content
    "collapse list": lambda p: p[0] if p else "",
    "collapse": lambda p: p[0] if p else "",

    # File references - handled specially in resolve_template()
    # Links to anchors
    "anchor": lambda p: "",

    # Tables and formatting
    "clear": lambda p: "",
    "br": lambda p: "\n",
    "sic": lambda p: p[0] if p else "",

    # Math and special characters
    "e": lambda p: "×10^" + (p[0] if p else ""),
    "x": lambda p: "×",
    "times": lambda p: "×",
    "plusminus": lambda p: "±",

    # Game-specific icons as plain text
    "yes": lambda p: "Yes",
    "no": lambda p: "No",
    "partial": lambda p: "Partial",
    "maybe": lambda p: "Maybe",
    "unknown": lambda p: "Unknown",

    # Effect modifiers
    "modifier": lambda p: p[0] if p else "",
    "effect": lambda p: p[0] if p else "",

    # Quote/citation templates
    "quote": lambda p: f'"{p[0]}"' if p else "",
    "cquote": lambda p: f'"{p[0]}"' if p else "",
}

# Templates that should be completely stripped (return empty string)
STRIP_TEMPLATES = {
    "traitnav", "conceptsnavbox", "navbox", "version", "stub",
    "outdated", "todo", "verify", "clarify", "anchor", "clear",
    "main", "see also", "hatnote", "portal", "commons category",
    "reflist", "notelist", "col-begin", "col-end", "col-break",
    "div col", "div col end", "columns-list", "refbegin", "refend",
    "efn", "sfn", "r", "rp", "citation needed",
}

# Case-insensitive template name normalization
def normalize_template_name(name: str) -> str:
    """Normalize template name for lookup."""
    return name.strip().lower().replace("_", " ")


def get_template_params(template) -> list[str]:
    """
    Extract positional parameters from a wikitextparser template.
    Returns list of string values.
    """
    params = []
    for arg in template.arguments:
        # Get argument name and value
        name = arg.name.strip() if arg.name else None
        value = str(arg.value).strip() if arg.value else ""

        # Positional arguments have numeric or empty names
        if name is None or name == "" or name.isdigit():
            params.append(value)

    return params


def resolve_template(template) -> str:
    """
    Convert a wikitextparser template to clean text.

    Args:
        template: A wikitextparser Template object

    Returns:
        Clean text representation of the template
    """
    name = normalize_template_name(str(template.name))
    params = get_template_params(template)

    # Check if it should be completely stripped
    if name in STRIP_TEMPLATES:
        return ""

    # Check for direct mapping
    if name in TEMPLATE_MAPPINGS:
        try:
            return TEMPLATE_MAPPINGS[name](params)
        except (IndexError, TypeError):
            return ""

    # Handle icon variants (icon|xxx, iconify|xxx, etc.)
    if name.startswith("icon"):
        return f"[{params[0]}]" if params else ""

    # Handle color variants
    color_names = {"green", "red", "yellow", "blue", "grey", "gray", "white", "orange", "purple", "cyan"}
    if name in color_names:
        return params[0] if params else ""

    # Handle DLC-specific templates (often formatted as {{dlc|name}})
    if name in {"dlc", "expansion", "required dlc"}:
        return f"[{params[0].upper()} DLC]" if params else ""

    # Default: return first parameter or empty string
    # This handles many simple wrapper templates
    if params:
        return params[0]

    return ""


def clean_templates_from_text(text: str) -> str:
    """
    Clean all templates from wikitext, replacing them with resolved values.
    This is a helper that uses wikitextparser to parse and resolve templates.

    Note: This function is typically called by parser.py which handles
    the full wikitextparser integration.
    """
    import wikitextparser as wtp

    parsed = wtp.parse(text)
    result = text

    # Process templates from innermost to outermost to handle nesting
    for template in reversed(parsed.templates):
        resolved = resolve_template(template)
        result = result.replace(str(template), resolved, 1)

    return result


# Additional patterns for post-processing after template resolution
def clean_wiki_markup(text: str) -> str:
    """
    Clean remaining wiki markup after template resolution.
    Handles links, formatting, etc.
    """
    # Remove file/image links but not their alt text
    # [[File:Example.png|24px|link=Something|Alt text]] -> Alt text (if present) or ""
    text = re.sub(r'\[\[File:[^\]]*\]\]', '', text)
    text = re.sub(r'\[\[Image:[^\]]*\]\]', '', text)

    # Convert wiki links to plain text
    # [[Link|Display text]] -> Display text
    # [[Simple link]] -> Simple link
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)

    # Remove bold/italic markup
    text = re.sub(r"'''([^']+)'''", r'\1', text)  # '''bold''' -> bold
    text = re.sub(r"''([^']+)''", r'\1', text)    # ''italic'' -> italic

    # Clean up HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

    # Clean up HTML tags (simple cases)
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</?(?:div|span|p|ref|references|small|big|sup|sub|nowiki)[^>]*>', '', text, flags=re.IGNORECASE)

    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)

    return text.strip()


if __name__ == "__main__":
    # Simple test
    test_templates = [
        "{{icon|energy}}",
        "{{iconify|Unity}}",
        "{{green|+10%}}",
        "{{red|−20%}}",
        "{{expansion|utopia}}",
        "{{desc small|This is a description}}",
        "{{version|4.2}}",
    ]

    import wikitextparser as wtp

    print("Template resolver test:")
    for t in test_templates:
        parsed = wtp.parse(t)
        if parsed.templates:
            result = resolve_template(parsed.templates[0])
            print(f"  {t} -> '{result}'")
