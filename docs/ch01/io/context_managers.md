# Context Managers (`with`)

Context managers ensure that resources are properly acquired and released. For file I/O, they are the preferred approach.

---

## 1. The problem with manual closing

If an exception occurs:

```python
f = open("data.txt")
x = 1 / 0
f.close()
```

The file is never closed.

---

## 2. Using `with`

```python
with open("data.txt") as f:
    for line in f:
        print(line)
```

The file is **automatically closed**, even if an error occurs.

---

## 3. Why context managers matter

They guarantee:
- proper cleanup,
- simpler code,
- fewer bugs.

They are used for files, locks, network connections, etc.

---

## 4. Custom context managers

You can define your own context managers using:
- `__enter__` / `__exit__`
- or `contextlib`

---

## Key takeaways

- Always prefer `with open(...)`.
- Context managers handle cleanup safely.
- They are essential for robust programs.
