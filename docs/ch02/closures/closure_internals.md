# Closure Internals

## Scope Chain

### Nested Scopes

```python
def level1():
    x = 1
    
    def level2():
        y = 2
        
        def level3():
            z = 3
            return x + y + z  # Can access x, y, z
        
        return level3
    
    return level2

f = level1()()
print(f())  # 6
```

### Lookup Order (LEGB)

```python
x = "global"

def level1():
    x = "level1"
    
    def level2():
        x = "level2"
        
        def level3():
            # Looks in: level3 -> level2 -> level1 -> global
            print(x)  # "level2"
        
        level3()
    
    level2()
```

### Skipping Levels

```python
def outer():
    x = 10
    
    def middle():
        # No x here
        
        def inner():
            return x  # Skips middle, uses outer's x
        
        return inner
    
    return middle()

f = outer()
print(f())  # 10
```

### Shadowing

```python
def outer():
    x = "outer"
    
    def middle():
        x = "middle"  # Shadows outer's x
        
        def inner():
            print(x)  # "middle"
        
        inner()
    
    middle()
```

### nonlocal Resolution

```python
def level1():
    x = 1
    
    def level2():
        x = 2
        
        def level3():
            nonlocal x  # Modifies level2's x (closest)
            x = 3
        
        level3()
        print(x)  # 3
    
    level2()
    print(x)  # 1 (unchanged)
```

---

## Closure Lifetime

### Outlives Enclosing Function

```python
def outer():
    x = [1, 2, 3]
    
    def inner():
        return x
    
    return inner
    # outer's frame is destroyed
    # but x persists for inner

f = outer()
print(f())  # [1, 2, 3] - still accessible
```

### Shared Cells

Multiple closures from the same enclosing function share the same cell:

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
print(get())  # 2 — both share same x
```

```python
def outer():
    x = 10
    
    f1 = lambda: x
    f2 = lambda: x
    
    return f1, f2

a, b = outer()
print(a.__closure__[0] is b.__closure__[0])  # True — same cell
```

### Cleanup

```python
def outer():
    x = [1, 2, 3]
    return lambda: x

f = outer()
print(f())  # Works

del f  # Remove closure reference
# Now x can be garbage collected
```

---

## Memory Considerations

### Closures Keep Objects Alive

```python
def make_handler():
    large_data = [0] * 1_000_000  # Large object
    
    def handler():
        return len(large_data)  # Only uses len
    
    return handler
    # Entire large_data kept alive!

h = make_handler()
# 1 million integers still in memory
```

### Memory Leak Risk

```python
def outer():
    huge_list = list(range(1_000_000))
    
    def inner():
        return huge_list[0]  # Only needs first element
    
    return inner
    # Entire list kept alive, not just first element
```

### Circular References

```python
def outer():
    x = []
    
    def inner():
        return x
    
    x.append(inner)  # Cycle: inner -> x -> inner
    return inner

# Requires cycle garbage collector
```

---

## Performance

### Cell Access Overhead

```python
# Slower: cell lookup required
def outer():
    x = 10
    return lambda: x

# Faster: direct local access
def function():
    x = 10
    return x
```

The difference is usually negligible, but can matter in tight loops.

### Unnecessary Captures

```python
# Bad: captures variables not used in closure body
def outer():
    a, b, c = 1, 2, 3
    return lambda: a  # b, c may also be kept alive

# Better: only define what's needed
def outer():
    a = 1
    return lambda: a
```

---

## Best Practices

### Minimize Captured Variables

```python
# Bad: captures entire config and data
def make_processor():
    config = load_config()
    data = load_data()
    
    def process():
        return config['key']  # Only uses one key
    
    return process  # data also kept alive!

# Better: capture only what's needed
def make_processor():
    config = load_config()
    key = config['key']  # Extract just what's needed
    
    def process():
        return key
    
    return process
```

### Make Intent Clear

```python
def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
```

---

## Inspection

### View Closure Cells

```python
def outer():
    x = 1
    y = 2
    
    def inner():
        return x + y
    
    return inner

f = outer()

# Inspect closure
print(f.__closure__)  # (<cell ...>, <cell ...>)
print(f.__code__.co_freevars)  # ('x', 'y')

for var, cell in zip(f.__code__.co_freevars, f.__closure__):
    print(f"{var} = {cell.cell_contents}")
# x = 1
# y = 2
```

---

## Summary

| Aspect | Key Points |
|--------|------------|
| **Scope chain** | Lookup goes Local → Enclosing → Global → Builtin |
| **Lifetime** | Closures keep captured variables alive beyond enclosing function |
| **Shared cells** | Multiple closures from same function share the same cell |
| **Memory** | Entire captured objects stay alive, not just used parts |
| **Performance** | Cell access has slight overhead; minimize captures |
| **Best practice** | Capture only what's needed; avoid large objects |
