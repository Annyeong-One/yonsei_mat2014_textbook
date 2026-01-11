# Code Review

## Check For

### 1. Clear Names

```python
# Good
user_data = get_data()

# Bad
x = get_data()
```

### 2. Mutable Defaults

```python
# Fix
def function(items=None):
    if items is None:
        items = []
```

### 3. Late Binding

```python
# Fix
funcs = [lambda x=i: x for i in range(3)]
```

## Summary

- Clear naming
- Small functions
- Fix common bugs
