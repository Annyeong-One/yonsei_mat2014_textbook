# Method Resolution Order


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The **Method Resolution Order (MRO)** defines how Python resolves methods in inheritance hierarchies, especially with multiple inheritance.

---

## Why MRO Exists

### 1. Ambiguity Problem

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
d.method()  # Which method?
```

### 2. Diamond Problem

```python
    A
   / \
  B   C
   \ /
    D
```

When `D` inherits from both `B` and `C`, which inherit from `A`, how should methods resolve?

### 3. Deterministic Order

MRO provides a consistent, predictable resolution order.

---

## Inspecting MRO

### 1. Using `.mro()`

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())
# [<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

### 2. Using `__mro__`

```python
print(D.__mro__)
# Same output as .mro()
```

### 3. Reading the Order

Methods are searched left to right through this list.

---

## MRO Principles

### 1. Child First

The class itself is always first in MRO.

### 2. Left-to-Right

Parents are searched in declaration order.

```python
class D(B, C):  # B before C
    pass
```

### 3. Parents Before Ancestors

A parent appears before its own parents.

```python
# D → B → C → A
# B appears before A
# C appears before A
```

---

## C3 Linearization

### 1. Algorithm Used

Python uses C3 linearization to compute MRO.

### 2. Three Properties

- Preserves local precedence order
- Maintains parent MRO
- Ensures monotonicity

### 3. Consistency

Guarantees a consistent resolution order or raises an error.

---

## MRO and `super()`

### 1. `super()` Follows MRO

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        super().method()  # calls next in MRO
        print("B")
```

### 2. Cooperative Calls

```python
class D(B, C):
    def method(self):
        super().method()  # calls B.method
        # B.method calls super() → C.method
        # C.method calls super() → A.method
```

### 3. Each Class Once

Even in diamond inheritance, each class is called exactly once.

---

## Invalid MRO

### 1. Inconsistent Hierarchy

```python
class X: pass
class Y: pass

class A(X, Y): pass
class B(Y, X): pass  # reversed order

class C(A, B): pass  # Error!
```

### 2. TypeError Raised

```plaintext
TypeError: Cannot create a consistent method resolution order (MRO)
```

### 3. Fix the Design

Rearrange inheritance to be consistent.

---

## Practical Advice

### 1. Single Inheritance

Prefer single inheritance when possible—simpler MRO.

### 2. Understand Your MRO

Always check `.mro()` in complex hierarchies.

### 3. Use `super()` Consistently

Design all classes to work cooperatively.

### 4. Avoid Deep Hierarchies

Keep inheritance shallow for maintainability.

---

## Key Takeaways

- MRO defines method lookup order.
- Python uses C3 linearization algorithm.
- `.mro()` reveals the resolution order.
- `super()` follows MRO, not just parent.
- Invalid hierarchies raise `TypeError`.
