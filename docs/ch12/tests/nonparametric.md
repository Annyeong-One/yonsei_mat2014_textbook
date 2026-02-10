# Non-Parametric Tests
Non-parametric tests use ranks instead of raw values, making them robust to outliers and applicable without normality assumptions.
## Rank Tests
### 1. Mann-Whitney U
```python
from scipy import stats
u_stat, p = stats.mannwhitneyu(group1, group2)
```
### 2. Wilcoxon Signed-Rank
```python
w_stat, p = stats.wilcoxon(before, after)
```
### 3. Kruskal-Wallis
```python
h_stat, p = stats.kruskal(g1, g2, g3)
```
## Summary
Non-parametric tests sacrifice power for robustness, ideal for small samples or non-normal data.
