# Asyncio Introduction

## What is Asyncio?

**asyncio** is Python's built-in library for writing concurrent code using the **async/await** syntax. It provides a framework for managing asynchronous I/O operations, enabling thousands of concurrent connections with a single thread.

```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
```

---

## Concurrency Models Comparison

| Model | Library | Best For | Parallelism |
|-------|---------|----------|-------------|
| Threading | `threading` | I/O-bound (simple) | Limited by GIL |
| Multiprocessing | `multiprocessing` | CPU-bound | True parallelism |
| **Asyncio** | `asyncio` | I/O-bound (many connections) | Single-threaded concurrency |

---

## When to Use Asyncio

### ✅ Good Use Cases

```python
# Network requests (HTTP clients)
async def fetch_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Web servers (FastAPI, aiohttp)
# Database queries (asyncpg, motor)
# WebSocket connections
# File I/O (aiofiles)
```

**Asyncio excels when**:
- Many concurrent I/O operations
- High number of connections (1000s)
- Network-bound applications
- Real-time applications (chat, streaming)

### ❌ Poor Use Cases

```python
# CPU-bound work - use multiprocessing instead
def compute_heavy():
    return sum(i * i for i in range(10_000_000))

# Simple scripts with few I/O operations
# Code that needs true parallelism
```

---

## Asyncio vs Threading

### Threading Approach

```python
import threading
import time

def fetch(url):
    time.sleep(1)  # Simulate I/O
    return f"Result from {url}"

# 10 threads for 10 URLs
threads = []
for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

**Problems**:
- Thread overhead (memory, context switching)
- Limited scalability (100s of threads, not 1000s)
- Race conditions with shared state

### Asyncio Approach

```python
import asyncio

async def fetch(url):
    await asyncio.sleep(1)  # Simulate I/O
    return f"Result from {url}"

async def main():
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

asyncio.run(main())
```

**Benefits**:
- Single thread, no race conditions
- Minimal overhead per task
- Scales to 10,000s of concurrent operations
- Explicit yield points (`await`)

---

## Key Concepts Overview

### 1. Coroutines

Functions defined with `async def`:

```python
async def my_coroutine():
    return "Hello"

# Calling returns a coroutine object, not the result
coro = my_coroutine()  # <coroutine object>

# Must be awaited or run
result = asyncio.run(my_coroutine())  # "Hello"
```

### 2. await Keyword

Suspends coroutine until the awaited operation completes:

```python
async def fetch_data():
    result = await some_async_operation()  # Pause here
    return result                           # Resume when done
```

### 3. Event Loop

The central scheduler that runs coroutines:

```python
# Modern way (Python 3.7+)
asyncio.run(main())

# Manual control (rarely needed)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### 4. Tasks

Wrap coroutines for concurrent execution:

```python
async def main():
    # Create tasks for concurrent execution
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    
    # Both run concurrently
    result1 = await task1
    result2 = await task2
```

---

## Minimal Working Example

```python
import asyncio

async def say_after(delay, message):
    """Coroutine that waits then prints."""
    await asyncio.sleep(delay)
    print(message)

async def main():
    print(f"Started at {asyncio.get_event_loop().time():.2f}")
    
    # Sequential (3 seconds total)
    # await say_after(1, "Hello")
    # await say_after(2, "World")
    
    # Concurrent (2 seconds total)
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )
    
    print(f"Finished at {asyncio.get_event_loop().time():.2f}")

asyncio.run(main())
```

Output:
```
Started at 0.00
Hello
World
Finished at 2.00
```

---

## Common Async Libraries

| Category | Library | Description |
|----------|---------|-------------|
| HTTP Client | `aiohttp`, `httpx` | Async HTTP requests |
| Web Framework | `FastAPI`, `Starlette` | Async web servers |
| Database | `asyncpg`, `motor`, `aiosqlite` | Async database drivers |
| File I/O | `aiofiles` | Async file operations |
| Redis | `aioredis` | Async Redis client |

---

## Summary

| Concept | Description |
|---------|-------------|
| `asyncio` | Python's async I/O framework |
| `async def` | Defines a coroutine |
| `await` | Suspends until operation completes |
| Event loop | Scheduler that runs coroutines |
| Best for | High-concurrency I/O-bound tasks |

**Key Takeaways**:

- Asyncio provides single-threaded concurrency
- Use for I/O-bound tasks with many concurrent operations
- `async`/`await` makes async code readable
- Not a replacement for multiprocessing (CPU-bound work)
- Modern Python async ecosystem is mature and widely adopted
