# Pearson and Spearman

Quantifying the strength and direction of a relationship between two variables is one of the most common tasks in statistical analysis. The Pearson correlation coefficient measures the degree of linear association, while the Spearman rank correlation captures monotonic relationships without assuming linearity. Choosing the right measure depends on the data's distributional properties and the type of relationship under investigation.

## Pearson Correlation

The **Pearson correlation coefficient** between two random variables $X$ and $Y$ is defined as

$$
\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \, \sigma_Y} = \frac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \, \sigma_Y}
$$

Given a sample of $n$ paired observations $(x_1, y_1), \ldots, (x_n, y_n)$, the **sample Pearson correlation** is

$$
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \;\sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

The coefficient satisfies $-1 \leq r \leq 1$, where $r = 1$ indicates a perfect positive linear relationship, $r = -1$ indicates a perfect negative linear relationship, and $r = 0$ indicates no linear association.

!!! note "Assumptions for Pearson Correlation"
    Pearson correlation assumes that both variables are measured on an interval or ratio scale. The coefficient captures only **linear** relationships: a strong nonlinear relationship (e.g., $Y = X^2$) can produce $r \approx 0$. Inference (p-values, confidence intervals) additionally assumes bivariate normality.

```python
import numpy as np
from scipy import stats

# Generate linearly related data with noise
np.random.seed(42)
x = np.random.normal(0, 1, 200)
y = 0.8 * x + np.random.normal(0, 0.5, 200)

r, p_value = stats.pearsonr(x, y)
print(f"Pearson r = {r:.4f}, p-value = {p_value:.2e}")
```

The function `stats.pearsonr` returns both the correlation coefficient and a two-sided p-value testing the null hypothesis $H_0\!: \rho = 0$ against $H_1\!: \rho \neq 0$.

## Spearman Rank Correlation

The **Spearman rank correlation** is a nonparametric measure that assesses monotonic relationships. It is defined as the Pearson correlation applied to the ranks of the data. When there are no tied ranks, it simplifies to

$$
r_s = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}
$$

where $d_i = \text{rank}(x_i) - \text{rank}(y_i)$ is the difference between the ranks of corresponding observations.

Like Pearson, $-1 \leq r_s \leq 1$, where $r_s = 1$ indicates a perfect monotonically increasing relationship and $r_s = -1$ a perfect monotonically decreasing one.

Because Spearman operates on ranks rather than raw values, it is robust to outliers and does not require the variables to be normally distributed. It also detects monotonic nonlinear relationships that Pearson may miss.

```python
# Generate monotonically (but nonlinearly) related data
np.random.seed(42)
x = np.random.uniform(0.1, 5, 200)
y = np.log(x) + np.random.normal(0, 0.3, 200)

rho, p_value = stats.spearmanr(x, y)
print(f"Spearman rho = {rho:.4f}, p-value = {p_value:.2e}")

# Compare with Pearson on the same data
r, _ = stats.pearsonr(x, y)
print(f"Pearson r    = {r:.4f}")
```

## When to Use Each Measure

| Criterion | Pearson | Spearman |
|---|---|---|
| Relationship type | Linear | Monotonic |
| Scale requirement | Interval/ratio | Ordinal or above |
| Sensitivity to outliers | High | Low |
| Distribution assumption | Bivariate normality (for inference) | None |

!!! tip "Practical Guidance"
    When in doubt, compute both. If Pearson and Spearman yield similar values, the relationship is approximately linear. If Spearman is substantially larger in magnitude, the relationship may be monotonic but nonlinear. If both are near zero, there may still be a non-monotonic association that neither measure captures.

## Summary

Pearson correlation quantifies linear association through the ratio of covariance to the product of standard deviations, while Spearman rank correlation measures monotonic association by applying Pearson to ranked data. Pearson is sensitive to outliers and assumes linearity, whereas Spearman is robust and distribution-free. Both return values in $[-1, 1]$ with associated p-values testing the null hypothesis of zero correlation, and they are accessible through `scipy.stats.pearsonr` and `scipy.stats.spearmanr`.
