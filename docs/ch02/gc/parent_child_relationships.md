# Parent-Child Relationships

## Weak Back References

### 1. Avoid Cycles

```python
import weakref

class Child:
    def __init__(self, parent):
        self._parent = weakref.ref(parent)
    
    def get_parent(self):
        return self._parent()
```

## Summary

- Parent has strong ref to child
- Child has weak ref to parent
- Avoids cycles
