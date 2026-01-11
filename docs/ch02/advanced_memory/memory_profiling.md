# Memory Profiling

## Tools

### 1. sys.getsizeof

```python
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))  # Bytes
```

### 2. tracemalloc

```python
import tracemalloc

tracemalloc.start()

# ... code ...

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 10**6} MB")
print(f"Peak: {peak / 10**6} MB")

tracemalloc.stop()
```

## Analysis

### 1. Top Allocations

```python
import tracemalloc

tracemalloc.start()

# Code here

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:5]:
    print(stat)
```

## Summary

- Use sys.getsizeof for size
- Use tracemalloc for tracking
- Analyze snapshots
