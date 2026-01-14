# Compile vs Runtime Errors

Programming errors fall into two main categories based on when they occur: compile-time errors (caught before execution) and runtime errors (caught during execution).


## Compile-Time Errors

Compile errors occur during the compilation or parsing phase before the program runs. In Python, these are primarily **syntax errors**.

```python
# SyntaxError: Missing colon
if True
    print("Hello")

# SyntaxError: Invalid syntax
x = 5 +

# SyntaxError: Unmatched parenthesis
print("Hello"
```

Python catches these errors when it parses the code, before any execution begins.


## Syntax Error Examples

```python
# Missing colon after if
if x > 5
    print(x)

# IndentationError (a type of SyntaxError)
def foo():
print("Hello")

# Invalid assignment
5 = x

# Unclosed string
message = "Hello
```


## Runtime Errors

Runtime errors occur during program execution when the code encounters a situation it cannot handle.

```python
# ZeroDivisionError
result = 10 / 0

# TypeError
result = "5" + 5

# IndexError
lst = [1, 2, 3]
print(lst[10])

# KeyError
d = {"a": 1}
print(d["b"])

# FileNotFoundError
f = open("nonexistent.txt")
```


## Common Runtime Error Types

| Error | Cause |
|-------|-------|
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Wrong type for operation |
| `ValueError` | Right type, wrong value |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `AttributeError` | Object has no attribute |
| `NameError` | Name not defined |
| `FileNotFoundError` | File does not exist |


## Key Differences

| Feature | Compile Error | Runtime Error |
|---------|---------------|---------------|
| When detected | Before execution | During execution |
| Program runs? | No | Partially (until error) |
| Type in Python | `SyntaxError` | Various exception types |
| Can be caught? | No | Yes, with `try/except` |
| Fix required | Yes, to run at all | Yes, for correct behavior |


## Compile Errors Prevent Execution

With a syntax error, no code runs at all.

```python
print("This never prints")

if True  # SyntaxError here
    print("Hello")

print("This also never prints")
```

None of the `print` statements execute because Python fails to parse the file.


## Runtime Errors Allow Partial Execution

With runtime errors, code runs until the error occurs.

```python
print("This prints")  # Executes

x = 10 / 0  # RuntimeError here

print("This never prints")  # Never reached
```

Output:
```
This prints
ZeroDivisionError: division by zero
```


## Handling Runtime Errors

Runtime errors can be caught and handled with `try/except`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = 0

print(f"Result: {result}")
```

Output:
```
Cannot divide by zero
Result: 0
```


## Compile Errors Cannot Be Caught

Syntax errors cannot be caught with `try/except` in the same file.

```python
# This doesn't work
try:
    if True  # SyntaxError
        pass
except SyntaxError:
    print("Caught")  # Never reached
```

The entire file fails to parse, so `try/except` never executes.


## Logical Errors

A third category exists: **logical errors**. The code runs without exceptions but produces incorrect results.

```python
# Logical error: wrong formula
def average(a, b):
    return a + b  # Should be (a + b) / 2

result = average(10, 20)
print(result)  # 30, but should be 15
```

Logical errors are the hardest to find because Python cannot detect them.
