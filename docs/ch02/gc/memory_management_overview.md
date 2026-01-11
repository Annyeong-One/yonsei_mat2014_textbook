# Memory Management Overview

## Two Mechanisms

### 1. Reference Counting

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Count references
```

### 2. Garbage Collection

```python
import gc

# Handle cycles
gc.collect()
```

## How They Work Together

### 1. Refcount First

Most objects freed immediately by refcount

### 2. GC for Cycles

Periodic collection for circular references

## Summary

- Refcount: immediate
- GC: cycles
- Automatic management
