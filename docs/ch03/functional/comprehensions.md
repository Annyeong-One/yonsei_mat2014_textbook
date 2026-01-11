# Comprehensions

## List Comprehension

### 1. Basic

```python
squares = [x**2 for x in range(10)]
```

### 2. With Condition

```python
evens = [x for x in range(10) if x % 2 == 0]
```

### 3. Multiple Loops

```python
pairs = [(x, y) for x in range(3) for y in range(3)]
```

## Dict Comprehension

### 1. Create Dict

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Set Comprehension

### 1. Create Set

```python
unique_lengths = {len(word) for word in words}
```

## Nested

### 1. Flatten

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6]
```

## Summary

- Concise syntax
- List, dict, set
- Conditions supported
- Nested possible
