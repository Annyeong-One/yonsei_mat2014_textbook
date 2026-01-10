# `__name__ == "__main__"`

The `__name__` variable distinguishes between running a file as a script and importing it as a module.

---

## 1. The `__name__` variable

- When run directly: `__name__ == "__main__"`
- When imported: `__name__ == "module_name"`

---

## 2. The main guard pattern

```python
def main():
    print("running main")

if __name__ == "__main__":
    main()
```

This ensures code runs only when executed directly.

---

## 3. Why it matters

The main guard:
- prevents unwanted side effects on import,
- enables reuse of code,
- supports testing.

It is a best practice for all scripts.

---

## Key takeaways

- `__name__` identifies execution context.
- Use main guards in executable scripts.
- Essential for reusable modules.
