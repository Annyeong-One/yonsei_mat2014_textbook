# Axes Method - imshow (KDE)

Use `ax.imshow()` with kernel density estimation for smooth 2D density visualization.

[Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)

## Basic Usage

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def main():
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x = np.random.multivariate_normal(mean, cov, 10000)
    print(f"{x.shape = }")
    
    kde = stats.gaussian_kde(x.T)
    
    # Evaluate on a regular grid
    x_ = np.linspace(-3.5, 3.5, 40)  # (40,)
    y_ = np.linspace(-6, 6, 40)      # (40,)
    X, Y = np.meshgrid(x_, y_)       # (40, 40)
    XY = np.vstack([X.ravel(), Y.ravel()])  # (2, 1600)
    Z = kde.evaluate(XY).reshape(X.shape)   # (40, 40)
    
    fig, ax = plt.subplots()
    a = ax.imshow(Z,
                  origin='lower',
                  aspect='auto',
                  extent=[-3.5, 3.5, -6, 6],
                  cmap='Blues')
    plt.colorbar(a, label="density")
    plt.show()

if __name__ == "__main__":
    main()
```

## Understanding the Workflow

### Step-by-Step

```python
import numpy as np
from scipy import stats

# 1. Generate sample data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
print(f"Data shape: {x.shape}")  # (10000, 2)

# 2. Create KDE object
kde = stats.gaussian_kde(x.T)  # Transpose: (2, 10000)

# 3. Create evaluation grid
x_ = np.linspace(-3.5, 3.5, 40)  # (40,)
y_ = np.linspace(-6, 6, 40)      # (40,)
X, Y = np.meshgrid(x_, y_)       # (40, 40) each
print(f"Grid shape: {X.shape}")

# 4. Prepare points for evaluation
XY = np.vstack([X.ravel(), Y.ravel()])  # (2, 1600)
print(f"Evaluation points: {XY.shape}")

# 5. Evaluate KDE
Z = kde.evaluate(XY).reshape(X.shape)  # (40, 40)
print(f"Density matrix: {Z.shape}")
```

| Step | Operation | Shape |
|------|-----------|-------|
| 1 | Sample data | (10000, 2) |
| 2 | Transpose for KDE | (2, 10000) |
| 3 | meshgrid | (40, 40) each |
| 4 | vstack + ravel | (2, 1600) |
| 5 | Evaluate + reshape | (40, 40) |

## Key imshow Parameters

### origin Parameter

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
kde = stats.gaussian_kde(x.T)

x_ = np.linspace(-3.5, 3.5, 50)
y_ = np.linspace(-6, 6, 50)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# origin='upper' (default) - INCORRECT for KDE
axes[0].imshow(Z, origin='upper', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')
axes[0].set_title("origin='upper' (incorrect)")

# origin='lower' - CORRECT for KDE
axes[1].imshow(Z, origin='lower', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')
axes[1].set_title("origin='lower' (correct)")

plt.tight_layout()
plt.show()
```

### extent Parameter

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
kde = stats.gaussian_kde(x.T)

x_ = np.linspace(-3.5, 3.5, 50)
y_ = np.linspace(-6, 6, 50)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Without extent
axes[0].imshow(Z, origin='lower', cmap='Blues')
axes[0].set_title('Without extent (pixels)')

# With extent [xmin, xmax, ymin, ymax]
axes[1].imshow(Z, origin='lower', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')
axes[1].set_title('With extent (data coords)')

plt.tight_layout()
plt.show()
```

### aspect Parameter

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
kde = stats.gaussian_kde(x.T)

x_ = np.linspace(-3.5, 3.5, 50)
y_ = np.linspace(-6, 6, 50)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
aspects = ['equal', 'auto', 0.5]

for ax, aspect in zip(axes, aspects):
    ax.imshow(Z, origin='lower', aspect=aspect,
              extent=[-3.5, 3.5, -6, 6], cmap='Blues')
    ax.set_title(f"aspect='{aspect}'" if isinstance(aspect, str) else f"aspect={aspect}")

plt.tight_layout()
plt.show()
```

## Grid Resolution

### Different Resolutions

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
kde = stats.gaussian_kde(x.T)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
resolutions = [20, 40, 80, 150]

for ax, res in zip(axes, resolutions):
    x_ = np.linspace(-3.5, 3.5, res)
    y_ = np.linspace(-6, 6, res)
    X, Y = np.meshgrid(x_, y_)
    Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)
    
    im = ax.imshow(Z, origin='lower', aspect='auto',
                   extent=[-3.5, 3.5, -6, 6], cmap='Blues')
    ax.set_title(f'Resolution: {res}x{res}')
    fig.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

## Comparison: Three Methods

### hist2d vs hexbin vs KDE

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# hist2d - rectangular bins
_, _, _, im1 = axes[0].hist2d(x[:, 0], x[:, 1], bins=30, cmap='Blues')
axes[0].set_title('hist2d')
fig.colorbar(im1, ax=axes[0])

# hexbin - hexagonal bins
im2 = axes[1].hexbin(x[:, 0], x[:, 1], gridsize=30, cmap='Blues')
axes[1].set_title('hexbin')
fig.colorbar(im2, ax=axes[1])

# KDE with imshow - smooth density
kde = stats.gaussian_kde(x.T)
x_ = np.linspace(-4, 4, 80)
y_ = np.linspace(-6, 6, 80)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)
im3 = axes[2].imshow(Z, origin='lower', aspect='auto',
                     extent=[-4, 4, -6, 6], cmap='Blues')
axes[2].set_title('KDE (imshow)')
fig.colorbar(im3, ax=axes[2])

plt.tight_layout()
plt.show()
```

| Method | Bins | Output | Best For |
|--------|------|--------|----------|
| hist2d | Rectangle | Counts | Large datasets |
| hexbin | Hexagon | Counts | Better perception |
| KDE | Continuous | Density | Smooth estimate |

## Practical Example

### Complete KDE Visualization

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Generate bimodal data
np.random.seed(42)
n = 5000
x1 = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], n)
x2 = np.random.multivariate_normal([3, 3], [[0.8, -0.3], [-0.3, 0.8]], n)
x = np.vstack([x1, x2])

# Compute KDE
kde = stats.gaussian_kde(x.T)

# High resolution grid
x_ = np.linspace(-4, 7, 100)
y_ = np.linspace(-4, 7, 100)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

im = ax.imshow(Z, origin='lower', aspect='equal',
               extent=[-4, 7, -4, 7], cmap='YlOrRd')

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Kernel Density Estimation', fontsize=14)

cbar = fig.colorbar(im, ax=ax, label='Density')
plt.tight_layout()
plt.show()
```
