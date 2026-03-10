# Memory Access Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Why Access Patterns Matter

The same data processed in different orders can have 10-100x performance difference. Understanding access patterns is crucial for writing fast code.

```
Same data, different access patterns:

Sequential:     ████████████████████  Fast (cache friendly)
                → → → → → → → → → →

Strided:        ████░░░░████░░░░████  Medium (some cache hits)
                →       →       →

Random:         █░░█░█░░░█░░█░░░█░█░  Slow (cache hostile)
                →  ↗  ↘   ↗  ↘
```

## Cache Hierarchy

Modern CPUs have multiple levels of cache, each with different sizes and latencies:

```
CPU Registers
     │
L1 Cache   ~32 KB     ~1 ns       (~4 cycles)
     │
L2 Cache   ~512 KB    ~4 ns       (~10 cycles)
     │
L3 Cache   ~10-60 MB  ~12 ns      (~30-50 cycles)
     │
RAM         ~16+ GB   ~80-120 ns  (~200 cycles)

Latencies vary by CPU model and generation.
```

Performance depends on **which level** your working set fits in. The **working set** is the portion of memory actively used during a computation phase — not the total data size, but the data touched within a short time window.

- Working set fits in L1: extremely fast
- Working set fits in L2: fast
- Working set fits in L3: moderate
- Working set exceeds L3: slow (memory-bound)

!!! note "Simplified Model"
    The examples on this page use a simplified single-level cache model for clarity. Real CPUs have multi-level caches, hardware prefetchers that detect stride patterns, SIMD vectorization for contiguous data, and translation lookaside buffers (TLBs) for virtual-to-physical address translation. These features mean real-world performance can differ from the simplified model.

## Sequential Access

**Sequential access** reads memory addresses in order. This is the most cache-friendly pattern.

```python
import numpy as np

arr = np.arange(10_000_000)

# Sequential: NumPy's internal C loop iterates addresses in order
total = np.sum(arr)  # Addresses: 0, 8, 16, 24, ... (8 bytes per int64)
```

!!! warning "Python Loop Overhead"
    A Python `for` loop costs ~50-100 ns per iteration, which dwarfs L1 cache latency (~1 ns). Using explicit Python loops to demonstrate cache effects actually measures interpreter overhead, not memory access patterns. Use NumPy vectorized operations or compiled code (Numba, C, Cython) to observe real cache effects.

### Why Sequential is Fast

Sequential access exploits **spatial locality** — the principle that data near recently accessed memory is likely to be accessed soon. A related concept is **temporal locality**, where recently accessed data is likely to be accessed again.

```
Cache Line Loading (typical cache line: 64 bytes on modern CPUs)

Memory: [0][1][2][3][4][5][6][7][8][9][10]...
        └────────────────────────┘
              Cache Line (64 bytes = 8 float64s)

Access arr[0]:
  - Cache miss, load entire cache line
  - arr[0] through arr[7] now in cache

Access arr[1] through arr[7]:
  - Cache HITS! (already loaded)
  - Much cheaper than a cache miss (~1 ns vs ~100 ns)

Access arr[8]:
  - Cache miss, load next cache line
  - Pattern repeats...

Result: 1 miss per 8 accesses = 87.5% hit rate
```

## Strided Access

**Strided access** skips elements at regular intervals.

```python
import numpy as np

arr = np.arange(10_000_000)
stride = 100

# Strided: skip elements (vectorized to avoid Python loop overhead)
total = np.sum(arr[::stride])  # Addresses: 0, 800, 1600, 2400, ...
```

### Stride Impact on Cache

```
Stride = 8 (exactly one cache line worth):
  Access: [X][ ][ ][ ][ ][ ][ ][ ][X][ ][ ][ ][ ][ ][ ][ ]
          └──────cache line──────┘└──────cache line──────┘
  Each access uses only 1/8 of the loaded cache line
  Note: hardware prefetchers can detect constant strides and
  prefetch ahead, so real performance may be better than expected

Stride = 2–16 (small to moderate):
  Hardware prefetchers often handle these well
  Performance degrades gradually, not catastrophically

Stride = 4 (half a cache line):
  Access: [X][ ][ ][ ][X][ ][ ][ ][X][ ][ ][ ]
  50% of cache line used → wasted bandwidth

Stride = 1 (sequential):
  Access: [X][X][X][X][X][X][X][X]
  100% of cache line used → optimal
```

### 2D Array Row vs Column Access

```python
import numpy as np
import time

arr = np.random.rand(10000, 10000)  # Row-major (C order)

# Row-major sum: FAST (sequential in memory)
start = time.perf_counter()
row_total = np.sum(arr, axis=1).sum()  # Sum along rows first
row_time = time.perf_counter() - start

# Column-major sum: SLOWER (strided in memory)
start = time.perf_counter()
col_total = np.sum(arr, axis=0).sum()  # Sum along columns first
col_time = time.perf_counter() - start

print(f"Row-major: {row_time*1000:.1f} ms")
print(f"Col-major: {col_time*1000:.1f} ms")
print(f"Ratio: {col_time/row_time:.1f}x slower")
```

!!! note "Measuring Cache Effects in Python"
    Explicit Python `for` loops are too slow to reveal cache effects — the interpreter overhead (~50-100 ns per iteration) dwarfs cache miss penalties (~100 ns). The examples above use NumPy vectorized operations, which execute in compiled C code where memory access patterns dominate performance. Note that NumPy's reduction kernels are optimized and may internally reorder loops or vectorize, so the observed row vs column difference may be smaller than with naive C implementations.

### Memory Layout Visualization

```
Row-major (C order) - NumPy default
arr[0,0] arr[0,1] arr[0,2] arr[1,0] arr[1,1] arr[1,2]
   ↓        ↓        ↓        ↓        ↓        ↓
[  0  ][  1  ][  2  ][  3  ][  4  ][  5  ]  Memory
  └────────────────────────────────────────→ Sequential access

Column-major (Fortran order)
arr[0,0] arr[1,0] arr[2,0] arr[0,1] arr[1,1] arr[2,1]
   ↓        ↓        ↓        ↓        ↓        ↓
[  0  ][  1  ][  2  ][  3  ][  4  ][  5  ]  Memory
```

## Random Access

**Random access** visits memory locations in unpredictable order. This is the worst pattern for cache.

```python
import numpy as np

arr = np.arange(10_000_000)
indices = np.random.permutation(len(arr))

# Random access via fancy indexing
total = np.sum(arr[indices])  # Unpredictable addresses
```

!!! note "Fancy Indexing Creates a Copy"
    `arr[indices]` performs a **gather** operation that creates a new contiguous array. The random access cost occurs during the gather step, after which `np.sum` processes the copy sequentially. This still demonstrates the cost of random reads, but the reduction itself runs sequentially on the copy.

### Why Random is Slow

```
Random Access Pattern

Memory: [0][1][2][3][4][5][6][7][8][9]...
        
Access arr[7]: Load cache line containing [4-11]
Access arr[2]: Load cache line containing [0-7] (maybe evicts previous!)
Access arr[9]: Load cache line containing [8-15]
Access arr[1]: Is [0-7] still in cache? Maybe not!

Each access likely:
  - Misses cache
  - Evicts useful data
  - Wastes most of the loaded cache line
```

### Quantifying the Impact

```python
import numpy as np
import time

def benchmark_access_pattern(n=10_000_000):
    arr = np.arange(n, dtype=np.float64)

    # Sequential
    start = time.perf_counter()
    _ = np.sum(arr)
    seq_time = time.perf_counter() - start

    # Random (via fancy indexing — includes gather, allocation, and sequential sum)
    indices = np.random.permutation(n)
    start = time.perf_counter()
    _ = np.sum(arr[indices])
    rand_time = time.perf_counter() - start

    print(f"Sequential: {seq_time*1000:.1f} ms")
    print(f"Random:     {rand_time*1000:.1f} ms")
    print(f"Ratio:      {rand_time/seq_time:.1f}x")

benchmark_access_pattern()
```

Typical output:

```
Sequential: 15.0 ms
Random:     250.0 ms
Ratio:      16.7x
```

The random case is slower due to the gather step, where random reads cause frequent cache misses and TLB (translation lookaside buffer) misses across many memory pages. The benchmark also includes the cost of allocating the temporary array created by `arr[indices]`.

## Prefetching

Modern CPUs detect sequential patterns and **prefetch** upcoming data:

```
Without Prefetching:
CPU: [Work][Wait][Work][Wait][Work][Wait]
              ↑       ↑       ↑
           Memory  Memory  Memory
           fetch   fetch   fetch

With Prefetching:
CPU: [Work][Work][Work][Work][Work][Work]
        └──Prefetch──┘
        
Memory loads happen in parallel with computation!
```

### What Prefetchers Can Detect

Modern hardware prefetchers can detect:

- **Sequential** access (stride = 1): always prefetched effectively
- **Constant stride** access: many CPUs detect and prefetch regular strides
- **Adjacent cache lines**: some prefetchers speculatively load neighboring lines

Prefetchers **cannot** help with truly random access patterns, where the next address is unpredictable.

```python
import numpy as np

# Good: Predictable pattern — prefetcher works well
result = arr * 2  # Sequential access, handled in compiled C

# Bad: Unpredictable access — prefetcher cannot help
result = arr[random_indices] * 2  # Random gather defeats prefetching
```

## Optimizing Access Patterns

### Technique 1: Reorder Data

```python
import numpy as np

# Sparse access pattern
sparse_indices = np.array([0, 1000, 2000, 3000, 4000])
data = np.arange(10000)

# Bad: Access scattered locations
values = data[sparse_indices]

# Good: Compact the data first
compact_data = data[sparse_indices].copy()  # Now contiguous
# Future accesses to compact_data are sequential
```

### Technique 2: Reorder Operations

```python
import numpy as np

# Process 2D array
arr = np.random.rand(1000, 1000)

# Bad: Column-major traversal
for j in range(arr.shape[1]):
    for i in range(arr.shape[0]):
        arr[i, j] *= 2

# Good: Row-major traversal
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        arr[i, j] *= 2

# Best: Vectorized (NumPy handles it optimally)
arr *= 2
```

### Technique 3: Blocking/Tiling

Process data in cache-sized chunks:

```python
import numpy as np

def blocked_transpose(A, block_size=64):
    """Transpose with cache-friendly blocking.

    Block size 64 is chosen so one block fits in L1 cache:
    64 × 64 × 8 bytes (float64) = 32 KB ≈ typical L1 cache size.
    """
    n = A.shape[0]
    B = np.empty_like(A)

    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            # Process one block at a time — block fits in L1 cache
            i_end = min(i + block_size, n)
            j_end = min(j + block_size, n)
            B[j:j_end, i:i_end] = A[i:i_end, j:j_end].T

    return B
```

### Technique 4: Structure of Arrays (SoA)

```python
import numpy as np

# Array of Structures (AoS) - cache unfriendly for single-field access
class Particle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.mass = 0.0

particles = [Particle() for _ in range(1000000)]
# Accessing all x values touches scattered memory
# (Python objects also add pointer indirection overhead)

# Structure of Arrays (SoA) - cache friendly
class ParticleSystem:
    def __init__(self, n):
        self.x = np.zeros(n)  # Contiguous float64 arrays
        self.y = np.zeros(n)
        self.z = np.zeros(n)
        self.mass = np.zeros(n)

system = ParticleSystem(1000000)
# Accessing all x values is sequential: system.x[:]
```

## Beyond Cache Misses

Cache misses are not the only reason access patterns matter. Several other hardware mechanisms are affected:

**TLB (Translation Lookaside Buffer)** — Virtual addresses must be translated to physical addresses via page tables. The TLB caches recent translations. Random access across many memory pages causes TLB misses, adding significant latency on top of cache misses.

**SIMD Vectorization** — Modern CPUs can process multiple data elements simultaneously (e.g., AVX loads 8 float32 values at once). SIMD requires contiguous, aligned memory, so only sequential access benefits from vectorization.

**Memory Bandwidth** — Even with perfect cache behavior, sequential throughput is ultimately limited by memory bandwidth (typically 50-200 GB/s). Algorithms with good locality can approach this hardware limit.

**False Sharing (Multithreading)** — When two threads write to different variables that share the same cache line, the cache line bounces between cores. This can severely degrade multithreaded performance even when there is no logical data sharing.

## Real-World Example: Matrix Multiplication

Matrix multiplication is a classic case where access patterns determine performance. A naive triple loop has poor locality on one of the three matrices:

```python
import numpy as np
import time

n = 512
A = np.random.rand(n, n)
B = np.random.rand(n, n)

# Naive: C[i,j] += A[i,k] * B[k,j]
# A is accessed row-wise (sequential) ✓
# B is accessed column-wise (strided) ✗
C_naive = np.zeros((n, n))
start = time.perf_counter()
for i in range(n):
    for j in range(n):
        for k in range(n):
            C_naive[i, j] += A[i, k] * B[k, j]
naive_time = time.perf_counter() - start

# NumPy: uses blocked algorithms with optimal access patterns
start = time.perf_counter()
C_numpy = A @ B
numpy_time = time.perf_counter() - start

print(f"Naive loops:  {naive_time:.2f}s")
print(f"NumPy (BLAS): {numpy_time*1000:.1f} ms")
print(f"Speedup:      {naive_time/numpy_time:.0f}x")
```

!!! note
    The massive speedup here reflects both better memory access patterns *and* the elimination of Python loop overhead. The naive version is dominated by interpreter cost (~50-100 ns per iteration), while BLAS runs entirely in optimized compiled code with blocking/tiling, SIMD vectorization, and cache-aware iteration order.

## Compute-Bound vs Memory-Bound

Every algorithm's performance is ultimately limited by one of two bottlenecks:

- **Compute-bound**: the CPU cannot perform arithmetic fast enough (e.g., complex math on small data)
- **Memory-bound**: the CPU stalls waiting for data from memory (e.g., simple operations on large arrays)

The **operational intensity** — the ratio of compute operations to bytes transferred — determines which bottleneck dominates. This relationship is captured by the **Roofline model**:

```
Performance
(FLOPS)
     |         _______________  ← peak compute (CPU limit)
     |        /
     |       /
     |      /
     |     /  ← peak memory bandwidth (slope)
     |    /
     |   /
     +──────────────────────────
        Operational Intensity
        (FLOPS / byte)
```

Algorithms to the left of the "knee" are **memory-bound** — improving access patterns directly increases performance. Algorithms to the right are **compute-bound** — memory layout matters less because the CPU is already the limiting factor.

## Access Pattern Summary

| Pattern | Cache Behavior | Relative Speed | Example |
|---------|---------------|----------------|---------|
| **Sequential** | Excellent | 1x (baseline) | `for i in range(n): arr[i]` |
| **Small Stride** | Good | 1-2x slower | `for i in range(0, n, 4): arr[i]` |
| **Large Stride** | Poor | 5-10x slower | `arr[:, 0]` in row-major |
| **Random** | Terrible | Often 10-50x slower | `arr[random_indices]` |

## Best Practices

1. **Prefer sequential access** when possible
2. **Match traversal order to memory layout** (row-major vs column-major)
3. **Keep working set small** enough to fit in cache
4. **Use blocking/tiling** for large data structures
5. **Let NumPy handle it** when possible (optimized implementations)
6. **Profile before optimizing** (access patterns may not be the bottleneck)

```python
# The NumPy way: trust the library
# These are implemented with optimal access patterns:
np.sum(arr)           # Sequential reduction
np.dot(A, B)          # Blocked matrix multiply
arr.T                 # Lazy transpose (no memory movement)
np.einsum('ij->ji', A)  # Optimized strided access
```
