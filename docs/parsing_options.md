# Stellaris Wiki Parsing Options

## Overview

This document compares different approaches for parsing Stellaris Wiki content into clean, token-efficient formats for LLM consumption.

---

## Option 1: Wikitext Parser (Current Implementation)

**Status:** Implemented, but suboptimal results

### How It Works
- Fetch raw wikitext using `action=query&prop=revisions`
- Parse with `wikitextparser` library
- Manually resolve templates using `template_resolver.py`

### Pros
- Direct access to source markup
- Batch fetching (10+ pages per request)
- No re-fetching required (data already in `output_4.2/`)

### Cons
- **Templates leak through** - many templates not properly mapped
- **Output is LARGER** than input (11MB vs 4.3MB) due to JSON structure
- Requires maintaining comprehensive template mappings
- Complex nested templates fail to resolve

### Files
- `parser.py` - WikiParser class
- `template_resolver.py` - 50+ template mappings

---

## Option 2: HTML to Markdown (Recommended)

**Status:** Planned

### How It Works
1. Re-fetch pages using `action=parse` API (returns rendered HTML)
2. MediaWiki server expands ALL templates automatically
3. Convert HTML → clean Markdown using BeautifulSoup + custom logic

### Pros
- **Server-side template expansion** - no template mapping needed
- **Clean output** - all formatting artifacts handled by MediaWiki
- **Token efficient** - Markdown is compact
- **Table preservation** - can extract HTML tables perfectly

### Cons
- Requires re-fetching all 56 pages
- `action=parse` only handles ONE page per request (slower)
- Need HTML→Markdown conversion logic

### Libraries
```
beautifulsoup4>=4.11.0
lxml>=4.9.0  # Fast HTML parser
```

### API Parameters
```python
params = {
    "action": "parse",
    "page": "Page_Title",
    "prop": "text|sections|categories|displaytitle",
    "disabletoc": "true",
    "format": "json"
}
```

---

## Option 3: markdownify Library

**Status:** Alternative to Option 2

### How It Works
- Fetch HTML via `action=parse`
- Use `markdownify` library for automatic conversion

### Pros
- Minimal code - library handles conversion
- Good table support

### Cons
- Less control over output format
- Complex tables may lose structure
- Limited handling of MediaWiki-specific HTML

### Libraries
```
markdownify>=0.11.6
```

---

## Option 4: html2text Library

**Status:** Not Recommended

### How It Works
- Fetch HTML via `action=parse`
- Use `html2text` for conversion

### Pros
- Very clean text output
- Removes formatting artifacts well

### Cons
- **LOSES TABLE STRUCTURE** - converts tables to plain text
- Unsuitable for game data with tabular information
- Critical data loss for Stellaris content

---

## Comparison Matrix

| Criteria | Wikitext (Current) | HTML→MD (Recommended) | markdownify | html2text |
|----------|-------------------|----------------------|-------------|-----------|
| Template handling | Manual mapping | Server-side | Server-side | Server-side |
| Table preservation | Good | Excellent | Good | Poor |
| Token efficiency | Poor (larger output) | Excellent | Good | Good |
| Development effort | Done | Medium | Low | Low |
| Batch fetching | Yes (10+/request) | No (1/request) | No | No |
| Maintenance burden | High (templates) | Low | Low | Low |
| Output quality | Fair | Excellent | Good | Fair |

---

## Recommendation

**Use Option 2: HTML to Markdown with BeautifulSoup**

Reasons:
1. **Server-side template expansion** eliminates need to maintain template mappings
2. **Full control** over table extraction and formatting
3. **Token efficient** - Markdown is 50-70% smaller than JSON
4. **Clean output** - no wiki markup artifacts

The re-fetching cost (56 individual requests) is acceptable for a one-time parse operation.

---

## Output Format Comparison

### Raw Wikitext (Current Input)
```
{{icon|energy}} {{green|+10%}} Energy from Jobs
```
Size: ~50KB per page, ~4.3MB total

### Current JSON Output
```json
{
  "sections": {
    "Traits": {
      "content": "[energy] +10% Energy from Jobs",
      "tables": [{"headers": [...], "rows": [...]}]
    }
  }
}
```
Size: ~124KB per page, ~11MB total (WORSE)

### Target Markdown Output
```markdown
## Traits

| Name | Effect | Cost |
|------|--------|------|
| Efficient Processors | +10% Energy from Jobs | 3 |
```
Size: ~20KB per page, ~2MB total (BEST)
