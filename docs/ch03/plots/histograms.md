# Histograms and

Histograms and density plots are fundamental tools for exploring the distributional properties of data, especially in statistics and finance.

---

## Histograms

A histogram visualizes the frequency distribution of data by grouping values into bins.

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=1000)
plt.hist(data, bins=30)
plt.show()
```

Key parameters:
- `bins`: number of bins or bin edges
- `density`: normalize to form a probability density

---

## Normalized

```python
plt.hist(data, bins=30, density=True)
```

This allows comparison with theoretical densities.

---

## Overlaying density

```python
from scipy.stats import norm

x = np.linspace(data.min(), data.max(), 200)
plt.hist(data, bins=30, density=True)
plt.plot(x, norm.pdf(x), linewidth=2)
```

---

## Financial

Histograms are used for:
- return distributions,
- residual analysis,
- stress scenario inspection.

---

## Key takeaways

- Histograms summarize distributions.
- Normalization enables density comparison.
- Choose bins carefully.
