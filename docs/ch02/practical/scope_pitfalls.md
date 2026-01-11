# Scope Pitfalls

## Late Binding

### 1. Loop Variables

```python
# Bug
funcs = [lambda: i for i in range(3)]

# Fix
funcs = [lambda x=i: x for i in range(3)]
```

## UnboundLocalError

### 1. Missing nonlocal

```python
def outer():
    x = 0
    def inner():
        x += 1  # Error!
        # Need: nonlocal x
```

## Summary

- Watch late binding
- Remember nonlocal
- Common gotchas
