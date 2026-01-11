# Lambda vs Def

## Lambda Functions

### 1. Anonymous

```python
# Lambda
add = lambda x, y: x + y

# Equivalent def
def add(x, y):
    return x + y
```

## Closures Work Same

### 1. Both Capture

```python
def outer():
    x = 10
    
    # Lambda closure
    f1 = lambda: x
    
    # Def closure
    def f2():
        return x
    
    return f1, f2
```

## Summary

- Lambda: single expression
- Def: full statements
- Both support closures
