# The `builtins` Namespace

Python’s built-in functions, exceptions, and types live in the **`builtins` namespace**. Understanding this namespace clarifies what is always available without imports.

---

## 1. What is `builtins`?

`builtins` is a module automatically loaded by Python that contains:
- core functions (`len`, `print`, `range`, …),
- built-in types (`int`, `list`, `dict`, …),
- built-in exceptions (`ValueError`, `TypeError`, …).

You normally use these names without qualification.

---

## 2. Inspecting `builtins`

```python
import builtins
dir(builtins)
```

This shows all names that are globally available.

---

## 3. Shadowing builtins

You can accidentally override built-ins:

```python
list = [1, 2, 3]   # BAD
```

After this, `list()` no longer refers to the type.

Avoid shadowing built-in names.

---

## 4. Why this matters

Understanding `builtins` helps with:
- debugging name conflicts,
- reading unfamiliar code,
- metaprogramming and introspection.

---

## Key takeaways

- Built-ins live in the `builtins` module.
- They are always available without imports.
- Avoid shadowing built-in names.
