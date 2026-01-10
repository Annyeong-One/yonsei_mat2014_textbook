# `float`: IEEE 754 and Precision

Python `float` implements the IEEE 754 double-precision floating-point standard. This has important consequences for numerical accuracy.

---

## 1. What is IEEE 754?

Python `float` is:
- 64-bit double precision
- binary floating-point
- approximate, not exact

Structure:
- 1 sign bit
- 11 exponent bits
- 52 mantissa bits

---

## 2. Representation error

Many decimal numbers cannot be represented exactly:

```python
0.1 + 0.2
# 0.30000000000000004
```

This is **not a bug**, but a consequence of binary representation.

---

## 3. Equality pitfalls

Avoid direct equality checks:

```python
x = 0.1 + 0.2
x == 0.3   # False
```

Use tolerances instead:

```python
abs(x - 0.3) < 1e-9
```

---

## 4. Financial implications

Floating-point issues matter for:
- pricing
- risk aggregation
- iterative algorithms

For exact decimal arithmetic, consider:
- `decimal.Decimal`
- integer-based representations (e.g. cents)

---

## Key takeaways

- Python `float` is approximate.
- Decimal fractions are often inexact.
- Always compare floats with tolerances.
