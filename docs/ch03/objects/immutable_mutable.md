# Immutable vs Mutable


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

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

### 3. Reference Sharing

When two names point to the same mutable object:

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4]
```

```
Before:
a ─┬──► [1, 2, 3]
   │
b ─┘

After a.append(4):
a ─┬──► [1, 2, 3, 4]
   │
b ─┘
```

### 4. Immutable Rebinding

```python
a = 10
b = a
b += 1
print(a)  # 10 (unchanged)
```

```
Before:
a ─┬──► 10
   │
b ─┘

After b += 1:
a ───► 10

b ───► 11  (new object)
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

### 3. Shallow Immutability

Tuples containing mutable objects are **not hashable**:

```python
t = (1, [2, 3])      # Tuple with list inside
hash(t)              # TypeError: unhashable type: 'list'
```

The tuple is immutable (can't reassign `t[1]`), but the list inside can change.


## Operations That Create New Objects

Even with mutable types, some operations create new objects:

```python
lst = [1, 2, 3]
print(id(lst))

# In-place (same object)
lst.append(4)
lst.sort()
print(id(lst))       # Same id

# Creates new object
lst = lst + [5]
print(id(lst))       # Different id!

lst = sorted(lst)
print(id(lst))       # Different id!

lst = [x for x in lst]
print(id(lst))       # Different id!
```

| Operation | Same Object? |
|-----------|--------------|
| `lst.append(x)` | ✅ Yes |
| `lst.sort()` | ✅ Yes |
| `lst += [x]` | ✅ Yes |
| `lst = lst + [x]` | ❌ No |
| `lst = sorted(lst)` | ❌ No |
| `lst = [x for x in lst]` | ❌ No |

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
