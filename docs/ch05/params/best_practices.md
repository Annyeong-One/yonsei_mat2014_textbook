# Parameter Best Practices


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Order

### 1. Standard Order

```python
def function(
    pos_only, /,
    standard,
    *args,
    kw_only,
    **kwargs
):
    pass
```

## Defaults

### 1. Immutable Defaults

```python
# Good
def function(items=None):
    if items is None:
        items = []

# Bad
def function(items=[]):  # Mutable default!
    pass
```

## Clarity

### 1. Descriptive Names

```python
# Good
def create_user(username, email, is_admin=False):
    pass

# Bad
def create_user(u, e, a=False):
    pass
```

## Summary

- Follow standard order
- Use immutable defaults
- Descriptive names
- Document parameters
