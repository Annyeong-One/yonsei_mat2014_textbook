# Key Takeaways

## Variables Are References

### 1. Core Model

```python
x = [1, 2, 3]
y = x

# Both reference same object
print(x is y)  # True
```

### 2. Assignment Binds

```python
x = 42  # Binds name to object
x = 100  # Rebinds to new object
```

## Objects Have Three Properties

### 1. Identity Type Value

```python
x = [1, 2, 3]

print(id(x))    # Identity
print(type(x))  # Type
print(x)        # Value
```

### 2. Identity Stable

```python
x = [1, 2, 3]
x.append(4)
# Same identity
```

## Memory Management

### 1. Automatic

```python
def function():
    data = [1, 2, 3]
    return data[0]
    # data freed automatically
```

### 2. Two Systems

- Reference counting (immediate)
- Garbage collection (cycles)

## Closures

### 1. Capture Variables

```python
def outer():
    x = 10
    def inner():
        return x
    return inner
```

### 2. Late Binding

```python
# Use defaults to capture value
funcs = [lambda x=i: x for i in range(3)]
```

## Scope

### 1. LEGB Rule

- Local
- Enclosing
- Global
- Built-in

### 2. Lookup Order

```python
# Searches: L -> E -> G -> B
```

## Summary

- Names reference objects
- Objects have identity/type/value
- Automatic memory management
- Closures capture variables
- LEGB scope resolution
