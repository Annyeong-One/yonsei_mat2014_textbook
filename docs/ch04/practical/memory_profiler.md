# memory_profiler


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `memory_profiler` module tracks memory usage at the line level, helping identify memory leaks and inefficient memory access patterns.

---

## Installation

```bash
pip install memory_profiler
```

## Basic Usage

```python
# memory_example.py
from memory_profiler import profile

@profile
def create_list():
    large_list = [i ** 2 for i in range(100000)]
    filtered = [x for x in large_list if x % 2 == 0]
    return filtered

if __name__ == "__main__":
    result = create_list()
```

Run with:
```
python -m memory_profiler memory_example.py
```

## Output Format

```
Filename: memory_example.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     3   38.4 MiB      0.0 MiB           1   @profile
     4                                        def create_list():
     5   42.8 MiB      4.4 MiB           1       large_list = [i ** 2 for i in range(100000)]
     6   43.2 MiB      0.4 MiB           1       filtered = [x for x in large_list if x % 2 == 0]
     7                                        return filtered
```

## Programmatic Memory Profiling

```python
from memory_profiler import profile

def process_arrays():
    # This will be tracked
    arr1 = list(range(1000000))
    arr2 = [x ** 2 for x in arr1]
    del arr1  # Memory freed
    return arr2

# Get memory without decorator
from memory_profiler import show_results

profile(process_arrays)()
```

## Memory Optimization Patterns

```python
# Inefficient: creates multiple intermediate lists
def inefficient():
    data = [i for i in range(100000)]
    filtered = [x for x in data if x > 50000]
    squared = [x ** 2 for x in filtered]
    return squared

# Efficient: single pass generator
def efficient():
    return (x ** 2 for x in range(100000) if x > 50000)
```

## Practical Tips

- Use generators instead of list comprehensions for large datasets
- Delete large objects explicitly when done: `del large_obj`
- Profile before and after optimization
- Monitor peak memory usage, not just line-by-line
