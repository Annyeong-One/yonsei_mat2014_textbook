# Cache Systems

## LRU Cache

### 1. Built-in

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive(x):
    return x ** 2
```

## Weak Value Cache

### 1. Auto-Cleaning

```python
import weakref

cache = weakref.WeakValueDictionary()
```

## Custom Cache

### 1. Size-Limited

```python
class Cache:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.cache = {}
    
    def get(self, key):
        return self.cache.get(key)
    
    def put(self, key, value):
        if len(self.cache) >= self.maxsize:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value
```

## Summary

- LRU cache built-in
- Weak caches auto-clean
- Custom caches possible
