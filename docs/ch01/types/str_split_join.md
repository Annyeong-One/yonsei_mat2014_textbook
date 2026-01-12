# Split and Join

The `split()` and `join()` methods convert between strings and lists, enabling powerful text processing.

## Basic Split

Divide strings into lists of substrings.

### 1. Default Split

Without arguments, splits on any whitespace.

```python
s = "The brand has had its ups and downs."

words = s.split()
print(words)
# ['The', 'brand', 'has', 'had', 'its', 'ups', 'and', 'downs.']

print(type(words))  # <class 'list'>
```

### 2. Whitespace Handling

Default split handles multiple spaces and newlines.

```python
s = "  hello   world  \n  foo  "

# Default: splits on any whitespace, removes empty
print(s.split())     # ['hello', 'world', 'foo']

# Explicit space: keeps empty strings
print(s.split(" "))  # ['', '', 'hello', '', '', 'world', '', '\n', '', 'foo', '', '']
```

### 3. Custom Separator

Specify a delimiter string.

```python
s = "apple,banana,cherry"
print(s.split(","))  # ['apple', 'banana', 'cherry']

s = "one---two---three"
print(s.split("---"))  # ['one', 'two', 'three']

# Separator not found
s = "hello"
print(s.split(","))  # ['hello']
```

## Split Options

Control split behavior with parameters.

### 1. Limit Splits

Use `maxsplit` to limit number of splits.

```python
s = "a,b,c,d,e"

print(s.split(","))        # ['a', 'b', 'c', 'd', 'e']
print(s.split(",", 1))     # ['a', 'b,c,d,e']
print(s.split(",", 2))     # ['a', 'b', 'c,d,e']
```

### 2. Right Split

Use `rsplit()` to split from the right.

```python
s = "a,b,c,d,e"

print(s.rsplit(",", 1))    # ['a,b,c,d', 'e']
print(s.rsplit(",", 2))    # ['a,b,c', 'd', 'e']

# Useful for file paths
path = "/home/user/docs/file.txt"
print(path.rsplit("/", 1))  # ['/home/user/docs', 'file.txt']
```

### 3. Split Lines

Use `splitlines()` for line-based splitting.

```python
text = "line1\nline2\nline3"
print(text.splitlines())   # ['line1', 'line2', 'line3']

# Handles different line endings
text = "line1\r\nline2\rline3"
print(text.splitlines())   # ['line1', 'line2', 'line3']

# Keep line endings
print(text.splitlines(keepends=True))
# ['line1\r\n', 'line2\r', 'line3']
```

## Basic Join

Combine list elements into a string.

### 1. Join Syntax

The separator calls `join()` with an iterable.

```python
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Hello World

# Different separators
print("-".join(words))     # Hello-World
print("".join(words))      # HelloWorld
print(", ".join(words))    # Hello, World
```

### 2. From Any Iterable

Join works with any iterable of strings.

```python
# From tuple
parts = ("2025", "01", "12")
date = "-".join(parts)
print(date)  # 2025-01-12

# From generator
chars = (c.upper() for c in "hello")
print("-".join(chars))  # H-E-L-L-O

# From string (each character)
print("-".join("abc"))  # a-b-c
```

### 3. String Elements Only

Join requires all elements to be strings.

```python
# Works: all strings
words = ["a", "b", "c"]
print(" ".join(words))  # a b c

# Fails: contains non-string
# nums = [1, 2, 3]
# print(" ".join(nums))  # TypeError

# Solution: convert to strings
nums = [1, 2, 3]
print(" ".join(str(n) for n in nums))  # 1 2 3
```

## Partition Methods

Split into exactly three parts.

### 1. The partition() Method

Returns (before, separator, after) tuple.

```python
s = "hello=world"

before, sep, after = s.partition("=")
print(before)  # hello
print(sep)     # =
print(after)   # world
```

### 2. Separator Not Found

Returns (string, '', '') when separator missing.

```python
s = "hello world"

before, sep, after = s.partition("=")
print(before)  # hello world
print(sep)     # (empty string)
print(after)   # (empty string)
```

### 3. Right Partition

Use `rpartition()` to find last occurrence.

```python
s = "a=b=c=d"

# partition: first occurrence
print(s.partition("="))   # ('a', '=', 'b=c=d')

# rpartition: last occurrence
print(s.rpartition("="))  # ('a=b=c', '=', 'd')
```

## Practical Patterns

Common split/join operations.

### 1. CSV Processing

Simple CSV line parsing.

```python
line = "Alice,30,Engineer"
name, age, role = line.split(",")
print(f"{name} is a {role}")  # Alice is a Engineer

# Join back
record = ["Bob", "25", "Designer"]
csv_line = ",".join(record)
print(csv_line)  # Bob,25,Designer
```

### 2. Path Manipulation

Work with file paths.

```python
path = "/home/user/docs/file.txt"

# Get filename
parts = path.rsplit("/", 1)
filename = parts[-1]
print(filename)  # file.txt

# Build path
components = ["home", "user", "docs"]
new_path = "/" + "/".join(components)
print(new_path)  # /home/user/docs
```

### 3. Word Processing

Count words in text.

```python
text = """
adduser alias apropos arch awk
bash bg
cal cat cd chmod chown clear
"""

words = text.split()
print(f"Word count: {len(words)}")  # Word count: 11

# Filter words
long_words = [w for w in words if len(w) > 4]
print(long_words)  # ['adduser', 'alias', 'apropos', 'chmod', 'chown', 'clear']
```

## Round-Trip Patterns

Split and rejoin with modifications.

### 1. Word Transformation

Transform each word in a string.

```python
s = "hello world python"

# Capitalize each word
words = s.split()
capitalized = [w.capitalize() for w in words]
result = " ".join(capitalized)
print(result)  # Hello World Python
```

### 2. Line Processing

Process text line by line.

```python
text = "line one\nline two\nline three"

# Number each line
lines = text.splitlines()
numbered = [f"{i+1}. {line}" for i, line in enumerate(lines)]
result = "\n".join(numbered)
print(result)
# 1. line one
# 2. line two
# 3. line three
```

### 3. Filter and Rebuild

Remove unwanted elements.

```python
s = "apple, , banana, , cherry"

# Split, filter empty, rejoin
parts = s.split(", ")
filtered = [p for p in parts if p]
result = ", ".join(filtered)
print(result)  # apple, banana, cherry
```
