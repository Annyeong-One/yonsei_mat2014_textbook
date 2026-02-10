# Return Values

The `ax.hist()` method returns three objects that provide information about the created histogram.

## Return Signature

```python
n, bins, patches = ax.hist(data, ...)
```

| Return | Type | Description |
|--------|------|-------------|
| `n` | array or list of arrays | Values of the histogram bins (counts or density) |
| `bins` | array | Edges of the bins (length = number of bins + 1) |
| `patches` | BarContainer or list | Container of individual bar artists |

## Using Return Values

The returned `bins` array is particularly useful for overlaying fitted distributions, as it provides the exact x-coordinates used by the histogram.

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    # data generation
    n_samples = 10_000
    data = np.random.randn(n_samples)

    # parameter estimation
    mu = data.mean()
    sigma = data.std()

    # plot histogram and capture return values
    fig, ax = plt.subplots()
    _, x, _ = ax.hist(data, bins=100, density=True, alpha=0.2)
    
    # use bins (x) to compute and plot pdf
    pdf = stats.norm(loc=mu, scale=sigma).pdf(x)
    ax.plot(x, pdf, '--r')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()

if __name__ == "__main__":
    main()
```

## Practical Applications

### Accessing bin counts

```python
n, bins, patches = ax.hist(data, bins=50)
print(f"Total count: {n.sum()}")
print(f"Max bin count: {n.max()}")
print(f"Bin with max count: {bins[n.argmax()]:.2f} to {bins[n.argmax()+1]:.2f}")
```

### Customizing individual bars

```python
n, bins, patches = ax.hist(data, bins=50)

# Color bars based on height
for count, patch in zip(n, patches):
    patch.set_facecolor(plt.cm.viridis(count / n.max()))
```

## Documentation

- [matplotlib.axes.Axes.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html)
