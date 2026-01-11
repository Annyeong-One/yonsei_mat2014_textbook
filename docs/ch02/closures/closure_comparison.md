# Closure Comparison

## vs Global Variables

### 1. Global

```python
count = 0

def increment():
    global count
    count += 1
    return count

# Issues: namespace pollution, single instance
```

### 2. Closure

```python
def make_counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

# Better: encapsulated, multiple instances
c1 = make_counter()
c2 = make_counter()
```

## vs Classes

### 1. Class

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count

c = Counter()
```

### 2. Closure

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()

# Simpler for single method
```

## Summary

| Aspect | Closure | Class | Global |
|--------|---------|-------|--------|
| Encapsulation | Good | Good | Poor |
| Multiple instances | Yes | Yes | No |
| Complexity | Low | Medium | Low |
| Use when | Simple state | Complex state | Avoid |
