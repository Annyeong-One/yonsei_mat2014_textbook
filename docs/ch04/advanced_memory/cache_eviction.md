
# Cache Eviction


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview

CPU caches are **limited in size**. When the cache becomes full, the processor must decide which existing data to remove in order to make room for new data.

This process is called **cache eviction**.

Because caches are designed to hold the **most useful and recently accessed data**, eviction policies attempt to remove data that is less likely to be needed again soon.

---

## Why Eviction Is Necessary

A typical CPU cache is small compared to main memory.

Example sizes (approximate):

| Level | Size |
|------|------|
| L1 cache | 32–64 KB per core |
| L2 cache | 512 KB – 2 MB per core |
| L3 cache | several MB to tens of MB |
| RAM | gigabytes |

Because the cache cannot store all memory data, older entries must be replaced as new data arrives.

---

## Eviction Policies

The CPU uses **eviction policies** to decide which cache line to remove.

Common strategies include:

| Policy | Idea |
|------|------|
| **LRU (Least Recently Used)** | Remove the data that has not been used for the longest time |
| **LFU (Least Frequently Used)** | Remove the data that has been used least often |
| **Random** | Remove a randomly selected cache line |

In practice, many CPUs implement **pseudo-LRU**, which approximates LRU but is cheaper to implement in hardware.

---

## The Sliding Window Model

A useful way to think about cache eviction is as a **sliding window of recently used data**.

```

new data → enters cache
old data → evicted

````

The cache therefore tends to contain the **current working set** of the program.

---

## Example

Consider a program that processes a large array:

```python
for i in range(n):
    total += arr[i]
````

As the loop progresses:

1. New cache lines are loaded from memory.
2. Older cache lines that are no longer needed are evicted.
3. The cache continually updates to keep the most relevant data.

---

## Why Eviction Matters

Eviction behavior can strongly influence performance.

Programs that reuse data frequently benefit from **temporal locality**, allowing data to remain in cache longer.

Programs that access large datasets randomly may constantly evict useful data, causing frequent **cache misses** and slower execution.

Designing algorithms that reuse data efficiently helps minimize unnecessary cache eviction.


