# Map Filter Reduce

## map()

### 1. Transform Elements

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### 2. Multiple Iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]
```

### 3. Lazy Iterator

`map()` returns an iterator, not a list. Values are computed on demand.

```python
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(squares)        # <map object at 0x...>
print(list(squares))  # [1, 4, 9, 16]
```

## filter()

### 1. Select Elements

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
```

### 2. Lazy Iterator

`filter()` also returns an iterator.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(evens)        # <filter object at 0x...>
print(list(evens))  # [2, 4, 6]
```

## reduce()

### 1. Accumulate

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15
```

### 2. With Initial

```python
product = reduce(lambda x, y: x * y, numbers, 1)
print(product)  # 120
```

## Comprehensions Alternative

### 1. More Pythonic

```python
# map equivalent
squared = [x**2 for x in numbers]

# filter equivalent
evens = [x for x in numbers if x % 2 == 0]
```

## Functional Composition

Chain filter, map, and reduce for data pipelines.

### 1. Pipeline Example

```python
from functools import reduce

names = ["Alice", "Bob", "Charlie", "David"]

# filter → map → reduce
result = reduce(
    lambda a, b: a + " & " + b,
    map(str.upper, filter(lambda name: len(name) > 4, names))
)

print(result)  # ALICE & CHARLIE & DAVID
```

### 2. Step by Step

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: filter evens
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: map to squares
squares = map(lambda x: x ** 2, evens)

# Step 3: reduce to sum
total = reduce(lambda x, y: x + y, squares)

print(total)  # 56 (4 + 16 + 36)
```

## Summary

- map: transform
- filter: select
- reduce: accumulate
- Comprehensions often better
