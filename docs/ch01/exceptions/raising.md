# Raising Exceptions

You can raise exceptions explicitly to signal error conditions in your own code.

---

## 1. Using `raise`

```python
raise ValueError("Invalid parameter")
```

This immediately stops execution unless caught.

---

## 2. Raising conditionally

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

---

## 3. Re-raising exceptions

Inside an `except` block, you can re-raise:

```python
try:
    ...
except Exception:
    log_error()
    raise
```

This preserves the original traceback.

---

## 4. Custom exceptions

Define your own exception types:

```python
class PricingError(Exception):
    pass
```

Custom exceptions improve clarity and structure.

---

## Key takeaways

- Use `raise` to signal errors explicitly.
- Re-raise to preserve tracebacks.
- Custom exceptions clarify intent.
