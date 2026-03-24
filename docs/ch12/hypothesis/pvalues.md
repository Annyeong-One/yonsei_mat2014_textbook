# p-values and Statistical Significance

In hypothesis testing, after computing a test statistic, we need a way to calibrate how surprising the observed result is under the null hypothesis. The p-value provides this calibration by converting the test statistic into a probability scale. This section defines p-values formally, explains their correct interpretation, and presents the standard decision rule for statistical significance.

## Definition

A **p-value** is the probability, under the null hypothesis $H_0$, of obtaining a test statistic at least as extreme as the value actually observed from the sample data.

For an observed test statistic $t_{\text{obs}}$, the p-value depends on whether the test is one-sided or two-sided. In a one-sided (upper-tail) test, the p-value is

$$
p = P(T \geq t_{\text{obs}} \mid H_0)
$$

where $T$ denotes the random test statistic under $H_0$. For a two-sided test, the p-value accounts for extreme values in both tails:

$$
p = P(|T| \geq |t_{\text{obs}}| \mid H_0)
$$

A small p-value indicates that the observed data would be unlikely if $H_0$ were true, providing evidence against the null hypothesis.

!!! warning "Common Misconception"
    The p-value is **not** the probability that $H_0$ is true. It is the probability of observing a test statistic as extreme as or more extreme than the one obtained, assuming $H_0$ holds. Confusing these two interpretations is one of the most widespread errors in applied statistics.

## Decision Rule

Given a pre-specified significance level $\alpha$ (commonly $\alpha = 0.05$), the decision rule is:

- **Reject** $H_0$ if $p < \alpha$
- **Fail to reject** $H_0$ if $p \geq \alpha$

The significance level $\alpha$ represents the maximum tolerable probability of a Type I error — rejecting $H_0$ when it is in fact true.

The following example illustrates how to compute a p-value using a one-sample $t$-test. Suppose we have measurements and wish to test $H_0: \mu = 22$ against $H_1: \mu \neq 22$.

```python
import numpy as np
from scipy import stats

# Sample data: 10 measurements
data = np.array([23.1, 22.5, 24.0, 21.8, 23.7, 22.9, 24.3, 23.0, 22.6, 23.5])

# One-sample t-test: H₀: μ = 22 vs H₁: μ ≠ 22
t_stat, p_value = stats.ttest_1samp(data, 22)
# p_value = P(|T| >= |t_obs| | H₀ true) for a two-sided test

alpha = 0.05
if p_value < alpha:
    print(f"Reject H₀ (p = {p_value:.4f} < {alpha})")
else:
    print(f"Fail to reject H₀ (p = {p_value:.4f} >= {alpha})")
```

## Summary

The p-value converts a test statistic into a probability that measures the strength of evidence against $H_0$. By comparing the p-value to a pre-specified significance level $\alpha$, we obtain a binary decision rule for hypothesis testing.
