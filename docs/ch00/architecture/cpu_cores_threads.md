# CPU Cores and Threads

Modern CPUs contain multiple independent execution engines called cores, and operating systems schedule threads onto them. Understanding this hardware-software interaction is essential for writing concurrent Python programs.

## Definition

A **core** is an independent hardware execution unit with its own ALU, registers, and L1/L2 caches. Multiple cores execute different instruction streams simultaneously (true parallelism).

A **thread** is a lightweight execution context within a process. Threads share the process heap but each has its own stack and registers. A **process** is an isolated execution environment with its own virtual address space.

**Simultaneous Multithreading (SMT)** -- Intel calls it Hyperthreading -- allows one physical core to present two logical cores to the OS by maintaining separate register states and filling idle execution slots when one thread stalls.

## Explanation

**Concurrency vs. parallelism**: Concurrency is a program structure where multiple tasks can make progress independently (possibly interleaved on one core). Parallelism is simultaneous execution on separate cores. You need concurrent structure to exploit parallel hardware.

**The GIL constraint**: CPython's Global Interpreter Lock ensures only one thread executes Python bytecode at a time. This means Python threads cannot parallelize CPU-bound work. The GIL is released during blocking I/O and inside C extensions like NumPy.

**Amdahl's Law** sets the ceiling on parallel speedup. If a fraction $s$ of runtime is serial, maximum speedup with $n$ cores is:

$$
S(n) = \frac{1}{s + \frac{1-s}{n}}
$$

With 10% serial code, you can never exceed 10x speedup regardless of core count.

**Practical guidelines**:

| Workload | Tool | Reason |
|----------|------|--------|
| CPU-bound Python | `multiprocessing` | Bypasses GIL with separate processes |
| I/O-bound | `threading` or `asyncio` | GIL released during I/O waits |
| Numerical computation | NumPy/SciPy | GIL released in C kernels; BLAS parallelism |

## Examples

```python
import os

# Logical cores include hyperthreads
print(f"Logical cores: {os.cpu_count()}")  # e.g., 8 on a 4-core/8-thread CPU
```

```python
import multiprocessing

def compute(x):
    return x * x

# CPU-bound: use separate processes to bypass the GIL
if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute, range(100))
    print(results[:5])  # [0, 1, 4, 9, 16]
```

```python
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as resp:
        return len(resp.read())

# I/O-bound: threads work well because the GIL is released during network I/O
urls = ["https://example.com"] * 4
with ThreadPoolExecutor(max_workers=4) as executor:
    sizes = list(executor.map(fetch, urls))
print(sizes)
```
