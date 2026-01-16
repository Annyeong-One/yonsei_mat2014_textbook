# Caching Strategies

Effective caching can significantly improve performance by avoiding redundant computation and object creation.

## LRU Cache

The built-in `functools.lru_cache` provides a simple Least Recently Used cache:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_computation(x):
    print(f"Computing {x}...")
    return x ** 2

# First call computes
result = expensive_computation(10)  # Prints: Computing 10...

# Second call uses cache
result = expensive_computation(10)  # No print (cached)

# Check cache stats
print(expensive_computation.cache_info())
# CacheInfo(hits=1, misses=1, maxsize=128, currsize=1)
```

### Cache Configuration

```python
# Unlimited cache
@lru_cache(maxsize=None)
def unlimited_cache(x):
    return x ** 2

# Small cache
@lru_cache(maxsize=32)
def small_cache(x):
    return x ** 2

# Clear cache
expensive_computation.cache_clear()
```

### Typed Cache

```python
# typed=True: treat different types as different keys
@lru_cache(maxsize=128, typed=True)
def typed_cache(x):
    return x ** 2

typed_cache(10)    # Cached separately
typed_cache(10.0)  # Different cache entry
```

---

## Weak Value Cache

Automatically removes entries when values are garbage collected:

```python
import weakref

class ExpensiveObject:
    def __init__(self, data):
        self.data = data

cache = weakref.WeakValueDictionary()

def get_or_create(key):
    if key in cache:
        return cache[key]
    obj = ExpensiveObject(key)
    cache[key] = obj
    return obj

obj = get_or_create("key1")
# When obj is deleted, cache entry auto-removed
```

---

## Custom Cache Implementation

### Size-Limited Cache

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, maxsize=128):
        self.maxsize = maxsize
        self.cache = OrderedDict()
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.maxsize:
            # Remove oldest (least recently used)
            self.cache.popitem(last=False)
    
    def clear(self):
        self.cache.clear()
```

### Time-Based Cache

```python
import time

class TTLCache:
    def __init__(self, ttl_seconds=60):
        self.ttl = ttl_seconds
        self.cache = {}
    
    def get(self, key):
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            del self.cache[key]
        return None
    
    def put(self, key, value):
        self.cache[key] = (value, time.time())
```

---

## Object Pools

Object pools reuse expensive objects instead of creating new ones.

### Basic Object Pool

```python
class ObjectPool:
    def __init__(self, cls, size=10):
        self.cls = cls
        self.available = [cls() for _ in range(size)]
    
    def acquire(self):
        if self.available:
            return self.available.pop()
        return self.cls()  # Create new if pool empty
    
    def release(self, obj):
        self.available.append(obj)
```

### Usage Pattern

```python
class ExpensiveObject:
    def __init__(self):
        # Expensive initialization
        self.data = [0] * 10000
    
    def reset(self):
        # Reset state for reuse
        for i in range(len(self.data)):
            self.data[i] = 0

pool = ObjectPool(ExpensiveObject, size=10)

# Use object from pool
obj = pool.acquire()
try:
    # Use obj...
    obj.data[0] = 42
finally:
    obj.reset()
    pool.release(obj)
```

### Context Manager Pool

```python
from contextlib import contextmanager

class ObjectPool:
    def __init__(self, cls, size=10):
        self.cls = cls
        self.available = [cls() for _ in range(size)]
    
    @contextmanager
    def acquire(self):
        obj = self.available.pop() if self.available else self.cls()
        try:
            yield obj
        finally:
            self.available.append(obj)

# Clean usage
pool = ObjectPool(ExpensiveObject)

with pool.acquire() as obj:
    # Use obj...
    pass  # Automatically returned to pool
```

### Benefits of Object Pools

```python
import time

class HeavyObject:
    def __init__(self):
        time.sleep(0.01)  # Simulate expensive init

# Without pool: many allocations
start = time.time()
for i in range(100):
    obj = HeavyObject()
print(f"Without pool: {time.time() - start:.2f}s")

# With pool: reuse objects
pool = ObjectPool(HeavyObject, size=10)
start = time.time()
for i in range(100):
    obj = pool.acquire()
    pool.release(obj)
print(f"With pool: {time.time() - start:.2f}s")
```

---

## Choosing a Caching Strategy

| Strategy | Use When | Pros | Cons |
|----------|----------|------|------|
| `lru_cache` | Function memoization | Simple, built-in | Memory grows |
| Weak cache | Large objects | Auto-cleanup | Complex |
| TTL cache | Time-sensitive data | Fresh data | Stale window |
| Object pool | Expensive construction | Fast reuse | Manual management |

---

## Summary

Key points:
- Use `@lru_cache` for simple function memoization
- Use `WeakValueDictionary` for caches that auto-clean
- Implement custom caches for specific requirements (TTL, size)
- Use object pools when object creation is expensive
- Always consider memory vs. speed tradeoffs
- Clear caches when data becomes stale
