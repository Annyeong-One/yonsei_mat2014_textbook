# Style Guide

## PEP 8

### 1. Naming

```python
def my_function():
    local_var = 10

class MyClass:
    pass

MAX_SIZE = 100
```

### 2. Spacing

```python
def function(a, b):
    return a + b
```

## Documentation

### 1. Clear Names

```python
user_count = len(users)
```

### 2. Small Functions

```python
def process():
    data = load()
    clean = process(data)
    return save(clean)
```

## Summary

- Follow PEP 8
- Clear names
- Small functions
