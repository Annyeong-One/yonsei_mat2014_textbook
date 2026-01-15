# Integer Caching

## CPython Behavior

### 1. Small Integers

CPython caches [-5, 256]:

```python
# Cached range
a = 100
b = 100
print(a is b)           # True
print(id(a) == id(b))   # True
```

### 2. Outside Range

```python
# Not cached
x = 1000
y = 1000
print(x is y)           # Usually False
print(x == y)           # True
```

## Why Cache

### 1. Performance

```python
# Without caching:
# Every loop creates new objects
for i in range(100):
    total += i          # 100 objects

# With caching:
# Reuses same 100 objects
```

### 2. Memory

```python
# Without caching
numbers = [1, 2, 3, 1, 2, 3]
# 6 separate objects

# With caching
# Only 3 objects shared
```

## Best Practices

### 1. Never Rely On

```python
# Bad: assumes caching
def bad(x):
    if x is 42:         # Don't!
        return True

# Good: use ==
def good(x):
    if x == 42:         # Correct
        return True
```

### 2. Singletons Only

```python
# Use 'is' only for:
if x is None:           # OK
    pass

if x is True:           # OK
    pass

# Not for integers:
# if x is 0:            # Bad!
```

## Summary

### 1. CPython

- Caches [-5, 256]
- Automatic optimization
- Not part of language spec

### 2. Write Portable

```python
# Always use ==
if count == 0:
    pass

# Only is for singletons
if result is None:
    pass
```
