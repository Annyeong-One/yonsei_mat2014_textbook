# Identity Type Value


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Three Characteristics

### 1. Every Object

```python
x = [1, 2, 3]

print(id(x))        # Identity
print(type(x))      # Type
print(x)            # Value
```

## Identity

### 1. Unique ID

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a) != id(b))  # True
```

**CPython note**: `id()` returns the memory address:

```python
x = [1, 2, 3]
print(id(x))       # e.g., 140234567890
print(hex(id(x)))  # e.g., '0x7f8b2c3d4e50'
```

Other implementations (PyPy, Jython) may return a different unique token.

### 2. Constant

```python
x = [1, 2, 3]
original_id = id(x)

x.append(4)
print(id(x) == original_id)  # True
```

### 3. Identity Check

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False
```

## Type

### 1. Determines Behavior

```python
x = 42
y = "42"

print(type(x))      # <class 'int'>
print(type(y))      # <class 'str'>
```

### 2. Type Immutable

```python
x = [1, 2, 3]
# Cannot change type
```

## Value

### 1. Object Data

```python
x = [1, 2, 3]
print(x)            # [1, 2, 3]
```

### 2. Mutable Values

```python
x = [1, 2, 3]
x[0] = 100
print(x)            # [100, 2, 3]
```

## Summary

| Property | Check | Example |
|----------|-------|---------|
| Identity | `is` | `id(x)` |
| Type | `isinstance()` | `type(x)` |
| Value | `==` | `x[:]` |
