# String Interning


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## What Is Interning

### 1. Concept

Share memory for identical strings:

```python
s1 = "hello"
s2 = "hello"
print(s1 is s2)         # Often True
print(id(s1) == id(s2)) # Often True
```

### 2. Why Intern

```python
# Without interning:
names = ["hello"] * 1000
# 1000 separate objects

# With interning:
# All share one object
```

## CPython Rules

### 1. Identifier-Like

Automatically interned:

```python
# Identifier-like
s1 = "hello"
s2 = "hello"
print(s1 is s2)         # True

s1 = "hello_world"
s2 = "hello_world"
print(s1 is s2)         # True
```

### 2. Not Interned

```python
# Contains spaces/special chars
s1 = "hello world"
s2 = "hello world"
print(s1 is s2)         # May be False

s1 = "hello!"
s2 = "hello!"
print(s1 is s2)         # May be False
```

## Force Interning

### 1. sys.intern()

```python
import sys

# Force interning
s1 = sys.intern("hello world")
s2 = sys.intern("hello world")
print(s1 is s2)         # True
```

### 2. Use Case

```python
# Many duplicate strings
data = ["user_id"] * 10000

# Intern keys
data_interned = [
    sys.intern("user_id")
    for _ in range(10000)
]

# All same object
print(data_interned[0] is data_interned[9999])
```

## Best Practices

### 1. Never Rely On

```python
# Bad: assumes interning
def bad(s):
    if s is "hello":    # Don't!
        return True

# Good: use ==
def good(s):
    if s == "hello":    # Correct
        return True
```

### 2. Explicit Intern

```python
# When many duplicates
import sys

class Config:
    def __init__(self):
        self.USER_ID = sys.intern("user_id")
        
    def check(self, key):
        if key is self.USER_ID:  # Fast
            return "id"
```

## Summary

### 1. CPython

- Auto-interns identifier-like
- Can force with sys.intern()
- Performance optimization
- Not guaranteed by spec

### 2. Portable Code

```python
# Always use ==
if name == "admin":
    pass

# Never use is for strings
# except explicit interning
admin_key = sys.intern("admin")
if name is admin_key:   # OK
    pass
```
