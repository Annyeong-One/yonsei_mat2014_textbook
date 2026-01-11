# Advanced Concepts

## Nested Closures

### 1. Multiple Levels

```python
def outer():
    x = 1
    def middle():
        y = 2
        def inner():
            return x + y
        return inner
    return middle()

f = outer()
print(f())  # 3
```

## Closure Composition

### 1. Combining Closures

```python
def add(x):
    def adder(y):
        return x + y
    return adder

add5 = add(5)
add10 = add(10)

print(add5(3))   # 8
print(add10(3))  # 13
```

## Summary

- Nested closures
- Composition patterns
- Multiple captures
