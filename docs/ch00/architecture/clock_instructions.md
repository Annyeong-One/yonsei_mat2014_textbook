# Clock Speed and Instructions

CPU performance depends on two factors: how fast the clock ticks (frequency) and how much work each tick accomplishes (instructions per cycle). Understanding both is essential for reasoning about why code runs at the speed it does.

## Definition

**Clock speed** (frequency) is the number of clock cycles a CPU completes per second, measured in GHz. A 4 GHz CPU completes 4 billion cycles per second, with each cycle lasting 0.25 nanoseconds.

**Instructions per cycle (IPC)** is the average number of instructions a CPU retires in one clock cycle. Effective throughput is the product of both:

$$
\text{Throughput} \approx \text{Clock Speed} \times \text{IPC}
$$

## Explanation

Clock speed alone does not determine performance. A 3 GHz CPU with IPC of 4 outperforms a 4 GHz CPU with IPC of 2 (12 vs. 8 billion instructions per second). Modern CPUs boost IPC through three mechanisms:

- **Pipelining**: Overlapping instruction stages (fetch, decode, execute, write) so a new instruction completes roughly every cycle.
- **Superscalar execution**: Multiple execution units (ALUs, load/store units) process several instructions simultaneously, achieving IPC greater than 1.
- **Out-of-order execution**: The CPU dynamically reorders independent instructions to keep execution units busy while others wait for memory.

**Branch prediction** allows the CPU to speculatively execute one path of a conditional before the condition is resolved. Mispredictions flush the pipeline, wasting 10-20 cycles. Modern predictors exceed 95% accuracy for typical code.

**Memory latency** is often the dominant bottleneck. At 4 GHz, a single RAM access (~60 ns, ~240 cycles) wastes enough time for hundreds of instructions. This is why cache locality matters more than raw clock speed for memory-intensive workloads.

| Level | Approximate Latency |
|-------|---------------------|
| L1 cache | 3-5 cycles |
| L2 cache | 10-15 cycles |
| L3 cache | 30-50 cycles |
| RAM | 200-400 cycles |

## Examples

```python
# Cycle time at 4 GHz
cycle_time = 1 / 4_000_000_000  # 0.25 nanoseconds per cycle
print(f"Cycle time: {cycle_time * 1e9:.2f} ns")
```

```python
import numpy as np
import time

def estimate_gflops():
    """Estimate floating-point throughput via matrix multiplication."""
    n = 2048
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    flops = 2 * n ** 3  # standard GEMM operation count
    start = time.perf_counter()
    C = A @ B
    elapsed = time.perf_counter() - start

    gflops = (flops / elapsed) / 1e9
    print(f"Performance: {gflops:.1f} GFLOPS")

estimate_gflops()  # Typically 100-500 GFLOPS with optimized BLAS
```

```python
import timeit

# Measure Python-level operation cost
result = timeit.timeit('sum(range(1000))', number=10000)
print(f"Average: {result / 10000 * 1e6:.2f} microseconds")
```
