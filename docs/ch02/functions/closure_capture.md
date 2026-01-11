# Closure Capture

## How Functions Capture

### 1. Free Variables

```python
def outer():
    x = 10
    
    def inner():
        return x  # Captures x
    
    return inner
```

### 2. Multiple Captures

```python
def outer():
    x = 1
    y = 2
    
    def inner():
        return x + y  # Captures both
    
    return inner
```

## Summary

- Functions capture free variables
- Stored in cells
- Multiple captures possible
