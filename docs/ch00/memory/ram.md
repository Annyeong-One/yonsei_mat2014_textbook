# RAM (Main Memory)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## What is RAM?

**RAM (Random Access Memory)** is the main working memory of a computer. It stores:

- Running programs (code)
- Active data (variables, objects)
- Operating system components

Each process sees its own **virtual address space**, mapped by the OS to physical RAM pages. The diagram below shows a single process's view — not the physical layout of RAM:

```
Virtual Address Space (one process, e.g., Python)

High address
┌─────────────────────────────────────────────────────┐
│              Stack                                   │
│   (C-level call frames, return addresses)            │
├─────────────────────────────────────────────────────┤
│                    ↓ grows down                      │
│                                                      │
│                    ↑ grows up                         │
├─────────────────────────────────────────────────────┤
│              Heap                                    │
│                                                     │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐               │
│  │ int  │ │ str  │ │ list │ │ dict │  ...          │
│  └──────┘ └──────┘ └──────┘ └──────┘               │
│  (scattered, each with per-object overhead)         │
│                                                     │
│  ┌──────────┐   ┌────────────────────────────┐     │
│  │ ndarray  │──▶│ 1.0 │ 2.0 │ 3.0 │ 4.0 │..│     │
│  │ (object) │   └────────────────────────────┘     │
│  └──────────┘   contiguous raw values               │
│                                                     │
├─────────────────────────────────────────────────────┤
│              Shared Libraries                        │
├─────────────────────────────────────────────────────┤
│              Program Code (text)                     │
└─────────────────────────────────────────────────────┘
Low address
```

!!! note "Virtual vs Physical Memory"
    This diagram shows **virtual** addresses. Physical RAM contains interleaved pages from many processes — the OS and hardware translate virtual addresses to physical locations via page tables. See the [Virtual Memory](virtual_memory.md) page for details.

!!! note "Stack vs Heap in Python"
    In C, local variables live on the stack. In CPython, the C call stack drives the interpreter loop, but Python frame objects (`PyFrameObject`) and all Python objects (including local variables) are allocated on the **heap**. The "stack" in the virtual address space diagram is the C-level stack used by the CPython interpreter itself, not by Python-level variables. Modern OSes also randomize these region addresses (ASLR) for security.

## RAM Characteristics

| Property | Typical Value |
|----------|---------------|
| **Capacity** | 8-128 GB |
| **Latency** | ~80-120 ns (varies with access pattern) |
| **Bandwidth** | ~20-50 GB/s per channel (depends on DDR generation) |
| **Volatility** | Data lost when power off |
| **Access** | Random (any address accessible, but latency varies — see below) |

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

Capacitors leak → must refresh every ~64 ms (each row refreshed individually)
```

"Random Access" means any address is directly accessible (unlike tape which requires sequential seeking), but DRAM access time is **not truly uniform**. Accessing data in an already-open row (row buffer hit, ~20 ns) is much faster than opening a new row (row miss, ~80-120 ns).

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

| Generation | Speed | Bandwidth (single channel) | Year |
|------------|-------|---------------------------|------|
| DDR3 | 1600 MT/s | ~12 GB/s | 2007 |
| DDR4 | 3200 MT/s | ~25 GB/s | 2014 |
| DDR5 | 6400 MT/s | ~50 GB/s | 2020 |

These are **theoretical peak** bandwidths per channel. Sustained throughput is lower due to refresh cycles, access patterns, and memory controller overhead. Dual-channel configurations roughly double these numbers; quad-channel (workstations/servers) roughly quadruple them.

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

Bandwidth depends on DDR generation (e.g., ~25 GB/s × 2 channels)
```

## RAM Latency Breakdown

Accessing RAM involves multiple steps. If a different row is already open, it must be closed first:

```
CPU Request                            Time

     ▼  (if a different row is already open)
┌─────────────┐
│ Precharge   │ ─── tRP ────▶  ~14 ns  (close current row)
└─────────────┘
     │
     ▼
┌─────────────┐
│ Activate    │ ─── tRCD ───▶  ~14 ns  (open new row)
│ Row (RAS)   │
└─────────────┘
     │
     ▼
┌─────────────┐
│ Column Read │ ─── tCL ────▶  ~14 ns  (select column, read data)
│   (CAS)     │
└─────────────┘
     │
     ▼
┌─────────────┐
│ Data Burst  │              (data transferred to memory controller)
└─────────────┘

Row buffer hit (same row already open): ~20-40 ns  (just tCL)
Row miss (different row):              ~80-120 ns (tRP + tRCD + tCL + controller overhead)
```

### CAS Latency (CL)

The number of clock cycles between column address and data. Note that DDR's "speed" rating refers to **transfer rate**, not clock speed — DDR transfers data on both edges of the clock, so the actual clock runs at half the rated speed:

```
DDR4-3200 = 1600 MHz actual clock, 3200 MT/s (megatransfers/second)
DDR4-2400 = 1200 MHz actual clock, 2400 MT/s

CAS latency in nanoseconds = CL × (1 / actual clock frequency)

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

Python uses a custom allocator (pymalloc) optimized for the many small, short-lived objects typical of Python programs:

```
Python Memory Allocator Hierarchy

┌─────────────────────────────────────────────┐
│           Python Object Allocator           │
│    (small objects < 512 bytes)              │
├─────────────────────────────────────────────┤
│         pymalloc (arena-based)              │
│                                             │
│    Arena (256 KB, obtained from OS)         │
│     ├── Pool (4 KB, one size class)         │
│     │    ├── Block (8-512 bytes)            │
│     │    ├── Block                          │
│     │    └── ...                            │
│     ├── Pool                                │
│     └── ...                                 │
├─────────────────────────────────────────────┤
│            C malloc/free                    │
│    (objects ≥ 512 bytes bypass pymalloc)    │
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

### NumPy Lives in the Heap Too

NumPy arrays live in the heap just like all other Python objects — they get no special separate memory region. What makes NumPy different is not *where* the data lives, but *how* it is laid out.

All Python objects have metadata and data. The real distinction is whether the actual values are **contiguous raw bytes** or **scattered objects accessed via pointers**:

```
Python list [1.0, 2.0, 3.0]:

Heap:
┌──────────┐      ┌──────────┐
│   list   │─────▶│ ref[0]   │──▶ [PyObject float: 1.0] (somewhere in heap)
│  object  │      │ ref[1]   │──▶ [PyObject float: 2.0] (somewhere else)
└──────────┘      │ ref[2]   │──▶ [PyObject float: 3.0] (somewhere else)
                  └──────────┘
                  stores pointers,     actual values scattered
                  not values           all over heap


NumPy array([1.0, 2.0, 3.0]):

Heap:
┌──────────┐      ┌────────────────────────┐
│ ndarray  │─────▶│ 1.0 │ 2.0 │ 3.0 │ ... │
│  object  │      └────────────────────────┘
└──────────┘      actual values, contiguous,
                  no per-element Python object overhead
                  (array has fixed overhead: dtype, strides, shape)
```

| | Python list | NumPy array |
|---|---|---|
| **Stores** | Pointers to objects | Raw values directly |
| **Values location** | Scattered across heap | Contiguous block in heap |
| **Per-element overhead** | ~28 bytes per int + 8-byte pointer in list | None (raw values, no Python object wrapper) |
| **Cache friendliness** | Poor (pointer chasing) | Excellent (one block) |

Both are in the heap. The difference is purely layout — and that layout difference is what makes NumPy cache-friendly and fast.

### Contiguous Allocation

```python
import numpy as np

# Allocate 1 GB array
arr = np.zeros(125_000_000, dtype=np.float64)
print(f"Size: {arr.nbytes / 1e9:.1f} GB")

# Memory is contiguous in virtual address space
print(f"Contiguous: {arr.flags['C_CONTIGUOUS']}")  # True
# Note: virtually contiguous, but physical RAM pages may be scattered
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

Memory-mapped files work through the OS **page cache**. When you access a page that is not yet in RAM, a **page fault** occurs — the OS pauses execution, loads the page from disk into the page cache, updates the mapping, and resumes. Frequently accessed pages stay in RAM, so subsequent accesses are fast. The OS transparently manages this, making it appear as if the entire file is in memory.

## RAM Bandwidth Limits

RAM bandwidth is often the bottleneck for data processing. The following benchmark approximates memory bandwidth for sequential reads (actual throughput is affected by prefetching, vectorization, and cache effects):

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

When the system runs out of RAM, the Linux OOM killer selects and terminates processes based on their memory usage, oom_score, and priority:

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
| **Latency** | ~80-120 ns (row miss); ~20 ns (row hit) |
| **Bandwidth** | ~20-50 GB/s per channel (varies by DDR generation) |
| **Volatility** | Lost when power off |
| **Python Use** | Heap for all objects, pymalloc for small objects |
| **NumPy Use** | Contiguous buffers, memory-mapped files for large data |

Key points:

- RAM is much slower than cache (~80-120 ns vs 1-12 ns)
- Bandwidth limits data processing speed
- Python objects have significant per-object overhead
- NumPy's contiguous arrays are more RAM-efficient
- Memory-mapped files extend beyond physical RAM
