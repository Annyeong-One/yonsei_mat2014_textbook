
# Raising Exceptions

Python programs can **raise exceptions explicitly** using the `raise` statement.

This allows functions to signal that something went wrong.

```mermaid2
flowchart LR
    A[Function detects problem]
    A --> B[raise exception]
    B --> C[Caller handles exception]
````

---

## 1. Basic raise

```python
raise ValueError("Invalid value")
```

This immediately stops execution and raises the specified exception.

---

## 2. Raising Exceptions in Functions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b
```

Example:

```python
print(divide(10, 2))
print(divide(10, 0))
```

---

## 3. Custom Error Checking

Raising exceptions helps enforce constraints.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

---

## 4. Re-raising Exceptions

Sometimes a function catches an exception but wants to propagate it upward.

```python
try:
    x = int("abc")
except ValueError:
    print("Conversion error")
    raise
```

This re-raises the same exception.

---

## 5. Custom Exception Classes

Programs may define their own exception types.

```python
class NegativeNumberError(Exception):
    pass
```

Example:

```python
def sqrt(x):
    if x < 0:
        raise NegativeNumberError("Negative value")
```

Custom exceptions help express domain-specific errors.

---

## 6. Worked Examples

### Example 1

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

### Example 2

```python
def temperature(c):
    if c < -273.15:
        raise ValueError("Below absolute zero")
```

---

## 7. When to Raise Exceptions

Raising exceptions is appropriate when:

* inputs violate assumptions
* an operation cannot be completed
* continuing would produce incorrect results

---

## 8. Summary

Key ideas:

* `raise` explicitly signals errors
* functions can validate inputs and raise exceptions
* exceptions propagate up the call stack
* custom exception classes can represent domain-specific problems

Raising exceptions allows programs to enforce correctness and communicate errors clearly.

