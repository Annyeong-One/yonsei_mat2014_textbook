# Functions

A **function** is a named block of code that performs a specific task.

You can think of a function as a small **machine** inside your program.
Later we will see how values can go into and come out of that machine,
but for now our machine has no input slot and no output tray — it simply runs a fixed set of instructions when activated.

Functions help programs:

- organize logic
- reuse code
- avoid repetition
- divide large problems into smaller parts

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
def greet():
    print("Hello")
```

This defines a function named `greet`.

!!! warning "Defining is not executing"

    Writing `def greet(): ...` only tells Python that a function named `greet` exists.
    No code inside the function body runs at this point.
    The function runs only when it is **called**.

## Calling a Function

To run a function, we **call** it using parentheses.

```python
greet()
```

Output

```text
Hello
```

Parentheses tell Python that the function should be executed.
Without them, `greet` just refers to the function object.

## Execution Flow

When a function is called, execution temporarily moves into the function body and then returns to where the call occurred.
We will explore how Python tracks these jumps in [Runtime Model (Call Stack)](call_stack.md).

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

## Key Ideas

Functions let us name a block of code and reuse it throughout a program.
The `def` keyword creates a function, and parentheses after the name call it.
Remember that defining a function only registers it — no code runs until the function is called.

So far our functions do not accept parameters or return values.
Next we will see how functions can receive input from the caller.
