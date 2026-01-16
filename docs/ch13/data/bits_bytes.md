# Bits and Bytes

## The Bit: Foundation of Digital Computing

A **bit** (binary digit) is the smallest unit of data—it can be either 0 or 1.

```
Physical representations of bits:

Voltage:     Low (0V) = 0    High (5V) = 1
Magnetism:   North = 0       South = 1
Light:       Off = 0         On = 1
Transistor:  Off = 0         On = 1
```

Everything in a computer—numbers, text, images, programs—is ultimately stored as patterns of bits.

## The Byte: Practical Unit

A **byte** is 8 bits, the standard unit for measuring data:

```
1 byte = 8 bits

┌───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │ 1 │  = 101 in decimal
└───┴───┴───┴───┴───┴───┴───┴───┘
 bit bit bit bit bit bit bit bit
  7   6   5   4   3   2   1   0
 MSB                         LSB
(most significant)    (least significant)
```

### Why 8 Bits?

- 2⁸ = 256 possible values (0-255)
- Enough for ASCII characters (128 values)
- Convenient for hexadecimal (2 hex digits)
- Historical: early microprocessors used 8-bit buses

## Data Size Units

| Unit | Bytes | Bits | Example |
|------|-------|------|---------|
| **Bit (b)** | 1/8 | 1 | Single binary digit |
| **Byte (B)** | 1 | 8 | One ASCII character |
| **Kilobyte (KB)** | 1,024 | 8,192 | Short text file |
| **Megabyte (MB)** | 1,048,576 | 8,388,608 | MP3 song |
| **Gigabyte (GB)** | ~1 billion | ~8 billion | HD movie |
| **Terabyte (TB)** | ~1 trillion | ~8 trillion | Large hard drive |

### Binary vs Decimal Prefixes

```
Binary (IEC):                    Decimal (SI):
1 KiB = 1,024 bytes             1 KB = 1,000 bytes
1 MiB = 1,048,576 bytes         1 MB = 1,000,000 bytes
1 GiB = 1,073,741,824 bytes     1 GB = 1,000,000,000 bytes

Storage manufacturers use decimal (makes drives look bigger!)
Operating systems often use binary (more accurate for memory)
```

## Bit Operations

### AND, OR, XOR, NOT

```
AND (&): Both bits must be 1
  1 AND 1 = 1
  1 AND 0 = 0
  0 AND 1 = 0
  0 AND 0 = 0

OR (|): At least one bit must be 1
  1 OR 1 = 1
  1 OR 0 = 1
  0 OR 1 = 1
  0 OR 0 = 0

XOR (^): Exactly one bit must be 1
  1 XOR 1 = 0
  1 XOR 0 = 1
  0 XOR 1 = 1
  0 XOR 0 = 0

NOT (~): Flip the bit
  NOT 1 = 0
  NOT 0 = 1
```

### Python Bitwise Operations

```python
a = 0b1100  # 12 in decimal
b = 0b1010  # 10 in decimal

print(bin(a & b))   # 0b1000 (AND)
print(bin(a | b))   # 0b1110 (OR)
print(bin(a ^ b))   # 0b0110 (XOR)
print(bin(~a))      # -0b1101 (NOT, with two's complement)
```

### Bit Shifting

```python
x = 0b0001  # 1

# Left shift: multiply by 2^n
print(bin(x << 1))  # 0b0010 (2)
print(bin(x << 2))  # 0b0100 (4)
print(bin(x << 3))  # 0b1000 (8)

# Right shift: divide by 2^n (floor)
y = 0b1000  # 8
print(bin(y >> 1))  # 0b0100 (4)
print(bin(y >> 2))  # 0b0010 (2)
```

## Common Data Type Sizes

| Type | Bytes | Bits | Range/Values |
|------|-------|------|--------------|
| `bool` | 1 | 8 | True/False (wastes 7 bits!) |
| `char` | 1 | 8 | 0-255 or -128 to 127 |
| `int16` | 2 | 16 | -32,768 to 32,767 |
| `int32` | 4 | 32 | -2.1B to 2.1B |
| `int64` | 8 | 64 | ±9.2 × 10¹⁸ |
| `float32` | 4 | 32 | ~7 decimal digits |
| `float64` | 8 | 64 | ~15 decimal digits |

## Python's Bit/Byte Functions

```python
# Number of bits needed to represent an integer
x = 255
print(x.bit_length())  # 8

x = 256
print(x.bit_length())  # 9

# Count set bits (1s)
x = 0b11011
print(bin(x).count('1'))  # 4

# Python 3.10+
print(x.bit_count())  # 4

# Convert to/from bytes
x = 1000
b = x.to_bytes(2, byteorder='big')    # b'\x03\xe8'
print(int.from_bytes(b, byteorder='big'))  # 1000
```

## Byte Order (Endianness)

Multi-byte values can be stored in different orders:

```
Value: 0x12345678 (4 bytes)

Big-endian (network byte order):
Address:  0    1    2    3
Bytes:   [12] [34] [56] [78]
         MSB             LSB

Little-endian (x86, ARM):
Address:  0    1    2    3
Bytes:   [78] [56] [34] [12]
         LSB             MSB
```

```python
import sys
print(sys.byteorder)  # 'little' on most modern systems

x = 0x12345678
print(x.to_bytes(4, 'big'))     # b'\x12\x34\x56\x78'
print(x.to_bytes(4, 'little'))  # b'\x78\x56\x34\x12'
```

## Bits in NumPy

```python
import numpy as np

# Explicit bit widths
arr8 = np.array([1, 2, 3], dtype=np.int8)    # 1 byte each
arr64 = np.array([1, 2, 3], dtype=np.int64)  # 8 bytes each

print(arr8.nbytes)   # 3 bytes
print(arr64.nbytes)  # 24 bytes

# View bytes directly
arr = np.array([256], dtype=np.int16)
print(arr.tobytes())  # b'\x00\x01' (little-endian)

# Bit manipulation with NumPy
a = np.array([0b1100, 0b1010], dtype=np.uint8)
b = np.array([0b1010, 0b0101], dtype=np.uint8)
print(np.bitwise_and(a, b))  # [8 0] = [0b1000, 0b0000]
```

## Practical Applications

### Flags and Bitmasks

```python
# Permission flags (like Unix file permissions)
READ = 0b100    # 4
WRITE = 0b010   # 2
EXECUTE = 0b001 # 1

# Combine permissions
user_perms = READ | WRITE  # 0b110 = 6

# Check permission
if user_perms & READ:
    print("Can read")

# Add permission
user_perms |= EXECUTE  # 0b111 = 7

# Remove permission
user_perms &= ~WRITE   # 0b101 = 5
```

### Compact Data Storage

```python
import numpy as np

# Store 8 boolean values in 1 byte instead of 8
flags = np.packbits([True, False, True, True, False, False, True, False])
print(flags)  # [178] = 0b10110010

# Unpack
unpacked = np.unpackbits(flags)
print(unpacked)  # [1 0 1 1 0 0 1 0]
```

## Summary

| Concept | Description |
|---------|-------------|
| **Bit** | Binary digit, 0 or 1 |
| **Byte** | 8 bits, 256 possible values |
| **MSB/LSB** | Most/Least Significant Bit |
| **Endianness** | Byte order in multi-byte values |
| **Bitwise ops** | AND, OR, XOR, NOT, shifts |

Key points:

- All computer data is ultimately bits
- 1 byte = 8 bits = 256 possible values
- Know your data type sizes for memory estimation
- Bitwise operations enable compact storage and fast computation
- Endianness matters when reading binary data across systems
