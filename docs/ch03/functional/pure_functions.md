# Pure Functions

## Definition

### 1. No Side Effects

```python
# Pure
def add(x, y):
    return x + y

# Impure
def add_and_print(x, y):
    print(f"Adding {x} and {y}")  # Side effect
    return x + y
```

### 2. Same Input → Same Output

```python
# Pure
def square(x):
    return x ** 2

# Impure
import random
def random_square(x):
    return x ** 2 + random.randint(0, 10)
```

## Benefits

### 1. Testable

```python
# Easy to test
def multiply(x, y):
    return x * y

assert multiply(3, 4) == 12
```

### 2. Cacheable

```python
@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Summary

- No side effects
- Deterministic
- Easy to test
- Cacheable
