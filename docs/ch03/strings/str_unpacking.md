# String Unpacking

Strings are iterable sequences, allowing their characters to be unpacked into individual variables using Python's assignment syntax.

## Basic Unpacking

Assign each character of a string to separate variables.

### 1. Simple Assignment

The number of variables must match the string length.

```python
word = "hello"
a, b, c, d, e = word

print(a)  # h
print(b)  # e
print(c)  # l
print(d)  # l
print(e)  # o
```

### 2. Length Mismatch

Unpacking fails if variable count doesn't match string length.

```python
word = "hi"

# Too many variables - ValueError
# a, b, c = word

# Too few variables - ValueError
# a = word  # This works (single assignment)
# a, = word  # ValueError: too many values

# Correct
a, b = word
print(a, b)  # h i
```

### 3. Tuple Context

Parentheses are optional but can improve readability.

```python
word = "abc"

# Without parentheses
a, b, c = word

# With parentheses (equivalent)
(a, b, c) = word

# In expressions
first, second, third = "xyz"
print(first, second, third)  # x y z
```

## Underscore Placeholder

Use `_` to ignore unwanted characters during unpacking.

### 1. Ignoring Positions

Convention uses `_` for values you don't need.

```python
word = "hippo"

# Only need middle character
_, _, c, _, _ = word
print(c)  # p

# Only need first and last
first, _, _, _, last = word
print(first, last)  # h o
```

### 2. Multiple Ignores

Each `_` is a valid variable that gets reassigned.

```python
word = "abcde"

_, _, middle, _, _ = word
print(middle)  # c

# Note: _ is reassigned each time
a, _, _, _, e = word
print(_)  # d (last assigned value)
```

### 3. Readability Trade-off

Too many underscores reduce readability; consider slicing instead.

```python
word = "hello"

# Unpacking approach
_, _, c, d, _ = word

# Slicing approach (often clearer)
c, d = word[2], word[3]
# Or
c, d = word[2:4]
```

## Star Unpacking

Use `*` to collect multiple characters into a list.

### 1. Collect Remaining

Star captures remaining elements as a list.

```python
word = "hello"

first, *rest = word
print(first)  # h
print(rest)   # ['e', 'l', 'l', 'o']

*start, last = word
print(start)  # ['h', 'e', 'l', 'l']
print(last)   # o
```

### 2. Middle Collection

Place star in any position to collect middle elements.

```python
word = "hippo"

first, *middle, last = word
print(first)   # h
print(middle)  # ['i', 'p', 'p']
print(last)    # o

a, b, *rest = word
print(a, b)    # h i
print(rest)    # ['p', 'p', 'o']
```

### 3. Star with Underscore

Combine `*_` to ignore multiple characters.

```python
word = "hello"

# Get only first and last
first, *_, last = word
print(first, last)  # h o

# Get specific positions
_, _, *middle, _ = word
print(middle)  # ['l', 'l']

# Ignore everything except last two
*_, second_last, last = word
print(second_last, last)  # l o
```

## Type Behavior

Understand what unpacking produces.

### 1. Variables Are Strings

Individual unpacked characters are single-character strings.

```python
word = "abc"
a, b, c = word

print(type(a))  # <class 'str'>
print(len(a))   # 1
print(a == "a") # True
```

### 2. Star Produces List

Star unpacking always produces a list, not a string.

```python
word = "hello"

first, *rest = word
print(type(rest))  # <class 'list'>
print(rest)        # ['e', 'l', 'l', 'o']

# Convert back to string if needed
rest_str = "".join(rest)
print(rest_str)    # ello
```

### 3. Empty Star Result

Star can capture zero elements, producing empty list.

```python
word = "ab"

first, *middle, last = word
print(first)   # a
print(middle)  # [] (empty list)
print(last)    # b

# Minimum: star needs at least 0 elements
a, *b, c = "xy"
print(b)  # []
```

## Practical Patterns

Common use cases for string unpacking.

### 1. Swap Characters

Unpack and repack to rearrange.

```python
def swap_ends(s):
    """Swap first and last characters."""
    if len(s) < 2:
        return s
    first, *middle, last = s
    return last + "".join(middle) + first

print(swap_ends("hello"))  # oellh
print(swap_ends("ab"))     # ba
```

### 2. Parse Fixed Format

Unpack strings with known structure.

```python
# Date string YYYYMMDD
date_str = "20250112"
y1, y2, y3, y4, m1, m2, d1, d2 = date_str
year = y1 + y2 + y3 + y4
month = m1 + m2
day = d1 + d2
print(f"{year}-{month}-{day}")  # 2025-01-12

# Simpler with slicing for this case
year, month, day = date_str[:4], date_str[4:6], date_str[6:]
```

### 3. Iteration Unpacking

Unpack during iteration over strings.

```python
pairs = ["ab", "cd", "ef"]

for first, second in pairs:
    print(f"{first} -> {second}")
# a -> b
# c -> d
# e -> f

# With enumerate
word = "abc"
for i, char in enumerate(word):
    print(f"{i}: {char}")
```

## Limitations

Understand unpacking constraints.

### 1. Single Star Only

Only one starred expression is allowed.

```python
word = "hello"

# Valid
first, *middle, last = word

# Invalid - multiple stars
# *start, middle, *end = word  # SyntaxError
```

### 2. Minimum Variables

Need at least as many non-star variables as required.

```python
# Need minimum 2 characters for this pattern
first, *middle, last = "ab"  # Works
# first, *middle, last = "a"   # ValueError

# Star alone works with any length
*all_chars, = "a"
print(all_chars)  # ['a']
```

### 3. Performance Note

Unpacking creates new objects; for large strings, consider slicing.

```python
# For large strings, slicing is more efficient
large = "a" * 10000

# Creates 10000 string objects
# a, *rest = large  # Slow

# Creates just one new string
first = large[0]
rest = large[1:]   # Fast
```
