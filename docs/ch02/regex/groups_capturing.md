# Groups and Capturing

## Capturing Groups

Parentheses `(...)` serve two purposes in regex: **grouping** (treating multiple tokens as a unit) and **capturing** (extracting the matched substring).

```python
import re

text = "2024-01-15"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)

print(match.group(0))   # '2024-01-15'  — full match
print(match.group(1))   # '2024'        — first group (year)
print(match.group(2))   # '01'          — second group (month)
print(match.group(3))   # '15'          — third group (day)
print(match.groups())   # ('2024', '01', '15')
```

Groups are numbered left to right by their **opening parenthesis**:

```python
import re

# Groups numbered by opening parenthesis position
#       1         2    3
match = re.search(r'((a)(b))', 'ab')
print(match.group(1))  # 'ab'  — outer group
print(match.group(2))  # 'a'   — first inner
print(match.group(3))  # 'b'   — second inner
```

## `findall()` with Groups

When a pattern contains capturing groups, `re.findall()` returns the **group contents** instead of the full match:

```python
import re

text = "2024-01-15 and 2024-12-31"

# No groups — returns full matches
re.findall(r'\d{4}-\d{2}-\d{2}', text)
# ['2024-01-15', '2024-12-31']

# One group — returns list of strings (the group)
re.findall(r'(\d{4})-\d{2}-\d{2}', text)
# ['2024', '2024']

# Multiple groups — returns list of tuples
re.findall(r'(\d{4})-(\d{2})-(\d{2})', text)
# [('2024', '01', '15'), ('2024', '12', '31')]
```

!!! warning "`findall()` Behavior Changes with Groups"
    This is a common source of confusion. If you want the full match but also need groups, use `re.finditer()` and access both `.group(0)` and `.groups()`.

## Non-Capturing Groups

Use `(?:...)` when you need grouping for quantifiers or alternation but do **not** need to capture:

```python
import re

text = "gray grey"

# Capturing group — findall returns group content
re.findall(r'gr(a|e)y', text)
# ['a', 'e']

# Non-capturing group — findall returns full match
re.findall(r'gr(?:a|e)y', text)
# ['gray', 'grey']
```

Non-capturing groups are useful for applying quantifiers to a sub-pattern:

```python
import re

# Match repeated word patterns
re.findall(r'(?:ha)+', 'hahaha haha ha')
# ['hahaha', 'haha', 'ha']

# Optional prefix
re.findall(r'(?:un)?happy', 'happy unhappy')
# ['happy', 'unhappy']
```

## Named Groups

Named groups use the syntax `(?P<name>...)` and can be accessed by name via `.group('name')` or `.groupdict()`:

```python
import re

text = "2024-01-15"
match = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', text)

print(match.group('year'))   # '2024'
print(match.group('month'))  # '01'
print(match.group('day'))    # '15'
print(match.groupdict())     # {'year': '2024', 'month': '01', 'day': '15'}
```

Named groups improve readability, especially in complex patterns:

```python
import re

log = '192.168.1.100 - - [15/Jan/2024:10:30:45] "GET /index.html HTTP/1.1" 200 1234'

pattern = r'(?P<ip>[\d.]+) .+ \[(?P<date>[^\]]+)\] "(?P<method>\w+) (?P<path>\S+)'
match = re.search(pattern, log)

if match:
    info = match.groupdict()
    print(info)
    # {'ip': '192.168.1.100', 'date': '15/Jan/2024:10:30:45',
    #  'method': 'GET', 'path': '/index.html'}
```

## Backreferences

Backreferences match the **same text** that was previously captured by a group. Use `\1`, `\2`, etc. (or `(?P=name)` for named groups):

```python
import re

# Find repeated words
text = "the the cat sat on on the mat"
re.findall(r'\b(\w+)\s+\1\b', text)
# ['the', 'on']

# Find matching HTML tags
html = '<b>bold</b> <i>italic</i> <b>mismatch</i>'
re.findall(r'<(\w+)>.*?</\1>', html)
# ['b', 'i']  — only properly closed tags
```

Named backreference:

```python
import re

# Detect repeated words using named groups
text = "the the quick quick fox"
re.findall(r'\b(?P<word>\w+)\s+(?P=word)\b', text)
# ['the', 'quick']
```

## Groups with Quantifiers

When a group is inside a quantifier, only the **last** iteration is captured:

```python
import re

# Only the last repetition is captured
match = re.search(r'(\d)+', '12345')
print(match.group(0))  # '12345' — full match
print(match.group(1))  # '5'     — only the last digit captured

# To capture all, put the quantifier inside the group
match = re.search(r'(\d+)', '12345')
print(match.group(1))  # '12345'
```

## Practical Examples

### Parsing Key-Value Pairs

```python
import re

config = "host=localhost port=5432 db=mydb user=admin"
pairs = re.findall(r'(\w+)=(\S+)', config)
print(pairs)
# [('host', 'localhost'), ('port', '5432'), ('db', 'mydb'), ('user', 'admin')]
print(dict(pairs))
# {'host': 'localhost', 'port': '5432', 'db': 'mydb', 'user': 'admin'}
```

### Swapping Name Order

```python
import re

names = "Smith, John\nDoe, Jane\nLee, Alice"
# Swap "Last, First" to "First Last"
result = re.sub(r'(\w+), (\w+)', r'\2 \1', names)
print(result)
# John Smith
# Jane Doe
# Alice Lee
```

### Extracting URLs

```python
import re

text = "Visit https://example.com or http://test.org/page?q=1"
urls = re.findall(r'https?://\S+', text)
print(urls)
# ['https://example.com', 'http://test.org/page?q=1']

# With named groups for parts
pattern = r'(?P<scheme>https?)://(?P<host>[\w.]+)(?P<path>/\S*)?'
for m in re.finditer(pattern, text):
    print(m.groupdict())
# {'scheme': 'https', 'host': 'example.com', 'path': None}
# {'scheme': 'http', 'host': 'test.org', 'path': '/page?q=1'}
```

## Summary

| Concept | Syntax | Key Takeaway |
|---|---|---|
| Capturing group | `(...)` | Groups and captures; accessed by number |
| Non-capturing | `(?:...)` | Groups without capturing |
| Named group | `(?P<name>...)` | Capture accessible by name |
| Backreference | `\1` or `(?P=name)` | Matches same text as a previous group |
| `findall` + groups | — | Returns group contents, not full match |
| `groupdict()` | — | Dictionary of named groups |
