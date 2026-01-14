# Basic Histogram

The `ax.hist()` method creates histogram visualizations from data arrays. Histograms display the distribution of numerical data by grouping values into bins and showing the frequency or density of each bin.

## Basic Usage

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
| `bins` | int or sequence | Number of bins or bin edges |
| `density` | bool | If True, normalize to form probability density |
| `histtype` | str | Type of histogram: 'bar', 'barstacked', 'step', 'stepfilled' |
| `alpha` | float | Transparency (0.0 to 1.0) |

## Documentation

- [matplotlib.axes.Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)
