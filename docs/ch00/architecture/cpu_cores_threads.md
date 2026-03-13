

# CPU Cores and Threads

Modern processors contain multiple independent execution units called **cores**. Operating systems schedule program execution onto these cores using **threads**.

Understanding how cores, threads, and processes interact is essential for writing efficient concurrent and parallel programs, especially in Python.

Many performance issues in Python arise not from CPU speed but from how work is distributed across cores and how the Python runtime interacts with hardware.

---

## 1. CPU Cores

A **CPU core** is an independent hardware execution unit capable of running its own instruction stream.

Each core contains:

* arithmetic and logical execution units
* registers
* instruction pipelines
* private caches (L1 and often L2)

Multiple cores allow a processor to execute several programs or tasks simultaneously.

---

## Example CPU configuration

| Component      | Example      |
| -------------- | ------------ |
| CPU package    | 1            |
| Physical cores | 4            |
| Logical cores  | 8 (with SMT) |

---

### Multi-core CPU visualization

```mermaid
flowchart LR
    CPU --> Core1
    CPU --> Core2
    CPU --> Core3
    CPU --> Core4
```

Each core can independently fetch and execute instructions.

---

## 2. Processes

A **process** is an isolated execution environment created by the operating system.

Each process has:

* its own **virtual address space**
* its own **heap and stack**
* its own **system resources**

Processes are isolated from one another for security and stability.

---

## Process structure

```mermaid
flowchart TD
    Process --> Code
    Process --> Heap
    Process --> Stack
```

Because processes have separate address spaces, they cannot directly access each other’s memory.

Communication between processes typically occurs through **inter-process communication (IPC)** mechanisms such as pipes, sockets, or shared memory.

---

## 3. Threads

A **thread** is a lightweight execution unit within a process.

Threads share the process memory but maintain their own execution state.

Each thread has:

* its own stack
* its own program counter
* its own registers

However, threads share:

* the process heap
* global variables
* open files

---

### Thread structure

```mermaid
flowchart LR
    Process --> Thread1
    Process --> Thread2
    Process --> Thread3

    Thread1 --> Stack1
    Thread2 --> Stack2
    Thread3 --> Stack3
```

Because threads share memory, communication between them is faster than between processes.

However, shared memory also introduces risks such as **race conditions**.

---

## 4. Simultaneous Multithreading (SMT)

Many modern CPUs support **Simultaneous Multithreading (SMT)**.

Intel refers to this technology as **Hyperthreading**.

SMT allows one physical core to support **multiple logical threads**.

---

## How SMT works

A single core maintains multiple register states so that it can switch between threads when one stalls.

For example, if one thread is waiting for memory, another thread can use the core’s execution units.

---

### SMT visualization

```mermaid
flowchart LR
    Core --> ThreadA
    Core --> ThreadB
```

SMT improves utilization of CPU resources but does not double performance.

Typical gains range from **10% to 30%**, depending on workload.

---

## 5. Concurrency vs Parallelism

Two important concepts often confused in programming are **concurrency** and **parallelism**.

---

## Concurrency

Concurrency refers to a program structure in which multiple tasks can make progress independently.

Tasks may be interleaved on a single CPU core.

Example:

```
Task A
Task B
Task A
Task B
```

---

## Parallelism

Parallelism refers to tasks executing **simultaneously** on different CPU cores.

Example:

```
Core 1 → Task A
Core 2 → Task B
```

---

### Visualization

```mermaid
flowchart LR
    Concurrency --> Interleaving
    Parallelism --> SimultaneousExecution
```

Concurrency is necessary to exploit parallel hardware, but concurrency alone does not guarantee parallel execution.

---

## 6. The Global Interpreter Lock (GIL)

One important constraint in CPython is the **Global Interpreter Lock (GIL)**.

The GIL ensures that **only one thread executes Python bytecode at a time** within a single process.

---

## Why the GIL exists

The GIL simplifies memory management in CPython by protecting shared data structures such as reference counts.

However, it also prevents Python threads from achieving true parallelism for CPU-bound tasks.

---

## Implication

Python threads cannot parallelize CPU-bound computations.

Example:

```python
for i in range(10_000_000):
    total += i
```

Running this loop in multiple Python threads will not use multiple CPU cores.

---

## When the GIL is released

The GIL is temporarily released during:

* blocking I/O operations
* system calls
* execution of many C extensions (NumPy, SciPy, BLAS)

This allows threads to run concurrently during I/O waits.

---

## 7. Amdahl’s Law

Even with many CPU cores, the speedup of a program is limited by the portion of the code that cannot be parallelized.

This relationship is described by **Amdahl’s Law**.

[
S(n) = \frac{1}{s + \frac{1-s}{n}}
]

Where:

* (S(n)) = speedup using (n) cores
* (s) = fraction of execution time that is serial
* (n) = number of cores

---

## Example

If 10% of a program is serial:

```
s = 0.10
```

Even with infinite cores:

[
S_{max} = \frac{1}{0.10} = 10
]

Thus the maximum speedup is **10×**, regardless of hardware.

---

### Speedup visualization

```mermaid
flowchart LR
    SerialPart --> LimitsSpeedup
    ParallelPart --> UsesCores
```

Amdahl’s Law highlights the importance of minimizing serial sections of code.

---

## 8. Choosing the Right Parallelism Strategy

Different workloads benefit from different parallel programming techniques.

---

## CPU-bound workloads

Use **multiprocessing**.

Each process runs on a separate CPU core and bypasses the GIL.

---

## I/O-bound workloads

Use **threading** or **asyncio**.

Threads can overlap I/O waits even with the GIL.

---

## Numerical computation

Use **NumPy, SciPy, or BLAS libraries**.

These libraries release the GIL and often use parallel native code internally.

---

### Strategy summary

| Workload            | Recommended Tool    |
| ------------------- | ------------------- |
| CPU-bound Python    | multiprocessing     |
| I/O-bound           | threading / asyncio |
| numerical workloads | NumPy / SciPy       |

---

## 9. Example: Counting CPU Cores

```python
import os

print(os.cpu_count())
```

This returns the number of **logical cores** available to the operating system.

For example:

```
8
```

may correspond to a **4-core CPU with SMT**.

---

## 10. Example: Parallel Processing with Multiprocessing

```python
import multiprocessing

def compute(x):
    return x * x

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(compute, range(100))

print(results[:5])
```

Each worker process runs independently on a separate CPU core.

---

## 11. Example: Threading for I/O

```python
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as resp:
        return len(resp.read())

urls = ["https://example.com"] * 4

with ThreadPoolExecutor(max_workers=4) as executor:
    sizes = list(executor.map(fetch, urls))

print(sizes)
```

Here threads overlap network latency.

---

## 12. Summary

| Concept      | Explanation                                       |
| ------------ | ------------------------------------------------- |
| Core         | independent CPU execution unit                    |
| Thread       | lightweight execution context within a process    |
| Process      | isolated execution environment                    |
| SMT          | multiple logical threads per core                 |
| Concurrency  | tasks make progress independently                 |
| Parallelism  | tasks execute simultaneously                      |
| GIL          | allows only one Python thread to execute bytecode |
| Amdahl’s Law | limits achievable parallel speedup                |

Modern CPUs contain many cores capable of executing multiple threads simultaneously.

However, achieving high performance requires understanding:

* how operating systems schedule threads
* how Python interacts with hardware
* how parallel algorithms scale

By structuring programs to minimize serial work and using appropriate parallel tools, developers can effectively utilize modern multi-core processors.
