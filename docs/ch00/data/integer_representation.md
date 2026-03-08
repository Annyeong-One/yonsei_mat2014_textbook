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

In two's complement interpretation, the most significant bit (MSB) contributes −2^(n−1) to the value. This is a mathematical interpretation of the bit pattern — the hardware still performs ordinary binary addition on all bits; the "negative weight" is how we interpret the result:

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

**Why does this work?** Two's complement represents −x as 2ⁿ − x (where n is the bit width). For 8-bit: −5 = 256 − 5 = 251 = `11111011`. Inverting all bits of x gives (2ⁿ − 1 − x), and adding 1 gives exactly 2ⁿ − x. This is why the "invert and add 1" trick works — it's not arbitrary, it follows directly from the definition.

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

### Overflow in Two's Complement

When a result exceeds the representable range, the bit pattern wraps around. This is the most important property of fixed-width integers:

```
  0111 1111  (127, max int8)
+ 0000 0001  (1)
───────────
  1000 0000  (-128!)

The carry into the MSB flips the sign bit — the result wraps
from the maximum positive value to the minimum negative value.
```

```python
import numpy as np
x = np.int8(127)
print(x + 1)  # -128 (wrapped!)
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

### How Python Actually Stores Integers

Unlike C/NumPy which use two's complement, Python stores integers as **sign + magnitude** — the sign and the absolute value are kept separately:

```
Python int object in memory:
┌─────────────┬───────────┬──────────────────┐
│  ob_refcnt  │  ob_size  │   ob_digit[]     │
│ (ref count) │ (+ or -)  │ (magnitude only) │
└─────────────┴───────────┴──────────────────┘
```

- `ob_size` is negative if the number is negative, positive if positive
- `ob_digit[]` stores the magnitude as an array of **base-2³⁰ chunks** (not decimal digits or single bits) — each element holds up to 30 bits of the integer's magnitude
- The sign is carried separately — more like how humans write `−5`

So `-5` is stored as: sign = negative, magnitude = 5. Not two's complement.

| | Storage | Sign | Overflow |
|---|---|---|---|
| **Two's complement** (C/NumPy) | Single bit pattern, sign baked in | MSB has negative weight | Possible |
| **Python int** | Sign field + magnitude separately | `ob_size` positive/negative | Never |

In two's complement, `-5` and `5` look completely different in bits (`1111 1011` vs `0000 0101`). In Python, they have the **same magnitude** (`ob_digit = [5]`), just opposite `ob_size` signs.

### Python's Two's Complement Convention

`bin(-5)` returns `'-0b101'` — the `'-'` prefix is just a **display convention**, not the internal storage. Python's `bin()` reads the sign field and prepends `'-'` to the magnitude.

However, Python *simulates* infinite-width two's complement when doing bitwise operations — it computes results *as if* the number were stored in two's complement with infinite width. A key mental model: **negative numbers behave as if they have infinitely many leading 1 bits** (e.g. −1 is conceptually `...11111111`, −5 is `...11111011`):

```python
# bin() shows sign-magnitude display, not internal storage
print(bin(-1))   # '-0b1' but conceptually ...1111111
print(bin(-5))   # '-0b101' but conceptually ...1111011

# Bitwise ops simulate infinite two's complement
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

# NumPy wraps on overflow (like C) — silently, with no warning
x = np.int8(127)
print(x + 1)  # -128 (wrapped!)

y = np.uint8(255)
print(y + 1)  # 0 (wrapped!)

# Python ints don't overflow
print(127 + 1)  # 128 (correct)
```

> **Note**: NumPy integer overflow is silent — there is no built-in warning mechanism for integer wraparound (unlike floating-point). Always validate your data range before choosing a dtype.

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
# Memory considerations (rough estimates — sys.getsizeof counts
# the integer object only, not list pointers or list array overhead)
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

> **Two ways Python handles negative integers**: Python actually has two different representations depending on context. Native Python integers use **sign + magnitude** (the sign and absolute value stored separately) — this enables arbitrary precision and no overflow. NumPy integers use **C-style two's complement** — because under the hood, NumPy runs C code operating directly on fixed-width bit patterns. Same Python environment, two fundamentally different internal representations depending on whether you're using `int` or `np.int8/int32/int64`.

| Representation | Description | Example |
|----------------|-------------|---------|
| **Unsigned** | Non-negative only, full range | uint8: 0 to 255 |
| **Two's Complement** | MSB has negative weight | int8: -128 to 127 |
| **Python int** | Arbitrary precision | No overflow possible |
| **NumPy int** | Fixed width, wraps on overflow | Like C integers |

Key points:

- Two's complement is the dominant representation for signed integers in modern hardware
- Python ints never overflow (but use more memory)
- NumPy ints overflow silently—choose appropriate dtype
- Bit width determines range and memory usage
- Know your data range to choose optimal integer type
