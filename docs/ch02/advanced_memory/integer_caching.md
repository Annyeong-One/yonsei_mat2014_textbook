# Integer Caching

## CPython Caching

### 1. Range [-5, 256]

```python
a = 100
b = 100
print(a is b)  # True (cached)

a = 1000
b = 1000
print(a is b)  # May be False
```

## Why Cache

### 1. Performance

Small integers used frequently

### 2. Memory

Share common values

## Summary

- [-5, 256] cached
- Performance optimization
- Don't rely on it
