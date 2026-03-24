# Polynomial Class

The `numpy.polynomial.Polynomial` class wraps a coefficient array together with domain and window metadata into a single object. This design enables numerically stable fitting, evaluation, and arithmetic without manually managing coordinate transformations. While the sibling page on the np.polynomial module introduces the basics, this page explores the class mechanics in depth — domain and window mapping, weighted fitting, truncation, conversion, and serialization.

```python
import numpy as np
from numpy.polynomial import Polynomial
```

---

## Construction

A `Polynomial` object is created from an array of coefficients in **ascending** power order. Optional `domain` and `window` parameters control the coordinate mapping used during fitting and evaluation.

```python
# 2 + 3x + x²  (ascending order: constant, x, x², ...)
p = Polynomial([2, 3, 1])
print(p)         # 2.0 + 3.0·x + 1.0·x²
print(p.coef)    # [2. 3. 1.]
print(p.degree())  # 2
```

### From Roots

```python
# Create polynomial with roots at x = 1 and x = 3
# (x - 1)(x - 3) = x² - 4x + 3  →  coefficients [3, -4, 1]
p = Polynomial.fromroots([1, 3])
print(p.coef)  # [3. -4.  1.]
print(p.roots())  # [1. 3.]
```

### Identity and Basis Polynomials

```python
# Identity polynomial: p(x) = x
p_x = Polynomial.identity()
print(p_x.coef)  # [0. 1.]

# Basis polynomial of degree k: p(x) = x^k
p_x3 = Polynomial.basis(3)
print(p_x3.coef)  # [0. 0. 0. 1.]
```

---

## Domain and Window

Every `Polynomial` object carries two intervals: `domain` and `window`. These control the affine mapping applied during evaluation.

- **domain**: the interval in the original data space (e.g., $[0, 100]$ for data spanning 0 to 100)
- **window**: the interval in the computational space (default $[-1, 1]$)

When calling `p(x)`, the class maps $x$ from the domain to the window before evaluating the polynomial. This mapping is the key to numerical stability for high-degree fits.

### The Mapping Formula

The affine mapping from domain $[a, b]$ to window $[c, d]$ is

$$
u = c + (d - c) \cdot \frac{x - a}{b - a}
$$

For the default window $[-1, 1]$ and domain $[a, b]$, this simplifies to

$$
u = \frac{2x - (a + b)}{b - a}
$$

```python
# Polynomial with custom domain
p = Polynomial([1, 2, 3], domain=[0, 10], window=[-1, 1])

# Evaluation maps x=0 → u=-1, x=10 → u=1, x=5 → u=0
print(p(0))   # p evaluated at u = -1: 1 - 2 + 3 = 2.0
print(p(10))  # p evaluated at u =  1: 1 + 2 + 3 = 6.0
print(p(5))   # p evaluated at u =  0: 1 + 0 + 0 = 1.0
```

### Why Domain Mapping Matters

Without mapping, fitting a degree-10 polynomial to data in $[0, 1000]$ requires computing $1000^{10} = 10^{30}$, which causes floating-point overflow. Mapping to $[-1, 1]$ keeps all powers bounded by 1.

```python
# High-degree fit with large x values — stable with Polynomial.fit
x = np.linspace(0, 1000, 100)
y = np.sin(x / 100)

p_fit = Polynomial.fit(x, y, deg=10)
print(p_fit.domain)  # [   0. 1000.]
print(np.max(np.abs(p_fit(x) - y)))  # Small residual
```

---

## Fitting with Polynomial.fit

`Polynomial.fit` is a class method that performs least-squares polynomial fitting with automatic domain mapping.

```python
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 2.7, 5.8, 11.2, 18.1, 26.5])

# Fit degree-2 polynomial
p = Polynomial.fit(x, y, deg=2)
print(p(x))  # Fitted values close to y
```

### Weighted Fitting

Assign weights to data points to give some observations more influence than others. Points with higher weight contribute more to the fit.

```python
x = np.array([0, 1, 2, 3, 4])
y = np.array([1.0, 2.1, 3.9, 8.5, 16.2])

# Uniform weights (default)
p_uniform = Polynomial.fit(x, y, deg=2)

# High weight on the first three points
w = np.array([10, 10, 10, 1, 1])
p_weighted = Polynomial.fit(x, y, deg=2, w=w)

# The weighted fit follows the first three points more closely
print(p_uniform(x))
print(p_weighted(x))
```

### Specifying the Fitting Domain

By default, `Polynomial.fit` sets the domain to $[\min(x), \max(x)]$. You can override this.

```python
# Force domain to [0, 10] even though data only covers [0, 5]
p = Polynomial.fit(x, y, deg=2, domain=[0, 10])
print(p.domain)  # [ 0. 10.]
```

---

## Conversion and Truncation

### Converting to Standard Coefficients

A fitted `Polynomial` stores coefficients relative to its domain mapping. Use `convert` to obtain coefficients in a different domain or the standard power basis.

```python
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 7, 13, 21])

p_fit = Polynomial.fit(x, y, deg=2)

# Convert to standard domain [-1, 1] → gives "raw" power-basis coefficients
p_standard = p_fit.convert()
print(p_standard.coef)  # [1. 1. 1.] → 1 + x + x²

# Convert to a specific domain
p_custom = p_fit.convert(domain=[0, 10])
print(p_custom.domain)  # [ 0. 10.]
```

### Truncation

Remove high-degree terms by truncating to a lower degree.

```python
p = Polynomial([1, 2, 3, 4, 5])  # degree 4
p_trunc = p.truncate(3)           # keep only up to degree 2
print(p_trunc.coef)  # [1. 2. 3.]
```

### Trimming

Remove trailing near-zero coefficients.

```python
p = Polynomial([1, 2, 3, 1e-16, 2e-17])
p_trimmed = p.trim()
print(p_trimmed.coef)  # [1. 2. 3.]
```

---

## Serialization and Interoperability

### Converting Between Bases

The `convert` method also enables switching between different polynomial basis classes.

```python
from numpy.polynomial import Chebyshev

# Start with a power-basis polynomial
p = Polynomial([1, 2, 3])

# Convert to Chebyshev basis
p_cheb = p.convert(kind=Chebyshev)
print(type(p_cheb))  # <class 'numpy.polynomial.chebyshev.Chebyshev'>

# Convert back
p_back = p_cheb.convert(kind=Polynomial)
print(np.allclose(p.coef, p_back.coef))  # True
```

### String Representation

```python
p = Polynomial([1, -2, 3])
print(repr(p))  # Polynomial([1., -2., 3.], domain=[-1,  1], window=[-1,  1])
print(str(p))   # 1.0 - 2.0·x + 3.0·x²
```

---

## Summary

| Operation | Method / Syntax |
|-----------|----------------|
| Create from coefficients | `Polynomial([c0, c1, c2])` |
| Create from roots | `Polynomial.fromroots([r1, r2])` |
| Fit data | `Polynomial.fit(x, y, deg)` |
| Weighted fit | `Polynomial.fit(x, y, deg, w=weights)` |
| Evaluate | `p(x)` |
| Get coefficients | `p.coef` |
| Get degree | `p.degree()` |
| Derivative | `p.deriv(n)` |
| Integral | `p.integ(k=0)` |
| Roots | `p.roots()` |
| Convert domain/basis | `p.convert(domain=..., kind=...)` |
| Truncate degree | `p.truncate(n)` |
| Trim near-zero | `p.trim()` |

**Key Takeaways**:

- The `Polynomial` class bundles coefficients with domain and window metadata
- Domain-to-window mapping is the mechanism behind numerical stability in fitting
- `Polynomial.fit` handles domain mapping automatically; use `convert` to extract standard coefficients
- Weighted fitting adjusts influence of individual data points via the `w` parameter
- `convert(kind=...)` enables basis conversion between Polynomial, Chebyshev, Legendre, and other classes
- `truncate` and `trim` simplify polynomials by removing high-degree or near-zero terms
