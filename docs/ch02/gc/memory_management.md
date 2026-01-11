# Memory Management

## Overview

### 1. Automatic

```python
# Python manages automatically
x = [1, 2, 3]  # Allocated
del x          # Freed (eventually)
```

### 2. Two Systems

- Reference counting (immediate)
- Garbage collection (cycles)

## Best Practices

### 1. Let Python Handle

```python
# Good: normal code
def process():
    data = load_data()
    result = transform(data)
    return result
    # data freed automatically
```

### 2. Break Cycles

```python
# Break cycles when done
obj.parent = None  # Clear reference
```

### 3. Use Context Managers

```python
with open('file.txt') as f:
    data = f.read()
# File closed automatically
```

## Monitoring

### 1. Check Objects

```python
import gc

# List all objects
objects = gc.get_objects()
print(len(objects))
```

### 2. Track Type

```python
import sys

# Count by type
types = {}
for obj in gc.get_objects():
    t = type(obj).__name__
    types[t] = types.get(t, 0) + 1
```

## Summary

- Automatic management
- Refcount + GC
- Break cycles explicitly
- Use context managers
- Monitor when needed
