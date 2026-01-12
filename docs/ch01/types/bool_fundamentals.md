# Boolean Basics

The `bool` type in Python represents binary logic values and is fundamental to conditional evaluation and control flow.

---

## Introduction

Python's boolean type encapsulates classical binary logic values essential for computational decision-making.

### 1. Two Values

Python has exactly two boolean values:

```python
a = True
print(a, type(a))

b = False
print(b, type(b))
```

### 2. Role in Logic

Boolean values serve as the backbone of:
- Conditional evaluation
- Control flow mechanisms
- Algorithmic decision-making
- Data validation protocols

### 3. Type Definition

```python
print(True)  # Represents logical truth
print(False) # Represents logical falsehood
```

---

## Typical Usage

Booleans are commonly used in loops and conditionals.

### 1. Range Iteration

```python
for i in range(7):
    print(i, type(i))
```

### 2. Odd Number Filter

```python
for i in range(7):
    if i % 2 == 1:
        print(i)
```

### 3. Even Number Filter

```python
for i in range(7):
    if i % 2 == 0:
        print(i)
```

### 4. Inline Output

```python
for i in range(7):
    if i % 2 == 1:
        print(i, end='\t')
```

---

## Conclusion

The `bool` type is foundational to Python, enabling logical inference and control structures across all programming paradigms.
