# Immutable vs Mutable

## Immutable Objects

### 1. Cannot Change

```python
x = 42
s = "hello"
t = (1, 2, 3)

# Cannot modify
# s[0] = "H"        # TypeError
```

### 2. Create New

```python
x = 42
x = x + 1           # New object

s = "hello"
s = s + " world"    # New string
```

## Mutable Objects

### 1. Can Change

```python
lst = [1, 2, 3]
d = {'a': 1}
s = {1, 2, 3}

# Can modify
lst[0] = 100
d['b'] = 2
s.add(4)
```

### 2. Same Object

```python
lst = [1, 2, 3]
original_id = id(lst)

lst.append(4)
print(id(lst) == original_id)  # True
```

## Type Classification

### 1. Immutable

- int, float, str
- tuple, frozenset
- bytes, bool, None

### 2. Mutable

- list, dict, set
- bytearray
- User classes

## Hashability

### 1. Immutable Hashable

```python
d = {42: "int", "key": "str"}
s = {1, "two", (3, 4)}
```

### 2. Mutable Unhashable

```python
# Cannot use as dict key
# d[[1, 2]] = "bad"  # TypeError
```

## Default Arguments

### 1. Dangerous

```python
def bad(item, lst=[]):
    lst.append(item)
    return lst

print(bad(1))       # [1]
print(bad(2))       # [1, 2]  # Bug!
```

### 2. Safe

```python
def good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

## Summary

| Aspect | Immutable | Mutable |
|--------|-----------|---------|
| Change | No | Yes |
| Operations | New object | In-place |
| Hashable | Yes | No |
| Default arg | Safe | Danger |
