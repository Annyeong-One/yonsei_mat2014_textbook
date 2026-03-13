# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

MkDocs Material documentation site for a book. Content is mathematical with LaTeX (MathJax) and includes Python example scripts.

## Build Commands

```bash
# Local development server with live reload
mkdocs serve

# Build static site (used in CI with --strict)
mkdocs build
mkdocs build --strict

# Install dependencies
pip install -r requirements.txt
```

## Deployment

GitHub Actions (`.github/workflows/deploy-mkdocs.yml`) auto-deploys to GitHub Pages on push to `main`. Build uses `--strict` mode, so all warnings are errors.

## Repository Structure

```
book_name/
├── CLAUDE.md
├── README.md
├── mkdocs.yml
├── requirements.txt
├── .github/
│   └── workflows/
│       └── deploy-mkdocs.yml
└── docs/
    ├── index.md
    ├── assets/
    │   └── favicon.ico
    ├── stylesheets/
    │   └── extra.css
    ├── javascripts/
    │   └── mathjax.js
    └── chapter_name/
        ├── index.md
        └── section_name/
            ├── topic.md
            ├── topic.py
            ├── module/        
            │   ├── __init__.py
            │   └── module.py
            └── figures/
                ├── fig_name.png
                └── another_fig_name.svg
```

## Navigation Structure in mkdocs.yml

The nav is organized as: **Parts → Chapters → Sections → Pages**. Each chapter typically has numbered subsections. Nav entries must point to `.md` files and `.py` files only.

Example nav entry:
```yaml
nav:
  - I Part Title:
    - 1 Chapter Title:
      - Chapter Overview: ch01/index.md
      - 1.1 Section Title:
        - Topic Title: ch01/section_title/topic_title.md
        - Another Topic Title: ch01/section_title/another_topic_title.py
```

YAML quoting rules for nav titles:
- Quote any title containing `:`, `#`, `*`, `&`, or other special characters
- Example: `'Black-Scholes Model #1'` not `Black-Scholes Model #1`
- Hash symbols in titles must always be quoted: `'Greeks: Δ, Γ, #'`
- Use full words without abbreviations, and keep titles to no more than two lines when displayed

## Content Conventions

- **Math**: Use MathJax with `$...$` (inline) and `$$...$$` (display). Display math blocks must be surrounded by empty lines (blank line, then `$$...$$`, then blank line) for proper rendering
- **Python files**: Educational style with docstrings, section dividers (`# ===`), and `if __name__ == "__main__":` pattern
- **Markdown extensions available**: admonition, details, attr_list, md_in_html, superfences, arithmatex
- **Diagrams**: Use `mermaid2` (via `mkdocs-mermaid2-plugin`) for all box-and-line diagrams (flowcharts, sequence diagrams, architecture overviews). Never use ASCII/text art for diagrams.

## Mermaid2 Diagrams

Use `mermaid2` for any simple box-and-line diagram. Prefer Mermaid over ASCII art or SVG hand-drawing.

### Setup (mkdocs.yml)

```yaml
plugins:
  - mermaid2

markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:mermaid2.fence_mermaid_custom
```

### Usage in Markdown

````markdown
```mermaid
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do Something]
    B -->|No| D[Do Nothing]
    C --> E[End]
    D --> E
```
````

### Common Diagram Types

| Use case | Mermaid type |
|---|---|
| Flowchart / architecture | `graph TD` (top-down) or `graph LR` (left-right) |
| Sequence diagram | `sequenceDiagram` |
| State machine | `stateDiagram-v2` |
| Class diagram | `classDiagram` |
| Timeline / Gantt | `gantt` |

### Mermaid Pitfalls

- **No MathJax inside Mermaid**: Do not use `$...$` or `$$...$$` inside Mermaid blocks — MathJax and Mermaid do not interoperate. Use plain text labels instead.
- **Special characters in labels**: Wrap node labels containing `(`, `)`, `:`, or quotes in double quotes: `A["f(x) → output"]`
- **Avoid very long labels**: Long text in nodes wraps unpredictably; keep labels short and move details to surrounding prose.
- **Dark/light theme**: Mermaid picks up the MkDocs Material theme. Use `%%{init: {'theme': 'neutral'}}%%` at the top of a diagram if you need a fixed appearance.

## MathJax Conventions and Pitfalls

- **Currency vs math**: Use `\$` for literal dollar signs (e.g. `\$100` not `$100`), use `$...$` for math. Never use bare `$` for currency inside markdown.
- **`\boldsymbol`**: Requires the AMS extension. If rendering fails, use `\mathbf` for roman letters or ensure the MathJax config loads `boldsymbol`.
- **LaTeX in headings**: Avoid `$...$` in `#` headings — MathJax in headings breaks the auto-generated TOC anchor links. Use plain text or Unicode symbols in headings instead.
- **Display math**: Always wrap `$$...$$` blocks with blank lines above and below. Missing blank lines cause MathJax to fail silently.
- **No blank lines inside display math**: Never place a blank line inside a `$$...$$` block — MathJax treats the blank line as the end of the block, breaking the equation. This means bullet lists, numbered lists, or any Markdown that requires blank lines must live *outside* the `$$...$$` delimiters. For example, annotating individual terms (diagonal vs off-diagonal) must be done in a Markdown list after the closing `$$`, not interleaved inside it.
- **Escaping in MkDocs**: Backslashes in MathJax sometimes need doubling (`\\alpha`) inside certain admonition or HTML blocks — test when in doubt.
- **No trailing punctuation in display math**: Never place `.` or `,` at the end of a `$$...$$` block, or immediately before `\blacksquare` / `\square` (end-of-proof markers). Punctuation after display math should appear in the surrounding prose, not inside the delimiters.

## Admonitions and Details

Using `pymdownx.details` for collapsible blocks (non-obvious syntax):

```markdown
??? note "Title"
    Collapsed by default.

!!! note "Title"
    Always expanded.

??? example "Click to expand"
    Hidden content here.
```

Standard admonition types: `note`, `tip`, `warning`, `danger`, `info`, `example`, `quote`.

## Common Tasks

### Adding a new section to an existing chapter
1. Create a new `section_name/` directory under `docs/chapter_name/`
2. Add `.md` or `.py` files for each topic inside the section directory
3. Add entries to `mkdocs.yml` nav under the correct chapter, pointing to `.md` or `.py` files only
4. Ensure display math has blank lines above and below, and no LaTeX in headings

### Adding a new chapter
1. Create `docs/chapter_name/` directory with an `index.md`
2. Create section subdirectories with `.md` and `.py` files
3. Add the full chapter block to `mkdocs.yml` nav under the correct Part
4. Follow the Parts → Chapters → Sections → Pages hierarchy

### Adding a Python example
1. Create the `.py` script inside the relevant `section_name/` directory
2. Use the educational style: module docstring, `# ===` section dividers, `if __name__ == "__main__":` guard
3. If the script is a reusable module, create a proper package with `__init__.py`

### Adding a diagram
1. Use a `mermaid` fenced code block — never ASCII art
2. Choose the appropriate diagram type (see Mermaid2 Diagrams section above)
3. Keep node labels short; put detailed explanations in surrounding prose
4. Ensure `mermaid2` plugin and `superfences` custom fence are configured in `mkdocs.yml`