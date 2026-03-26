
# Return Values

Functions can compute results and send them back to the caller.

This is done using the `return` statement.

## The Problem

In Python, every function returns a value.
If no `return` statement is present, Python automatically returns `None`.

Consider this function:

```python
def add(a, b):
    print(a + b)

result = add(3, 4)

print("Result:", result)
```

Output

```text
7
Result: None
```

The function printed the value `7`, but it did not return anything.
Because there is no `return` statement, `result` receives `None`.

## The Solution

The `return` statement sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(3, 4)

print("Result:", result)
```

Output

```text
Result: 7
```

Now `result` holds the value `7` and can be used later in the program.

## Printing vs Returning

`print` displays a value on the screen.
`return` sends a value back to the caller.

The key difference is that a returned value can be **reused** — stored in a variable, passed to another function, or used in an expression.

```python
def add(a, b):
    return a + b

print(add(2, 5) * 2)
```

Output

```text
14
```

Because `add(2, 5)` returns `7`, the expression `add(2, 5) * 2` evaluates to `14`.
If `add` had used `print` instead of `return`, this would not be possible.

## Key Ideas

The `return` statement lets a function produce a value that the caller can store, print, or use in further computation.
Without `return`, a function always returns `None`.
The distinction between printing and returning is one of the most important concepts for beginners to internalize — `print` is for humans to read, `return` is for the program to use.

Next: [Type Hints](type_hints.md).
