# Chapter 14: Concurrency

Most Python programs run one task at a time — when one operation waits for a network response or a disk read, the entire program stalls. Concurrency lets a program overlap waiting periods or distribute computation across multiple CPU cores. This chapter introduces Python's concurrency toolkit: threads for IO-bound parallelism, processes for CPU-bound work, and `asyncio` for high-throughput asynchronous IO. By the end, you will know which tool to reach for in each situation and how to avoid common pitfalls like deadlocks and race conditions.

The sections build on each other — start with Concurrency Concepts (14.1) for the foundational vocabulary, then explore each execution model in order.

## 14.1 Concurrency Concepts

- [Introduction](concepts/introduction.md)
- [GIL Explained](concepts/gil.md)
- [CPU-bound vs IO-bound](concepts/cpu_vs_io.md)
- [Threads vs Processes](concepts/threads_vs_processes.md)
- [Deadlocks](concepts/deadlocks.md)
- [Race Conditions](concepts/race_conditions.md)

## 14.2 concurrent.futures

- [Executor Interface](futures/executor_interface.md)
- [ThreadPoolExecutor](futures/thread_pool.md)
- [ProcessPoolExecutor](futures/process_pool.md)
- [Future Objects](futures/future_objects.md)

## 14.3 Threading

- [Thread Basics](threading/thread_basics.md)
- [Thread Synchronization](threading/synchronization.md)
- [Thread Communication](threading/communication.md)
- [Thread-Local Storage](threading/thread_local.md)

## 14.4 Multiprocessing

- [Process Basics](multiprocessing/process_basics.md)
- [Process Pool](multiprocessing/pool.md)
- [Sharing State](multiprocessing/sharing_state.md)

## 14.5 Asyncio

- [Asyncio Introduction](asyncio/introduction.md)
- [async and await](asyncio/async_await.md)
- [Event Loop](asyncio/event_loop.md)
- [Tasks and Coroutines](asyncio/tasks_coroutines.md)
- [gather vs wait](asyncio/gather_vs_wait.md)
- [Async Iteration (async for/with)](asyncio/async_iteration.md)
- [Asyncio Patterns](asyncio/patterns.md)
- [Async HTTP (aiohttp)](asyncio/aiohttp_examples.md)
- [Context Variables](asyncio/contextvars.md)

## 14.6 Practical Patterns

- [When to Use What](patterns/decision_guide.md)
- [Common Patterns](patterns/common_patterns.md)
- [Error Handling](patterns/error_handling.md)
