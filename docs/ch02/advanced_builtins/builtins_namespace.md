# The `builtins`


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python’s built-in functions, exceptions, and types live in the **`builtins` namespace**. Understanding this namespace clarifies what is always available without imports.

---

## What is `builtins`?

`builtins` is a module automatically loaded by Python that contains:
- core functions (`len`, `print`, `range`, …),
- built-in types (`int`, `list`, `dict`, …),
- built-in exceptions (`ValueError`, `TypeError`, …).

You normally use these names without qualification.

---

## Inspecting

```python
import builtins
dir(builtins)
```

This shows all names that are globally available.

---

## Shadowing builtins

You can accidentally override built-ins:

```python
list = [1, 2, 3]   # BAD
```

After this, `list()` no longer refers to the type.

Avoid shadowing built-in names.

---

## Why this matters

Understanding `builtins` helps with:
- debugging name conflicts,
- reading unfamiliar code,
- metaprogramming and introspection.

---

## Key takeaways

- Built-ins live in the `builtins` module.
- They are always available without imports.
- Avoid shadowing built-in names.
