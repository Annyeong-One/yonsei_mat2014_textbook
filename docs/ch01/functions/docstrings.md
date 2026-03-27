# Docstrings

A **docstring** is a string literal placed as the first statement in a function body. It documents what the function does.

```python
def celsius_to_fahrenheit(c: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32
```

Python stores the docstring on the function object and makes it available at runtime. Type hints say *what* the types are; the docstring says *why* the function exists and what it does.

## Single-Line Docstrings

Use a single line for simple functions. The string sits on one line, inside triple quotes:

```python
def square(x: int) -> int:
    """Return the square of x."""
    return x * x

def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0
```

Write the docstring as an imperative sentence — *"Return ..."*, *"Compute ..."*, *"Check ..."* — not *"Returns ..."* or *"This function returns ..."*.

## Multi-Line Docstrings

Use multiple lines when the function needs more explanation. The first line is a short summary; a blank line separates it from the rest:

```python
def describe_point(x: float, y: float) -> str:
    """Return a formatted string describing a 2D point.

    The output uses the format '(x, y)' with two decimal places.
    Negative coordinates are shown with a minus sign.
    """
    return f"({x:.2f}, {y:.2f})"
```

## Accessing Docstrings

Python stores the docstring in the `__doc__` attribute:

```python
def greet(name: str) -> None:
    """Print a welcome message for the given name."""
    print(f"Welcome, {name}!")

print(greet.__doc__)   # Print a welcome message for the given name.
```

`help()` displays it in a formatted view — useful in an interactive session:

```python
help(greet)
```

Output:

```text
Help on function greet in module __main__:

greet(name: str) -> None
    Print a welcome message for the given name.
```

## Docstrings and Type Hints Together

Type hints and docstrings complement each other. Type hints handle the *what*; the docstring handles the *why* and *how*:

```python
def calculate_bmi(weight: float, height: float) -> float:
    """Return the Body Mass Index for the given weight and height.

    weight is in kilograms, height is in metres.
    A result below 18.5 is underweight; above 25.0 is overweight.
    """
    return weight / height ** 2
```

The type hints tell a reader (and static analysis tools) that both arguments are floats. The docstring explains the units and what the result means — information that types alone cannot convey.

## Key Ideas

A docstring is the first string in a function body. It is stored on `__doc__` and displayed by `help()`.
Single-line docstrings suit simple functions; multi-line docstrings add detail when needed.
Write docstrings as imperative sentences and use them to explain intent, units, and constraints — the things type hints cannot express.

Next: [Function Examples](function_examples.md).
