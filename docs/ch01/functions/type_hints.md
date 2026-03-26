# Type Hints

Python allows functions to include **type hints** that describe the expected types of parameters and return values.

## The Problem

Consider this function:

```python
def area(length, width):
    return length * width
```

What types are `length` and `width`?
Are they integers, floats, or something else?

Without additional context, the reader cannot tell.

## The Solution

Type hints make the expected types explicit.

```python
def area(length: float, width: float) -> float:
    return length * width
```

A reader can immediately see the intended types.

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

A slightly richer example:

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

## Returning None

Functions that do not return a value can be annotated with `-> None`.

```python
def greet(name: str) -> None:
    print("Welcome,", name)
```

This tells the reader — and any analysis tool — that `greet` is called for its side effect (printing), not for a return value.

## Type Hints Are Optional

Python does **not enforce type hints at runtime**.

This means the following will still run without error:

```python
def add(a: int, b: int) -> int:
    return a + b

print(add("2", "3"))
```

Output

```text
23
```

The function was annotated for `int`, but Python happily accepted two strings and concatenated them.
The result `"23"` is valid Python but almost certainly not what the caller intended.

Static analysis tools such as mypy or pyright can examine the code without running it and warn about mismatches like this before they cause bugs.

## Key Ideas

Type hints document the expected types of parameters (`: type`) and return values (`-> type`).
Python does not enforce them at runtime, but they make code easier to read and allow static analysis tools to catch type errors early.
For functions that only perform side effects and return nothing, use `-> None`.

Next: [Function Examples](function_examples.md).
