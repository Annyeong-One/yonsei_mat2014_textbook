# Debugging Tools

## Inspect Closure

### 1. __closure__

```python
def outer():
    x = 10
    return lambda: x

f = outer()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
```

## Code Object

### 1. co_freevars

```python
print(f.__code__.co_freevars)  # ('x',)
```

## Summary

- Use __closure__
- Check co_freevars
- Inspect cell_contents
