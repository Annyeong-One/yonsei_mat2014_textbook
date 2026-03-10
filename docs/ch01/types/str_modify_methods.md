# Modify Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

String modification methods return new strings with content replaced, removed, or transformed.

## Replace Method

Substitute substrings with new values.

### 1. Basic Replace

Replace all occurrences of a substring.

```python
s = "Hello World"
result = s.replace("World", "Python")
print(result)  # Hello Python
print(s)       # Hello World (unchanged)
```

### 2. All Occurrences

By default, replaces every match found.

```python
s = "hello hello hello"
result = s.replace("hello", "hi")
print(result)  # hi hi hi
```

### 3. Limited Replace

Use count parameter to limit replacements.

```python
s = "hello hello hello"

print(s.replace("hello", "hi", 1))  # hi hello hello
print(s.replace("hello", "hi", 2))  # hi hi hello
```

## Strip Methods

Remove characters from string edges.

### 1. Whitespace Strip

Remove leading and trailing whitespace.

```python
s = "   Hello World   "

print(f"[{s.strip()}]")    # [Hello World]
print(f"[{s.lstrip()}]")   # [Hello World   ]
print(f"[{s.rstrip()}]")   # [   Hello World]
```

### 2. Character Strip

Specify characters to remove.

```python
s = "###Hello World###"

print(s.strip("#"))    # Hello World
print(s.lstrip("#"))   # Hello World###
print(s.rstrip("#"))   # ###Hello World
```

### 3. Character Set Strip

Strips any character in the given set.

```python
s = "   Hello World   "

# Strip space and 'H' and 'd'
print(s.strip(" Hd"))   # ello Worl

# Strip space, 'l', 'o', 'H'
print(s.strip(" ldoH"))  # ello Wor

# Order doesn't matter - it's a set
print(s.strip("loHd "))  # ello Wor
```

## Prefix and Suffix

Remove specific prefixes or suffixes (Python 3.9+).

### 1. Remove Prefix

Remove exact prefix string.

```python
s = "HelloWorld"

print(s.removeprefix("Hello"))  # World
print(s.removeprefix("Hi"))     # HelloWorld (no match)
print(s.removeprefix(""))       # HelloWorld
```

### 2. Remove Suffix

Remove exact suffix string.

```python
filename = "document.txt"

print(filename.removesuffix(".txt"))   # document
print(filename.removesuffix(".pdf"))   # document.txt

# Useful for file extensions
files = ["data.csv", "notes.txt", "image.png"]
names = [f.removesuffix(".csv").removesuffix(".txt").removesuffix(".png") 
         for f in files]
print(names)  # ['data', 'notes', 'image']
```

### 3. Vs Strip Behavior

Unlike strip, these match exact strings.

```python
s = "Hello"

# strip removes characters from set
print(s.strip("Helo"))       # (empty - all chars in set)

# removeprefix/suffix match exact string
print(s.removeprefix("He"))  # llo
print(s.removeprefix("el"))  # Hello (not a prefix)
```

## Translate Method

Character-level replacements using translation table.

### 1. Basic Translation

Use `str.maketrans()` to build translation table.

```python
# Create translation table
table = str.maketrans("aeiou", "12345")

s = "hello world"
print(s.translate(table))  # h2ll4 w4rld
```

### 2. Delete Characters

Map characters to None to delete them.

```python
# Delete vowels
table = str.maketrans("", "", "aeiou")

s = "hello world"
print(s.translate(table))  # hll wrld
```

### 3. Combined Operation

Replace some, delete others simultaneously.

```python
# Replace digits, delete punctuation
table = str.maketrans(
    "0123456789",           # from
    "OOOOOOOOOO",           # to
    "!@#$%^&*()"           # delete
)

s = "Price: \$99.99!"
print(s.translate(table))  # Price: OO.OO
```

## Expand Tabs

Convert tabs to spaces.

### 1. Default Tab Size

Expands tabs to 8-space columns.

```python
s = "a\tb\tc"
print(s.expandtabs())
# a       b       c
print(len(s.expandtabs()))  # 17
```

### 2. Custom Tab Size

Specify column width.

```python
s = "a\tb\tc"

print(s.expandtabs(4))   # a   b   c
print(s.expandtabs(2))   # a b c
```

### 3. Column Alignment

Tabs align to column positions, not fixed widths.

```python
lines = "name\tage\ncity\tzip"
print(lines.expandtabs(8))
# name    age
# city    zip
```

## Practical Patterns

Common modification operations.

### 1. Clean User Input

Sanitize user-provided strings.

```python
def clean_input(s):
    """Clean and normalize user input."""
    # Strip whitespace
    s = s.strip()
    # Normalize internal whitespace
    s = " ".join(s.split())
    # Remove control characters
    s = s.replace("\x00", "")
    return s

dirty = "  hello   world  \x00 "
clean = clean_input(dirty)
print(repr(clean))  # 'hello world'
```

### 2. Template Processing

Simple placeholder replacement.

```python
def render_template(template, values):
    """Replace placeholders with values."""
    result = template
    for key, value in values.items():
        result = result.replace(f"{{{key}}}", str(value))
    return result

template = "Hello, {name}! You have {count} messages."
data = {"name": "Alice", "count": 5}
print(render_template(template, data))
# Hello, Alice! You have 5 messages.
```

### 3. Filename Sanitize

Make strings safe for filenames.

```python
def sanitize_filename(name):
    """Remove characters invalid in filenames."""
    invalid = '<>:"/\\|?*'
    table = str.maketrans("", "", invalid)
    clean = name.translate(table)
    return clean.strip()

dirty = 'My "Report" <2025>.txt'
safe = sanitize_filename(dirty)
print(safe)  # My Report 2025.txt
```
