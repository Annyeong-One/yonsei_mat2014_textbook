# Locals Caveats

## Read-Only

### 1. Cannot Modify

```python
def function():
    locals()['x'] = 10
    # Doesn't create x!
```

### 2. Use Assignment

```python
def function():
    x = 10  # Correct way
```

## Inspection Only

Good for debugging, not for creating variables

## Summary

- locals() read-only
- Use normal assignment
- For inspection only
