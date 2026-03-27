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
├── agents/
│   ├── MATH_REVIEWER.md
│   ├── WRITING_REVIEWER.md
│   └── WRITER.md
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

## Agent Commands

Three specialized agents live in `agents/`. Always run sequentially, batch size = 1, commit after each file.

### File Path Convention
Commands accept the path relative to `docs/` — omit the `docs/` prefix.
```
review ch04/martingale_foundations/local_martingale.md
        ↑ resolves to docs/ch04/martingale_foundations/local_martingale.md
```

### File Convention
For every file processed by any agent command, versioned snapshots are maintained:

```
docs/ch04/martingale_foundations/
├── local_martingale.md          ← current best (updated in place)
├── local_martingale_v1.md       ← original, frozen forever
├── local_martingale_v2.md       ← after 1st update
├── local_martingale_v3.md       ← after 2nd update
├── local_martingale_review.md   ← latest review report (math + writing)
└── local_martingale_score.md    ← score history across all updates
```

- On the first `update`: save current `<file>` as `_v1.md`, then overwrite `<file>` with the result
- On each subsequent `update`: save current `<file>` as `_v(N+1).md`, then overwrite `<file>` with the result
- `local_martingale.md` always reflects the latest result — no separate `_vN.md` for it
- `_v1.md` is always the true original, never overwritten
- To roll back to any version: copy `_vN.md` over `local_martingale.md` and commit

### Score File Format
`_score.md` is a single growing table — each `write` or `update` appends a new version column:

```
┌───────────────┬──────────┬──────────┬──────────┬──────────┬─────
│               │    v1    │    v2    │    v3    │    v4    │ ...
├───────────────┼──────────┼──────────┼──────────┼──────────┼─────
│ Math score    │ 8.5 / 10 │ 9.5 / 10 │ 9.7 / 10 │          │
├───────────────┼──────────┼──────────┼──────────┼──────────┼─────
│ Writing score │ 7.5 / 10 │ 9.0 / 10 │ 9.3 / 10 │          │
└───────────────┴──────────┴──────────┴──────────┴──────────┴─────
```

- `v1` scores come from the first `review` pass (the original file)
- Each subsequent `vN` score is WRITER's estimate after that update
- Empty cells mean that version has not been written yet

### Review Reports (for `review` only)
When running `review` without `write`, the report is also saved to `reviews/` with a datestamp for score history tracking:
```
reviews/ch04/martingale_foundations/local_martingale.2026-03-20.review.md
```

### `review <file>`
Copy and review only — no write.
1. Determine next version N by counting existing `_vN.md` files + 1
2. Copy (not rename) `<file>` → `<file>_vN.md` (freeze the input; `<file>` remains intact)
3. MATH_REVIEWER reads `<file>_vN.md` → math report
4. WRITING_REVIEWER reads `<file>_vN.md` → writing report
5. Save combined report → `<file>_review.md`
6. Also save datestamped copy → `reviews/<file>.<YYYY-MM-DD>.review.md`
7. Print full report to stdout
8. `<file>` still exists — `mkdocs serve` continues to work normally after a review-only run

### `review <folder>` / `review all`
Run `review` on every `.md` recursively inside `docs/<folder>` (or all of `docs/`), regardless of git status.
Batch size = 1.

---

### `write <file>`
Write only — requires `<file>_review.md` and a frozen `<file>_vN.md` to already exist.
1. Load `agents/WRITER.md`
2. Read latest `<file>_vN.md` + `<file>_review.md`
3. Overwrite `<file>` with improved version
4. Append dated score entry to `<file>_score.md`
5. Commit: `write: <file>`

### `write <folder>` / `write all`
Run `write` on every `.md` recursively inside `docs/<folder>` (or all of `docs/`) that has a `_review.md`, regardless of git status.
Batch size = 1, commit after each file.

### `write <file|folder|all> if score < N`
Conditional write — only write files where the latest math score **or** writing score is below N (e.g. `write ch01 if score < 9.3`).

Shared per-file logic (applies to single file, folder, and `all` variants equally):
1. If `_score.md` does not exist: run `review <file>` first to generate scores, then apply the threshold check, then write if triggered.
2. If `_score.md` exists: read the latest (rightmost) math and writing scores. If either is below N, proceed to `write`; otherwise skip and log to stdout with actual scores.
3. If `_review.md` does not exist but `_score.md` does: run `review <file>` first to refresh `_review.md`, then apply the threshold check, then write if triggered.

Batch size = 1, commit after each file that is actually written.

---

### `update <file>`
Shorthand for `review` + `write` in one step.
1. Determine next version N by counting existing `_vN.md` files + 1
2. Copy `<file>` → `<file>_vN.md` (freeze the input)
3. MATH_REVIEWER reads `<file>_vN.md` → math report
4. WRITING_REVIEWER reads `<file>_vN.md` → writing report
5. Save combined report → `<file>_review.md`
6. WRITER reads `<file>_vN.md` + `<file>_review.md` → overwrites `<file>` with improved version
7. Append dated score entry to `<file>_score.md`
8. Commit: `update: <file> → v(N)`

### `update <folder>` / `update all`
Run `update` on every `.md` recursively inside `docs/<folder>` (or all of `docs/`), regardless of git status.
- Example: `update ch04` processes all `.md` files in ch04 and all its subfolders
- Example: `update ch04/martingale_foundations` processes just that section and its subfolders
- Batch size = 1, commit after each file

### `update <file|folder|all> if score < N`
Conditional update — review first to get a score, then write only if the score is below N.

Per-file logic:
1. If `_score.md` does not exist: run `review <file>` first to generate scores, then apply the threshold check, then write if triggered.
2. If `_score.md` exists: read the latest (rightmost) math and writing scores. If either is below N, run full `update`; otherwise skip and log to stdout with actual scores.

Batch size = 1, commit after each file that is actually updated.



## Agent File Management

Files generated by agents fall into three categories:

| File | Git | GitHub Pages |
|---|---|---|
| `<name>.md` | ✅ committed | ✅ published |
| `<name>_score.md` | ✅ committed | ❌ excluded via `mkdocs.yml` |
| `<name>_v[0-9]*.md` | ❌ gitignored | ❌ never built |
| `<name>_review.md` | ❌ gitignored | ❌ never built |

The `.gitignore` entries covering this:
```
docs/**/*_v[0-9]*.md
docs/**/*_review.md
!docs/ch15/definition_and_setup/markov_processes_review.md
```

**Important:** The versioned-file pattern uses `_v[0-9]*` (not `_v*`) to avoid
matching content files that contain `_v` in their names (e.g., `quadratic_variation.md`,
`stochastic_volatility_models.md`). The `_review.md` pattern requires a negation rule
for any content file whose name ends in `_review.md` (e.g., `markov_processes_review.md`).

The `mkdocs.yml` exclusion for agent files:
```yaml
exclude_docs: |
  *_score.md
  *_v[0-9]*.md
  *_review.md
  !ch15/definition_and_setup/markov_processes_review.md
```

When committing after `update`, only stage `<name>.md` and `<name>_score.md`:
```bash
git add docs/path/to/<name>.md docs/path/to/<name>_score.md
git commit -m "update: <name>"
```



## Execution Rules (All Agents)

- **Sequential only**: Never run two agent passes on the same file simultaneously
- **Batch size = 1**: One file per agent invocation
- **Commit after each file**: only stage `<name>.md` and `<name>_score.md` — never `_vN.md` or `_review.md`
- **Do not modify `mkdocs.yml`** unless explicitly instructed
- **Do not create new files** unless explicitly instructed

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

## MathJax Conventions and Pitfalls

- **Currency vs math**: Use `\$` for literal dollar signs (e.g. `\$100` not `$100`), use `$...$` for math. Never use bare `$` for currency inside markdown.
- **`\boldsymbol`**: Requires the AMS extension. If rendering fails, use `\mathbf` for roman letters or ensure the MathJax config loads `boldsymbol`.
- **LaTeX in headings**: Avoid `$...$` in `#` headings — MathJax in headings breaks the auto-generated TOC anchor links. Use plain text or Unicode symbols in headings instead.
- **Display math**: Always wrap `$$...$$` blocks with blank lines above and below. Missing blank lines cause MathJax to fail silently.
- **No blank lines inside display math**: Never place a blank line inside a `$$...$$` block — MathJax treats the blank line as the end of the block, breaking the equation. This means bullet lists, numbered lists, or any Markdown that requires blank lines must live *outside* the `$$...$$` delimiters.
- **Escaping in MkDocs**: Backslashes in MathJax sometimes need doubling (`\\alpha`) inside certain admonition or HTML blocks — test when in doubt.
- **No trailing punctuation in display math**: Never place `.` or `,` at the end of a `$$...$$` block, or immediately before `\blacksquare` / `\square` (end-of-proof markers).

## Admonitions and Details

Using `pymdownx.details` for collapsible blocks:

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
