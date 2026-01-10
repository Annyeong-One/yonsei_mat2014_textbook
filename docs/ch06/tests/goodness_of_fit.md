# Goodness of Fit
Tests assess how well data matches a theoretical distribution, validating modeling assumptions.
## Tests
### 1. Chi-Square
```python
from scipy import stats
chi2, p = stats.chisquare(observed, expected)
```
### 2. Kolmogorov-Smirnov
```python
ks_stat, p = stats.kstest(data, 'norm')
```
### 3. Shapiro-Wilk
```python
sw_stat, p = stats.shapiro(data)
```
## Summary
Different tests emphasize different distributional aspects (tails, center, overall).
