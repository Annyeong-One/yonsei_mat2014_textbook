# Rebinding vs Mutation

## Core Difference

### 1. Rebinding

Creates new binding:

```python
def outer():
    x = [1, 2, 3]
    
    def rebind():
        x = [4, 5, 6]  # New local x!
    
    rebind()
    print(x)  # [1, 2, 3] (unchanged)
```

### 2. Mutation

Modifies object:

```python
def outer():
    x = [1, 2, 3]
    
    def mutate():
        x.append(4)  # Modifies outer's x
    
    mutate()
    print(x)  # [1, 2, 3, 4]
```

## Why Different

### 1. Rebinding

```python
# Assignment creates local
def inner():
    x = value  # Local assignment
```

### 2. Mutation

```python
# Method call on object
def inner():
    x.method()  # Uses outer's x
```

## Operators

### 1. += on Mutable

```python
def outer():
    items = [1, 2, 3]
    
    def extend():
        items += [4, 5]  # Mutation
    
    extend()
    print(items)  # [1, 2, 3, 4, 5]
```

### 2. += on Immutable

```python
def outer():
    count = 0
    
    def increment():
        count += 1  # Rebinding! Error
        # Need: nonlocal count
```

## Solutions

### 1. Use nonlocal

```python
def outer():
    x = 10
    
    def inner():
        nonlocal x
        x = 20
```

### 2. Use Mutable

```python
def outer():
    count = [0]
    
    def increment():
        count[0] += 1  # Mutation works
```

## Summary

- Rebinding: creates new binding, needs nonlocal
- Mutation: modifies object, works naturally
- Assignment = rebinding
- Method calls = mutation
