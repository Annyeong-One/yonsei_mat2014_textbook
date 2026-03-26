# Function Examples

These examples reinforce the concepts from the previous sections:
parameters, return values, type hints, and composition.

## Square

A function with a single parameter and a return value.

```python
def square(x: int) -> int:
    return x * x

print(square(5))
```

Output

```text
25
```

## Rectangle Area

A function with multiple parameters.

```python
def area(length: float, width: float) -> float:
    return length * width

print(area(3, 4))
```

Output

```text
12
```

## Format Name

Functions work with any data type, not just numbers.

```python
def format_name(first: str, last: str) -> str:
    return last.upper() + ", " + first

print(format_name("Alice", "Smith"))
print(format_name("Bob", "Lee"))
```

Output

```text
SMITH, Alice
LEE, Bob
```

## Temperature Conversion

A function that performs a real calculation.

```python
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(25))
```

Output

```text
77.0
```

## Maximum Value

Functions can include conditional logic.

```python
def max_value(a: int, b: int) -> int:
    if a > b:
        return a
    return b

print(max_value(10, 4))
```

Output

```text
10
```

## Composition

Functions can be combined by passing the return value of one function as the argument to another.

```python
def square(x: int) -> int:
    return x * x

def double(x: int) -> int:
    return 2 * x

print(double(square(3)))
```

`square(3)` runs first and returns `9`.
That value is then passed to `double`, which returns `18`.

Output

```text
18
```

## Key Ideas

This page concludes the functions section.
A function is a black box that optionally takes inputs and optionally produces an output.
Parameters let a function accept different values each time it is called, and the `return` statement sends a result back to the caller.
Type hints document the expected types without changing how Python runs the code.
Small functions can be composed — the return value of one becomes the argument of another — to build larger programs from simple, reusable pieces.

Next: [Runtime Model (Call Stack)](call_stack.md).
