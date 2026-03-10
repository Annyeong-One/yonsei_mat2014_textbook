# Compiling Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Why Compile?

`re.compile()` converts a pattern string into a **compiled regular expression object**. This object has the same methods as the `re` module functions (`search`, `match`, `findall`, etc.) but avoids re-parsing the pattern on every call.

```python
import re

# Without compilation — pattern parsed each time
for line in lines:
    if re.search(r'\d{4}-\d{2}-\d{2}', line):
        process(line)

# With compilation — pattern parsed once
date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
for line in lines:
    if date_pattern.search(line):
        process(line)
```

## Creating Compiled Patterns

```python
import re

# Compile with optional flags
pattern = re.compile(r'hello', re.IGNORECASE)

# Use the compiled pattern's methods
pattern.search('Hello World')    # <re.Match object; match='Hello'>
pattern.findall('Hello HELLO hello')  # ['Hello', 'HELLO', 'hello']
```

## Compiled Pattern Methods

A compiled pattern object provides all the same functions as the `re` module, but without the `pattern` argument:

| Module Function | Compiled Method |
|---|---|
| `re.search(pattern, string)` | `pattern.search(string)` |
| `re.match(pattern, string)` | `pattern.match(string)` |
| `re.fullmatch(pattern, string)` | `pattern.fullmatch(string)` |
| `re.findall(pattern, string)` | `pattern.findall(string)` |
| `re.finditer(pattern, string)` | `pattern.finditer(string)` |
| `re.sub(pattern, repl, string)` | `pattern.sub(repl, string)` |
| `re.subn(pattern, repl, string)` | `pattern.subn(repl, string)` |
| `re.split(pattern, string)` | `pattern.split(string)` |

```python
import re

email_re = re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')

text = "Contact alice@example.com or bob@test.org"

email_re.findall(text)
# ['alice@example.com', 'bob@test.org']

email_re.sub('[REDACTED]', text)
# 'Contact [REDACTED] or [REDACTED]'
```

## Compiled Pattern Attributes

Compiled patterns expose useful attributes:

```python
import re

pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})', re.VERBOSE | re.IGNORECASE)

print(pattern.pattern)      # '(?P<year>\\d{4})-(?P<month>\\d{2})'
print(pattern.flags)        # 98 (integer bitmask)
print(pattern.groups)       # 2
print(pattern.groupindex)   # {'year': 1, 'month': 2}
```

## When to Compile

### Compile When:

- The **same pattern** is used in a **loop** or called multiple times
- The pattern is **complex** and benefits from a descriptive variable name
- You want to store the pattern in a **module-level constant**
- You need to inspect pattern attributes like `.groups` or `.groupindex`

```python
import re

# Module-level constants — clear intent, compiled once
DATE_RE = re.compile(r'\d{4}-\d{2}-\d{2}')
EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
PHONE_RE = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

def extract_contacts(text):
    return {
        'emails': EMAIL_RE.findall(text),
        'phones': PHONE_RE.findall(text),
        'dates': DATE_RE.findall(text),
    }
```

### Skip Compilation When:

- The pattern is used **once** or in a one-off script
- Readability is better with inline patterns
- You're in an interactive session

```python
import re

# One-off usage — compilation adds nothing
result = re.findall(r'\d+', 'abc 123 def 456')
```

!!! note "Internal Caching"
    Python's `re` module caches the most recently used patterns internally (up to `re._MAXCACHE = 512` entries). So for one-off usage, there is virtually no performance difference between compiled and non-compiled patterns. Compilation is primarily a **code organization** benefit.

## Verbose Patterns

`re.VERBOSE` (or `re.X`) lets you write readable patterns with comments and whitespace. This pairs naturally with compilation:

```python
import re

# A readable phone number pattern
PHONE_RE = re.compile(r"""
    \(?             # optional opening parenthesis
    (\d{3})         # area code (captured)
    \)?             # optional closing parenthesis
    [-.\s]?         # optional separator
    (\d{3})         # exchange (captured)
    [-.\s]?         # optional separator
    (\d{4})         # subscriber (captured)
""", re.VERBOSE)

text = "Call (555) 123-4567 or 555.987.6543"
PHONE_RE.findall(text)
# [('555', '123', '4567'), ('555', '987', '6543')]
```

Compare with the non-verbose version:

```python
# Same pattern, but much harder to read
PHONE_RE = re.compile(r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})')
```

## Pattern Organization Example

A common pattern is to define all compiled regexes at the module level:

```python
import re
from typing import NamedTuple

# --- Compiled patterns ---
RE_DATE = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
RE_TIME = re.compile(r'(?P<hour>\d{2}):(?P<min>\d{2})(?::(?P<sec>\d{2}))?')
RE_IP = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

class LogEntry(NamedTuple):
    date: str
    time: str
    ip: str
    message: str

def parse_log_line(line: str) -> LogEntry | None:
    date_m = RE_DATE.search(line)
    time_m = RE_TIME.search(line)
    ip_m = RE_IP.search(line)
    
    if date_m and time_m and ip_m:
        return LogEntry(
            date=date_m.group(0),
            time=time_m.group(0),
            ip=ip_m.group(0),
            message=line.strip(),
        )
    return None
```

## Summary

| Concept | Key Takeaway |
|---|---|
| `re.compile()` | Parse pattern once, reuse the compiled object |
| Compiled methods | Same API as `re` module functions |
| When to compile | Loops, module constants, complex patterns |
| Internal cache | `re` caches ~512 patterns, so one-off use is fine without compiling |
| `re.VERBOSE` | Pair with compilation for readable, documented patterns |
