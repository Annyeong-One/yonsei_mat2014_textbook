# Call by Object Reference

## Python's Model

### 1. Pass Reference

```python
def modify(lst):
    lst.append(4)

data = [1, 2, 3]
modify(data)
print(data)  # [1, 2, 3, 4]
```

### 2. Rebinding Local

```python
def rebind(x):
    x = [4, 5, 6]

data = [1, 2, 3]
rebind(data)
print(data)  # [1, 2, 3]
```

## Summary

- Pass by object reference
- Mutations visible
- Rebinding local only
