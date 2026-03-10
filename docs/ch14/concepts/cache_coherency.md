
# Cache Coherency

## Overview

Modern CPUs contain multiple cores, and each core typically has its own private caches (L1 and L2).  
This creates a challenge: **the same memory location may exist in multiple caches at the same time.**

Example:

```

Core 1 cache → copy of variable X
Core 2 cache → copy of variable X
RAM           → original X

```

If one core modifies its copy, the other cores' copies may become **stale**.

Ensuring that all cores see a **consistent view of memory** is called **cache coherency**.

---

# 1. The Coherency Problem

Consider two CPU cores running simultaneously.

Initial state:

```

RAM:        X = 10

Core 1 L1:  X = 10
Core 2 L1:  X = 10

```

Core 1 updates the value:

```

Core 1 writes: X = 20

```

Now the system may look like:

```

Core 1 L1:  X = 20
Core 2 L1:  X = 10   (stale!)
RAM:        X = 10

```

If Core 2 reads `X`, it may see an **outdated value**.

Cache coherency mechanisms prevent this situation.

---

# 2. Coherency Protocols

Hardware uses **cache coherency protocols** to keep caches synchronized.

The most widely used protocol family is **MESI**.

MESI stands for:

| State | Meaning |
|------|--------|
| Modified | Cache line modified and different from RAM |
| Exclusive | Cache line only exists in one cache |
| Shared | Cache line may exist in multiple caches |
| Invalid | Cache line is not valid |

These states allow the CPU to track **who owns the most recent copy of a cache line**.

---

# 3. Example: Write Operation

Suppose two cores share a cache line containing variable `X`.

Initial state:

```

Core1: Shared
Core2: Shared

```

Core1 writes to `X`.

The protocol performs two actions:

1. Core1 changes its state to **Modified**
2. Core2's copy becomes **Invalid**

Result:

```

Core1: Modified
Core2: Invalid

```

Core2 must reload the value before using it again.

---

# 4. Cache Coherency Traffic

Maintaining coherency requires communication between cores.

This happens through the CPU's internal interconnect.

Typical events include:

- **invalidate messages**
- **cache line transfers**
- **ownership changes**

Frequent updates to shared data can generate large amounts of coherency traffic.

This can significantly impact performance in multi-threaded programs.

---

# 5. False Sharing

A particularly important performance problem is **false sharing**.

Caches operate on **cache lines**, typically **64 bytes**.

If two threads modify different variables located in the same cache line:

```

Thread 1 → modifies variable A
Thread 2 → modifies variable B

```

Even though the variables are unrelated, the cache line must bounce between cores.

This creates unnecessary coherency traffic.

Example layout:

```

## Cache Line

A | B | C | D | ... (64 bytes)

```

If A and B are modified by different threads, the line constantly moves between cores.

This phenomenon is called **false sharing**.

---

# 6. Why This Matters for Python

Python programs also run on multi-core CPUs, so cache coherency still exists.

However, Python's **Global Interpreter Lock (GIL)** prevents multiple threads from executing Python bytecode simultaneously in a single process.

This means:

- Python threads rarely suffer from heavy coherency traffic.
- CPU-intensive Python workloads often use **multiprocessing instead of threading**.

In lower-level languages (C, C++, Rust), cache coherency and false sharing are major performance concerns.

---

# Summary

| Concept | Description |
|-------|-------------|
| Cache coherency | Ensuring all CPU cores see consistent memory |
| MESI protocol | Common hardware protocol managing cache states |
| Invalidation | Removing stale cache copies |
| Coherency traffic | Communication between cores to synchronize caches |
| False sharing | Performance problem when unrelated variables share a cache line |

Cache coherency is a fundamental mechanism that allows modern multi-core processors to behave like a **single shared-memory system**.
