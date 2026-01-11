# Interning

## String Interning

### 1. Concept

Share identical strings in memory

```python
a = "hello"
b = "hello"
print(a is b)  # Usually True
```

### 2. Explicit Interning

```python
import sys

s1 = sys.intern("my string")
s2 = sys.intern("my string")
print(s1 is s2)  # True
```

## Integer Caching

### 1. Small Integers

```python
a = 256
b = 256
print(a is b)  # True

a = 257
b = 257
print(a is b)  # May be False
```

## Summary

- Strings auto-interned
- Small ints cached
- Memory optimization
