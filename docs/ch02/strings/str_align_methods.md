# Align Methods

String alignment methods pad strings to a specified width with fill characters, useful for formatting text output.

## Basic Alignment

Left, right, and center alignment methods.

### 1. Left Justify

Use `ljust()` to left-align with right padding.

```python
s = "Hello"

print(s.ljust(10))       # 'Hello     '
print(s.ljust(10, "-"))  # 'Hello-----'
print(len(s.ljust(10)))  # 10
```

### 2. Right Justify

Use `rjust()` to right-align with left padding.

```python
s = "Hello"

print(s.rjust(10))       # '     Hello'
print(s.rjust(10, "-"))  # '-----Hello'
```

### 3. Center Align

Use `center()` to center with padding on both sides.

```python
s = "Hello"

print(s.center(11))       # '   Hello   '
print(s.center(11, "-"))  # '---Hello---'

# Odd padding goes to right
print(s.center(10))       # '  Hello   '
```

## Width Behavior

How methods handle various width values.

### 1. Width Less Than Length

No truncation occurs; original string returned.

```python
s = "Hello World"

print(s.ljust(5))   # 'Hello World' (unchanged)
print(s.rjust(5))   # 'Hello World' (unchanged)
print(s.center(5))  # 'Hello World' (unchanged)
```

### 2. Exact Width

Returns string padded to exact width.

```python
s = "Hi"

print(f"[{s.ljust(10)}]")   # [Hi        ]
print(f"[{s.rjust(10)}]")   # [        Hi]
print(f"[{s.center(10)}]")  # [    Hi    ]
```

### 3. Dynamic Width

Calculate width based on content.

```python
items = ["Apple", "Banana", "Cherry"]
max_width = max(len(item) for item in items)

for item in items:
    print(item.ljust(max_width + 2) + "|")
# Apple   |
# Banana  |
# Cherry  |
```

## Zero Fill

Pad numbers with leading zeros.

### 1. Basic zfill()

Pad string with zeros to specified width.

```python
s = "42"

print(s.zfill(5))   # 00042
print(s.zfill(10))  # 0000000042
print(s.zfill(2))   # 42 (no change)
```

### 2. Sign Handling

Zeros are inserted after the sign.

```python
pos = "42"
neg = "-42"

print(pos.zfill(5))  # 00042
print(neg.zfill(5))  # -0042

# Plus sign also handled
plus = "+42"
print(plus.zfill(6))  # +00042
```

### 3. Non-Numeric Strings

Works on any string, not just numbers.

```python
s = "abc"
print(s.zfill(5))  # 00abc

# Leading sign still handled
s = "-abc"
print(s.zfill(5))  # -0abc
```

## Table Formatting

Create aligned text tables.

### 1. Simple Columns

Align data in columns.

```python
data = [
    ("Alice", 95),
    ("Bob", 87),
    ("Carol", 100)
]

for name, score in data:
    print(name.ljust(10) + str(score).rjust(5))
# Alice         95
# Bob           87
# Carol        100
```

### 2. Header with Border

Create formatted table headers.

```python
headers = ["Name", "Age", "City"]
widths = [15, 5, 12]

# Header row
header_line = ""
for h, w in zip(headers, widths):
    header_line += h.center(w) + "|"
print(header_line)
print("-" * len(header_line))

# Output:
#      Name     | Age |    City    |
# ---------------------------------
```

### 3. Receipt Style

Format receipt or invoice items.

```python
items = [
    ("Coffee", 4.50),
    ("Sandwich", 12.99),
    ("Cookie", 2.50)
]

width = 25
print("=" * width)
print("RECEIPT".center(width))
print("=" * width)

for item, price in items:
    price_str = f"${price:.2f}"
    padding = width - len(item) - len(price_str)
    print(item + "." * padding + price_str)

total = sum(p for _, p in items)
print("-" * width)
print("TOTAL".ljust(width - 7) + f"${total:.2f}")

# =========================
#         RECEIPT
# =========================
# Coffee...............\$4.50
# Sandwich...........\$12.99
# Cookie..............\$2.50
# -------------------------
# TOTAL              \$19.99
```

## ID Formatting

Format identifiers and codes.

### 1. Padded IDs

Create fixed-width identifiers.

```python
for i in range(1, 4):
    print(f"ID-{str(i).zfill(4)}")
# ID-0001
# ID-0002
# ID-0003
```

### 2. File Numbering

Number files with consistent width.

```python
files = ["report", "data", "summary"]

for i, name in enumerate(files, 1):
    filename = f"{str(i).zfill(3)}_{name}.txt"
    print(filename)
# 001_report.txt
# 002_data.txt
# 003_summary.txt
```

### 3. Time Formatting

Format time components.

```python
hours, minutes, seconds = 9, 5, 3

time_str = (
    str(hours).zfill(2) + ":" +
    str(minutes).zfill(2) + ":" +
    str(seconds).zfill(2)
)
print(time_str)  # 09:05:03
```

## Comparison Methods

Compare alignment methods.

### 1. Align vs Format Spec

Alignment methods vs format specifiers.

```python
s = "Hi"
width = 10

# Using methods
print(s.ljust(width))    # 'Hi        '
print(s.rjust(width))    # '        Hi'
print(s.center(width))   # '    Hi    '

# Using format specifiers
print(f"{s:<{width}}")   # 'Hi        '
print(f"{s:>{width}}")   # '        Hi'
print(f"{s:^{width}}")   # '    Hi    '
```

### 2. Fill Characters

Both support custom fill characters.

```python
s = "Hi"

# Methods
print(s.center(10, "*"))  # ****Hi****

# Format spec
print(f"{s:*^10}")        # ****Hi****
```

### 3. When to Use Each

Methods for variables, format specs for literals.

```python
# Method: when width/fill are variables
width = 10
fill = "-"
result = "test".center(width, fill)

# Format spec: for fixed formatting in f-strings
name = "Alice"
score = 95
print(f"{name:<10} {score:>5}")  # Alice          95
```
