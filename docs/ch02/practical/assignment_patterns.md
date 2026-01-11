# Assignment Patterns

## Unpacking

### 1. Multiple Assignment

```python
a, b = 1, 2
first, *rest = [1, 2, 3, 4]
```

## Swapping

### 1. Pythonic Swap

```python
a, b = b, a
```

## Walrus Operator

### 1. Assignment in Expression

```python
if (n := len(data)) > 10:
    print(f"Large: {n}")
```

## Summary

- Unpacking common
- Swap without temp
- Walrus for efficiency
