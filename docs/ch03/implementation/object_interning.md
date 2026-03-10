# Object Interning


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python optimizes memory usage by reusing identical immutable objects through interning and caching.

## String Interning

### Concept

String interning shares identical strings in memory, reducing memory usage and enabling fast identity comparisons.

```python
a = "hello"
b = "hello"
print(a is b)  # True (same object)
print(id(a) == id(b))  # True
```

### Auto-Interning Rules

Python automatically interns strings that look like identifiers:

```python
# Auto-interned (identifier-like)
a = "hello"
b = "hello"
print(a is b)  # True

a = "hello_world"
b = "hello_world"
print(a is b)  # True
```

Strings with spaces or special characters may not be auto-interned:

```python
# May not be interned
a = "hello world!"
b = "hello world!"
print(a is b)  # May be False
print(a == b)  # Always True (same value)
```

### Explicit Interning

Use `sys.intern()` to force interning:

```python
import sys

s1 = sys.intern("any string with spaces!")
s2 = sys.intern("any string with spaces!")
print(s1 is s2)  # True (forced interning)
```

### When to Use Explicit Interning

```python
import sys

# Useful for repeated string comparisons
keys = [sys.intern(key) for key in many_keys]

# Fast identity check instead of value comparison
if key is interned_key:  # Faster than key == interned_key
    pass
```

---

## Integer Caching

### CPython Caching Range

CPython caches small integers in the range **[-5, 256]**:

```python
# Cached integers
a = 100
b = 100
print(a is b)  # True (same cached object)

a = 256
b = 256
print(a is b)  # True (still cached)

# Non-cached integers
a = 257
b = 257
print(a is b)  # May be False (different objects)
print(a == b)  # True (same value)

a = -6
b = -6
print(a is b)  # May be False
```

### Why This Range?

Small integers are used frequently in programs (loop counters, indices, etc.), so caching them:
- Reduces memory usage
- Improves performance
- Avoids repeated object creation

### Important Warning

**Never rely on integer caching for logic!**

```python
# WRONG - Don't do this
if x is 100:  # May not work as expected
    pass

# CORRECT - Always use ==
if x == 100:  # Always works correctly
    pass
```

---

## Other Cached Objects

### Singletons

```python
# None, True, False are singletons
a = None
b = None
print(a is b)  # Always True

a = True
b = True
print(a is b)  # Always True
```

### Empty Immutables

```python
# Empty tuple is cached
a = ()
b = ()
print(a is b)  # True

# Empty frozenset is cached
a = frozenset()
b = frozenset()
print(a is b)  # True
```

---

## Summary

| Type | Interning/Caching | Range/Condition |
|------|-------------------|-----------------|
| Strings | Auto/Explicit | Identifier-like / `sys.intern()` |
| Integers | Auto | [-5, 256] |
| None | Always | Singleton |
| True/False | Always | Singletons |
| Empty tuple | Auto | `()` |

Key points:
- Interning saves memory by sharing objects
- Use `==` for value comparison, `is` for identity
- Don't rely on caching in program logic
- Use `sys.intern()` for explicit string interning
- Caching is an implementation detail, not guaranteed
