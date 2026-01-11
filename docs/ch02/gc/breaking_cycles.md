# Breaking Cycles

## Manual Breaking

### 1. Clear References

```python
class Node:
    def __init__(self):
        self.next = None

# Create cycle
a = Node()
b = Node()
a.next = b
b.next = a

# Break cycle
a.next = None
```

## Context Managers

### 1. Automatic Cleanup

```python
class Resource:
    def __exit__(self, *args):
        self.ref = None
```

## Summary

- Clear references explicitly
- Use context managers
- Prevents leaks
