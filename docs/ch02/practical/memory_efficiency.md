# Memory Efficiency

## Generators

### 1. Lazy Evaluation

```python
# Efficient
gen = (x**2 for x in range(1000000))

# vs list
lst = [x**2 for x in range(1000000)]
```

## __slots__

### 1. Reduce Overhead

```python
class Point:
    __slots__ = ['x', 'y']
```

## Summary

- Use generators
- Consider __slots__
- Minimize allocations
