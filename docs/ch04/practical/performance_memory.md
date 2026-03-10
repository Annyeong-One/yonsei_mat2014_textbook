# Performance and Memory


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Techniques for writing efficient Python code with optimal memory usage.

## Measuring Performance

### Using `timeit`

```python
import timeit

# Time a simple statement
time = timeit.timeit('sum(range(100))', number=10000)
print(f"Time: {time:.4f}s")

# Time a function
def my_function():
    return [x**2 for x in range(1000)]

time = timeit.timeit(my_function, number=1000)
print(f"Time: {time:.4f}s")

# Compare approaches
list_time = timeit.timeit('[x**2 for x in range(1000)]', number=1000)
gen_time = timeit.timeit('list(x**2 for x in range(1000))', number=1000)
print(f"List comp: {list_time:.4f}s, Generator: {gen_time:.4f}s")
```

### Using `cProfile`

```python
import cProfile

def slow_function():
    result = []
    for i in range(10000):
        result.append(i ** 2)
    return result

# Profile the function
cProfile.run('slow_function()')
```

---

## Performance Optimizations

### Use Comprehensions

Comprehensions are faster than equivalent loops:

```python
# Fast: list comprehension
squares = [x**2 for x in range(1000)]

# Slower: explicit loop
squares = []
for x in range(1000):
    squares.append(x**2)
```

### Local Variable Caching

Accessing local variables is faster than global lookups:

```python
# Slower: global lookup each iteration
def slow():
    for i in range(10000):
        len([1, 2, 3])  # Looks up len() each time

# Faster: cache the function locally
def fast():
    _len = len  # Local reference
    for i in range(10000):
        _len([1, 2, 3])
```

### Use Built-in Functions

Built-in functions are implemented in C and optimized:

```python
# Fast: built-in sum
total = sum(numbers)

# Slower: manual loop
total = 0
for n in numbers:
    total += n

# Fast: built-in map
result = list(map(str, numbers))

# Slower: list comprehension for simple transforms
result = [str(n) for n in numbers]
```

### String Joining

```python
# Fast: join method
result = ''.join(strings)

# Slow: concatenation in loop
result = ''
for s in strings:
    result += s  # Creates new string each time
```

### Use `collections` Module

```python
from collections import Counter, defaultdict, deque

# Fast counting
counts = Counter(words)

# Fast grouping
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# Fast append/pop from both ends
queue = deque()
queue.append(item)      # O(1)
queue.appendleft(item)  # O(1)
```

---

## Memory Efficiency

### Generators for Lazy Evaluation

Generators produce values on-demand, avoiding memory allocation for entire sequences:

```python
# Memory efficient: generator expression
gen = (x**2 for x in range(10000000))

# Memory expensive: list comprehension
lst = [x**2 for x in range(10000000)]  # All in memory at once

# Generator function
def squares(n):
    for x in range(n):
        yield x**2

# Process without loading all into memory
for square in squares(10000000):
    process(square)
```

### `__slots__` for Classes

Reduce memory overhead when creating many instances:

```python
# Without __slots__: ~152 bytes per instance
class PointRegular:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__: ~56 bytes per instance
class PointSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Significant savings with many instances
points = [PointSlots(i, i) for i in range(1000000)]
```

### Use `array` for Homogeneous Data

```python
import array

# Regular list: ~8MB for 1M integers
lst = list(range(1000000))

# Array: ~4MB for 1M integers
arr = array.array('i', range(1000000))
```

### Avoid Unnecessary Copies

```python
# Creates copy (uses memory)
subset = large_list[100:200]

# Use iterator (no copy)
import itertools
subset = itertools.islice(large_list, 100, 200)

# Process in chunks
def chunked(iterable, size):
    it = iter(iterable)
    while chunk := list(itertools.islice(it, size)):
        yield chunk

for chunk in chunked(large_data, 1000):
    process(chunk)
```

### Delete Large Objects

```python
def process_large_data():
    data = load_huge_file()  # 1GB
    result = compute(data)
    
    del data  # Free memory immediately
    gc.collect()  # Optional: force garbage collection
    
    return result
```

---

## Profiling Memory

```python
import sys
import tracemalloc

# Check object size
x = [1, 2, 3]
print(sys.getsizeof(x))  # Bytes

# Track memory allocations
tracemalloc.start()

# ... your code ...
data = [x**2 for x in range(100000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

---

## Summary

### Performance Tips

| Technique | Benefit |
|-----------|---------|
| List comprehensions | Faster than loops |
| Local variable caching | Faster lookups |
| Built-in functions | C-optimized |
| `''.join()` | O(n) vs O(n²) |
| `collections` module | Optimized data structures |

### Memory Tips

| Technique | Benefit |
|-----------|---------|
| Generators | Lazy evaluation |
| `__slots__` | Smaller instances |
| `array.array` | Compact numeric storage |
| Iterators | Avoid copies |
| `del` + `gc.collect()` | Free memory early |

### Key Principles

1. **Measure before optimizing** - Use `timeit` and `cProfile`
2. **Prefer built-ins** - They're implemented in C
3. **Use appropriate data structures** - `deque`, `Counter`, etc.
4. **Think about memory** - Generators for large data
5. **Cache expensive operations** - Local variables, `lru_cache`
