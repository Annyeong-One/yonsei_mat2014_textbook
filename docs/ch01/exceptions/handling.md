# `try` / `except` / `finally`

Python provides structured exception handling using `try`, `except`, `else`, and `finally`.

---

## 1. Basic structure

```python
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input")
```

---

## 2. Catching multiple exceptions

```python
try:
    ...
except (TypeError, ValueError):
    ...
```

---

## 3. `else` clause

Runs only if no exception occurs.

```python
try:
    x = int("123")
except ValueError:
    print("error")
else:
    print("success")
```

---

## 4. `finally` clause

Always runs, regardless of exceptions.

```python
try:
    f = open("file.txt")
finally:
    f.close()
```

This is essential for resource cleanup.

---

## Key takeaways

- Use `try` / `except` for error handling.
- `else` runs only on success.
- `finally` guarantees cleanup.
