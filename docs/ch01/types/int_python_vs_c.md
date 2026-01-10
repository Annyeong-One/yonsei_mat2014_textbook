# `int`: Python vs C (Memory & Semantics)

Python integers (`int`) differ fundamentally from integers in low-level languages like C. Understanding this difference prevents many bugs and misconceptions.

---

## 1. Fixed-size vs arbitrary precision

### C integers
- Fixed size (e.g. 32-bit or 64-bit)
- Overflow wraps around or is undefined

```c
int x = INT_MAX;
x = x + 1;   // overflow
```

### Python integers
- Arbitrary precision
- No overflow (memory grows as needed)

```python
x = 10**100
print(x)
```

---

## 2. Memory representation

- C `int`: stored directly in a fixed number of bits
- Python `int`: object containing
  - sign
  - length
  - array of machine words

This makes Python `int`:
- slower than C `int`
- but mathematically safe

---

## 3. Semantics

Python integers obey **mathematical integer semantics**:
- exact arithmetic
- no overflow surprises

This is crucial for:
- financial calculations
- cryptography
- symbolic computation

---

## 4. Performance considerations

Because Python `int` is an object:
- arithmetic is slower than in C
- large integers cost more memory

For heavy numerical work, libraries like NumPy use fixed-size types internally.

---

## Key takeaways

- Python `int` has arbitrary precision.
- No overflow, but higher memory and CPU cost.
- Safer semantics than C for finance and math.
