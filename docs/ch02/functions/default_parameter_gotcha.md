# Default Parameter Gotcha

## Mutable Defaults

### 1. The Problem

```python
def append_to(item, lst=[]):
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]  # Bug!
```

### 2. The Fix

```python
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Summary

- Mutable defaults dangerous
- Use None sentinel
- Create new each call
