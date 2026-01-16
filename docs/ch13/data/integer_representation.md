# Integer Representation

## Unsigned Integers

The simplest integer representation—just the binary value:

```
8-bit unsigned integer (uint8)

Binary:    0 1 1 0 0 1 0 1
Weights: 128 64 32 16 8 4 2 1
Value:     0 + 64 + 32 + 0 + 0 + 4 + 0 + 1 = 101
```

### Range of Unsigned Integers

| Type | Bits | Minimum | Maximum |
|------|------|---------|---------|
| uint8 | 8 | 0 | 255 (2⁸ - 1) |
| uint16 | 16 | 0 | 65,535 (2¹⁶ - 1) |
| uint32 | 32 | 0 | 4,294,967,295 (2³² - 1) |
| uint64 | 64 | 0 | 18,446,744,073,709,551,615 (2⁶⁴ - 1) |

```python
import numpy as np

# NumPy unsigned integers
arr = np.array([255], dtype=np.uint8)
print(arr + 1)  # [0] - overflow wraps around!

print(np.iinfo(np.uint8))   # min=0, max=255
print(np.iinfo(np.uint64))  # min=0, max=18446744073709551615
```

## Signed Integers: Two's Complement

Most computers use **two's complement** to represent negative numbers.

### How Two's Complement Works

The most significant bit (MSB) has negative weight:

```
8-bit signed integer (int8)

Binary:    1 0 1 1 0 1 0 1
Weights: -128 64 32 16 8 4 2 1
Value:   -128 + 0 + 32 + 16 + 0 + 4 + 0 + 1 = -75
```

### Two's Complement Range

| Type | Bits | Minimum | Maximum |
|------|------|---------|---------|
| int8 | 8 | -128 | 127 |
| int16 | 16 | -32,768 | 32,767 |
| int32 | 32 | -2,147,483,648 | 2,147,483,647 |
| int64 | 64 | -9.2 × 10¹⁸ | 9.2 × 10¹⁸ |

Note: There's one more negative value than positive (no "negative zero").

### Converting to Two's Complement

To negate a number: **invert all bits, then add 1**

```
Convert 5 to -5 (8-bit):

Start:      0000 0101  (5)
Invert:     1111 1010
Add 1:      1111 1011  (-5)

Verify: -128 + 64 + 32 + 16 + 8 + 0 + 2 + 1 = -5 ✓
```

### Why Two's Complement?

1. **Single zero**: No separate +0 and -0
2. **Simple arithmetic**: Same hardware for signed/unsigned addition
3. **Easy negation**: Invert and add 1

```
Addition works without special cases:

    0000 0101  (5)
  + 1111 1011  (-5)
  ──────────────
  1 0000 0000  (0, carry discarded)

    1111 1111  (-1)
  + 0000 0001  (1)
  ──────────────
  1 0000 0000  (0, carry discarded)
```

## Python's Integers

### Arbitrary Precision

Unlike C/NumPy, Python integers have **unlimited size**:

```python
# Python ints grow as needed
x = 2 ** 1000
print(x)  # Huge number, no overflow!

# Check bit length
print(x.bit_length())  # 1001 bits needed

# Underlying storage
import sys
print(sys.getsizeof(0))      # 24 bytes (small int)
print(sys.getsizeof(2**100)) # 44 bytes
print(sys.getsizeof(2**1000)) # 160 bytes
```

### Python's Two's Complement Convention

Python conceptually uses infinite-width two's complement:

```python
# Negative numbers have infinite leading 1s
print(bin(-1))   # '-0b1' but conceptually ...1111111
print(bin(-5))   # '-0b101' but conceptually ...1111011

# Bitwise operations work as expected
print(-1 & 0xFF)  # 255 (mask to 8 bits)
print(-5 & 0xFF)  # 251 (0b11111011)
```

## NumPy Fixed-Width Integers

NumPy provides C-style fixed-width integers:

```python
import numpy as np

# Signed types
i8 = np.int8(127)
i16 = np.int16(32767)
i32 = np.int32(2147483647)
i64 = np.int64(9223372036854775807)

# Unsigned types
u8 = np.uint8(255)
u16 = np.uint16(65535)
u32 = np.uint32(4294967295)
u64 = np.uint64(18446744073709551615)

# Check ranges
print(np.iinfo(np.int8))   # min=-128, max=127
print(np.iinfo(np.uint8))  # min=0, max=255
```

### Overflow Behavior

```python
import numpy as np

# NumPy wraps on overflow (like C)
x = np.int8(127)
print(x + 1)  # -128 (wrapped!)

y = np.uint8(255)
print(y + 1)  # 0 (wrapped!)

# Python ints don't overflow
print(127 + 1)  # 128 (correct)
```

### Overflow Detection

```python
import numpy as np
import warnings

# Enable overflow warnings
old_settings = np.seterr(over='warn')

x = np.int8(127)
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    result = x + np.int8(1)
    if w:
        print("Overflow occurred!")

np.seterr(**old_settings)
```

## Bit Manipulation with Integers

### Extracting Bits

```python
x = 0b11010110

# Get nth bit
def get_bit(x, n):
    return (x >> n) & 1

print(get_bit(x, 0))  # 0
print(get_bit(x, 1))  # 1
print(get_bit(x, 2))  # 1

# Get bits n through m
def get_bits(x, n, m):
    mask = (1 << (m - n + 1)) - 1
    return (x >> n) & mask

print(bin(get_bits(x, 2, 5)))  # 0b1101
```

### Setting and Clearing Bits

```python
x = 0b11010110

# Set nth bit
def set_bit(x, n):
    return x | (1 << n)

# Clear nth bit
def clear_bit(x, n):
    return x & ~(1 << n)

# Toggle nth bit
def toggle_bit(x, n):
    return x ^ (1 << n)

print(bin(set_bit(x, 0)))     # 0b11010111
print(bin(clear_bit(x, 1)))   # 0b11010100
print(bin(toggle_bit(x, 4)))  # 0b11000110
```

## Integer Sizes in Practice

### Choosing the Right Size

```python
import numpy as np

# Memory considerations
data = list(range(1_000_000))

# Python list of ints: ~28 MB
print(sum(sys.getsizeof(x) for x in data[:100]) / 100 * 1_000_000 / 1e6)

# NumPy int64: 8 MB
arr64 = np.array(data, dtype=np.int64)
print(arr64.nbytes / 1e6)  # 8.0 MB

# NumPy int32: 4 MB
arr32 = np.array(data, dtype=np.int32)
print(arr32.nbytes / 1e6)  # 4.0 MB

# NumPy int16: 2 MB (if values fit!)
arr16 = np.array(data, dtype=np.int16)  # Might overflow!
```

### Overflow Dangers

```python
import numpy as np

# Silent data corruption
prices = np.array([30000, 35000, 40000], dtype=np.int16)
print(prices)  # [30000 -30536 -25536] - WRONG!

# Use appropriate type
prices = np.array([30000, 35000, 40000], dtype=np.int32)
print(prices)  # [30000 35000 40000] - Correct
```

## Summary

| Representation | Description | Example |
|----------------|-------------|---------|
| **Unsigned** | Non-negative only, full range | uint8: 0 to 255 |
| **Two's Complement** | MSB has negative weight | int8: -128 to 127 |
| **Python int** | Arbitrary precision | No overflow possible |
| **NumPy int** | Fixed width, wraps on overflow | Like C integers |

Key points:

- Two's complement is universal for signed integers
- Python ints never overflow (but use more memory)
- NumPy ints overflow silently—choose appropriate dtype
- Bit width determines range and memory usage
- Know your data range to choose optimal integer type
