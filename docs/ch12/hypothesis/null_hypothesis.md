# Null and Alternative Hypotheses

Every hypothesis test begins with a precise question: is there evidence that a population parameter differs from a specified value? To answer this, we formulate two competing statements — the null hypothesis, which represents the status quo, and the alternative hypothesis, which represents the effect we are trying to detect. The testing framework then uses sample data to decide which hypothesis the evidence supports.

---

## Definitions

The **null hypothesis** $H_0$ is a statement of no effect or no difference. It specifies a particular value (or set of values) for the parameter of interest. The **alternative hypothesis** $H_1$ (or $H_a$) is the complementary claim that the parameter differs from the null value.

For a population mean $\mu$ with hypothesized value $\mu_0$:

$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_1: \mu \neq \mu_0
$$

This is a **two-sided** test. One-sided alternatives take the form $H_1: \mu > \mu_0$ or $H_1: \mu < \mu_0$.

!!! note "Simple vs Composite Hypotheses"
    A **simple** hypothesis specifies the parameter exactly (e.g., $H_0: \mu = 100$). A **composite** hypothesis specifies a range (e.g., $H_1: \mu \neq 100$). Most null hypotheses in practice are simple, while alternatives are composite.

---

## Test Statistic

A **test statistic** is a function of the sample data that measures how far the observed data are from what $H_0$ predicts. For testing a mean with unknown variance, the $t$-statistic is

$$
t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
$$

where $\bar{X}$ is the sample mean, $s$ is the sample standard deviation, and $n$ is the sample size. Under $H_0$, this statistic follows a $t$-distribution with $n - 1$ degrees of freedom.

```python
import numpy as np
from scipy import stats

# Sample data
np.random.seed(42)
data = np.random.normal(loc=102, scale=15, size=30)

# Test H0: mu = 100 vs H1: mu != 100
mu_0 = 100
t_stat, p_value = stats.ttest_1samp(data, mu_0)
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.4f}")
```

---

## Significance Level and Decision Rule

The **significance level** $\alpha$ is the maximum probability of rejecting $H_0$ when it is actually true (Type I error rate). Common choices are $\alpha = 0.05$ and $\alpha = 0.01$.

The **rejection region** consists of all test statistic values that lead to rejecting $H_0$. For a two-sided $t$-test at level $\alpha$, the rejection region is

$$
|t| > t_{\alpha/2,\, n-1}
$$

where $t_{\alpha/2,\, n-1}$ is the upper $\alpha/2$ critical value of the $t$-distribution.

The decision rule is:

- **Reject** $H_0$ if $p\text{-value} < \alpha$
- **Fail to reject** $H_0$ if $p\text{-value} \ge \alpha$

```python
alpha = 0.05

# Critical value approach
t_crit = stats.t.ppf(1 - alpha / 2, df=len(data) - 1)
print(f"Critical value: ±{t_crit:.3f}")
print(f"|t| = {abs(t_stat):.3f}")
print(f"Reject H0 (critical value): {abs(t_stat) > t_crit}")

# p-value approach (equivalent)
print(f"Reject H0 (p-value): {p_value < alpha}")
```

!!! warning "Fail to Reject vs Accept"
    Failing to reject $H_0$ does not mean $H_0$ is true. It means the data do not provide sufficient evidence against $H_0$ at the chosen significance level. The distinction matters: absence of evidence is not evidence of absence.

---

## Types of Hypotheses in Practice

| Test | $H_0$ | $H_1$ |
|---|---|---|
| One-sample $t$-test | $\mu = \mu_0$ | $\mu \neq \mu_0$ |
| Two-sample $t$-test | $\mu_1 = \mu_2$ | $\mu_1 \neq \mu_2$ |
| Paired $t$-test | $\mu_D = 0$ | $\mu_D \neq 0$ |
| Proportion test | $p = p_0$ | $p \neq p_0$ |
| Chi-square test | Variables are independent | Variables are associated |
| ANOVA | $\mu_1 = \mu_2 = \cdots = \mu_k$ | At least one $\mu_i$ differs |

```python
# Two-sample t-test: H0: mu1 = mu2
np.random.seed(42)
group1 = np.random.normal(100, 15, 25)
group2 = np.random.normal(108, 15, 25)

t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"\nTwo-sample t-test:")
print(f"t = {t_stat:.3f}, p = {p_value:.4f}")
print(f"Reject H0 at alpha=0.05: {p_value < 0.05}")
```

---

## Steps of a Hypothesis Test

The complete procedure follows five steps:

1. **State the hypotheses**: Write $H_0$ and $H_1$ in terms of the population parameter
2. **Choose the significance level**: Set $\alpha$ before collecting data
3. **Compute the test statistic**: Calculate the statistic from the observed data
4. **Find the p-value or critical value**: Determine the probability of the observed result under $H_0$
5. **Make a decision**: Reject or fail to reject $H_0$

```python
# Complete example: testing whether a coin is fair
np.random.seed(42)
n_flips = 100
n_heads = 58  # Observed heads

# Step 1: H0: p = 0.5 vs H1: p != 0.5
# Step 2: alpha = 0.05
# Step 3-4: Binomial test
result = stats.binomtest(n_heads, n_flips, p=0.5, alternative='two-sided')
print(f"Observed proportion: {n_heads / n_flips:.2f}")
print(f"p-value: {result.pvalue:.4f}")

# Step 5: Decision
alpha = 0.05
print(f"Reject H0: {result.pvalue < alpha}")
```

---

## Summary

Hypothesis testing provides a formal framework for making decisions about population parameters from sample data. The null hypothesis $H_0$ represents the default assumption of no effect, while the alternative $H_1$ represents the effect being investigated. The test statistic measures the discrepancy between the data and $H_0$, and the p-value quantifies the strength of evidence against $H_0$. The significance level $\alpha$ controls the maximum acceptable probability of a false rejection (Type I error).
