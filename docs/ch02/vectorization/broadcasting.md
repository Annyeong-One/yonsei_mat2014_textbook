# Broadcasting Rules

Broadcasting allows NumPy to perform elementwise operations on arrays of different shapes without explicit loops.

---

## 1. Motivation

Broadcasting avoids:
- manual reshaping,
- explicit Python loops,
- unnecessary memory copies.

It enables concise, high-performance code.

---

## 2. Basic idea

When operating on two arrays, NumPy compares shapes **from the trailing dimensions**.

Dimensions are compatible if:
- they are equal, or
- one of them is 1.

---

## 3. Example

```python
import numpy as np

a = np.ones((3, 4))
b = np.array([1, 2, 3, 4])

a + b   # b is broadcast across rows
```

Here, `b` behaves like shape `(1, 4)`.

---

## 4. More examples

```python
x = np.ones((5, 1))
y = np.ones((1, 3))
x + y   # result shape (5, 3)
```

---

## 5. Broadcasting errors

If shapes are incompatible:

```python
np.ones((3, 2)) + np.ones((3, 3))
```

NumPy raises a `ValueError`.

---

## Key takeaways

- Broadcasting aligns trailing dimensions.
- Size 1 dimensions can be expanded.
- Broadcasting avoids explicit loops.
