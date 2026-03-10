
# Cache Lines


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

CPUs do not transfer individual bytes between memory and cache.

Instead, data moves in **fixed-size blocks called cache lines**.

On most modern CPUs, a cache line is **64 bytes**.

This means when the CPU reads a single value from memory, it actually loads the **entire 64-byte cache line containing that value** into the cache.

---

## Why Cache Lines Exist

Memory transfers are expensive. Moving data in blocks improves efficiency because nearby data is often used together.

This property is called **spatial locality**.

Example:

```python
for i in range(n):
    total += arr[i]
````

When `arr[0]` is accessed, the CPU loads a cache line that may contain:

```
arr[0], arr[1], arr[2], arr[3], ...
```

The next values are therefore **already in the cache**.

---

## Sequential vs Random Access

Cache lines make **sequential access much faster** than random access.

Sequential example:

```python
for i in range(n):
    total += arr[i]
```

Random example:

```python
for i in random_indices:
    total += arr[i]
```

Sequential access benefits from cache lines, while random access causes frequent **cache misses**.

---

## Cache Line Diagram

Example layout of a 64-byte cache line:

```
Cache Line (64 bytes)
-----------------------------------------
| value0 | value1 | value2 | value3 | ...
-----------------------------------------
```

When the CPU loads `value0`, the entire line enters the cache.

---

## Why This Matters

Cache lines explain several performance patterns:

* **Arrays are faster than scattered objects**
* **Sequential algorithms outperform random memory access**
* **Contiguous data structures (NumPy arrays, C arrays) are cache-friendly**

Understanding cache lines helps explain why memory layout can significantly affect program performance.


