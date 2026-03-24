# t-Tests

The t-test is the fundamental tool for comparing means when the population standard deviation is unknown. Unlike the z-test, which requires known variance, the t-test estimates variance from the sample and uses the heavier-tailed t-distribution to account for this additional uncertainty. SciPy provides three variants: one-sample, independent two-sample, and paired.

## One-Sample t-Test

The one-sample t-test determines whether a sample mean differs significantly from a hypothesized population mean $\mu_0$.

The hypotheses are

$$
H_0: \mu = \mu_0 \quad \text{vs} \quad H_1: \mu \neq \mu_0
$$

The test statistic is

$$
t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
$$

where $\bar{X}$ is the sample mean, $s$ is the sample standard deviation, and $n$ is the sample size. Under $H_0$, the statistic follows a t-distribution with $n - 1$ degrees of freedom:

$$
t \sim t_{n-1}
$$

**Assumptions**: the data are independent and approximately normally distributed (the test is robust to moderate non-normality for $n \geq 30$).

```python
from scipy import stats

# Test whether the mean differs from 50
data = [52.1, 48.3, 51.7, 49.8, 53.2, 50.5, 47.9, 51.0]
t_stat, p_value = stats.ttest_1samp(data, popmean=50)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
```

## Independent Two-Sample t-Test

The independent two-sample t-test compares the means of two unrelated groups. This is the most commonly used t-test variant.

The hypotheses are

$$
H_0: \mu_1 = \mu_2 \quad \text{vs} \quad H_1: \mu_1 \neq \mu_2
$$

When the two groups have equal variances (the pooled t-test), the test statistic is

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
$$

where $s_p$ is the pooled standard deviation:

$$
s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}
$$

Under $H_0$, the statistic follows $t_{n_1 + n_2 - 2}$.

### Welch's t-Test

When the equal-variance assumption is questionable, Welch's t-test provides a more reliable alternative. The test statistic uses separate variance estimates:

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
$$

The degrees of freedom are approximated by the Welch-Satterthwaite equation:

$$
\nu = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}
$$

!!! tip "Default to Welch's Test"
    Welch's t-test performs well even when variances are equal, with minimal power loss. Many statisticians recommend using it by default. In SciPy, set `equal_var=False` to use Welch's version.

**Assumptions**: independent samples, each group is approximately normally distributed.

```python
from scipy import stats

group_a = [23.1, 25.3, 24.8, 22.9, 26.1, 24.5]
group_b = [28.4, 30.1, 27.6, 29.8, 31.2, 28.9]

# Pooled t-test (assumes equal variances)
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=True)
print(f"Pooled t-test: t = {t_stat:.4f}, p = {p_value:.6f}")

# Welch's t-test (does not assume equal variances)
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
print(f"Welch's t-test: t = {t_stat:.4f}, p = {p_value:.6f}")
```

## Paired t-Test

The paired t-test compares means from the same subjects measured under two conditions (e.g., before and after a treatment). By analyzing within-subject differences, it controls for individual variability.

Given paired observations $(X_{1i}, X_{2i})$, define the differences $D_i = X_{1i} - X_{2i}$. The test reduces to a one-sample t-test on the differences:

$$
H_0: \mu_D = 0 \quad \text{vs} \quad H_1: \mu_D \neq 0
$$

$$
t = \frac{\bar{D}}{s_D / \sqrt{n}}
$$

where $\bar{D}$ and $s_D$ are the mean and standard deviation of the differences, and $n$ is the number of pairs. Under $H_0$, the statistic follows $t_{n-1}$.

**Assumptions**: the differences $D_i$ are independent and approximately normally distributed. The original measurements need not be normal — only the differences must be.

```python
from scipy import stats

before = [120, 135, 128, 142, 130, 125, 138]
after = [115, 128, 122, 138, 125, 118, 132]
t_stat, p_value = stats.ttest_rel(before, after)
print(f"Paired t-test: t = {t_stat:.4f}, p = {p_value:.4f}")
```

## Summary of t-Test Variants

| Variant | SciPy Function | Use Case | Degrees of Freedom |
|---|---|---|---|
| One-sample | `ttest_1samp` | Sample mean vs known value | $n - 1$ |
| Independent (pooled) | `ttest_ind(equal_var=True)` | Two independent groups, equal variance | $n_1 + n_2 - 2$ |
| Independent (Welch) | `ttest_ind(equal_var=False)` | Two independent groups, unequal variance | Welch-Satterthwaite $\nu$ |
| Paired | `ttest_rel` | Same subjects, two conditions | $n - 1$ (number of pairs) |

## Summary

The three t-test variants address distinct experimental designs: one-sample tests compare a single group to a reference value, independent tests compare two separate groups, and paired tests compare two measurements on the same subjects. All three share the same core structure of forming a t-ratio (signal divided by estimated noise) and comparing it to the t-distribution, differing only in how the signal, noise, and degrees of freedom are computed.
