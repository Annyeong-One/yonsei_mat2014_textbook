# Type Conversions

Python allows explicit conversion between built-in types. Understanding these conversions is essential for correct programs.

---

## Numeric conversions

```python
int(3.7)      # 3   (truncates toward zero)
float(3)      # 3.0
```

Be careful: `int()` does **not** round.

---

## String conversions

```python
str(123)      # "123"
int("123")    # 123
float("3.14") # 3.14
```

Invalid conversions raise exceptions:

```python
int("abc")    # ValueError
```

---

## Boolean conversions

Rules for `bool(x)`:
- `0`, `0.0`, `""`, `[]`, `{}`, `None` → `False`
- everything else → `True`

```python
bool(0)       # False
bool(10)      # True
```

---

## Explicit vs implicit

Python avoids implicit numeric conversions that lose information.
Always convert explicitly when needed.

---

## Key takeaways

- Use `int()`, `float()`, `str()`, `bool()` explicitly.
- Numeric conversions can lose information.
- Invalid conversions raise exceptions.
