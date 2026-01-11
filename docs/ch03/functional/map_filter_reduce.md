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

## filter()

### 1. Select Elements

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
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

## Summary

- map: transform
- filter: select
- reduce: accumulate
- Comprehensions often better
