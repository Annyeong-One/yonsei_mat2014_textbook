# Distribution Fitting

A common use case for histograms is visualizing empirical data alongside theoretical probability distributions. This involves estimating distribution parameters from data and overlaying the fitted PDF.

## Fitting Normal Distribution

### Manual PDF Formula

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)  # (10_000,)

    # plot histogram with theoretical PDF (standard normal)
    fig, ax = plt.subplots()
    _, bins, _ = ax.hist(data, bins=100, density=True)
    ax.plot(bins, np.exp(-bins**2 / 2) / np.sqrt(2 * np.pi), 
            '--r', alpha=0.9, lw=5)
    plt.show()

if __name__ == "__main__":
    main()
```

### With Parameter Estimation

When data may not be standard normal, estimate parameters from the sample:

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)  # (10_000,)

    # parameter estimation
    mu = data.mean()
    sigma = data.std()

    # plot histogram with fitted PDF
    fig, ax = plt.subplots()
    _, bins, _ = ax.hist(data, bins=100, density=True)
    pdf = np.exp(-(bins - mu)**2 / (2 * sigma**2)) / np.sqrt(2 * np.pi * sigma**2)
    ax.plot(bins, pdf, '--r', alpha=0.9, lw=5)
    plt.show()

if __name__ == "__main__":
    main()
```

## Using scipy.stats

The `scipy.stats` module provides a cleaner interface for distribution fitting.

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def main():
    # data generation from non-standard normal
    n_samples = 10_000
    data = stats.norm(loc=1, scale=2).rvs(n_samples)  # mean=1, std=2

    # parameter estimation
    mu = data.mean()
    sigma = data.std()

    # plot histogram with fitted PDF
    fig, ax = plt.subplots()
    _, bins, _ = ax.hist(data, bins=100, density=True)
    ax.plot(bins, stats.norm(loc=mu, scale=sigma).pdf(bins), 
            '--r', alpha=0.9, lw=5)
    plt.show()

if __name__ == "__main__":
    main()
```

## General Workflow

1. **Generate or load data**: Obtain the empirical dataset
2. **Estimate parameters**: Use sample statistics (mean, std) or MLE
3. **Plot histogram**: Use `density=True` to normalize
4. **Overlay PDF**: Evaluate theoretical PDF at bin edges
5. **Assess fit**: Visual comparison of histogram and fitted curve

## Fitting Other Distributions

The same pattern applies to other distributions:

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Exponential distribution
data = stats.expon(scale=2).rvs(10_000)
scale_hat = data.mean()

fig, ax = plt.subplots()
_, bins, _ = ax.hist(data, bins=100, density=True, alpha=0.5)
ax.plot(bins, stats.expon(scale=scale_hat).pdf(bins), '--r', lw=2)
plt.show()
```

## Documentation

- [matplotlib.axes.Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)
- [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
