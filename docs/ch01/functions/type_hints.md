# Type Hints

Python allows functions to include **type hints** that describe the expected types of parameters and return values.

---

## The Problem

Consider this function:

```python
def area(length, width):
    return length * width
```

What types are `length` and `width`?
Are they integers, floats, or something else?

Without additional context, the reader cannot tell.

---

## The Solution

Type hints make the expected types explicit.

```python
def area(length: float, width: float) -> float:
    return length * width
```

A reader can immediately see the intended types.

---

## Syntax

Type hints appear after parameter names and after the function arrow.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:

- `a: int` means `a` should be an integer
- `b: int` means `b` should be an integer
- `-> int` means the function returns an integer

---

## Example

```python
def average(a: float, b: float) -> float:
    return (a + b) / 2

result = average(3.0, 7.0)
print(result)
```

Output

```text
5.0
```

---

## Type Hints Are Optional

Python does **not enforce type hints at runtime**.

This means the following will still run:

```python
add("2", "3")
```

However, static analysis tools can examine the code without running it and warn about possible type errors.

---

## Why Use Type Hints

Type hints improve code readability and help tools detect potential errors.

---

## Summary

- type hints describe expected parameter types
- `:` indicates the parameter type
- `->` indicates the return type
- type hints are optional but improve readability and tooling
