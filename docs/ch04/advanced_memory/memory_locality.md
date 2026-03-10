
# Memory Locality


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

CPU caches rely on predictable memory access patterns to improve performance.  
Programs often access the same data repeatedly or access data located close together in memory.

These behaviors are called **memory locality**.

There are two primary types of locality:

- **Temporal locality**
- **Spatial locality**

---

## Temporal Locality

**Temporal locality** means that if a program accesses a value, it is likely to access the **same value again soon**.

Example:

```python
for i in range(1000):
    total += x
````

The variable `x` is used repeatedly inside the loop.
Once it is loaded into the CPU cache, it can be reused quickly without accessing RAM again.

This makes repeated operations on the same data very efficient.

---

## Spatial Locality

**Spatial locality** means that if a program accesses a memory location, it is likely to access **nearby memory locations** soon.

Example:

```python
for i in range(n):
    total += arr[i]
```

Arrays store elements **contiguously in memory**.
When the CPU loads `arr[i]`, the surrounding elements are also loaded into the cache because they belong to the same **cache line**.

This allows the next accesses to be very fast.

---

## Locality and Performance

Algorithms that follow locality patterns run much faster than those that access memory randomly.

Example comparison:

```
Sequential access → cache-friendly
Random access     → many cache misses
```

Cache-friendly algorithms make better use of the CPU cache hierarchy.

---

## Example: Lists vs Arrays

Memory layout strongly affects locality.

```
NumPy array → contiguous memory
Python list → many separate objects
```

Because NumPy arrays store elements in a single continuous block, they benefit greatly from **spatial locality**.

Python lists store references to objects scattered throughout memory, reducing cache efficiency.

---

## Why Locality Matters

Memory locality is one of the most important principles in high-performance computing.

Programs that access memory sequentially and reuse data frequently can be **orders of magnitude faster** than programs that jump randomly through memory.


