# Basic Assignment

## Simple Assignment

### 1. Create Binding

```python
x = 42
# Creates name 'x' bound to int 42
```

### 2. Rebinding

```python
x = 42
x = 100  # Rebind to new value
```

## Multiple Assignment

### 1. Tuple Unpacking

```python
a, b = 1, 2
x, y, z = [10, 20, 30]
```

### 2. Star Unpacking

```python
first, *rest = [1, 2, 3, 4]
print(first)  # 1
print(rest)   # [2, 3, 4]
```

## Chained Assignment

### 1. Same Object

```python
a = b = c = [1, 2, 3]
# All point to same list
print(a is b is c)  # True
```

## Augmented Assignment

### 1. Shortcuts

```python
x = 10
x += 5   # x = x + 5
x *= 2   # x = x * 2
```

### 2. In-place

```python
lst = [1, 2]
lst += [3, 4]  # Modifies in place
```

## Summary

- Simple: `x = value`
- Multiple: `a, b = 1, 2`
- Chained: `a = b = c`
- Augmented: `x += 1`
