# p-values and Significance
P-values quantify the probability of observing data as extreme as observed, assuming H₀ is true.
## Interpretation
### 1. Meaning
```python
from scipy import stats
t_stat, p_value = stats.ttest_1samp(data, 22)
# p = P(observe data | H₀ true)
```
### 2. Decision Rule
```python
if p_value < 0.05:
    print("Significant")
```
## Summary
P-values measure evidence against H₀, interpreted alongside effect sizes and confidence intervals.
