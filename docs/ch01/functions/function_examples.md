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

print(area(3.0, 4.0))
```

Output

```text
12.0
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

## Exercises

**Exercise 1.**
Write a function `is_even(n)` that takes an integer and returns `True` if it is even, `False` otherwise. Test it with the values 4, 7, and 0.

??? success "Solution to Exercise 1"
    ```python
    def is_even(n: int) -> bool:
        return n % 2 == 0

    print(is_even(4))   # True
    print(is_even(7))   # False
    print(is_even(0))   # True
    ```

    The modulo operator `%` returns the remainder when dividing by 2. If the remainder is 0, the number is even. Note that 0 is even because `0 % 2 == 0`.

---

**Exercise 2.**
Predict the output of the following code without running it, then verify.

```python
def mystery(a, b):
    return a + b, a * b

x, y = mystery(3, 4)
print(x)
print(y)
```

??? success "Solution to Exercise 2"
    Output:

    ```
    7
    12
    ```

    The function returns a tuple `(3 + 4, 3 * 4)` which is `(7, 12)`. The assignment `x, y = mystery(3, 4)` unpacks the tuple, so `x = 7` and `y = 12`.

---

**Exercise 3.**
Write a function `circle_area(radius)` with a type hint that accepts a `float` and returns a `float`. Use `3.14159` as the value of pi. Then write a second function `ring_area(outer, inner)` that computes the area of a ring by **composing** `circle_area` -- calling it twice and subtracting the results.

??? success "Solution to Exercise 3"
    ```python
    def circle_area(radius: float) -> float:
        return 3.14159 * radius * radius

    def ring_area(outer: float, inner: float) -> float:
        return circle_area(outer) - circle_area(inner)

    print(circle_area(5.0))
    print(ring_area(5.0, 3.0))
    ```

    Output:

    ```
    78.53975
    50.26544
    ```

    `ring_area` composes `circle_area` by calling it for both the outer and inner radii. The ring area is $\pi r_{\text{outer}}^2 - \pi r_{\text{inner}}^2 = \pi(5^2 - 3^2) = \pi \times 16 \approx 50.27$.

---

**Exercise 4.**
A student writes the following function but gets unexpected results. Identify the bug and explain how to fix it.

```python
def greet(name):
    greeting = "Hello, " + name

greet("Alice")
print(greeting)
```

??? success "Solution to Exercise 4"
    The code raises a `NameError: name 'greeting' is not defined`.

    There are two bugs:

    1. The function does not `return` anything. The variable `greeting` is local to the function and cannot be accessed outside it.
    2. The code tries to use `greeting` outside the function, but local variables do not exist after the function returns.

    Fix:

    ```python
    def greet(name):
        greeting = "Hello, " + name
        return greeting

    result = greet("Alice")
    print(result)
    ```

    Output:

    ```
    Hello, Alice
    ```

    The function must return the value, and the caller must capture the return value in a variable.

---

**Exercise 5.**
Explain the difference between calling `square(5)` and referencing `square` without parentheses. What does each evaluate to? Why is this distinction important?

??? success "Solution to Exercise 5"
    `square(5)` **calls** the function with argument `5` and evaluates to the return value, which is `25`.

    `square` without parentheses evaluates to the **function object itself**. It does not execute the function. Printing it shows something like:

    ```
    <function square at 0x7f3a1c2b4d30>
    ```

    This distinction is important because:

    - Functions in Python are **first-class objects**. They can be assigned to variables, passed as arguments, and stored in data structures.
    - A common beginner mistake is writing `result = square` instead of `result = square(5)`, which assigns the function object rather than calling it.
    - The parentheses `()` are the **call operator**. Without them, no execution occurs.
