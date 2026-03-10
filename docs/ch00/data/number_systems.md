# Binary and Hexadecimal

Computers store data in binary, but programmers use hexadecimal and octal as compact, human-readable representations of the same bit patterns. Fluency in base conversion is essential for debugging, binary file formats, and low-level programming.

## Definition

A **number system** (or base) defines how digits map to values by position. **Binary** (base 2) uses digits 0-1; **hexadecimal** (base 16) uses digits 0-9 and A-F; **octal** (base 8) uses digits 0-7. One hex digit represents exactly 4 bits, making hex-to-binary conversion trivial.

## Explanation

Each position in a number represents a power of the base. In binary, the rightmost bit is 2^0 = 1, then 2^1 = 2, then 2^2 = 4, and so on. To convert decimal to binary, repeatedly divide by 2 and read remainders bottom-to-top.

Hexadecimal is popular because one hex digit maps to exactly 4 bits (a nibble), so one byte is always two hex digits. This makes memory dumps, color codes (#RRGGBB), and binary data far more readable than raw binary.

Python provides literal prefixes: `0b` for binary, `0x` for hex, `0o` for octal. The built-in functions `bin()`, `hex()`, `oct()` convert integers to string representations, and `int(string, base)` parses any base back to an integer.

## Examples

```python
# Literals and conversions
print(0b101101)       # 45 (binary)
print(0xFF)           # 255 (hex)
print(0o755)          # 493 (octal -- Unix permissions: rwxr-xr-x)

# Integer to string in any base
print(bin(45))        # '0b101101'
print(hex(255))       # '0xff'
print(oct(493))       # '0o755'

# String to integer from any base
print(int('101101', 2))  # 45
print(int('FF', 16))     # 255
```

```python
# Hex is compact binary: group bits by 4
# Binary: 1010 1111 0011 1100
# Hex:      A    F    3    C
print(hex(0b1010111100111100))  # '0xaf3c'
```

```python
# Practical: extract RGB color components
color = 0x3498DB
r = (color >> 16) & 0xFF  # 52
g = (color >> 8) & 0xFF   # 152
b = color & 0xFF           # 219
print(f"RGB({r}, {g}, {b})")  # RGB(52, 152, 219)
```

```python
# Fixed-width formatting (no prefix)
print(format(45, '08b'))   # '00101101' (8-bit binary)
print(format(255, '02x'))  # 'ff' (2-digit hex)

# Bytes and hex strings
data = bytes([0xDE, 0xAD, 0xBE, 0xEF])
print(data.hex())                    # 'deadbeef'
print(bytes.fromhex('deadbeef'))     # b'\xde\xad\xbe\xef'
```
