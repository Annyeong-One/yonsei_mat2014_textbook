# Cellvars vs Freevars

## Cell Variables

### 1. In Enclosing

```python
def outer():
    x = 10  # Cellvar in outer
    
    def inner():
        return x
    
    return inner

print(outer.__code__.co_cellvars)  # ('x',)
```

## Free Variables

### 1. In Inner

```python
def outer():
    x = 10
    
    def inner():
        return x  # Freevar in inner
    
    return inner

f = outer()
print(f.__code__.co_freevars)  # ('x',)
```

## Summary

- Cellvar: defining function
- Freevar: using function
- Same variable, different view
