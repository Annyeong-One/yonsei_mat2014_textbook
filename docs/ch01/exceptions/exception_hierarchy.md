
# Exception Hierarchy

Exceptions are objects that represent **errors or unusual conditions** that occur during program execution.

When an error occurs, Python raises an exception that interrupts normal execution.

Understanding how exceptions are organized helps programmers interpret error messages and handle problems correctly.

```mermaid2
flowchart TD
    A[BaseException]
    A --> B[Exception]
    B --> C[ArithmeticError]
    B --> D[LookupError]
    B --> E[TypeError]
    B --> F[ValueError]
    B --> G[RuntimeError]
````

---

## 1. What Is an Exception?

An exception is an event that occurs during program execution and disrupts the normal flow of instructions.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError: division by zero
```

Python stops execution because it cannot perform the operation.

---

## 2. Exception Objects

Exceptions are implemented as objects belonging to classes.

For example:

* `ZeroDivisionError`
* `TypeError`
* `ValueError`

These classes inherit from a common base.

```mermaid2
flowchart TD
    A[BaseException]
    A --> B[Exception]
    B --> C[Specific Exception Classes]
```

Most user programs interact only with exceptions derived from `Exception`.

---

## 3. Why Exceptions Exist

Exceptions allow programs to:

* detect errors
* stop incorrect computations
* report problems clearly
* recover gracefully

Without exceptions, programs would need complex error-checking code everywhere.

---

## 4. Interpreting Tracebacks

When an exception occurs, Python prints a **traceback**.

Example:

```python
def f():
    return 1 / 0

f()
```

Output:

```text
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

The traceback shows the chain of function calls that led to the error.

---

## 5. Built-in Exception Categories

Some common exception families include:

| Category       | Example                  |
| -------------- | ------------------------ |
| arithmetic     | `ZeroDivisionError`      |
| type errors    | `TypeError`              |
| value errors   | `ValueError`             |
| lookup errors  | `IndexError`, `KeyError` |
| runtime issues | `RuntimeError`           |

These categories help organize Python’s exception system.

---

## 6. Example: Index Error

```python
values = [1, 2, 3]
print(values[5])
```

Output:

```text
IndexError: list index out of range
```

This occurs when accessing a sequence outside its valid range.

---

## 7. Summary

Key ideas:

* exceptions represent runtime errors
* exceptions are objects derived from `Exception`
* Python prints tracebacks to explain failures
* different exception types represent different problems

Understanding the exception hierarchy helps programmers diagnose errors effectively.

