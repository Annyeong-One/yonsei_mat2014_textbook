# Axes Method - hist2d

The `ax.hist2d()` method creates 2D histograms with rectangular bins.

[Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html)

## Basic Usage

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x = np.random.multivariate_normal(mean, cov, 10000)
    print(f"{x.shape = }")
    
    fig, ax = plt.subplots()
    ax.hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')
    plt.show()

if __name__ == "__main__":
    main()
```

## Understanding the Data

### Multivariate Normal Distribution

```python
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

print(f"Shape: {x.shape}")        # (10000, 2)
print(f"X column: {x[:, 0].shape}")  # (10000,)
print(f"Y column: {x[:, 1].shape}")  # (10000,)
```

| Parameter | Value | Description |
|-----------|-------|-------------|
| mean | [0, 0] | Center of distribution |
| cov | [[1, 1], [1, 2]] | Covariance matrix |
| n_samples | 10000 | Number of points |

## bins Parameter

### Uniform Bins

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
bin_counts = [10, 20, 30, 50]

for ax, bins in zip(axes, bin_counts):
    ax.hist2d(x[:, 0], x[:, 1], bins=bins, cmap='Blues')
    ax.set_title(f'bins={bins}')

plt.tight_layout()
plt.show()
```

### Asymmetric Bins

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Symmetric
axes[0].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')
axes[0].set_title('bins=30')

# Asymmetric [x_bins, y_bins]
axes[1].hist2d(x[:, 0], x[:, 1], bins=[40, 20], cmap='Blues')
axes[1].set_title('bins=[40, 20]')

plt.tight_layout()
plt.show()
```

## Colormaps

### Different Colormaps

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
cmaps = ['Blues', 'Reds', 'Greens', 'viridis', 'plasma', 'hot']

for ax, cmap in zip(axes.flat, cmaps):
    ax.hist2d(x[:, 0], x[:, 1], bins=30, cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")

plt.tight_layout()
plt.show()
```

## Return Values

### Accessing Histogram Data

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, ax = plt.subplots()
h, xedges, yedges, image = ax.hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')

print(f"h shape: {h.shape}")           # (30, 30) - count matrix
print(f"xedges shape: {xedges.shape}") # (31,) - bin edges
print(f"yedges shape: {yedges.shape}") # (31,) - bin edges
print(f"image type: {type(image)}")    # QuadMesh

plt.show()
```

| Return | Shape | Description |
|--------|-------|-------------|
| h | (bins, bins) | Count per bin |
| xedges | (bins+1,) | X bin edges |
| yedges | (bins+1,) | Y bin edges |
| image | QuadMesh | Rendered image |

## range Parameter

### Limiting Data Range

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Full range
axes[0].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')
axes[0].set_title('Full range')

# Limited range
axes[1].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues',
               range=[[-2, 2], [-3, 3]])
axes[1].set_title('range=[[-2, 2], [-3, 3]]')

plt.tight_layout()
plt.show()
```

## density Parameter

### Counts vs Density

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Counts (default)
_, _, _, im1 = axes[0].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')
axes[0].set_title('Counts (default)')
fig.colorbar(im1, ax=axes[0], label='counts')

# Density
_, _, _, im2 = axes[1].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues', density=True)
axes[1].set_title('density=True')
fig.colorbar(im2, ax=axes[1], label='density')

plt.tight_layout()
plt.show()
```

## Practical Example

### Distribution Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate correlated data
np.random.seed(42)
mean = [0, 0]
cov = [[1, 0.8], [0.8, 1]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, ax = plt.subplots(figsize=(8, 6))

h, xedges, yedges, im = ax.hist2d(
    x[:, 0], x[:, 1], 
    bins=40, 
    cmap='YlOrRd'
)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('2D Histogram: Correlated Normal', fontsize=14)
fig.colorbar(im, ax=ax, label='Counts')

plt.tight_layout()
plt.show()
```
