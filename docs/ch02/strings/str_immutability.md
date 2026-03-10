# `str`: Immutability


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python strings are immutable: once created, their content cannot be changed.

---

## Core Concept

### 1. Fixed After Creation

A string's characters cannot be modified in place:

```python
a = "Hello Pi"
print(a[1])  # e

a[1] = "E"   # Attempt to modify
# TypeError: 'str' object does not support item assignment
```

### 2. Methods Return New

String methods create new objects, not modify originals:

```python
def main():
    s = "the brand has had its ups and downs."
    
    s.upper()  # Returns new string, doesn't modify s
    print(s)   # Still lowercase
    
    a = s.upper()  # Must capture the result
    print(a)       # THE BRAND HAS HAD ITS UPS AND DOWNS.

if __name__ == "__main__":
    main()
```

---

## Method Examples

### 1. Lowercase

```python
a = "Hello Pi"
print(a.lower())      # hello pi
print(str.lower(a))   # hello pi
print(a)              # Hello Pi (unchanged)
```

### 2. Uppercase

```python
a = "Hello Pi"
print(a.upper())      # HELLO PI
print(str.upper(a))   # HELLO PI
print(a)              # Hello Pi (unchanged)
```

### 3. Capitalize

```python
a = "hello pi"
print(a.capitalize())      # Hello pi
print(str.capitalize(a))   # Hello pi
print(a)                   # hello pi (unchanged)
```

---

## Reassignment

### 1. Explicit Assignment

To persist changes, reassign the variable:

```python
a = "Hello Pi"
a.upper()
print(a)   # Hello Pi (unchanged)

a = a.upper()
print(a)   # HELLO PI (now changed)
```

### 2. Slicing Example

```python
a = "PI"
a = a[::-1]
print(a)  # IP
```

---

## Why Immutable?

### 1. Memory Efficiency

Python can cache and reuse identical strings:

```python
a = "hello"
b = "hello"
print(a is b)  # True (same object)
```

### 2. Hashability

Immutable objects can be dictionary keys:

```python
d = {"hello": 1}  # Works because strings are immutable
```

### 3. Thread Safety

Immutable objects prevent race conditions:

```python
# Multiple threads can safely read the same string
# No synchronization needed
```

### 4. Predictability

No unintended side effects:

```python
def process(s):
    # Cannot accidentally modify caller's string
    return s.upper()

original = "hello"
result = process(original)
print(original)  # Still "hello"
```

---

## Key Takeaways

- Strings cannot be modified after creation.
- String methods return new objects.
- Must reassign to capture changes.
- Immutability enables caching and hashing.
