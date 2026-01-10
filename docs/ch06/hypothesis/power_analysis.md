# Power Analysis
Statistical power (1-β) is the probability of correctly rejecting a false null hypothesis.
## Concept
### 1. Sample Size
```python
from statsmodels.stats.power import tt_solve_power
n = tt_solve_power(effect_size=0.5, alpha=0.05, power=0.80)
```
### 2. Effect Size
```python
# Cohen's d
d = (mean1 - mean2) / pooled_std
```
## Summary
Power analysis ensures studies detect meaningful effects, balancing α and 1-β.
