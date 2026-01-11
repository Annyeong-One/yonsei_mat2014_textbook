# Cyclic Garbage

## The Problem

### 1. Reference Cycle

```python
a = []
b = []
a.append(b)
b.append(a)

# Cycle: a → b → a
# Refcount never reaches 0
```

### 2. More Complex

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create cycle
head = Node(1)
second = Node(2)
head.next = second
second.next = head

# Cycle in linked structure
```

## Detection

### 1. Mark and Sweep

```python
# GC marks reachable objects
# Sweeps unreachable objects

import gc

# Force cycle detection
gc.collect()
```

### 2. Example

```python
class Item:
    def __init__(self):
        self.ref = None

a = Item()
b = Item()
a.ref = b
b.ref = a

# Create cycle
del a
del b

# Cycle collected by GC
import gc
gc.collect()  # Collects cycle
```

## Prevention

### 1. Break Cycles

```python
# Manually break
a = Item()
b = Item()
a.ref = b
b.ref = a

# When done
a.ref = None
b.ref = None
# No cycle
```

### 2. Weak References

```python
import weakref

class Item:
    def __init__(self):
        self._ref = None
    
    @property
    def ref(self):
        return self._ref() if self._ref else None
    
    @ref.setter
    def ref(self, value):
        self._ref = weakref.ref(value) if value else None

# Weak ref breaks cycle
```

## Context Managers

### 1. Automatic Cleanup

```python
class Resource:
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.cleanup()  # Break cycles
    
    def cleanup(self):
        self.ref = None

with Resource() as r:
    # Use resource
    pass
# Cleaned up automatically
```

## Summary

- Cycles prevent refcount GC
- Need cycle detector
- Break explicitly when possible
- Use weak refs
- Context managers help
