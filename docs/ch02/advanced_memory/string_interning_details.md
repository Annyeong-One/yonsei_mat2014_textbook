# String Interning Details

## Auto Interning

### 1. Identifier-Like

```python
# Auto-interned
a = "hello"
b = "hello"
print(a is b)  # True
```

### 2. Not Identifier-Like

```python
# May not be interned
a = "hello world!"
b = "hello world!"
print(a is b)  # May be False
```

## Explicit Interning

### 1. sys.intern()

```python
import sys

s1 = sys.intern("any string!")
s2 = sys.intern("any string!")
print(s1 is s2)  # True
```

## Summary

- Auto for identifiers
- Explicit with sys.intern()
- Memory optimization
