# Quantifiers and Anchors

## Quantifiers

Quantifiers specify **how many times** the preceding element must occur for a match. By default, quantifiers are **greedy** — they match as much text as possible.

### Basic Quantifiers

| Quantifier | Meaning | Example | Matches |
|---|---|---|---|
| `*` | Zero or more | `ab*c` | `ac`, `abc`, `abbc`, `abbbc` |
| `+` | One or more | `ab+c` | `abc`, `abbc`, `abbbc` (not `ac`) |
| `?` | Zero or one | `colou?r` | `color`, `colour` |
| `{n}` | Exactly *n* | `\d{4}` | `2024` (exactly 4 digits) |
| `{n,}` | At least *n* | `\d{2,}` | `42`, `007`, `12345` |
| `{n,m}` | Between *n* and *m* | `\d{2,4}` | `42`, `007`, `2024` |

```python
import re

# * — zero or more
re.findall(r'go*d', 'gd god good goood')
# ['gd', 'god', 'good', 'goood']

# + — one or more
re.findall(r'go+d', 'gd god good goood')
# ['god', 'good', 'goood']

# ? — zero or one
re.findall(r'colou?r', 'color and colour')
# ['color', 'colour']

# {n} — exactly n
re.findall(r'\b\d{3}\b', '1 12 123 1234')
# ['123']

# {n,m} — between n and m
re.findall(r'\b\d{2,4}\b', '1 12 123 1234 12345')
# ['12', '123', '1234']
```

### Greedy vs Lazy Quantifiers

By default, quantifiers are **greedy** — they consume as much text as possible. Adding `?` after a quantifier makes it **lazy** (also called non-greedy or reluctant) — it matches as little as possible.

| Greedy | Lazy | Behavior |
|---|---|---|
| `*` | `*?` | Zero or more (prefer fewer) |
| `+` | `+?` | One or more (prefer fewer) |
| `?` | `??` | Zero or one (prefer zero) |
| `{n,m}` | `{n,m}?` | Between n and m (prefer fewer) |

```python
import re

html = '<b>bold</b> and <i>italic</i>'

# Greedy — matches from first < to LAST >
re.findall(r'<.*>', html)
# ['<b>bold</b> and <i>italic</i>']

# Lazy — matches from first < to NEXT >
re.findall(r'<.*?>', html)
# ['<b>', '</b>', '<i>', '</i>']
```

This distinction is critical when parsing structured text:

```python
import re

text = '"first" and "second" and "third"'

# Greedy: matches from first " to last "
re.findall(r'".*"', text)
# ['"first" and "second" and "third"']

# Lazy: matches each quoted string
re.findall(r'".*?"', text)
# ['"first"', '"second"', '"third"']
```

!!! tip "When to Use Lazy Quantifiers"
    Use lazy quantifiers when you want to match the **shortest** possible substring, especially with delimiters like quotes, tags, or brackets. For simple patterns without ambiguity, greedy quantifiers work fine.

### Possessive Quantifiers (Python 3.11+)

Python 3.11 introduced **possessive quantifiers** (`*+`, `++`, `?+`, `{n,m}+`). These are greedy but never backtrack, which can improve performance:

```python
import re

# Possessive + (Python 3.11+)
# Fails fast — no backtracking
try:
    re.search(r'[a-z]++[a-z]', 'abcdef')  # None — possessive consumed all
except Exception:
    pass  # Older Python versions
```

Possessive quantifiers are an optimization tool; in most cases, greedy and lazy are sufficient.

## Anchors

Anchors match **positions** in the string, not characters. They have zero width — they don't consume any characters.

### String Anchors

| Anchor | Matches |
|---|---|
| `^` | Start of string (or line with `re.M`) |
| `$` | End of string (or line with `re.M`) |
| `\A` | Start of string (ignores `re.M`) |
| `\Z` | End of string (ignores `re.M`) |

```python
import re

text = "line one\nline two\nline three"

# ^ matches start of string only
re.findall(r'^line', text)
# ['line']

# ^ with MULTILINE matches start of each line
re.findall(r'^line', text, re.M)
# ['line', 'line', 'line']

# \A always matches start of string, regardless of flags
re.findall(r'\Aline', text, re.M)
# ['line']
```

### Word Boundaries

| Anchor | Matches |
|---|---|
| `\b` | Boundary between word and non-word character |
| `\B` | Position that is **not** a word boundary |

```python
import re

text = "cat concatenate scattered"

# \b — word boundary
re.findall(r'\bcat\b', text)   # ['cat']
re.findall(r'\bcat', text)     # ['cat', 'cat']

# \B — NOT a word boundary
re.findall(r'\Bcat', text)     # ['cat']  — the 'cat' inside 'scattered'
re.findall(r'cat\B', text)     # ['cat', 'cat']  — 'cat' not at end of word
```

Word boundaries are essential for matching **whole words**:

```python
import re

text = "I like Java but not JavaScript"

# Without boundary — matches both
re.findall(r'Java', text)
# ['Java', 'Java']

# With boundary — matches only the standalone word
re.findall(r'\bJava\b', text)
# ['Java']
```

## Combining Quantifiers and Anchors

Quantifiers and anchors work together to create precise patterns:

```python
import re

# Match lines that contain only digits
text = "123\nabc\n456\na1b"
re.findall(r'^\d+$', text, re.M)
# ['123', '456']

# Validate a string is exactly 5 uppercase letters
def is_valid_code(s):
    return bool(re.fullmatch(r'[A-Z]{5}', s))

print(is_valid_code("HELLO"))   # True
print(is_valid_code("Hello"))   # False
print(is_valid_code("HELLOO"))  # False
```

### Validating Input Formats

```python
import re

# Simple integer validation (optional sign)
def is_integer(s):
    return bool(re.fullmatch(r'[+-]?\d+', s))

print(is_integer("42"))    # True
print(is_integer("-17"))   # True
print(is_integer("3.14"))  # False

# Simple float validation
def is_float(s):
    return bool(re.fullmatch(r'[+-]?\d*\.?\d+', s))

print(is_float("3.14"))   # True
print(is_float(".5"))     # True
print(is_float("42"))     # True
print(is_float(""))       # False
```

## Summary

| Concept | Key Takeaway |
|---|---|
| `* + ?` | Zero+, one+, zero-or-one repetitions |
| `{n}` `{n,m}` | Exact or range repetitions |
| Greedy | Default — match as much as possible |
| Lazy (`*?` `+?`) | Match as little as possible |
| `^` / `$` | Start/end of string (or line with `re.M`) |
| `\A` / `\Z` | Start/end of string (always, ignoring `re.M`) |
| `\b` / `\B` | Word boundary / not a word boundary |
| `re.fullmatch()` | Anchor the entire string (like `^...$`) |
