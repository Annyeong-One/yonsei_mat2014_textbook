# Circular References

## The Problem

### 1. Cycle Example

```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a
# Cycle: a → b → a
```

## Detection

### 1. Cycle Detector

```python
import gc

# GC finds cycles
gc.collect()
```

## Prevention

### 1. Break Manually

```python
a.ref = None
b.ref = None
```

## Summary

- Cycles prevent refcount collection
- GC detects cycles
- Break manually when possible
