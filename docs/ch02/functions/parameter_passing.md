# Parameter Passing

## Pass by Reference

### 1. All Pass by Reference

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
    x = [4, 5, 6]  # Local rebinding

data = [1, 2, 3]
rebind(data)
print(data)  # [1, 2, 3] (unchanged)
```

## Immutables

### 1. Cannot Modify

```python
def modify(x):
    x += 1  # Creates new int

value = 10
modify(value)
print(value)  # 10 (unchanged)
```

## Default Arguments

### 1. Mutable Defaults

```python
# Dangerous
def append(item, lst=[]):
    lst.append(item)
    return lst

# Safe
def append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Summary

- Pass by object reference
- Mutations visible
- Rebinding local only
- Watch mutable defaults
