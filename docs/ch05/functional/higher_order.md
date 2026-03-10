# Higher-Order Functions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Definition

Functions that:
1. Take functions as arguments
2. Return functions

## Take Functions

### 1. Apply Function

```python
def apply_twice(func, value):
    return func(func(value))

def add_one(x):
    return x + 1

print(apply_twice(add_one, 5))  # 7
```

## Return Functions

### 1. Function Factory

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## Built-in Examples

### 1. map, filter

```python
# map takes function
squared = map(lambda x: x**2, [1, 2, 3])

# filter takes function
evens = filter(lambda x: x % 2 == 0, range(10))
```

## Summary

- Take functions as args
- Return functions
- Enable abstraction
- Powerful pattern
