# `id()`, `type()`,

These built-ins support **introspection**, allowing programs to examine objects at runtime.

---

## `id()`

Returns a unique identifier for an object during its lifetime:

```python
x = []
id(x)
```

Conceptually corresponds to a memory address.

---

## `type()`

Returns the type of an object:

```python
type(3)        # <class 'int'>
type([1, 2])   # <class 'list'>
```

---

## `isinstance()`

Checks whether an object is an instance of a type:

```python
isinstance(3, int)
isinstance(True, int)   # True
```

Supports tuples of types:

```python
isinstance(x, (int, float))
```

---

## Best practices

- Use `isinstance()` instead of `type(x) == T`.
- Avoid excessive type checking; prefer polymorphism.

---

## Key takeaways

- `id` checks identity.
- `type` reports object type.
- `isinstance` is the correct type-checking tool.
