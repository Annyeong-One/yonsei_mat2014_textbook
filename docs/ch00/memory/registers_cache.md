# Registers and Cache

Registers and caches are the fastest storage in a computer. They sit between the CPU and RAM, and their behavior explains why NumPy is dramatically faster than Python lists for numerical work.

## Definition

**Registers** are tiny storage locations inside the CPU (~128 bytes total for 16 general-purpose 64-bit registers on x86-64), accessed in ~1 cycle. The compiler and CPU hardware (via register renaming) manage register allocation.

**Cache** is small, fast memory organized in levels: L1 (~32 KB, ~4 cycles), L2 (~256 KB, ~12 cycles), and L3 (~8-32 MB, ~40 cycles, shared across cores). L1 is split into separate instruction (L1-I) and data (L1-D) caches. All cache management is done automatically by hardware.

## Explanation

Caches operate on **cache lines** (64 bytes). When any byte is accessed, the entire 64-byte block is loaded. This means sequential array access gets 7 out of 8 float64 elements "free" after each cache miss.

Modern CPUs also include **SIMD registers** (128-bit XMM, 256-bit YMM, 512-bit ZMM) that hold multiple values simultaneously. NumPy exploits these for vectorized operations: one instruction can add 4 or 8 floats at once, rather than one at a time.

**Cache associativity** determines how cache lines are organized into sets. N-way associativity means N lines can map to each set. Conflict misses occur when many addresses compete for the same set.

Python code does not directly use registers -- the CPython interpreter does. A simple `x = a + b` in Python triggers type dispatch, dictionary lookups, and object allocation, requiring orders of magnitude more instructions than a single machine ADD in C. NumPy bypasses this overhead by delegating to pre-compiled C code that operates directly on contiguous data using registers and SIMD instructions.

## Examples

```python
import numpy as np
import time

# Observe bandwidth drop as data exceeds cache levels
for name, n in [('L1 32KB', 4000), ('L2 256KB', 32000),
                ('L3 8MB', 1000000), ('RAM 64MB', 8000000)]:
    arr = np.random.rand(n)
    _ = np.sum(arr)  # warm up
    start = time.perf_counter()
    for _ in range(100):
        _ = np.sum(arr)
    elapsed = time.perf_counter() - start
    bw = (n * 8 * 100) / elapsed / 1e9
    print(f"{name:12}: {bw:6.1f} GB/s")
```

```python
import numpy as np

# Cache line effect: sequential access is fast, strided is slower
arr = np.arange(1_000_000, dtype=np.float64)

# Sequential sum: 1 miss per 8 elements (64 bytes / 8 bytes each)
total_seq = np.sum(arr)

# Strided access: wastes most of each cache line
total_strided = np.sum(arr[::64])  # every 64th element
```
