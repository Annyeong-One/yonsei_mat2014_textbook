# Generator Expressions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Syntax

### 1. Like Comprehension

```python
# List comprehension
squares_list = [x**2 for x in range(1000)]

# Generator expression
squares_gen = (x**2 for x in range(1000))
```

## Lazy Evaluation

### 1. Memory Efficient

```python
# Consumes memory
large_list = [x**2 for x in range(1000000)]

# Memory efficient
large_gen = (x**2 for x in range(1000000))

# Use one at a time
for value in large_gen:
    process(value)
```

## Use Cases

### 1. Pipeline

```python
# Chained generators
numbers = range(1000)
squares = (x**2 for x in numbers)
evens = (x for x in squares if x % 2 == 0)
result = sum(evens)
```

## Reimplementing map and filter

Generators can recreate the behavior of `map()` and `filter()`.

### 1. Custom map

```python
def my_map(func, iterable):
    for item in iterable:
        yield func(item)

squares = my_map(lambda x: x * x, [1, 2, 3, 4])
print(list(squares))  # [1, 4, 9, 16]
```

### 2. Custom filter

```python
def my_filter(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item

evens = my_filter(lambda x: x % 2 == 0, range(10))
print(list(evens))  # [0, 2, 4, 6, 8]
```

### 3. Comparison

| Operation | Built-in | Custom Generator | Generator Expression |
|-----------|----------|------------------|----------------------|
| map | `map(f, xs)` | `my_map(f, xs)` | `(f(x) for x in xs)` |
| filter | `filter(p, xs)` | `my_filter(p, xs)` | `(x for x in xs if p(x))` |

All three approaches are **lazy** — values computed on demand.

## Summary

- Lazy evaluation
- Memory efficient
- Single iteration
- Good for pipelines
