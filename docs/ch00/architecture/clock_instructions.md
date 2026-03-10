# Clock Speed and Instructions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The CPU Clock

Every CPU's timing originates from a crystal oscillator that provides a stable base frequency (often 100 MHz). PLL (phase-locked loop) circuits multiply this base frequency to generate the CPU's operating frequency, synchronizing all CPU operations.

```
Clock Signal
    │     │     │     │     │     │     │
────┴─────┴─────┴─────┴─────┴─────┴─────┴────
    ▲     ▲     ▲     ▲     ▲     ▲     ▲
   Cycle Cycle Cycle Cycle Cycle Cycle Cycle
```

Each pulse is a **clock cycle**—the fundamental unit of CPU time.

## Clock Speed (Frequency)

**Clock speed** measures cycles per second, expressed in Hertz (Hz):

| Unit | Cycles per Second | Era |
|------|------------------|-----|
| MHz | 1,000,000 | 1990s |
| GHz | 1,000,000,000 | 2000s-present |

A 4 GHz CPU completes 4 billion cycles per second.

```python
# Conceptually, one cycle at 4 GHz takes:
cycle_time = 1 / 4_000_000_000  # 0.25 nanoseconds
```

### Clock Speed History

```
Clock Speed Evolution
     │
5 GHz┤                              ┌───────
     │                         ┌────┘
4 GHz┤                    ┌────┘
     │               ┌────┘
3 GHz┤          ┌────┘
     │     ┌────┘
2 GHz┤┌────┘
     │
1 GHz┤
     └────────────────────────────────────────
      2000   2005   2010   2015   2020   2025

     "The clock speed wall" - heat/power limits
```

Frequency scaling slowed after the breakdown of **Dennard scaling** around the mid-2000s—the end of easy frequency scaling. Modern CPUs still increase turbo frequencies (e.g., Ryzen 7950X reaches ~5.7 GHz), but the real limit was **power density**, not absolute frequency:

- **Power consumption**: Higher frequencies require more power
- **Heat dissipation**: Power becomes heat that must be removed
- **Diminishing returns**: Other bottlenecks (memory) limit benefits

## Instructions Per Cycle (IPC)

Clock speed alone doesn't determine performance. **IPC** measures the number of instructions retired per cycle on average. IPC varies widely depending on the workload and memory access patterns.

```
Instruction Throughput ≈ Clock Speed × IPC
```

More formally, execution time can be expressed as:

```
Execution Time = Instructions × Cycles per Instruction × Seconds per Cycle
```

### Why IPC Varies

Different operations take different numbers of cycles:

**Arithmetic latency:**

| Operation | Approximate Latency (cycles) |
|-----------|------------------------------|
| Add | 1 |
| Multiply | 3–5 |
| Divide | 10–40 |

**Memory hierarchy latency:**

| Level | Approximate Latency (cycles) |
|-------|------------------------------|
| L1 cache | 3–5 |
| L2 cache | 10–15 |
| L3 cache | 30–50 |
| RAM | 200–400 |

### Pipelining Increases IPC

Modern CPUs overlap instruction stages. Pipelining increases instruction **throughput**, but does not reduce the **latency** of a single instruction:

```
Without Pipelining (one instruction every several cycles):
┌───────┬───────┬───────┬───────┐
│ Fetch │Decode │Execute│ Write │ Instruction 1
└───────┴───────┴───────┴───────┘
                                 ┌───────┬───────┬───────┬───────┐
                                 │ Fetch │Decode │Execute│ Write │ Inst 2
                                 └───────┴───────┴───────┴───────┘

With Pipelining (roughly one instruction per cycle):
┌───────┬───────┬───────┬───────┐
│ Fetch │Decode │Execute│ Write │ Instruction 1
└───────┼───────┼───────┼───────┤
        │ Fetch │Decode │Execute│ Write │ Instruction 2
        └───────┼───────┼───────┼───────┤
                │ Fetch │Decode │Execute│ Write │ Instruction 3
                └───────┴───────┴───────┴───────┘
```

### Superscalar Execution (IPC > 1)

Modern CPUs have multiple execution units, allowing several instructions per cycle:

```
Superscalar CPU

Cycle N:
  ALU 0: [ADD instruction]
  ALU 1: [SUB instruction]
  Load Unit: [LOAD instruction]
  Store Unit: [STORE instruction]

  Up to several instructions can complete in one cycle!
```

### Out-of-Order Execution

Modern CPUs dynamically reorder instructions to avoid pipeline stalls. Independent instructions can execute while others wait for memory, keeping execution units busy and increasing effective IPC. Modern CPUs can also issue multiple memory requests in parallel, a technique called **memory-level parallelism** (MLP).

```
Load A       ← waiting for RAM
Add B, C     ← executes immediately (independent)
Multiply D, E ← executes immediately (independent)
```

### ILP vs TLP

Modern CPUs exploit two forms of parallelism:

- **Instruction-Level Parallelism (ILP)**: Multiple instructions per cycle within a single core (via pipelining and superscalar execution)
- **Thread-Level Parallelism (TLP)**: Multiple cores executing independent threads simultaneously

Frequency scaling slowed after ~2005, so performance improvements increasingly relied on multi-core designs (TLP).

## Branch Prediction

Conditional branches create pipeline problems:

```python
if x > 0:
    result = expensive_a()
else:
    result = expensive_b()
```

The CPU must decide which path to fetch before knowing the condition result.

### Prediction and Misprediction

```
Branch Prediction

                    ┌─── Predicted Path (fetched speculatively)
                    │
if condition: ──────┤
                    │
                    └─── Other Path (not fetched)

If prediction is WRONG:
  - Pipeline flushed (10-20 cycles wasted)
  - Correct path fetched
```

Modern predictors achieve >95% accuracy for typical code. When a prediction is wrong, the CPU must flush the pipeline and roll back speculative execution, wasting 10–20 cycles. Unpredictable branches therefore hurt performance:

```python
import numpy as np

# Predictable branch (same outcome many times)
data = np.sort(np.random.randint(0, 256, 100000))
for x in data:
    if x < 128:  # False for first half, True for second
        total += x

# Unpredictable branch (random outcomes)
data = np.random.randint(0, 256, 100000)
for x in data:
    if x < 128:  # Randomly True/False
        total += x

# The unpredictable version is significantly slower!
# Note: In CPython the interpreter overhead dominates, but the effect
# becomes clearly visible in compiled code or NumPy kernels.
```

## Memory Hierarchy

The gap between CPU speed and memory speed is one of the dominant performance constraints in modern computing:

```
CPU vs Memory Speed Gap

L1 cache:  ~1 ns    (3–5 cycles)
L2 cache:  ~4 ns    (10–15 cycles)
L3 cache:  ~10 ns   (30–50 cycles)
RAM:       ~60–100+ ns (200–400+ cycles)
```

Two aspects of this gap matter:

- **Latency**: Time to access a single piece of data
- **Bandwidth**: Amount of data transferred per second

This explains why **cache locality often dominates performance in memory-intensive workloads**—a CPU at 4 GHz can execute hundreds of instructions in the time it takes to fetch a single value from RAM.

```
Good locality:  iterate sequentially through an array
Poor locality:  random pointer chasing (linked lists, hash maps)
```

## FLOPS: Floating-Point Performance

**FLOPS** (Floating-point Operations Per Second) measures computational throughput:

| Scale | Abbreviation | Operations/Second |
|-------|-------------|-------------------|
| Mega | MFLOPS | 10⁶ |
| Giga | GFLOPS | 10⁹ |
| Tera | TFLOPS | 10¹² |
| Peta | PFLOPS | 10¹⁵ |

A modern CPU core can theoretically reach tens to over 100 GFLOPS depending on vector width and FMA usage. These FLOPS rates rely on **SIMD** (Single Instruction, Multiple Data) vector instructions such as AVX2 or AVX-512 that process multiple values per cycle. A GPU can achieve 10+ TFLOPS.

```
Scalar:  add 1 number per instruction
SIMD:    add 8 numbers per instruction (AVX2, 256-bit)
```

### Python FLOPS Estimation

```python
import numpy as np
import time

def estimate_flops():
    n = 2048
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    
    # Matrix multiply: 2*n³ floating-point operations
    flops = 2 * n ** 3
    
    start = time.perf_counter()
    C = A @ B
    elapsed = time.perf_counter() - start
    
    gflops = (flops / elapsed) / 1e9
    print(f"Performance: {gflops:.1f} GFLOPS")

estimate_flops()  # Typically 100-500 GFLOPS with optimized BLAS
# Performance depends heavily on the BLAS library used (MKL, OpenBLAS, etc.)
```

## Why Clock Speed Doesn't Tell the Whole Story

### Same Clock, Different Performance

```
CPU A: 4 GHz, IPC = 2  →  8 billion instructions/sec
CPU B: 3 GHz, IPC = 4  →  12 billion instructions/sec

CPU B is faster despite lower clock speed!
```

### Memory Bottleneck

Even with high clock speeds, CPUs often wait for memory:

```
CPU at 4 GHz (0.25 ns/cycle)
RAM access: ~60 ns = 240 cycles

During those 240 cycles, the CPU could have executed
~1000 instructions if data were available!
```

This is why cache efficiency matters more than raw clock speed.

## Python Timing Considerations

### Time Resolution

```python
import time

# time.time() - wall clock, ~ms resolution
# time.perf_counter() - high resolution for benchmarking
# time.process_time() - CPU time only (excludes sleep)

start = time.perf_counter()
# ... code to benchmark ...
elapsed = time.perf_counter() - start
```

### Clock Cycles in Python

```python
# Python operations typically require thousands to tens of thousands of CPU
# cycles due to interpreter overhead
x = a + b  # type check, dict lookup, object allocation, etc.

# NumPy operations: Python overhead + very fast vectorized inner loop
np.add(arr1, arr2)  # Python dispatch overhead + fast SIMD loop
```

### Measuring CPU Cycles

```python
import timeit

# Measure with proper repetition
result = timeit.timeit(
    'sum(range(1000))',
    number=10000
)
print(f"Average: {result/10000*1e6:.2f} microseconds")
```

## Summary

| Concept | Description |
|---------|-------------|
| **Clock Speed** | Cycles per second (GHz) |
| **Clock Cycle** | Smallest time unit for CPU operations |
| **IPC** | Instructions retired per cycle |
| **Pipelining** | Overlapping instruction stages |
| **Superscalar** | Multiple instructions per cycle |
| **Branch Prediction** | Guessing conditional outcomes |
| **FLOPS** | Floating-point operations per second |

Key insights for Python programmers:

- Clock speed × IPC ≈ instruction throughput
- Memory access often dominates execution time
- Branch-heavy Python code suffers from misprediction overhead
- NumPy achieves high FLOPS by amortizing Python overhead
- Modern CPUs are often limited by memory latency and bandwidth, not raw speed
