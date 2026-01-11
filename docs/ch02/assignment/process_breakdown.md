# Process Breakdown

## Assignment Steps

### 1. Evaluate RHS

```python
x = 2 + 3
# 1. Evaluate 2 + 3 → 5
# 2. Bind x to 5
```

### 2. Create Binding

```python
# Namespace updated
x = 42  # locals()['x'] = 42
```

## Summary

- Evaluate right side first
- Then bind name
- Update namespace
