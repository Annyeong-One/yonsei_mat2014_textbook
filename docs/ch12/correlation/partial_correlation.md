# Partial Correlation

Two variables may exhibit a strong correlation not because of a direct relationship, but because both are driven by a common third variable. For example, ice cream sales and drowning incidents are positively correlated, yet neither causes the other; temperature drives both. Partial correlation addresses this confounding problem by measuring the linear association between two variables after removing the linear effect of one or more controlling variables.

## First-Order Partial Correlation

The **partial correlation** of $X$ and $Y$ given $Z$, denoted $r_{XY \cdot Z}$, measures the linear association between $X$ and $Y$ after removing the linear influence of $Z$ from both. It is defined as

$$
r_{XY \cdot Z} = \frac{r_{XY} - r_{XZ} \, r_{YZ}}{\sqrt{(1 - r_{XZ}^2)(1 - r_{YZ}^2)}}
$$

where $r_{XY}$, $r_{XZ}$, and $r_{YZ}$ are the pairwise Pearson correlations.

Like Pearson correlation, the partial correlation satisfies $-1 \leq r_{XY \cdot Z} \leq 1$. When $r_{XY \cdot Z} \approx 0$ despite $r_{XY}$ being large, the apparent association between $X$ and $Y$ is explained by the confounding variable $Z$.

## Residual Interpretation

Partial correlation has an equivalent and geometrically intuitive formulation through regression residuals. The partial correlation $r_{XY \cdot Z}$ equals the Pearson correlation between:

1. The residuals $e_X$ from regressing $X$ on $Z$
2. The residuals $e_Y$ from regressing $Y$ on $Z$

$$
r_{XY \cdot Z} = r_{e_X, e_Y}
$$

The residuals represent the parts of $X$ and $Y$ that cannot be linearly predicted by $Z$, so their correlation captures only the direct linear relationship between $X$ and $Y$.

## Matrix Formulation

For $p$ variables, all partial correlations (controlling for all remaining variables) can be computed simultaneously from the **precision matrix** $P = \Sigma^{-1}$ (the inverse of the covariance matrix). The partial correlation between $X_i$ and $X_j$, controlling for all other variables, is

$$
r_{ij \cdot \text{rest}} = -\frac{P_{ij}}{\sqrt{P_{ii} \, P_{jj}}}
$$

This approach is computationally efficient when the number of variables is large and all pairwise partial correlations are needed.

## Computing Partial Correlation

```python
import numpy as np
from scipy import stats

# Generate data with a confounding variable
np.random.seed(42)
n = 500
z = np.random.normal(0, 1, n)         # confounding variable
x = 0.8 * z + np.random.normal(0, 0.5, n)
y = 0.7 * z + np.random.normal(0, 0.5, n)

# Marginal correlation (inflated by confounder z)
r_xy, _ = stats.pearsonr(x, y)
print(f"Marginal r(X,Y) = {r_xy:.4f}")

# First-order partial correlation via formula
r_xz, _ = stats.pearsonr(x, z)
r_yz, _ = stats.pearsonr(y, z)
r_partial = (r_xy - r_xz * r_yz) / np.sqrt((1 - r_xz**2) * (1 - r_yz**2))
print(f"Partial  r(X,Y|Z) = {r_partial:.4f}")
```

The marginal correlation $r_{XY}$ is large because both $X$ and $Y$ are driven by $Z$. The partial correlation $r_{XY \cdot Z}$ is close to zero, revealing that the direct relationship is weak.

```python
# Residual-based approach (equivalent result)
slope_xz = np.polyfit(z, x, 1)
slope_yz = np.polyfit(z, y, 1)
residuals_x = x - np.polyval(slope_xz, z)
residuals_y = y - np.polyval(slope_yz, z)

r_residual, _ = stats.pearsonr(residuals_x, residuals_y)
print(f"Residual r(e_X, e_Y) = {r_residual:.4f}")
```

```python
# Precision matrix approach for all pairwise partial correlations
data = np.column_stack([x, y, z])
cov_matrix = np.cov(data, rowvar=False)
precision = np.linalg.inv(cov_matrix)

# Partial correlation between X (index 0) and Y (index 1)
r_precision = -precision[0, 1] / np.sqrt(precision[0, 0] * precision[1, 1])
print(f"Precision matrix r(X,Y|Z) = {r_precision:.4f}")
```

!!! tip "Higher-Order Partial Correlation"
    The formula above handles first-order partial correlation (one controlling variable). For controlling multiple variables simultaneously, the residual-based or precision matrix approaches generalize naturally without requiring recursive formulas.

## Summary

Partial correlation isolates the direct linear association between two variables by removing the influence of confounding variables. It can be computed from pairwise correlations using a closed-form formula, from regression residuals, or from the precision matrix. When a strong marginal correlation drops to near zero after conditioning, the original association is explained by the confounders rather than by a direct relationship.
