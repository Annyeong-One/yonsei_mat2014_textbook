# LEGB Rule

## Four Scopes

### 1. Local (L)

```python
def function():
    x = 10  # Local
    print(x)
```

### 2. Enclosing (E)

```python
def outer():
    x = 10  # Enclosing for inner
    
    def inner():
        print(x)  # Access enclosing
    
    inner()
```

### 3. Global (G)

```python
x = 10  # Global

def function():
    print(x)  # Access global
```

### 4. Built-in (B)

```python
# Built-ins always available
print(len([1, 2, 3]))
```

## Lookup Order

### 1. LEGB Chain

```python
x = "builtin"  # (hypothetically)
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # "local"
    
    inner()

# Searches: Local → Enclosing → Global → Builtin
```

### 2. First Match

```python
x = "global"

def function():
    # No local x
    print(x)  # Uses global

function()
```

## Summary

- L: Local scope
- E: Enclosing scope
- G: Global scope
- B: Built-in scope
- Lookup order: L → E → G → B
