# Assignment vs Mutation

Understanding the difference between rebinding a name and modifying an object.

## Assignment (Rebinding)

Assignment creates a new binding from a name to an object:

```python
x = [1, 2, 3]
print(id(x))  # 140234567890

x = [4, 5, 6]  # New binding - different object
print(id(x))  # 140234567999 (different!)
```

The original list `[1, 2, 3]` still exists (until garbage collected), but `x` no longer refers to it.

## Mutation (In-Place Modification)

Mutation modifies the object itself:

```python
x = [1, 2, 3]
print(id(x))  # 140234567890

x.append(4)   # Same object, modified
print(id(x))  # 140234567890 (same!)
print(x)      # [1, 2, 3, 4]
```

## Visual Comparison

```
Assignment (x = [4, 5, 6]):
    Before: x ──→ [1, 2, 3]
    After:  x ──→ [4, 5, 6]
            (old list orphaned)

Mutation (x.append(4)):
    Before: x ──→ [1, 2, 3]
    After:  x ──→ [1, 2, 3, 4]
            (same list, modified)
```

## Why It Matters: Aliasing

When two names refer to the same object, mutation affects both:

```python
a = [1, 2, 3]
b = a  # b refers to same object

b.append(4)  # Mutation
print(a)     # [1, 2, 3, 4] - a sees the change!

b = [5, 6, 7]  # Assignment (rebinding)
print(a)       # [1, 2, 3, 4] - a unchanged
```

## Augmented Assignment

Augmented assignment (`+=`, `-=`, etc.) behaves differently for mutable vs immutable types:

### Mutable (list) - Mutation

```python
x = [1, 2]
y = x

x += [3, 4]  # Modifies in place (x.__iadd__)
print(y)     # [1, 2, 3, 4] - y sees change
print(x is y)  # True
```

### Immutable (int, str, tuple) - Rebinding

```python
x = 10
y = x

x += 5  # Creates new int, rebinds x
print(y)  # 10 - y unchanged
print(x is y)  # False
```

---

## Assignment Examples

### Simple Assignment

```python
x = 42
name = "Alice"
pi = 3.14159
```

### Multiple Assignment (Unpacking)

```python
a, b, c = 1, 2, 3
x, y = "hello", "world"
```

### Chained Assignment

```python
x = y = z = 0
# All three refer to the same object
print(x is y is z)  # True
```

### Swap Values

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20, 10
```

### Assignment with Expression

```python
result = (x + y) * z
count = len(items) if items else 0
```

### Attribute Assignment

```python
class Point:
    pass

p = Point()
p.x = 10  # Assigns to object attribute
p.y = 20
```

### Index/Slice Assignment

```python
lst = [1, 2, 3, 4, 5]
lst[0] = 10        # Index assignment
lst[1:3] = [20, 30]  # Slice assignment
```

---

## Common Patterns

### Initialize Multiple Variables

```python
# Same value
x = y = z = 0

# Different values
x, y, z = 0, 0, 0
```

### Conditional Assignment

```python
# Ternary
result = value if condition else default

# Or pattern (for falsy defaults)
name = user_input or "Anonymous"
```

### Increment/Decrement

```python
count = 0
count += 1  # Increment
count -= 1  # Decrement
```

---

## Summary

| Operation | Effect | Example |
|-----------|--------|---------|
| Assignment | New binding | `x = [1, 2]` |
| Mutation | Modify object | `x.append(3)` |
| Augmented (mutable) | Mutation | `x += [3]` on list |
| Augmented (immutable) | Rebinding | `x += 1` on int |

Key points:
- Assignment changes what a name refers to
- Mutation changes the object itself
- Aliased names share mutations
- Augmented assignment depends on mutability
