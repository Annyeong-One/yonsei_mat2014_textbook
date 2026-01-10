# Shape, Strides, and Views

Understanding **shape**, **strides**, and **views** explains why NumPy slicing is fast and how memory is shared.

---

## 1. Shape

The shape describes array dimensions:

```python
a = np.zeros((3, 4))
a.shape   # (3, 4)
```

Changing shape (without copying):

```python
a.reshape((4, 3))
```

---

## 2. Strides

Strides describe how many bytes to step in memory when moving along each axis.

```python
a.strides
```

They allow NumPy to interpret the same memory in different ways.

---

## 3. Views vs copies

Many NumPy operations return **views**:

```python
b = a[:, :2]
```

- `b` shares memory with `a`
- modifying `b` modifies `a`

Check with:

```python
b.base is a
```

---

## 4. When copies occur

Copies occur when:
- dtype changes,
- memory layout must be contiguous,
- explicit `.copy()` is called.

---

## 5. Performance implications

Views:
- are cheap to create,
- save memory,
- enable fast slicing.

But shared memory requires care.

---

## Key takeaways

- Shape defines dimensions.
- Strides define memory layout.
- Slicing usually returns views, not copies.
