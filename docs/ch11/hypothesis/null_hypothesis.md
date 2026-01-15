# Null Hypothesis
The null hypothesis (H₀) represents no effect, tested against an alternative (H₁) using p-values and significance levels.
## Framework
### 1. Setup
```python
# H₀: μ = 100
# H₁: μ ≠ 100
from scipy import stats
t_stat, p = stats.ttest_1samp(data, 100)
```
### 2. Decision
```python
alpha = 0.05
if p < alpha:
    print("Reject H₀")
```
## Summary
Null hypothesis testing balances Type I (α) and Type II (β) errors through significance level selection.
