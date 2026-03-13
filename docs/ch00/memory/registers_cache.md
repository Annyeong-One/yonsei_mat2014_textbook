

# Registers and Cache

Registers and caches are the **fastest storage locations in a computer**. They sit between the CPU's execution units and main memory, allowing programs to operate on data with extremely low latency.

Because modern processors execute instructions much faster than data can be retrieved from RAM, these small but fast storage layers play a critical role in overall performance.

Understanding registers and caches explains why:

* sequential array processing is fast
* random memory access is slow
* vectorized operations outperform loops
* NumPy is dramatically faster than Python lists for numerical computation

---

# 1. Registers: The Fastest Storage

**Registers** are small storage locations located directly inside the CPU.

They are used to hold:

* intermediate computation results
* operands for arithmetic instructions
* memory addresses
* loop counters and temporary variables

Because registers are part of the processor itself, accessing them requires **only one CPU cycle**.

---

## Register characteristics

Typical properties for modern x86-64 CPUs:

| Property                            | Value        |
| ----------------------------------- | ------------ |
| Number of general-purpose registers | 16           |
| Register size                       | 64 bits      |
| Total capacity                      | ~128 bytes   |
| Access latency                      | ~1 CPU cycle |

Compared to other memory layers, registers are extremely small but extremely fast.

---

## Register usage example

A simple arithmetic operation in machine code might look like:

```text id="j30v79"
ADD RAX, RBX
```

This instruction adds the value in register `RBX` to register `RAX`.

Because both operands are already in registers, the operation completes in a single cycle.

---

### Visualization

```mermaid id="pso53r"
flowchart LR
    A[Register RAX] --> C[ALU]
    B[Register RBX] --> C
    C --> D[Result stored in RAX]
```

---

# 2. Register Allocation

Registers are limited resources. Programs often require more temporary values than available registers.

Two mechanisms help manage this constraint:

---

## Compiler allocation

Compilers attempt to keep frequently used values in registers.

Example:

```c id="0t86d4"
c = a + b
```

The compiler loads `a` and `b` into registers, performs the addition, and stores the result.

---

## Register renaming

Modern CPUs dynamically map logical registers to physical registers using **register renaming**.

This allows processors to:

* avoid false dependencies
* execute instructions out of order
* improve pipeline utilization

These mechanisms are invisible to software but critical for high performance.

---

# 3. Cache Memory

Caches store recently accessed memory values closer to the CPU.

They are implemented using fast **SRAM** rather than the slower **DRAM** used for main memory.

---

## Cache hierarchy

Most processors use multiple cache levels.

| Cache | Size     | Latency    |
| ----- | -------- | ---------- |
| L1    | ~32 KB   | ~4 cycles  |
| L2    | ~256 KB  | ~12 cycles |
| L3    | ~8–32 MB | ~40 cycles |

---

## L1 cache split

The L1 cache is usually divided into two separate caches:

| Cache | Purpose           |
| ----- | ----------------- |
| L1-I  | instruction cache |
| L1-D  | data cache        |

This separation allows instruction fetching and data access to occur simultaneously.

---

### Cache hierarchy visualization

```mermaid id="0z48xp"
flowchart TD
    CPU --> L1[L1 Cache]
    L1 --> L2[L2 Cache]
    L2 --> L3[L3 Cache]
    L3 --> RAM[Main Memory]
```

Data moves down the hierarchy when needed.

---

# 4. Cache Lines

Caches store memory in blocks called **cache lines**.

Typical size:

```text id="r1k5tq"
64 bytes
```

When a single byte is requested, the entire cache line containing that byte is loaded.

---

## Example

Suppose a program reads memory address:

```text id="9z8htc"
100
```

The CPU loads the block:

```text id="ck7p9p"
64-byte region containing address 100
```

This block might include addresses:

```text id="cy2og1"
64–127
```

---

### Visualization

```mermaid id="uz1ipf"
flowchart LR
    A[Memory block 64 bytes] --> B[Cache line]
    B --> C[CPU accesses data]
```

This design improves performance when nearby data is accessed.

---

# 5. Sequential Access and Cache Efficiency

Cache lines make **sequential memory access** extremely efficient.

Consider a NumPy array of `float64` values.

Each element uses:

```text id="a4kbf7"
8 bytes
```

Because cache lines contain **64 bytes**, each cache line stores:

```text id="z3k82c"
8 float64 values
```

Thus a single cache miss loads eight elements.

---

## Example access pattern

Sequential access:

```text id="l2jqfh"
arr[0], arr[1], arr[2], arr[3]
```

Behavior:

| Access | Result     |
| ------ | ---------- |
| arr[0] | cache miss |
| arr[1] | cache hit  |
| arr[2] | cache hit  |
| arr[3] | cache hit  |

---

### Visualization

```mermaid id="k4qnh2"
flowchart LR
    A[arr[0]] --> B[cache line loaded]
    B --> C[arr[1]]
    B --> D[arr[2]]
    B --> E[arr[3]]
```

---

# 6. Cache Associativity

Caches are organized into **sets** containing multiple cache lines.

The number of lines per set defines the **associativity**.

---

## Types of caches

| Type              | Description       |
| ----------------- | ----------------- |
| Direct-mapped     | one line per set  |
| N-way associative | N lines per set   |
| Fully associative | any line anywhere |

Most modern caches are **8-way or 16-way associative**.

---

## Conflict misses

A **conflict miss** occurs when multiple memory addresses map to the same cache set.

If more addresses compete for a set than the associativity allows, lines must be repeatedly evicted.

This can degrade performance significantly.

---

### Visualization

```mermaid id="pd1c88"
flowchart TD
    A[Memory address] --> B[Cache set]
    C[Memory address] --> B
    D[Memory address] --> B

    B --> E[Cache lines]
```

If too many addresses map to the same set, older lines are evicted.

---

# 7. SIMD Registers and Vectorization

Modern CPUs include **SIMD (Single Instruction Multiple Data)** registers.

These registers allow a single instruction to operate on multiple data elements simultaneously.

---

## SIMD register types

| Register | Size     |
| -------- | -------- |
| XMM      | 128 bits |
| YMM      | 256 bits |
| ZMM      | 512 bits |

Example capacities:

| Data type | Values per register (256-bit) |
| --------- | ----------------------------- |
| float32   | 8                             |
| float64   | 4                             |

---

### Visualization

```mermaid id="zj2in6"
flowchart LR
    A[SIMD register] --> B[value1]
    A --> C[value2]
    A --> D[value3]
    A --> E[value4]
```

Multiple values are processed in parallel.

---

# 8. NumPy and Vectorized Computation

NumPy operations are fast because they:

1. operate on **contiguous memory**
2. use **SIMD instructions**
3. run in **compiled C code**

Example:

```python id="aq9p5c"
import numpy as np

a = np.arange(1_000_000)
b = np.arange(1_000_000)

c = a + b
```

Instead of performing one addition at a time, the CPU processes multiple elements per instruction using SIMD registers.

---

# 9. Python Interpreter Overhead

Pure Python arithmetic is much slower because each operation involves many steps.

Example:

```python id="y10tdg"
x = a + b
```

Internally this requires:

1. type checking
2. method dispatch
3. object allocation
4. reference counting

Instead of a single machine instruction, Python may execute **dozens of instructions**.

---

### Visualization

```mermaid id="pnjv1k"
flowchart TD
    A[Python expression] --> B[type checks]
    B --> C[object operations]
    C --> D[allocation]
    D --> E[result]
```

NumPy bypasses this overhead by operating on raw memory arrays in compiled code.

---

# 10. Observing Cache Effects

The impact of cache size can be observed experimentally.

When arrays fit in cache, operations are very fast.

When arrays exceed cache capacity, performance drops because data must be fetched from slower memory.

---

## Example experiment

```python id="i21ylt"
import numpy as np
import time

for name, n in [('L1 32KB', 4000), ('L2 256KB', 32000),
                ('L3 8MB', 1000000), ('RAM 64MB', 8000000)]:

    arr = np.random.rand(n)
    _ = np.sum(arr)

    start = time.perf_counter()
    for _ in range(100):
        _ = np.sum(arr)

    elapsed = time.perf_counter() - start
    bw = (n * 8 * 100) / elapsed / 1e9

    print(f"{name:12}: {bw:6.1f} GB/s")
```

Typical result:

* small arrays → high bandwidth
* large arrays → slower bandwidth

---

# 11. Strided Access and Cache Waste

Cache lines improve sequential access but can be wasted by **strided access patterns**.

---

## Example

```python id="5j7bq1"
arr = np.arange(1_000_000, dtype=np.float64)

total_seq = np.sum(arr)
total_strided = np.sum(arr[::64])
```

The strided version accesses only one element per cache line, wasting most of the data fetched.

---

### Visualization

```mermaid id="qjot8r"
flowchart LR
    A[Cache line] --> B[value used]
    A --> C[value unused]
    A --> D[value unused]
    A --> E[value unused]
```

---

# 12. Worked Examples

### Example 1

How many `float64` values fit in a 256-bit SIMD register?

[
256 / 64 = 4
]

---

### Example 2

If a cache line is 64 bytes and each value is 8 bytes:

[
64 / 8 = 8
]

So one cache miss loads 8 elements.

---

### Example 3

Explain why NumPy operations outperform Python loops.

NumPy performs operations in compiled code using SIMD registers and contiguous memory, avoiding interpreter overhead.

---

# 13. Exercises

1. What are CPU registers used for?
2. How large are general-purpose registers on x86-64?
3. What is a cache line?
4. Why is sequential memory access faster than random access?
5. What is SIMD?
6. How many float64 values fit in a 512-bit register?
7. What causes conflict misses?
8. Why is NumPy faster than Python loops?

---

# 14. Short Answers

1. Temporary storage for CPU operations
2. 64 bits
3. Block of memory transferred between cache and RAM
4. Cache lines preload nearby values
5. Single Instruction Multiple Data processing
6. 8
7. Multiple addresses mapping to the same cache set
8. Vectorized compiled operations and contiguous memory

---

# 15. Summary

* **Registers** are the fastest storage in a computer and hold temporary computation data.
* **Caches** store recently accessed memory to reduce RAM access latency.
* Memory is transferred in **cache lines**, typically 64 bytes.
* Sequential access benefits from **spatial locality**.
* **Cache associativity** affects how memory addresses map to cache sets.
* **SIMD registers** allow multiple values to be processed in parallel.
* NumPy exploits SIMD and contiguous memory to achieve much higher performance than Python loops.

Understanding registers and cache behavior is essential for writing **efficient numerical and high-performance code**.
