# Positional-Only Parameters

## Syntax (Python 3.8+)

### 1. Before /

```python
def function(a, b, /, c, d):
    return a + b + c + d

# a, b must be positional
function(1, 2, 3, 4)        # OK
function(1, 2, c=3, d=4)    # OK
# function(a=1, b=2, c=3, d=4)  # Error
```

## Use Cases

### 1. Implementation Freedom

```python
def process(data, /):
    # Can rename 'data' without breaking API
    pass
```

### 2. Prevent Misuse

```python
def divmod(a, b, /):
    # Clear which is dividend/divisor
    return a // b, a % b
```

## Combined

### 1. All Types

```python
def function(pos_only, /, pos_or_kw, *, kw_only):
    pass

function(1, 2, kw_only=3)           # OK
function(1, pos_or_kw=2, kw_only=3) # OK
```

## Summary

- Python 3.8+ feature
- Use / to mark boundary
- Implementation flexibility
- Clearer APIs
