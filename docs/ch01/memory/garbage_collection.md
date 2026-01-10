# Reference Counting and Garbage Collection

Python manages memory automatically using **reference counting** combined with **garbage collection**.

---

## 1. Reference counting

Each object keeps a count of how many references point to it.

- Count increases when referenced.
- Count decreases when references are removed.
- When count reaches zero, object is deallocated.

---

## 2. Circular references

Reference counting alone cannot handle cycles:

```python
a = []
a.append(a)
```

The reference count never reaches zero.

---

## 3. Garbage collector

Python includes a cyclic garbage collector that:
- detects reference cycles,
- reclaims unreachable objects,
- runs periodically.

You usually don’t need to think about it.

---

## 4. Practical implications

- Deterministic deallocation is not guaranteed.
- Resource management uses context managers (`with`).
- Manual memory management is unnecessary.

---

## Key takeaways

- Python uses reference counting + GC.
- Cycles are handled automatically.
- Memory management is mostly invisible to users.
