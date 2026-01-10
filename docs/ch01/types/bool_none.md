# `bool` and `None`

Python includes two special built-in types: `bool` for truth values and `None` for the absence of a value.

---

## `bool`

`bool` has exactly two values:
- `True`
- `False`

Internally, `bool` is a subclass of `int`:

```python
True == 1     # True
False == 0   # True
```

But semantically, booleans represent truth, not numbers.

---

## Truthiness

Many objects are implicitly true or false:

```python
bool(0)        # False
bool(1)        # True
bool("")       # False
bool("abc")    # True
bool([])       # False
```

This is widely used in conditionals.

---

## `None`

`None` represents:
- absence of a value
- uninitialized state
- missing result

```python
x = None
```

---

## Comparing with

Always use `is` / `is not`:

```python
if x is None:
    print("missing")
```

Never use `==` for `None`.

---

## Key takeaways

- `bool` represents truth values.
- Many objects have truthiness.
- `None` represents “no value” and is compared with `is`.
