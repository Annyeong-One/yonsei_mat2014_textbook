# CPU Cores and Threads

## From Single-Core to Multi-Core

Early CPUs had a single core—one execution unit that processed instructions sequentially. Clock speeds eventually faced power and thermal limits, so performance improvements increasingly came from parallelism through multiple cores.

```
Single-Core CPU (2000s)          Multi-Core CPU (Today)
┌─────────────────────┐          ┌─────────────────────────────┐
│     ┌───────┐       │          │  ┌───────┐    ┌───────┐    │
│     │ Core  │       │          │  │ Core 0│    │ Core 1│    │
│     └───────┘       │          │  └───────┘    └───────┘    │
│         │           │          │      │            │        │
│     ┌───────┐       │          │  ┌───────┐    ┌───────┐    │
│     │L1/L2  │       │          │  │ Core 2│    │ Core 3│    │
│     └───────┘       │          │  └───────┘    └───────┘    │
└─────────────────────┘          │         │    │             │
                                 │     ┌───────────────┐      │
                                 │     │ Shared L3 Cache│      │
                                 │     └───────────────┘      │
                                 └─────────────────────────────┘
```

## What is a Core?

A **core** is a complete, independent processing unit capable of executing instructions. Each core typically has its own execution units, registers, and L1 cache, and often its own L2 cache. L3 cache is usually shared across all cores.

Multiple cores can execute different instructions simultaneously—true parallelism.

```python
import os

# Check number of CPU cores
print(os.cpu_count())  # e.g., 8
```

## Physical vs Logical Cores

### Physical Cores

The actual hardware execution units on the CPU die.

### Logical Cores (Hyperthreading/SMT)

**Simultaneous Multithreading (SMT)**, Intel's version called **Hyperthreading**, allows one physical core to appear as two logical cores:

```
Physical Core with Hyperthreading
┌─────────────────────────────────────────┐
│           Physical Core                 │
│  ┌─────────────┐  ┌─────────────┐      │
│  │  Thread 0   │  │  Thread 1   │      │
│  │  (Arch.     │  │  (Arch.     │      │
│  │   State)    │  │   State)    │      │
│  └──────┬──────┘  └──────┬──────┘      │
│         │                │              │
│         └───────┬────────┘              │
│                 ▼                       │
│  ┌─────────────────────────────┐       │
│  │    Shared Execution Units   │       │
│  │    (ALU, Cache, etc.)       │       │
│  └─────────────────────────────┘       │
└─────────────────────────────────────────┘
```

Each logical thread has its own architectural state (registers, program counter), but shares execution resources (ALU, cache). This helps when one thread is stalled (e.g., waiting for memory), allowing the other thread to use the execution units.

```python
import psutil

# Distinguish physical from logical
print(f"Physical cores: {psutil.cpu_count(logical=False)}")
print(f"Logical cores:  {psutil.cpu_count(logical=True)}")

# Example output on a 4-core, 8-thread CPU:
# Physical cores: 4
# Logical cores:  8
```

## Threads vs Processes

### Process

A **process** is an independent program execution with its own:

- Memory space
- File handles
- System resources

Processes are isolated—one process cannot directly access another's memory.

### Thread

A **thread** is a lightweight execution unit within a process:

- Shares memory space with other threads in the same process
- Has its own stack and registers
- Can communicate easily with sibling threads

```
Process
┌─────────────────────────────────────────────────┐
│                                                 │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│   │ Thread 1│  │ Thread 2│  │ Thread 3│       │
│   │ (stack) │  │ (stack) │  │ (stack) │       │
│   └────┬────┘  └────┬────┘  └────┬────┘       │
│        │            │            │             │
│        └────────────┼────────────┘             │
│                     ▼                          │
│   ┌─────────────────────────────────────┐     │
│   │         Shared Memory (Heap)        │     │
│   │    (Global variables, objects)      │     │
│   └─────────────────────────────────────┘     │
│                                                 │
└─────────────────────────────────────────────────┘
```

## Parallelism vs Concurrency

These terms are often confused:

### Concurrency

Multiple tasks making progress over time, possibly by interleaving:

```
Concurrent (single core, time-slicing)

Core:  [Task A][Task B][Task A][Task B][Task A]
       ─────────────────────────────────────────▶ Time
```

Tasks take turns, giving the illusion of parallelism.

### Parallelism

Multiple tasks executing simultaneously on different cores:

```
Parallel (multiple cores)

Core 0: [────────── Task A ──────────]
Core 1: [────────── Task B ──────────]
        ─────────────────────────────▶ Time
```

True simultaneous execution.

### The Relationship

- **Concurrency** is about program structure — organizing a program as multiple tasks that can make progress independently
- **Parallelism** is about execution — tasks actually running at the same time on multiple hardware execution units (such as CPU cores)

Concurrency is about dealing with many things at once. Parallelism is about doing many things at once. A concurrent program can run on a single core (via time-slicing) or on multiple cores (with true parallelism). Parallelism requires both concurrent structure and multiple execution units.

## Python and Parallelism

### The GIL Problem

Python's **Global Interpreter Lock (GIL)** allows only one thread to execute Python bytecode at a time:

```
CPU-bound Python Threads on Multi-Core CPU

Core 0: [Thread 1][        ][Thread 1][        ]
Core 1: [        ][Thread 2][        ][Thread 2]
        └─────────────────────────────────────────▶

Only ONE thread executes Python bytecode at a time despite multiple cores!
```

This means Python threads don't achieve true parallelism for CPU-bound tasks. The GIL is automatically released during blocking I/O operations and by many C extensions (such as NumPy), allowing other threads to run while a thread is waiting.

### Workarounds

**For I/O-bound tasks** (waiting for network, disk):

```python
import threading

# Threads work well here - they release GIL while waiting
def fetch_url(url):
    response = requests.get(url)  # GIL released during I/O
    return response.text

threads = [threading.Thread(target=fetch_url, args=(url,)) 
           for url in urls]
```

**For CPU-bound tasks** (computation):

```python
import multiprocessing

# Processes bypass GIL - each has its own interpreter
def compute(data):
    return heavy_calculation(data)

with multiprocessing.Pool(4) as pool:
    results = pool.map(compute, data_chunks)
```

**Using NumPy** (releases GIL during computation):

```python
import numpy as np

# NumPy operations release GIL and can use multiple cores
result = np.dot(large_matrix1, large_matrix2)
```

## Core Affinity and Scheduling

The operating system's **scheduler** decides which threads run on which cores:

```
OS Scheduler
┌─────────────────────────────────────────────┐
│                                             │
│   Ready Queue: [T1] [T2] [T3] [T4] [T5]    │
│                                             │
│         ┌─────────┬─────────┐              │
│         ▼         ▼         ▼              │
│     ┌──────┐ ┌──────┐ ┌──────┐            │
│     │Core 0│ │Core 1│ │Core 2│            │
│     └──────┘ └──────┘ └──────┘            │
│                                             │
└─────────────────────────────────────────────┘
```

Python can set **CPU affinity** (which cores a process can use). This is usually unnecessary for most applications but can help in specialized performance tuning:

```python
import os
import psutil

# Get current process
p = psutil.Process(os.getpid())

# Set affinity to cores 0 and 1 only
p.cpu_affinity([0, 1])

# Check affinity
print(p.cpu_affinity())  # [0, 1]
```

## Practical Guidelines

| Task Type | Recommended Approach |
|-----------|---------------------|
| **CPU-bound Python** | `multiprocessing` (separate processes) |
| **I/O-bound Python** | `threading` or `asyncio` |
| **NumPy computation** | Let NumPy handle it (uses BLAS threads) |
| **Mixed workloads** | `concurrent.futures` for flexibility |

### Choosing Worker Count

```python
import psutil
from concurrent.futures import ProcessPoolExecutor

# For CPU-bound: use physical core count (hyperthreads rarely double performance)
cpu_workers = psutil.cpu_count(logical=False)

# For I/O-bound: can exceed core count
io_workers = os.cpu_count() * 2  # or more

with ProcessPoolExecutor(max_workers=cpu_workers) as executor:
    results = executor.map(cpu_task, data)
```

## Summary

| Concept | Description |
|---------|-------------|
| **Core** | Independent execution unit with own ALU and cache |
| **Thread** | Lightweight execution context within a process |
| **Hyperthreading** | One physical core appearing as two logical cores |
| **Parallelism** | Simultaneous execution on multiple cores |
| **Concurrency** | Multiple tasks making progress (possibly interleaved) |
| **GIL** | Python lock preventing true thread parallelism for CPU-bound code |

Understanding cores and threads explains why:

- Python threads don't speed up CPU-bound code
- `multiprocessing` bypasses the GIL
- NumPy can utilize multiple cores despite Python's limitations
- The number of workers should match your workload type

> **Amdahl's Law**: Adding more cores does not give linear speedups. If a fraction $s$ of a program is inherently serial, the maximum speedup with $n$ cores is $1 / (s + (1 - s) / n)$. Even with infinite cores, the serial portion limits the total speedup — which is why optimizing the serial bottleneck often matters more than adding cores.
