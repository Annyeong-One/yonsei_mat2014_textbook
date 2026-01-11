# Observer Pattern

## Weak Observers

### 1. Implementation

```python
import weakref

class Observable:
    def __init__(self):
        self._observers = weakref.WeakSet()
    
    def subscribe(self, observer):
        self._observers.add(observer)
    
    def notify(self):
        for obs in self._observers:
            obs.update()
```

## Summary

- Weak references for observers
- Automatic cleanup
- Prevents leaks
