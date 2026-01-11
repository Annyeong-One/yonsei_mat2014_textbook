# Self-Cleaning Cache

## Weak Value Dictionary

### 1. Auto Cleanup

```python
import weakref

cache = weakref.WeakValueDictionary()

def get_object(key):
    if key not in cache:
        obj = create_expensive_object(key)
        cache[key] = obj
    return cache[key]
```

## Summary

- Auto-cleaning cache
- Saves memory
- Simple implementation
