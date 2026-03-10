# `str`: Python vs C


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python strings differ fundamentally from C strings in storage, safety, and semantics.

---

## C Strings

### 1. Null Termination

C strings are character arrays terminated by `\0`:

```c
char str[] = "Hello";  // Actually 6 bytes: H e l l o \0
```

This leads to:

- Buffer overflow vulnerabilities
- Manual length tracking required
- Undefined behavior on missing null

### 2. No Length Storage

C has no built-in string length:

```c
// Must scan for null terminator
size_t len = strlen(str);
```

---

## Python Strings

### 1. Explicit Length

Python stores length explicitly, no null terminator:

```python
s = "Hello, world!"
length = len(s)
print("Length of the string:", length)  # 13
```

### 2. Object-Based

Python strings are immutable objects:

```python
s = "finance"
print(len(s))   # 7
print(type(s))  # <class 'str'>
```

---

## Immutability

### 1. Cannot Modify

Strings cannot be changed in place:

```python
s = "abc"
# s[0] = "A"  # TypeError: 'str' does not support item assignment
s = "A" + s[1:]  # Create new string instead
```

### 2. Benefits

Immutability enables:

- Thread safety
- Use as dictionary keys
- Efficient string interning
- Predictable behavior

---

## Unicode Support

### 1. Native Unicode

Python handles Unicode naturally:

```python
s = "π ≈ 3.14"
print(s)  # π ≈ 3.14
```

### 2. International Text

```python
# Multiple scripts in one string
text = "Hello 世界 مرحبا"
print(len(text))  # Character count, not bytes
```

---

## Comparison Table

| Feature | C | Python |
|---------|---|--------|
| Termination | Null byte | Length stored |
| Mutability | Mutable | Immutable |
| Unicode | Manual | Native |
| Safety | Buffer risks | Safe |
| Length | `strlen()` | `len()` |

---

## Key Takeaways

- Python strings store length explicitly.
- No null terminator needed in Python.
- Immutability provides safety and hashability.
- Unicode support is built-in.
