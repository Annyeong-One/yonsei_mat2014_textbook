# Beta Distribution

The beta distribution is the most natural continuous distribution for modeling random variables that represent probabilities, proportions, or rates confined to the interval $[0, 1]$. It arises as the conjugate prior for the Bernoulli and binomial likelihoods in Bayesian statistics, and it appears in the theory of order statistics. Its two shape parameters allow a remarkably flexible family of density shapes on $[0, 1]$.

---

## Mathematical Definition

A random variable $X$ follows a beta distribution with shape parameters $\alpha > 0$ and $\beta > 0$, written $X \sim \text{Beta}(\alpha, \beta)$, if its probability density function is:

$$
f(x) = \frac{x^{\alpha - 1}(1 - x)^{\beta - 1}}{B(\alpha, \beta)}, \quad 0 \le x \le 1
$$

where $B(\alpha, \beta)$ is the **beta function**, defined as:

$$
B(\alpha, \beta) = \frac{\Gamma(\alpha)\,\Gamma(\beta)}{\Gamma(\alpha + \beta)}
$$

The beta function serves as the normalization constant that ensures the density integrates to 1 over $[0, 1]$.

## Usage in scipy.stats

The `scipy.stats.beta` distribution object takes parameters `a` ($\alpha$) and `b` ($\beta$):

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

alpha, beta_param = 2.0, 5.0
a = stats.beta(alpha, beta_param)

print(f"Mean: {a.mean():.4f}")        # α/(α+β) = 2/7
print(f"Variance: {a.var():.4f}")      # αβ/((α+β)²(α+β+1))

x = np.linspace(0, 1, 200)
y_pdf = a.pdf(x)
y_cdf = a.cdf(x)

plt.plot(x, y_pdf, label='PDF')
plt.plot(x, y_cdf, label='CDF')
plt.legend()
plt.title(f'Beta Distribution (α={alpha}, β={beta_param})')
plt.xlabel('x')
plt.ylabel('Density / Probability')
plt.show()
```

The PDF shows the shape of the distribution on $[0, 1]$, while the CDF gives $P(X \le x)$, rising from 0 to 1.

## Effect of Parameters

The two shape parameters control the density shape with great flexibility. Varying $\alpha$ and $\beta$ produces uniform, U-shaped, J-shaped, and bell-shaped densities all within the same family:

```python
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 200)
params = [(0.5, 0.5), (1, 1), (2, 2), (2, 5), (5, 2)]
for (a, b) in params:
    plt.plot(x, stats.beta(a, b).pdf(x), label=f'α={a}, β={b}')

plt.legend()
plt.title('Beta PDFs for Various Parameter Combinations')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 4)
plt.show()
```

## Key Properties

The beta distribution has the following properties:

- **Mean**: $E[X] = \dfrac{\alpha}{\alpha + \beta}$
- **Variance**: $\text{Var}(X) = \dfrac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$
- **Mode** (for $\alpha > 1$ and $\beta > 1$): $\dfrac{\alpha - 1}{\alpha + \beta - 2}$

### Special Cases

- $\text{Beta}(1, 1) = \text{Uniform}(0, 1)$: when both parameters equal 1, the density is flat
- $\text{Beta}(\alpha, \alpha)$: symmetric about $x = 0.5$ for any $\alpha$
- $\text{Beta}(1/2, 1/2)$: the arcsine distribution, with density concentrated near $x = 0$ and $x = 1$

### Parameters in scipy.stats

| Parameter | Symbol | `scipy.stats` keyword | Default |
|-----------|--------|-----------------------|---------|
| Shape 1   | $\alpha$ | `a`               | (required) |
| Shape 2   | $\beta$  | `b`               | (required) |
| Location  | —        | `loc`             | 0       |
| Scale     | —        | `scale`           | 1       |

## Financial Applications

In quantitative finance, the beta distribution models recovery rates in credit risk (the fraction of face value recovered after default), portfolio weight distributions, and loss-given-default rates. In Bayesian portfolio analysis, it serves as a prior for the probability of outperformance. The PERT distribution, widely used in project risk analysis, is a scaled beta distribution.

## Summary

The beta distribution provides a flexible family of densities on $[0, 1]$, controlled by two shape parameters. In `scipy.stats`, use `stats.beta(a, b)` to create a frozen distribution for computing PDFs, CDFs, quantiles, and generating random samples.
