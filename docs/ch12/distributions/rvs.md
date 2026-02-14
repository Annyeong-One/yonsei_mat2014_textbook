# Sampling (rvs)

The `.rvs()` method generates **random variates** (random samples) from a probability distribution. It is the primary tool for Monte Carlo simulation, bootstrapping, and any workflow that requires synthetic data from a known distribution.

---

## Basic Usage

Every frozen distribution in `scipy.stats` provides the `.rvs()` method:

```python
import scipy.stats as stats

a = stats.norm(loc=3.0)  # frozen normal distribution, mean=3, std=1
samples = a.rvs(size=(2, 3), random_state=1)
print(samples)
# [[4.62434536 2.38824359 2.47182825]
#  [1.92703138 3.86540763 0.6984613 ]]
print(type(samples))   # <class 'numpy.ndarray'>
print(samples.shape)   # (2, 3)
print(samples.dtype)   # float64
```

The output is always a NumPy array whose shape is determined by the `size` parameter. With `size=(2, 3)`, you get a 2x3 matrix of independent samples.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `size` | int or tuple | Shape of the output array. `size=1000` gives a 1D array; `size=(100, 5)` gives a 2D array. |
| `random_state` | int, Generator, or RandomState | Seed for reproducibility. Pass an integer for deterministic results. |

## Reproducibility

The `random_state` parameter ensures that the same sequence of random numbers is generated each time:

```python
# These two calls produce identical samples
s1 = stats.norm(0, 1).rvs(size=5, random_state=42)
s2 = stats.norm(0, 1).rvs(size=5, random_state=42)
assert (s1 == s2).all()
```

For more control, pass a `numpy.random.Generator` object:

```python
import numpy as np
rng = np.random.default_rng(seed=42)
samples = stats.norm(0, 1).rvs(size=1000, random_state=rng)
```

## Verifying Samples Against Theory

A standard validation technique is to overlay a histogram of samples with the theoretical PDF (continuous) or PMF (discrete):

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Generate samples and overlay with theoretical PDF
a = stats.norm(loc=0, scale=1)
samples = a.rvs(size=10000, random_state=337)
x = np.linspace(-4, 4, 100)

plt.hist(samples, density=True, bins=50, alpha=0.7, label='Histogram')
plt.plot(x, a.pdf(x), 'r-', linewidth=2, label='Theoretical PDF')
plt.legend()
plt.title('Sampling Verification: Histogram vs PDF')
plt.show()
```

As the sample size increases, the histogram converges to the theoretical distribution — a visual demonstration of the law of large numbers.

## Sampling from Different Distribution Types

The `.rvs()` method works identically for continuous and discrete distributions:

```python
# Continuous distributions
stats.norm(0, 1).rvs(size=5)           # normal
stats.expon(scale=1/3).rvs(size=5)     # exponential with rate λ=3

# Discrete distributions
stats.poisson(mu=3.0).rvs(size=5)      # Poisson
stats.binom(n=100, p=0.6).rvs(size=5)  # binomial
```

For discrete distributions, `.rvs()` returns integer-valued arrays.

## Financial Applications

Random sampling is fundamental to Monte Carlo methods in finance: simulating asset price paths under geometric Brownian motion, generating scenarios for Value at Risk (VaR) estimation, pricing path-dependent options, and stress testing portfolio performance under various distributional assumptions.

## Summary

The `.rvs()` method is the gateway to simulation-based analysis. Combined with the `random_state` parameter for reproducibility and NumPy's array infrastructure, it provides an efficient and consistent interface for generating random samples from any `scipy.stats` distribution.
