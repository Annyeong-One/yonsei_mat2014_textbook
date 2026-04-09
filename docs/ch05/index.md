# Chapter 4: Memory and Performance

Understanding how Python manages memory and how to measure performance is essential for writing efficient programs. This chapter examines Python's memory architecture, reference counting, garbage collection, and profiling tools.

## 4.1 Memory Architecture

- [Stack vs Heap Overview](memory/stack_heap_overview.md)
- [Frame Objects](memory/frame_objects.md)
- [Heap Object Storage](memory/heap_storage.md)
- [Stack-Heap Interaction](memory/stack_heap_interaction.md)
- [Recursion and Stack Growth](memory/recursion_stack.md)
- [Object Identity Stability](memory/identity_stability.md)
- [Buffer Reallocation](memory/buffer_reallocation.md)
- [Stack Overflow](memory/stack_overflow.md)
- [Python vs C Memory](memory/python_vs_c_memory.md)

## 4.2 Reference Counting and GC

- [Memory Management Overview](gc/memory_management_overview.md)
- [Reference Counting](gc/reference_counting.md)
- [Garbage Collection](gc/garbage_collection.md)
- [Memory Leaks](gc/memory_leaks.md)

## 4.3 Weak References

- [Weak Reference Basics](gc/weak_references.md)
- [Weak Reference Patterns](gc/weak_ref_patterns.md)

## 4.4 Advanced Memory Topics

- [Caching Strategies](advanced_memory/caching_strategies.md)
- [Memory Management](advanced_memory/memory_management.md)
- [Memory Optimization](advanced_memory/memory_optimization.md)
- [\_\_slots\_\_](advanced_memory/slots.md)
- [sys.getsizeof()](advanced_memory/getsizeof.md)
- [tracemalloc](advanced_memory/tracemalloc.md)

## 4.5 Performance and Profiling

- [Performance and Memory](practical/performance_memory.md)
- [cProfile Module](practical/cprofile.md)
- [line_profiler](practical/line_profiler.md)
- [memory_profiler](practical/memory_profiler.md)
- [Benchmarking Methodology](practical/benchmarking.md)
- [Optimization Strategies](practical/optimization_strategies.md)
- [Profiling Visualization (snakeviz)](practical/profiling_visualization.md)
