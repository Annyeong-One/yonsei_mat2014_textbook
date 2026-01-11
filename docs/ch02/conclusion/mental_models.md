# Mental Models

## Post-it Notes

### 1. Names as Labels

```python
# Think of names as sticky notes
obj = [1, 2, 3]  # Stick "obj" note on object

x = obj  # Stick "x" note on same object
y = obj  # Stick "y" note on same object

# All notes on one object
```

### 2. Not Boxes

```python
# Wrong: variable as box containing value
# Right: variable as label pointing to object
```

## Object Pool

### 1. Objects in Heap

```python
# All objects floating in heap
# Names point to them

x = [1, 2, 3]  # Create object in heap
y = x          # Point to same object
```

## Garbage Collector

### 1. Janitor Model

```python
# GC is janitor
# Cleans up unreferenced objects

x = [1, 2, 3]
del x
# Janitor collects when no references
```

## Closure as Backpack

### 1. Functions Carry State

```python
def outer():
    x = 10  # Put x in backpack
    
    def inner():
        return x  # Access from backpack
    
    return inner
```

## Scope as Nested Boxes

### 1. Boxes Within Boxes

```python
# Global box
x = 1

def outer():
    # Enclosing box
    y = 2
    
    def inner():
        # Local box
        z = 3
        # Can see out to enclosing and global
```

## Summary

- Names: post-it notes
- Objects: items in heap
- GC: janitor
- Closures: backpacks
- Scope: nested boxes
