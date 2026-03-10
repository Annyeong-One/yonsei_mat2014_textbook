# Floating-Point Representation

Computers cannot represent most real numbers exactly. IEEE 754 floating-point is the universal compromise between range, precision, and performance, and its limitations directly cause some of the most common bugs in numerical code.

## Definition

**IEEE 754** represents a floating-point number as three fields:

$$
\text{value} = (-1)^S \times 1.\text{Significand} \times 2^{(\text{Exponent} - \text{Bias})}
$$

| Component | float32 | float64 | Purpose |
|-----------|---------|---------|---------|
| Sign (S) | 1 bit | 1 bit | 0 = positive, 1 = negative |
| Exponent | 8 bits (bias 127) | 11 bits (bias 1023) | Scale (power of 2) |
| Significand | 23 bits (24 effective) | 52 bits (53 effective) | Precision digits |

The leading 1 is implicit (free bit of precision). **Machine epsilon** is the gap between 1.0 and the next representable float: ~1.19e-7 for float32, ~2.22e-16 for float64.

## Explanation

Many decimal fractions have infinite binary expansions (0.1 in binary is 0.0001100110011... repeating), so they cannot be represented exactly. This is why `0.1 + 0.2 != 0.3` in every language using IEEE 754.

**Special values**: +/- infinity (overflow), NaN (undefined operations like 0/0). NaN is not equal to anything, including itself -- always use `np.isnan()` to check.

**Precision is not uniform**: the gap between representable numbers scales with magnitude. Near value $v$, the spacing is roughly $v \times \epsilon$. This means adding a small number to a large one can lose the small number entirely (absorption).

**Catastrophic cancellation** occurs when subtracting nearly equal numbers, destroying most significant digits. Algebraic reformulation often avoids this.

## Examples

```python
# The classic floating-point surprise
print(0.1 + 0.2)         # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False

# Correct comparison: use tolerance
import numpy as np
print(np.isclose(0.1 + 0.2, 0.3))  # True
```

```python
import numpy as np

# Precision limits: small values absorbed by large ones
print(1e16 + 1 == 1e16)   # True -- the 1 is lost!

# Machine epsilon
print(np.finfo(np.float64).eps)  # ~2.22e-16

# Special values
print(np.inf - np.inf)     # nan
print(np.nan == np.nan)    # False
print(np.isnan(np.nan))    # True
```

```python
import numpy as np

# Memory vs. precision tradeoff
n = 10_000_000
print(f"float64: {np.zeros(n, dtype=np.float64).nbytes / 1e6:.0f} MB")  # 80 MB
print(f"float32: {np.zeros(n, dtype=np.float32).nbytes / 1e6:.0f} MB")  # 40 MB
```
