# Scope Lifetime


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Local Scope

### 1. Function Call

```python
def function():
    x = 10  # Created at call
    return x
    # Destroyed after return

result = function()
# x no longer exists
```

### 2. Frame Lifetime

```python
def outer():
    x = 10
    
    def inner():
        return x
    
    return inner
    # Frame ends but x kept for closure

f = outer()
print(f())  # x still accessible
```

## Global Scope

### 1. Module Lifetime

```python
# Exists for program lifetime
x = 10

def function():
    print(x)

# x available throughout
```

## Summary

- Local: function call duration
- Enclosing: kept if captured
- Global: program lifetime
- Built-in: always available
