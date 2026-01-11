# Array Creation and

NumPy’s core object is the **ndarray**, a homogeneous, fixed-size array designed for efficient numerical computation.

---

## Creating arrays from

The most common way to create an array is with `np.array`:

```python
import numpy as np

a = np.array([1, 2, 3])
```

All elements are stored with the same **dtype**.

---

## dtypes (data types)

A dtype specifies:
- how many bytes each element uses,
- how the bytes are interpreted.

Examples:
```python
np.array([1, 2, 3]).dtype        # int64 (platform-dependent)
np.array([1.0, 2.0]).dtype      # float64
```

You can specify a dtype explicitly:

```python
np.array([1, 2, 3], dtype=np.float64)
```

---

## Common array

NumPy provides efficient constructors:

```python
np.zeros((3, 4))
np.ones((2, 2))
np.empty((5,))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

These avoid Python loops and are highly optimized.

---

## Type promotion

NumPy promotes types automatically:

```python
np.array([1, 2.5])   # float array
```

Promotion follows fixed rules to preserve information.

---

## Financial computing

Choosing the right dtype matters for:
- memory usage,
- numerical precision,
- performance in large simulations.

---

## Key takeaways

- ndarrays store homogeneous data.
- dtypes control memory and precision.
- Use NumPy constructors for efficiency.
