# Von Neumann Architecture

The Von Neumann architecture is the foundational blueprint behind nearly every modern computer. Understanding it explains why memory access dominates performance, why cache locality matters, and why NumPy arrays outperform Python lists.

## Definition

The **Von Neumann architecture** is a stored-program computer model in which program instructions and data share the same memory space and are accessed through the same bus. A Von Neumann machine consists of four components:

1. **CPU** — containing a control unit (CU), an arithmetic logic unit (ALU), and registers
2. **Memory** — a single address space holding both instructions and data
3. **I/O devices** — peripherals for input and output
4. **Bus system** — the interconnect linking CPU, memory, and I/O

The **Von Neumann bottleneck** is the fundamental throughput limitation that arises because instructions and data compete for the same memory channel: the CPU must wait for each memory access to complete before proceeding, and processor speed has far outpaced memory speed.

## Explanation

### The Stored-Program Concept

Before Von Neumann's 1945 design, computers were programmed by physically rewiring circuits. The stored-program concept treats instructions as data — both live in the same memory. This means a program can be loaded, modified, and replaced without changing hardware, which is the basis of all modern software.

### Fetch–Decode–Execute–Writeback Cycle

Programs execute through a repeating four-step cycle:

1. **Fetch** — read the instruction at the address in the Program Counter (PC)
2. **Decode** — the control unit interprets the instruction's opcode and operands
3. **Execute** — the ALU or other functional unit performs the operation
4. **Writeback** — the result is stored back to a register or memory; the PC advances

This cycle repeats until the program terminates or an interrupt occurs.

### The Bus System

The bus has three logical parts:

| Bus | Direction | Purpose |
|-----|-----------|---------|
| **Address bus** | CPU → memory | Specifies which memory location to access |
| **Data bus** | Bidirectional | Transfers data between CPU and memory |
| **Control bus** | Bidirectional | Carries timing, read/write, and interrupt signals |

Because a single data bus serves both instructions and data, the CPU cannot fetch an instruction and read data simultaneously — this is the Von Neumann bottleneck in hardware terms.

### Memory Hierarchy

Modern systems mitigate the bottleneck with a hierarchy of progressively larger and slower storage:

| Level | Typical latency | Typical size |
|-------|-----------------|--------------|
| Registers | ~1 cycle | ~1 KB |
| L1 cache | ~4 cycles | 32–64 KB |
| L2 cache | ~12 cycles | 256 KB–1 MB |
| L3 cache | ~40 cycles | 4–32 MB |
| RAM | ~200 cycles | 8–64 GB |
| SSD / disk | ~100,000+ cycles | TB-scale |

This hierarchy works because of two locality principles:

- **Temporal locality** — recently accessed data is likely to be accessed again soon
- **Spatial locality** — data near a recently accessed address is likely to be accessed next

### Modified Harvard Architecture

Most modern CPUs use a **modified Harvard architecture**: main memory remains unified (Von Neumann style), but the L1 cache is split into separate instruction and data caches. This allows the CPU to fetch an instruction and read data in parallel at the cache level, reducing the bottleneck while preserving the stored-program model.

### Why This Matters for Python

Python lists store an array of pointers, each pointing to a heap-allocated object at an arbitrary memory address. Iterating over a list means chasing pointers to scattered locations — poor spatial locality, frequent cache misses.

NumPy arrays store values contiguously in a single memory block. Walking through an array touches consecutive addresses — excellent spatial locality, efficient cache prefetching. But memory layout is only half the advantage. NumPy operations also run in compiled C loops that process raw values directly, bypassing the per-element cost of Python's interpreter: no boxing/unboxing, no dynamic type dispatch, no reference-count updates. The combination of cache-friendly layout and compiled execution is what makes NumPy dramatically faster.

## Examples

```
┌─────────────────────────────────────────────────────┐
│                        CPU                          │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐ │
│  │ Control  │  │   ALU    │  │    Registers      │ │
│  │  Unit    │  │          │  │ (PC, IR, R0–Rn)   │ │
│  └──────────┘  └──────────┘  └───────────────────┘ │
└────────────────────┬────────────────────────────────┘
                     │  Address Bus ↓   Data Bus ↕   Control Bus ↕
              ═══════╧══════════════════════════════════════
              ║            System Bus                      ║
              ═══════╤════════════════════╤════════════════
                     │                    │
          ┌──────────┴──────────┐  ┌──────┴──────┐
          │       Memory        │  │  I/O Devices │
          │  ┌───────────────┐  │  │  (keyboard,  │
          │  │ Instructions  │  │  │   display,   │
          │  ├───────────────┤  │  │   disk, …)   │
          │  │     Data      │  │  │              │
          │  └───────────────┘  │  └──────────────┘
          └─────────────────────┘
```

### Object Size: Python int vs. Raw Value

```python
import sys

# Every Python integer is a heap-allocated object with metadata
x = 42
print(sys.getsizeof(x))  # 28 bytes on 64-bit CPython
# Breakdown: ob_refcnt (8) + ob_type pointer (8) + ob_size (8) + digit (4) = 28
```

### Memory Layout: NumPy Array vs. Python List

```python
import sys
import numpy as np

# NumPy: one contiguous block of 8-byte float64 values -- cache-friendly
arr = np.zeros(1_000_000, dtype=np.float64)

# Python list: array of pointers, each to a separate heap object
lst = [float(i) for i in range(1_000_000)]  # distinct float objects

arr_bytes = arr.nbytes
lst_bytes = sys.getsizeof(lst) + sys.getsizeof(lst[0]) * len(lst)

print(f"NumPy array: {arr_bytes / 1e6:.1f} MB (contiguous raw data)")
print(f"Python list: ~{lst_bytes / 1e6:.1f} MB (pointers + scattered objects)")
```

### Performance: Contiguous Memory and Compiled Loops

```python
import numpy as np
import time

n = 1_000_000
arr = np.arange(n, dtype=np.float64)
lst = [float(i) for i in range(n)]  # same type (floats) for fair comparison

start = time.perf_counter()
_ = np.sum(arr)
numpy_time = time.perf_counter() - start

start = time.perf_counter()
_ = sum(lst)
list_time = time.perf_counter() - start

print(f"NumPy sum: {numpy_time:.4f}s")
print(f"List sum:  {list_time:.4f}s")
print(f"Ratio:     {list_time / numpy_time:.0f}x slower")
# Both cache locality (contiguous vs scattered) and compiled C execution
# (no per-element Python overhead) contribute to the difference.
```
