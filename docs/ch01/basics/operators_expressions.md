

# Python Operators and Expressions

Programs manipulate data by **combining values using operators**.
In Python, these combinations form **expressions**, which Python evaluates to produce results.

Understanding operators and expressions explains how Python performs arithmetic, comparisons, logical reasoning, and function calls.

This chapter introduces:

* operators and operands
* expressions and statements
* operator precedence
* short-circuit evaluation
* Python’s operator methods (dunder methods)

These concepts explain **how Python interprets and evaluates code**.

---

# 1. Operators and Operands

An **operator** is a symbol that performs an operation on one or more values.

The values involved are called **operands**.

Example:

```python
a = 1
b = 1

c = a + b
```

In the expression

```
a + b
```

* `+` is the **operator**
* `a` and `b` are the **operands**

The result is a new value produced by applying the operator to the operands. 

### Conceptual structure

```mermaid2
flowchart LR
    A[Operand a] --> C[Operator +]
    B[Operand b] --> C
    C --> D[Result]
```

Operators appear throughout Python programs, performing tasks such as:

* arithmetic
* comparison
* logical reasoning
* sequence manipulation

---

# 2. Operators as Method Calls

Python implements operators using **special methods**, often called **dunder methods** (double-underscore methods).

Example:

```
a + b
```

is equivalent to

```
a.__add__(b)
```

or explicitly

```
int.__add__(a, b)
```

Example code:

```python
a = 1
b = 2

print(a + b)
print(int.__add__(a, b))
```

Output

```
3
3
```

This means operators are essentially **syntactic sugar for method calls**. 

### Operator translation

```mermaid2
flowchart LR
    A[a + b] --> B[a.__add__(b)]
    B --> C[int.__add__(a,b)]
    C --> D[result]
```

This mechanism allows Python objects to define **custom behavior for operators**.

For example, lists implement `+` as concatenation rather than arithmetic.

---

# 3. Common Operator Methods

Python defines many special methods corresponding to operators.

| Operator | Method        |
| -------- | ------------- |
| `+`      | `__add__`     |
| `-`      | `__sub__`     |
| `*`      | `__mul__`     |
| `/`      | `__truediv__` |
| `==`     | `__eq__`      |
| `<`      | `__lt__`      |
| `>`      | `__gt__`      |

Example with strings:

```python
a = "1"
b = "1"

print(a + b)
print(str.__add__(a, b))
```

Output

```
11
11
```

Example with lists:

```python
a = [1]
b = [2]

print(a + b)
print(list.__add__(a, b))
```

Output

```
[1, 2]
```

Different types can therefore define **different meanings for the same operator**.

---

# 4. Expressions

An **expression** is any piece of code that evaluates to a value.

Examples:

```python
3 + 5
len([1,2,3])
x > 0
```

Each expression produces a result when evaluated.

### Expression evaluation

```mermaid2
flowchart LR
    A[Expression] --> B[Evaluation]
    B --> C[Value]
```

Examples:

```python
3 + 5
```

produces

```
8
```

```python
len([1,2,3])
```

produces

```
3
```

Expressions can appear inside larger expressions or statements. 

---

# 5. Statements

A **statement** is a complete instruction executed by Python.

Examples:

```python
x = 10
import math
del x
```

Statements perform actions such as:

* creating variables
* importing modules
* controlling program flow

### Expression vs statement

```mermaid2
flowchart TD
    A[Python code]

    A --> B[Expressions]
    A --> C[Statements]

    B --> D[produce values]
    C --> E[perform actions]
```

Expressions can appear inside statements:

```python
x = 3 + 5
```

Here:

* `3 + 5` is an **expression**
* `x = ...` is an **assignment statement**

Statements themselves do **not evaluate to values**. 

---

# 6. Operator Precedence

When an expression contains multiple operators, Python follows **operator precedence rules**.

Higher-precedence operators are evaluated first.

Example:

```python
2 + 3 * 4
```

Multiplication occurs before addition:

```
2 + (3 * 4)
```

Result

```
14
```

### Example with exponentiation

```python
2 + 3 * 4 ** 2
```

Evaluation order:

```
4 ** 2 = 16
3 * 16 = 48
2 + 48 = 50
```

### Precedence hierarchy

| Level   | Operators         |
| ------- | ----------------- |
| highest | `()`              |
|         | `**`              |
|         | `* /`             |
|         | `+ -`             |
|         | comparisons       |
| lowest  | logical operators |

### Precedence diagram

```mermaid2
flowchart TD
    A[Parentheses]
    B[Exponentiation]
    C[Multiplication / Division]
    D[Addition / Subtraction]
    E[Comparisons]
    F[Logical operators]

    A --> B --> C --> D --> E --> F
```

Parentheses override precedence:

```python
(2 + 3) * 4
```

Result

```
20
```

---

# 7. Associativity

When operators have the same precedence, **associativity** determines evaluation order.

Most operators associate **left-to-right**.

Example:

```python
10 - 5 - 2
```

Evaluation:

```
(10 - 5) - 2 = 3
```

Exponentiation associates **right-to-left**.

Example:

```python
2 ** 3 ** 2
```

Evaluation:

```
2 ** (3 ** 2)
```

Result

```
512
```

---

# 8. Logical Operators and Short-Circuiting

Logical operators include:

| Operator | Meaning          |
| -------- | ---------------- |
| `and`    | logical AND      |
| `or`     | logical OR       |
| `not`    | logical negation |

Python evaluates logical expressions using **short-circuit evaluation**.

### AND

Evaluation stops when the result becomes false.

Example:

```python
False and print("hello")
```

`print()` is never executed.

### OR

Evaluation stops when the result becomes true.

Example:

```python
True or print("hello")
```

Again, `print()` is not executed.

### Short-circuit visualization

```mermaid2
flowchart LR
    A[Evaluate first operand]
    A --> B{Result known?}
    B -->|yes| C[Stop evaluation]
    B -->|no| D[Evaluate second operand]
```

Short-circuiting is useful for guard expressions:

```python
x is not None and x.method()
```

The method call only occurs if `x` is not `None`. 

---

# 9. Type Promotion

When operands have different numeric types, Python **promotes the result to the wider type**.

Example:

```python
1 + 1.5
```

Result

```
2.5
```

This occurs because:

```
int + float → float
```

Another example:

```python
True + 2
```

Result

```
3
```

because `bool` is a subclass of `int`.

---

# 10. Conditional Expressions

Python provides a compact conditional expression called the **ternary operator**.

Syntax:

```
value_if_true if condition else value_if_false
```

Example:

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

Result:

```
adult
```

### Visualization

```mermaid2
flowchart TD
    A[Condition]
    A -->|True| B[value_if_true]
    A -->|False| C[value_if_false]
```

---

# 11. Assignment Expressions (Walrus Operator)

Python 3.8 introduced the **assignment expression** operator `:=`.

Example:

```python
if (n := len(items)) > 10:
    print(n)
```

Here the variable `n` is assigned and used in the same expression.

This can simplify code involving repeated computations. 

---

# 12. Worked Examples

### Example 1 — operator precedence

```python
2 + 3 * 4 ** 2
```

Step-by-step:

```
4 ** 2 = 16
3 * 16 = 48
2 + 48 = 50
```

Result

```
50
```

---

### Example 2 — logical evaluation

```python
False and (5 / 0)
```

Result

```
False
```

The division is never evaluated.

---

### Example 3 — ternary expression

```python
temperature = 30
state = "hot" if temperature > 25 else "cool"
```

Result

```
hot
```

---

# 13. Concept Checks

1. What is the difference between an operator and an operand?
2. Why does `a + b` correspond to a method call in Python?
3. What distinguishes expressions from statements?
4. Why does `False and something()` skip evaluating `something()`?
5. Why does `1 + 1.5` produce a float?

---

# 14. Practice Problems

1. Evaluate:

```
5 + 3 * 2
```

2. Evaluate:

```
2 ** 3 ** 2
```

3. What value does this produce?

```python
True + True + False
```

4. Rewrite the expression using parentheses:

```
2 + 4 * 5
```

5. Write a conditional expression that returns `"positive"` if `x > 0` and `"nonpositive"` otherwise.

---

# 15. Summary

Key ideas from this chapter:

* **operators** perform actions on operands
* operators correspond to **special methods**
* **expressions evaluate to values**
* **statements perform actions**
* Python evaluates expressions using **precedence and associativity**
* logical operators use **short-circuit evaluation**
* Python supports **conditional expressions and assignment expressions**

These rules determine how Python **interprets and executes code**.

