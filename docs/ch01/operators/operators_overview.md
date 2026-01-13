# Operators Overview

Operators are special symbols that perform operations on values (operands). Python provides several categories of operators.


## Operators and Operands

```python
result = 10 + 5
#        ^  ^ ^
#        |  | operand
#        |  operator
#        operand
```

- **Operator**: Symbol that performs an operation (`+`, `-`, `*`, etc.)
- **Operand**: Value the operator acts upon


## Operator Categories

| Category | Operators | Example |
|----------|-----------|---------|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `3 + 2` |
| Comparison | `==`, `!=`, `<`, `>`, `<=`, `>=` | `3 > 2` |
| Logical | `and`, `or`, `not` | `True and False` |
| Assignment | `=`, `+=`, `-=`, `*=`, etc. | `x += 1` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` | `5 & 3` |
| Identity | `is`, `is not` | `x is None` |
| Membership | `in`, `not in` | `'a' in 'cat'` |


## Quick Examples

```python
# Arithmetic
print(10 + 3)   # 13
print(10 / 3)   # 3.333...
print(10 // 3)  # 3 (floor division)
print(10 % 3)   # 1 (remainder)
print(2 ** 3)   # 8 (power)

# Comparison
print(5 > 3)    # True
print(5 == 5)   # True

# Logical
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Identity
x = [1, 2]
y = [1, 2]
print(x == y)   # True (same value)
print(x is y)   # False (different objects)

# Membership
print('a' in 'cat')     # True
print(3 in [1, 2, 3])   # True
```


## Operator Behavior Depends on Types

The same operator can behave differently based on operand types:

```python
# + with numbers: addition
print(3 + 2)        # 5

# + with strings: concatenation
print("Hello" + " World")  # "Hello World"

# + with lists: concatenation
print([1, 2] + [3, 4])     # [1, 2, 3, 4]

# * with number and string: repetition
print("ab" * 3)     # "ababab"

# * with number and list: repetition
print([1, 2] * 2)   # [1, 2, 1, 2]
```


## Summary

- Operators perform operations on operands
- Python has 7 main operator categories
- Operator behavior can vary by operand type
- See specific pages for details on each category
