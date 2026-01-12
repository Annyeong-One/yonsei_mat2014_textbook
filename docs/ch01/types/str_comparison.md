# String Comparison

Python strings support comparison using standard operators. Comparisons follow lexicographic ordering based on Unicode code points.

## Equality Testing

The `==` and `!=` operators test if strings have identical content.

### 1. Basic Equality

Two strings are equal if they contain the same sequence of characters.

```python
a = "hello"
b = "hello"
c = "Hello"

print(a == b)    # True
print(a == c)    # False (case differs)
print(a != c)    # True
```

### 2. Case Sensitivity

String equality is case-sensitive by default.

```python
s1 = "Python"
s2 = "python"
s3 = "PYTHON"

print(s1 == s2)                  # False
print(s1.lower() == s2.lower())  # True
print(s1.upper() == s3)          # True
```

### 3. Identity vs Equality

Use `==` for content comparison, `is` for identity.

```python
a = "hello"
b = "hello"
c = "".join(["h", "e", "l", "l", "o"])

print(a == b)    # True (same content)
print(a == c)    # True (same content)
print(a is b)    # True (interned)
print(a is c)    # False (different objects)
```

## Lexicographic Order

Comparison operators `<`, `<=`, `>`, `>=` use lexicographic ordering.

### 1. Character by Character

Strings are compared character by character using Unicode code points.

```python
print("apple" < "banana")    # True ('a' < 'b')
print("apple" < "apply")     # True ('e' < 'y')
print("abc" < "abcd")        # True (shorter)
```

### 2. Unicode Code Points

Each character's Unicode value determines its order.

```python
# ASCII values
print(ord("A"))    # 65
print(ord("Z"))    # 90
print(ord("a"))    # 97
print(ord("z"))    # 122

# Uppercase comes before lowercase
print("Z" < "a")   # True (90 < 97)
print("Apple" < "apple")  # True
```

### 3. Numeric Strings

Digit characters compare by their code points, not numeric value.

```python
# String comparison (lexicographic)
print("9" > "10")     # True ('9' > '1')
print("100" < "20")   # True ('1' < '2')

# For numeric comparison, convert to int
print(int("9") > int("10"))   # False
print(int("100") < int("20")) # False
```

## Case Handling

Methods for case-insensitive comparison.

### 1. Using lower()

Convert both strings to lowercase for comparison.

```python
s1 = "Hello"
s2 = "HELLO"

print(s1.lower() == s2.lower())  # True

# Sorting case-insensitive
words = ["Banana", "apple", "Cherry"]
sorted_words = sorted(words, key=str.lower)
print(sorted_words)  # ['apple', 'Banana', 'Cherry']
```

### 2. Using casefold()

More aggressive case folding for international text.

```python
# German sharp s
s1 = "straße"
s2 = "STRASSE"

print(s1.lower() == s2.lower())      # False
print(s1.casefold() == s2.casefold())  # True

# casefold handles special cases
print("ß".casefold())   # ss
print("ß".lower())      # ß
```

### 3. Locale Comparison

For locale-aware sorting, use the `locale` module.

```python
import locale

# Set locale (system-dependent)
locale.setlocale(locale.LC_ALL, '')

words = ["éclair", "apple", "Éclair"]

# Default sort (by code point)
print(sorted(words))
# ['apple', 'Éclair', 'éclair']

# Locale-aware sort
print(sorted(words, key=locale.strxfrm))
# Order varies by locale settings
```

## Comparison Methods

String methods that perform specialized comparisons.

### 1. Prefix Comparison

Check if strings share common prefixes.

```python
import os

def common_prefix(s1, s2):
    """Find common prefix of two strings."""
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

print(common_prefix("python", "pyre"))    # "py"
print(common_prefix("hello", "world"))    # ""

# Using os.path for paths
paths = ["/home/user/docs", "/home/user/pics"]
print(os.path.commonprefix(paths))  # "/home/user/"
```

### 2. Similarity Comparison

Check approximate equality for fuzzy matching.

```python
def similarity_ratio(s1, s2):
    """Calculate similarity ratio between strings."""
    from difflib import SequenceMatcher
    return SequenceMatcher(None, s1, s2).ratio()

print(similarity_ratio("python", "pyhton"))  # 0.833...
print(similarity_ratio("hello", "hallo"))    # 0.8
print(similarity_ratio("abc", "xyz"))        # 0.0
```

### 3. Content Classification

Use string methods to classify content type.

```python
# Character type checks
print("abc".isalpha())      # True
print("123".isdigit())      # True
print("abc123".isalnum())   # True
print("   ".isspace())      # True

# Case checks
print("HELLO".isupper())    # True
print("hello".islower())    # True
print("Title".istitle())    # True
```

## Sorting Strings

Apply comparison operations to sort string collections.

### 1. Default Sorting

Default sort uses lexicographic ordering.

```python
words = ["banana", "Apple", "cherry", "date"]

print(sorted(words))
# ['Apple', 'banana', 'cherry', 'date']

# Reverse order
print(sorted(words, reverse=True))
# ['date', 'cherry', 'banana', 'Apple']
```

### 2. Custom Key Function

Provide a key function for custom sort order.

```python
words = ["banana", "Apple", "cherry", "Date"]

# Case-insensitive sort
print(sorted(words, key=str.lower))
# ['Apple', 'banana', 'cherry', 'Date']

# Sort by length, then alphabetically
print(sorted(words, key=lambda x: (len(x), x.lower())))
# ['Date', 'Apple', 'banana', 'cherry']
```

### 3. Natural Sorting

Sort strings containing numbers in natural order.

```python
def natural_key(s):
    """Key for natural sorting of strings with numbers."""
    import re
    return [
        int(c) if c.isdigit() else c.lower()
        for c in re.split(r'(\d+)', s)
    ]

files = ["file10.txt", "file2.txt", "file1.txt"]

# Lexicographic (wrong for humans)
print(sorted(files))
# ['file1.txt', 'file10.txt', 'file2.txt']

# Natural order (human-expected)
print(sorted(files, key=natural_key))
# ['file1.txt', 'file2.txt', 'file10.txt']
```

## Edge Cases

Handle special comparison scenarios.

### 1. Empty Strings

Empty string is less than any non-empty string.

```python
print("" < "a")      # True
print("" == "")      # True
print("" < " ")      # True (space has code point 32)
```

### 2. Unicode Normalization

Visually identical strings may differ at byte level.

```python
import unicodedata

# Two ways to represent "é"
s1 = "é"                    # Single character
s2 = "e\u0301"              # e + combining accent

print(s1 == s2)             # False
print(len(s1), len(s2))     # 1, 2

# Normalize for comparison
n1 = unicodedata.normalize("NFC", s1)
n2 = unicodedata.normalize("NFC", s2)
print(n1 == n2)             # True
```

### 3. Whitespace Handling

Consider trimming whitespace before comparison.

```python
s1 = "hello"
s2 = "  hello  "

print(s1 == s2)              # False
print(s1 == s2.strip())      # True

# Normalize all whitespace
import re
def normalize_ws(s):
    return re.sub(r'\s+', ' ', s.strip())

s3 = "hello   world"
s4 = "hello world"
print(normalize_ws(s3) == s4)  # True
```
