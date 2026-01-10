# Method Resolution

The **Method Resolution Order (MRO)** defines how Python resolves methods in multiple inheritance.

---

## Why MRO exists

Multiple inheritance can create ambiguity:
```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...
```

Which method should be used?

---

## C3 linearization

Python uses **C3 linearization** to compute MRO:
- preserves local precedence,
- ensures monotonicity,
- avoids ambiguity.

---

## Inspecting MRO

```python
D.mro()
```

This returns the order in which classes are searched.

---

## Practical advice

- Prefer single inheritance when possible.
- Use MRO-aware designs.
- Always use `super()`.

---

## Key takeaways

- MRO defines method lookup order.
- Python uses C3 linearization.
- `mro()` helps debugging inheritance issues.
