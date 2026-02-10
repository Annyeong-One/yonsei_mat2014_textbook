# Lookahead and Lookbehind

## What Are Lookarounds?

Lookarounds are **zero-width assertions** — they check whether a pattern exists before or after the current position without consuming any characters. The matched text is not included in the result.

| Syntax | Name | Meaning |
|---|---|---|
| `(?=...)` | Positive lookahead | Followed by `...` |
| `(?!...)` | Negative lookahead | NOT followed by `...` |
| `(?<=...)` | Positive lookbehind | Preceded by `...` |
| `(?<!...)` | Negative lookbehind | NOT preceded by `...` |

```
         Lookbehind          Lookahead
         (?<=...) (?<!...)   (?=...) (?!...)
                    ↓            ↓
    ... [before] [current pos] [after] ...
```

## Positive Lookahead `(?=...)`

Matches a position where the lookahead pattern **exists** ahead, without consuming it:

```python
import re

# Find "Python" only when followed by a space and a version number
re.findall(r'Python(?=\s\d)', 'Python 3 and Python are great')
# ['Python']  — only the first "Python" (followed by " 3")

# Find words followed by a comma
re.findall(r'\w+(?=,)', 'apple, banana, cherry')
# ['apple', 'banana']
```

The key insight is that the lookahead text is **not consumed**:

```python
import re

# Without lookahead — "ing" is consumed
re.findall(r'\w+ing', 'running jumping sitting')
# ['running', 'jumping', 'sitting']

# With lookahead — "ing" is checked but not part of the match
re.findall(r'\w+(?=ing)', 'running jumping sitting')
# ['runn', 'jump', 'sitt']
```

## Negative Lookahead `(?!...)`

Matches a position where the lookahead pattern does **not** exist:

```python
import re

# Match "foo" NOT followed by "bar"
re.findall(r'foo(?!bar)', 'foobar foobaz foo')
# ['foo', 'foo']  — the 'foo' in 'foobaz' and standalone 'foo'

# Match numbers NOT followed by a percent sign
re.findall(r'\d+(?!%)', '42% 100 85% 7')
# ['4', '10', '8', '7']  — careful with greedy matching!

# Better: use word boundary
re.findall(r'\b\d+\b(?!%)', '42% 100 85% 7')
# ['100', '7']
```

### Password Validation Example

Negative lookahead is often used for validation logic (checking that something is absent):

```python
import re

def validate_password(pw):
    """
    Requires:
    - At least 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - No spaces
    """
    pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{8,}$'
    return bool(re.fullmatch(pattern, pw))

print(validate_password("Abc12345"))     # True
print(validate_password("abc12345"))     # False — no uppercase
print(validate_password("ABC12345"))     # False — no lowercase
print(validate_password("Abcdefgh"))     # False — no digit
print(validate_password("Ab 12345"))     # False — contains space
print(validate_password("Ab12"))         # False — too short
```

Multiple lookaheads at position 0 act as **AND conditions**: each must be satisfied independently.

## Positive Lookbehind `(?<=...)`

Matches a position where the lookbehind pattern **exists** before:

```python
import re

# Find numbers preceded by a dollar sign
re.findall(r'(?<=\$)\d+', 'Price: $42, €50, $100')
# ['42', '100']

# Find words preceded by "@" (mentions)
re.findall(r'(?<=@)\w+', 'Hello @alice and @bob')
# ['alice', 'bob']
```

!!! warning "Fixed-Width Lookbehind"
    In Python, lookbehind patterns must match a **fixed-length** string. Variable-length patterns like `(?<=\d+)` are not allowed and raise `re.error`. However, alternations of different fixed lengths are permitted: `(?<=ab|cde)` works.

```python
import re

# Fixed-width — OK
re.findall(r'(?<=\$)\d+', '$42')          # ['42']
re.findall(r'(?<=USD\s)\d+', 'USD 42')    # ['42']

# Variable-width — ERROR
try:
    re.findall(r'(?<=\$\d+\.)\d+', '$3.50')
except re.error as e:
    print(e)  # look-behind requires fixed-width pattern

# Alternation of fixed widths — OK
re.findall(r'(?<=\$|€)\d+', '$42 €50')    # ['42', '50']
```

## Negative Lookbehind `(?<!...)`

Matches a position where the lookbehind pattern does **not** exist:

```python
import re

# Match numbers NOT preceded by a dollar sign
re.findall(r'(?<!\$)\b\d+', 'Price: $42, quantity: 100, code: $7')
# ['100']

# Match "test" NOT preceded by "unit"
re.findall(r'(?<!unit)test', 'unittest test mytest')
# ['test', 'test']
```

## Combining Lookarounds

Lookarounds can be combined for precise matching:

```python
import re

# Find numbers that are both preceded by $ and followed by a decimal point
re.findall(r'(?<=\$)\d+(?=\.)', '$42.99 $100 €50.00')
# ['42']

# Find words surrounded by underscores (like _word_) 
# without including the underscores in the match
re.findall(r'(?<=_)\w+(?=_)', 'This is _bold_ and _italic_ text')
# ['bold', 'italic']
```

### Overlapping Matches

Since lookarounds don't consume characters, they enable finding "overlapping" patterns:

```python
import re

# Find all positions where "aa" occurs (including overlapping)
text = "aaa"

# Without lookahead — non-overlapping only
re.findall(r'aa', text)
# ['aa']  — finds only one

# With lookahead — overlapping
re.findall(r'(?=(aa))', text)
# ['aa', 'aa']  — finds both positions (0 and 1)
```

## Practical Examples

### Number Formatting (Thousands Separator)

```python
import re

def add_commas(n):
    """Add thousand separators: 1234567 → '1,234,567'"""
    s = str(n)
    # Insert comma before groups of 3 digits from the right
    # Positive lookahead: followed by groups of exactly 3 digits to the end
    # Positive lookbehind: preceded by a digit
    return re.sub(r'(?<=\d)(?=(\d{3})+$)', ',', s)

print(add_commas(1234567))     # '1,234,567'
print(add_commas(1000000000))  # '1,000,000,000'
print(add_commas(42))          # '42'
```

### Extracting Values After Labels

```python
import re

text = "Name: Alice  Age: 30  City: Seoul"

# Extract values after specific labels
labels = re.findall(r'(?<=Name:\s)\w+', text)    # ['Alice']
ages = re.findall(r'(?<=Age:\s)\d+', text)        # ['30']
cities = re.findall(r'(?<=City:\s)\w+', text)     # ['Seoul']
```

### Splitting Without Losing Context

```python
import re

# Split before uppercase letters (camelCase → words)
text = "camelCaseVariableName"
re.split(r'(?=[A-Z])', text)
# ['camel', 'Case', 'Variable', 'Name']

# Split after digits
re.split(r'(?<=\d)(?=[a-zA-Z])', 'abc123def456ghi')
# ['abc123', 'def456', 'ghi']
```

### URL Protocol Check

```python
import re

urls = [
    "https://example.com",
    "http://test.org",
    "ftp://files.example.com",
    "example.com",
]

# Match URLs that do NOT start with https
for url in urls:
    if re.match(r'(?!https://)\S+', url) and '://' in url:
        print(f"Not HTTPS: {url}")
# Not HTTPS: http://test.org
# Not HTTPS: ftp://files.example.com
```

## Summary

| Lookaround | Syntax | Meaning | Width |
|---|---|---|---|
| Positive lookahead | `(?=...)` | Must be followed by | Zero |
| Negative lookahead | `(?!...)` | Must NOT be followed by | Zero |
| Positive lookbehind | `(?<=...)` | Must be preceded by | Zero (fixed-width only) |
| Negative lookbehind | `(?<!...)` | Must NOT be preceded by | Zero (fixed-width only) |
| Combined | Stack multiple | AND conditions at a position | Zero |
