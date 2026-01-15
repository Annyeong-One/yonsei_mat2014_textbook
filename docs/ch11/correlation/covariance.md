# Covariance
Covariance measures how two variables change together, scale-dependent unlike correlation.
## Definition
### 1. Formula
```python
import numpy as np
cov = np.cov(x, y)[0, 1]
```
### 2. Matrix
```python
cov_matrix = np.cov(data.T)
```
## Summary
Covariance quantifies joint variability but is scale-dependent; correlation (standardized covariance) preferred for comparisons.
