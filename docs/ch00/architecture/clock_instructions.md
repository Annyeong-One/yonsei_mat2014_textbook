# Clock Speed and Instructions

## The CPU Clock

Every CPU's timing originates from a crystal oscillator, which feeds internal clock generators (via phase-locked loops) that synchronize all CPU operations.

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

Clock speeds plateaued around 2005 due to:

- **Power consumption**: Higher frequencies require more power
- **Heat dissipation**: Power becomes heat that must be removed
- **Diminishing returns**: Other bottlenecks (memory) limit benefits

## Instructions Per Cycle (IPC)

Clock speed alone doesn't determine performance. **IPC** measures how many instructions complete per cycle:

```
Performance ≈ Clock Speed × IPC
```

### Why IPC Varies

Different instructions take different numbers of cycles:

| Operation | Typical Latency (cycles) |
|-----------|--------------------------|
| Register-to-register add | 1 |
| L1 cache access | 4 |
| L2 cache access | 12 |
| Multiply | 3-5 |
| Divide | 10-40 |
| RAM access | 200+ |

### Pipelining Increases IPC

Modern CPUs overlap instruction stages:

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

Modern predictors achieve >95% accuracy for typical code, but unpredictable branches hurt performance:

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
```

## FLOPS: Floating-Point Performance

**FLOPS** (Floating-point Operations Per Second) measures computational throughput:

| Scale | Abbreviation | Operations/Second |
|-------|-------------|-------------------|
| Mega | MFLOPS | 10⁶ |
| Giga | GFLOPS | 10⁹ |
| Tera | TFLOPS | 10¹² |
| Peta | PFLOPS | 10¹⁵ |

Modern CPU cores can reach tens to hundreds of GFLOPS depending on vector width (e.g., AVX2 vs AVX-512) and clock speed. A GPU can achieve 10+ TFLOPS.

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
# Python operations take thousands of CPU cycles
x = a + b  # thousands of cycles (type check, dict lookup, allocation)

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
| **IPC** | Instructions completed per cycle |
| **Pipelining** | Overlapping instruction stages |
| **Superscalar** | Multiple instructions per cycle |
| **Branch Prediction** | Guessing conditional outcomes |
| **FLOPS** | Floating-point operations per second |

Key insights for Python programmers:

- Clock speed × IPC ≈ instruction throughput
- Memory access often dominates execution time
- Branch-heavy Python code suffers from misprediction overhead
- NumPy achieves high FLOPS by amortizing Python overhead
- Modern CPUs are limited by memory bandwidth, not raw speed
