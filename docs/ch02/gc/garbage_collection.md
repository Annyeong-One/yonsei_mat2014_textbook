# Reference Counting

Python manages memory automatically using **reference counting** combined with **garbage collection**.

---

## Reference counting

Each object keeps a count of how many references point to it.

- Count increases when referenced.
- Count decreases when references are removed.
- When count reaches zero, object is deallocated.

---

## Circular references

Reference counting alone cannot handle cycles:

```python
a = []
a.append(a)
```

The reference count never reaches zero.

---

## Garbage collector

Python includes a cyclic garbage collector that:
- detects reference cycles,
- reclaims unreachable objects,
- runs periodically.

You usually don’t need to think about it.

---

## Practical

- Deterministic deallocation is not guaranteed.
- Resource management uses context managers (`with`).
- Manual memory management is unnecessary.

---

## Key takeaways

- Python uses reference counting + GC.
- Cycles are handled automatically.
- Memory management is mostly invisible to users.
