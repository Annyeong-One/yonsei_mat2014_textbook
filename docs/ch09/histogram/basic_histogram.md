# Basic Histogram

A histogram groups numerical data into bins and displays the count (or density) of observations in each bin, revealing the shape of the underlying distribution. Whether the data is symmetric, skewed, or multimodal becomes immediately visible, making histograms one of the most common first steps in exploratory data analysis. The `ax.hist()` method in Matplotlib creates histogram visualizations from data arrays.

## Basic Usage

The following example generates 10,000 samples from a standard normal distribution and plots the histogram with 100 bins.

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)  # (10_000,)

    # plot histogram
    fig, ax = plt.subplots()
    ax.hist(data, bins=100)
    plt.show()

if __name__ == "__main__":
    main()
```

## Method Signature

The most commonly used parameters are `bins`, `density`, and `histtype`. The full signature is shown below for reference.

```python
ax.hist(x, bins=None, range=None, density=False, weights=None,
        cumulative=False, bottom=None, histtype='bar', align='mid',
        orientation='vertical', rwidth=None, log=False, color=None,
        label=None, stacked=False, **kwargs)
```

## Key Parameters Overview

| Parameter | Type | Description |
|-----------|------|-------------|
| `x` | array-like | Input data |
| `bins` | int or sequence | Number of bins or bin edges (default: `rcParams["hist.bins"]`, typically 10) |
| `density` | bool | If True, normalize so that the total area equals 1. Each bin height equals count / (total count × bin width) |
| `histtype` | str | Type of histogram: `'bar'`, `'barstacked'`, `'step'`, `'stepfilled'` |
| `alpha` | float | Transparency (0.0 to 1.0), passed via `**kwargs` to the underlying patch artist |

!!! tip "Official Documentation"
    The full parameter descriptions, return values, and additional examples are available in the [Matplotlib API reference for `ax.hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html).
