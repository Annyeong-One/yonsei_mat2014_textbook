# Pythonic Idioms

## EAFP

### 1. Easier to Ask Forgiveness

```python
# Pythonic
try:
    value = d[key]
except KeyError:
    value = default

# vs LBYL
if key in d:
    value = d[key]
else:
    value = default
```

## Context Managers

### 1. Resource Management

```python
with open('file.txt') as f:
    data = f.read()
```

## Comprehensions

### 1. Concise

```python
# Pythonic
squares = [x**2 for x in range(10)]

# vs
squares = []
for x in range(10):
    squares.append(x**2)
```

## Summary

- EAFP over LBYL
- Use context managers
- Prefer comprehensions
