# async and await

## The async Keyword

The `async` keyword defines a **coroutine function**. Calling it returns a coroutine object, not the result.

```python
async def greet(name):
    return f"Hello, {name}"

# Calling returns a coroutine object
coro = greet("Alice")
print(coro)  # <coroutine object greet at 0x...>

# Must run it to get the result
import asyncio
result = asyncio.run(greet("Alice"))
print(result)  # "Hello, Alice"
```

---

## The await Keyword

`await` suspends the coroutine until the awaited operation completes. It can only be used inside `async` functions.

```python
async def fetch_data():
    print("Starting fetch...")
    await asyncio.sleep(1)  # Suspend here, let other tasks run
    print("Fetch complete!")
    return {"data": 42}

async def main():
    result = await fetch_data()  # Wait for fetch_data to complete
    print(result)

asyncio.run(main())
```

Output:
```
Starting fetch...
Fetch complete!
{'data': 42}
```

---

## What Can Be Awaited?

Only **awaitable** objects can be used with `await`:

### 1. Coroutines

```python
async def my_coroutine():
    return "result"

async def main():
    result = await my_coroutine()  # ✅ Coroutine is awaitable
```

### 2. Tasks

```python
async def main():
    task = asyncio.create_task(my_coroutine())
    result = await task  # ✅ Task is awaitable
```

### 3. Futures

```python
async def main():
    future = asyncio.Future()
    # ... something sets future.set_result(value)
    result = await future  # ✅ Future is awaitable
```

### 4. Objects with `__await__`

```python
class MyAwaitable:
    def __await__(self):
        yield
        return "custom result"

async def main():
    result = await MyAwaitable()  # ✅ Has __await__
```

---

## Sequential vs Concurrent Execution

### Sequential (Slow)

```python
async def fetch(url):
    await asyncio.sleep(1)  # Simulate network delay
    return f"Data from {url}"

async def main():
    # Each await blocks until complete
    result1 = await fetch("url1")  # 1 second
    result2 = await fetch("url2")  # 1 second
    result3 = await fetch("url3")  # 1 second
    # Total: 3 seconds

asyncio.run(main())
```

### Concurrent (Fast)

```python
async def main():
    # Create tasks - starts all immediately
    task1 = asyncio.create_task(fetch("url1"))
    task2 = asyncio.create_task(fetch("url2"))
    task3 = asyncio.create_task(fetch("url3"))
    
    # Await results
    result1 = await task1
    result2 = await task2
    result3 = await task3
    # Total: ~1 second (parallel execution)

asyncio.run(main())
```

### Using gather (Preferred)

```python
async def main():
    results = await asyncio.gather(
        fetch("url1"),
        fetch("url2"),
        fetch("url3")
    )
    # results = ["Data from url1", "Data from url2", "Data from url3"]
    # Total: ~1 second

asyncio.run(main())
```

---

## Common Mistakes

### 1. Forgetting await

```python
async def main():
    result = fetch_data()  # ❌ Missing await - returns coroutine object
    print(result)  # <coroutine object fetch_data at 0x...>

async def main():
    result = await fetch_data()  # ✅ Correct
    print(result)  # Actual result
```

**Warning**: Python shows `RuntimeWarning: coroutine was never awaited`

### 2. Using await Outside async Function

```python
def main():
    result = await fetch_data()  # ❌ SyntaxError

async def main():
    result = await fetch_data()  # ✅ Must be inside async function
```

### 3. Blocking the Event Loop

```python
import time

async def bad_example():
    time.sleep(1)  # ❌ Blocks the entire event loop!
    return "done"

async def good_example():
    await asyncio.sleep(1)  # ✅ Yields control to event loop
    return "done"
```

### 4. Not Running Coroutines

```python
async def my_task():
    print("Running")

# ❌ Does nothing - coroutine created but never run
my_task()

# ✅ Actually runs the coroutine
asyncio.run(my_task())
```

---

## Async Context Managers

Use `async with` for async setup/cleanup:

```python
class AsyncConnection:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(0.1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Disconnecting...")
        await asyncio.sleep(0.1)

async def main():
    async with AsyncConnection() as conn:
        print("Using connection")

asyncio.run(main())
```

Output:
```
Connecting...
Using connection
Disconnecting...
```

### Real-World Example

```python
import aiohttp

async def fetch(url):
    async with aiohttp.ClientSession() as session:  # Async context manager
        async with session.get(url) as response:    # Another one
            return await response.text()
```

---

## Async Iterators

Use `async for` to iterate over async iterables:

```python
class AsyncCounter:
    def __init__(self, stop):
        self.stop = stop
    
    def __aiter__(self):
        self.current = 0
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.current += 1
        return self.current

async def main():
    async for num in AsyncCounter(5):
        print(num)

asyncio.run(main())
```

### Async Generator (Simpler)

```python
async def async_counter(stop):
    for i in range(stop):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in async_counter(5):
        print(num)
```

---

## Async Comprehensions

```python
# Async list comprehension
async def main():
    results = [await fetch(url) async for url in async_url_generator()]

# Async generator expression
async def main():
    gen = (await fetch(url) async for url in async_url_generator())
```

---

## Summary

| Syntax | Purpose |
|--------|---------|
| `async def` | Define a coroutine function |
| `await` | Suspend until awaitable completes |
| `async with` | Async context manager |
| `async for` | Iterate over async iterable |
| `asyncio.run()` | Entry point to run async code |

**Key Rules**:

1. `await` can only be used inside `async` functions
2. Only awaitables can be awaited (coroutines, tasks, futures)
3. Don't use blocking calls (`time.sleep`, `requests.get`) in async code
4. Use `asyncio.gather()` for concurrent execution
5. Always `await` your coroutines or they won't run
