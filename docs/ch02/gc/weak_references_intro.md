# Weak References Intro

## What Are They

### 1. Don't Prevent GC

```python
import weakref

obj = [1, 2, 3]
weak = weakref.ref(obj)

# Can still be collected
```

## Basic Usage

### 1. Create Weak Ref

```python
import weakref

obj = [1, 2, 3]
ref = weakref.ref(obj)

# Access
if ref() is not None:
    print(ref())
```

## Summary

- Don't prevent GC
- For caches
- Check before access
