# rv_continuous and rv_discrete

All probability distributions in `scipy.stats` inherit from one of two base classes: `rv_continuous` for continuous distributions and `rv_discrete` for discrete distributions. Understanding these base classes reveals the unified design behind the entire `scipy.stats` distribution system.

---

## The Distribution Class Hierarchy

Every distribution in `scipy.stats` is an instance of either `rv_continuous` or `rv_discrete`, both of which inherit from `rv_generic`:

```
rv_generic
├── rv_continuous  →  norm, expon, gamma, chi2, t, f, beta, ...
└── rv_discrete    →  binom, poisson, geom, hypergeom, nbinom, ...
```

When you write `stats.norm(loc=3.0)`, you are calling `rv_continuous.__call__()` which returns a **frozen distribution** — an object with fixed parameters.

## rv_continuous

Continuous distributions are defined on intervals of the real line and provide the `.pdf()` method for the probability density function:

```python
import scipy.stats as stats
import numpy as np

# stats.norm is an instance of rv_continuous
a = stats.norm(loc=3.0)        # frozen: mean=3, std=1
samples = a.rvs(size=(2, 3), random_state=1)
print(samples)
print(type(samples))   # <class 'numpy.ndarray'>
print(samples.shape)   # (2, 3)
print(samples.dtype)   # float64

# Key methods: pdf, cdf, sf, ppf, isf, rvs, fit, mean, var, std, entropy
```

## rv_discrete

Discrete distributions are defined on countable sets (typically non-negative integers) and provide the `.pmf()` method for the probability mass function:

```python
# stats.poisson is an instance of rv_discrete
b = stats.poisson(mu=3.0)      # frozen: mean=3
print(b.pmf(3))                # P(X = 3) — exact probability
print(b.cdf(5))                # P(X ≤ 5)
```

The key difference: discrete distributions use `.pmf(k)` where continuous distributions use `.pdf(x)`. All other methods (`.cdf()`, `.sf()`, `.ppf()`, `.rvs()`, etc.) work identically.

## Common Interface

Both `rv_continuous` and `rv_discrete` share a consistent interface through `rv_generic`:

| Method | Continuous | Discrete | Description |
|--------|-----------|----------|-------------|
| Density/Mass | `.pdf(x)` | `.pmf(k)` | Density or mass at a point |
| Log density | `.logpdf(x)` | `.logpmf(k)` | Log of density/mass (numerically stable) |
| CDF | `.cdf(x)` | `.cdf(k)` | $P(X \le x)$ |
| Survival | `.sf(x)` | `.sf(k)` | $P(X > x)$ |
| Quantile | `.ppf(q)` | `.ppf(q)` | Inverse CDF |
| Sampling | `.rvs(size)` | `.rvs(size)` | Random variates |
| Moments | `.mean()`, `.var()` | `.mean()`, `.var()` | Theoretical moments |
| Fit | `.fit(data)` | — | MLE parameter estimation |

## Frozen vs Unfrozen

The base classes support two usage patterns. In the unfrozen pattern, parameters are passed to each method call: `stats.norm.pdf(0, loc=3, scale=1)`. In the frozen pattern, a distribution object is created once and methods are called without parameters: `a = stats.norm(loc=3, scale=1); a.pdf(0)`. The frozen pattern is preferred for clarity and efficiency.

## Summary

The `rv_continuous` and `rv_discrete` base classes define the unified API that makes `scipy.stats` distributions interchangeable. By understanding this class hierarchy, you can write generic code that works with any distribution and leverage the full suite of methods consistently.
