# GIL Interaction

## Global Interpreter Lock

### 1. One Thread at Time

Python threads don't run truly parallel (CPython)

### 2. Impact on Variables

```python
# Thread-safe for most operations
x = 42  # Atomic
```

## Memory Management

### 1. GC and GIL

GC operations need GIL

## Summary

- GIL limits parallelism
- Most ops thread-safe
- GC needs GIL
