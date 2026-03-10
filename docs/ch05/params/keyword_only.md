# Keyword-Only Parameters


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Syntax

### 1. After *

```python
def function(a, b, *, c, d):
    return a + b + c + d

# Must use keywords for c, d
function(1, 2, c=3, d=4)  # OK
# function(1, 2, 3, 4)    # Error
```

### 2. After *args

```python
def function(*args, key1, key2):
    print(args)
    print(key1, key2)

function(1, 2, 3, key1=4, key2=5)
```

## Use Cases

### 1. Clarity

```python
def create_user(name, email, *, admin=False, active=True):
    # admin and active must be named
    pass

create_user("Alice", "a@example.com", admin=True)
```

### 2. API Design

```python
def configure(*, host, port, timeout=30):
    # Force keyword arguments
    # Prevents positional mistakes
    pass
```

## Summary

- Force keyword arguments
- Improves clarity
- Better API design
- Use * to separate
