# Guarantees vs Details


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Language Guarantees

### 1. Semantic Behavior

Always guaranteed:

```python
# Assignment creates binding
x = 42

# Identity stable
lst = [1, 2, 3]
original_id = id(lst)
lst.append(4)
# Guaranteed: id(lst) == original_id
```

### 2. Type Behavior

```python
# Immutable behavior
x = "hello"
# x[0] = "H"  # TypeError (guaranteed)

# Mutable behavior  
lst = [1, 2, 3]
lst[0] = 100        # Works (guaranteed)
```

## Implementation Details

### 1. Not Guaranteed

CPython specifics (marked with note):

```python
# Small int caching (CPython)
a = 42
b = 42
# a is b may be True (NOT guaranteed)

# Large ints
x = 1000
y = 1000
# x is y may be False
```

### 2. Memory Layout

```python
# id() returns address in CPython
x = [1, 2, 3]
print(id(x))  # Address (CPython)

# Other implementations may differ
```

## Comparison Table

| Aspect | Guaranteed | Not Guaranteed |
|--------|-----------|----------------|
| Equality check | Yes | - |
| Identity for None | Yes | - |
| Small int identity | No | CPython: True |
| id() = address | No | CPython: Yes |
| String interning | No | CPython: Sometimes |

## Best Practices

### 1. Rely on Guarantees

```python
# Good: language guarantees
if x == y:              # Value comparison
    pass

if x is None:           # Singleton
    pass

# Bad: implementation details
if id(x) < id(y):       # Address comparison
    pass
```

### 2. Portable Code

```python
# Use == for values
if count == 0:
    pass

# Use is only for singletons
if result is None:
    pass
```

## Summary

### 1. Depend On

- Equality (==)
- Identity for None/True/False
- Mutability behavior
- Type semantics

### 2. Don't Depend On

- Small integer caching
- String interning
- id() being address
- Reference counts
- GIL existence
