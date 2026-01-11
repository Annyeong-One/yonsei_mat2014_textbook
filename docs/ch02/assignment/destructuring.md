# Destructuring

## Overview

Python's unpacking as destructuring:

### 1. Sequences

```python
# Destructure tuple
point = (10, 20)
x, y = point

# Destructure list
data = [1, 2, 3]
a, b, c = data
```

### 2. Dictionaries

```python
person = {'name': 'Alice', 'age': 30}
name = person['name']
age = person['age']

# Or
name, age = person['name'], person['age']
```

## Function Returns

### 1. Multiple Returns

```python
def get_coords():
    return 10, 20, 30

x, y, z = get_coords()
```

### 2. Ignore Values

```python
def stats():
    return 100, 50, 75

mean, _, _ = stats()  # Only want mean
```

## Nested

### 1. Deep Destructuring

```python
data = [(1, 2), (3, 4), (5, 6)]
(a, b), (c, d), (e, f) = data
```

## Summary

- Unpack sequences
- Multiple return values
- Nested structures
- Use `_` to ignore
