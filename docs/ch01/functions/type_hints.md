

# Type Hints

Python allows functions to include **type hints**, which are annotations describing the expected types of parameters and return values.

Type hints improve:

- readability
- documentation
- editor support
- static analysis

They do **not** enforce types at runtime by themselves.

```mermaid2
flowchart LR
    A[Function definition] --> B[Type hints]
    B --> C[Clearer intent]
````

---

## 1. Basic Syntax

Type hints are written after parameter names and after `->` for return types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This suggests:

* `a` should be an `int`
* `b` should be an `int`
* the function should return an `int`

---

## 2. Hints Improve Readability

Even without any external tool, type hints make code easier to understand.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

A reader immediately sees that the function expects a string and returns a string.

---

## 3. Type Hints Are Not Runtime Enforcement

Python does not automatically reject wrong argument types just because hints are present.

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("3", "4"))
```

This may still run, because Python itself does not enforce the hint.

Type hints are mainly guidance for humans and tools such as static type checkers.

---

## 4. Common Built-in Hints

Some common type hints:

| Hint             | Meaning                             |
| ---------------- | ----------------------------------- |
| `int`            | integer                             |
| `float`          | floating-point number               |
| `str`            | string                              |
| `bool`           | Boolean                             |
| `None`           | no return value or absence          |
| `list[int]`      | list of integers                    |
| `dict[str, int]` | dictionary from strings to integers |

Example:

```python
def total(values: list[int]) -> int:
    return sum(values)
```

---

## 5. Hints for Functions That Return Nothing

A function that is intended only for side effects can use `-> None`.

```python
def show_message(text: str) -> None:
    print(text)
```

This signals that the function does not return a useful value.

---

## 6. Optional-Like Patterns

A function may sometimes return a real value and sometimes return `None`.

At an introductory level, this can be described conceptually even before introducing more advanced type constructs.

```python
def reciprocal(x: float) -> float | None:
    if x == 0:
        return None
    return 1 / x
```

This says the result may be either a float or `None`.

---

## 7. Type Hints and Documentation

Type hints complement docstrings.

```python
def square(x: int) -> int:
    """Return x squared."""
    return x * x
```

Together, hints and docstrings make functions much easier to read and maintain.

---

## 8. Worked Examples

### Example 1: typed add function

```python
def add(a: int, b: int) -> int:
    return a + b
```

### Example 2: typed greeting

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### Example 3: no useful return

```python
def show_total(n: int) -> None:
    print(n)
```

---

## 9. Common Pitfalls

### Assuming type hints enforce behavior

They do not automatically check argument correctness at runtime.

### Overcomplicating hints too early

Hints should clarify, not overwhelm.

### Ignoring return hints

Return annotations are often just as important as parameter annotations.

---

## 10. Summary

Key ideas:

* type hints annotate expected parameter and return types
* they improve readability and tooling
* they do not automatically enforce types at runtime
* type hints work well together with docstrings

Type hints make function definitions more explicit and easier to understand.