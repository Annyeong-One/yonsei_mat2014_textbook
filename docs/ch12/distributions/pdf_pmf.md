# PDF and PMF

The **probability density function** (PDF) and **probability mass function** (PMF) describe how probability is distributed across the values a random variable can take. The PDF applies to continuous distributions, while the PMF applies to discrete distributions.

---

## Probability Density Function (PDF)

For a continuous random variable $X$, the PDF $f(x)$ gives the **relative likelihood** of $X$ taking a value near $x$. Crucially, $f(x)$ is not itself a probability — it can exceed 1. Probabilities are obtained by integrating the PDF over an interval:

$$P(a < X \le b) = \int_a^b f(x)\, dx$$

### Example: Normal Distribution PDF

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.norm(loc=mu)
x = np.linspace(mu - 3, mu + 3, 100)
y = a.pdf(x)

plt.plot(x, y, label='PDF')
plt.fill_between(x, y, alpha=0.3)
plt.title(f'Normal PDF (μ={mu}, σ=1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
```

The PDF peaks at the mean and decays symmetrically. The total area under the curve equals 1.

## Probability Mass Function (PMF)

For a discrete random variable $X$, the PMF $P(X = k)$ gives the **exact probability** that $X$ equals $k$. Unlike the PDF, PMF values are true probabilities and must satisfy:

$$\sum_k P(X = k) = 1$$

### Example: Poisson Distribution PMF

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.poisson(mu)
x = np.arange(0, 11)
y = a.pmf(x)

plt.bar(x, y, alpha=0.7, label='PMF')
plt.title(f'Poisson PMF (μ={mu})')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.legend()
plt.show()
```

Each bar represents the exact probability of observing that count. The distribution is right-skewed for small $\mu$ and becomes more symmetric as $\mu$ increases.

## PDF vs PMF: Key Differences

| Property | PDF (Continuous) | PMF (Discrete) |
|----------|-----------------|-----------------|
| Method in `scipy.stats` | `.pdf(x)` | `.pmf(k)` |
| Values represent | Density (not probability) | Exact probability |
| Can exceed 1? | Yes | No |
| Sums/integrates to | $\int f(x)\,dx = 1$ | $\sum P(X=k) = 1$ |
| Plotting | Line plot | Bar chart |

## Evaluating PDF and PMF

Both `.pdf()` and `.pmf()` accept arrays for vectorized computation:

```python
# Continuous: evaluate PDF at multiple points
normal = stats.norm(loc=0, scale=1)
x_values = np.array([-2, -1, 0, 1, 2])
pdf_values = normal.pdf(x_values)
# [0.0540, 0.2420, 0.3989, 0.2420, 0.0540]

# Discrete: evaluate PMF at multiple points
poisson = stats.poisson(mu=5)
k_values = np.array([0, 3, 5, 7, 10])
pmf_values = poisson.pmf(k_values)
```

## Financial Context

In financial mathematics, the PDF is used extensively: the normal PDF models log-return densities, risk-neutral densities are extracted from option prices, and kernel density estimation (KDE) uses PDF evaluation to construct smooth empirical distributions from sample data.

## Summary

The PDF and PMF are the fundamental functions that characterize probability distributions. In `scipy.stats`, continuous distributions provide `.pdf()` and discrete distributions provide `.pmf()`, both accepting scalar or array inputs for efficient vectorized evaluation.
