# Cells & Free Variables

## Free Variables

### 1. Definition

Variables referenced but not defined locally:

```python
def outer():
    x = 10
    
    def inner():
        return x  # Free in inner
    
    return inner
```

### 2. Cell Objects

CPython uses cells:

```python
def outer():
    x = 10
    
    def inner():
        return x
    
    return inner

f = outer()
print(f.__closure__[0].cell_contents)  # 10
```

## Inspection

### 1. View Closure

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter()
print(counter.__closure__)
print(counter.__code__.co_freevars)
```

## Summary

- Free variables from enclosing scope
- Stored in cell objects
- Enable closures
