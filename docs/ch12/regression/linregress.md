# Simple Linear Regression with linregress

In many scientific and engineering applications, we observe two variables and want to
quantify how one depends on the other. Simple linear regression provides the most
fundamental approach: fit a straight line through the data and measure how well that
line explains the observed variation. SciPy's `stats.linregress` offers a fast,
one-call interface for this task, returning the fitted parameters along with key
inferential statistics.

---

## The Linear Model

Simple linear regression assumes that the relationship between a predictor $x$ and
a response $y$ follows

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad i = 1, \dots, n
$$

where $\beta_0$ is the intercept, $\beta_1$ is the slope, and $\varepsilon_i$ are
independent error terms with $\mathbb{E}[\varepsilon_i] = 0$ and
$\operatorname{Var}(\varepsilon_i) = \sigma^2$.

The goal is to estimate $\beta_0$ and $\beta_1$ from observed data
$\{(x_i, y_i)\}_{i=1}^n$ so that the fitted line $\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$
best approximates the data in the least-squares sense.

## OLS Estimators

Ordinary least squares (OLS) minimizes the sum of squared residuals

$$
S(\beta_0, \beta_1) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2
$$

Setting partial derivatives to zero yields the closed-form solutions

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
$$

$$
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}
$$

where $\bar{x}$ and $\bar{y}$ are the sample means of $x$ and $y$ respectively.

## Coefficient of Determination

The coefficient of determination $R^2$ measures the proportion of variance in
$y$ that the linear model explains. It is defined as

$$
R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}
$$

An $R^2$ value near 1 indicates that the line captures most of the variability,
while a value near 0 indicates a poor fit. In simple linear regression,
$R^2 = r^2$ where $r$ is the Pearson correlation coefficient.

## Hypothesis Test for the Slope

To test whether the predictor $x$ has a statistically significant linear
relationship with $y$, we test

$$
H_0: \beta_1 = 0 \quad \text{vs} \quad H_1: \beta_1 \neq 0
$$

The test statistic is

$$
t = \frac{\hat{\beta}_1}{\text{SE}(\hat{\beta}_1)}
$$

where the standard error of the slope is

$$
\text{SE}(\hat{\beta}_1) = \sqrt{\frac{\hat{\sigma}^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}}
$$

and $\hat{\sigma}^2 = \frac{1}{n-2}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$ is the
residual variance estimator. Under $H_0$, $t$ follows a $t$-distribution with
$n - 2$ degrees of freedom.

## Using scipy.stats.linregress

The `linregress` function accepts two arrays and returns five values packed into
a named result object.

```python
from scipy import stats

# Example: hours studied vs exam score
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [52, 58, 65, 68, 73, 79, 84, 90]

result = stats.linregress(hours, scores)
```

The returned `LinregressResult` contains:

| Attribute     | Description                                       |
|---------------|---------------------------------------------------|
| `slope`       | Estimated slope $\hat{\beta}_1$                   |
| `intercept`   | Estimated intercept $\hat{\beta}_0$               |
| `rvalue`      | Pearson correlation coefficient $r$                |
| `pvalue`      | Two-sided p-value for testing $H_0: \beta_1 = 0$  |
| `stderr`      | Standard error of the slope $\text{SE}(\hat{\beta}_1)$ |

!!! tip "Accessing intercept standard error"
    Since SciPy 1.7, `result.intercept_stderr` provides the standard error
    of the intercept estimate $\text{SE}(\hat{\beta}_0)$.

## Interpreting the Output

```python
print(f"Slope:     {result.slope:.4f}")
print(f"Intercept: {result.intercept:.4f}")
print(f"R-squared: {result.rvalue**2:.4f}")
print(f"p-value:   {result.pvalue:.4e}")
print(f"Std error: {result.stderr:.4f}")
```

The slope $\hat{\beta}_1$ estimates the average change in $y$ per unit increase
in $x$. The p-value tests whether this slope differs significantly from zero.
A small p-value (typically below 0.05) leads to rejecting $H_0$ and concluding
that the linear relationship is statistically significant.

The $R^2$ value (obtained as `result.rvalue**2`) indicates how much of the
variation in the response is captured by the linear fit.

## Prediction

Once the model is fitted, predictions for new values of $x$ are computed as

$$
\hat{y}_{\text{new}} = \hat{\beta}_0 + \hat{\beta}_1 x_{\text{new}}
$$

```python
import numpy as np

x_new = np.array([9, 10])
y_pred = result.intercept + result.slope * x_new
```

!!! warning "Extrapolation risk"
    Predictions outside the range of the observed $x$ values rely on the
    assumption that the linear relationship continues to hold. Extrapolation
    can produce misleading results if the true relationship is nonlinear
    beyond the observed range.

## Assumptions and Limitations

Simple linear regression via `linregress` assumes:

1. **Linearity** -- the true relationship between $x$ and $y$ is linear
2. **Independence** -- observations are independent of each other
3. **Homoscedasticity** -- the error variance $\sigma^2$ is constant across all $x$
4. **Normality** -- the errors $\varepsilon_i$ are normally distributed (required for the $t$-test and p-value to be exact)

When these assumptions are violated, consider transformations, robust regression,
or nonparametric alternatives. Residual analysis provides diagnostic tools for
checking these assumptions.

## Summary

`scipy.stats.linregress` fits a simple linear regression model by ordinary least
squares and returns the slope, intercept, Pearson correlation, p-value, and
standard error in a single function call. The slope estimator and its p-value
enable formal testing of linear dependence, while $R^2$ quantifies the
explanatory power of the fitted line.
