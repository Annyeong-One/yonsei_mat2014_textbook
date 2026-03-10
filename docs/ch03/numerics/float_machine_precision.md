# Machine Precision


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Machine precision (or machine epsilon) quantifies the smallest relative difference between consecutive floating-point numbers. This fundamental limit determines the accuracy achievable in numerical computations.

## Machine Epsilon

The machine epsilon $\epsilon$ is the smallest value such that $1 + \epsilon \neq 1$ in floating-point arithmetic.

### 1. Definition

For IEEE 754 double precision with 52 mantissa bits:

$$\epsilon = 2^{-52} \approx 2.22 \times 10^{-16}$$

```python
import sys

# Machine epsilon from sys
eps = sys.float_info.epsilon
print(f"Machine epsilon: {eps}")
print(f"Scientific:      {eps:.2e}")
print(f"As power of 2:   2^{-52} = {2**-52}")

# Verify: 1 + eps != 1
print(f"\n1 + eps == 1: {1 + eps == 1}")      # False
print(f"1 + eps/2 == 1: {1 + eps/2 == 1}")  # True
```

### 2. Precision Test

Systematically find where precision is lost.

```python
# Double-Precision Floating-Point Accuracy Test
epsilon = 1.0

while epsilon > 1e-20:
    if 1 + epsilon == 1:
        print(f"{epsilon:.1e}  ->  1 + epsilon = 1 (Precision lost)")
    else:
        print(f"{epsilon:.1e}  ->  1 + epsilon != 1 (Precision maintained)")
    epsilon *= 0.1

# Precision is lost around 10^-16
```

### 3. NumPy Epsilon Access

NumPy provides epsilon for all float types.

```python
import numpy as np

# Different precisions have different epsilons
print(f"float16 eps: {np.finfo(np.float16).eps:.2e}")
print(f"float32 eps: {np.finfo(np.float32).eps:.2e}")
print(f"float64 eps: {np.finfo(np.float64).eps:.2e}")

# Verify for float32
eps32 = np.finfo(np.float32).eps
one = np.float32(1.0)
print(f"\nfloat32: 1 + eps != 1: {one + eps32 != one}")
print(f"float32: 1 + eps/2 == 1: {one + eps32/2 == one}")
```

## Relative vs Absolute Error

Machine epsilon bounds relative error, not absolute error.

### 1. Relative Error Bound

For any floating-point operation, the relative error is bounded by $\epsilon$:

$$\left| \frac{x - \text{fl}(x)}{x} \right| \leq \epsilon$$

where $\text{fl}(x)$ is the floating-point representation of $x$.

```python
import math

def relative_error(exact, approx):
    """Calculate relative error."""
    if exact == 0:
        return abs(approx)
    return abs((exact - approx) / exact)

# Example: representation error of 0.1
exact = 1/10  # Mathematical 0.1
stored = 0.1  # Floating-point 0.1

# The error is tiny but nonzero
from decimal import Decimal
exact_decimal = Decimal('0.1')
stored_decimal = Decimal(stored)
error = float(abs(stored_decimal - exact_decimal))

print(f"Absolute error: {error:.2e}")
print(f"Machine epsilon: {2**-52:.2e}")
print(f"Error < epsilon: {error < 2**-52}")  # True
```

### 2. Error Scales with Magnitude

Absolute error grows with the magnitude of the number.

```python
# Near 1: absolute error ~ epsilon
x1 = 1.0
print(f"Near {x1}: smallest diff = {x1 * 2**-52:.2e}")

# Near 10^10: absolute error ~ epsilon * 10^10
x2 = 1e10
print(f"Near {x2}: smallest diff = {x2 * 2**-52:.2e}")

# Near 10^-10: absolute error ~ epsilon * 10^-10
x3 = 1e-10
print(f"Near {x3}: smallest diff = {x3 * 2**-52:.2e}")

# Demonstration
print(f"\n1.0 + 1e-16 == 1.0: {1.0 + 1e-16 == 1.0}")  # True (lost)
print(f"1e-10 + 1e-26 == 1e-10: {1e-10 + 1e-26 == 1e-10}")  # True (lost)
```

### 3. ULP (Unit in Last Place)

The ULP is the spacing between adjacent floats.

```python
import math

def ulp(x):
    """Calculate unit in last place for x."""
    if x == 0:
        return math.ldexp(1, -1074)  # Smallest subnormal
    exp = math.floor(math.log2(abs(x)))
    return math.ldexp(1, exp - 52)

# ULP varies with magnitude
for val in [1.0, 100.0, 1e10, 1e-10]:
    print(f"ulp({val:>10}) = {ulp(val):.2e}")

# math.ulp() available in Python 3.9+
import sys
if sys.version_info >= (3, 9):
    print(f"\nmath.ulp(1.0) = {math.ulp(1.0)}")
```

## Single vs Double Precision

Single precision loses precision much faster.

### 1. Precision Comparison

```python
import numpy as np

# Single precision (float32)
epsilon32 = np.float32(1.0)
while epsilon32 > np.float32(1e-10):
    if np.float32(1) + epsilon32 == np.float32(1):
        print(f"float32: {float(epsilon32):.1e} -> Precision lost")
        break
    epsilon32 *= np.float32(0.1)
else:
    print("float32: No precision loss detected")

# Double precision (float64)
epsilon64 = np.float64(1.0)
while epsilon64 > np.float64(1e-20):
    if np.float64(1) + epsilon64 == np.float64(1):
        print(f"float64: {float(epsilon64):.1e} -> Precision lost")
        break
    epsilon64 *= np.float64(0.1)
else:
    print("float64: No precision loss detected")
```

### 2. Significant Digits

| Type | Mantissa Bits | Decimal Digits | Epsilon |
|------|--------------|----------------|---------|
| float16 | 10 | ~3 | ~10⁻³ |
| float32 | 23 | ~7 | ~10⁻⁷ |
| float64 | 52 | ~15 | ~10⁻¹⁶ |

```python
import numpy as np

for dtype in [np.float16, np.float32, np.float64]:
    info = np.finfo(dtype)
    print(f"{dtype.__name__:>8}: {info.precision:>2} digits, eps = {info.eps:.2e}")
```

## Operation Order Matters

Due to finite precision, mathematically equivalent expressions may produce different results.

### 1. Non-Associativity

Floating-point addition is not associative: $(a + b) + c \neq a + (b + c)$.

```python
# Classic example
a = 1e16
b = -1e16
c = 1.0

# Different groupings, different results
result1 = (a + b) + c
result2 = a + (b + c)

print(f"(a + b) + c = {result1}")  # 1.0
print(f"a + (b + c) = {result2}")  # 0.0 (wrong!)

# Why? b + c loses c due to magnitude difference
print(f"b + c = {b + c}")  # -1e16 (c is lost)
```

### 2. Subtraction Sensitivity

Subtracting nearly equal numbers amplifies relative error.

```python
# Compute 1 + epsilon - 1 two ways
eps = 1e-15

# Method 1: (1 + eps) - 1
result1 = (1 + eps) - 1
print(f"(1 + eps) - 1 = {result1}")

# Method 2: 1 - 1 + eps
result2 = (1 - 1) + eps
print(f"(1 - 1) + eps = {result2}")

# Method 2 is exact; Method 1 has error
print(f"Error in method 1: {abs(result1 - eps):.2e}")
```

### 3. Demonstrating Order Effects

```python
import numpy as np

# Sum a large array: order matters
np.random.seed(42)
data = np.random.randn(1000000).astype(np.float32)

# Different orderings
sum_forward = np.float32(0)
for x in data:
    sum_forward += x

sum_sorted = np.float32(0)
for x in sorted(data):
    sum_sorted += x

print(f"Forward sum:  {sum_forward}")
print(f"Sorted sum:   {sum_sorted}")
print(f"Difference:   {abs(sum_forward - sum_sorted)}")
print(f"NumPy sum:    {data.sum()}")  # Uses pairwise summation
```

## Practical Guidelines

Apply these rules for robust numerical code.

### 1. Tolerance-Based Comparison

Never use `==` for float comparison.

```python
import math

a = 0.1 + 0.2
b = 0.3

# Wrong
print(f"a == b: {a == b}")  # False

# Correct: use tolerance
print(f"isclose: {math.isclose(a, b)}")  # True

# Custom tolerance for your application
def approx_equal(x, y, rel_tol=1e-9, abs_tol=1e-12):
    """Check approximate equality."""
    return abs(x - y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)

print(f"approx_equal: {approx_equal(a, b)}")
```

### 2. Avoid Subtracting Similar Values

Restructure calculations to avoid catastrophic cancellation.

```python
import math

# Bad: direct formula for quadratic (when b² >> 4ac)
def quadratic_bad(a, b, c):
    disc = math.sqrt(b*b - 4*a*c)
    x1 = (-b + disc) / (2*a)
    x2 = (-b - disc) / (2*a)
    return x1, x2

# Good: avoid cancellation using alternative formula
def quadratic_good(a, b, c):
    disc = math.sqrt(b*b - 4*a*c)
    if b >= 0:
        x1 = (-b - disc) / (2*a)
    else:
        x1 = (-b + disc) / (2*a)
    x2 = c / (a * x1)  # Vieta's formula
    return x1, x2

# Test with b² >> 4ac
a, b, c = 1, 1e8, 1
print(f"Bad:  {quadratic_bad(a, b, c)}")
print(f"Good: {quadratic_good(a, b, c)}")
```

### 3. Condition Number Awareness

Check if your problem is inherently sensitive.

```python
import numpy as np

# Well-conditioned matrix
A_good = np.array([[1, 0], [0, 1]])
print(f"Identity condition number: {np.linalg.cond(A_good)}")

# Ill-conditioned matrix (Hilbert matrix)
def hilbert(n):
    return np.array([[1/(i+j+1) for j in range(n)] for i in range(n)])

for n in [3, 5, 10]:
    H = hilbert(n)
    cond = np.linalg.cond(H)
    print(f"Hilbert({n}) condition number: {cond:.2e}")

# Rule: expect to lose log10(cond) digits of accuracy
```

### 4. Use Appropriate Precision

Choose precision based on requirements.

```python
import numpy as np

# Memory vs precision tradeoff
data_size = 1_000_000

# float64: 8 bytes, ~15 digits
arr64 = np.random.randn(data_size).astype(np.float64)
print(f"float64: {arr64.nbytes / 1e6:.1f} MB")

# float32: 4 bytes, ~7 digits
arr32 = arr64.astype(np.float32)
print(f"float32: {arr32.nbytes / 1e6:.1f} MB")

# Precision loss when converting
max_diff = np.max(np.abs(arr64 - arr32))
print(f"Max conversion error: {max_diff:.2e}")
```

## Testing Precision Bounds

Verify your numerical code respects precision limits.

### 1. Round-Trip Tests

Check that operations preserve expected precision.

```python
import math

def test_round_trip(x, operations):
    """Apply operations and check precision."""
    result = x
    for op, inv_op in operations:
        result = op(result)
        result = inv_op(result)
    
    rel_error = abs(result - x) / abs(x) if x != 0 else abs(result)
    return rel_error

# Test: multiply then divide
x = 1.234567890123456
ops = [(lambda y: y * 7.3, lambda y: y / 7.3)]
error = test_round_trip(x, ops * 100)  # 100 round trips
print(f"Error after 100 mul/div: {error:.2e}")

# Test: exp then log
ops_exp = [(math.exp, math.log)]
error_exp = test_round_trip(x, ops_exp * 100)
print(f"Error after 100 exp/log: {error_exp:.2e}")
```

### 2. Stability Under Perturbation

Test sensitivity to small input changes.

```python
import numpy as np

def test_stability(func, x, delta=1e-10, n_tests=1000):
    """Test function stability under small perturbations."""
    base_result = func(x)
    max_relative_change = 0
    
    for _ in range(n_tests):
        perturbed_x = x * (1 + np.random.uniform(-delta, delta))
        perturbed_result = func(perturbed_x)
        
        if base_result != 0:
            rel_change = abs(perturbed_result - base_result) / abs(base_result)
            input_rel_change = abs(perturbed_x - x) / abs(x)
            amplification = rel_change / input_rel_change if input_rel_change > 0 else 0
            max_relative_change = max(max_relative_change, amplification)
    
    return max_relative_change

# Stable function
print(f"sin stability: {test_stability(np.sin, 1.0):.1f}x")

# Less stable near discontinuity
print(f"tan stability (near π/2): {test_stability(np.tan, 1.57):.1f}x")
```
