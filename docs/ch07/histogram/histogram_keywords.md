# Histogram Keywords

The `ax.hist()` method accepts various keyword arguments to customize histogram appearance and behavior.

## bins

The `bins` parameter controls how data is grouped. It accepts either an integer (number of bins) or a sequence (explicit bin edges).

### bins as int

When `bins` is an integer, matplotlib automatically calculates bin edges spanning the data range.

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)

    # plot histogram with integer bins
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.hist(data, bins=100, alpha=0.2)  # <--- int used
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

### bins as sequence

When `bins` is a sequence, it defines the exact positions of bin edges, providing precise control over binning.

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)

    # plot histogram with sequence bins
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.hist(data, bins=np.linspace(-4, 4, 100), alpha=0.2)  # <--- sequence used
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## density

The `density` parameter controls whether the histogram shows counts or probability density.

- `density=False` (default): y-axis shows raw counts
- `density=True`: y-axis shows probability density (area under histogram equals 1)

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)

    # plot histogram in density scale
    fig, ax = plt.subplots()
    ax.hist(data, bins=100, density=True, alpha=0.2)  # <--- density=True
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()

if __name__ == "__main__":
    main()
```

## histtype

The `histtype` parameter controls the visual style of the histogram.

| Value | Description |
|-------|-------------|
| `'bar'` | Traditional bar-style histogram (default) |
| `'barstacked'` | Bar-style with stacked data |
| `'step'` | Unfilled line histogram |
| `'stepfilled'` | Filled line histogram |

### Example: step histogram with PMF overlay

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Set the seed for reproducibility
np.random.seed(42)

# Parameters for the binomial distribution
num_trials = 10
success_probability = 0.6

# Number of random samples to generate
num_samples = 100

# Generate random samples from the binomial distribution
samples = stats.binom(num_trials, success_probability).rvs(num_samples)

# Possible outcomes from 0 successes to 'num_trials' successes
outcomes = np.arange(num_trials + 1)

# Probability mass function values for each outcome
pmf_values = stats.binom(num_trials, success_probability).pmf(outcomes)

# Set up the plot
fig, ax = plt.subplots(figsize=(12, 3))

# Bar plot to show the probability mass function
ax.bar(outcomes, pmf_values, alpha=0.2, color='red', label='Binomial PMF')

# Histogram of the sampled data with step style
ax.hist(samples, bins=np.arange(num_trials + 2) - 0.5, 
        density=True, histtype='step', label='Sampled Data Histogram')

# Adding labels and legend
ax.set_xlabel('Number of Successes')
ax.set_ylabel('Probability')
ax.legend()

plt.show()
```

## Documentation

- [matplotlib.axes.Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)
