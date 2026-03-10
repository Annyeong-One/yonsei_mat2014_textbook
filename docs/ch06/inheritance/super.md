# `super()` Mechanics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `super()` function enables cooperative multiple inheritance by following the Method Resolution Order (MRO).

---

## What `super()` Does

### 1. Not Just Parent

`super()` doesn't call the "parent" class—it calls the **next class in MRO**.

```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        super().method()
        print("B")
```

### 2. MRO-Aware

```python
class D(B, C):
    def method(self):
        super().method()  # follows MRO, not just B
```

### 3. Dynamic Dispatch

The next class depends on the instance's type, not where `super()` appears.

---

## Cooperative Inheritance

### 1. All Use `super()`

```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()
```

### 2. Diamond Pattern

```python
class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()

d = D()
# Output:
# D init
# B init
# C init
# A init
```

### 3. Each Called Once

`super()` ensures each class in MRO is called exactly once.

---

## `super()` Syntax

### 1. Python 3 (Preferred)

```python
class Child(Parent):
    def method(self):
        super().method()  # automatic
```

### 2. Python 2 (Legacy)

```python
class Child(Parent):
    def method(self):
        super(Child, self).method()
```

### 3. No `self` Argument

```python
# Wrong
super().__init__(self, x, y)

# Correct
super().__init__(x, y)
```

---

## When to Use `super()`

### 1. Always in Hierarchies

Use `super()` in any inheritance hierarchy.

### 2. Multiple Inheritance

Essential for cooperative multiple inheritance.

### 3. Framework Design

Critical when designing extensible frameworks.

---

## Common Pitfalls

### 1. Forgetting `super()`

```python
class B(A):
    def __init__(self):
        # forgot super().__init__()
        self.b = "value"
```

Breaks the chain—`A.__init__` never runs.

### 2. Mixing Styles

```python
class B(A):
    def __init__(self):
        A.__init__(self)  # don't mix with super()
```

Use `super()` consistently throughout hierarchy.

### 3. Assuming Parent

```python
# super() calls next in MRO, not necessarily parent
class D(B, C):
    def method(self):
        super().method()  # might call C, not B!
```

---

## Advanced: MRO Flow

### 1. Simple Chain

```python
class A: pass
class B(A): pass
class C(B): pass

# MRO: C → B → A → object
```

### 2. Multiple Inheritance

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# MRO: D → B → C → A → object
```

### 3. `super()` Follows MRO

At each step, `super()` moves to the next class in this order.

---

## Key Takeaways

- `super()` follows MRO, not just parent.
- Use `super()` consistently in hierarchies.
- Never pass `self` to `super()`.
- Cooperative inheritance requires all classes use `super()`.
