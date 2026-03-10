# *args and **kwargs


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## *args

### 1. Variable Positional

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))        # 6
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

print_info(name="Alice", age=30, city="NYC")
```

### 2. Dict Inside

```python
def function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
```

## Combined

### 1. All Parameters

```python
def function(a, b, *args, key=None, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"key={key}")
    print(f"kwargs={kwargs}")

function(1, 2, 3, 4, key=5, x=6, y=7)
```

## Unpacking

### 1. Call Time

```python
def func(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(func(*args))  # 6

kwargs = {'a': 1, 'b': 2, 'c': 3}
print(func(**kwargs))  # 6
```

## Summary

- *args: variable positional
- **kwargs: variable keyword
- Order matters
- Unpack with * and **
