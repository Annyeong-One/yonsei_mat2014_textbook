
# CPU Microarchitecture and Performance


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

While computer architecture describes the **overall structure of a computer system**,  
**microarchitecture** describes how a particular CPU implements that architecture internally.

Modern CPU performance depends heavily on microarchitectural techniques such as:

- instruction pipelining
- superscalar execution
- out-of-order execution
- branch prediction
- cache hierarchies
- prefetching

These mechanisms allow CPUs to execute many instructions simultaneously and reduce idle time caused by slow memory access.

---

# 1. The Performance Gap: CPU vs Memory

CPU speeds have increased much faster than memory speeds.

Typical latency comparison (approximate):

| Component | Latency |
|----------|--------|
| Registers | ~1 cycle |
| L1 cache | ~4 cycles |
| L2 cache | ~12 cycles |
| L3 cache | ~40 cycles |
| RAM | ~100+ cycles |

Because memory access is slow relative to CPU speed, modern processors rely heavily on **caches** and **parallel instruction execution** to keep the CPU busy.

---

# 2. Instruction-Level Parallelism (ILP)

Modern CPUs try to execute multiple instructions at the same time.

Example:

```python
a = b + c
d = e + f
g = h * i
````

These operations are independent, so the CPU may execute them in parallel.

This capability is called **instruction-level parallelism (ILP)**.

Two major techniques enable ILP:

* pipelining
* superscalar execution

---

# 3. Pipelining

Instruction execution is divided into stages:

Fetch → Decode → Execute → Writeback

Instead of waiting for one instruction to finish before starting another, the CPU overlaps stages.

Example pipeline timeline:

Cycle:          1        2        3        4
Instruction A:  Fetch    Decode   Execute  Write
Instruction B:           Fetch    Decode   Execute
Instruction C:                    Fetch    Decode

This significantly increases instruction throughput.

---

# 4. Superscalar Execution

A **superscalar CPU** can issue multiple instructions per clock cycle.

Example execution units inside a CPU core:

* multiple ALUs
* floating point units
* load/store units
* vector units

If instructions are independent, the CPU may execute several at once.

Typical desktop CPUs can issue **2–6 instructions per cycle**.

---

# 5. Out-of-Order Execution

Some instructions take longer than others (especially memory loads).

If the CPU waited for each instruction in strict order, performance would suffer.

Instead, CPUs dynamically reorder instructions.

Example:

Original program order:

1. LOAD A
2. LOAD B
3. ADD C

If instruction 2 is waiting on memory, instruction 3 may execute earlier.

The CPU ensures the **final results still appear in program order**.

---

# 6. Branch Prediction

Branches disrupt pipelines because the CPU does not know which instruction comes next.

Example:

```python
if x > 0:
    do_A()
else:
    do_B()
```

Modern CPUs use **branch predictors** to guess which path will execute.

If the prediction is correct:

* the pipeline continues smoothly

If the prediction is wrong:

* the CPU must discard speculative work and restart the pipeline

Accurate branch prediction is critical for high performance.

---

# 7. CPU Caches

Caches store recently used data close to the CPU.

Typical hierarchy:

| Level | Location | Size                     |
| ----- | -------- | ------------------------ |
| L1    | per-core | ~32–64 KB                |
| L2    | per-core | ~512 KB – 2 MB           |
| L3    | shared   | several MB to tens of MB |

When data is requested:

1. CPU checks L1 cache
2. then L2
3. then L3
4. finally RAM

Cache hits are much faster than RAM access.

---

# 8. Prefetching

CPUs attempt to predict future memory accesses and load data into cache before it is needed.

Example:

```python
for i in range(n):
    total += arr[i]
```

Hardware prefetchers detect the pattern and load upcoming cache lines early.

This hides memory latency and improves performance.

---

# 9. Why This Matters for Python

Although Python is an interpreted language, microarchitecture still influences performance.

### Vectorized Libraries

Libraries such as **NumPy** use optimized C loops and SIMD instructions, allowing CPUs to exploit instruction-level parallelism.

### Memory Locality

Contiguous memory access patterns perform much better than scattered objects.

Example:

NumPy array → contiguous memory
Python list → many separate objects

Cache-friendly data structures significantly improve performance.

### Branch-heavy Code

Frequent unpredictable branches can reduce performance due to branch misprediction.

---

# Summary

| Technique              | Purpose                                 |
| ---------------------- | --------------------------------------- |
| Pipelining             | Overlap instruction stages              |
| Superscalar execution  | Execute multiple instructions per cycle |
| Out-of-order execution | Avoid stalls from slow instructions     |
| Branch prediction      | Reduce pipeline stalls                  |
| Caches                 | Hide memory latency                     |
| Prefetching            | Load data before it is needed           |

Understanding CPU microarchitecture helps explain why some programs run faster than others, even when the algorithm is the same.

