# Decorator Syntax and

Decorators modify functions or methods **without changing their source code**. They are a powerful metaprogramming tool in Python.

---

## What is a decorator?

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

## Applying decorators

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

## Preserving metadata

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

## Common use cases

Decorators are used for:
- logging,
- timing and profiling,
- access control,
- caching.

---

## Cautionary notes

- Decorators can obscure control flow.
- Overuse hurts readability.
- Prefer clarity over cleverness.

---

## Key takeaways

- Decorators wrap functions.
- `@decorator` is syntactic sugar.
- Use `functools.wraps` for correctness.
