# LEGB Resolution

## Four Scopes

### 1. Local (L)

```python
def function():
    x = 10  # Local
```

### 2. Enclosing (E)

```python
def outer():
    x = 10  # Enclosing for inner
    def inner():
        print(x)
```

### 3. Global (G)

```python
x = 10  # Global

def function():
    print(x)
```

### 4. Built-in (B)

```python
# Always available
print(len([1, 2, 3]))
```

## Lookup Order

Searches: L → E → G → B

## Summary

- Four scope levels
- Specific lookup order
- First match wins
