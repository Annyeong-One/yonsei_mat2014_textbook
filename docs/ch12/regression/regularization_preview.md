# Regularization Preview (Ridge, Lasso)

When a linear model has many predictors or correlated features, OLS estimates
can become unstable and overfit the training data. Regularization addresses this
by adding a penalty term to the OLS objective, shrinking coefficients toward
zero. This controlled shrinkage introduces a small bias but can substantially
reduce variance, often improving prediction on new data.

This page introduces the two most common regularization methods -- Ridge and
Lasso -- as a preview. Full treatment with cross-validation tuning and elastic
net belongs to dedicated machine learning resources.

---

## The Overfitting Problem

Recall the OLS objective for $p$ predictors:

$$
\hat{\boldsymbol{\beta}}_{\text{OLS}} = \arg\min_{\boldsymbol{\beta}} \sum_{i=1}^{n}(y_i - \mathbf{x}_i^\top \boldsymbol{\beta})^2
$$

When $p$ is large relative to $n$, or when predictors are highly correlated,
OLS produces coefficients with large magnitudes that cancel each other. The
fitted model captures noise rather than signal, and predictions on new data
deteriorate.

## Ridge Regression (L2 Penalty)

Ridge regression adds the squared $L^2$ norm of the coefficient vector as a
penalty:

$$
\hat{\boldsymbol{\beta}}_{\text{Ridge}} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^{n}(y_i - \mathbf{x}_i^\top \boldsymbol{\beta})^2 + \lambda \sum_{j=1}^{p} \beta_j^2 \right\}
$$

where $\lambda \geq 0$ is the regularization parameter. The closed-form solution is

$$
\hat{\boldsymbol{\beta}}_{\text{Ridge}} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^\top \mathbf{y}
$$

The addition of $\lambda \mathbf{I}$ to $\mathbf{X}^\top\mathbf{X}$ ensures the
matrix is invertible even when $\mathbf{X}$ does not have full column rank. As
$\lambda$ increases, the coefficients shrink toward zero but never reach exactly
zero.

!!! note "Intercept is not penalized"
    Standard practice excludes the intercept $\beta_0$ from the penalty.
    Predictors should be centered (and often standardized) before applying
    Ridge regression so that the penalty treats all coefficients equally.

## Lasso Regression (L1 Penalty)

Lasso regression replaces the squared penalty with the $L^1$ norm:

$$
\hat{\boldsymbol{\beta}}_{\text{Lasso}} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^{n}(y_i - \mathbf{x}_i^\top \boldsymbol{\beta})^2 + \lambda \sum_{j=1}^{p} |\beta_j| \right\}
$$

The $L^1$ penalty has a distinctive property: for sufficiently large $\lambda$,
some coefficients are driven exactly to zero. This makes Lasso a simultaneous
estimation and variable selection method.

Unlike Ridge, there is no closed-form solution for Lasso. The optimization
requires iterative algorithms such as coordinate descent.

## Comparing Ridge and Lasso

| Aspect                  | Ridge ($L^2$)                        | Lasso ($L^1$)                        |
|-------------------------|--------------------------------------|--------------------------------------|
| Penalty                 | $\lambda \sum \beta_j^2$             | $\lambda \sum \lvert\beta_j\rvert$   |
| Closed-form solution    | Yes                                  | No (iterative)                       |
| Feature selection       | No (coefficients shrink but remain nonzero) | Yes (some coefficients become exactly zero) |
| Correlated predictors   | Retains all, shares weight           | Tends to select one, drop the rest   |
| Geometric view          | Constraint region is a sphere        | Constraint region is a diamond       |

## The Role of Lambda

The regularization parameter $\lambda$ controls the bias-variance trade-off:

- $\lambda = 0$: no penalty, solution equals OLS
- $\lambda \to \infty$: all coefficients shrink to zero (intercept-only model)
- Optimal $\lambda$: balances fit quality against model complexity

Cross-validation is the standard method for choosing $\lambda$: fit the model
for a grid of $\lambda$ values and select the one that minimizes prediction
error on held-out folds.

## Computing Ridge with NumPy

The Ridge closed-form solution is straightforward to implement:

```python
import numpy as np

# Design matrix (centered, without intercept column for simplicity)
X = np.array([[1.0, 2.0], [3.0, 1.0], [2.0, 4.0],
              [5.0, 3.0], [4.0, 5.0]])
y = np.array([3.0, 5.0, 7.0, 10.0, 11.0])

lam = 1.0  # regularization parameter
p = X.shape[1]

beta_ridge = np.linalg.solve(X.T @ X + lam * np.eye(p), X.T @ y)
print(f"Ridge coefficients: {beta_ridge}")

# Compare with OLS
beta_ols = np.linalg.solve(X.T @ X, X.T @ y)
print(f"OLS coefficients:   {beta_ols}")
```

!!! warning "Standardize predictors"
    The penalty $\lambda \sum \beta_j^2$ depends on the scale of each
    predictor. If predictors are on different scales, Ridge and Lasso
    penalize them unequally. Always standardize predictors to zero mean
    and unit variance before applying regularization.

## Elastic Net

The elastic net combines both penalties:

$$
\hat{\boldsymbol{\beta}}_{\text{EN}} = \arg\min_{\boldsymbol{\beta}} \left\{ \sum_{i=1}^{n}(y_i - \mathbf{x}_i^\top \boldsymbol{\beta})^2 + \lambda_1 \sum_{j=1}^{p} |\beta_j| + \lambda_2 \sum_{j=1}^{p} \beta_j^2 \right\}
$$

This hybrid approach retains Lasso's variable selection ability while
handling correlated predictors more gracefully than Lasso alone.

## Summary

Regularization combats overfitting by penalizing large coefficients. Ridge
regression adds an $L^2$ penalty and shrinks coefficients smoothly toward
zero, while Lasso uses an $L^1$ penalty that can drive coefficients to
exactly zero, performing variable selection. The regularization parameter
$\lambda$ balances bias and variance, and is typically chosen by
cross-validation.
