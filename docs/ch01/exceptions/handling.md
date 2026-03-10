# `try` / `except` /


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides structured exception handling using `try`, `except`, `else`, and `finally`.

---

## Basic structure

```python
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input")
```

---

## Catching multiple

```python
try:
    ...
except (TypeError, ValueError):
    ...
```

---

## `else` clause

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

## `finally` clause

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
