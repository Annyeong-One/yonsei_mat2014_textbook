# Format Specifiers

The format specification mini-language provides fine-grained control over value presentation. This syntax works in f-strings, `str.format()`, and the built-in `format()` function.

## Spec Structure

The complete format specification follows a structured pattern where each component is optional.

### 1. Full Grammar

The format spec syntax is: `[[fill]align][sign][#][0][width][,][.precision][type]`

```python
value = 42.5

# All components demonstrated
print(f"{value:*>+10,.1f}")
# Output: "****+42.5"

# *   = fill character
# >   = right align
# +   = show sign
# 10  = width
# ,   = thousands separator
# .1  = precision
# f   = float type
```

### 2. Component Order

Parse format specs left to right; each component has specific valid characters.

```python
pi = 3.14159

# Fill and align together
print(f"{'test':*^10}")    # ***test***

# Sign before width
print(f"{42:+5}")          #   +42

# Precision before type
print(f"{pi:.2f}")         # 3.14
```

### 3. Default Behavior

Omitted components use sensible defaults based on value type.

```python
# Strings: left-aligned
print(f"{'abc':10}")       # 'abc       '

# Numbers: right-aligned
print(f"{123:10}")         # '       123'

# Floats: 6 decimal places
print(f"{3.14159:f}")      # '3.141590'
```

## Alignment Options

Control padding character and alignment direction within specified width.

### 1. Direction Symbols

Use `<` for left, `>` for right, `^` for center alignment.

```python
val = "test"

print(f"{val:<10}")    # 'test      '
print(f"{val:>10}")    # '      test'
print(f"{val:^10}")    # '   test   '
```

### 2. Fill Characters

Any character can serve as fill; it must precede the alignment symbol.

```python
print(f"{'test':*<10}")    # 'test******'
print(f"{'test':->10}")    # '------test'
print(f"{'test':_^10}")    # '___test___'
```

### 3. Numeric Padding

The `=` alignment places padding between sign and digits.

```python
print(f"{-42:0=8}")     # '-0000042'
print(f"{42:0=+8}")     # '+0000042'

# Compare with right align
print(f"{-42:>08}")     # '00000-42'
```

## Width and Precision

Width sets minimum field size; precision limits decimal places or string length.

### 1. Minimum Width

Width specifies minimum characters; longer values are not truncated.

```python
for word in ["a", "abc", "abcdefgh"]:
    print(f"[{word:5}]")
# [a    ]
# [abc  ]
# [abcdefgh]
```

### 2. Float Precision

For floats, `.n` specifies decimal places with rounding.

```python
pi = 3.14159265

print(f"{pi:.0f}")     # 3
print(f"{pi:.2f}")     # 3.14
print(f"{pi:.4f}")     # 3.1416
```

### 3. String Truncation

For strings, `.n` truncates to maximum n characters.

```python
text = "Hello, World!"

print(f"{text:.5}")      # Hello
print(f"{text:10.5}")    # Hello     
```

## Integer Types

Integers support multiple representation bases.

### 1. Decimal Format

Use `d` for standard decimal, which is the default for integers.

```python
num = 255

print(f"{num}")        # 255
print(f"{num:d}")      # 255
print(f"{num:+d}")     # +255
print(f"{num:10d}")    #        255
```

### 2. Binary and Hex

Use `b` for binary, `x`/`X` for hexadecimal, `o` for octal.

```python
num = 255

print(f"{num:b}")      # 11111111
print(f"{num:#b}")     # 0b11111111
print(f"{num:x}")      # ff
print(f"{num:#X}")     # 0xFF
print(f"{num:o}")      # 377
```

### 3. Thousands Separator

Use `,` for comma grouping or `_` for underscore grouping.

```python
big = 1234567890

print(f"{big:,}")      # 1,234,567,890
print(f"{big:_}")      # 1_234_567_890
print(f"{big:,.0f}")   # 1,234,567,890
```

## Float Types

Floating-point numbers support fixed-point, scientific, and percentage formats.

### 1. Fixed Point

Use `f` for fixed-point notation with specified decimal places.

```python
pi = 3.14159265

print(f"{pi:f}")       # 3.141593
print(f"{pi:.2f}")     # 3.14
print(f"{pi:10.2f}")   #       3.14
print(f"{pi:010.2f}")  # 0000003.14
```

### 2. Scientific Notation

Use `e`/`E` for exponential notation.

```python
large = 1234567.89

print(f"{large:e}")      # 1.234568e+06
print(f"{large:.2e}")    # 1.23e+06
print(f"{large:.2E}")    # 1.23E+06
```

### 3. Percentage Format

Use `%` to multiply by 100 and add percent sign.

```python
ratio = 0.8567

print(f"{ratio:%}")      # 85.670000%
print(f"{ratio:.1%}")    # 85.7%
print(f"{ratio:.0%}")    # 86%
```

## Datetime Codes

Datetime objects support strftime codes within format specifiers.

### 1. Date Components

Extract year, month, and day with `%Y`, `%m`, `%d`.

```python
from datetime import datetime

dt = datetime(2025, 3, 15)

print(f"{dt:%Y-%m-%d}")      # 2025-03-15
print(f"{dt:%B %d, %Y}")     # March 15, 2025
print(f"{dt:%A}")            # Saturday
```

### 2. Time Components

Extract hour, minute, second with `%H`, `%M`, `%S`.

```python
from datetime import datetime

dt = datetime(2025, 1, 12, 14, 30, 45)

print(f"{dt:%H:%M:%S}")      # 14:30:45
print(f"{dt:%I:%M %p}")      # 02:30 PM
```

### 3. Combined Formats

Build complete datetime strings from components.

```python
from datetime import datetime

dt = datetime(2025, 1, 12, 14, 30)

# ISO format
print(f"{dt:%Y-%m-%dT%H:%M:%S}")
# 2025-01-12T14:30:00

# Log timestamp
print(f"[{dt:%Y-%m-%d %H:%M}]")
# [2025-01-12 14:30]
```

## Common Patterns

Frequently used format specifier combinations.

### 1. Currency Display

Combine symbols with number formatting.

```python
price = 1234.5

print(f"${price:,.2f}")      # $1,234.50
print(f"${price:>10,.2f}")   #  $1,234.50
```

### 2. Table Alignment

Create aligned columns for tabular display.

```python
data = [("Alice", 95.5), ("Bob", 87.3)]

for name, score in data:
    print(f"{name:<10} {score:>6.1f}")
# Alice       95.5
# Bob         87.3
```

### 3. ID Generation

Zero-padded identifiers for consistent width.

```python
for i in range(1, 4):
    print(f"ID-{i:04d}")
# ID-0001
# ID-0002
# ID-0003
```
