# Buffer Reallocation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## List Growth

### 1. Dynamic Arrays

Lists grow dynamically:

```python
lst = []
for i in range(100):
    lst.append(i)
    # May trigger reallocation
```

### 2. Capacity

```python
import sys

lst = []
print(sys.getsizeof(lst))  # Initial

lst.append(1)
print(sys.getsizeof(lst))  # Grew

# Over-allocates for efficiency
```

## Growth Strategy

### 1. Exponential

```python
# CPython strategy:
# new_capacity = old_capacity + (old_capacity >> 3) + 6

# Example progression:
# 0 -> 4 -> 8 -> 16 -> 25 -> 35 -> ...
```

### 2. Amortized O(1)

```python
# Average append is O(1)
# Occasional reallocation is O(n)
# Amortized: O(1)

lst = []
for i in range(1000):
    lst.append(i)  # Fast on average
```

## Pre-allocation

### 1. If Known Size

```python
# Inefficient
lst = []
for i in range(1000):
    lst.append(i)

# Better: pre-allocate
lst = [0] * 1000
for i in range(1000):
    lst[i] = i
```

### 2. List Comprehension

```python
# Also pre-allocates
lst = [i for i in range(1000)]
```

## Memory Impact

### 1. Over-allocation

```python
import sys

lst = [1, 2, 3]
print(sys.getsizeof(lst))  # e.g., 80

# Has extra capacity
# Not just 3 items worth
```

### 2. Shrinking

```python
# Doesn't automatically shrink
lst = list(range(1000))
size1 = sys.getsizeof(lst)

del lst[100:]
size2 = sys.getsizeof(lst)

# size2 may equal size1
```

## Summary

### 1. Dynamic Growth

- Lists grow automatically
- Exponential strategy
- Over-allocates
- Amortized O(1) append

### 2. Optimization

- Pre-allocate when possible
- Use comprehensions
- Avoid many appends
