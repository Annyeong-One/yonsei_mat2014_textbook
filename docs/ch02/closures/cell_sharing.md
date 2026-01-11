# Cell Sharing

## Shared Cells

### 1. Multiple Functions

```python
def outer():
    x = 0
    
    def inc():
        nonlocal x
        x += 1
        return x
    
    def dec():
        nonlocal x
        x -= 1
        return x
    
    return inc, dec

inc, dec = outer()
print(inc())  # 1
print(inc())  # 2
print(dec())  # 1
```

## Same Cell Object

### 1. Verify Sharing

```python
def outer():
    x = 10
    f1 = lambda: x
    f2 = lambda: x
    return f1, f2

a, b = outer()
print(a.__closure__[0] is b.__closure__[0])  # True
```

## Summary

- Multiple functions share cells
- Enables shared state
- Same cell object
