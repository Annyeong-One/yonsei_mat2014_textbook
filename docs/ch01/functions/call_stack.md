# Runtime Model (Call Stack)

When functions call other functions, Python must remember where execution should return after each function finishes.

This is handled by a structure called the **call stack**.

## Nested Function Calls

Functions can call other functions.

```python
def g():
    print("inside g")

def f():
    print("inside f")
    g()
    print("back in f")

f()
```

Output

```text
inside f
inside g
back in f
```

Execution order:

1. `f()` starts running
2. `f()` calls `g()`
3. `g()` runs and finishes
4. execution returns to `f()`
5. `f()` continues and finishes

## How the Call Stack Works

The call stack keeps track of which functions are currently running.

The program itself runs inside a **main frame** at the bottom of the call stack.

The stack follows a **last-in, first-out (LIFO)** rule:
the most recent function call is always on top of the stack.
The function at the top of the stack is the one currently running.

Program start:

```text
+--------+
|  main  |
+--------+
```

When `main` calls `f()`:

```text
+--------+
|   f    |
|  main  |
+--------+
```

When `f()` calls `g()`:

```text
+--------+
|   g    |
|   f    |
|  main  |
+--------+
```

`g()` is now running. `f()` is paused and waiting for `g()` to finish.

When `g()` returns:

```text
+--------+
|   f    |
|  main  |
+--------+
```

Execution returns to `f()`.

When `f()` returns:

```text
+--------+
|  main  |
+--------+
```

When the program ends:

```text
(empty)
```

## Stack Frames

Each function call creates a **stack frame** that stores information needed while the function runs.

A stack frame stores:

- local variables
- the current execution position
- where to return after the function completes

Each function call creates its own separate stack frame.
This means that local variables in one function are completely isolated from local variables in another, even if they share the same name.

```python
def f():
    x = 10
    g()
    print("f sees x =", x)

def g():
    x = 99
    print("g sees x =", x)

f()
```

Output

```text
g sees x = 99
f sees x = 10
```

Both `f` and `g` use a variable named `x`, but each function has its own stack frame with its own `x`.
When `g` sets `x = 99`, it does not affect the `x` inside `f`.

## Tracebacks and the Call Stack

When an error occurs, Python prints a **traceback**.

A traceback lists the sequence of calls from the program entry point to the location where the error occurred.

```python
def g():
    x = 1 / 0

def f():
    g()

f()
```

Output

```text
Traceback (most recent call last):
  File "example.py", line 7, in <module>
    f()
  File "example.py", line 5, in f
    g()
  File "example.py", line 2, in g
    x = 1 / 0
ZeroDivisionError: division by zero
```

This traceback shows the call stack at the moment of the error.

!!! tip

    Reading a traceback is essentially reading the call stack from the point where the error occurred.

## Key Ideas

Python tracks function calls using the call stack, which follows a last-in, first-out rule.
Each function call creates a stack frame that holds its own local variables, execution position, and return address.
Because each call gets its own frame, local variables are fully isolated between functions.
Tracebacks are snapshots of the call stack at the moment an error occurs — learning to read them is one of the most practical debugging skills in Python.

Understanding the call stack becomes especially important when learning **recursion**.
