# Context Managers

Context managers ensure that resources are properly acquired and released. For file I/O, they are the preferred approach.

---

## The problem with

If an exception occurs:

```python
f = open("data.txt")
x = 1 / 0
f.close()
```

The file is never closed.

---

## Using `with`

```python
with open("data.txt") as f:
    for line in f:
        print(line)
```

The file is **automatically closed**, even if an error occurs.

---

## Why context managers

They guarantee:
- proper cleanup,
- simpler code,
- fewer bugs.

They are used for files, locks, network connections, etc.

---

## Custom context

You can define your own context managers using:
- `__enter__` / `__exit__`
- or `contextlib`

---

## Key takeaways

- Always prefer `with open(...)`.
- Context managers handle cleanup safely.
- They are essential for robust programs.
