# Closure Performance

## Overhead

### 1. Cell Access

```python
# Slower: cell lookup
def outer():
    x = 10
    return lambda: x

# Faster: local access
def function():
    x = 10
    return x
```

## Best Practices

### 1. Minimize Captures

```python
# Bad: captures unused
def outer():
    a, b, c = 1, 2, 3
    return lambda: a  # Still captures b, c

# Better: only needed
def outer():
    a = 1
    return lambda: a
```

## Summary

- Closure has overhead
- Cell access slower
- Minimize captures
