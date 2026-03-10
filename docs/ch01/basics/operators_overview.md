# Operators Overview

Operators are symbols or keywords that perform operations on values. Python groups them into six categories, each with defined precedence rules.

## Definition

An **operator** acts on one or more **operands** to produce a result. Python's operator categories: **arithmetic** (`+`, `-`, `*`, `/`, `//`, `%`, `**`), **comparison** (`==`, `!=`, `<`, `>`, `<=`, `>=`), **logical** (`and`, `or`, `not`), **assignment** (`=`, `+=`, `-=`, etc.), **membership** (`in`, `not in`), and **identity** (`is`, `is not`).

## Explanation

**Arithmetic**: `/` always returns `float`; `//` performs floor division (rounds toward negative infinity: `-7 // 2` is `-4`); `**` is right-associative (`2 ** 3 ** 2` equals `2 ** 9`).

**Comparison**: Returns `bool`. Python supports chaining: `0 < x < 10` is equivalent to `x > 0 and x < 10`. Strings compare lexicographically.

**Logical**: `and` returns the first falsy operand (or the last); `or` returns the first truthy operand (or the last). Both short-circuit: unevaluated operands are never executed.

**Membership**: `in` checks containment in sequences, sets, and dict keys. Time complexity is O(1) for `set`/`dict`, O(n) for `list`/`tuple`.

**Identity**: `is` tests whether two names reference the same object (same `id()`). Use `is` only for `None` checks; use `==` for value comparison.

**Precedence** (high to low): `**`, unary `+`/`-`/`~`, `*`/`/`/`//`/`%`, `+`/`-`, comparisons, `not`, `and`, `or`. When uncertain, use parentheses.

## Examples

```python
# Arithmetic: floor division and modulus
minutes, seconds = divmod(185, 60)  # (3, 5)
last_digit = 1234 % 10              # 4

# True division always returns float
print(6 / 2)    # 3.0
print(-7 // 2)  # -4 (toward negative infinity)
```

```python
# Chained comparison
age = 25
if 18 <= age <= 65:
    print("Working age")

# Short-circuit: safe attribute access
user = None
if user and user.is_active:
    print("Active")
```

```python
# Membership and identity
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)      # True  (O(1) for set)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)    # True  (same value)
print(x is y)    # False (different objects)

value = None
if value is None:  # always use 'is' for None
    print("No value")
```

```python
# Augmented assignment
count = 10
count += 5   # 15
count *= 2   # 30
count //= 7  # 4

message = "Hello"
message += " World"  # "Hello World"
```
