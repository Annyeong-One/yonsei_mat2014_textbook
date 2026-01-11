# Common Pitfalls

## Late Binding

### 1. Loop Variable

```python
# Bug
funcs = [lambda: i for i in range(3)]

# Fix
funcs = [lambda x=i: x for i in range(3)]
```

## Large Captures

### 1. Memory Issue

```python
# Bad
def outer():
    big = [0] * 1000000
    return lambda: big[0]

# Better
def outer():
    big = [0] * 1000000
    first = big[0]
    return lambda: first
```

## Summary

- Watch late binding
- Minimize captures
- Use defaults to capture value
