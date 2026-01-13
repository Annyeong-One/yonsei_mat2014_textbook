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
print(counter.__code__.co_freevars)  # ('count',)
```


## Multi-Level Nesting

### 1. Three-Level Example

```python
def outer():
    x = "outer"
    
    def middle():
        y = "middle"
        
        def inner():
            return x, y  # Both are free variables
        
        return inner
    
    return middle()

f = outer()
print(f())  # ('outer', 'middle')
print(f.__code__.co_freevars)  # ('x', 'y')
print(f.__closure__[0].cell_contents)  # 'outer'
print(f.__closure__[1].cell_contents)  # 'middle'
```

### 2. Only Used Variables Captured

```python
def outer():
    x = "outer"
    def middle():
        y = "middle"
        def inner():
            return y  # Only y is used
        return inner
    return middle()

f = outer()
print(f.__code__.co_freevars)  # ('y',) — x not captured
```


## Variable Shadowing

When enclosing scopes use the same variable name:

```python
def outer():
    x = "outer"
    
    def middle():
        x = "middle"  # Shadows outer's x
        
        def inner():
            return x  # Captures nearest x
        
        return inner
    
    return middle()

f = outer()
print(f())  # 'middle' — nearest enclosing scope wins
```

Python resolves free variables from **inner to outer**, stopping at the first match.


## Summary

- Free variables from enclosing scope
- Stored in cell objects
- Enable closures
