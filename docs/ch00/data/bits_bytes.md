# Bits and Bytes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Bit: Foundation of Digital Computing

A **bit** (binary digit) is the smallest unit of information in digital systems—it can be either 0 or 1.

```
Physical representations of bits:

Voltage:        Low voltage  = 0    High voltage = 1
Magnetization:  One direction = 0   Other direction = 1
Light:          Off = 0             On = 1
Transistor:     Off = 0             On = 1
```

Everything in a computer—numbers, text, images, programs—is ultimately represented as patterns of bits interpreted according to encoding rules.

> **Prerequisite**: This page uses binary numbers (e.g. `0b1100` = 12). If you are not yet comfortable reading base-2 notation, see [Binary and Hexadecimal](number_systems.md) first.

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
- Fits extended character sets (7-bit ASCII only needs 128 values, but 8 bits accommodates larger encodings); modern text uses Unicode (UTF-8)
- Convenient for hexadecimal (1 byte = 2 hex digits, since each hex digit represents 4 bits)
- Convenient hardware alignment (powers of two simplify circuit design)
- Historical: IBM System/360 (1964) standardized the 8-bit byte; early microprocessors followed with 8-bit buses

## Storage Unit Prefixes: IEC (Binary) vs SI (Decimal)

| Unit | Bytes | Bits | Example |
|------|-------|------|---------|
| **Bit (b)** | 1/8 | 1 | Single binary digit |
| **Byte (B)** | 1 | 8 | One ASCII character (7-bit encoding) |
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
Operating systems often use binary units for memory (RAM)

> **Note**: Historically many operating systems displayed binary units but labeled them using decimal prefixes (GB instead of GiB), which caused confusion. Modern macOS uses decimal prefixes correctly, while Windows still shows binary values with decimal labels.


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

> **Note on `~` (bitwise NOT)**: Python integers are unbounded signed integers using two's complement semantics, so `~x` equals `-(x + 1)`. For example, `~12` is `-13`. This differs from fixed-width languages (like C) where NOT flips a fixed number of bits. For a full explanation of two's complement representation, see [Integer Representation](integer_representation.md).

> **Note on `0b` prefix**: `0b` is Python's binary literal prefix — it tells the interpreter the number is written in base 2, not base 10. The leading `0` is part of the prefix, not a sign indicator. For negative binary, write `-0b0001`. Python uses the same prefix convention for other bases: `0o` for octal and `0x` for hexadecimal. Leading zeros inside the literal (e.g. `0b0001` vs `0b1`) are just padding for readability — the value is identical.

### Bit Shifting

```python
x = 0b0001  # 1 

# Left shift: multiply by 2^n (assuming no overflow in fixed-width types)
print(bin(x << 1))  # 0b0010 (2)
print(bin(x << 2))  # 0b0100 (4)
print(bin(x << 3))  # 0b1000 (8)
```

> **Note**: In Python, left shift always equals multiplication by 2ⁿ because integers have arbitrary precision. In fixed-width languages (C, Java), left shift can overflow and produce incorrect results.



## Common Data Type Sizes

> **Note**: The sizes below apply to **C/C++ types**, not Python. In Python, `int` is arbitrary precision, `bool` is a full object (~28 bytes), and there is no `char` type. Use `numpy` dtypes (e.g. `np.int32`) when you need fixed-width types in Python. Note that `char` is the only type whose size (1 byte) is guaranteed by the C standard; `int` is implementation-dependent (commonly 4 bytes on modern platforms). The fixed-width types (`int16_t`, `int32_t`, etc.) come from `<stdint.h>`.

| Type | Bytes | Bits | Range/Values |
|------|-------|------|--------------|
| `bool` | 1 | 8 | True/False (1 bit of info; 1 byte in C; ~28 bytes in CPython) |
| `char` | 1 | 8 | 0-255 or -128 to 127 |
| `int16_t` | 2 | 16 | -32,768 to 32,767 |
| `int32_t` | 4 | 32 | -2.1B to 2.1B |
| `int64_t` | 8 | 64 | ±9.2 × 10¹⁸ |
| `float` | 4 | 32 | ~7 decimal digits (IEEE-754) |
| `double` | 8 | 64 | ~15 decimal digits (IEEE-754) |

> **Why does `bool` use so much space?** Most general-purpose CPUs are **byte-addressable** — the smallest directly addressable unit is a byte, not a bit — so a C `bool` occupies 1 byte even though it only needs 1 bit of information. In CPython, however, `bool` is a full Python object (a subclass of `int`) and occupies around 28 bytes due to object overhead. Note that bit-addressable hardware does exist (e.g. Intel 8051, some DSPs), so byte-addressability is the norm, not a universal rule. C also provides **bit fields** (`struct { unsigned flag : 1; }`) for packing multiple booleans into fewer bytes. If you need to pack multiple booleans efficiently in Python, use bitmasks or `numpy.packbits()` (see Practical Applications).

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

> **Why little-endian on most modern systems?** Big-endian feels more natural to humans (most significant byte first, like how we write numbers), but little-endian became dominant for several reasons:
>
> 1. **Free integer size casting**: With little-endian, a 1-byte and 4-byte integer at the same address share the same first byte correctly — reading fewer bytes always gives the right smaller value. With big-endian you'd read the wrong byte.
>
> 2. **Efficient variable-length arithmetic**: Addition starts from the least significant byte, which is at the lowest address in little-endian — no need to calculate the end address first.
>
> 3. **x86 dominance**: Intel's x86 used little-endian and became the dominant PC architecture. ARM originally supported both endian modes (bi-endian) but adopted little-endian as default. Many older architectures (SPARC, MIPS, Motorola 68k) were big-endian. Network protocols (TCP/IP) standardized on big-endian — which is why big-endian is also called "network byte order."

### Byte Order in Practice

When reading binary files or network data, you must know the byte order. Python's `struct` module handles this:

```python
import struct

# Pack an integer as big-endian (>) and little-endian (<)
big = struct.pack('>I', 0x12345678)     # b'\x12\x34\x56\x78'
little = struct.pack('<I', 0x12345678)  # b'\x78\x56\x34\x12'

# Unpack from a known byte order
value = struct.unpack('>I', big)[0]     # 0x12345678
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
print(arr.tobytes())  # b'\x00\x01' (little-endian representation of 256)

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

- All computer data is ultimately represented as bits
- 1 byte = 8 bits = 256 possible values
- Know your data type sizes for memory estimation
- Bitwise operations enable compact storage and fast computation
- Endianness matters when reading binary data across systems
