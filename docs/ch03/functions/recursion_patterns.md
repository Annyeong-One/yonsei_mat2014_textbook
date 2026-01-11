# Recursion Patterns

## Basic Recursion

### 1. Factorial

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## Tree Recursion

### 1. Fibonacci

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8
```

## Tail Recursion

### 1. Not Optimized

```python
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n-1, n*acc)

# Python doesn't optimize tail calls
```

## Iteration Alternative

### 1. Better Performance

```python
def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
```

## Summary

- Base case essential
- Tree recursion expensive
- No tail call optimization
- Consider iteration
