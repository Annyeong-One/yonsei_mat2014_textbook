# Performance

## Measure First

### 1. timeit

```python
import timeit

time = timeit.timeit('sum(range(100))', number=10000)
```

## Optimizations

### 1. Comprehensions

```python
# Fast
result = [i * 2 for i in range(1000)]
```

### 2. Generators

```python
# Memory efficient
def gen(n):
    for i in range(n):
        yield i * 2
```

### 3. Local Cache

```python
def function():
    length = len
    for i in range(1000):
        result = length(data)
```

## Summary

- Measure first
- Use comprehensions
- Use generators
- Cache lookups
