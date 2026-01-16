# Memory Access Patterns

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

## Sequential Access

**Sequential access** reads memory addresses in order. This is the most cache-friendly pattern.

```python
import numpy as np

arr = np.arange(10_000_000)

# Sequential: each element follows the previous
total = 0
for i in range(len(arr)):
    total += arr[i]  # Addresses: 0, 8, 16, 24, ...
```

### Why Sequential is Fast

```
Cache Line Loading

Memory: [0][1][2][3][4][5][6][7][8][9][10]...
        └────────────────────────┘
              Cache Line (64 bytes = 8 float64s)

Access arr[0]:
  - Cache miss, load entire cache line
  - arr[0] through arr[7] now in cache

Access arr[1] through arr[7]:
  - Cache HITS! (already loaded)
  - Essentially free

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

# Strided: skip elements
total = 0
for i in range(0, len(arr), stride):
    total += arr[i]  # Addresses: 0, 800, 1600, 2400, ...
```

### Stride Impact on Cache

```
Stride = 8 (exactly one cache line worth):
  Access: [X][ ][ ][ ][ ][ ][ ][ ][X][ ][ ][ ][ ][ ][ ][ ]
          └──────cache line──────┘└──────cache line──────┘
  Every access misses cache → 0% hit rate

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

# Row-major access: FAST (sequential in memory)
start = time.perf_counter()
total = 0
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        total += arr[i, j]  # Consecutive memory addresses
row_time = time.perf_counter() - start

# Column-major access: SLOW (strided in memory)
start = time.perf_counter()
total = 0
for j in range(arr.shape[1]):
    for i in range(arr.shape[0]):
        total += arr[i, j]  # Jumps 80,000 bytes between accesses!
col_time = time.perf_counter() - start

print(f"Row-major: {row_time:.2f}s")
print(f"Col-major: {col_time:.2f}s")
print(f"Ratio: {col_time/row_time:.1f}x slower")
```

Typical output:

```
Row-major: 2.50s
Col-major: 25.00s
Ratio: 10.0x slower
```

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

# Random access
total = 0
for i in indices:
    total += arr[i]  # Unpredictable addresses
```

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
    
    # Random (via fancy indexing)
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

### Helping the Prefetcher

```python
import numpy as np

# Good: Predictable sequential access
def process_sequential(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 2  # Prefetcher predicts next addresses

# Bad: Unpredictable access (prefetcher can't help)
def process_random(arr, indices):
    for i in indices:
        arr[i] = arr[i] * 2  # Where's next? Prefetcher gives up
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
    """Transpose with cache-friendly blocking."""
    n = A.shape[0]
    B = np.empty_like(A)
    
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            # Process one block at a time
            # Block fits in cache
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

# Structure of Arrays (SoA) - cache friendly
class ParticleSystem:
    def __init__(self, n):
        self.x = np.zeros(n)
        self.y = np.zeros(n)
        self.z = np.zeros(n)
        self.mass = np.zeros(n)

system = ParticleSystem(1000000)
# Accessing all x values is sequential: system.x[:]
```

## Access Pattern Summary

| Pattern | Cache Behavior | Relative Speed | Example |
|---------|---------------|----------------|---------|
| **Sequential** | Excellent | 1x (baseline) | `for i in range(n): arr[i]` |
| **Small Stride** | Good | 1-2x slower | `for i in range(0, n, 4): arr[i]` |
| **Large Stride** | Poor | 5-10x slower | `arr[:, 0]` in row-major |
| **Random** | Terrible | 10-50x slower | `arr[random_indices]` |

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
