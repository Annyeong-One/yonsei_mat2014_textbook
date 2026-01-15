# Memory Leaks

메모리 누수의 원인, 탐지, 예방 방법입니다.

## Common Causes

### 1. Global References

```python
# Bad: accumulates forever
cache = []

def process(data):
    cache.append(data)  # Never cleared!

# Better: limit size
from collections import deque

cache = deque(maxlen=100)
```

### 2. Circular References

```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
# Cycle keeps both alive
```

### 3. Closures Capturing Large Objects

```python
# Leak: large object captured
def process_data():
    large = [0] * 1000000
    
    def get_first():
        return large[0]  # Captures entire list
    
    return get_first  # Keeps large alive

# Better: capture only what's needed
def process_data():
    large = [0] * 1000000
    first = large[0]
    
    def get_first():
        return first  # Only captures the value
    
    return get_first
```

### 4. Event Handlers Not Removed

```python
# Leak: handler keeps object alive
class Widget:
    def __init__(self, event_system):
        event_system.subscribe('click', self.handle)
    
    def handle(self, event):
        pass
    # Widget never collected until unsubscribed
```

---

## Finalizers (`__del__`)

`__del__`은 신뢰할 수 없고 문제를 일으킬 수 있습니다.

### Problems with `__del__`

```python
class Resource:
    def __del__(self):
        self.cleanup()

# May not be called if:
# - Program exits abruptly
# - Circular references exist
# - Exceptions in __del__
```

### Object Resurrection

```python
saved = None

class Item:
    def __del__(self):
        global saved
        saved = self  # Resurrect!

obj = Item()
del obj
print(saved)  # Object still exists!
```

### Best Practices: Avoid `__del__`

```python
# Instead of __del__, use explicit cleanup
class Resource:
    def close(self):
        # Explicit cleanup
        pass

r = Resource()
try:
    use(r)
finally:
    r.close()
```

### Better: Context Managers

```python
class Resource:
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.cleanup()

# Guaranteed cleanup
with Resource() as r:
    use(r)
```

### Or: weakref Callbacks

```python
import weakref

def cleanup(ref):
    print("Object collected")

obj = SomeObject()
ref = weakref.ref(obj, cleanup)

# cleanup called on GC (more reliable than __del__)
```

---

## Detection

### 1. Track Memory Growth

```python
import tracemalloc

tracemalloc.start()

for i in range(100):
    process()
    
    if i % 10 == 0:
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current: {current / 10**6:.1f} MB")

tracemalloc.stop()
```

### 2. Monitor Object Count

```python
import gc

before = len(gc.get_objects())

process()

after = len(gc.get_objects())
print(f"Objects created: {after - before}")
```

### 3. Find Top Allocations

```python
import tracemalloc

tracemalloc.start()

# Run code
process()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("Top 10 allocations:")
for stat in top_stats[:10]:
    print(stat)
```

---

## GC Performance

### Collection Pauses

```python
import gc
import time

start = time.time()
collected = gc.collect()
pause = time.time() - start

print(f"Pause: {pause*1000:.2f}ms")
print(f"Collected: {collected}")
```

### Disable During Critical Sections

```python
import gc

gc.disable()
try:
    # Performance-critical code
    compute()
finally:
    gc.enable()
    gc.collect()
```

### Manual Collection Control

```python
import gc

gc.disable()

for i in range(1000):
    process()
    
    if i % 100 == 0:
        gc.collect()

gc.enable()
```

---

## GC Tuning

### Adjust Thresholds

```python
import gc

# Default: (700, 10, 10)
# Fewer collections, longer pauses:
gc.set_threshold(10000, 100, 100)

# More collections, shorter pauses:
gc.set_threshold(100, 5, 5)
```

### Reduce Allocations

```python
# Bad: many allocations
result = []
for i in range(1000):
    result.append([i])

# Better: pre-allocate
result = [None] * 1000
for i in range(1000):
    result[i] = i
```

### Monitor GC Impact

```python
import gc

# Before
before = gc.get_count()

process()

# After
after = gc.get_count()
print(f"Gen0 delta: {after[0] - before[0]}")
```

---

## Prevention Checklist

| Strategy | Implementation |
|----------|----------------|
| Limit caches | `functools.lru_cache(maxsize=128)` |
| Break cycles | `obj.parent = None` |
| Weak references | `weakref.WeakValueDictionary()` |
| Context managers | `with open_resource() as r:` |
| Explicit cleanup | `try/finally` with `.close()` |
| Avoid `__del__` | Use context managers instead |

---

## Summary

- **Causes**: globals, cycles, closures, event handlers
- **Detection**: `tracemalloc`, `gc.get_objects()`
- **Prevention**: limit caches, break cycles, use weak refs
- **Finalizers**: avoid `__del__`, use context managers
- **Performance**: tune thresholds, control collection timing
