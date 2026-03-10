# Comparisons


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides relational operators that return boolean values for comparing objects.

---

## Relational Operators

Basic comparison operators return boolean results.

### 1. Greater Than

```python
print(10 > 5)    # Output: True
```

### 2. Equality

```python
print(10 == 10)  # Output: True
```

### 3. Inequality

```python
print(10 != 5)   # Output: True
```

### 4. Less Than

```python
print(10 < 5)    # Output: False
```

---

## Chained Comparisons

Python allows chained comparisons for improved readability.

### 1. Basic Chaining

```python
print(1 < 2 < 3)  # Equivalent to: (1 < 2) and (2 < 3) → True
```

### 2. Mixed Operators

```python
print(1 < 2 > 3)  # Equivalent to: (1 < 2) and (2 > 3) → False
```

### 3. Readability

Chained comparisons reduce verbosity and improve code clarity.

---

## Equality vs Identity

Understanding the difference between `==` and `is`.

### 1. == Operator

The `==` operator checks whether values are equal.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (content is the same)
```

### 2. is Operator

The `is` operator checks if two variables refer to the same object in memory.

```python
x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)  # Output: False (different objects)
```

### 3. Basic Example

```python
def main():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)  # Output: True (content is the same)

    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x is y)  # Output: False (different objects)

if __name__ == "__main__":
    main()
```

### 4. Key Difference

- `==`: Compares **values** (content)
- `is`: Compares **identity** (memory address)

### 5. When to Use

Use `==` for value comparison. Use `is` for:
- Checking for `None`
- Checking if two variables refer to the exact same object

---

## Integer Caching

Python caches small integers for optimization.

### 1. Small Integer

```python
def main():
    a = 256
    b = 256
    print(a is b)  # Output: True (cached)

if __name__ == "__main__":
    main()
```

### 2. List Container

```python
def main():
    a = [256]
    b = [256]
    print(a is b)  # Output: False (different list objects)

if __name__ == "__main__":
    main()
```

[Reel from instagram](https://www.instagram.com/reel/C3aULcRNa5G/?igsh=MWdidnA2NGF3bGoyMA==)

---

## Best Practices

Guidelines for comparison operations.

### 1. Value Comparison

Use `==` when comparing values or content.

### 2. Identity Check

Use `is` specifically for `None` checks:

```python
if x is None:
    print("x is None")
```

### 3. Avoid with None

Never use `==` for `None` comparison:

```python
# Bad
if x == None:
    pass

# Good
if x is None:
    pass
```

---

## Conclusion

Understanding the distinction between `==` (value equality) and `is` (identity) is crucial for writing correct Python code. Chained comparisons provide elegant syntax for range checking and multiple condition evaluation.
