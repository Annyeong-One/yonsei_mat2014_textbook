# Normal Distribution

The normal (Gaussian) distribution is the most fundamental continuous probability distribution in statistics and financial mathematics. It arises naturally from the Central Limit Theorem and underpins much of quantitative finance, from asset return modeling to option pricing.

---

## Mathematical Definition

The probability density function (PDF) of a normal distribution with mean $\mu$ and standard deviation $\sigma$ is:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

When $\mu = 0$ and $\sigma = 1$, this is the **standard normal distribution**.

## Manual PDF Computation

Before using `scipy.stats`, it is instructive to compute the normal PDF directly from the formula. This builds intuition about how the bell curve arises from the exponential of a squared deviation:

```python
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
x = np.linspace(mu - 3, mu + 3, num=100)
y = np.exp(-(x - mu)**2 / 2) / np.sqrt(2 * np.pi)

plt.plot(x, y)
plt.title(f'Normal PDF (μ={mu}, σ=1) — Manual Computation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
```

Here the formula is implemented element-wise using NumPy vectorization. The denominator $\sigma\sqrt{2\pi}$ normalizes the area under the curve to 1, and the exponent $-(x-\mu)^2 / (2\sigma^2)$ controls the bell shape centered at $\mu$.

## Using scipy.stats.norm

The `scipy.stats.norm` distribution object provides a consistent interface for all distribution computations:

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.norm(loc=mu)  # Frozen distribution with mean=3, std=1

# Evaluate PDF and CDF over a range
x = np.linspace(mu - 3, mu + 3, 100)
y_pdf = a.pdf(x)
y_cdf = a.cdf(x)

plt.plot(x, y_pdf, label='PDF')
plt.plot(x, y_cdf, label='CDF')
plt.legend(loc='lower left')
plt.title(f'Normal Distribution (μ={mu}, σ=1)')
plt.xlabel('x')
plt.ylabel('Density / Probability')
plt.show()
```

The PDF curve shows the relative likelihood of each value (its height at the mean is the maximum), while the CDF is the S-shaped curve that gives $P(X \le x)$, rising from 0 to 1.

## Key Properties

The normal distribution has several important properties:

- **Symmetry**: The distribution is symmetric about the mean, so $\text{mean} = \text{median} = \text{mode} = \mu$.
- **68-95-99.7 Rule**: Approximately 68% of values fall within $\mu \pm \sigma$, 95% within $\mu \pm 2\sigma$, and 99.7% within $\mu \pm 3\sigma$.
- **Additivity**: If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, then $X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$.
- **Central Limit Theorem**: The sum (or mean) of a large number of independent random variables tends toward a normal distribution, regardless of the original distribution.

## Parameters in scipy.stats

| Parameter | Symbol | `scipy.stats` keyword | Default |
|-----------|--------|----------------------|---------|
| Mean      | $\mu$  | `loc`                | 0       |
| Std Dev   | $\sigma$| `scale`             | 1       |

## Financial Applications

The normal distribution is central to quantitative finance. Log-returns of assets are often modeled as normally distributed, which leads to the lognormal model for prices. The Black-Scholes option pricing model assumes that log-returns follow a normal distribution. Value at Risk (VaR) calculations frequently use the normal quantile function (`ppf`). Portfolio theory relies on the normal distribution for computing efficient frontiers under mean-variance optimization.

## Summary

The normal distribution serves as the foundation for much of statistics and financial mathematics. Understanding both its manual derivation and its `scipy.stats` interface is essential for any quantitative analysis workflow.
