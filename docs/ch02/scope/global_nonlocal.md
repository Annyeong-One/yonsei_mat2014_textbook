# Global and Nonlocal

## global Keyword

### 1. Modify Global

```python
x = 10

def function():
    global x
    x = 20

function()
print(x)  # 20
```

## nonlocal Keyword

### 1. Modify Enclosing

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
    
    inner()
    print(x)  # 20
```

## Summary

- global: module level
- nonlocal: enclosing level
- Both modify outer scope
