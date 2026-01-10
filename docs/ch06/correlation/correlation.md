# Pearson and Spearman
Correlation measures strength and direction of relationships: Pearson for linear, Spearman for monotonic.
## Methods
### 1. Pearson
```python
from scipy import stats
r, p = stats.pearsonr(x, y)
```
### 2. Spearman
```python
rho, p = stats.spearmanr(x, y)
```
## Summary
Pearson measures linear relationships, Spearman measures monotonic; use Spearman for non-linear or with outliers.
