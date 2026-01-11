# Unpacking

## Basic Unpacking

### 1. Tuples

```python
point = (10, 20)
x, y = point

print(x, y)  # 10 20
```

### 2. Lists

```python
data = [1, 2, 3]
a, b, c = data
```

## Star Unpacking

### 1. Collect Rest

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

### 2. Middle Elements

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(middle)  # [2, 3, 4]
```

### 3. Ignore

```python
first, *_, last = range(10)
print(first, last)  # 0 9
```

## Nested Unpacking

### 1. Nested Structures

```python
data = [(1, 2), (3, 4)]
(a, b), (c, d) = data

print(a, b, c, d)  # 1 2 3 4
```

## Dictionary Unpacking

### 1. Function Args

```python
def func(a, b, c):
    return a + b + c

data = {'a': 1, 'b': 2, 'c': 3}
result = func(**data)
```

## Summary

- Basic: `a, b = iterable`
- Star: `*rest` for remainder
- Nested: `(a, b), (c, d)`
- Dict: `**kwargs`
