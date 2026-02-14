# Binomial and Poisson

The binomial and Poisson distributions are the two most important discrete distributions in statistics and financial mathematics. The binomial counts successes in a fixed number of trials, while the Poisson counts events occurring at a constant average rate.

---

## Binomial Distribution

The binomial distribution models the number of successes in $n$ independent Bernoulli trials, each with success probability $p$:

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n$$

### Usage in scipy.stats

```python
import scipy.stats as stats

# 100 trials with 60% success probability
n, p = 100, 0.6
binom_dist = stats.binom(n, p)

print(f"Mean: {binom_dist.mean():.2f}")       # np = 60
print(f"Variance: {binom_dist.var():.2f}")     # np(1-p) = 24
print(f"P(X = 60): {binom_dist.pmf(60):.4f}")
print(f"P(X ≤ 55): {binom_dist.cdf(55):.4f}")
```

### Visualizing Samples vs Theory

A powerful way to verify understanding is to overlay a histogram of random samples with the theoretical PMF:

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

n_, p_ = 100, 0.6
a = stats.binom(n_, p_)
x_samples = a.rvs(size=10000, random_state=337)
x_theory = np.arange(101)
y_theory = a.pmf(x_theory)

plt.plot(x_theory, y_theory, color='r', label='Theoretical PMF')
plt.hist(x_samples, density=True, bins=20, alpha=0.7, label='Sampled histogram')
plt.legend()
plt.title(f'Binomial(n={n_}, p={p_}): Samples vs Theory')
plt.xlabel('k')
plt.ylabel('Probability')
plt.show()
```

## Poisson Distribution

The Poisson distribution models the number of events occurring in a fixed interval when events happen at a constant average rate $\mu$:

$$P(X = k) = \frac{\mu^k e^{-\mu}}{k!}, \quad k = 0, 1, 2, \ldots$$

A distinctive property is that the mean equals the variance: $E[X] = \text{Var}(X) = \mu$.

### Usage in scipy.stats

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

mu = 3.0
a = stats.poisson(mu)
x = np.arange(0, 11)
y_pmf = a.pmf(x)
y_cdf = a.cdf(x)

plt.bar(x, y_cdf, label='CDF', alpha=0.5)
plt.bar(x, y_pmf, label='PMF', alpha=0.5)
plt.legend()
plt.title(f'Poisson Distribution (μ={mu})')
plt.xlabel('k')
plt.show()
```

The PMF bars show the probability of each count $k$, while the CDF bars show the cumulative probability $P(X \le k)$. For $\mu = 3$, the mode is at $k = 2$ and $k = 3$, and the distribution is slightly right-skewed.

## Relationship: Poisson as Limit of Binomial

When $n$ is large and $p$ is small, the binomial distribution is well-approximated by the Poisson distribution with $\mu = np$:

$$\text{Binom}(n, p) \approx \text{Poisson}(np), \quad \text{for large } n, \text{ small } p$$

This is useful in practice because the Poisson distribution has a simpler form and only one parameter.

## Financial Applications

The binomial distribution appears in the binomial option pricing model (Cox-Ross-Rubinstein), where asset prices move up or down at each step. It also models the number of defaults in a credit portfolio when default events are independent. The Poisson distribution models the number of trades in a time interval, insurance claim counts, and jump events in jump-diffusion models for asset prices.

## Summary

The binomial and Poisson distributions are workhorses of discrete probability. In `scipy.stats`, use `stats.binom(n, p)` and `stats.poisson(mu)` to create frozen distributions, then call `.pmf()`, `.cdf()`, `.rvs()`, and other methods as needed.
