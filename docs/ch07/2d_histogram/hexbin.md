# Axes Method - hexbin

The `ax.hexbin()` method creates hexagonal binning plots for 2D data visualization.

[Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html)

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
    a = ax.hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues')
    plt.colorbar(a, label="density")
    plt.show()

if __name__ == "__main__":
    main()
```

## Why Hexagonal Bins?

| Shape | Advantages |
|-------|------------|
| Hexagon | Equal distance to all neighbors, better visual perception |
| Rectangle | Simpler but diagonal neighbors are farther |

## gridsize Parameter

### Different Grid Sizes

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
gridsizes = [10, 20, 30, 50]

for ax, gs in zip(axes, gridsizes):
    hb = ax.hexbin(x[:, 0], x[:, 1], gridsize=gs, cmap='Blues')
    ax.set_title(f'gridsize={gs}')
    fig.colorbar(hb, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

### Asymmetric Gridsize

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Symmetric
hb1 = axes[0].hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues')
axes[0].set_title('gridsize=30')
fig.colorbar(hb1, ax=axes[0])

# Asymmetric (x, y)
hb2 = axes[1].hexbin(x[:, 0], x[:, 1], gridsize=(40, 20), cmap='Blues')
axes[1].set_title('gridsize=(40, 20)')
fig.colorbar(hb2, ax=axes[1])

plt.tight_layout()
plt.show()
```

## Return Value

### PolyCollection Object

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, ax = plt.subplots()
hb = ax.hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues')

print(f"Type: {type(hb)}")              # PolyCollection
print(f"Array shape: {hb.get_array().shape}")  # Counts per hexagon

plt.colorbar(hb, label='counts')
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
cmaps = ['Blues', 'Reds', 'viridis', 'plasma', 'hot', 'YlOrRd']

for ax, cmap in zip(axes.flat, cmaps):
    hb = ax.hexbin(x[:, 0], x[:, 1], gridsize=30, cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")
    fig.colorbar(hb, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

## mincnt Parameter

### Filtering Low Counts

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
mincnts = [None, 5, 20]

for ax, mc in zip(axes, mincnts):
    hb = ax.hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues', mincnt=mc)
    ax.set_title(f'mincnt={mc}')
    fig.colorbar(hb, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

## Logarithmic Scale

### bins='log'

```python
import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Linear scale
hb1 = axes[0].hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues')
axes[0].set_title('Linear scale')
fig.colorbar(hb1, ax=axes[0])

# Log scale
hb2 = axes[1].hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues', bins='log')
axes[1].set_title("bins='log'")
fig.colorbar(hb2, ax=axes[1])

plt.tight_layout()
plt.show()
```

## Practical Example

### Density Analysis

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate bimodal data
np.random.seed(42)
n = 5000
x1 = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], n)
x2 = np.random.multivariate_normal([3, 3], [[1, -0.5], [-0.5, 1]], n)
x = np.vstack([x1, x2])

fig, ax = plt.subplots(figsize=(10, 8))

hb = ax.hexbin(x[:, 0], x[:, 1], gridsize=35, cmap='YlOrRd', 
               edgecolors='white', linewidths=0.2)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Hexbin: Bimodal Distribution', fontsize=14)

cbar = fig.colorbar(hb, ax=ax, label='Point Count')
plt.tight_layout()
plt.show()
```
