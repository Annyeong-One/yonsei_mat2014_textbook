# Polynomial Regression

Many real-world relationships are not well described by a straight line. A
chemical reaction rate might rise and then plateau, or a projectile's height
follows a parabolic arc. Polynomial regression captures these curved
relationships by adding powers of the predictor to the model. Despite the
nonlinear shape of the fitted curve, polynomial regression is a special case
of multiple linear regression, so the entire OLS machinery applies unchanged.

---

## The Polynomial Model

A polynomial regression of degree $d$ models the response as

$$
y_i = \beta_0 + \beta_1 x_i + \beta_2 x_i^2 + \cdots + \beta_d x_i^d + \varepsilon_i
$$

This is equivalent to multiple regression with derived predictors
$z_1 = x$, $z_2 = x^2$, $\dots$, $z_d = x^d$. The design matrix becomes
the Vandermonde matrix

$$
\mathbf{X} = \begin{pmatrix} 1 & x_1 & x_1^2 & \cdots & x_1^d \\ 1 & x_2 & x_2^2 & \cdots & x_2^d \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_n & x_n^2 & \cdots & x_n^d \end{pmatrix}
$$

The OLS estimator is the same as in multiple regression:

$$
\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1}\mathbf{X}^\top \mathbf{y}
$$

## Fitting with NumPy

NumPy provides `numpy.polyfit` for polynomial fitting and `numpy.polynomial.polynomial.polyfit`
for the same task with a different coefficient ordering convention.

```python
import numpy as np

# Sample data with a quadratic relationship
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.5, 6.2, 11.0, 17.1, 24.8, 33.9, 44.2, 56.1])

# Fit degree-2 polynomial: y = c2*x^2 + c1*x + c0
coeffs = np.polyfit(x, y, deg=2)
print(f"Coefficients (highest to lowest degree): {coeffs}")

# Evaluate the fitted polynomial
p = np.poly1d(coeffs)
y_hat = p(x)
```

!!! tip "Vandermonde matrix approach"
    For explicit control, construct the design matrix with `numpy.vander`
    and solve via `numpy.linalg.lstsq`:
    ```python
    V = np.vander(x, N=3, increasing=True)
    beta, _, _, _ = np.linalg.lstsq(V, y, rcond=None)
    ```

## Degree Selection and Overfitting

Choosing the polynomial degree $d$ involves a bias-variance trade-off:

- **Too low** ($d$ small): underfitting. The model cannot capture the true
  curvature, leading to high bias.
- **Too high** ($d$ large): overfitting. The model fits noise in the training
  data, leading to high variance and poor generalization.

A polynomial of degree $n - 1$ passes exactly through all $n$ data points
(interpolation), but this perfect fit almost always generalizes poorly.

Practical criteria for selecting $d$ include:

- **Adjusted $R^2$**: penalizes additional parameters
- **Cross-validation**: evaluates prediction error on held-out data
- **Information criteria**: AIC and BIC balance fit quality against model complexity

## Numerical Conditioning

As the degree increases, the columns of the Vandermonde matrix become
increasingly correlated, making $\mathbf{X}^\top\mathbf{X}$ ill-conditioned.
The condition number grows rapidly with $d$, causing numerical instability
in the OLS solution.

Two remedies are common:

1. **Centering and scaling**: replace $x$ with $(x - \bar{x})/s_x$ before
   forming the powers. This reduces correlation among columns.
2. **Orthogonal polynomials**: use a basis of orthogonal polynomials (e.g.,
   Legendre or Chebyshev) so that $\mathbf{X}^\top\mathbf{X}$ is diagonal
   or nearly so.

```python
# Centering and scaling before polynomial fit
x_centered = (x - x.mean()) / x.std()
coeffs_stable = np.polyfit(x_centered, y, deg=4)
```

!!! warning "High-degree polynomial pitfalls"
    Polynomials of degree $d \geq 5$ often exhibit Runge's phenomenon: large
    oscillations near the boundaries of the data range. Piecewise polynomials
    (splines) are generally preferred for flexible curve fitting.

## Comparison with Multiple Regression

| Aspect                  | Multiple Regression           | Polynomial Regression              |
|-------------------------|-------------------------------|------------------------------------|
| Predictors              | Multiple independent variables | Powers of a single variable        |
| Design matrix           | Observed features              | Vandermonde matrix                 |
| Interpretation          | Each coefficient = partial effect | Coefficients lack simple interpretation |
| Multicollinearity risk  | Depends on data                | Inherent (powers are correlated)   |

## Summary

Polynomial regression extends simple linear regression by including powers of
the predictor as additional features. The model remains linear in the parameters,
so OLS applies directly. The key challenge is choosing the polynomial degree:
too low produces underfitting, too high produces overfitting and numerical
instability. Centering, scaling, and orthogonal polynomial bases help manage
conditioning issues.
