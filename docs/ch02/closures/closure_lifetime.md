# Closure Lifetime

## Object Persistence

### 1. Outlives Enclosing

```python
def outer():
    x = [1, 2, 3]
    
    def inner():
        return x
    
    return inner
    # outer frame destroyed
    # but x persists for inner

f = outer()
print(f())  # [1, 2, 3] - still accessible
```

### 2. Reference Keeps Alive

```python
def outer():
    data = [1, 2, 3]
    
    def inner():
        return data
    
    return inner

f = outer()
# 'data' kept alive by closure
# Won't be garbage collected
```

## Shared Closures

### 1. Multiple Functions

```python
def outer():
    x = 0
    
    def inc():
        nonlocal x
        x += 1
        return x
    
    def get():
        return x
    
    return inc, get

inc, get = outer()
inc()
inc()
print(get())  # 2
# Both share same x
```

### 2. Same Cell

```python
def outer():
    x = 10
    
    f1 = lambda: x
    f2 = lambda: x
    
    return f1, f2

a, b = outer()
# Both reference same cell
print(a.__closure__[0] is b.__closure__[0])  # True
```

## Memory Impact

### 1. Keeps Objects Alive

```python
def make_handler():
    # Large object
    large_data = [0] * 1000000
    
    def handler():
        # Even if only uses len
        return len(large_data)
    
    return handler
    # large_data kept alive!

h = make_handler()
# Entire large_data in memory
```

### 2. Memory Leak Risk

```python
# Careful with large captures
def outer():
    huge_list = list(range(1000000))
    
    def inner():
        return huge_list[0]  # Only needs first
    
    return inner
    # Entire list kept alive
```

## Cleanup

### 1. Delete Reference

```python
def outer():
    x = [1, 2, 3]
    return lambda: x

f = outer()
print(f())  # Works

del f  # Remove closure
# Now x can be GC'd
```

### 2. Break Cycles

```python
def outer():
    x = []
    
    def inner():
        return x
    
    x.append(inner)  # Cycle!
    return inner

# Cycle: inner -> x -> inner
# Needs cycle GC
```

## Best Practices

### 1. Minimize Capture

```python
# Bad: captures everything
def make_processor():
    config = load_config()
    data = load_data()
    
    def process():
        # Only uses config
        return config['key']
    
    return process  # data also captured!

# Better: explicit
def make_processor():
    config = load_config()
    key = config['key']
    
    def process():
        return key  # Only captures key
    
    return process
```

### 2. Clear Intent

```python
# Explicit capture
def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
```

## Summary

### 1. Lifetime

- Closure keeps variables alive
- Outlives enclosing function
- Multiple closures can share
- Deleted when closure deleted

### 2. Watch Out

- Memory leaks
- Large captures
- Circular references
