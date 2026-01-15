# Identity and Equality

Understanding the difference between `is` (identity) and `==` (equality) operators.

## Identity (`is`)

The `is` operator checks if two names refer to the **same object** in memory:

```python
a = [1, 2, 3]
b = a

print(a is b)  # True (same object)
print(id(a) == id(b))  # True (same id)
```

### Different Objects

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False (different objects)
print(id(a))   # 140234567890
print(id(b))   # 140234567999
```

Even though `a` and `b` have the same values, they are different objects in memory.

## Equality (`==`)

The `==` operator checks if two objects have the **same value**:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (same values)
print(a is b)  # False (different objects)
```

## When to Use Each

### Use `is` for Singletons

```python
# For None
if x is None:
    print("x is None")

if x is not None:
    print("x has a value")

# For True/False (rare, but valid)
if flag is True:
    pass

if flag is False:
    pass
```

### Use `==` for Values

```python
# For comparing values
if x == 42:
    pass

if name == "Alice":
    pass

if items == [1, 2, 3]:
    pass
```

## Common Pitfall: Integer Caching

Python caches small integers (-5 to 256), which can cause confusion:

```python
# Small integers are cached
a = 256
b = 256
print(a is b)  # True (cached)

# Large integers are not
a = 257
b = 257
print(a is b)  # False (different objects)
print(a == b)  # True (same value)
```

**Rule**: Always use `==` for comparing values, even integers.

## String Interning

Similar caching happens with some strings:

```python
a = "hello"
b = "hello"
print(a is b)  # True (interned)

a = "hello world!"
b = "hello world!"
print(a is b)  # May be False
print(a == b)  # True (same value)
```

---

## Special Cases

### Augmented Assignment

Augmented assignment behaves differently based on mutability:

```python
# Mutable: modifies in place
x = [1, 2]
y = x
x += [3, 4]
print(x is y)  # True (same object)

# Immutable: creates new object
x = 10
y = x
x += 5
print(x is y)  # False (different objects)
```

### None Comparison

Always use `is` for `None`:

```python
# Correct
if result is None:
    pass

# Incorrect (works but not recommended)
if result == None:
    pass
```

### Boolean Context

For boolean checks, often no comparison needed:

```python
# Instead of
if flag == True:
    pass

# Prefer
if flag:
    pass

# Instead of
if len(items) == 0:
    pass

# Prefer
if not items:
    pass
```

---

## Summary Table

| Operator | Checks | Use For | Example |
|----------|--------|---------|---------|
| `is` | Identity (same object) | `None`, singletons | `x is None` |
| `==` | Equality (same value) | Values, objects | `x == 42` |
| `is not` | Not same object | `None` check | `x is not None` |
| `!=` | Not same value | Value comparison | `x != 0` |

## Key Takeaways

- `is` checks if two names point to the **same object**
- `==` checks if two objects have the **same value**
- Use `is` for `None`, `True`, `False`
- Use `==` for all value comparisons
- Don't rely on integer/string caching
- Identity implies equality, but not vice versa
