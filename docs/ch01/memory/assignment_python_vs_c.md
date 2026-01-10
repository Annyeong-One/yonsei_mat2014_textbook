# Assignment Semantics

Assignment in Python is fundamentally different from assignment in C and other low-level languages.

---

## Assignment in C

In C:
- variables represent memory locations,
- assignment copies values,
- pointers must be explicit.

```c
int a = 10;
int b = a;  // copies value
```

---

## Assignment in Python

In Python:
- assignment binds a name to an object,
- no copying is implied.

```python
a = 10
b = a
```

Both names refer to the same object.

---

## Consequences

- Assignment is cheap.
- Mutability matters.
- Aliasing can occur silently.

This model simplifies memory safety but requires conceptual clarity.

---

## Key takeaways

- Python assignment binds names to objects.
- No implicit copying.
- Very different semantics from C.
