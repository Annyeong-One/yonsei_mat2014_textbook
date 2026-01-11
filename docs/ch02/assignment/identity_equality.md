# Identity vs Equality

## Identity (is)

### 1. Same Object

```python
a = [1, 2, 3]
b = a

print(a is b)  # True (same object)
```

### 2. Different Objects

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False (different)
```

## Equality (==)

### 1. Same Values

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (same values)
```

## When to Use

### 1. Use is

```python
# For None
if x is None:
    pass

# For True/False
if flag is True:
    pass
```

### 2. Use ==

```python
# For values
if x == 42:
    pass

if name == "Alice":
    pass
```

## Summary

| Operator | Checks | Use For |
|----------|--------|---------|
| `is` | Identity | None, True, False |
| `==` | Equality | Values, objects |

- `is`: same object
- `==`: same value
- Use `is` for singletons
- Use `==` for values
