# Memory Access Patterns

The order in which your code accesses memory can cause 10-100x performance differences on the same data. Access patterns determine cache hit rates and are the single most important factor in memory-bound performance.

## Definition

A **memory access pattern** describes the order in which a program reads or writes memory addresses. **Sequential access** visits addresses in order, achieving near-optimal cache utilization. **Strided access** skips elements at regular intervals, wasting portions of each loaded cache line. **Random access** visits unpredictable addresses, causing frequent cache misses.

## Explanation

When the CPU accesses one address, it loads an entire **cache line** (64 bytes) containing that address. Sequential access exploits this: accessing `arr[0]` loads `arr[0]` through `arr[7]` (for float64), giving 87.5% hit rate. Random access wastes most of each loaded cache line and defeats hardware prefetching.

For 2D arrays, memory layout matters critically. NumPy defaults to **row-major** (C order), so iterating row-by-row is sequential in memory while column-by-column is strided, hitting a different cache line on each access.

**Optimization techniques**: (1) match traversal order to memory layout, (2) use blocking/tiling to keep working sets in cache, (3) prefer Structure of Arrays (SoA) over Array of Structures for single-field access, (4) use NumPy vectorized operations that handle optimal access patterns internally.

## Examples

```python
import numpy as np
import time

arr = np.arange(10_000_000, dtype=np.float64)

# Sequential: cache-friendly (1 miss per 8 accesses)
start = time.perf_counter()
_ = np.sum(arr)
seq_time = time.perf_counter() - start

# Random: cache-hostile (gather step causes random reads)
indices = np.random.permutation(len(arr))
start = time.perf_counter()
_ = np.sum(arr[indices])
rand_time = time.perf_counter() - start

print(f"Sequential: {seq_time*1000:.1f} ms")
print(f"Random:     {rand_time*1000:.1f} ms")
print(f"Ratio:      {rand_time/seq_time:.1f}x")
```

```python
import numpy as np

# Row-major (C order): row iteration is sequential, column is strided
arr = np.random.rand(10000, 10000)

# Fast: sum along rows (sequential in memory)
row_sum = np.sum(arr, axis=1)

# Slower: sum along columns (strided in memory)
col_sum = np.sum(arr, axis=0)
```

```python
import numpy as np

# Structure of Arrays: cache-friendly for single-field access
class ParticleSystem:
    def __init__(self, n):
        self.x = np.zeros(n)     # contiguous
        self.y = np.zeros(n)     # contiguous
        self.mass = np.zeros(n)  # contiguous

system = ParticleSystem(1_000_000)
total_mass = np.sum(system.mass)  # sequential access through one array
```
