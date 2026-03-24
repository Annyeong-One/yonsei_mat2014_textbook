# Custom Distributions

The built-in distribution families in `scipy.stats` cover a wide range of common models, but real-world data sometimes requires a distribution with a specific functional form not available in the library. The `rv_continuous` base class provides a framework for defining custom continuous distributions that automatically gain access to all standard methods (PDF, CDF, PPF, random sampling, moment computation) once you specify the density.

---

## The rv_continuous Subclass Pattern

To create a custom continuous distribution, define a class that inherits from `scipy.stats.rv_continuous` and override the `_pdf` method with your desired density function. The density $f(x)$ must satisfy:

$$
f(x) \ge 0 \quad \text{for all } x, \qquad \int_{-\infty}^{\infty} f(x)\, dx = 1
$$

At minimum, providing `_pdf` is sufficient. SciPy will numerically compute the CDF, PPF (quantile function), and moments from the PDF via numerical integration. For better performance, you can also override `_cdf`, `_ppf`, `_sf` (survival function), and `_stats`.

## Basic Example: Power Distribution

Consider the power distribution on $[0, 1]$ with parameter $\alpha > 0$:

$$
f(x) = \alpha\, x^{\alpha - 1}, \quad 0 \le x \le 1
$$

This density integrates to 1 since $\int_0^1 \alpha\, x^{\alpha - 1}\, dx = \alpha \cdot \frac{x^\alpha}{\alpha}\Big|_0^1 = 1$.

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


class PowerDistribution(stats.rv_continuous):
    """Custom power distribution on [0, 1] with shape parameter alpha."""

    def _pdf(self, x, alpha):
        return alpha * x ** (alpha - 1)

    def _cdf(self, x, alpha):
        return x ** alpha

    def _ppf(self, q, alpha):
        return q ** (1.0 / alpha)

    def _stats(self, alpha):
        mean = alpha / (alpha + 1)
        var = alpha / ((alpha + 1) ** 2 * (alpha + 2))
        return mean, var, None, None


power_dist = PowerDistribution(a=0, b=1, name='power')
```

The constructor arguments `a=0` and `b=1` set the support of the distribution to $[0, 1]$.

## Using the Custom Distribution

Once defined, the custom distribution supports the same interface as any built-in `scipy.stats` distribution:

```python
# Create a frozen distribution with alpha=3
frozen = power_dist(alpha=3)

print(f"Mean: {frozen.mean():.4f}")        # 3/4 = 0.75
print(f"Variance: {frozen.var():.4f}")      # 3/48 = 0.0375
print(f"Median: {frozen.median():.4f}")     # 0.5^(1/3)

# PDF, CDF, and random samples
x = np.linspace(0, 1, 200)
y_pdf = frozen.pdf(x)
y_cdf = frozen.cdf(x)

samples = frozen.rvs(size=5000, random_state=42)

plt.plot(x, y_pdf, 'r-', label='PDF')
plt.hist(samples, density=True, bins=40, alpha=0.5, label='Samples')
plt.legend()
plt.title('Custom Power Distribution (α=3)')
plt.xlabel('x')
plt.ylabel('Density')
plt.show()
```

## Overriding Additional Methods

Providing only `_pdf` works but can be slow for repeated CDF or quantile evaluations because SciPy falls back to numerical integration. The methods you can override, in order of impact, are:

| Method | Mathematical meaning | Benefit of overriding |
|--------|---------------------|-----------------------|
| `_pdf(x, ...)` | $f(x)$ | Required |
| `_cdf(x, ...)` | $F(x) = \int_{-\infty}^{x} f(t)\, dt$ | Avoids numerical integration |
| `_ppf(q, ...)` | $F^{-1}(q)$ | Avoids numerical root-finding |
| `_sf(x, ...)`  | $1 - F(x)$ | Better numerical accuracy in the tail |
| `_stats(...)` | $(E[X],\; \text{Var}(X),\; \text{skew},\; \text{kurt})$ | Avoids numerical moment computation |

## Validating a Custom Distribution

After defining a custom distribution, verify that the density integrates to 1 and that the CDF is consistent with the PDF:

```python
from scipy.integrate import quad

frozen = power_dist(alpha=3)

# Check normalization
total, _ = quad(frozen.pdf, 0, 1)
print(f"Integral of PDF: {total:.6f}")  # Should be 1.000000

# Check CDF consistency at a specific point
x0 = 0.7
cdf_from_integral, _ = quad(frozen.pdf, 0, x0)
cdf_from_method = frozen.cdf(x0)
print(f"CDF from integral: {cdf_from_integral:.6f}")
print(f"CDF from method:   {cdf_from_method:.6f}")
```

## Key Considerations

- **Support specification**: Set `a` and `b` in the constructor to define the support $[a, b]$. Values outside this range receive zero density automatically.
- **Shape parameters**: Pass shape parameter names as string arguments to the constructor via the `shapes` keyword, or let SciPy infer them from the `_pdf` signature.
- **Performance**: Override `_cdf` and `_ppf` whenever closed-form expressions exist. Numerical fallbacks can be orders of magnitude slower.
- **Normalization**: SciPy does not automatically verify that your PDF integrates to 1. Always check this manually.

## Summary

The `rv_continuous` subclass pattern allows you to define any continuous distribution by specifying its PDF. Once defined, the distribution inherits the full `scipy.stats` interface including CDF, PPF, moment computation, and random sampling. For production use, override `_cdf`, `_ppf`, and `_stats` with closed-form expressions to avoid numerical overhead.
