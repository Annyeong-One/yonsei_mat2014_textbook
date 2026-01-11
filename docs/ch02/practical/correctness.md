# Correctness

## Avoid Common Bugs

### 1. Mutable Defaults

```python
# Wrong
def func(lst=[]):
    lst.append(1)

# Right
def func(lst=None):
    if lst is None:
        lst = []
```

### 2. Late Binding

```python
# Wrong
funcs = [lambda: i for i in range(3)]

# Right
funcs = [lambda x=i: x for i in range(3)]
```

## Summary

- Fix mutable defaults
- Fix late binding
- Write tests
