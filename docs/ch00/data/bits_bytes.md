# Bits and Bytes

## The Bit: Foundation of Digital Computing

A **bit** (binary digit) is the smallest unit of data—it can be either 0 or 1.

```
Physical representations of bits:

Voltage:     Low voltage  = 0    High voltage = 1
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
│ 0 │ 1 │ 1 │ 0 │ 0 │ 1 │ 0 │ 1 │  ← example byte
└───┴───┴───┴───┴───┴───┴───┴───┘
 bit bit bit bit bit bit bit bit
  7   6   5   4   3   2   1   0
 MSB                         LSB
(most significant)    (least significant)
```

### Why 8 Bits?

- 2⁸ = 256 possible values (0-255)
- Originally enough for ASCII characters (128 values); modern text uses Unicode (UTF-8)
- Convenient for hexadecimal (2 hex digits)
- Historical: early microprocessors used 8-bit buses

## Storage Unit Prefixes: IEC (Binary) vs SI (Decimal)

| Unit | Bytes | Bits | Example |
|------|-------|------|---------|
| **Bit (b)** | 1/8 | 1 | Single binary digit |
| **Byte (B)** | 1 | 8 | One ASCII character |
| **Kilobyte (KB)** | 1,000 | 8,000 | Short text file |
| **Kibibyte (KiB)** | 1,024 | 8,192 | Short text file |
| **Megabyte (MB)** | 1,000,000 | 8,000,000 | MP3 song |
| **Mebibyte (MiB)** | 1,048,576 | 8,388,608 | MP3 song |
| **Gigabyte (GB)** | 1,000,000,000 | 8,000,000,000 | High-resolution video file |
| **Gibibyte (GiB)** | 1,073,741,824 | 8,589,934,592 | High-resolution video file |
| **Terabyte (TB)** | 1,000,000,000,000 | 8,000,000,000,000 | Large hard drive |
| **Tebibyte (TiB)** | 1,099,511,627,776 | 8,796,093,022,208 | Large hard drive |

### IEC vs SI Comparison

```
Binary (IEC):                    Decimal (SI):
1 KiB = 1,024 bytes             1 KB = 1,000 bytes
1 MiB = 1,048,576 bytes         1 MB = 1,000,000 bytes
1 GiB = 1,073,741,824 bytes     1 GB = 1,000,000,000 bytes
```

Storage manufacturers use decimal (makes drives look bigger!)
Operating systems often use binary (more accurate for memory)


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

XOR (^): True if exactly one of two bits is 1
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

> **Note on `0b` prefix**: `0b` is Python's binary literal prefix — it tells the interpreter the number is written in base 2, not base 10. The leading `0` is part of the prefix, not a sign indicator. For negative binary, write `-0b0001`. Python uses the same prefix convention for other bases: `0o` for octal and `0x` for hexadecimal. Leading zeros inside the literal (e.g. `0b0001` vs `0b1`) are just padding for readability — the value is identical.

### Bit Shifting

```python
x = 0b0001  # 1 

# Left shift: multiply by 2^n
print(bin(x << 1))  # 0b0010 (2)
print(bin(x << 2))  # 0b0100 (4)
print(bin(x << 3))  # 0b1000 (8)
```



## Common Data Type Sizes (C/C++ primitives)

> **Note**: These sizes apply to **C/C++ primitive types**, not Python. In Python, `int` is arbitrary precision, `bool` is a full object (~28 bytes), and there is no `char` type. Use `numpy` dtypes (e.g. `np.int32`) when you need fixed-width types in Python.

| Type | Bytes | Bits | Range/Values |
|------|-------|------|--------------|
| `bool` | 1 | 8 | True/False (1 bit of info; 1 byte in C; ~28 bytes in CPython) |
| `char` | 1 | 8 | 0-255 or -128 to 127 |
| `int16` | 2 | 16 | -32,768 to 32,767 |
| `int32` | 4 | 32 | -2.1B to 2.1B |
| `int64` | 8 | 64 | ±9.2 × 10¹⁸ |
| `float32` | 4 | 32 | ~7 decimal digits |
| `float64` | 8 | 64 | ~15 decimal digits |

> **Why does `bool` use so much space?** Most modern CPUs are **byte-addressable** — the smallest directly addressable unit is a byte, not a bit — so a C `bool` occupies 1 byte even though it only needs 1 bit of information. In CPython, however, `bool` is a full Python object (a subclass of `int`) and occupies around 28 bytes due to object overhead. Note that bit-addressable hardware does exist (e.g. Intel 8051, some DSPs), so byte-addressability is the norm, not a universal rule. If you need to pack multiple booleans efficiently, use bitmasks or `numpy.packbits()` (see Practical Applications).

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

# Python 3.10+: avoids string conversion, faster
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

> **Why little-endian on most modern systems?** Big-endian feels more natural to humans (most significant byte first, like how we write numbers), but little-endian won the hardware war for two key reasons:
>
> 1. **Free integer size casting**: With little-endian, a 1-byte and 4-byte integer at the same address share the same first byte correctly — reading fewer bytes always gives the right smaller value. With big-endian you'd read the wrong byte.
>
> 2. **Intel won**: x86 used little-endian and became the dominant PC architecture. ARM later adopted little-endian as default too. Network protocols (TCP/IP) went the other way, standardizing on big-endian — which is why big-endian is also called "network byte order."

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
