# Bits and Bytes

All computer data is ultimately represented as patterns of bits. Understanding bits, bytes, and their operations is foundational to reasoning about data types, memory, and storage.

## Definition

A **bit** (binary digit) is the smallest unit of information in digital systems, representing either 0 or 1. A **byte** is 8 bits, providing 256 possible values (0-255). The byte is the standard addressable unit on most modern CPUs.

## Explanation

Bits map to physical states: high/low voltage in transistors, magnetic orientation on disk, or light on/off in fiber optics. Every number, character, image, and program reduces to bit patterns interpreted according to encoding rules.

**Why 8 bits per byte**: 256 values cover extended character sets, align conveniently with hexadecimal (1 byte = 2 hex digits), and suit power-of-two hardware design. IBM System/360 (1964) standardized this convention.

**Endianness** determines byte order in multi-byte values. **Little-endian** (x86, ARM) stores the least significant byte first; **big-endian** (network byte order) stores the most significant byte first.

**Bitwise operations** (AND, OR, XOR, NOT, shifts) enable compact flag storage and fast computation. Python integers have arbitrary precision, so `~x` equals `-(x + 1)` rather than flipping a fixed number of bits.

**Storage prefixes**: SI units (KB = 1,000 bytes) vs. IEC units (KiB = 1,024 bytes). Storage manufacturers use SI; operating systems often report IEC values.

## Examples

```python
# Bitwise operations
a = 0b1100  # 12
b = 0b1010  # 10
print(bin(a & b))   # 0b1000 (AND)
print(bin(a | b))   # 0b1110 (OR)
print(bin(a ^ b))   # 0b0110 (XOR)

# Bit shifting: left shift multiplies by 2^n
print(bin(1 << 3))  # 0b1000 (8)
```

```python
# Byte order (endianness)
import sys
print(sys.byteorder)  # 'little' on most modern systems

x = 0x12345678
print(x.to_bytes(4, 'big'))     # b'\x12\x34\x56\x78'
print(x.to_bytes(4, 'little'))  # b'\x78\x56\x34\x12'
```

```python
# Practical: permission flags using bitmasks
READ    = 0b100  # 4
WRITE   = 0b010  # 2
EXECUTE = 0b001  # 1

perms = READ | WRITE       # 0b110 = 6
print(bool(perms & READ))  # True  (has read permission)
perms &= ~WRITE            # remove write: 0b100 = 4
```
