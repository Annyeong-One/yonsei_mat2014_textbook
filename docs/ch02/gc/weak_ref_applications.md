# Weak Ref Applications

## Caching

### 1. Weak Value Dict

```python
import weakref

cache = weakref.WeakValueDictionary()
obj = SomeObject()
cache['key'] = obj

# obj can be collected
```

## Observer Pattern

### 1. Weak Observers

```python
import weakref

class Subject:
    def __init__(self):
        self._observers = weakref.WeakSet()
    
    def attach(self, observer):
        self._observers.add(observer)
```

## Summary

- Caches
- Observer pattern
- Parent-child relationships
