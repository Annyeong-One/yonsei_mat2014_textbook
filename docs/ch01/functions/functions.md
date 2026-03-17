# Functions

A **function** is a named block of code that performs a specific task.

You can think of a function as a small **machine** inside your program that performs a task.
Later we will see how values can go into and come out of that function.

Functions help programs:

- organize logic
- reuse code
- avoid repetition
- divide large problems into smaller parts

---

## Why Functions

Consider the following code:

```python
print("Hello")
print("Hello")
print("Hello")
```

The same instruction is repeated several times.

Instead of repeating the same statement, we can place it inside a function and call that function whenever we need it.

```python
def greet():
    print("Hello")

greet()
greet()
greet()
```

Output

```text
Hello
Hello
Hello
```

---

## Defining a Function

In Python, functions are defined using the `def` keyword.

```python
def greet():
    print("Hello")
```

This defines a function named `greet`.
However, defining a function does **not** execute it.

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

---

## Execution Flow

The program always runs statements from top to bottom.
When a function is called, execution temporarily moves into the function body,
and then returns to where the call occurred.

```mermaid
flowchart TD
    A[Start program] --> B[call greet()]
    B --> C[execute function body]
    C --> D[return to main program]
    D --> E[End program]
```

Example:

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

---

## Functions Calling Functions

Functions can call other functions.

```python
def say_hi():
    print("Hi")

def greet():
    say_hi()
    print("Welcome")

greet()
```

Output

```text
Hi
Welcome
```

When `greet()` runs, it calls `say_hi()`.
After `say_hi()` finishes, the program continues executing the rest of `greet()`.

```mermaid
flowchart TD
    A[call greet()] --> B["greet() calls say_hi()"]
    B --> C["execute body of say_hi()"]
    C --> D["return to greet()"]
    D --> E["print Welcome"]
```

---

## Key Ideas

- a **function** is a reusable block of code
- `def` defines a function
- functions run only when they are **called**
- parentheses tell Python to execute the function
- functions can call other functions
- functions help structure programs

So far our functions do not accept parameters or return values.
Next we will see how functions can receive input from the caller.
