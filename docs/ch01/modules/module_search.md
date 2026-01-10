# `sys.path` and

Python searches for modules in a well-defined order stored in `sys.path`.

---

## The module search

```python
import sys
sys.path
```

This is a list of directories Python checks in order.

---

## Search order

Typical order:
1. Current script directory
2. Directories in `PYTHONPATH`
3. Standard library directories
4. Site-packages (installed libraries)

The first match wins.

---

## Modifying `sys.path`

You can modify `sys.path` at runtime:

```python
sys.path.append("/my/custom/path")
```

This is sometimes useful but should be avoided in production code.

---

## Common pitfalls

- Name collisions with standard library modules
- Accidental imports from the wrong directory

Use clear module names.

---

## Key takeaways

- `sys.path` controls module discovery.
- Order matters.
- Avoid manual path manipulation when possible.
