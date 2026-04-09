
# Putting It All Together

At this point, you have seen all the fundamental pieces of Python: **objects**, **names**, **expressions**, **types**, and **structure**. Now we bring them together into a single program that demonstrates how Python works as a system.

---

## A Complete Example

```python
name = "Alice"
age = 20
scores = [80, 90, 85]

average = sum(scores) / len(scores)
status = "adult" if age >= 18 else "minor"

print(f"{name} is {status} with average score {average}")
```

Output:

```
Alice is adult with average score 85.0
```

---

## Mapping to Core Concepts

| Concept    | Example in this program         |
| ---------- | ------------------------------- |
| Object     | `"Alice"`, `20`, `[80, 90, 85]` |
| Name       | `name`, `age`, `scores`         |
| Expression | `sum(scores) / len(scores)`     |
| Operator   | `/`, `>=`                       |
| Type       | `int`, `list`, `str`            |
| Structure  | conditional expression, f-string |
| Statement  | assignment, `print()`           |

---

## Step-by-Step Breakdown

**Step 1 --- Objects and Names.** `"Alice"`, `20`, and `[80, 90, 85]` are objects. The names `name`, `age`, and `scores` are bound to them.

**Step 2 --- Expressions.** `sum(scores) / len(scores)` composes smaller expressions: `sum(scores)` produces `255`, `len(scores)` produces `3`, and `255 / 3` produces `85.0`. Each step creates new objects.

**Step 3 --- Type-Dependent Behavior.** `>=` is an operator that calls a method on `age` (an `int`). The result is a Boolean that determines which string the conditional expression selects.

**Step 4 --- Output.** The f-string constructs a new string from all the computed values, and `print` sends it to the console.

---

## The Big Idea

This entire program follows one principle:

> Python programs transform objects through expressions, under the control of structure.

With this model, Python stops being a collection of rules. You can now explain:

- why `"1" + "1"` produces `"11"` (string concatenation)
- why `True + True` produces `2` (Boolean is a subclass of `int`)
- why modifying a list can affect multiple variables (shared references)
- why `a + b` depends on the type of `a` (method dispatch)

These are not exceptions---they are consequences of the system.

---

## When Things Go Wrong

The model also explains failures. Consider this broken version:

```python
scores = [80, 90, "85"]
average = sum(scores) / len(scores)
```

This raises `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. The `sum()` function calls `+` on each element, and `int.__add__` does not know how to add a string. The type mismatch is caught at runtime, not at definition time.

Another common failure:

```python
scores = []
average = sum(scores) / len(scores)
```

This raises `ZeroDivisionError: division by zero` because `len([])` is `0`. The model predicts this: `sum([])` returns `0`, `len([])` returns `0`, and `0 / 0` is undefined.

Understanding the model lets you predict *where* and *why* errors occur---not just *what* went wrong.

---

## Mental Model Checklist

When reading any Python program, ask:

1. **What objects are involved?**
2. **What names refer to them?**
3. **What expressions are being evaluated?**
4. **What types determine behavior?**
5. **What structure controls execution?**

If you can answer these five questions, you understand the program.

---

## The Python Mental Model

Every program you write follows this flow:

```mermaid
flowchart LR
    A[Names] --> B[Objects]
    B --> C[Types]
    C --> D[Expressions]
    D --> E[Evaluation]
    E --> F[New Objects]
    F --> G[Statements]
    G --> H[Output]
```

> Python programs transform objects through expressions, under the control of structure.

## Exercises

**Exercise 1.**
Predict the output of the following program without running it, then verify your answer.

```python
width = 5
height = 3
area = width * height
perimeter = 2 * (width + height)
print("Area:", area)
print("Perimeter:", perimeter)
```

??? success "Solution to Exercise 1"
    Output:

    ```
    Area: 15
    Perimeter: 16
    ```

    `width * height` evaluates to `5 * 3 = 15`. `2 * (width + height)` evaluates to `2 * (5 + 3) = 2 * 8 = 16`. Each result is stored in a variable and then printed.

---

**Exercise 2.**
Write a short program that converts a temperature from Celsius to Fahrenheit. Define a variable `celsius = 25`, compute the Fahrenheit value using the formula $F = C \times \frac{9}{5} + 32$, and print the result.

??? success "Solution to Exercise 2"
    ```python
    celsius = 25
    fahrenheit = celsius * 9 / 5 + 32
    print("Fahrenheit:", fahrenheit)
    ```

    Output:

    ```
    Fahrenheit: 77.0
    ```

    The expression `25 * 9 / 5 + 32` evaluates left to right: `25 * 9 = 225`, then `225 / 5 = 45.0` (true division returns a float), then `45.0 + 32 = 77.0`.

---

**Exercise 3.**
A student writes the following program and expects the output `Total: 10`. Instead, the program produces `Total: 55`. Identify the bug and fix it.

```python
price = 5
quantity = "10"
total = price + quantity
print("Total:", total)
```

??? success "Solution to Exercise 3"
    The program raises a `TypeError` because `price` is an `int` and `quantity` is a `str` (the quotes make it a string). Python cannot add an integer and a string.

    To fix the bug, remove the quotes so that `quantity` is an integer:

    ```python
    price = 5
    quantity = 10
    total = price * quantity
    print("Total:", total)
    ```

    Output:

    ```
    Total: 50
    ```

    Note: the expected output of `10` in the problem statement suggests addition (`5 + 10 = 15`), not multiplication. If the intent was `price * quantity`, the correct output is `50`. The key lesson is that mixing types without conversion causes errors.

---

**Exercise 4.**
Explain the difference between an **expression** and a **statement** in Python. Give one example of each.

??? success "Solution to Exercise 4"
    An **expression** is a piece of code that evaluates to a value. For example:

    ```python
    3 + 4 * 2
    ```

    This evaluates to `11`.

    A **statement** is a complete instruction that Python executes. For example:

    ```python
    x = 10
    ```

    This is an assignment statement -- it binds the name `x` to the integer object `10`. While the right-hand side `10` is an expression, the entire `x = 10` line is a statement.

    All expressions can appear as statements (expression statements), but not all statements are expressions. For instance, `print("hello")` is both an expression (it evaluates to `None`) and a statement.

---

**Exercise 5.**
Write a program that defines three variables -- your name (a string), your age (an integer), and your height in meters (a float) -- and prints a single sentence containing all three values using string concatenation or an f-string.

??? success "Solution to Exercise 5"
    Using an f-string:

    ```python
    name = "Alice"
    age = 25
    height = 1.68

    print(f"{name} is {age} years old and {height} meters tall.")
    ```

    Output:

    ```
    Alice is 25 years old and 1.68 meters tall.
    ```

    Alternatively, using concatenation and `str()`:

    ```python
    name = "Alice"
    age = 25
    height = 1.68

    print(name + " is " + str(age) + " years old and " + str(height) + " meters tall.")
    ```

    Both approaches produce the same output. The f-string version is more readable and is generally preferred.
