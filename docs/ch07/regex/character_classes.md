# Character Classes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## What Is a Character Class?

A **character class** (also called a character set) matches **one character** from a defined set. Character classes are enclosed in square brackets `[...]`.

```python
import re

# Match any vowel
re.findall(r'[aeiou]', 'Hello World')
# ['e', 'o', 'o']

# Match any digit
re.findall(r'[0123456789]', 'Room 404')
# ['4', '0', '4']
```

## Ranges

Use a hyphen `-` inside brackets to specify a range of characters:

```python
import re

text = "Agent 007 has clearance Level-A3"

# Digit range (equivalent to \d)
re.findall(r'[0-9]', text)
# ['0', '0', '7', '3']

# Lowercase letters
re.findall(r'[a-z]+', text)
# ['gent', 'has', 'clearance', 'evel']

# Uppercase letters
re.findall(r'[A-Z]+', text)
# ['A', 'L', 'A']

# Letters and digits combined
re.findall(r'[a-zA-Z0-9]+', text)
# ['Agent', '007', 'has', 'clearance', 'Level', 'A3']
```

Multiple ranges can be combined in a single class:

```python
# Hexadecimal digits
re.findall(r'[0-9a-fA-F]+', '0xFF 0x1A 255 0xGG')
# ['0', 'FF', '0', '1A', '255', '0', 'GG' won't match fully]
# Actually:
re.findall(r'[0-9a-fA-F]+', '0xFF 0x1A 255 0xGG')
# ['0', 'FF', '0', '1A', '255', '0']
```

## Negated Character Classes

A caret `^` at the **beginning** of a character class negates it — matching any character **not** in the set:

```python
import re

# Match non-digits
re.findall(r'[^0-9]+', 'Room 404 is on Floor 4')
# ['Room ', ' is on Floor ']

# Match non-vowels
re.findall(r'[^aeiouAEIOU]+', 'Hello World')
# ['H', 'll', ' W', 'rld']

# Match non-whitespace (similar to \S)
re.findall(r'[^ \t\n]+', 'hello   world')
# ['hello', 'world']
```

!!! note "Caret Position Matters"
    The `^` only negates when it appears as the **first** character inside `[...]`. Elsewhere, it matches a literal caret: `[a^b]` matches `a`, `^`, or `b`.

## Special Characters Inside Classes

Most metacharacters lose their special meaning inside character classes. Only a few remain special:

| Character | Special inside `[...]`? | How to use literally |
|---|---|---|
| `]` | Yes — closes the class | `\]` or place first: `[]abc]` |
| `\` | Yes — escape character | `\\` |
| `^` | Yes — negation (only if first) | Place after first position: `[a^b]` |
| `-` | Yes — range operator | `\-` or place first/last: `[-abc]` or `[abc-]` |

```python
import re

# Match literal special characters
re.findall(r'[\[\]]', 'array[0] = list[1]')
# ['[', ']', '[', ']']

# Hyphen at end — matches literal hyphen
re.findall(r'[a-z-]+', 'well-known self-driving')
# ['well-known', 'self-driving']

# Dot inside class — just a literal dot
re.findall(r'[.]', 'version 3.14')
# ['.']
```

## Shorthand Classes vs Bracket Notation

The shorthand classes `\d`, `\w`, `\s` and their negations can be used inside character classes:

```python
import re

# Digits or hyphens (for phone numbers)
re.findall(r'[\d-]+', 'Call 555-123-4567 today')
# ['555-123-4567']

# Word characters or dots (for filenames)
re.findall(r'[\w.]+', 'file_v2.py and data.csv')
# ['file_v2.py', 'and', 'data.csv']

# Digits and whitespace
re.findall(r'[\d\s]+', 'score: 42 out of 50')
# [' 42 ', ' 50']
```

## POSIX-like Classes (Unicode)

Python's `\d`, `\w`, and `\s` match Unicode characters by default. Use the `re.ASCII` flag to restrict to ASCII:

```python
import re

# \d matches Unicode digits by default
re.findall(r'\d+', '123 ١٢٣ ୧୨୩')
# ['123', '١٢٣', '୧୨୩']

# Restrict to ASCII digits
re.findall(r'\d+', '123 ١٢٣ ୧୨୩', re.ASCII)
# ['123']
```

## Practical Examples

### Matching Identifiers

A valid Python identifier starts with a letter or underscore, followed by letters, digits, or underscores:

```python
import re

text = "x = 42; _name = 'hello'; 3bad = True"
re.findall(r'[a-zA-Z_]\w*', text)
# ['x', '_name', 'hello', 'bad', 'True']
```

### Extracting Vowels and Consonants

```python
import re

word = "Mississippi"
vowels = re.findall(r'[aeiouAEIOU]', word)
consonants = re.findall(r'[^aeiouAEIOU]', word)

print(f"Vowels: {vowels}")       # ['i', 'i', 'i', 'i']
print(f"Consonants: {consonants}")  # ['M', 's', 's', 's', 's', 'p', 'p']
```

### Matching Hex Color Codes

```python
import re

css = "color: #FF5733; background: #0a0; border: #12ab"
# Full 6-digit or 3-digit hex codes
re.findall(r'#[0-9a-fA-F]{3,6}\b', css)
# ['#FF5733', '#0a0', '#12ab']

# Strictly 6-digit or 3-digit
re.findall(r'#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b', css)
# ['#FF5733', '#0a0']
```

## Summary

| Concept | Key Takeaway |
|---|---|
| `[abc]` | Matches one character: `a`, `b`, or `c` |
| `[a-z]` | Matches one character in the range `a` to `z` |
| `[^abc]` | Matches one character **not** in the set |
| `-` in class | Range operator; literal if first or last |
| `^` in class | Negation only if first character |
| Metacharacters | Most lose special meaning inside `[...]` |
| `\d \w \s` | Can be used inside character classes |
