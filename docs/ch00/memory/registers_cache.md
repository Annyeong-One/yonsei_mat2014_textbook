# Registers and Cache


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Registers: The Fastest Memory

**Registers** are tiny storage locations inside the CPU itself—the fastest memory in the entire system.

```
┌─────────────────────────────────────────────────────────┐
│                         CPU                             │
│                                                         │
│   ┌─────────────────────────────────────────────────┐  │
│   │                  Registers                       │  │
│   │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │  │
│   │  │ RAX │ │ RBX │ │ RCX │ │ RDX │ │ ... │       │  │
│   │  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘       │  │
│   │                                                 │  │
│   │  ┌─────┐ ┌─────┐ ┌─────┐                       │  │
│   │  │ RSP │ │ RBP │ │ RIP │  (Stack, Base, Instr) │  │
│   │  └─────┘ └─────┘ └─────┘                       │  │
│   └─────────────────────────────────────────────────┘  │
│                         │                               │
│                    ┌────┴────┐                          │
│                    │   ALU   │                          │
│                    └─────────┘                          │
└─────────────────────────────────────────────────────────┘
```

### Register Characteristics

| Property | Value |
|----------|-------|
| **Size** | 8 bytes each (64-bit CPU) |
| **Count** | 16 architectural general-purpose (x86-64) |
| **Total Capacity** | ~128 bytes (architectural); CPUs internally have hundreds of physical registers via register renaming |
| **Access Time** | ~1 cycle (effectively immediate compared to memory) |
| **Managed By** | Compiler + CPU hardware (register renaming) |

### Types of Registers

| Register Type | Purpose | Example |
|--------------|---------|---------|
| **General Purpose** | Computation, temporary storage | RAX, RBX, RCX, RDX |
| **Instruction Pointer** | Address of next instruction | RIP |
| **Stack Pointer** | Top of call stack | RSP |
| **Base Pointer** | Stack frame reference | RBP |
| **Flags** | Status of last operation | RFLAGS |
| **Floating Point** | FP computation (legacy) | ST0-ST7 |
| **SIMD** | Vector operations | XMM0-XMM15, YMM, ZMM |

### Python and Registers

Python code doesn't directly use registers—the CPython interpreter does:

```python
x = a + b
```

CPython compiles this to **bytecode**, not machine code directly:

```
LOAD_FAST   a
LOAD_FAST   b
BINARY_ADD
STORE_FAST  x
```

The `BINARY_ADD` bytecode triggers a C function (`PyNumber_Add`) that performs type dispatch, calls the appropriate addition routine, and may allocate a new Python object for the result. This is **orders of magnitude** slower than a single machine `ADD` instruction.

For comparison, in compiled C code, `x = a + b` for integers becomes something like:

```assembly
MOV RAX, [a_address]    ; Load 'a' into register
ADD RAX, [b_address]    ; Add 'b'
MOV [x_address], RAX    ; Store result
```

This distinction explains why Python arithmetic is slow and why NumPy (which executes compiled C loops internally) is so much faster.

NumPy operations are far more register-efficient than pure Python — but the reason is more nuanced than "it uses registers."

### How NumPy Handles Variable Array Sizes

NumPy's internals are pre-compiled C code (already compiled when you `pip install numpy`, sitting as a `.so` / `.dll` binary). This C code uses loops with `n` passed at runtime:

```c
// Simplified NumPy internals (pre-compiled, size n varies at runtime)
void add_arrays(double* a, double* b, double* c, int n) {
    for (int i = 0; i < n; i++) {
        c[i] = a[i] + b[i];
    }
}
```

When you write `c = a + b` in Python, NumPy hands off to this compiled function immediately, passing the current array size as `n`. The compiled binary never changes — only `n` does.

### Scalar Loop vs Vectorization

The plain C loop above processes **one element at a time** — this is a **scalar loop**:

```
Scalar loop (one element per iteration):

iteration 1: a[0] + b[0] → c[0]
iteration 2: a[1] + b[1] → c[1]
iteration 3: a[2] + b[2] → c[2]
...
```

**Vectorization** goes further — it uses special CPU instructions called **SIMD (Single Instruction, Multiple Data)** that process multiple elements simultaneously in one instruction:

```
Vectorization (multiple elements per instruction):

instruction 1: a[0], a[1], a[2], a[3]
             + b[0], b[1], b[2], b[3]
             = c[0], c[1], c[2], c[3]   ← all 4 in ONE instruction

instruction 2: a[4], a[5], a[6], a[7]
             + b[4], b[5], b[6], b[7]
             = c[4], c[5], c[6], c[7]   ← all 4 in ONE instruction
```

This is possible because SIMD registers are **wider** than normal registers:

```
Normal register:  64 bits  → holds 1 float64
XMM register:    128 bits  → holds 2 float64s  (SSE)
YMM register:    256 bits  → holds 4 float64s  (AVX/AVX2)
ZMM register:    512 bits  → holds 8 float64s  (AVX-512, not on all CPUs)
```

These SIMD registers are **overlays** of the same physical registers — YMM0 contains XMM0 as its lower half, and ZMM0 contains YMM0 as its lower half.

NumPy's compiled C code exploits SIMD instructions where the build and CPU support them. The exact SIMD level used depends on the compiler, CPU features detected at runtime, and the specific operation — some operations may still run as scalar loops. Your Python code never sees any of this — it just calls `c = a + b` and NumPy handles the rest invisibly.

## CPU Cache

**Cache** is small, fast memory between registers and RAM. Modern CPUs have multiple cache levels.

```
┌─────────────────────────────────────────────────────────────┐
│                          CPU Core                           │
│                                                             │
│  ┌───────────────┐    ┌───────────────────────────────┐    │
│  │   Registers   │    │           L1 Cache            │    │
│  │    (~128 B)   │◀──▶│  ┌───────────┬───────────┐   │    │
│  └───────────────┘    │  │ L1-I (32K)│ L1-D (32K)│   │    │
│                       │  │(instruction)│  (data)   │   │    │
│                       │  └───────────┴───────────┘   │    │
│                       └───────────────────────────────┘    │
│                                    │                        │
│                       ┌────────────┴────────────┐          │
│                       │       L2 Cache          │          │
│                       │       (~256 KB)         │          │
│                       └────────────┬────────────┘          │
└────────────────────────────────────┼────────────────────────┘
                                     │
                        ┌────────────┴────────────┐
                        │       L3 Cache          │
                        │   (Shared, 8-32 MB)     │
                        └────────────┬────────────┘
                                     │
                                 To RAM
```

### Cache Levels Compared

| Level | Size | Latency | Shared? | Purpose |
|-------|------|---------|---------|---------|
| **L1** | ~32 KB data + ~32 KB instruction | ~1 ns (~4 cycles) | Per-core | Immediate data needs |
| **L2** | 256-512 KB | 3 ns (~12 cycles) | Per-core | Recent data |
| **L3** | 8-32 MB | 10 ns (~40 cycles) | All cores | Working set |

### L1 Cache: Split Design

L1 is typically split into two parts:

- **L1-I (Instruction)**: Stores machine code being executed
- **L1-D (Data)**: Stores data being processed

```
CPU Fetch Unit ──▶ L1-I Cache ──▶ Instructions
CPU Load/Store ──▶ L1-D Cache ──▶ Data
```

### Cache Lines

Caches operate on **cache lines**, typically 64 bytes:

```
Cache Line (64 bytes)
┌────────────────────────────────────────────────────────────┐
│ byte0 │ byte1 │ byte2 │ ... │ byte62 │ byte63 │
└────────────────────────────────────────────────────────────┘

When you access byte0, the entire line is loaded — bytes 1-63
are available at no extra cost if accessed before the line is evicted
```

This is why sequential access is fast:

```python
import numpy as np

arr = np.arange(1000000, dtype=np.float64)

# Sequential: each cache line serves 8 elements (64/8)
for i in range(len(arr)):
    _ = arr[i]  # 7 of 8 accesses are "free" cache hits

# Strided: may miss cache on every access
for i in range(0, len(arr), 100):
    _ = arr[i]  # Each access likely misses cache
```

### Cache Associativity

Caches use **sets** to organize data. **N-way associativity** means N cache lines can map to each set:

```
8-way Set-Associative Cache
┌─────────────────────────────────────────────────────────┐
│ Set 0: │Line│Line│Line│Line│Line│Line│Line│Line│      │
│ Set 1: │Line│Line│Line│Line│Line│Line│Line│Line│      │
│ Set 2: │Line│Line│Line│Line│Line│Line│Line│Line│      │
│  ...                                                    │
└─────────────────────────────────────────────────────────┘

Memory address determines which SET
Any of 8 LINES within set can hold the data

Address bits:  | tag | set index | offset (6 bits for 64-byte line) |
               used to    selects     selects byte
               check if   which set   within line
               it's a hit
```

**Conflict misses** occur when many addresses map to the same set, evicting useful data even though other sets have free space.

### Cache Replacement

When a cache set is full, which line gets evicted? CPUs approximate **LRU (Least Recently Used)** using hardware heuristics like pseudo-LRU or tree-PLRU, since true LRU tracking is too expensive for highly associative caches:

```
Set with 4 lines, LRU replacement:

Access A: [A, -, -, -]
Access B: [A, B, -, -]
Access C: [A, B, C, -]
Access D: [A, B, C, D]  ← Full
Access E: [E, B, C, D]  ← A evicted (least recent)
Access B: [E, B, C, D]  ← B stays (recently used)
Access F: [E, B, F, D]  ← C evicted
```

## Cache Performance Metrics

### Hit Rate

```
Hit Rate = Cache Hits / Total Accesses
```

Hit rates vary greatly by workload — dense linear algebra may achieve 95%+ while streaming large arrays or graph traversal may be much lower. There is no single "good" or "bad" number; it depends entirely on data size, access pattern, and working set relative to cache size.

### Miss Types

| Miss Type | Cause | Solution |
|-----------|-------|----------|
| **Compulsory** | First access to data | Prefetching |
| **Capacity** | Working set too large | Reduce data size |
| **Conflict** | Multiple addresses map to same set | Better data layout |

## Observing Cache Effects

```python
import numpy as np
import time

def cache_demo():
    # Array sizes targeting different cache levels
    sizes = {
        'L1 (32KB)': 32 * 1024 // 8,
        'L2 (256KB)': 256 * 1024 // 8,
        'L3 (8MB)': 8 * 1024 * 1024 // 8,
        'RAM (64MB)': 64 * 1024 * 1024 // 8,
    }
    
    for name, n in sizes.items():
        arr = np.random.rand(n)
        
        # Warm up
        _ = np.sum(arr)
        
        # Time repeated access
        start = time.perf_counter()
        for _ in range(100):
            _ = np.sum(arr)
        elapsed = time.perf_counter() - start
        
        bytes_processed = n * 8 * 100
        bandwidth = bytes_processed / elapsed / 1e9
        print(f"{name:15}: {bandwidth:6.1f} GB/s")

cache_demo()
```

Expected output shows bandwidth drop as data exceeds cache:

```
L1 (32KB)      :  180.0 GB/s
L2 (256KB)     :  120.0 GB/s
L3 (8MB)       :   70.0 GB/s
RAM (64MB)     :   35.0 GB/s
```

Exact boundaries between cache levels are fuzzy in practice — hardware prefetchers, memory-level parallelism (CPUs can issue multiple memory requests simultaneously), vectorization, and OS scheduling all affect measured bandwidth.

## Cache-Friendly Python Code

### Good: Sequential Access (Conceptual)

```python
import numpy as np

arr = np.random.rand(10000, 10000)

# Sequential access - cache friendly pattern
# (but Python loop overhead dominates; use NumPy instead)
total = 0
for row in arr:
    for val in row:
        total += val
```

### Bad: Strided Access (Conceptual)

```python
# Column-major access in row-major array - cache hostile pattern
# (Python loop overhead dominates here too)
total = 0
for col in range(arr.shape[1]):
    for row in range(arr.shape[0]):
        total += arr[row, col]  # Jumps 80KB between accesses!
```

!!! warning "Python Loop Overhead"
    Both examples above are dominated by Python interpreter overhead (~50-100 ns per iteration), which dwarfs cache effects (~1-100 ns). These loops illustrate the **conceptual access patterns** but should not be used for real performance measurement. Use NumPy vectorized operations to observe actual cache effects.

### Best: Let NumPy Handle It

```python
# NumPy's compiled C code uses cache-optimized access patterns
total = np.sum(arr)  # 100x+ faster than Python loops
```

## Summary

| Component | Size | Latency | Key Point |
|-----------|------|---------|-----------|
| **Registers** | ~128 B | ~1 cycle | Compiler + register renaming hardware |
| **L1 Cache** | ~32 KB data + ~32 KB instr | ~4 cycles | Split I/D, per-core |
| **L2 Cache** | 256-512 KB | 12 cycles | Per-core |
| **L3 Cache** | 8-32 MB | 40 cycles | Shared across cores |

Key insights:

- Registers are the only "free" memory access
- Cache works automatically but benefits from sequential access patterns
- Cache lines (64 bytes) mean nearby data comes free
- Working set size determines which cache level you hit
- NumPy's speed comes partly from cache-friendly memory layout
