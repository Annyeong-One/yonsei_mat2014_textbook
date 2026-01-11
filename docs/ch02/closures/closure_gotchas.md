# Closure Gotchas

## Late Binding

### 1. Loop Problem

```python
# Wrong
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2]

# Right
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)

print([f() for f in funcs])  # [0, 1, 2]
```

## Memory Leaks

### 1. Large Captures

```python
# Bad: captures entire object
def process_data():
    data = load_large_file()  # 1GB
    
    def get_first():
        return data[0]  # Only needs first item
    
    return get_first  # Keeps entire 1GB!

# Better
def process_data():
    data = load_large_file()
    first = data[0]
    
    def get_first():
        return first  # Only keeps first item
    
    return get_first
```

## Circular References

### 1. Self Reference

```python
def outer():
    items = []
    
    def inner():
        return items
    
    items.append(inner)  # Cycle!
    return inner

# inner -> items -> inner
```

## Summary

Watch for:
- Late binding in loops
- Large object captures
- Circular references
- Unexpected mutations
