# Memory Overview

Modern CPUs execute billions of instructions per second, but memory cannot deliver data that fast. The memory hierarchy bridges this gap and its behavior determines the performance of nearly all programs.

## Definition

The **memory hierarchy** is a series of storage layers with decreasing speed and increasing capacity: registers, L1/L2/L3 caches, RAM, and SSD/disk. Data moves between levels in units called **cache lines** (typically 64 bytes). The hierarchy works because programs exhibit **temporal locality** (reusing recent data) and **spatial locality** (accessing nearby addresses).

## Explanation

| Level | Size | Latency | Managed By |
|-------|------|---------|------------|
| Registers | ~1 KB | ~0.25 ns | Compiler |
| L1 Cache | ~32 KB | ~1 ns | Hardware (cache controller) |
| L2 Cache | ~256-512 KB | ~4 ns | Hardware |
| L3 Cache | ~4-32 MB | ~12 ns | Hardware |
| RAM | 8-128 GB | ~80-120 ns | OS |
| SSD | 256 GB-4 TB | ~100 us | OS |

When the CPU requests data, it checks each cache level in order. A **cache hit** returns data immediately; a **cache miss** triggers a fetch from the next level. The cache controller handles all promotion and eviction decisions in hardware, invisibly to software.

Cache lines are the fundamental transfer unit. Accessing one byte loads the entire 64-byte block containing it. This is why sequential array access is fast: paying for one miss gives the next 7 elements (for float64) free.

**Python implication**: Python lists store scattered heap objects (poor spatial locality). NumPy arrays store contiguous raw values (excellent spatial locality), which is the primary reason NumPy is dramatically faster for numerical work.

## Examples

```python
import sys

# Python object overhead: every int is a full heap object
x = 42
print(sys.getsizeof(x))  # 28 bytes (not 4 or 8!)

# List stores pointers to scattered objects
lst = [1, 2, 3]
print(sys.getsizeof(lst))  # 80 bytes (just the container)
```

```python
import numpy as np

# NumPy: contiguous raw values, no per-element overhead
arr = np.array([1, 2, 3], dtype=np.int64)
print(arr.nbytes)  # 24 bytes (8 bytes x 3, contiguous)
```

```python
import numpy as np
import time

def measure_bandwidth(size_mb):
    """Observe hierarchy effects: small arrays hit cache, large ones hit RAM."""
    n = size_mb * 1024 * 1024 // 8
    arr = np.random.rand(n)
    _ = np.sum(arr)  # warm up

    start = time.perf_counter()
    for _ in range(10):
        _ = np.sum(arr)
    elapsed = time.perf_counter() - start

    bandwidth = (n * 8 * 10) / elapsed / 1e9
    print(f"{size_mb:6.2f} MB: {bandwidth:.1f} GB/s")

for size in [0.01, 0.1, 1, 10, 100]:
    measure_bandwidth(size)
# Bandwidth drops as array size exceeds cache levels
```
