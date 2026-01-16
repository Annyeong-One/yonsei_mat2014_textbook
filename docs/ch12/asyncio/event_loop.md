# Event Loop

## What is the Event Loop?

The **event loop** is the core of asyncio. It:
- Schedules and runs coroutines
- Handles I/O events
- Manages callbacks and timers
- Coordinates all async operations

Think of it as a central dispatcher that decides which coroutine runs next.

```
┌─────────────────────────────────────────┐
│              Event Loop                 │
│  ┌─────────────────────────────────┐    │
│  │  Ready Queue: [task1, task2]    │    │
│  └─────────────────────────────────┘    │
│  ┌─────────────────────────────────┐    │
│  │  Waiting: {task3: I/O, task4}   │    │
│  └─────────────────────────────────┘    │
│                                         │
│  Loop: Pick ready task → Run until      │
│        await → Check I/O → Repeat       │
└─────────────────────────────────────────┘
```

---

## Running the Event Loop

### Modern Way: `asyncio.run()` (Python 3.7+)

```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Recommended approach
asyncio.run(main())
```

`asyncio.run()`:
- Creates a new event loop
- Runs the coroutine until complete
- Closes the loop when done
- Handles cleanup automatically

### Manual Control (Rarely Needed)

```python
async def main():
    return "result"

# Get or create event loop
loop = asyncio.get_event_loop()

# Run until coroutine completes
result = loop.run_until_complete(main())

# Clean up
loop.close()
```

### Running Forever (Servers)

```python
async def server():
    while True:
        await handle_connection()

loop = asyncio.get_event_loop()
loop.run_forever()  # Runs until loop.stop() is called
```

---

## Event Loop Lifecycle

```python
import asyncio

async def task(name, delay):
    print(f"{name}: starting")
    await asyncio.sleep(delay)
    print(f"{name}: done")
    return name

async def main():
    # Event loop is running here
    print("Main: creating tasks")
    
    t1 = asyncio.create_task(task("A", 2))
    t2 = asyncio.create_task(task("B", 1))
    
    print("Main: waiting for tasks")
    await t1
    await t2
    print("Main: all done")

# Event loop: created → running → closed
asyncio.run(main())
```

Output:
```
Main: creating tasks
Main: waiting for tasks
A: starting
B: starting
B: done
A: done
Main: all done
```

---

## Getting the Current Loop

### Inside Async Code

```python
async def my_coroutine():
    loop = asyncio.get_running_loop()  # ✅ Use this inside async
    print(f"Running on loop: {loop}")
```

### Outside Async Code

```python
def setup():
    loop = asyncio.get_event_loop()  # Gets or creates loop
    # Schedule work...
```

### Difference

| Function | Context | Behavior |
|----------|---------|----------|
| `get_running_loop()` | Inside async | Returns current loop or raises |
| `get_event_loop()` | Anywhere | Gets/creates loop (deprecated pattern) |

---

## Scheduling Callbacks

### Call Soon (Next Iteration)

```python
def callback(message):
    print(f"Callback: {message}")

async def main():
    loop = asyncio.get_running_loop()
    
    loop.call_soon(callback, "Hello")
    print("Scheduled callback")
    
    await asyncio.sleep(0)  # Let loop process callbacks
    print("After sleep")

asyncio.run(main())
```

Output:
```
Scheduled callback
Callback: Hello
After sleep
```

### Call Later (Delayed)

```python
async def main():
    loop = asyncio.get_running_loop()
    
    # Call after 1 second
    loop.call_later(1.0, callback, "Delayed")
    
    print("Waiting...")
    await asyncio.sleep(2)

asyncio.run(main())
```

### Call At (Specific Time)

```python
async def main():
    loop = asyncio.get_running_loop()
    
    # Call at loop time + 1 second
    when = loop.time() + 1.0
    loop.call_at(when, callback, "At specific time")
    
    await asyncio.sleep(2)
```

---

## Running Blocking Code

### Problem: Blocking Calls

```python
import time

async def bad():
    time.sleep(5)  # ❌ Blocks entire event loop!
    return "done"
```

### Solution: run_in_executor

```python
import asyncio
import time

def blocking_io():
    """Blocking function (e.g., file I/O, legacy code)"""
    time.sleep(1)
    return "Blocking operation complete"

async def main():
    loop = asyncio.get_running_loop()
    
    # Run in default thread pool executor
    result = await loop.run_in_executor(None, blocking_io)
    print(result)

asyncio.run(main())
```

### Custom Executor

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

async def main():
    loop = asyncio.get_running_loop()
    
    # Thread pool for I/O-bound blocking code
    with ThreadPoolExecutor(max_workers=4) as pool:
        result = await loop.run_in_executor(pool, blocking_io)
    
    # Process pool for CPU-bound code
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_heavy_task)
```

---

## Event Loop Methods

### Time

```python
async def main():
    loop = asyncio.get_running_loop()
    
    # Current loop time (monotonic)
    now = loop.time()
    print(f"Loop time: {now}")
```

### Debug Mode

```python
# Enable debug mode
asyncio.run(main(), debug=True)

# Or via environment variable
# PYTHONASYNCIODEBUG=1 python script.py
```

Debug mode:
- Warns about unawaited coroutines
- Logs slow callbacks (>100ms)
- Enables additional checks

---

## Multiple Event Loops (Advanced)

### Different Threads, Different Loops

```python
import asyncio
import threading

def run_in_thread():
    # Create new loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    async def task():
        return "From thread"
    
    result = loop.run_until_complete(task())
    loop.close()
    return result

# Main thread has its own loop
thread = threading.Thread(target=run_in_thread)
thread.start()
thread.join()
```

### Nested Loops (Avoid!)

```python
async def outer():
    asyncio.run(inner())  # ❌ RuntimeError: cannot run nested

# Use create_task or gather instead
async def outer():
    await inner()  # ✅ Just await it
```

---

## Common Patterns

### Graceful Shutdown

```python
import signal

async def main():
    loop = asyncio.get_running_loop()
    
    # Handle shutdown signals
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown()))

async def shutdown():
    print("Shutting down...")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks, return_exceptions=True)
    asyncio.get_event_loop().stop()
```

### Event Loop in Class

```python
class AsyncService:
    def __init__(self):
        self._loop = None
    
    async def start(self):
        self._loop = asyncio.get_running_loop()
        # Initialize async resources
    
    async def stop(self):
        # Cleanup async resources
        pass
```

---

## Summary

| Function | Purpose |
|----------|---------|
| `asyncio.run(coro)` | Run coroutine (main entry point) |
| `asyncio.get_running_loop()` | Get loop inside async code |
| `asyncio.get_event_loop()` | Get/create loop (sync code) |
| `loop.run_until_complete()` | Run until coroutine finishes |
| `loop.run_forever()` | Run until `stop()` called |
| `loop.run_in_executor()` | Run blocking code in thread/process |
| `loop.call_soon()` | Schedule callback for next iteration |
| `loop.call_later()` | Schedule delayed callback |
| `loop.time()` | Get current loop time |

**Key Takeaways**:

- Use `asyncio.run()` for most applications
- One event loop per thread
- Don't block the event loop — use `run_in_executor`
- Debug mode helps find common mistakes
- The event loop handles all scheduling automatically
