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


---

## Exercises

**Exercise 1.** Write code that generates 2000 samples from a normal distribution, plots a histogram with `density=True`, and overlays the theoretical PDF curve using `scipy.stats.norm.pdf()`.

??? success "Solution to Exercise 1"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    data = np.random.normal(5, 2, 1000)

    fig, ax = plt.subplots()
    ax.hist(data, bins=30, density=True, alpha=0.7, color='steelblue',
            edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Density')
    ax.set_title('Histogram')
    plt.show()
    ```

---

**Exercise 2.** Explain why `density=True` is necessary when overlaying a PDF curve on a histogram. What units does the y-axis represent?

??? success "Solution to Exercise 2"
    `ax.hist()` returns `(n, bins, patches)` where `n` has shape `(20,)` containing the count or density in each bin, `bins` has shape `(21,)` containing the bin edges (one more than the number of bins), and `patches` is a list of 20 Rectangle objects.

---

**Exercise 3.** Create a figure that fits and overlays an exponential distribution PDF on histogram data generated from `np.random.exponential()`.

??? success "Solution to Exercise 3"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    normal_data = np.random.normal(0, 1, 1000)
    exp_data = np.random.exponential(1, 1000)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.hist(normal_data, bins=30, density=True, alpha=0.7, color='steelblue')
    ax1.set_title('Normal Distribution')

    ax2.hist(exp_data, bins=30, density=True, alpha=0.7, color='coral')
    ax2.set_title('Exponential Distribution')

    plt.tight_layout()
    plt.show()
    ```

---

**Exercise 4.** Write code that generates data from a mixture of two normal distributions and overlays both individual component PDFs and the combined PDF on the histogram.

??? success "Solution to Exercise 4"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    data1 = np.random.normal(0, 1, 1000)
    data2 = np.random.normal(3, 1, 1000)

    fig, ax = plt.subplots()
    ax.hist(data1, bins=30, alpha=0.5, label='N(0, 1)', color='blue')
    ax.hist(data2, bins=30, alpha=0.5, label='N(3, 1)', color='red')
    ax.legend()
    ax.set_title('Overlaid Histograms')
    plt.show()
    ```
