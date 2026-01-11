# Names vs Objects

## Core Distinction

### 1. Python Model

Names are references to objects:

```python
x = [1, 2, 3]
# x is a name pointing to list object
```

### 2. Key Insight

```python
x = [1, 2, 3]
y = x
z = x

# Multiple names, one object
print(x is y is z)  # True
```

## Object Properties

### 1. Three Characteristics

```python
x = [1, 2, 3]

print(id(x))        # Identity
print(type(x))      # Type
print(x)            # Value
```

### 2. Identity Persists

```python
x = [1, 2, 3]
original_id = id(x)

x.append(4)
print(id(x) == original_id)  # True
```

## Name Binding

### 1. Assignment

```python
x = [1, 2, 3]
y = x

print(id(x) == id(y))  # True
```

### 2. Rebinding

```python
x = [1, 2, 3]
y = x

x = [4, 5, 6]

print(x is y)       # False
```

## Summary

### 1. Key Points

- Names are references
- Objects have identity/type/value
- Assignment binds names
- Multiple names → one object
