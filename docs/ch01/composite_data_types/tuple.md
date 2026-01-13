# `tuple` and Immutability

A **tuple** is an ordered, immutable collection. Tuples are fundamental to Python's design and are widely used for safety and performance.

---

## Creating Tuples

```python
t = (1, 2, 3)
empty = ()
single = (42,)   # Comma required!
```

Without the comma, `(42)` is just an integer in parentheses.

### From Other Types

```python
tuple("hello")      # ('h', 'e', 'l', 'l', 'o')
tuple([1, 2, 3])    # (1, 2, 3)
tuple(range(5))     # (0, 1, 2, 3, 4)
```

### Implicit Construction (Packing)

Parentheses are optional:

```python
t = 1, 2, 3         # Same as (1, 2, 3)
print(type(t))      # <class 'tuple'>
```

---

## Indexing and Slicing

Same syntax as lists:

```python
t = (0, 1, 2, 3, 4, 5)
t[0]        # 0
t[-1]       # 5
t[1:4]      # (1, 2, 3) — returns tuple
t[::-1]     # (5, 4, 3, 2, 1, 0)
```

---

## Immutability

Tuples cannot be modified after creation:

```python
t = (1, 2, 3)
t[0] = 10   # TypeError: 'tuple' object does not support item assignment
t.append(4) # AttributeError: 'tuple' object has no attribute 'append'
```

### Referential vs Deep Immutability

Tuples can contain mutable objects:

```python
t = (1, [2, 3], 4)
t[1].append(5)      # Works! List inside is mutable
print(t)            # (1, [2, 3, 5], 4)

t[1] = [9, 9]       # TypeError: cannot reassign the reference
```

The tuple's **references** are immutable, but referenced **objects** may be mutable.

### The `+=` Edge Case

```python
t = (1, [2, 3])
t[1] += [4, 5]      # Raises TypeError, BUT list is still mutated!
print(t)            # (1, [2, 3, 4, 5])
```

This happens because `+=` first mutates the list, then tries to reassign (which fails).

---

## Packing and Unpacking

### Packing

Multiple values become a tuple:

```python
t = 1, 2, 3         # Packing into tuple
print(type(t))      # <class 'tuple'>

def get_stats():
    return 10, 20, 30   # Return values packed as tuple
```

### Unpacking

```python
t = (1, 2, 3)
a, b, c = t
print(a)            # 1
```

Works with any iterable:

```python
a, b, c, d, e = "hello"     # String
a, b, c = [1, 2, 3]         # List
a, b, c = {1, 2, 3}         # Set (order not guaranteed)
```

### Ignoring Values

```python
a, _, c = (1, 2, 3)           # Ignore middle
first, *rest = (1, 2, 3, 4)   # first=1, rest=[2, 3, 4]
first, *_, last = (1, 2, 3, 4, 5)  # first=1, last=5
_, *middle, _ = (1, 2, 3, 4, 5)    # middle=[2, 3, 4]
```

### Swap Idiom

Pythonic way to swap values:

```python
a, b = 1, 2
a, b = b, a         # Swap without temp variable
print(a, b)         # 2 1
```

This works because the right side is evaluated first (packed), then unpacked.

### Function Returns

```python
def get_point():
    return 10, 20       # Returns tuple

x, y = get_point()      # Unpack directly
```

---

## Tuple Methods

Tuples have only two methods:

```python
t = (1, 2, 2, 3, 2)
t.count(2)      # 3
t.index(3)      # 3 (first occurrence)
```

No mutating methods exist.

---

## Hashability

Tuples are hashable if all elements are hashable:

```python
t = (1, 2, 3)
hash(t)             # Works

t = (1, [2, 3])
hash(t)             # TypeError: unhashable type: 'list'
```

This makes tuples suitable as dictionary keys:

```python
locations = {
    (0, 0): "origin",
    (1, 2): "point A"
}
```

---

## Performance

| Aspect | Tuple | List |
|--------|-------|------|
| Memory | Less | More (over-allocation) |
| Creation | Faster | Slower |
| Access | Same | Same |
| Hashable | Yes* | No |

*If all elements are hashable.

---

## When to Use Tuples

| Use Case | Why Tuple |
|----------|-----------|
| Function return values | Natural unpacking |
| Dictionary keys | Hashable |
| Fixed records | Immutability guarantees |
| Thread-safe data | No mutation risk |
| Coordinates, RGB | Fixed structure |

---

## Tuple vs List Summary

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | ✅ | ❌ |
| Methods | Many | 2 (`count`, `index`) |
| Hashable | ❌ | ✅ (if elements are) |
| Memory | Higher | Lower |
| Dict key | ❌ | ✅ |
| Thread safe | ❌ | ✅ |

---

## Key Takeaways

- Tuples are immutable sequences
- Single-element tuple needs trailing comma: `(42,)`
- Contain mutable objects? References fixed, contents can change
- Hashable (if elements are) — use as dict keys
- Ideal for fixed records, function returns, coordinates
- Prefer tuples for read-only data (safer, faster, smaller)
