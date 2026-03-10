# Integer Representation

Integers are stored differently in Python (arbitrary precision, sign + magnitude) and in C/NumPy (fixed-width two's complement). Understanding both representations is essential for avoiding silent overflow bugs and reasoning about memory usage.

## Definition

**Unsigned integers** use standard base-2 positional notation. An n-bit unsigned integer ranges from 0 to 2^n - 1.

**Two's complement** is the standard signed integer representation in hardware. The most significant bit contributes -2^(n-1) to the value, giving a range of -2^(n-1) to 2^(n-1) - 1. To negate: invert all bits and add 1.

**Python integers** use a separate sign field plus arbitrary-precision magnitude stored as an array of base-2^30 chunks. They never overflow but use more memory.

## Explanation

Two's complement dominates because the same addition hardware works for both signed and unsigned values, and there is only one representation of zero. When a result exceeds the representable range, it wraps around (modulo 2^n arithmetic). In NumPy, this overflow is **silent** -- no error or warning.

Python integers avoid overflow entirely by growing dynamically. However, each Python `int` is a heap-allocated object (~28 bytes for small values), compared to 1-8 bytes for a NumPy fixed-width integer. For bitwise operations, Python simulates infinite-width two's complement: negative numbers behave as if they have infinitely many leading 1 bits.

**Key tradeoff**: Python `int` is safe but memory-heavy. NumPy fixed-width integers are compact and fast but silently wrap on overflow. Always validate data ranges before choosing a NumPy dtype.

## Examples

```python
import numpy as np

# Two's complement overflow in NumPy (silent!)
x = np.int8(127)
print(x + 1)  # -128 (wrapped around)

# Python int: no overflow, ever
print(2 ** 1000)  # huge number, no problem
```

```python
import numpy as np

# Memory comparison
import sys
print(sys.getsizeof(42))           # 28 bytes (Python int object)
print(np.int64(42).nbytes)         # 8 bytes (NumPy fixed-width)
print(np.int8(42).nbytes)          # 1 byte
```

```python
# Python simulates infinite two's complement for bitwise ops
print(bin(-5))       # '-0b101' (display convention)
print(-5 & 0xFF)     # 251 = 0b11111011 (8-bit two's complement of -5)

# Negation by hand: invert bits, add 1
#   5 = 00000101
#  ~5 = 11111010
#  +1 = 11111011 = 251 unsigned = -5 signed
```

```python
import numpy as np

# Choosing the right dtype: overflow danger
prices = np.array([30000, 35000, 40000], dtype=np.int16)
print(prices)  # [30000 -30536 -25536] -- WRONG! (max int16 = 32767)

prices = np.array([30000, 35000, 40000], dtype=np.int32)
print(prices)  # [30000 35000 40000] -- correct
```
