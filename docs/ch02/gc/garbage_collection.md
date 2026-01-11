# Garbage Collection

## Cycle Detection

### 1. Generational GC

```python
import gc

# Three generations
print(gc.get_count())  # (count0, count1, count2)
```

### 2. Force Collection

```python
import gc

gc.collect()  # Force collection
```

## Cycles

### 1. Example

```python
class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a

# Cycle: a → b → a
# Needs cycle GC
```

## Control

### 1. Disable/Enable

```python
import gc

gc.disable()  # Disable
# ... critical section ...
gc.enable()   # Re-enable
```

### 2. Thresholds

```python
# Get thresholds
print(gc.get_threshold())  # (700, 10, 10)

# Set thresholds
gc.set_threshold(1000, 15, 15)
```

## Summary

- Handles cycles
- Generational approach
- Can be controlled
- Complements refcounting
