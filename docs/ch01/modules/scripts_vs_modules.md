# Scripts vs Modules

Python files can act as **scripts**, **modules**, or both, depending on how they are used.

---

## 1. Scripts

Scripts are:
- executed directly,
- focused on performing a task,
- often include I/O and side effects.

Example:
```bash
python script.py
```

---

## 2. Modules

Modules are:
- imported by other code,
- organized around reusable functionality,
- avoid side effects at import time.

---

## 3. Combining both roles

A common pattern:
- define functions and classes,
- include a `main()` function,
- protect execution with a main guard.

---

## 4. Project structure

Larger projects separate:
- library code (modules),
- entry points (scripts).

This improves maintainability.

---

## Key takeaways

- Scripts are entry points.
- Modules are reusable building blocks.
- Use main guards to combine both roles cleanly.
