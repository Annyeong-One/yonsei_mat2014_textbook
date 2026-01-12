# `str`: Docstrings

Docstrings document Python functions, classes, and modules using triple-quoted strings.

---

## Basic Syntax

### 1. Function Docstring

Place a triple-quoted string as the first statement:

```python
def pow(x, n):
    """
    Calculate the power of a number.

    Parameters:
    - x (int or float): The base number.
    - n (int): The exponent.

    Returns:
    int or float: The result of x raised to the power of n.
    """
    if n == 0:
        return 1
    else:
        return x * pow(x, n-1)
```

### 2. Accessing Docstrings

Use `help()` to view documentation:

```python
help(pow)
```

Output:
```
Help on function pow in module __main__:

pow(x, n)
    Calculate the power of a number.
    
    Parameters:
    - x (int or float): The base number.
    - n (int): The exponent.
    
    Returns:
    int or float: The result of x raised to the power of n.
```

---

## Library Examples

### 1. NumPy Docstring

View documentation for library functions:

```python
import numpy as np

help(np.linspace)
```

### 2. __doc__ Attribute

Access docstrings programmatically:

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet.__doc__)  # Return a greeting message.
```

---

## Best Practices

### 1. First Line Summary

Start with a concise one-line summary:

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b
```

### 2. Extended Format

For complex functions, include parameters and returns:

```python
def divide(dividend, divisor):
    """
    Divide two numbers.

    Parameters:
    - dividend (float): The number to be divided.
    - divisor (float): The number to divide by.

    Returns:
    float: The quotient.

    Raises:
    ZeroDivisionError: If divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return dividend / divisor
```

---

## Key Takeaways

- Docstrings use triple quotes as first statement.
- Access via `help()` or `__doc__` attribute.
- Document parameters, returns, and exceptions.
- Essential for code maintainability.
