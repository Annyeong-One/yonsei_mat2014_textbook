# CPU Cores and Threads


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Think of a modern CPU as a **factory with multiple assembly lines**. Each **core** is an independent assembly line capable of executing instructions. Multiple cores allow the processor to work on several tasks simultaneously. Within each core, the processor contains specialized machinery — execution units, caches, and pipelines — that transform instructions into completed work.

However, these assembly lines do not operate in isolation. They share critical infrastructure such as memory bandwidth and last-level cache. Operating systems schedule **threads** onto these cores, and in Python, an additional constraint — the **Global Interpreter Lock (GIL)** — restricts how threads can run in parallel. This chapter explains the hardware and software layers that determine how your code actually runs on a modern CPU.

```
Layers of Execution

┌───────────────────────────────┐
│        Python Program         │
│   (threads, asyncio, tasks)   │
└───────────────▲───────────────┘
                │
┌───────────────┴───────────────┐
│        Python Runtime         │
│      (GIL, interpreter)       │
└───────────────▲───────────────┘
                │
┌───────────────┴───────────────┐
│        Operating System       │
│   (threads, processes,        │
│    scheduler, context switch) │
└───────────────▲───────────────┘
                │
┌───────────────┴───────────────┐
│            Hardware           │
│   (cores, caches, pipelines)  │
└───────────────────────────────┘
```

## What Is a Core?

A modern CPU is not a single processor but a collection of independent execution engines called **cores**. Understanding what a core contains is essential for reasoning about parallel performance.

A **core** is an independent execution engine capable of running its own instruction stream. Each core typically includes its own:

- **Execution units** — arithmetic/logic units (ALUs), branch units, load/store units
- **Registers** — fast on-chip storage holding the current thread's state
- **L1 cache** — private, fastest cache (~4 cycles latency, typically 32–64 KB)
- **L2 cache** — often private to each core, though some architectures share it among small groups of cores (~12 cycles)

**L3 cache** is shared across all cores on the same chip, acting as a common pool (~40 cycles latency, typically 8–64 MB on desktops; server CPUs may exceed 100 MB). Cores also share **memory controllers** and the **on-chip interconnect**.

Multiple cores can execute different instructions simultaneously — this is **true parallelism**.

However, cores still compete for shared resources such as memory bandwidth and cache capacity. This contention can limit scaling before Amdahl's Law alone would predict.

## From Single-Core to Multi-Core

Early CPUs had a single core. Clock frequency scaling delivered consistent performance gains through the 1990s, but by the mid-2000s this hit hard physical limits: dynamic power roughly scales with $V^2 \times f$. Increasing frequency typically requires higher voltage, which makes the practical power increase steeper than linear. This made further clock scaling impractical. The industry pivoted to putting **multiple cores on one chip** instead.

```
Single-Core CPU (early 2000s)        Quad-Core CPU (today)
┌──────────────────────┐             ┌───────────────────────────────┐
│   ┌────────────┐     │             │  ┌─────────┐   ┌─────────┐   │
│   │    Core    │     │             │  │ Core 0  │   │ Core 1  │   │
│   │ (ALU, Reg) │     │             │  │(L1, L2) │   │(L1, L2) │   │
│   └─────┬──────┘     │             │  └────┬────┘   └────┬────┘   │
│   ┌─────┴──────┐     │             │  ┌────┴────┐   ┌────┴────┐   │
│   │  L1/L2     │     │             │  │ Core 2  │   │ Core 3  │   │
│   │  Cache     │     │             │  │(L1, L2) │   │(L1, L2) │   │
│   └────────────┘     │             │  └────┬────┘   └────┬────┘   │
└──────────────────────┘             │       └──────┬───────┘        │
                                     │    ┌─────────┴──────────┐     │
                                     │    │   Shared L3 Cache  │     │
                                     │    └────────────────────┘     │
                                     └───────────────────────────────┘
```

## Physical vs Logical Cores

Modern CPUs expose more "cores" to the operating system than actually exist in hardware. This happens because of a technique called simultaneous multithreading.

### Physical Cores

Physical cores are the actual distinct hardware execution units. A quad-core CPU has four independent pipelines that can each execute a separate stream of instructions.

### Logical Cores and SMT (Hyperthreading)

**Simultaneous Multithreading (SMT)** — Intel's marketing name is **Hyperthreading** — allows one physical core to present itself to the operating system as two logical cores.

The key insight is that a single core's execution units are rarely fully utilized. A thread often stalls waiting for data from memory (a cache miss can cost 200+ cycles). SMT exploits these idle cycles by maintaining two separate **architectural states** (register files, program counters, stack pointers) and switching between them in hardware:

```
Physical Core with SMT (Hyperthreading)

  ┌───────────────────────────────────────────────┐
  │                  Physical Core                │
  │                                               │
  │  ┌──────────────────┐  ┌──────────────────┐  │
  │  │   Thread 0       │  │   Thread 1       │  │
  │  │  (private regs,  │  │  (private regs,  │  │
  │  │   program ctr,   │  │   program ctr,   │  │
  │  │   stack pointer) │  │   stack pointer) │  │
  │  └────────┬─────────┘  └────────┬─────────┘  │
  │           └──────────┬──────────┘             │
  │                      ▼                        │
  │  ┌─────────────────────────────────────────┐  │
  │  │         Shared Issue Queue              │  │
  │  └──────────────────┬──────────────────────┘  │
  │  ┌──────────────────┴──────────────────────┐  │
  │  │       Shared Execution Units            │  │
  │  │  (ALUs, branch unit, load/store unit)   │  │
  │  └─────────────────────────────────────────┘  │
  │  ┌─────────────────────────────────────────┐  │
  │  │          Shared L1 Cache                │  │
  │  └─────────────────────────────────────────┘  │
  │  ┌─────────────────────────────────────────┐  │
  │  │          Shared L2 Cache                │  │
  │  └─────────────────────────────────────────┘  │
  └───────────────────────────────────────────────┘
```

> **Important**: Both SMT threads run on the same physical core and therefore share the core's private resources, including the L1 cache, execution units, instruction pipeline, and reorder buffer. Each thread's private registers (including program counter and stack pointer) are truly separate. The shared execution units — ALUs, branch units, load/store units — are scheduled between threads in hardware.

Both threads' instructions enter the pipeline, and the scheduler can issue instructions from either thread depending on which has ready instructions — when Thread 0 stalls on a cache miss, the core fills those slots with Thread 1's instructions, keeping execution units busy. In practice, SMT yields **15–30% more throughput** for mixed workloads, not a full 2×. Threads also compete for internal resources such as reorder buffer entries, instruction fetch bandwidth, and execution ports. For some workloads (where both threads compete heavily for these resources or for cache), SMT can even reduce performance.

```python
import os

# os.cpu_count() returns the number of logical cores (including hyperthreads)
print(f"Logical cores: {os.cpu_count()}")  # e.g., 8 on a 4-core/8-thread CPU

# There is no standard-library function that returns only physical cores.
# The distinction is conceptual: a 4-core/8-thread CPU has 4 physical cores,
# each presenting 2 logical cores via SMT.
```

## Concurrency vs Parallelism

These terms are frequently conflated but describe fundamentally different things. Understanding the distinction is essential for reasoning about multi-threaded programs.

### Concurrency

**Concurrency** is a property of program *structure*: the program is organized as multiple tasks that can make progress independently, without requiring each to finish before the next begins.

On a single core, the OS **time-slices** between threads — each gets a short quantum (typically 1–10 ms), then is preempted so another can run:

```
Concurrent execution on a single core (time-slicing)

Core 0: [Task A]─[Task B]─[Task A]─[Task B]─[Task A]
        ──────────────────────────────────────────────▶ Time

Tasks interleave. Only one runs at any instant.
```

### Parallelism

**Parallelism** is a property of *execution*: multiple tasks are literally running at the same physical instant on separate hardware units.

```
Parallel execution on multiple cores

Core 0: [────────────── Task A ──────────────]
Core 1: [────────────── Task B ──────────────]
        ──────────────────────────────────────▶ Time

Both tasks run simultaneously.
```

### The Relationship

Concurrency and parallelism are orthogonal concepts:

| | Concurrent structure | Sequential structure |
|---|---|---|
| **Multiple cores** | Concurrent + parallel | Sequential (only one core used) |
| **Single core** | Concurrent (interleaved) | Purely sequential |

A useful framing: **concurrency is about dealing with many things at once; parallelism is about doing many things at once** (Rob Pike). You can have concurrency without parallelism (a single-core server juggling many connections), and you need concurrent program structure to exploit parallelism (you cannot parallelize an inherently sequential program).

## Threads vs Processes

Operating systems provide two primary ways to run multiple streams of execution: processes and threads. They differ in how memory and resources are shared.

### Process

A **process** is an independent execution environment with its own:

- **Virtual address space** (memory is fully isolated from other processes)
- **File descriptor table**
- **OS resources** (signal handlers, environment, working directory)

The OS enforces isolation: Process A cannot read or write Process B's memory without explicit IPC mechanisms (pipes, shared memory, sockets).

### Thread

A **thread** is a lightweight unit of execution *within* a process. All threads in a process share:

- The same heap (dynamically allocated objects, global variables)
- The same file descriptors and OS resources

Each thread has its own:

- **Stack** (local variables and call frames)
- **Registers** (including the program counter — where it is in the code)

```
Process (shared address space)
┌──────────────────────────────────────────────────┐
│  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ Thread 1 │  │ Thread 2 │  │ Thread 3 │       │
│  │  stack   │  │  stack   │  │  stack   │       │
│  │  regs    │  │  regs    │  │  regs    │       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘       │
│       └─────────────┼─────────────┘              │
│                     ▼                             │
│  ┌────────────────────────────────────────────┐  │
│  │              Shared Heap                   │  │
│  │  (objects, global variables, file handles) │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

**Trade-off**: threads are cheaper to create and communicate easily through shared memory, but that shared memory requires careful synchronization (locks, semaphores) to avoid **race conditions**. Processes are safer (isolated by default) but inter-process communication has higher overhead.

## Python and the GIL

Python's execution model adds an additional constraint on parallelism. Even on a multi-core machine, Python threads cannot normally execute CPU-bound code in parallel.

### The Global Interpreter Lock

CPython (the standard Python implementation) uses a **Global Interpreter Lock (GIL)**: a mutex that ensures only one thread executes Python bytecode at a time, even on a multi-core machine. Native extensions that release the GIL can run in parallel across cores.

The GIL exists primarily because CPython's reference-counting memory management would otherwise require atomic updates on every object access.

The consequence for CPU-bound workloads is stark:

```
CPU-bound Python threads — what actually happens

              GIL held by Thread 1     GIL held by Thread 2
              ◄──────────────────►     ◄──────────────────►
Core 0: [  Thread 1  ][          ][  Thread 1  ][          ]
Core 1: [            ][ Thread 2 ][            ][ Thread 2 ]
        ─────────────────────────────────────────────────────▶ Time

Only one thread executes Python bytecode at a time.
The other thread is blocked waiting for the GIL, even if a free core exists.
Total throughput is no better than a single thread.
```

The GIL is **automatically released** in two situations:
1. **Blocking I/O** — when a thread calls `read()`, `recv()`, etc., it releases the GIL while waiting for the OS, letting other threads run.
2. **C extensions** — libraries like NumPy release the GIL around their inner computation loops, enabling real multi-core use.

### Python 3.13+: The Free-Threaded Build

Python 3.13 introduced an **experimental no-GIL build** (`python3.13t`), and Python 3.12 added per-subinterpreter GILs. These changes are opt-in and the ecosystem is still adapting, but they suggest a long-term direction toward removing the GIL for CPU-bound parallelism.

### Workarounds (Current Practice)

**For I/O-bound tasks** (network requests, disk reads): threads work well, since the GIL is released during I/O.

```python
import threading
import requests

def fetch_url(url, results, index):
    response = requests.get(url)   # GIL released while waiting for network
    results[index] = response.text

urls = ["https://example.com", "https://example.org"]
results = [None] * len(urls)
threads = [threading.Thread(target=fetch_url, args=(url, results, i))
           for i, url in enumerate(urls)]

for t in threads:
    t.start()
for t in threads:
    t.join()   # wait for all threads to finish
```

**For I/O-bound tasks with many concurrent connections**: `asyncio` is often preferable to threads. It uses a single thread with an **event loop** — tasks voluntarily yield control at `await` points rather than being preempted by the OS. This avoids thread overhead entirely and scales to thousands of concurrent connections.

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)
```

**For CPU-bound tasks**: use `multiprocessing`. Each process gets its own Python interpreter and GIL, so they truly run in parallel.

```python
import multiprocessing

def compute(x):
    return x * x

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute, range(100))
```

**For CPU-bound numerical work**: NumPy releases the GIL around its C-level kernels and links against multi-threaded BLAS (e.g., OpenBLAS, MKL), so operations like matrix multiplication use multiple cores automatically.

```python
import numpy as np

# np.dot releases the GIL; OpenBLAS/MKL spawns threads across cores internally
result = np.dot(A, B)   # A, B are large 2D arrays
```

## OS Scheduling and Core Affinity

The OS **scheduler** decides which thread runs on which core at each moment. It maintains a **run queue** of ready threads and dispatches them to available cores:

```
OS Scheduler (run queue → cores)

  Ready: [T1][T2][T3][T4][T5]
               │
         ┌─────┼──────┐
         ▼     ▼      ▼
      ┌──────┬──────┬──────┐
      │Core 0│Core 1│Core 2│
      └──────┴──────┴──────┘
```

The scheduler also handles **context switches**: saving the register state of a running thread and restoring another's. Thread context switches avoid switching address spaces, so they are typically cheaper than process switches, though they still incur cache and pipeline disruption. Process switches are more expensive, though modern CPUs use **PCID/ASID tagging** to reduce TLB flushing costs. In both cases, the indirect costs — cache pollution and branch predictor disruption — often matter more than the direct register save/restore.

**CPU affinity** pins a process or thread to a specific set of cores. This is rarely needed but can reduce **cache thrashing** when a critical thread keeps migrating between cores and losing its warm cache:

```python
import os
import psutil  # third-party: pip install psutil

p = psutil.Process(os.getpid())
p.cpu_affinity([0, 1])   # restrict this process to cores 0 and 1
print(p.cpu_affinity())  # [0, 1]
```

Use affinity only when profiling reveals a concrete benefit — the OS scheduler is generally well-tuned.

## Amdahl's Law: The Ceiling on Parallel Speedup

Adding more cores does not give proportional speedup. Every real program has a **serial fraction** — setup, I/O coordination, sequential data dependencies — that cannot be parallelized. Amdahl's Law quantifies the resulting ceiling.

If a fraction $s$ of total runtime is inherently serial, the maximum speedup $S(n)$ achievable with $n$ cores is:

$$S(n) = \frac{1}{s + \dfrac{1-s}{n}}$$

As $n \to \infty$, $S(n) \to 1/s$. The serial portion alone determines the hard limit, regardless of how many cores you add.

**Concrete example**: suppose 10% of your program is serial ($s = 0.1$).

| Cores ($n$) | Speedup $S(n)$ | Efficiency $S(n)/n$ |
|---|---|---|
| 1 | 1.00× | 100% |
| 2 | 1.82× | 91% |
| 4 | 3.08× | 77% |
| 8 | 4.71× | 59% |
| 16 | 6.40× | 40% |
| ∞ | **10.0×** | → 0% |

With 10% serial code, you can never exceed a 10× speedup no matter how many cores you use. Doubling from 8 to 16 cores only gains 1.7×.

**The practical implication**: before adding more parallelism, profile and reduce the serial bottleneck. Halving the serial fraction (from 10% to 5%) doubles the theoretical ceiling (from 10× to 20×), more than any number of additional cores would achieve.

## Practical Guidelines

### Choosing an Approach

| Workload | Recommended Tool | Why |
|---|---|---|
| CPU-bound Python | `multiprocessing` | Bypasses GIL; each process has own interpreter |
| I/O-bound, many connections | `asyncio` | Event loop; no thread overhead; scales to 10k+ connections |
| I/O-bound, moderate concurrency | `threading` | Simpler code; GIL released during I/O |
| Numerical computation | NumPy / SciPy | BLAS-level parallelism; GIL released in C kernels |
| Mixed or flexible | `concurrent.futures` | Uniform API over threads and processes |

### Choosing Worker Count

```python
import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

# CPU-bound: start with the number of available CPU cores
cpu_workers = os.cpu_count() or 1

# I/O-bound: can safely exceed core count since threads mostly wait.
# Optimal values depend heavily on latency and workload characteristics; tune empirically.
io_workers = (os.cpu_count() or 1) * 4  # starting point; adjust based on profiling

# CPU-bound example
with ProcessPoolExecutor(max_workers=cpu_workers) as executor:
    results = list(executor.map(cpu_task, data_chunks))

# I/O-bound example
with ThreadPoolExecutor(max_workers=io_workers) as executor:
    results = list(executor.map(io_task, urls))
```

For CPU-bound tasks, profiling may reveal that fewer workers than `os.cpu_count()` perform better, since hyperthreads share physical core resources.

## Summary

| Concept | Description |
|---|---|
| **Core** | Independent hardware execution unit with private L1/L2 cache |
| **Logical core (SMT)** | Software-visible thread slot on a physical core; shares execution units |
| **Thread** | Lightweight execution context within a process; shares heap with siblings |
| **Process** | Isolated execution environment with its own memory space |
| **Concurrency** | Program structure enabling multiple tasks to make progress (possibly interleaved) |
| **Parallelism** | Simultaneous execution on multiple cores |
| **GIL** | CPython mutex serializing bytecode execution; prevents CPU-bound thread parallelism |
| **Amdahl's Law** | Serial fraction $s$ caps speedup at $1/s$ regardless of core count |

The four key takeaways for Python practitioners:

1. **Python threads don't parallelize CPU-bound code** — the GIL serializes bytecode execution.
2. **Use `multiprocessing` for CPU-bound tasks** — separate processes each have their own GIL.
3. **Use `asyncio` or threads for I/O-bound tasks** — the GIL is released during I/O waits.
4. **More cores have diminishing returns** — Amdahl's Law means reducing the serial bottleneck is often more effective than adding workers.
