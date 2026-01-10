# Performance vs Python Loops

Vectorization is the single most important performance concept in NumPy.

---

## 1. Python loops are slow

A pure Python loop:

```python
res = []
for i in range(n):
    res.append(a[i] + b[i])
```

This incurs:
- interpreter overhead,
- repeated attribute lookups,
- Python object creation.

---

## 2. Vectorized NumPy code

```python
res = a + b
```

This executes:
- in optimized C loops,
- with contiguous memory access,
- without Python-level iteration.

---

## 3. Orders of magnitude difference

Typical speedups:
- 10×–100× faster,
- even more for large arrays.

This is why NumPy is essential for numerical work.

---

## 4. Memory considerations

Vectorization may:
- allocate temporary arrays,
- increase peak memory usage.

Use in-place operations when appropriate:

```python
a += b
```

---

## 5. Practical guidance

- Avoid Python loops over arrays.
- Think in array operations.
- Profile before micro-optimizing.

---

## Key takeaways

- Python loops are slow for numeric work.
- NumPy vectorization is fast.
- Performance comes from moving work into C.
