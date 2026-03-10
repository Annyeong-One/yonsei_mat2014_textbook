# Expressions and Statements

Every line of Python is either an expression, a statement, or both. Understanding this distinction clarifies how Python evaluates and executes your code.

## Definition

An **expression** is any piece of code that evaluates to a value: `3 + 5`, `len([1,2,3])`, `x > 0`. A **statement** is a complete instruction that performs an action: `x = 10`, `import math`, `if x > 5: ...`. Expressions can appear inside statements, but statements cannot appear inside expressions.

## Explanation

Python evaluates expressions according to **operator precedence** (parentheses first, then exponentiation, then multiplication/division, then addition/subtraction, then comparisons, then logical operators). When precedence is equal, most operators associate left-to-right except exponentiation (right-to-left: `2 ** 3 ** 2` = `2 ** 9` = 512).

**Short-circuit evaluation**: `and` stops at the first falsy value; `or` stops at the first truthy value. The unevaluated operand is never executed, which is useful for guard conditions like `x is not None and x.method()`.

**Type coercion**: In mixed numeric operations, Python promotes to the wider type (`int + float` yields `float`; `bool + int` yields `int` because `bool` is a subclass of `int`).

Key statement types: assignment (`x = 10`), augmented assignment (`x += 5`), import, function/class definitions, control flow (`if`, `for`, `while`), and `try/except`.

## Examples

```python
# Expressions evaluate to values
3 + 5              # 8
len([1, 2, 3])     # 3
"hello".upper()    # "HELLO"
x > 0 and x < 10  # True or False

# Statements perform actions
x = 10             # assignment statement
import math        # import statement
del x              # deletion statement
```

```python
# Operator precedence: ** before *, * before +
result = 2 + 3 * 4 ** 2   # 2 + 3 * 16 = 2 + 48 = 50
result = (2 + 3) * 4 ** 2  # 5 * 16 = 80

# Short-circuit evaluation
False and print("skipped")  # print() never called
True or print("skipped")    # print() never called
```

```python
# Ternary (conditional) expression
age = 20
status = "adult" if age >= 18 else "minor"  # "adult"

# Walrus operator (assignment expression, Python 3.8+)
if (n := len(items)) > 10:
    print(f"Large list: {n} items")
```
