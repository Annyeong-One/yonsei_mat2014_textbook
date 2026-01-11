# __slots__

## Memory Savings

### 1. Without Slots

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Uses __dict__
p = Point(10, 20)
print(p.__dict__)  # {'x': 10, 'y': 20}
```

### 2. With Slots

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# No __dict__, uses slots
p = Point(10, 20)
# print(p.__dict__)  # AttributeError
```

## Size Comparison

### 1. Memory Usage

```python
import sys

class WithDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

d = WithDict(1, 2)
s = WithSlots(1, 2)

print(sys.getsizeof(d))  # Larger
print(sys.getsizeof(s))  # Smaller
```

## Restrictions

### 1. No New Attributes

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
# p.z = 30  # AttributeError
```

### 2. No __dict__

```python
# Can't use vars()
# p.__dict__  # AttributeError
```

## When to Use

### 1. Many Instances

```python
# Good: millions of objects
points = [Point(i, i) for i in range(1000000)]

# Saves significant memory
```

### 2. Performance Critical

```python
# Faster attribute access
# No dict lookup
```

## Summary

- Save memory
- Faster access
- No __dict__
- Can't add attributes
- Use for many instances
