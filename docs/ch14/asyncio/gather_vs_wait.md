# asyncio.gather() vs asyncio.wait()

Both functions run multiple coroutines concurrently, but with different behaviors and use cases.

## Quick Comparison

| Feature | `gather()` | `wait()` |
|---------|------------|----------|
| Input | Coroutines or tasks | Tasks only (must wrap coroutines) |
| Returns | List of results | Two sets: (done, pending) |
| Result order | Same as input order | Completion order |
| Exception handling | Configurable | Manual checking |
| Partial completion | No | Yes (FIRST_COMPLETED, timeout) |
| Cancellation | Group cancellation | Individual task control |

## asyncio.gather()

### Basic Usage

```python
import asyncio

async def fetch(url, delay):
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    # Pass coroutines directly
    results = await asyncio.gather(
        fetch("url1", 2),
        fetch("url2", 1),
        fetch("url3", 3)
    )
    
    # Results in input order (not completion order)
    print(results)
    # ['Data from url1', 'Data from url2', 'Data from url3']

asyncio.run(main())
```

### Exception Handling

```python
async def might_fail(n):
    if n == 2:
        raise ValueError(f"Error on {n}")
    return n * 10

async def main():
    # Default: First exception propagates, others cancelled
    try:
        results = await asyncio.gather(
            might_fail(1),
            might_fail(2),  # Raises
            might_fail(3)
        )
    except ValueError as e:
        print(f"Caught: {e}")
    
    # With return_exceptions=True: Exceptions returned in results
    results = await asyncio.gather(
        might_fail(1),
        might_fail(2),
        might_fail(3),
        return_exceptions=True
    )
    print(results)
    # [10, ValueError('Error on 2'), 30]
    
    # Check for exceptions
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")

asyncio.run(main())
```

### When to Use gather()

- You need **all results** in input order
- Simple concurrent execution
- Want to cancel all if one fails (default behavior)
- Want exceptions as values (`return_exceptions=True`)

## asyncio.wait()

### Basic Usage

```python
import asyncio

async def fetch(url, delay):
    await asyncio.sleep(delay)
    return f"Data from {url}"

async def main():
    # Must pass tasks (not coroutines)
    tasks = [
        asyncio.create_task(fetch("url1", 2)),
        asyncio.create_task(fetch("url2", 1)),
        asyncio.create_task(fetch("url3", 3))
    ]
    
    # Returns two sets
    done, pending = await asyncio.wait(tasks)
    
    # Process completed tasks
    for task in done:
        result = task.result()
        print(result)

asyncio.run(main())
```

### Return When Options

```python
async def main():
    tasks = [
        asyncio.create_task(fetch("url1", 2)),
        asyncio.create_task(fetch("url2", 1)),
        asyncio.create_task(fetch("url3", 3))
    ]
    
    # FIRST_COMPLETED: Return when any task completes
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    print(f"First done: {len(done)}, pending: {len(pending)}")
    
    # Continue with remaining
    done, pending = await asyncio.wait(pending)
```

```python
async def main():
    tasks = [
        asyncio.create_task(might_fail(1)),
        asyncio.create_task(might_fail(2)),  # Raises
        asyncio.create_task(might_fail(3))
    ]
    
    # FIRST_EXCEPTION: Return when first exception or all done
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_EXCEPTION
    )
    
    # Check which failed
    for task in done:
        if task.exception():
            print(f"Failed: {task.exception()}")
        else:
            print(f"Succeeded: {task.result()}")
    
    # Cancel remaining
    for task in pending:
        task.cancel()
```

### Timeout

```python
async def main():
    tasks = [
        asyncio.create_task(fetch("fast", 1)),
        asyncio.create_task(fetch("slow", 10))
    ]
    
    # Wait at most 2 seconds
    done, pending = await asyncio.wait(tasks, timeout=2.0)
    
    print(f"Completed: {len(done)}")
    print(f"Still pending: {len(pending)}")
    
    # Handle pending tasks
    for task in pending:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

asyncio.run(main())
```

### Exception Handling with wait()

```python
async def main():
    tasks = [
        asyncio.create_task(might_fail(1)),
        asyncio.create_task(might_fail(2)),
        asyncio.create_task(might_fail(3))
    ]
    
    done, pending = await asyncio.wait(tasks)
    
    results = []
    errors = []
    
    for task in done:
        try:
            results.append(task.result())
        except Exception as e:
            errors.append(e)
    
    print(f"Results: {results}")
    print(f"Errors: {errors}")
```

### When to Use wait()

- Need **partial results** (FIRST_COMPLETED)
- Want to **handle timeouts** with pending task control
- Need to **detect first exception** without cancelling others
- Want **fine-grained control** over individual tasks
- Need to **process results as they complete**

## Side-by-Side Examples

### Example 1: Fetch All URLs

```python
# Using gather() - simpler
async def fetch_all_gather(urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[
            fetch_url(session, url) for url in urls
        ])
    return results  # In input order

# Using wait() - more verbose
async def fetch_all_wait(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(fetch_url(session, url))
            for url in urls
        ]
        done, _ = await asyncio.wait(tasks)
        
    return [task.result() for task in done]  # Completion order
```

### Example 2: First Response Wins

```python
# wait() is better here
async def first_response(urls):
    tasks = [
        asyncio.create_task(fetch_url(url), name=url)
        for url in urls
    ]
    
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    
    # Cancel others
    for task in pending:
        task.cancel()
    
    # Get first result
    first_task = done.pop()
    return first_task.result()
```

### Example 3: Timeout with Partial Results

```python
# wait() with timeout
async def fetch_with_deadline(urls, timeout=5.0):
    tasks = [
        asyncio.create_task(fetch_url(url))
        for url in urls
    ]
    
    done, pending = await asyncio.wait(tasks, timeout=timeout)
    
    # Collect completed results
    results = []
    for task in done:
        try:
            results.append(task.result())
        except Exception:
            pass
    
    # Cancel slow tasks
    for task in pending:
        task.cancel()
    
    return results

# gather() can't do partial results with timeout
```

### Example 4: Aggregate Errors

```python
# gather() with return_exceptions
async def fetch_collecting_errors_gather(urls):
    results = await asyncio.gather(
        *[fetch_url(url) for url in urls],
        return_exceptions=True
    )
    
    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]
    
    return successes, failures

# wait() equivalent
async def fetch_collecting_errors_wait(urls):
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    done, _ = await asyncio.wait(tasks)
    
    successes = []
    failures = []
    
    for task in done:
        try:
            successes.append(task.result())
        except Exception as e:
            failures.append(e)
    
    return successes, failures
```

## asyncio.as_completed()

For processing results in completion order:

```python
async def process_as_completed(urls):
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    
    for coro in asyncio.as_completed(tasks):
        try:
            result = await coro
            print(f"Got: {result}")
            # Process immediately, don't wait for all
        except Exception as e:
            print(f"Error: {e}")
```

## Decision Guide

```
Need results in input order?
├─ Yes → gather()
└─ No
   ├─ Need timeout with partial results? → wait(timeout=...)
   ├─ Need first completed? → wait(return_when=FIRST_COMPLETED)
   ├─ Need to detect first exception? → wait(return_when=FIRST_EXCEPTION)
   └─ Process as completed? → as_completed()
```

## Key Takeaways

- **gather()**: Simple, ordered results, group error handling
- **wait()**: Flexible, partial completion, timeout support
- **as_completed()**: Process results in completion order
- gather() takes coroutines directly; wait() requires tasks
- gather() returns results list; wait() returns (done, pending) sets
- Use gather() for most cases; use wait() when you need control

---

## Runnable Example: `gather_vs_wait_tutorial.py`

```python
"""
Intermediate Tutorial 4: gather() vs wait()

Compares asyncio.gather() and asyncio.wait() for different use cases.
"""

import asyncio

# =============================================================================
# Definitions
# =============================================================================

async def demonstrate_gather_vs_wait():
    print("\n--- gather() vs wait() ---")
    print("""
    gather():
    • Returns results in order
    • Simple API
    • Best for: Getting all results
    
    wait():
    • Returns (done, pending) sets
    • More control
    • Best for: Processing as completed, timeouts
    
    Example - gather():
    results = await asyncio.gather(task1(), task2(), task3())
    
    Example - wait():
    done, pending = await asyncio.wait([task1(), task2()])
    for task in done:
        result = await task
    
    Use gather() for most cases!
    """)

async def main():
    await demonstrate_gather_vs_wait()

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    asyncio.run(main())
```
