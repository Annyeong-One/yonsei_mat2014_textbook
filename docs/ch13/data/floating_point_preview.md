# Floating Point (IEEE 754 Preview)

## The Problem with Real Numbers

Computers work with finite bits, but real numbers can have infinite decimal places. Floating-point representation is a compromise—trading exactness for range.

```
π = 3.14159265358979323846...  (infinite digits)

Stored as float32: 3.1415927   (7 significant digits)
Stored as float64: 3.141592653589793  (15 significant digits)
```

## IEEE 754 Format

The standard representation for floating-point numbers:

```
32-bit float (float32 / single precision)
┌───┬──────────┬───────────────────────────┐
│ S │ Exponent │        Mantissa           │
│ 1 │  8 bits  │        23 bits            │
└───┴──────────┴───────────────────────────┘

64-bit float (float64 / double precision)
┌───┬─────────────┬────────────────────────────────────────────┐
│ S │  Exponent   │               Mantissa                     │
│ 1 │   11 bits   │               52 bits                      │
└───┴─────────────┴────────────────────────────────────────────┘

Value = (-1)^S × 1.Mantissa × 2^(Exponent - Bias)
```

### Components

| Component | float32 | float64 | Purpose |
|-----------|---------|---------|---------|
| **Sign (S)** | 1 bit | 1 bit | 0 = positive, 1 = negative |
| **Exponent** | 8 bits | 11 bits | Scale (power of 2) |
| **Mantissa** | 23 bits | 52 bits | Precision digits |

### Example: Representing 6.5

```
6.5 in binary: 110.1

Scientific notation: 1.101 × 2²

Sign:     0 (positive)
Exponent: 2 + 127 (bias) = 129 = 10000001
Mantissa: 101 (the .101 part, leading 1 is implicit)

32-bit representation:
0 10000001 10100000000000000000000
S Exponent Mantissa
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

### Precision by Type

| Type | Decimal Digits | Example Use |
|------|---------------|-------------|
| float16 | ~3-4 | ML inference, memory-constrained |
| float32 | ~7 | Graphics, ML training |
| float64 | ~15-16 | Scientific computing, default |

```python
import numpy as np

# Demonstrating precision limits
f32 = np.float32(1.0)
f64 = np.float64(1.0)

# Add tiny values
tiny32 = np.float32(1e-8)
tiny64 = np.float64(1e-8)

print(f32 + tiny32)  # 1.00000001 (some precision)
print(f64 + tiny64)  # 1.00000001 (full precision)

# Machine epsilon - smallest distinguishable difference from 1
print(np.finfo(np.float32).eps)  # ~1.19e-07
print(np.finfo(np.float64).eps)  # ~2.22e-16
```

## Special Values

IEEE 754 defines special values:

```
┌─────────────┬─────────────────────────────┐
│    Value    │      Representation          │
├─────────────┼─────────────────────────────┤
│ +0          │ 0 00000000 00000...          │
│ -0          │ 1 00000000 00000...          │
│ +∞          │ 0 11111111 00000...          │
│ -∞          │ 1 11111111 00000...          │
│ NaN         │ X 11111111 XXXXX... (non-0)  │
└─────────────┴─────────────────────────────┘
```

### Python/NumPy Special Values

```python
import numpy as np

# Infinity
print(np.inf)           # inf
print(1.0 / 0.0)        # Warning, but returns inf
print(np.float64('inf')) # inf

# Negative infinity
print(-np.inf)          # -inf

# NaN (Not a Number)
print(np.nan)           # nan
print(0.0 / 0.0)        # nan (with warning)
print(np.inf - np.inf)  # nan

# Checking for special values
print(np.isinf(np.inf))  # True
print(np.isnan(np.nan))  # True
print(np.isfinite(1.0))  # True
```

### NaN Behavior

```python
import numpy as np

# NaN is not equal to anything, including itself!
print(np.nan == np.nan)  # False

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

# Underflow → zero
tiny = np.float64(1e-308)
print(tiny / 1e10)  # 0.0 (underflow)
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

# Better: use NumPy (uses pairwise summation)
arr = np.full(n, small)
print(f"NumPy sum: {np.sum(arr)}")  # More accurate

# Best for very high precision: math.fsum
import math
print(f"fsum: {math.fsum([small] * n)}")
```

### Loss of Significance

```python
import numpy as np

# Subtracting nearly equal numbers loses precision
a = 1.0000000001
b = 1.0000000000

# Expected: 1e-10, but...
print(a - b)  # 1.000000082740371e-10 (error in last digits!)
```

## Practical Guidelines

### Choosing Float Type

| Use Case | Recommended Type |
|----------|------------------|
| Scientific computing | float64 (default) |
| Deep learning training | float32 or float16 |
| Graphics | float32 |
| Financial (exact) | Decimal or integers |

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
| **Machine Epsilon** | Smallest distinguishable difference from 1 |

Key points:

- Floating-point is an approximation, not exact
- Most decimal fractions (like 0.1) can't be exactly represented
- Use `np.isclose()` for comparisons, not `==`
- Know your precision requirements and choose appropriate type
- Watch for accumulation errors in long computations
- NaN propagates and is not equal to itself

This is a preview—see Chapter 2 (float IEEE 754 Standard) for complete details.
