# list Copying

Understanding copy semantics is essential when working with mutable lists.

---

## The Aliasing Problem

Assignment creates a reference, not a copy:

```python
a = [1, 2, 3]
b = a           # b points to same object
a.append(4)
print(b)        # [1, 2, 3, 4]
```

```
a ─┬──► [1, 2, 3, 4]
   │
b ─┘
```

---

## Creating Copies

### Method 1: Slicing

```python
a = [1, 2, 3]
b = a[:]        # Shallow copy
a.append(4)
print(b)        # [1, 2, 3]
```

### Method 2: `copy()` method

```python
a = [1, 2, 3]
b = a.copy()    # Shallow copy
```

### Method 3: `list()` constructor

```python
a = [1, 2, 3]
b = list(a)     # Shallow copy
```

---

## Shallow vs Deep Copy

### Shallow Copy

Copies the list structure, but nested objects are still shared:

```python
a = [[1, 2], [3, 4]]
b = a.copy()          # Shallow copy

a[0][0] = 'X'
print(b)              # [['X', 2], [3, 4]]  (affected!)

a[0] = [9, 9]
print(b)              # [['X', 2], [3, 4]]  (not affected)
```

```
a ──► [ ref1, ref2 ]
         │      │
b ──► [ ref1, ref2 ]   (same inner refs)
         │      │
         ▼      ▼
      [1,2]  [3,4]
```

### Deep Copy

Recursively copies all nested objects:

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # Deep copy

a[0][0] = 'X'
print(b)              # [[1, 2], [3, 4]]  (unchanged)
```

---

## `+` vs `+=` Behavior

### `+` Creates New Object

```python
a = [1, 2, 3]
print(id(a))          # e.g., 140234567890

a = a + [4]
print(id(a))          # Different id (new object)
```

### `+=` Modifies In-Place

```python
a = [1, 2, 3]
print(id(a))          # e.g., 140234567890

a += [4]
print(id(a))          # Same id (same object)
```

This matters when other names reference the same list:

```python
a = [1, 2, 3]
b = a

a = a + [4]           # a is new object
print(b)              # [1, 2, 3] (b unchanged)

a = [1, 2, 3]
b = a

a += [4]              # a modified in-place
print(b)              # [1, 2, 3, 4] (b affected!)
```

---

## When to Use Which

| Scenario | Method |
|----------|--------|
| Simple list of immutables | `a[:]` or `a.copy()` |
| Nested lists/objects | `copy.deepcopy(a)` |
| Independent modification | Always copy first |

---

## Common Pitfall: Iterating While Modifying

```python
# Bug: skips elements
a = [1, 2, 3, 4]
for x in a:
    if x % 2 == 0:
        a.remove(x)
print(a)  # [1, 3] — but 4 was skipped!

# Fix: iterate over a copy
a = [1, 2, 3, 4]
for x in a[:]:        # a[:] is a copy
    if x % 2 == 0:
        a.remove(x)
print(a)  # [1, 3]

# Better: use list comprehension
a = [x for x in a if x % 2 != 0]
```

---

## Summary

| Method | Shallow | Deep | New Object |
|--------|---------|------|------------|
| `b = a` | ❌ | ❌ | ❌ (alias) |
| `b = a[:]` | ✅ | ❌ | ✅ |
| `b = a.copy()` | ✅ | ❌ | ✅ |
| `b = list(a)` | ✅ | ❌ | ✅ |
| `b = copy.deepcopy(a)` | ✅ | ✅ | ✅ |
