# Runtime Model (Call Stack)

When functions call other functions, Python must remember where execution should return after each function finishes.

This is handled by a structure called the **call stack**.

---

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

---

## How the Call Stack Works

The call stack keeps track of which functions are currently running.

The program itself runs inside a **main frame** at the bottom of the call stack.

The stack follows a **last-in, first-out (LIFO)** rule:
the most recent function call is always on top of the stack.
The function at the top of the stack is the one currently running.

Program start:

```text
Call Stack (top)

+------+
| main |
+------+
```

When `main` calls `f()`:

```text
Call Stack (top)

+------+
|  f   |
| main |
+------+
```

When `f()` calls `g()`:

```text
Call Stack (top)

+------+
|  g   |
|  f   |
| main |
+------+
```

`g()` is now running. `f()` is paused and waiting for `g()` to finish.

When `g()` returns:

```text
Call Stack (top)

+------+
|  f   |
| main |
+------+
```

Execution returns to `f()`.

When `f()` returns:

```text
Call Stack (top)

+------+
| main |
+------+
```

When the program ends:

```text
Call Stack

(empty)
```

---

## Stack Frames

Each function call creates a **stack frame** that stores information needed while the function runs.

A stack frame stores:

- local variables
- the current execution position
- where to return after the function completes

Each function call creates its own separate stack frame.

---

## Why the Call Stack Matters

The call stack explains:

- nested function calls
- where execution resumes after a function returns
- how local variables are isolated between function calls

Understanding the call stack becomes especially important when learning **recursion**.

---

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
Reading a traceback is essentially reading the call stack from the point where the error occurred.

---

## Summary

- Python tracks function calls using the **call stack**
- the stack follows a **last-in, first-out** rule
- each function call creates a **stack frame**
- tracebacks show the call stack when an error occurs
