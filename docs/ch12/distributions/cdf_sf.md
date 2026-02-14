# CDF and Survival Function

The **cumulative distribution function** (CDF) and **survival function** (SF) are complementary functions that describe the probability of a random variable falling below or above a threshold.

---

## Cumulative Distribution Function (CDF)

The CDF gives the probability that a random variable $X$ is less than or equal to a value $x$:

$$F(x) = P(X \le x)$$

For continuous distributions this is the integral of the PDF from $-\infty$ to $x$. For discrete distributions it is the sum of the PMF up to $k$.

### Properties of the CDF

The CDF is non-decreasing, right-continuous, and satisfies $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$.

### Continuous Example: Normal Distribution CDF

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.norm(loc=mu)
x = np.linspace(mu - 3, mu + 3, 100)
y_pdf = a.pdf(x)
y_cdf = a.cdf(x)

plt.plot(x, y_pdf, label='PDF')
plt.plot(x, y_cdf, label='CDF')
plt.legend(loc='lower left')
plt.title(f'Normal Distribution (μ={mu}, σ=1)')
plt.xlabel('x')
plt.show()
```

The CDF rises from 0 to 1 in an S-shaped (sigmoid) curve. At the mean $\mu$, the CDF equals 0.5.

### Continuous Example: Exponential Distribution CDF

The exponential distribution models waiting times and inter-arrival times. Its CDF rises quickly for high rate parameters:

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

la = 3.0  # rate parameter λ
a = stats.expon(scale=1/la)  # scale = 1/λ
x = np.linspace(0, 3, 100)
y_pdf = a.pdf(x)
y_cdf = a.cdf(x)

plt.plot(x, y_pdf, label='PDF')
plt.plot(x, y_cdf, label='CDF')
plt.legend(loc='lower left')
plt.title(f'Exponential Distribution (λ={la})')
plt.xlabel('x')
plt.show()
```

Note the important parametrization detail: `scipy.stats.expon` uses `scale = 1/λ`, so when the rate is $\lambda = 3$, you pass `scale=1/3`.

### Discrete Example: Poisson Distribution CDF

For discrete distributions, the CDF is a step function. A bar chart effectively shows both the PMF and CDF together:

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.poisson(mu)
x = np.arange(0, 11)
y_cdf = a.cdf(x)
y_pmf = a.pmf(x)

plt.bar(x, y_cdf, label='CDF', alpha=0.5)
plt.bar(x, y_pmf, label='PMF', alpha=0.5)
plt.legend()
plt.title(f'Poisson Distribution (μ={mu})')
plt.xlabel('k')
plt.show()
```

The CDF bars show the cumulative probability up to each value $k$, while the PMF bars show the individual probability at each $k$.

## Survival Function (SF)

The survival function is the complement of the CDF:

$$S(x) = 1 - F(x) = P(X > x)$$

In `scipy.stats`, use `.sf(x)` instead of computing `1 - .cdf(x)`. The dedicated method is numerically more accurate in the tails where CDF values are very close to 1:

```python
a = stats.norm(loc=0, scale=1)

# These are mathematically equivalent, but sf is more accurate in the tails
p1 = 1 - a.cdf(5)      # may lose precision
p2 = a.sf(5)            # numerically stable
```

## Computing Probabilities Over Intervals

The CDF enables computation of interval probabilities:

$$P(a < X \le b) = F(b) - F(a)$$

```python
a = stats.norm(loc=0, scale=1)
prob = a.cdf(1) - a.cdf(-1)  # P(-1 < X ≤ 1) ≈ 0.6827
```

## Summary

The CDF and survival function are essential tools for probability computation. In `scipy.stats`, `.cdf()` gives $P(X \le x)$ and `.sf()` gives $P(X > x)$ with numerical stability. Together with the PDF/PMF and quantile functions, they form the complete interface for working with probability distributions.
