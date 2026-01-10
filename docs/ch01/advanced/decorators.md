# Decorator Syntax and Semantics

Decorators modify functions or methods **without changing their source code**. They are a powerful metaprogramming tool in Python.

---

## 1. What is a decorator?

A decorator is a function that:
- takes another function,
- returns a new function.

```python
def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print("before")
        result = fn(*args, **kwargs)
        print("after")
        return result
    return wrapper
```

---

## 2. Applying decorators

Using decorator syntax:

```python
@my_decorator
def greet(name):
    print(f"Hello {name}")
```

This is equivalent to:

```python
greet = my_decorator(greet)
```

---

## 3. Preserving metadata

Decorators should preserve function metadata:

```python
from functools import wraps

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
```

---

## 4. Common use cases

Decorators are used for:
- logging,
- timing and profiling,
- access control,
- caching.

---

## 5. Cautionary notes

- Decorators can obscure control flow.
- Overuse hurts readability.
- Prefer clarity over cleverness.

---

## Key takeaways

- Decorators wrap functions.
- `@decorator` is syntactic sugar.
- Use `functools.wraps` for correctness.
