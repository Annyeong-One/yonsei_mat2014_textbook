# Architecture Review

This page summarizes the key concepts from the computer architecture section and provides a quick reference for Python programmers.

!!! warning "Incomplete page"
    This page is a landing/review page and does not follow the five-section structure. It serves as a summary reference for the architecture chapter.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **CPU** | Latency-optimized processor with few complex cores |
| **GPU** | Throughput-optimized processor with thousands of simple cores |
| **Core** | Independent hardware execution unit with private caches |
| **Clock speed** | Cycles per second (GHz); only part of the performance picture |
| **IPC** | Instructions per cycle; combined with clock speed determines throughput |
| **Pipeline** | Overlapping instruction stages for higher throughput |
| **Cache hierarchy** | L1/L2/L3 with increasing latency; locality determines performance |
| **SMT** | Simultaneous multithreading; one physical core presents two logical cores |

## Python Implications

- Python adds interpreter overhead (type checks, dictionary lookups, object allocation) on every operation
- NumPy bypasses this overhead by delegating to compiled C code with SIMD instructions
- The GIL prevents CPU-bound thread parallelism; use `multiprocessing` for CPU-bound tasks
- Memory access patterns matter: sequential access exploits cache locality
