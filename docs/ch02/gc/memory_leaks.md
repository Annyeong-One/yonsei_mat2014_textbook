# Memory Leaks

## Common Causes

### 1. Global References

```python
# Bad: accumulates
cache = []

def process(data):
    cache.append(data)  # Never cleared!

# Better: limit size
from collections import deque

cache = deque(maxlen=100)
```

### 2. Circular References

```python
# Leak
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
# Cycle keeps both alive
```

### 3. Closures

```python
# Leak: large object captured
def process_data():
    large = [0] * 1000000
    
    def get_first():
        return large[0]  # Captures all
    
    return get_first  # Keeps large alive
```

## Detection

### 1. Memory Growth

```python
import tracemalloc

tracemalloc.start()

# Run code
for i in range(100):
    process()
    
    if i % 10 == 0:
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current: {current / 10**6:.1f} MB")
```

### 2. Object Count

```python
import gc

before = len(gc.get_objects())

# Run code
process()

after = len(gc.get_objects())
print(f"Objects created: {after - before}")
```

## Prevention

### 1. Limit Caches

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive(x):
    return x ** 2
```

### 2. Break Cycles

```python
# Explicitly clear
obj.parent = None
obj.children.clear()
```

### 3. Weak References

```python
import weakref

cache = weakref.WeakValueDictionary()
```

### 4. Context Managers

```python
with open_resource() as r:
    use(r)
# Guaranteed cleanup
```

## Summary

- Watch globals
- Break cycles
- Limit closures
- Use weak refs
- Profile memory
