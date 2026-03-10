# RAM (Main Memory)

RAM is the working memory where running programs and their data reside. Its capacity limits how much data you can process at once, and its bandwidth is often the bottleneck for data-intensive Python code.

## Definition

**RAM (Random Access Memory)** is volatile main memory that stores active programs, data, and OS components. Modern systems use **DRAM** (Dynamic RAM), which stores bits as charge in capacitors that require periodic refresh (~64 ms). **DDR** (Double Data Rate) transfers data on both clock edges, with each generation (DDR4, DDR5) roughly doubling bandwidth.

## Explanation

RAM latency (~80-120 ns for a row miss) is 200-300x slower than a CPU cycle. Access time depends on whether the requested row is already open in the DRAM row buffer: a **row hit** (~20 ns) is much faster than a **row miss** (~80-120 ns) which requires closing and opening rows.

| Generation | Transfer Rate | Bandwidth (per channel) |
|------------|--------------|------------------------|
| DDR4 | 3200 MT/s | ~25 GB/s |
| DDR5 | 6400 MT/s | ~50 GB/s |

Multi-channel configurations multiply bandwidth (dual-channel roughly doubles it).

**Python memory layout**: Every Python object lives on the heap with metadata overhead (28+ bytes per integer). Python's pymalloc allocator optimizes for the many small, short-lived objects typical of Python programs. NumPy arrays also live on the heap but store raw values contiguously with no per-element overhead, making them both more memory-efficient and more cache-friendly.

## Examples

```python
import sys

# Python objects have significant per-object overhead
print(sys.getsizeof(42))       # 28 bytes
print(sys.getsizeof("hello"))  # 54 bytes
print(sys.getsizeof([1,2,3]))  # 80 bytes (plus 28*3 for the ints)
```

```python
import numpy as np

# NumPy: contiguous, minimal overhead
arr = np.zeros(125_000_000, dtype=np.float64)
print(f"Size: {arr.nbytes / 1e9:.1f} GB")  # 1.0 GB
print(f"Contiguous: {arr.flags['C_CONTIGUOUS']}")  # True
```

```python
import numpy as np

# Memory-mapped files: work with arrays larger than RAM
mmap_arr = np.memmap('large_array.dat',
                      dtype='float64',
                      mode='w+',
                      shape=(100_000_000,))  # 800 MB on disk
mmap_arr[0] = 42.0
print(mmap_arr[0])  # 42.0 (OS pages data in/out transparently)
```
