# Time vs Space Trade-offs

Efficient programs balance **time complexity** and **space complexity**. Understanding this trade-off is essential for writing performant Python code.

---

## 1. Time complexity

Time complexity measures how execution time grows with input size.

Common classes:
- O(1): constant time
- O(log n): logarithmic
- O(n): linear
- O(n log n), O(n²): increasingly expensive

In Python, constant factors also matter.

---

## 2. Space complexity

Space complexity measures memory usage:
- stack usage (call frames),
- heap usage (objects, containers),
- temporary allocations.

Faster algorithms often use more memory.

---

## 3. Trade-offs in practice

Examples:
- caching results speeds up computation but uses memory,
- precomputing arrays avoids recomputation,
- vectorization trades memory for speed.

```python
# trade memory for speed
cache = {}
```

---

## 4. Financial computing perspective

In quantitative finance:
- latency matters in trading,
- memory matters in simulations,
- robustness matters more than micro-optimizations.

Choose trade-offs intentionally.

---

## Key takeaways

- Faster code often uses more memory.
- Python performance depends on algorithm choice.
- Optimize only after correctness.
