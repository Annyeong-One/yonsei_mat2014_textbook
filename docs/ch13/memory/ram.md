# RAM (Main Memory)

## What is RAM?

**RAM (Random Access Memory)** is the main working memory of a computer. It stores:

- Running programs (code)
- Active data (variables, objects)
- Operating system components

```
┌─────────────────────────────────────────────────────────────┐
│                          RAM                                │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Operating System                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │              Python Interpreter                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │              Python Objects (Heap)                   │   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               │   │
│  │  │ int  │ │ str  │ │ list │ │ dict │  ...          │   │
│  │  └──────┘ └──────┘ └──────┘ └──────┘               │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │              NumPy Arrays                            │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │ Contiguous data buffers                     │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │              Other Applications                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## RAM Characteristics

| Property | Typical Value |
|----------|---------------|
| **Capacity** | 8-128 GB |
| **Latency** | ~60-100 ns |
| **Bandwidth** | 25-50 GB/s (per channel) |
| **Volatility** | Data lost when power off |
| **Access** | Random (any address, same time) |

## Types of RAM

### DRAM (Dynamic RAM)

The standard RAM in computers. "Dynamic" because it must be constantly refreshed.

```
DRAM Cell
┌─────────────┐
│ Capacitor   │ ← Stores charge (1 or 0)
│      │      │
│  Transistor │ ← Controls access
└─────────────┘

Capacitors leak → must refresh thousands of times/second
```

### DDR (Double Data Rate)

Modern standard. Transfers data on both clock edges:

```
Clock:    ─┐  ┌──┐  ┌──┐  ┌──┐  ┌──
          └──┘  └──┘  └──┘  └──┘

SDR:      [D1]    [D2]    [D3]    [D4]
           ↑       ↑       ↑       ↑
          One transfer per cycle

DDR:      [D1][D2][D3][D4][D5][D6][D7][D8]
           ↑  ↑   ↑  ↑   ↑  ↑   ↑  ↑
          Two transfers per cycle
```

### DDR Generations

| Generation | Speed | Bandwidth | Year |
|------------|-------|-----------|------|
| DDR3 | 1600 MT/s | ~12 GB/s | 2007 |
| DDR4 | 3200 MT/s | ~25 GB/s | 2014 |
| DDR5 | 6400 MT/s | ~50 GB/s | 2020 |

## Memory Channels

Modern systems use multiple memory channels for parallel access:

```
Dual-Channel Configuration
┌─────────┐          ┌─────────┐
│  CPU    │          │  CPU    │
│ Channel │          │ Channel │
│    A    │          │    B    │
└────┬────┘          └────┬────┘
     │                    │
┌────┴────┐          ┌────┴────┐
│  DIMM   │          │  DIMM   │
│  Slot 1 │          │  Slot 2 │
└─────────┘          └─────────┘

Bandwidth: 25 GB/s × 2 = 50 GB/s total
```

## RAM Latency Breakdown

Accessing RAM involves multiple steps:

```
CPU Request                            Time
     │
     ▼
┌─────────────┐
│ Row Address │ ─── tRCD ───▶  ~14 ns
│   (RAS)     │
└─────────────┘
     │
     ▼
┌─────────────┐
│ Col Address │ ─── tCL ────▶  ~14 ns
│   (CAS)     │
└─────────────┘
     │
     ▼
┌─────────────┐
│ Data Ready  │ ─── tRP ────▶  ~14 ns (if row change)
└─────────────┘

Total: ~40-100 ns depending on access pattern
```

### CAS Latency (CL)

The number of clock cycles between column address and data:

```
DDR4-3200 CL16:  16 cycles × (1/1600 MHz) = 10 ns
DDR4-2400 CL12:  12 cycles × (1/1200 MHz) = 10 ns

Higher speed with higher CL can have same actual latency!
```

## Python Memory Allocation

### Object Creation

Every Python object allocates heap memory:

```python
import sys

# Integers
x = 42
print(sys.getsizeof(x))  # 28 bytes

# Strings
s = "hello"
print(sys.getsizeof(s))  # 54 bytes

# Lists (just the container)
lst = [1, 2, 3]
print(sys.getsizeof(lst))  # 80 bytes (+ 28×3 for ints)
```

### Memory Allocator

Python uses a custom allocator optimized for small objects:

```
Python Memory Allocator Hierarchy

┌─────────────────────────────────────────────┐
│           Python Object Allocator           │
│    (small objects < 512 bytes)              │
├─────────────────────────────────────────────┤
│         Python Memory Allocator             │
│    (pymalloc - arena-based)                 │
├─────────────────────────────────────────────┤
│            C malloc/free                    │
│    (large objects)                          │
├─────────────────────────────────────────────┤
│           Operating System                  │
│    (mmap, brk)                              │
└─────────────────────────────────────────────┘
```

### Checking Memory Usage

```python
import sys
import tracemalloc

# Start tracking
tracemalloc.start()

# Create objects
data = [i ** 2 for i in range(100000)]

# Check usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.1f} MB")
print(f"Peak: {peak / 1024 / 1024:.1f} MB")

tracemalloc.stop()
```

## NumPy and RAM

NumPy allocates contiguous memory blocks:

```python
import numpy as np

# Allocate 1 GB array
arr = np.zeros(125_000_000, dtype=np.float64)
print(f"Size: {arr.nbytes / 1e9:.1f} GB")

# Memory is contiguous
print(f"Contiguous: {arr.flags['C_CONTIGUOUS']}")  # True
```

### Memory-Mapped Files

For arrays larger than RAM, NumPy can use memory-mapped files:

```python
import numpy as np

# Create memory-mapped array (data lives on disk)
mmap_arr = np.memmap('large_array.dat', 
                      dtype='float64',
                      mode='w+',
                      shape=(1_000_000_000,))  # 8 GB

# Access like normal array, but pages in/out automatically
mmap_arr[0] = 42
print(mmap_arr[0])  # 42.0
```

## RAM Bandwidth Limits

RAM bandwidth is often the bottleneck for data processing:

```python
import numpy as np
import time

def measure_bandwidth(size_gb):
    n = int(size_gb * 1e9 / 8)  # float64 elements
    arr = np.random.rand(n)
    
    # Memory-bound operation
    start = time.perf_counter()
    result = np.sum(arr)
    elapsed = time.perf_counter() - start
    
    bandwidth = (n * 8) / elapsed / 1e9
    print(f"{size_gb:.1f} GB: {bandwidth:.1f} GB/s")

measure_bandwidth(0.1)  # Small - may hit cache
measure_bandwidth(1.0)  # Medium - RAM limited
measure_bandwidth(4.0)  # Large - definitely RAM limited
```

Typical output:

```
0.1 GB: 45.0 GB/s  (some cache hits)
1.0 GB: 35.0 GB/s  (RAM bandwidth)
4.0 GB: 33.0 GB/s  (RAM bandwidth)
```

## Memory Errors

### MemoryError

```python
try:
    huge = [0] * (10 ** 12)  # Try to allocate ~8 TB
except MemoryError:
    print("Not enough RAM!")
```

### Out-of-Memory Killer (Linux)

When system runs out of RAM, Linux OOM killer terminates processes:

```python
# This might crash your system!
import numpy as np

arrays = []
while True:
    arrays.append(np.zeros(100_000_000))  # 800 MB each
    print(f"Allocated {len(arrays) * 0.8:.1f} GB")
```

## Summary

| Aspect | Description |
|--------|-------------|
| **Purpose** | Store running programs and active data |
| **Capacity** | 8-128 GB typical |
| **Latency** | 60-100 ns |
| **Bandwidth** | 25-50 GB/s per channel |
| **Volatility** | Lost when power off |
| **Python Use** | Heap for all objects, pymalloc for small objects |
| **NumPy Use** | Contiguous buffers, memory-mapped files for large data |

Key points:

- RAM is much slower than cache (60 ns vs 1-10 ns)
- Bandwidth limits data processing speed
- Python objects have significant per-object overhead
- NumPy's contiguous arrays are more RAM-efficient
- Memory-mapped files extend beyond physical RAM
