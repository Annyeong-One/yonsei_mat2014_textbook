# Closure Debugging

## Inspection

### 1. View Closure

```python
def outer():
    x = 10
    return lambda: x

f = outer()
print(f.__closure__)
print(f.__code__.co_freevars)
```

### 2. Cell Contents

```python
print(f.__closure__[0].cell_contents)
```

## Common Issues

### 1. Late Binding

```python
# Check if all share cell
funcs = [lambda: i for i in range(3)]
cells = [f.__closure__[0] for f in funcs]
print(all(c is cells[0] for c in cells))
```

## Summary

- Use __closure__
- Check co_freevars
- Inspect cell_contents
