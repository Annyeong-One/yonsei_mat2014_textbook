# KDE vs Histogram

Histograms and kernel density estimators are the two primary nonparametric approaches to estimating a probability density function from data. Both methods avoid assuming a specific distributional form, but they differ fundamentally in smoothness, convergence properties, and sensitivity to tuning parameters. Understanding these differences helps practitioners choose the right tool for visualization and analysis.

## Histogram as a Density Estimator

A histogram partitions the real line into bins $B_1, B_2, \ldots$ of width $w$ and estimates the density as a piecewise constant function:

$$
\hat{f}_{\text{hist}}(x) = \frac{1}{n \cdot w} \sum_{i=1}^{n} \mathbf{1}(x_i \in B_k) \quad \text{for } x \in B_k
$$

where $\mathbf{1}(\cdot)$ is the indicator function. The result is a step function: constant within each bin, discontinuous at bin edges. The bin width $w$ plays a role analogous to the bandwidth in KDE, controlling the bias-variance tradeoff.

## KDE as a Density Estimator

The kernel density estimator replaces the hard bin assignment with a smooth kernel centered at each observation:

$$
\hat{f}_{\text{KDE}}(x) = \frac{1}{nh}\sum_{i=1}^{n} K\!\left(\frac{x - x_i}{h}\right)
$$

With a Gaussian kernel, the result is an infinitely differentiable function. Every data point contributes to the estimate at every query point $x$, with the contribution decaying smoothly with distance.

## Key Differences

| Property | Histogram | KDE |
|---|---|---|
| Smoothness | Step function (discontinuous) | Inherits kernel smoothness (continuous) |
| Tuning parameter | Bin width $w$ and bin edges | Bandwidth $h$ |
| Sensitivity to parameter choice | Bin edges and width both matter | Only bandwidth matters |
| Optimal MISE rate | $O(n^{-2/3})$ | $O(n^{-4/5})$ |
| Computational cost | $O(n)$ to construct | $O(mn)$ to evaluate at $m$ points |
| Derivative estimation | Not possible (discontinuous) | Natural (smooth) |

The KDE achieves a faster convergence rate because it uses the smoothness of the kernel to extract more information from the data. The histogram's rate is limited by its piecewise-constant structure.

## Bin Edge Sensitivity

A notable disadvantage of histograms is sensitivity to the choice of bin edges. Shifting the bin boundaries by a fraction of the bin width can substantially change the shape of the estimate, creating or removing apparent modes.

```python
import numpy as np
from scipy.stats import gaussian_kde

# Generate data with two close modes
np.random.seed(42)
data = np.concatenate([
    np.random.normal(0, 0.5, 200),
    np.random.normal(1.5, 0.5, 200)
])

# Two histograms with different bin edges
bins_a = np.arange(-3, 5, 0.5)           # edges at 0.0, 0.5, 1.0, ...
bins_b = bins_a + 0.25                     # shifted by 0.25

counts_a, _ = np.histogram(data, bins=bins_a, density=True)
counts_b, _ = np.histogram(data, bins=bins_b, density=True)
print(f"Max density (edges A): {counts_a.max():.4f}")
print(f"Max density (edges B): {counts_b.max():.4f}")

# KDE is unaffected by any such shift
kde = gaussian_kde(data)
print(f"KDE at x=0:   {kde(np.array([0.0]))[0]:.4f}")
print(f"KDE at x=1.5: {kde(np.array([1.5]))[0]:.4f}")
```

KDE does not use bins, so it is invariant to any notion of edge placement. This makes KDE more reliable for detecting features like modes.

!!! warning "Histogram Artifacts"
    When using histograms to assess whether a distribution is unimodal or bimodal, small changes in bin width or edge placement can create or destroy apparent modes. KDE provides more stable visual evidence of multimodality.

## When to Use Each Method

Despite the theoretical advantages of KDE, histograms remain useful in several situations:

- **Large datasets**: Histograms are $O(n)$ to construct and fast to render, making them practical for millions of observations
- **Discrete data**: For integer-valued or categorical data, bins aligned with the discrete values give a natural representation
- **Quick exploration**: Histograms are available in virtually every plotting library with minimal configuration
- **Communication**: Many audiences are more familiar with histograms than with smooth density curves

KDE is preferred when:

- **Smoothness matters**: Density derivatives, mode detection, or probability computations require a smooth estimate
- **Accuracy matters**: The faster convergence rate of KDE means better estimates for moderate sample sizes
- **Resampling is needed**: A KDE provides a generative model from which new samples can be drawn

!!! tip "Combining Both"
    A common visualization strategy is to overlay a KDE curve on top of a histogram. The histogram provides an intuitive sense of the data distribution, while the KDE highlights the smooth underlying shape. In matplotlib, use `plt.hist(data, density=True)` followed by `plt.plot(x_grid, kde(x_grid))`.

## Summary

Histograms and KDE both estimate probability densities nonparametrically, but they differ in smoothness, convergence rate, and sensitivity to tuning choices. The histogram produces a discontinuous step function sensitive to bin edges and converges at rate $O(n^{-2/3})$, while KDE produces a smooth function invariant to edge placement and converges at $O(n^{-4/5})$. Histograms are computationally cheaper and more familiar to general audiences, while KDE provides smoother estimates better suited for inference and resampling.
