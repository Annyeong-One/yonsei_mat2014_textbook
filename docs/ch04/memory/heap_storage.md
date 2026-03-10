# Heap Storage


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Object Allocation

### 1. All Objects

Everything on heap:

```python
x = 42              # int on heap
s = "hello"         # str on heap
lst = [1, 2, 3]     # list on heap
```

### 2. Dynamic Growth

```python
# Heap grows as needed
data = []
for i in range(1000000):
    data.append(i)  # Heap expands
```

## Object Layout

### 1. Continuous Memory

```python
# List items contiguous
lst = [1, 2, 3, 4, 5]

# In memory:
# [header][ptr1][ptr2][ptr3][ptr4][ptr5]
```

### 2. Scattered Objects

```python
# Objects anywhere on heap
a = [1, 2]
b = "hello"
c = {'key': 'value'}

# Memory not sequential
```

## Memory Pools

### 1. Small Objects

Python uses memory pools:

```python
# Small objects (< 512 bytes)
# Allocated from pools
# Faster than malloc

x = 42              # From pool
s = "hi"            # From pool
```

### 2. Large Objects

```python
# Large objects
# Direct malloc
big = [0] * 1000000
```

## Fragmentation

### 1. Can Occur

```python
# Create many objects
data = [[] for _ in range(1000)]

# Delete some
for i in range(0, 1000, 2):
    del data[i]

# Holes in memory
```

### 2. GC Helps

```python
import gc

# Force collection
gc.collect()

# Helps reduce fragmentation
```

## Object Sizes

### 1. Check Size

```python
import sys

print(sys.getsizeof(42))        # Small
print(sys.getsizeof([1, 2, 3])) # Larger
print(sys.getsizeof("hello"))   # String
```

### 2. Container Overhead

```python
# List overhead
empty_list = []
print(sys.getsizeof(empty_list))  # ~56 bytes

# Plus items
lst = [1, 2, 3]
print(sys.getsizeof(lst))  # ~80 bytes
```

## Lifetime

### 1. Until GC'd

```python
x = [1, 2, 3]       # Created
# Lives on heap
del x               # Reference removed
# Eventually GC'd
```

### 2. Reference Counting

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2

y = x
print(sys.getrefcount(x))  # 3

del y
print(sys.getrefcount(x))  # 2
```

## Heap vs Stack

### 1. Comparison

```python
def function():
    # Local name on stack
    x = [1, 2, 3]   # Object on heap
    
    # x removed from stack at return
    # Object stays until GC'd
    return x
```

## Summary

### 1. Heap

- All objects stored here
- Dynamic size
- Slower than stack
- Manual/GC management

### 2. Memory Management

- Pools for small objects
- Direct allocation for large
- Fragmentation possible
- GC handles cleanup
