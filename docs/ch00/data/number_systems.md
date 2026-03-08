# Binary and Hexadecimal

## Number Systems Overview

Computers store data in binary, but programmers often use other bases (decimal, hexadecimal, octal) to represent or interpret that data:

| Base | Name | Digits | Use Case |
|------|------|--------|----------|
| 2 | Binary | 0, 1 | Hardware, bit operations |
| 10 | Decimal | 0-9 | Human-readable, default |
| 16 | Hexadecimal | 0-9, A-F | Compact binary representation |

## Binary (Base 2)

### Place Values

Binary is a positional number system like decimal — each digit's value depends on its position. Each position represents a power of 2:

```
Binary number: 1 0 1 1 0 1
               │ │ │ │ │ │
Position:      5 4 3 2 1 0
               │ │ │ │ │ │
Power of 2:   32 16 8 4 2 1

Value = 1×32 + 0×16 + 1×8 + 1×4 + 0×2 + 1×1
      = 32 + 8 + 4 + 1
      = 45
```

### Converting Decimal to Binary

**Method: Repeated division by 2**

```
Convert 45 to binary:

45 ÷ 2 = 22 remainder 1  ↑
22 ÷ 2 = 11 remainder 0  │
11 ÷ 2 = 5  remainder 1  │ Read remainders
5  ÷ 2 = 2  remainder 1  │ bottom to top
2  ÷ 2 = 1  remainder 0  │
1  ÷ 2 = 0  remainder 1  ↓

Result: 101101
```

### Python Binary

```python
# Binary literals (prefix 0b)
x = 0b101101
print(x)  # 45

# Convert to binary string
print(bin(45))  # '0b101101'

# Parse binary string
print(int('101101', 2))  # 45

# Format without prefix
print(format(45, 'b'))  # '101101'

# Fixed width with leading zeros
print(format(45, '08b'))  # '00101101'
```

## Hexadecimal (Base 16)

### Hex Digits

```
Decimal:  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
Hex:      0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
Binary:   0000 0001 0010 0011 0100 0101 0110 0111
          1000 1001 1010 1011 1100 1101 1110 1111
```

### Why Hexadecimal?

One hex digit = exactly 4 bits. This makes conversion trivial:

```
Binary:     1010 1111 0011 1100
               ↓    ↓    ↓    ↓
Hex:           A    F    3    C

Binary to Hex: group by 4 bits, convert each group
Hex to Binary: expand each hex digit to 4 bits
```

### Place Values

```
Hex number: 2 A F
            │ │ │
Position:   2 1 0
            │ │ │
Power of 16: 256 16 1

Value = 2×256 + 10×16 + 15×1
      = 512 + 160 + 15
      = 687
```

### Python Hexadecimal

```python
# Hex literals (prefix 0x)
x = 0x2AF
print(x)  # 687

# Convert to hex string
print(hex(687))  # '0x2af'

# Parse hex string
print(int('2AF', 16))  # 687
print(int('2af', 16))  # 687 (case insensitive)

# Format without prefix
print(format(687, 'x'))  # '2af'
print(format(687, 'X'))  # '2AF' (uppercase)

# Fixed width
print(format(687, '04x'))  # '02af'
```

## Octal (Base 8)

Less common but still used (Unix file permissions):

```python
# Octal literals (prefix 0o)
x = 0o755  # Common Unix permission
print(x)  # 493

# Convert to octal
print(oct(493))  # '0o755'

# File permissions example
# rwxr-xr-x = 111 101 101 = 7 5 5
# r=4, w=2, x=1 → owner: 4+2+1=7, group: 4+0+1=5, others: 4+0+1=5
import os
os.chmod('file.txt', 0o755)
```

## Conversion Between Bases

### Quick Reference Table

(Binary values use leading zeros for 4-bit alignment where applicable.)

| Decimal | Binary | Hex | Octal |
|---------|--------|-----|-------|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 8 | 10 |
| 9 | 1001 | 9 | 11 |
| 10 | 1010 | A | 12 |
| 11 | 1011 | B | 13 |
| 12 | 1100 | C | 14 |
| 13 | 1101 | D | 15 |
| 14 | 1110 | E | 16 |
| 15 | 1111 | F | 17 |
| 16 | 10000 | 10 | 20 |
| 255 | 11111111 | FF | 377 |
| 256 | 100000000 | 100 | 400 |

### Python Conversions

```python
# Any base to decimal
print(int('1010', 2))    # 10 (binary)
print(int('FF', 16))     # 255 (hex)
print(int('77', 8))      # 63 (octal)

# Decimal to any base
print(bin(255))  # '0b11111111'
print(hex(255))  # '0xff'
print(oct(255))  # '0o377'

# General format specification
print(format(255, 'b'))  # '11111111'
print(format(255, 'x'))  # 'ff'
print(format(255, 'o'))  # '377'
print(format(255, 'd'))  # '255'
```

## Common Hex Values

### Memory and Computing

```python
# Powers of 2 in hex
print(hex(1024))      # 0x400 (1 KB)
print(hex(1048576))   # 0x100000 (1 MB)
print(hex(2**32))     # 0x100000000 (4 GB)

# Max values
print(hex(255))       # 0xff (max uint8)
print(hex(65535))     # 0xffff (max uint16)
print(hex(2**32 - 1)) # 0xffffffff (max uint32)

# Common addresses/values
print(0xDEADBEEF)     # 3735928559 (debug marker)
print(0xCAFEBABE)     # 3405691582 (Java class magic)
print(0x7FFFFFFF)     # 2147483647 (max int32)
```

### Colors (RGB)

```python
# Web colors in hex: #RRGGBB
red = 0xFF0000     # Pure red
green = 0x00FF00   # Pure green
blue = 0x0000FF    # Pure blue
white = 0xFFFFFF   # All on
black = 0x000000   # All off

# Extract components
color = 0x3498DB  # A nice blue

red_component = (color >> 16) & 0xFF    # 0x34 = 52
green_component = (color >> 8) & 0xFF   # 0x98 = 152
blue_component = color & 0xFF           # 0xDB = 219

print(f"RGB({red_component}, {green_component}, {blue_component})")
# RGB(52, 152, 219)
```

## Bytes and Hex Strings

```python
# Bytes to hex
data = bytes([0xDE, 0xAD, 0xBE, 0xEF])
print(data.hex())  # 'deadbeef'

# Hex string to bytes
data = bytes.fromhex('deadbeef')
print(list(data))  # [222, 173, 190, 239]

# Hex dump of string
text = "Hello"
print(text.encode().hex())  # '48656c6c6f'

# Spacing in hex output
data = b'\xde\xad\xbe\xef'
print(data.hex(' '))  # 'de ad be ef' (Python 3.8+)
```

## NumPy and Number Bases

```python
import numpy as np

# Create arrays from different bases
arr = np.array([0b1010, 0xFF, 0o77])
print(arr)  # [10 255 63]

# Format array as hex (requires loop or apply)
arr = np.array([10, 255, 63])
hex_strings = [format(x, '02x') for x in arr]
print(hex_strings)  # ['0a', 'ff', '3f']

# Binary representation of floats
x = np.float32(1.5)
# Reinterpret the float's memory as a 32-bit integer to inspect raw bits
print(format(x.view(np.uint32), '032b'))
# 00111111110000000000000000000000
```

## Debugging with Hex

### Memory Addresses

```python
x = [1, 2, 3]
print(hex(id(x)))  # '0x7f8b8c0a5a00' (memory address)
```

### Viewing Binary Data

```python
import struct

# Pack float to bytes
data = struct.pack('f', 3.14)
print(data.hex())  # 'c3f54840'

# Examine individual bytes
for byte in data:
    print(f'{byte:02x} = {byte:08b}')
# c3 = 11000011
# f5 = 11110101
# 48 = 01001000
# 40 = 01000000
```

## Summary

| Base | Prefix | Digits | Primary Use |
|------|--------|--------|-------------|
| Binary | `0b` | 0-1 | Bit operations, flags |
| Octal | `0o` | 0-7 | Unix permissions |
| Decimal | None | 0-9 | Default, human-readable |
| Hexadecimal | `0x` | 0-9, A-F | Memory, bytes, colors |

Key conversions:

```python
# Quick reference
int('1010', 2)   # binary string → int
int('FF', 16)    # hex string → int
bin(x)           # int → binary string
hex(x)           # int → hex string
format(x, '08b') # int → binary, fixed width
format(x, '02x') # int → hex, fixed width
```

Understanding these number systems helps when:

- Debugging memory issues
- Working with binary file formats
- Handling colors and graphics
- Setting flags and permissions
- Reading low-level documentation
