# Generator Expressions

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

## Summary

- Lazy evaluation
- Memory efficient
- Single iteration
- Good for pipelines
