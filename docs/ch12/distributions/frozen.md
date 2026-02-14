# Frozen Distributions

A **frozen distribution** in `scipy.stats` is a distribution object with its parameters fixed (frozen) at creation time. This allows you to call methods like `.rvs()`, `.pdf()`, `.cdf()`, and `.ppf()` without repeatedly passing the distribution parameters.

---

## Creating a Frozen Distribution

When you call a distribution constructor with specific parameters, you get a frozen distribution object:

```python
import scipy.stats as stats

# Create a frozen normal distribution with mean=3.0, std=1.0
a = stats.norm(loc=3.0)

# Generate random samples from the frozen distribution
samples = a.rvs(size=(2, 3), random_state=1)
print(samples)
print(type(samples))   # <class 'numpy.ndarray'>
print(samples.shape)   # (2, 3)
print(samples.dtype)   # float64
```

The output is always a NumPy array, and the `random_state` parameter ensures reproducibility.

## Frozen vs Unfrozen Usage

Without a frozen distribution, you must pass parameters every time:

```python
# Unfrozen — parameters passed each time
stats.norm.pdf(0, loc=3.0, scale=1.0)
stats.norm.cdf(0, loc=3.0, scale=1.0)
stats.norm.rvs(loc=3.0, scale=1.0, size=5)

# Frozen — parameters set once
a = stats.norm(loc=3.0, scale=1.0)
a.pdf(0)
a.cdf(0)
a.rvs(size=5)
```

Frozen distributions are cleaner, less error-prone, and more efficient when you need to call multiple methods on the same distribution.

## Available Methods

Every frozen distribution object provides a consistent interface:

| Method | Description |
|--------|-------------|
| `rvs(size, random_state)` | Generate random variates (samples) |
| `pdf(x)` / `pmf(k)` | Probability density / mass function |
| `cdf(x)` | Cumulative distribution function $P(X \le x)$ |
| `sf(x)` | Survival function $1 - \text{CDF}(x)$ |
| `ppf(q)` | Percent point function (inverse CDF) |
| `isf(q)` | Inverse survival function |
| `mean()` | Distribution mean |
| `var()` | Distribution variance |
| `std()` | Distribution standard deviation |
| `stats(moments)` | Central moments (mean, variance, skew, kurtosis) |
| `entropy()` | Differential entropy |
| `fit(data)` | Fit parameters to data (class method) |
| `interval(confidence)` | Confidence interval around the median |

## Continuous vs Discrete

Frozen distributions work identically for both continuous (`rv_continuous`) and discrete (`rv_discrete`) distributions. The only difference is that discrete distributions use `.pmf()` (probability mass function) instead of `.pdf()`:

```python
# Continuous: use pdf
normal = stats.norm(loc=0, scale=1)
normal.pdf(0)  # height of the density curve at x=0

# Discrete: use pmf
poisson = stats.poisson(mu=3.0)
poisson.pmf(3)  # exact probability P(X = 3)
```

## Why Frozen Distributions Matter

Frozen distributions embody the **object-oriented design** of `scipy.stats`. Each distribution is an object that encapsulates its parameters and provides a unified API. This design pattern makes it easy to write generic code that works with any distribution, pass distributions as arguments to functions, and swap distributions in simulations without changing the calling code.

## Summary

Frozen distributions are the standard way to work with `scipy.stats`. By fixing parameters at creation time, they provide a clean, consistent interface for sampling, density evaluation, probability computation, and statistical analysis.
