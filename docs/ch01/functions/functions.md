# Functions

A **function** is a named block of code that performs a specific task.

You can think of a function as a **black box**:

- it optionally receives **inputs** (called parameters)
- it performs some operation on those inputs
- it optionally produces an **output** returned with the `return` keyword

```text
         ┌─────────────┐
inputs ──►│   function  ├──► output
         └─────────────┘
```

For now our examples use no inputs and no output.
We will add those in [Parameters](parameters.md) and [Return Values](return_values.md).

## Why Functions

Consider the following code:

```python
print("=" * 30)
print("  Welcome, Alice")
print("=" * 30)

print("=" * 30)
print("  Welcome, Alice")
print("=" * 30)

print("=" * 30)
print("  Welcome, Alice")
print("=" * 30)
```

The same three-line block is repeated several times.

Instead of repeating the same statements, we can place them inside a function and call that function whenever we need it.

```python
def greet():
    print("=" * 30)
    print("  Welcome, Alice")
    print("=" * 30)

greet()
greet()
greet()
```

Output

```text
==============================
  Welcome, Alice
==============================
==============================
  Welcome, Alice
==============================
==============================
  Welcome, Alice
==============================
```

## Defining a Function

In Python, functions are defined using the `def` keyword.

An important point before we look at the syntax: **defining a function does not execute it**.
Python reads the `def` block and stores the function for later use, but the body does not run until the function is called.

```python
def display_score():
    print("Score: 100")
```

This defines a function named `display_score`.

!!! warning "Defining is not executing"

    Writing `def display_score(): ...` only tells Python that a function named `display_score` exists.
    No code inside the function body runs at this point.
    The function runs only when it is **called**.

## Calling a Function

To run a function, we **call** it using parentheses.

```python
display_score()
```

Output

```text
Score: 100
```

Parentheses tell Python that the function should be executed.
Without them, `display_score` just refers to the function object.

```python
print(display_score())
print(display_score)
```

Output

```text
Score: 100
None
<function display_score at 0x7f3a1c2b4d30>
```

`display_score()` calls the function, which prints `Score: 100` and returns `None` (since there is no `return` statement).
`display_score` without parentheses prints the function object itself, showing its name and memory address.
The address shown will differ on your machine and between runs.

## Execution Flow

Statements above a `def` run first; the function body runs only at the call site.
When a function is called, execution temporarily moves into the function body and then returns to where the call occurred.

```python
def greet():
    print("Inside greet()")
    print("Hello")

print("Start program")
greet()
print("End program")
```

Output

```text
Start program
Inside greet()
Hello
End program
```

We will explore how Python tracks these jumps in [Runtime Model (Call Stack)](call_stack.md).

## Key Ideas

Functions let us name a block of code and reuse it throughout a program.
The `def` keyword creates a function, and parentheses after the name call it.
Remember that defining a function only registers it — no code runs until the function is called.

Next: [Parameters](parameters.md).
