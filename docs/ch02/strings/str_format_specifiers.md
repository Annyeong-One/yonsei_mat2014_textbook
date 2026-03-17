# Format Specifiers

Python's **format specification mini-language** controls how values are displayed in:

* **f-strings**
* `str.format()`
* the built-in `format()` function

The basic syntax is:

```
{value:format_spec}
```

Example:

```python
value = 42.5
print(f"{value:.1f}")   # 42.5
```

| Part    | Meaning                     |
| ------- | --------------------------- |
| `value` | object being formatted      |
| `:`     | begins the format specifier |
| `.1f`   | formatting instructions     |

---

## Basic Alignment

Format specifiers can align text within a specified width.

| Symbol | Meaning      |
| ------ | ------------ |
| `<`    | left align   |
| `>`    | right align  |
| `^`    | center align |

```python
text = "test"

print(f"{text:<10}")   # 'test      '
print(f"{text:>10}")   # '      test'
print(f"{text:^10}")   # '   test   '
```

These correspond to the string alignment methods from the previous chapter:

| Method       | Format Spec |
| ------------ | ----------- |
| `ljust(10)`  | `:<10`      |
| `rjust(10)`  | `:>10`      |
| `center(10)` | `:^10`      |

---

## Fill Characters

A fill character may be placed before the alignment symbol.

```python
print(f"{'test':*<10}")   # test******
print(f"{'test':->10}")   # ------test
print(f"{'test':_^10}")   # ___test___
```

The `=` alignment places padding between the sign and the digits.

```python
print(f"{-42:0=8}")     # -0000042
print(f"{42:0=+8}")     # +0000042
```

---

## Width

Width specifies the **minimum field size**.

```python
for word in ["a", "abc", "abcdefgh"]:
    print(f"[{word:5}]")
```

Output:

```
[a    ]
[abc  ]
[abcdefgh]
```

Values longer than the width are **not truncated**.

Default alignment depends on the value type:

```python
# Strings: left-aligned
print(f"{'abc':10}")       # 'abc       '

# Numbers: right-aligned
print(f"{123:10}")         # '       123'
```

---

## Precision

Precision controls decimal places for floats or maximum length for strings. Precision rounds floating-point values.

### Float Precision

```python
pi = 3.14159265

print(f"{pi:.0f}")   # 3
print(f"{pi:.2f}")   # 3.14
print(f"{pi:.4f}")   # 3.1416
```

### String Precision

```python
text = "Hello, World!"

print(f"{text:.5}")      # Hello
print(f"{text:10.5}")    # Hello
```

---

## Numeric Formatting

Numbers support several formatting options.

---

### Sign Control

```python
print(f"{42:+}")     # +42
print(f"{-42:+}")    # -42
```

---

### Thousands Separators

```python
big = 1234567890

print(f"{big:,}")    # 1,234,567,890
print(f"{big:_}")    # 1_234_567_890
```

---

### Integer Bases

```python
num = 255

print(f"{num:b}")     # binary
print(f"{num:x}")     # hexadecimal
print(f"{num:o}")     # octal
```

With prefixes:

```python
print(f"{num:#b}")    # 0b11111111
print(f"{num:#X}")    # 0xFF
```

---

## Floating-Point Types

### Fixed Point

```python
pi = 3.14159265

print(f"{pi:f}")       # 3.141593
print(f"{pi:.2f}")     # 3.14
print(f"{pi:10.2f}")   #       3.14
```

---

### Scientific Notation

```python
large = 1234567.89

print(f"{large:e}")      # 1.234568e+06
print(f"{large:.2e}")    # 1.23e+06
print(f"{large:.2E}")    # 1.23E+06
```

---

### Percentage

```python
ratio = 0.8567

print(f"{ratio:%}")      # 85.670000%
print(f"{ratio:.1%}")    # 85.7%
print(f"{ratio:.0%}")    # 86%
```

---

## Datetime Formatting

Datetime objects support **strftime codes** inside format specifiers. These codes are part of the `datetime.strftime` syntax, not the format mini-language itself.

```python
from datetime import datetime

dt = datetime(2025, 3, 15)

print(f"{dt:%Y-%m-%d}")     # 2025-03-15
print(f"{dt:%B %d, %Y}")    # March 15, 2025
print(f"{dt:%A}")           # Saturday
```

Time components:

```python
dt = datetime(2025, 1, 12, 14, 30, 45)

print(f"{dt:%H:%M:%S}")   # 14:30:45
print(f"{dt:%I:%M %p}")   # 02:30 PM
```

---

## Common Patterns

### Currency Formatting

```python
price = 1234.5

print(f"${price:,.2f}")     # $1,234.50
print(f"${price:>10,.2f}")  #  $1,234.50
```

---

### Table Alignment

```python
data = [("Alice", 95.5), ("Bob", 87.3)]

for name, score in data:
    print(f"{name:<10} {score:>6.1f}")
```

Output:

```
Alice       95.5
Bob         87.3
```

---

### ID Generation

```python
for i in range(1, 4):
    print(f"ID-{i:04d}")
```

Output:

```
ID-0001
ID-0002
ID-0003
```

---

## Full Format Specification Grammar

The complete format specification pattern is:

```
[[fill]align][sign][#][0][width][,][.precision][type]
```

Example combining multiple components:

```python
value = 42.5

print(f"{value:*>+10,.1f}")
# ****+42.5
```

| Component | Meaning              |
| --------- | -------------------- |
| fill      | padding character    |
| align     | `<`, `>`, `^`, `=`   |
| sign      | `+`, `-`, or space   |
| width     | minimum field size   |
| `,`       | thousands separator  |
| precision | decimal digits       |
| type      | value representation |

---

## Key Takeaways

* Format specifiers control how values are displayed.
* The syntax is `{value:format_spec}`.
* Alignment uses `<`, `>`, and `^`.
* Width defines minimum field size.
* Precision controls decimal places or string length.
* Numeric types support bases, separators, and signs.
* Datetime formatting uses `strftime` codes.
* Format specifiers are commonly used in **tables, reports, and numeric displays**.
