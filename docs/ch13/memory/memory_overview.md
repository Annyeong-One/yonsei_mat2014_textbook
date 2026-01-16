# Memory Overview

## The Memory Problem

Modern CPUs can execute billions of instructions per second, but memory cannot deliver data that fast. This fundamental mismatch shapes all of computing.

```
The Speed Gap

CPU Speed:     ████████████████████████████████  (4 GHz = 0.25 ns/cycle)
L1 Cache:      ████████████                      (~1 ns)
L2 Cache:      ██████████████                    (~3 ns)
L3 Cache:      ████████████████████              (~10 ns)
RAM:           ████████████████████████████████████████████████  (~60 ns)
SSD:           ████████████████████████████████████████████████████  (~100,000 ns)

CPU waits 240 cycles for RAM, 400,000 cycles for SSD!
```

## The Memory Hierarchy

To bridge this gap, computers use a **hierarchy** of memory types—each level trades capacity for speed:

```
                    ┌─────────────┐
                    │  Registers  │  ← Fastest, smallest
                    │   (~1 KB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L1 Cache   │
                    │  (~64 KB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L2 Cache   │
                    │  (~256 KB)  │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  L3 Cache   │
                    │  (~8 MB)    │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │    RAM      │
                    │  (~16 GB)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │   Storage   │  ← Slowest, largest
                    │  (~1 TB)    │
                    └─────────────┘
```

## Hierarchy Properties

Each level has distinct characteristics:

| Level | Size | Latency | Bandwidth | Managed By |
|-------|------|---------|-----------|------------|
| **Registers** | ~1 KB | 0.25 ns | N/A | Compiler |
| **L1 Cache** | 32-64 KB | 1 ns | ~1 TB/s | Hardware |
| **L2 Cache** | 256-512 KB | 3 ns | ~500 GB/s | Hardware |
| **L3 Cache** | 4-32 MB | 10 ns | ~200 GB/s | Hardware |
| **RAM** | 8-128 GB | 60 ns | ~50 GB/s | OS |
| **SSD** | 256 GB-4 TB | 100 μs | ~5 GB/s | OS |
| **HDD** | 1-20 TB | 10 ms | ~200 MB/s | OS |

## Why Hierarchy Works: Locality

The hierarchy exploits two types of **locality**:

### Temporal Locality

Recently accessed data is likely to be accessed again soon.

```python
# Temporal locality: 'total' accessed repeatedly
total = 0
for i in range(1000000):
    total += i  # 'total' stays in register/cache
```

### Spatial Locality

Data near recently accessed data is likely to be accessed soon.

```python
# Spatial locality: array elements are adjacent in memory
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(arr)):
    print(arr[i])  # Sequential access → prefetching works
```

## Cache Mechanics

When the CPU needs data:

```
CPU requests address X
        │
        ▼
┌───────────────────┐
│ Check L1 Cache    │──── Hit? ──→ Return data (1 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Check L2 Cache    │──── Hit? ──→ Return data (3 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Check L3 Cache    │──── Hit? ──→ Return data (10 ns)
└───────────────────┘
        │ Miss
        ▼
┌───────────────────┐
│ Fetch from RAM    │──────────→ Return data (60 ns)
└───────────────────┘
        │
        ▼
  Also load into L1, L2, L3 (for next access)
```

### Cache Lines

Caches don't transfer single bytes—they move **cache lines** (typically 64 bytes):

```
Memory:
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ a0 │ a1 │ a2 │ a3 │ a4 │ a5 │ a6 │ a7 │ b0 │ b1 │ b2 │ b3 │
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
└──────────────────────────────────────┘
              Cache Line (64 bytes)

Access a0 → entire cache line loaded
Access a1, a2, ... a7 → already in cache (free!)
```

## Python's Memory Usage

Python objects live in RAM, managed by the interpreter:

```python
import sys

# Every Python object has overhead
x = 1
print(sys.getsizeof(x))  # 28 bytes (not 4 or 8!)

# Lists store references, not values
lst = [1, 2, 3]
print(sys.getsizeof(lst))  # 80 bytes (just the list object)
# Plus 28 bytes × 3 for the integers = 164 bytes total
```

### NumPy's Memory Advantage

NumPy arrays use contiguous memory, enabling cache efficiency:

```python
import numpy as np

# NumPy: contiguous block of raw values
arr = np.array([1, 2, 3], dtype=np.int64)
print(arr.nbytes)  # 24 bytes (8 bytes × 3, no overhead per element)

# Python list: scattered objects
lst = [1, 2, 3]
# ~164 bytes, objects may not be contiguous
```

```
Python List Memory Layout:
┌─────────┐     ┌─────────┐
│  List   │────▶│ Ref[0]  │────▶ [PyObject: 1] (somewhere in heap)
│ Object  │     │ Ref[1]  │────▶ [PyObject: 2] (somewhere else)
└─────────┘     │ Ref[2]  │────▶ [PyObject: 3] (somewhere else)
                └─────────┘

NumPy Array Memory Layout:
┌─────────┐     ┌───────────────────────┐
│ ndarray │────▶│  1  │  2  │  3  │     │  ← Contiguous data buffer
│ Object  │     └───────────────────────┘
└─────────┘
```

## Measuring Memory Hierarchy Effects

```python
import numpy as np
import time

def measure_access_pattern(size_mb):
    """Measure time to sum array of given size."""
    n = size_mb * 1024 * 1024 // 8  # Number of float64 elements
    arr = np.random.rand(n)
    
    # Warm up cache
    _ = np.sum(arr)
    
    # Measure
    start = time.perf_counter()
    for _ in range(10):
        _ = np.sum(arr)
    elapsed = time.perf_counter() - start
    
    bandwidth = (n * 8 * 10) / elapsed / 1e9  # GB/s
    return bandwidth

# Test different sizes
for size in [0.01, 0.1, 1, 10, 100]:
    bw = measure_access_pattern(size)
    print(f"{size:6.2f} MB: {bw:.1f} GB/s")
```

Expected pattern:

```
  0.01 MB: 150.0 GB/s  ← Fits in L2, very fast
  0.10 MB: 120.0 GB/s  ← Fits in L3
  1.00 MB: 80.0 GB/s   ← Mostly L3
 10.00 MB: 45.0 GB/s   ← Spills to RAM
100.00 MB: 35.0 GB/s   ← RAM-limited
```

## Key Concepts Summary

| Concept | Description |
|---------|-------------|
| **Memory Hierarchy** | Multiple levels of storage trading speed for capacity |
| **Cache** | Small, fast memory that stores recently used data |
| **Cache Line** | Unit of transfer between cache levels (typically 64 bytes) |
| **Cache Hit** | Data found in cache (fast) |
| **Cache Miss** | Data not in cache, must fetch from lower level (slow) |
| **Temporal Locality** | Recently used data likely to be used again |
| **Spatial Locality** | Nearby data likely to be used together |

## Why This Matters for Python

Understanding the memory hierarchy explains:

- Why NumPy is faster than Python lists (contiguous memory → cache efficiency)
- Why accessing array elements sequentially is faster than randomly
- Why small, hot loops are fast (fit in cache)
- Why memory-bound operations don't benefit from faster CPUs
- Why data layout matters for performance

The hierarchy is invisible to most Python code, but its effects are everywhere.
