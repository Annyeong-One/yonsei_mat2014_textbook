# Memory Optimization

## Techniques

### 1. __slots__

```python
class Point:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Saves memory vs dict
```

### 2. Generators

```python
# Bad: list in memory
def get_numbers():
    return [x for x in range(1000000)]

# Good: generator
def get_numbers():
    return (x for x in range(1000000))
```

### 3. Itertools

```python
import itertools

# Memory efficient
for item in itertools.islice(data, 100):
    process(item)
```

## Summary

- Use __slots__ for classes
- Prefer generators
- Use itertools
- Avoid unnecessary copies
