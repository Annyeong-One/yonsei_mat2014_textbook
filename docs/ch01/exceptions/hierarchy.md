# Exception Hierarchy


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python exceptions are organized in a hierarchy. Understanding this hierarchy helps you write precise and robust error handling code.

---

## BaseException

At the top of the hierarchy is `BaseException`.

It is rarely caught directly and mainly exists to group:
- `Exception`
- `SystemExit`
- `KeyboardInterrupt`
- `GeneratorExit`

---

## Exception

Most runtime errors inherit from `Exception`.

Common subclasses include:
- `ValueError`
- `TypeError`
- `IndexError`
- `KeyError`
- `ZeroDivisionError`
- `FileNotFoundError`

In practice, you almost always catch subclasses of `Exception`.

---

## Why hierarchy

Because of inheritance, you can catch:
- specific errors when you know what to expect,
- broad categories when you want a fallback.

```python
try:
    ...
except ValueError:
    ...
except Exception:
    ...
```

---

## Key takeaways

- Exceptions form a class hierarchy.
- `Exception` is the main base class you handle.
- Catch specific exceptions whenever possible.
