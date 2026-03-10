# Floating Point (IEEE 754 Preview)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## The Problem with Real Numbers

Computers work with finite bits, but real numbers can have infinite decimal places. Floating-point representation is a compromise—trading exactness for range. Many decimal fractions (like 0.1) have infinite binary expansions, so they cannot be represented exactly in binary floating-point.

```
π = 3.14159265358979323846...  (infinite digits)

Stored as float32: 3.1415927   (7 significant digits)
Stored as float64: 3.141592653589793  (15 significant digits)

0.1 in binary: 0.0001100110011...  (repeating — like 1/3 in decimal)
```

## IEEE 754 Format

The standard representation for floating-point numbers:

```
32-bit float (float32 / single precision)
┌───┬──────────┬───────────────────────────┐
│ S │ Exponent │       Significand         │
│ 1 │  8 bits  │        23 bits            │
└───┴──────────┴───────────────────────────┘

64-bit float (float64 / double precision)
┌───┬─────────────┬────────────────────────────────────────────┐
│ S │  Exponent   │             Significand                    │
│ 1 │   11 bits   │               52 bits                      │
└───┴─────────────┴────────────────────────────────────────────┘

Value = (-1)^S × 1.Significand × 2^(Exponent - Bias)    [normalized numbers]

Note: This formula applies to normalized numbers. Subnormal numbers
(exponent field all zeros) use a leading 0 instead of the implicit 1,
providing gradual underflow at the cost of reduced precision.

> **Why Bias instead of two's complement for the exponent?** The exponent needs to represent both negative and positive powers, so a signed representation is needed. The exponent is stored using a bias so that both positive and negative exponents can be represented while keeping the stored exponent as a plain unsigned integer. The primary benefit is **ordering**: comparing exponent fields as unsigned integers corresponds to comparing their true exponents, which simplifies hardware comparisons. (Note that exponent arithmetic itself still requires bias correction.) The bias value is chosen as `2^(k-1) - 1` where `k` is the number of exponent bits: **127** for float32 (8 bits), **1023** for float64 (11 bits).
```

### Components

| Component | float32 | float64 | Purpose |
|-----------|---------|---------|---------|
| **Sign (S)** | 1 bit | 1 bit | 0 = positive, 1 = negative |
| **Exponent** | 8 bits | 11 bits | Scale (power of 2) |
| **Significand** | 23 bits (24 effective) | 52 bits (53 effective) | Precision digits (historically called mantissa); effective precision includes the implicit leading 1 |

### Example: Representing 6.5

```
6.5 in binary: 110.1

Scientific notation: 1.101 × 2²

Sign:     0 (positive)
Exponent: 2 + 127 (bias) = 129 = 10000001
Significand: 101 (the .101 part; the leading 1 is implicit — normalized
             numbers in binary always start with 1.xxx, so storing it
             would waste a bit. IEEE 754 omits it, gaining 1 free bit of
             precision. Subnormal numbers are the exception: they have
             no implicit leading 1, which is why they have less precision.)

32-bit representation:
0 10000001 10100000000000000000000
S Exponent Significand
```

## Precision Limitations

### Not All Numbers Are Representable

```python
# Classic example
print(0.1 + 0.2)  # 0.30000000000000004

# 0.1 cannot be exactly represented in binary
# Like 1/3 = 0.333... in decimal
print(format(0.1, '.20f'))  # 0.10000000000000000555
```

When a value falls between two representable numbers, IEEE 754 rounds to the nearest representable value (using **round-to-nearest-even** by default, which breaks ties by rounding to the value whose last significand bit is even). For example, in decimal analogy: 2.5 rounds to 2, but 3.5 rounds to 4.

### Precision by Type

| Type | Decimal Digits | Example Use |
|------|---------------|-------------|
| float16 | ~3-4 | ML inference, memory-constrained (very limited range and precision) |
| float32 | ~7 | Graphics, ML training |
| float64 | ~15-16 | Scientific computing, default |

```python
import numpy as np

# Demonstrating precision limits — add values near machine epsilon
# float32 epsilon ~1.19e-7: adding 1e-8 has no effect
print(np.float32(1.0) + np.float32(1e-8))   # 1.0 — unchanged!
print(np.float32(1.0) + np.float32(1e-6))   # 1.000001 — just visible

# float64 epsilon ~2.22e-16: much finer resolution
print(np.float64(1.0) + np.float64(1e-15))  # 1.000000000000001
print(np.float64(1.0) + np.float64(1e-17))  # 1.0 — below epsilon, lost

# Machine epsilon: difference between 1.0 and the next representable float
# Precision is NOT uniform — spacing between representable numbers scales
# with magnitude. Near value v, the gap is roughly v × epsilon.
# Epsilon itself only describes precision near 1.0.
print(np.finfo(np.float32).eps)  # ~1.19e-07
print(np.finfo(np.float64).eps)  # ~2.22e-16
```

## Special Values

IEEE 754 defines special values:

```
┌─────────────┬─────────────────────────────┐
│    Value    │      Representation          │
├─────────────┼─────────────────────────────┤
│ +0          │ 0 00000000 00000...          │  +0 and -0 compare equal
│ -0          │ 1 00000000 00000...          │  but: 1/+0 → +∞, 1/-0 → -∞
│ +∞          │ 0 11111111 00000...          │
│ -∞          │ 1 11111111 00000...          │
│ NaN         │ X 11111111 XXXXX... (non-0)  │
└─────────────┴─────────────────────────────┘
```

### Python/NumPy Special Values

```python
import numpy as np

# Infinity
print(np.inf)                        # inf
print(np.float64(1.0) / 0.0)        # inf (NumPy, not plain Python)
print(np.float64('inf'))             # inf
# Note: plain Python raises ZeroDivisionError for 1.0 / 0.0

# Negative infinity
print(-np.inf)          # -inf

# NaN (Not a Number)
print(np.nan)                         # nan
print(np.divide(0.0, 0.0))           # nan (NumPy; plain 0.0/0.0 raises ZeroDivisionError)
print(np.inf - np.inf)               # nan

# Checking for special values
print(np.isinf(np.inf))  # True
print(np.isnan(np.nan))  # True
print(np.isfinite(1.0))  # True
```

### NaN Behavior

```python
import numpy as np

# NaN is not equal to anything, including itself!
# IEEE-754 defines NaN as unordered: all comparisons return False except !=
print(np.nan == np.nan)  # False
print(np.nan != np.nan)  # True

# Use isnan() instead
x = np.nan
print(np.isnan(x))  # True

# NaN propagates through calculations
print(np.nan + 1)    # nan
print(np.nan * 0)    # nan
print(np.sqrt(-1))   # nan (with warning)
```

## Range and Limits

```python
import numpy as np

# float32 limits
info32 = np.finfo(np.float32)
print(f"float32 max: {info32.max}")     # ~3.4e38
print(f"float32 min: {info32.min}")     # ~-3.4e38
print(f"float32 tiny: {info32.tiny}")   # ~1.2e-38 (smallest positive normal)

# float64 limits
info64 = np.finfo(np.float64)
print(f"float64 max: {info64.max}")     # ~1.8e308
print(f"float64 min: {info64.min}")     # ~-1.8e308
print(f"float64 tiny: {info64.tiny}")   # ~2.2e-308
```

### Overflow and Underflow

```python
import numpy as np

# Overflow → infinity
huge = np.float64(1e308)
print(huge * 10)  # inf

# Underflow: very small numbers first become subnormal (losing precision
# gradually because the implicit leading 1 disappears), then underflow
# to zero. IEEE 754 supports subnormal numbers to avoid an abrupt jump
# to zero. Note: subnormal arithmetic can be significantly slower on
# some CPUs due to microcode assist rather than hardware fast-path.
tiny = np.float64(1e-308)
print(tiny / 1e10)   # subnormal (very small but nonzero)
print(tiny / 1e200)  # 0.0 (true underflow to zero)
```

## Common Pitfalls

### Comparison Errors

```python
# Bad: Direct equality comparison
if 0.1 + 0.2 == 0.3:  # False!
    print("Equal")

# Good: Use tolerance
import numpy as np
if np.isclose(0.1 + 0.2, 0.3):  # True
    print("Close enough")

# For arrays
a = np.array([0.1 + 0.2])
b = np.array([0.3])
print(np.allclose(a, b))  # True
```

### Accumulation Errors

```python
import numpy as np

# Summing many small numbers
small = 1e-10
n = 1_000_000

# Bad: accumulated error
total = 0.0
for _ in range(n):
    total += small
print(f"Loop sum: {total}")  # May not be exactly 1e-4

# Better: use NumPy (often uses pairwise summation, depending on size and BLAS)
arr = np.full(n, small)
print(f"NumPy sum: {np.sum(arr)}")  # More accurate

# Best for very high precision: math.fsum
import math
print(f"fsum: {math.fsum([small] * n)}")
```

### Loss of Significance

```python
import numpy as np

# Loss of precision during addition: the small value is absorbed
print((1e16 + 1) - 1e16)  # 0.0 — the 1 is completely lost!
print(1e16 + 1 == 1e16)   # True — 1 is below float64 precision at this scale

# Catastrophic cancellation: subtracting nearly equal numbers
# destroys most significant digits
a = 1.0000000001
b = 1.0000000000
# Expected: 1e-10, but precision is lost in the last digits
print(a - b)  # 1.000000082740371e-10 (error in last digits)

# Classic example: sqrt(x+1) - sqrt(x) for large x
import math
x = 1e15
direct = math.sqrt(x + 1) - math.sqrt(x)       # cancellation!
stable = 1.0 / (math.sqrt(x + 1) + math.sqrt(x))  # algebraically equivalent
print(f"Direct: {direct}")   # less accurate
print(f"Stable: {stable}")   # more accurate
```

## Practical Guidelines

### Choosing Float Type

| Use Case | Recommended Type |
|----------|------------------|
| Scientific computing | float64 (default) |
| Deep learning training | float32 or float16 |
| Graphics | float32 |
| Financial (exact) | `Decimal`, or integers in smallest unit (e.g. cents) |

### Memory Considerations

```python
import numpy as np

n = 10_000_000

arr64 = np.zeros(n, dtype=np.float64)
arr32 = np.zeros(n, dtype=np.float32)
arr16 = np.zeros(n, dtype=np.float16)

print(f"float64: {arr64.nbytes / 1e6:.0f} MB")  # 80 MB
print(f"float32: {arr32.nbytes / 1e6:.0f} MB")  # 40 MB
print(f"float16: {arr16.nbytes / 1e6:.0f} MB")  # 20 MB
```

## Summary

| Concept | Description |
|---------|-------------|
| **IEEE 754** | Standard floating-point representation |
| **Sign/Exponent/Mantissa** | Three components of a float |
| **Precision** | float32 ~7 digits, float64 ~15 digits |
| **Special Values** | ±0, ±∞, NaN |
| **Machine Epsilon** | Difference between 1.0 and the next representable float |

Key points:

- Floating-point is an approximation, not exact
- Most decimal fractions (like 0.1) can't be exactly represented
- Use `np.isclose()` for comparisons, not `==`
- Know your precision requirements and choose appropriate type
- Watch for accumulation errors in long computations
- NaN propagates and is not equal to itself

This is a preview—see Chapter 2 (float IEEE 754 Standard) for complete details.
