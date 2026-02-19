# Chapter 14: Concurrency

This chapter covers concurrent and parallel programming in Python, including the GIL, threading, multiprocessing, asyncio, and the concurrent.futures high-level interface.

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
