# Registers and Cache

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
| **Count** | 16 general-purpose (x86-64) |
| **Total Capacity** | ~128 bytes general-purpose |
| **Access Time** | 0 cycles (immediate) |
| **Managed By** | Compiler |

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

At the machine level, this becomes (conceptually):

```assembly
; Simplified - actual CPython is more complex
MOV RAX, [a_address]    ; Load 'a' into register
MOV RBX, [b_address]    ; Load 'b' into register
ADD RAX, RBX            ; Add in register
MOV [x_address], RAX    ; Store result
```

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
XMM register:    128 bits  → holds 2 float64s
YMM register:    256 bits  → holds 4 float64s
ZMM register:    512 bits  → holds 8 float64s
```

NumPy uses both — its compiled C code exploits SIMD instructions where possible. This is one of the core reasons NumPy is so fast: not just "compiled C" but "compiled C that uses SIMD vectorization." Your Python code never sees any of this — it just calls `c = a + b` and NumPy handles the rest invisibly.

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
| **L1** | 32-64 KB | 1 ns (~4 cycles) | Per-core | Immediate data needs |
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

When you access byte0, bytes 1-63 come along for free!
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
```

### Cache Replacement

When a cache set is full, which line gets evicted? Usually **LRU (Least Recently Used)**:

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

Good code: 95-99% hit rate
Poor code: 50-80% hit rate
```

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

## Cache-Friendly Python Code

### Good: Sequential Access

```python
import numpy as np

# Sequential access - cache friendly
arr = np.random.rand(10000, 10000)
total = 0
for row in arr:
    for val in row:
        total += val
```

### Bad: Strided Access

```python
# Column-major access in row-major array - cache hostile
total = 0
for col in range(arr.shape[1]):
    for row in range(arr.shape[0]):
        total += arr[row, col]  # Jumps 80KB between accesses!
```

### Best: Let NumPy Handle It

```python
# NumPy's sum is cache-optimized
total = np.sum(arr)  # 100x+ faster than Python loops
```

## Summary

| Component | Size | Latency | Key Point |
|-----------|------|---------|-----------|
| **Registers** | ~128 B | 0 cycles | Managed by compiler |
| **L1 Cache** | 32-64 KB | 4 cycles | Split I/D, per-core |
| **L2 Cache** | 256-512 KB | 12 cycles | Per-core |
| **L3 Cache** | 8-32 MB | 40 cycles | Shared across cores |

Key insights:

- Registers are the only "free" memory access
- Cache works automatically but benefits from sequential access patterns
- Cache lines (64 bytes) mean nearby data comes free
- Working set size determines which cache level you hit
- NumPy's speed comes partly from cache-friendly memory layout
