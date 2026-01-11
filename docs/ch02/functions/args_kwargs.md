# Args and Kwargs

## *args

### 1. Variable Positional

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

### 2. Tuple Inside

```python
def function(*args):
    print(type(args))  # <class 'tuple'>
    for arg in args:
        print(arg)
```

## **kwargs

### 1. Variable Keyword

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
```

### 2. Dict Inside

```python
def function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
```

## Combined

### 1. Order Matters

```python
def function(a, b, *args, key=None, **kwargs):
    # a, b: positional
    # args: extra positional
    # key: keyword-only
    # kwargs: extra keyword
    pass
```

## Unpacking

### 1. Call Time

```python
def function(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(function(*args))  # 6

kwargs = {'a': 1, 'b': 2, 'c': 3}
print(function(**kwargs))  # 6
```

## Summary

- *args: tuple of positional
- **kwargs: dict of keyword
- Order: positional, *args, keyword, **kwargs
- Unpack with * and **
