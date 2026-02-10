# re Module Overview

## What Are Regular Expressions?

A **regular expression** (regex) is a sequence of characters that defines a search pattern. Regular expressions let you match, search, extract, and replace text based on patterns rather than fixed strings. Python's built-in `re` module provides full support for Perl-style regular expressions.

```python
import re

text = "Order #12345 was placed on 2024-01-15"
match = re.search(r'\d{5}', text)
print(match.group())  # 12345
```

Regular expressions are indispensable for tasks like validating email addresses, parsing log files, extracting data from unstructured text, and cleaning datasets.

## The `re` Module

The `re` module is part of Python's standard library — no installation required.

```python
import re
```

### Core Functions

| Function | Purpose |
|---|---|
| `re.search(pattern, string)` | Find the first match anywhere in the string |
| `re.match(pattern, string)` | Match only at the beginning of the string |
| `re.fullmatch(pattern, string)` | Match the entire string |
| `re.findall(pattern, string)` | Return all non-overlapping matches as a list |
| `re.finditer(pattern, string)` | Return an iterator of `Match` objects |
| `re.sub(pattern, repl, string)` | Replace matches with a replacement string |
| `re.split(pattern, string)` | Split string by pattern occurrences |
| `re.compile(pattern)` | Compile a pattern for repeated use |

### Raw Strings

Regular expressions use backslashes extensively (`\d`, `\w`, `\s`). Python also uses backslashes for escape sequences (`\n`, `\t`). To avoid conflicts, always use **raw strings** (prefix with `r`):

```python
# Without raw string — Python interprets \b as backspace
pattern = '\bword\b'    # BAD: \b is a backspace character

# With raw string — \b passes through to regex engine
pattern = r'\bword\b'   # GOOD: \b is a word boundary
```

!!! warning "Always Use Raw Strings"
    Forgetting the `r` prefix is the most common regex mistake in Python. The pattern `'\d+'` happens to work because `\d` is not a Python escape sequence, but `'\bword\b'` silently breaks because `\b` is Python's backspace character.

## The Match Object

When `re.search()` or `re.match()` finds a match, it returns a `Match` object. If no match is found, it returns `None`.

```python
import re

text = "Temperature: 72.5°F"
match = re.search(r'(\d+\.?\d*)', text)

if match:
    print(match.group())    # '72.5'   — the full match
    print(match.group(0))   # '72.5'   — same as .group()
    print(match.group(1))   # '72.5'   — first capturing group
    print(match.start())    # 13       — start index
    print(match.end())      # 17       — end index (exclusive)
    print(match.span())     # (13, 17) — (start, end) tuple
```

### Key Match Methods

| Method | Description |
|---|---|
| `.group()` or `.group(0)` | The entire match |
| `.group(n)` | The *n*-th capturing group |
| `.groups()` | Tuple of all capturing groups |
| `.groupdict()` | Dictionary of named groups |
| `.start()` / `.end()` | Start/end indices of the match |
| `.span()` | Tuple of `(start, end)` |

### Checking for a Match

Since `re.search()` returns `None` on failure, always check before accessing the result:

```python
match = re.search(r'\d+', "no numbers here")
if match:
    print(match.group())
else:
    print("No match found")
# No match found
```

Using `match.group()` without checking first raises an `AttributeError`.

## Regex Workflow

A typical regex workflow follows these steps:

```
1. Define the pattern  →  r'\d{3}-\d{4}'
2. Choose the function  →  re.search(), re.findall(), etc.
3. Apply to text        →  re.search(pattern, text)
4. Process the result   →  match.group(), list of strings, etc.
```

```python
import re

# Step 1: Define pattern for US phone numbers
pattern = r'\d{3}-\d{3}-\d{4}'

# Step 2-3: Search the text
text = "Call us at 555-123-4567 or 555-987-6543"
phones = re.findall(pattern, text)

# Step 4: Process results
print(phones)  # ['555-123-4567', '555-987-6543']
```

## Flags (Optional Modifiers)

Flags modify how the regex engine interprets the pattern:

| Flag | Short Form | Effect |
|---|---|---|
| `re.IGNORECASE` | `re.I` | Case-insensitive matching |
| `re.MULTILINE` | `re.M` | `^` and `$` match at line boundaries |
| `re.DOTALL` | `re.S` | `.` matches newline characters too |
| `re.VERBOSE` | `re.X` | Allow comments and whitespace in pattern |
| `re.ASCII` | `re.A` | `\w`, `\d`, `\s` match ASCII only |

```python
# Case-insensitive search
re.findall(r'python', 'Python PYTHON python', re.IGNORECASE)
# ['Python', 'PYTHON', 'python']

# Combine flags with bitwise OR
re.findall(r'^hello', 'Hello\nhello', re.I | re.M)
# ['Hello', 'hello']
```

The `re.VERBOSE` flag is especially useful for complex patterns:

```python
pattern = re.compile(r"""
    \d{3}       # area code
    [-.\s]?     # optional separator
    \d{3}       # exchange
    [-.\s]?     # optional separator
    \d{4}       # subscriber number
""", re.VERBOSE)
```

## Summary

| Concept | Key Takeaway |
|---|---|
| `re` module | Python's built-in regex library — `import re` |
| Raw strings | Always use `r'...'` for regex patterns |
| Match object | Returned by `search()`/`match()`; use `.group()` to extract |
| `None` check | Always verify the match exists before accessing it |
| Flags | Modify behavior with `re.I`, `re.M`, `re.S`, `re.X` |
