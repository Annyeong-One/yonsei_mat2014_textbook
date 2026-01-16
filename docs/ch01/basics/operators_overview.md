# Operators Overview

Operators are special symbols that perform operations on values (operands). Python provides a rich set of operators for arithmetic, comparison, logic, and more.

---

## Categories of Operators

| Category | Purpose | Examples |
|----------|---------|----------|
| Arithmetic | Mathematical calculations | `+`, `-`, `*`, `/` |
| Comparison | Compare values | `==`, `!=`, `<`, `>` |
| Logical | Combine conditions | `and`, `or`, `not` |
| Assignment | Assign values | `=`, `+=`, `-=` |
| Membership | Check containment | `in`, `not in` |
| Identity | Check object identity | `is`, `is not` |

---

## Arithmetic Operators

Perform mathematical operations on numbers.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `7 / 2` | `3.5` |
| `//` | Floor Division | `7 // 2` | `3` |
| `%` | Modulus (remainder) | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Examples

```python
# Basic arithmetic
a = 10
b = 3

print(a + b)   # 13  (addition)
print(a - b)   # 7   (subtraction)
print(a * b)   # 30  (multiplication)
print(a / b)   # 3.333...  (true division)
print(a // b)  # 3   (floor division - rounds down)
print(a % b)   # 1   (remainder)
print(a ** b)  # 1000 (10 to the power of 3)
```

### Division Types

```python
# True division (always returns float)
print(7 / 2)    # 3.5
print(6 / 2)    # 3.0 (still a float!)

# Floor division (rounds down to integer)
print(7 // 2)   # 3
print(-7 // 2)  # -4 (rounds toward negative infinity)

# Modulus (remainder after division)
print(7 % 3)    # 1 (7 = 3*2 + 1)
print(10 % 3)   # 1 (10 = 3*3 + 1)
```

### Practical Uses

```python
# Check if number is even or odd
num = 17
if num % 2 == 0:
    print("Even")
else:
    print("Odd")  # Output: Odd

# Extract digits
number = 1234
last_digit = number % 10      # 4
remaining = number // 10      # 123

# Convert seconds to minutes and seconds
total_seconds = 185
minutes = total_seconds // 60  # 3
seconds = total_seconds % 60   # 5
print(f"{minutes}:{seconds:02d}")  # 3:05
```

---

## Comparison Operators

Compare two values and return `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 3` | `False` |

### Examples

```python
x = 10
y = 5

print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= 10)  # True
print(y <= 5)   # True
```

### Chained Comparisons

Python allows chaining comparisons naturally:

```python
x = 5

# Instead of: x > 0 and x < 10
print(0 < x < 10)    # True

# Multiple chains
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 0)     # True (1 < 2 and 2 > 0)

# Practical example
age = 25
if 18 <= age <= 65:
    print("Working age")
```

### Comparing Strings

Strings compare lexicographically (dictionary order):

```python
print("apple" < "banana")   # True (a comes before b)
print("cat" > "car")        # True (t comes after r)
print("Python" == "python") # False (case-sensitive)
```

---

## Logical Operators

Combine boolean expressions.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both must be True | `True and False` | `False` |
| `or` | At least one True | `True or False` | `True` |
| `not` | Inverts the value | `not True` | `False` |

### Truth Tables

**and:**
| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**or:**
| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Examples

```python
age = 25
has_license = True

# and - both conditions must be true
if age >= 18 and has_license:
    print("Can drive")

# or - at least one condition must be true
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("Day off!")

# not - inverts the boolean
is_raining = False
if not is_raining:
    print("No umbrella needed")
```

### Short-Circuit Evaluation

Python stops evaluating as soon as the result is known:

```python
# With 'and': stops at first False
False and print("Never printed")

# With 'or': stops at first True  
True or print("Never printed")

# Practical use: safe attribute access
user = None
if user and user.is_active:  # Won't error if user is None
    print("User is active")
```

---

## Assignment Operators

Assign and modify values.

| Operator | Example | Equivalent to |
|----------|---------|---------------|
| `=` | `x = 5` | Assign 5 to x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

### Examples

```python
count = 10

count += 5   # count is now 15
count -= 3   # count is now 12
count *= 2   # count is now 24
count //= 5  # count is now 4

# String concatenation
message = "Hello"
message += " World"  # "Hello World"

# List extension
numbers = [1, 2]
numbers += [3, 4]    # [1, 2, 3, 4]
```

---

## Membership Operators

Check if a value exists in a sequence.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `in` | Is member of | `'a' in 'cat'` | `True` |
| `not in` | Is not member of | `'x' not in 'cat'` | `True` |

### Examples

```python
# Strings
print('a' in 'apple')       # True
print('z' in 'apple')       # False

# Lists
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)    # True
print('grape' not in fruits) # True

# Dictionaries (checks keys)
person = {'name': 'Alice', 'age': 25}
print('name' in person)      # True
print('Alice' in person)     # False (values not checked)

# Practical use
valid_colors = ['red', 'green', 'blue']
user_input = 'purple'
if user_input not in valid_colors:
    print("Invalid color choice")
```

---

## Identity Operators

Check if two variables reference the same object in memory.

| Operator | Meaning | Example |
|----------|---------|---------|
| `is` | Same object | `a is b` |
| `is not` | Different objects | `a is not b` |

### Examples

```python
# Same object
a = [1, 2, 3]
b = a           # b references same list
print(a is b)   # True

# Different objects with same value
c = [1, 2, 3]
print(a == c)   # True (same value)
print(a is c)   # False (different objects)

# Common use: checking for None
value = None
if value is None:
    print("No value provided")

# Avoid using 'is' with integers/strings (interning)
x = 1000
y = 1000
print(x == y)   # True (always correct)
print(x is y)   # May be True or False (implementation detail)
```

### `is` vs `==`

- Use `==` to compare **values**
- Use `is` to compare **identity** (same object)
- Always use `is` for `None` comparisons

```python
# Correct
if x is None:
    pass

# Also correct but less Pythonic
if x == None:
    pass
```

---

## Operator Precedence

When multiple operators appear, Python evaluates them in this order (highest to lowest):

| Precedence | Operators |
|------------|-----------|
| 1 (highest) | `**` |
| 2 | `+x`, `-x`, `~x` (unary) |
| 3 | `*`, `/`, `//`, `%` |
| 4 | `+`, `-` |
| 5 | `<`, `<=`, `>`, `>=`, `!=`, `==` |
| 6 | `not` |
| 7 | `and` |
| 8 (lowest) | `or` |

### Examples

```python
# Exponentiation first
result = 2 + 3 ** 2    # 2 + 9 = 11

# Multiplication before addition
result = 2 + 3 * 4     # 2 + 12 = 14

# Comparison before logical
result = 5 > 3 and 2 < 4  # True and True = True

# Use parentheses for clarity
result = (2 + 3) * 4   # 5 * 4 = 20
```

### When in Doubt, Use Parentheses

```python
# Unclear
result = a and b or c and d

# Clear
result = (a and b) or (c and d)
```

---

## Special Operators

### String Operators

```python
# Concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# Repetition
line = "-" * 20  # "--------------------"

# Membership
has_at = "@" in "email@example.com"  # True
```

### List Operators

```python
# Concatenation
combined = [1, 2] + [3, 4]  # [1, 2, 3, 4]

# Repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]

# Membership
exists = 3 in [1, 2, 3, 4]  # True
```

---

## Quick Reference

```python
# Arithmetic
+ - * / // % **

# Comparison
== != < > <= >=

# Logical
and or not

# Assignment
= += -= *= /= //= %= **=

# Membership
in   not in

# Identity
is   is not
```

---

## Summary

| Category | Purpose | Key Operators |
|----------|---------|---------------|
| Arithmetic | Math operations | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Comparison | Compare values | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Logical | Boolean logic | `and`, `or`, `not` |
| Assignment | Update values | `=`, `+=`, `-=`, etc. |
| Membership | Check containment | `in`, `not in` |
| Identity | Check same object | `is`, `is not` |

**Key Points:**
- `/` always returns float, `//` returns integer (floor division)
- `%` gives the remainder (useful for even/odd checks)
- `**` is exponentiation (right-associative: `2**3**2` = `2**9`)
- Use `==` for value comparison, `is` for identity (especially `None`)
- `and`/`or` short-circuit (stop early when result is determined)
- When precedence is unclear, use parentheses
