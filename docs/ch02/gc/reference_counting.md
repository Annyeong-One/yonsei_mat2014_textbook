# Reference Counting

## CPython Mechanism

### 1. Every Object

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # 2
```

### 2. Increment/Decrement

```python
x = [1, 2, 3]  # refcount = 1
y = x          # refcount = 2
del y          # refcount = 1
del x          # refcount = 0 → freed
```

## Automatic

### 1. No Manual Management

```python
def function():
    x = [1, 2, 3]
    # Automatically freed at return
    return

# No memory leak
```

## Advantages

### 1. Immediate

```python
x = [1, 2, 3]
del x
# Memory freed immediately
```

## Limitations

### 1. Cycles

```python
a = []
b = []
a.append(b)
b.append(a)
# Cycle! Need cycle GC
```

## Summary

- Count references
- Free at zero
- Immediate collection
- Can't handle cycles
