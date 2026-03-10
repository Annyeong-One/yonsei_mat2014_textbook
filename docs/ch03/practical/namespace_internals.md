# Namespace Internals


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding Python's namespace system and the Global Interpreter Lock.

## Namespace Access

### `globals()` Function

Access and modify the global namespace:

```python
# View global namespace
print(globals().keys())

# Add to global namespace
globals()['dynamic_var'] = 42
print(dynamic_var)  # 42

# Dynamic variable creation
name = 'my_variable'
globals()[name] = 100
print(my_variable)  # 100
```

### `locals()` Function

View the local namespace (read-only in functions):

```python
def function():
    x = 10
    y = 20
    
    # View locals
    print(locals())  # {'x': 10, 'y': 20}
    
    # CANNOT modify locals this way
    locals()['z'] = 30
    # z is NOT defined

# At module level, locals() == globals()
print(locals() is globals())  # True (at module level)
```

### `vars()` Function

Access object's `__dict__`:

```python
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = MyClass()
print(vars(obj))  # {'x': 10, 'y': 20}

# Modify via vars
vars(obj)['z'] = 30
print(obj.z)  # 30
```

---

## Namespace Manipulation

### Dynamic Attribute Access

```python
# setattr/getattr
class Config:
    pass

config = Config()
setattr(config, 'debug', True)
print(getattr(config, 'debug'))  # True
print(getattr(config, 'verbose', False))  # False (default)

# Check existence
print(hasattr(config, 'debug'))  # True
```

### Dynamic Module Imports

```python
import importlib

# Import module by name
module_name = 'json'
module = importlib.import_module(module_name)

# Import from package
submodule = importlib.import_module('os.path')
```

### Exec and Eval

```python
# Execute code string
code = """
x = 10
y = 20
result = x + y
"""
namespace = {}
exec(code, namespace)
print(namespace['result'])  # 30

# Evaluate expression
result = eval('2 + 3 * 4')
print(result)  # 14

# With custom namespace
namespace = {'x': 10, 'y': 20}
result = eval('x + y', namespace)
print(result)  # 30
```

**Warning**: `exec` and `eval` are security risks with untrusted input.

---

## Global Interpreter Lock (GIL)

### What is the GIL?

The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time.

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Even with threads, they don't run truly parallel
threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# Result may not be 2000000 due to race conditions
# (counter += 1 is not atomic at bytecode level)
```

### Thread Safety

Most Python operations are thread-safe due to the GIL:

```python
# These are atomic (thread-safe)
x = 42                    # Simple assignment
y = x                     # Simple read
lst.append(item)          # Some built-in operations

# These are NOT atomic
counter += 1              # Read-modify-write
lst[0] = lst[1] + 1       # Multiple operations
```

### Working Around the GIL

**For CPU-bound tasks, use multiprocessing:**

```python
from multiprocessing import Pool

def cpu_intensive(n):
    return sum(i * i for i in range(n))

# Uses multiple processes (bypasses GIL)
with Pool(4) as pool:
    results = pool.map(cpu_intensive, [1000000] * 4)
```

**For I/O-bound tasks, threading works well:**

```python
import threading
import requests

def fetch_url(url):
    return requests.get(url).text

# GIL released during I/O operations
urls = ['http://example.com'] * 10
threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
```

**For async I/O:**

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

---

## Memory and Namespace Interaction

### Reference Counting

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Reference count (includes temp ref from getrefcount)

y = x  # Another reference
print(sys.getrefcount(x))  # Count increased

del y  # Remove reference
print(sys.getrefcount(x))  # Count decreased
```

### Garbage Collection

```python
import gc

# Force garbage collection
gc.collect()

# Check for circular references
gc.set_debug(gc.DEBUG_LEAK)

# Disable GC temporarily (for performance)
gc.disable()
# ... performance critical code ...
gc.enable()
```

---

## Summary

| Function | Purpose | Modifiable |
|----------|---------|------------|
| `globals()` | Global namespace | Yes |
| `locals()` | Local namespace | No (in functions) |
| `vars(obj)` | Object's `__dict__` | Yes |
| `dir(obj)` | List attributes | N/A |

GIL implications:
- Only one thread executes Python bytecode at a time
- I/O-bound: Use threading (GIL released during I/O)
- CPU-bound: Use multiprocessing (separate processes)
- Most simple operations are thread-safe
- Compound operations need explicit locking

Key points:
- Use `globals()` for dynamic global variables
- `locals()` is read-only in functions
- GIL affects CPU-bound parallelism
- Use multiprocessing for CPU-bound tasks
- Use threading/asyncio for I/O-bound tasks
