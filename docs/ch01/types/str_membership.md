# Membership and Search


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python strings support membership testing with `in` operator and various search methods for locating substrings, characters, and patterns.

## Membership Testing

The `in` and `not in` operators test whether a substring exists within a string.

### 1. Basic Syntax

Returns `True` if the substring is found anywhere in the string.

```python
text = "Hello, World!"

print("World" in text)      # True
print("world" in text)      # False (case-sensitive)
print("xyz" in text)        # False
print("" in text)           # True (empty string)
```

### 2. Case Sensitivity

Membership testing is case-sensitive; normalize case for insensitive checks.

```python
text = "Python Programming"

# Case-sensitive (default)
print("python" in text)           # False

# Case-insensitive check
print("python" in text.lower())   # True

query = "PROG"
print(query.lower() in text.lower())  # True
```

### 3. Negation Test

Use `not in` to check for absence of a substring.

```python
email = "user@example.com"

print("@" not in email)     # False
print(" " not in email)     # True

# Validation pattern
if "@" not in email:
    print("Invalid email")
```

## Finding Substrings

The `find()` and `index()` methods locate the position of substrings.

### 1. The find() Method

Returns the lowest index where substring is found, or `-1` if not found.

```python
text = "Hello, Hello, Hello"

print(text.find("Hello"))     # 0
print(text.find("World"))     # -1
print(text.find("l"))         # 2
```

### 2. The index() Method

Like `find()` but raises `ValueError` if substring is not found.

```python
text = "Python Programming"

print(text.index("Pro"))      # 7

# Raises ValueError
try:
    text.index("Java")
except ValueError as e:
    print(f"Not found: {e}")
```

### 3. Search Range

Both methods accept optional start and end positions.

```python
text = "abcabcabc"

# Start from index 1
print(text.find("abc", 1))    # 3

# Search within range [1, 6)
print(text.find("abc", 1, 6)) # 3
print(text.find("abc", 4, 6)) # -1
```

## Reverse Search

Search from the end of string using `rfind()` and `rindex()`.

### 1. The rfind() Method

Returns the highest index where substring is found.

```python
path = "/home/user/docs/file.txt"

print(path.rfind("/"))        # 15
print(path.find("/"))         # 0

# Get filename
last_slash = path.rfind("/")
filename = path[last_slash + 1:]
print(filename)               # file.txt
```

### 2. The rindex() Method

Like `rfind()` but raises `ValueError` if not found.

```python
text = "mississippi"

print(text.rindex("i"))       # 10
print(text.rindex("s"))       # 6
print(text.rindex("issi"))    # 4
```

### 3. Practical Usage

Reverse search is useful for parsing paths and extensions.

```python
filename = "archive.tar.gz"

# Find last dot for extension
dot = filename.rfind(".")
ext = filename[dot + 1:]
print(ext)                    # gz

# Find second-to-last dot
dot2 = filename.rfind(".", 0, dot)
full_ext = filename[dot2 + 1:]
print(full_ext)               # tar.gz
```

## Counting Occurrences

The `count()` method returns the number of non-overlapping occurrences.

### 1. Basic Counting

Count how many times a substring appears.

```python
text = "banana"

print(text.count("a"))        # 3
print(text.count("na"))       # 2
print(text.count("x"))        # 0
```

### 2. Non-Overlapping

Counts are non-overlapping; matches don't share characters.

```python
text = "aaaa"

print(text.count("aa"))       # 2 (not 3)
# Matches: [aa]aa, aa[aa]
# Not: a[aa]a (overlaps)
```

### 3. Range Counting

Count within a specific range of the string.

```python
text = "abracadabra"

print(text.count("a"))           # 5
print(text.count("a", 0, 5))     # 2 (in "abrac")
print(text.count("a", 5))        # 3 (in "adabra")
```

## Prefix and Suffix

Test string boundaries with `startswith()` and `endswith()`.

### 1. Single Check

Test if string starts or ends with a specific substring.

```python
filename = "document.pdf"

print(filename.startswith("doc"))    # True
print(filename.endswith(".pdf"))     # True
print(filename.endswith(".txt"))     # False
```

### 2. Multiple Options

Pass a tuple to check against multiple possibilities.

```python
filename = "image.png"

# Check multiple extensions
image_exts = (".jpg", ".png", ".gif")
print(filename.endswith(image_exts))  # True

# Check multiple prefixes
prefixes = ("http://", "https://")
url = "https://example.com"
print(url.startswith(prefixes))       # True
```

### 3. Position Range

Specify start and end positions for bounded checks.

```python
text = "Hello, World!"

# Check "World" starts at index 7
print(text.startswith("World", 7))    # True

# Check within range
print(text.startswith("ello", 1, 5))  # True
```

## Search Patterns

Common search patterns and their implementations.

### 1. Find All Positions

Locate all occurrences of a substring.

```python
def find_all(text, sub):
    """Find all starting positions of substring."""
    positions = []
    start = 0
    while True:
        pos = text.find(sub, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

text = "abcabcabc"
print(find_all(text, "abc"))  # [0, 3, 6]
```

### 2. Word Boundaries

Check if match is a complete word, not part of another.

```python
def contains_word(text, word):
    """Check if word exists as complete word."""
    import re
    pattern = r'\b' + re.escape(word) + r'\b'
    return bool(re.search(pattern, text))

text = "I love Python programming"
print(contains_word(text, "Python"))  # True
print(contains_word(text, "Pyth"))    # False
```

### 3. Case Folding

Use `casefold()` for robust case-insensitive search.

```python
def find_insensitive(text, sub):
    """Case-insensitive find using casefold."""
    return text.casefold().find(sub.casefold())

text = "Straße in München"
print(find_insensitive(text, "STRASSE"))  # 0
print(find_insensitive(text, "münchen"))  # 10
```
