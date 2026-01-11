# Debugging

## Inspect Variables

### 1. Check Type

```python
x = [1, 2, 3]
print(type(x))
print(isinstance(x, list))
```

### 2. Check Identity

```python
a = [1, 2, 3]
b = a
print(a is b)
print(id(a) == id(b))
```

## Common Issues

### 1. Mutable Defaults

```python
# Bug
def append_to(item, lst=[]):
    lst.append(item)
    return lst

# Fix
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 2. Late Binding

```python
# Bug
funcs = [lambda: i for i in range(3)]

# Fix
funcs = [lambda x=i: x for i in range(3)]
```

## Summary

- Check types
- Watch mutable defaults
- Fix late binding
