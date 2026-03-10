# Unpacking and Destructuring


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides powerful syntax for extracting values from sequences and assigning them to multiple variables.

## Basic Unpacking

### Tuple Unpacking

```python
point = (10, 20)
x, y = point

print(x, y)  # 10 20
```

### List Unpacking

```python
data = [1, 2, 3]
a, b, c = data

print(a, b, c)  # 1 2 3
```

### String Unpacking

```python
chars = "ABC"
a, b, c = chars

print(a, b, c)  # A B C
```

## Star Unpacking (Extended Unpacking)

### Collect Remaining Elements

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

### First and Last

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Ignore with Underscore

```python
first, *_, last = range(10)
print(first, last)  # 0 9
```

### Head and Tail Pattern

```python
head, *tail = [1, 2, 3, 4, 5]
# head = 1
# tail = [2, 3, 4, 5]
```

## Nested Unpacking

### Nested Tuples

```python
data = [(1, 2), (3, 4)]
(a, b), (c, d) = data

print(a, b, c, d)  # 1 2 3 4
```

### Mixed Structures

```python
data = (1, [2, 3], 4)
a, [b, c], d = data

print(a, b, c, d)  # 1 2 3 4
```

### Deep Nesting

```python
data = [(1, 2), (3, 4), (5, 6)]
(a, b), (c, d), (e, f) = data

print(a, b, c, d, e, f)  # 1 2 3 4 5 6
```

---

## Destructuring Patterns

### Function Return Values

```python
def get_coords():
    return 10, 20, 30

x, y, z = get_coords()
print(x, y, z)  # 10 20 30
```

### Ignore Unwanted Values

```python
def stats():
    return 100, 50, 75  # mean, min, max

mean, _, _ = stats()  # Only want mean
print(mean)  # 100
```

### Dictionary Access

```python
person = {'name': 'Alice', 'age': 30}

# Extract specific values
name, age = person['name'], person['age']

# Or use .values() if order is guaranteed (Python 3.7+)
name, age = person.values()
```

### Loop Destructuring

```python
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"x={x}, y={y}")
```

### Enumerate Destructuring

```python
items = ['a', 'b', 'c']

for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### Dictionary Items

```python
person = {'name': 'Alice', 'age': 30}

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Dictionary Unpacking

### Function Arguments

```python
def func(a, b, c):
    return a + b + c

data = {'a': 1, 'b': 2, 'c': 3}
result = func(**data)  # Unpack dict as keyword args
print(result)  # 6
```

### Merging Dictionaries

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

## Walrus Operator (`:=`)

The walrus operator (Python 3.8+) assigns a value and returns it in a single expression.

### Basic Syntax

```python
# := assigns AND returns value
if (n := len(data)) > 10:
    print(f"Long list: {n} items")
```

### Avoiding Repeated Computation

```python
# Before (computes len twice)
data = input()
if len(data) > 5:
    print(f"Long: {len(data)}")

# After (computes once)
if (n := len(data)) > 5:
    print(f"Long: {n}")
```

### While Loops

```python
# Read until empty
while (line := input("Enter: ")) != "":
    print(f"You entered: {line}")
```

### List Comprehensions

```python
# Reuse computed value
results = [y for x in data if (y := expensive(x)) > 0]
```

### Pattern Matching

```python
import re

if (match := re.search(r'\d+', text)):
    print(f"Found number: {match.group()}")
```

### If-Elif Chains

```python
if (match := pattern1.search(text)):
    handle_pattern1(match)
elif (match := pattern2.search(text)):
    handle_pattern2(match)
else:
    handle_no_match()
```

---

## Summary

| Pattern | Syntax | Example |
|---------|--------|---------|
| Basic unpacking | `a, b = iterable` | `x, y = (1, 2)` |
| Star unpacking | `first, *rest = iterable` | `head, *tail = [1,2,3]` |
| Nested | `(a, b), (c, d) = nested` | `(x, y), z = ((1,2), 3)` |
| Ignore values | `a, _, c = iterable` | `first, *_, last = data` |
| Dict unpacking | `**dict` | `func(**kwargs)` |
| Walrus | `(name := expr)` | `if (n := len(x)) > 0:` |

Key points:
- Use unpacking to extract values cleanly
- `*` collects remaining elements into a list
- `_` is convention for ignored values
- Walrus operator combines assignment and expression
- Works in loops, comprehensions, and conditions
