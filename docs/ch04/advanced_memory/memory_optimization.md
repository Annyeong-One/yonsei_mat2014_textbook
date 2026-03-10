# Memory Optimization


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Techniques for reducing memory usage and tools for profiling memory consumption.

## Optimization Techniques

### Use `__slots__`

Eliminate per-instance `__dict__` overhead:

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Saves ~100+ bytes per instance
points = [Point(i, i) for i in range(1000000)]
```

### Prefer Generators Over Lists

Generators produce values on-demand without storing all in memory:

```python
# Bad: entire list in memory
def get_numbers_list():
    return [x ** 2 for x in range(1000000)]

# Good: generator yields one at a time
def get_numbers_gen():
    return (x ** 2 for x in range(1000000))

# Or generator function
def get_numbers():
    for x in range(1000000):
        yield x ** 2
```

### Use `itertools` for Memory Efficiency

```python
import itertools

# Process without loading all data
for item in itertools.islice(huge_iterator, 100):
    process(item)

# Chain iterators without concatenating
for item in itertools.chain(iter1, iter2, iter3):
    process(item)

# Filter without creating intermediate list
for item in itertools.filterfalse(is_bad, data):
    process(item)
```

### Use Appropriate Data Structures

```python
# For many small integers, use array
import array
arr = array.array('i', range(1000000))  # Much smaller than list

# For boolean flags, use bitarray or integers
flags = 0
flags |= (1 << 0)  # Set flag 0
flags |= (1 << 3)  # Set flag 3

# For sparse data, use dict instead of list
sparse_data = {0: 'a', 1000000: 'b'}  # Not [0]*1000001
```

### Avoid Unnecessary Copies

```python
# Bad: creates copy
def process(data):
    data = list(data)  # Unnecessary copy
    return sum(data)

# Good: work with original
def process(data):
    return sum(data)

# Use slices carefully
big_list = list(range(1000000))
# Bad: creates copy
subset = big_list[100:200]
# Consider: itertools.islice for iteration
```

### Delete Unused Large Objects

```python
def process_large_file():
    data = load_huge_file()  # 1GB in memory
    result = compute(data)
    del data  # Free memory immediately
    return result
```

---

## Memory Profiling

### `sys.getsizeof()`

Get the size of a single object:

```python
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))  # ~88 bytes (list object itself)

# Note: doesn't include referenced objects
nested = [[1, 2], [3, 4]]
print(sys.getsizeof(nested))  # Only the outer list size
```

### Deep Size Calculation

```python
import sys

def deep_getsizeof(obj, seen=None):
    """Recursively calculate size of objects."""
    if seen is None:
        seen = set()
    
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    
    size = sys.getsizeof(obj)
    
    if isinstance(obj, dict):
        size += sum(deep_getsizeof(k, seen) + deep_getsizeof(v, seen) 
                   for k, v in obj.items())
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
        size += sum(deep_getsizeof(i, seen) for i in obj)
    
    return size

nested = [[1, 2], [3, 4], {'a': [5, 6]}]
print(deep_getsizeof(nested))  # Total size including contents
```

### `tracemalloc` Module

Track memory allocations:

```python
import tracemalloc

tracemalloc.start()

# ... your code ...
data = [x ** 2 for x in range(100000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

### Finding Memory Hogs

```python
import tracemalloc

tracemalloc.start()

# Your code here
data = load_data()
process(data)

# Take snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("Top 10 memory allocations:")
for stat in top_stats[:10]:
    print(stat)
```

### Comparing Snapshots

```python
import tracemalloc

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

# Code that might leak
data = create_large_data()

snapshot2 = tracemalloc.take_snapshot()

# Compare
top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("Memory changes:")
for stat in top_stats[:10]:
    print(stat)
```

### Memory Profiler Package

For line-by-line profiling (install: `pip install memory-profiler`):

```python
from memory_profiler import profile

@profile
def my_function():
    a = [1] * 1000000
    b = [2] * 2000000
    del b
    return a

my_function()
```

Output:
```
Line #    Mem usage    Increment   Line Contents
================================================
     3     38.0 MiB     38.0 MiB   @profile
     4                             def my_function():
     5     45.6 MiB      7.6 MiB       a = [1] * 1000000
     6     61.0 MiB     15.3 MiB       b = [2] * 2000000
     7     45.6 MiB    -15.3 MiB       del b
     8     45.6 MiB      0.0 MiB       return a
```

---

## Common Memory Issues

### Circular References

```python
# Problem: circular reference
class Node:
    def __init__(self):
        self.parent = None
        self.children = []

parent = Node()
child = Node()
parent.children.append(child)
child.parent = parent  # Circular!

# Solution: use weak references
import weakref

class Node:
    def __init__(self):
        self._parent = None
        self.children = []
    
    @property
    def parent(self):
        return self._parent() if self._parent else None
    
    @parent.setter
    def parent(self, value):
        self._parent = weakref.ref(value) if value else None
```

### Growing Caches

```python
# Problem: unbounded cache
cache = {}

def get_data(key):
    if key not in cache:
        cache[key] = expensive_compute(key)
    return cache[key]

# Solution: bounded cache
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_data(key):
    return expensive_compute(key)
```

---

## Summary

| Technique | Memory Saving | Complexity |
|-----------|--------------|------------|
| `__slots__` | ~100 bytes/instance | Low |
| Generators | Significant | Low |
| `array.array` | 4-8x for numbers | Low |
| Memory views | Avoids copies | Medium |
| Object pools | Reduces allocations | Medium |

Profiling tools:
- `sys.getsizeof()`: Quick object size
- `tracemalloc`: Detailed allocation tracking
- `memory_profiler`: Line-by-line analysis

Key points:
- Profile before optimizing
- Use generators for large sequences
- Choose appropriate data structures
- Watch for memory leaks and circular references
- Delete large objects when no longer needed
