# Parametric Tests
Parametric tests assume specific distributions (usually normal) with methods for comparing means, variances, and proportions based on distribution parameters.
## t-Tests
### 1. One-Sample t-Test
```python
from scipy import stats
data = [23, 25, 27, 24, 26]
t_stat, p_value = stats.ttest_1samp(data, popmean=25)
```
### 2. Two-Sample t-Test
```python
group1 = [23, 25, 27]
group2 = [30, 32, 31]
t_stat, p_value = stats.ttest_ind(group1, group2)
```
### 3. Paired t-Test
```python
before = [120, 125, 130]
after = [118, 122, 128]
t_stat, p_value = stats.ttest_rel(before, after)
```
## Summary
Parametric tests are powerful when assumptions hold but require normality and homogeneity of variance checks.
