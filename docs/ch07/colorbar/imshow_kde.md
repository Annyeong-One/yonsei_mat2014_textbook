# Axes Method - imshow (KDE)

Use `ax.imshow()` with kernel density estimation (KDE) for smooth density visualization.

[Official Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html)

## Basic Usage

### KDE with imshow

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
                  cmap='Blues')  # type(a) AxesImage
    plt.colorbar(a, label="density")
    plt.show()

if __name__ == "__main__":
    main()
```

## Understanding KDE

### Kernel Density Estimation Steps

```python
import numpy as np
from scipy import stats

# 1. Generate sample data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

# 2. Create KDE object (transpose for scipy)
kde = stats.gaussian_kde(x.T)  # Input shape: (2, n_samples)

# 3. Create evaluation grid
x_ = np.linspace(-3.5, 3.5, 40)
y_ = np.linspace(-6, 6, 40)
X, Y = np.meshgrid(x_, y_)

print(f"X shape: {X.shape}")  # (40, 40)
print(f"Y shape: {Y.shape}")  # (40, 40)

# 4. Prepare points for evaluation
XY = np.vstack([X.ravel(), Y.ravel()])
print(f"XY shape: {XY.shape}")  # (2, 1600)

# 5. Evaluate KDE
Z = kde.evaluate(XY).reshape(X.shape)
print(f"Z shape: {Z.shape}")  # (40, 40)
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
    XY = np.vstack([X.ravel(), Y.ravel()])
    Z = kde.evaluate(XY).reshape(X.shape)
    
    im = ax.imshow(Z, origin='lower', aspect='auto',
                   extent=[-3.5, 3.5, -6, 6], cmap='Blues')
    ax.set_title(f'Resolution: {res}x{res}')
    fig.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

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

# origin='upper' (default)
axes[0].imshow(Z, origin='upper', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')
axes[0].set_title("origin='upper' (default)")
axes[0].scatter(x[::100, 0], x[::100, 1], c='red', s=5, alpha=0.5)

# origin='lower' (correct for KDE)
axes[1].imshow(Z, origin='lower', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')
axes[1].set_title("origin='lower' (correct)")
axes[1].scatter(x[::100, 0], x[::100, 1], c='red', s=5, alpha=0.5)

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

# Without extent (pixel coordinates)
axes[0].imshow(Z, origin='lower', cmap='Blues')
axes[0].set_title('Without extent (pixels)')

# With extent (data coordinates)
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

## KDE Bandwidth

### Adjusting Smoothness

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)

x_ = np.linspace(-3.5, 3.5, 80)
y_ = np.linspace(-6, 6, 80)
X, Y = np.meshgrid(x_, y_)
XY = np.vstack([X.ravel(), Y.ravel()])

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
bw_factors = [0.3, 0.5, 1.0, 2.0]

for ax, bw in zip(axes, bw_factors):
    kde = stats.gaussian_kde(x.T, bw_method=bw)
    Z = kde.evaluate(XY).reshape(X.shape)
    
    im = ax.imshow(Z, origin='lower', aspect='auto',
                   extent=[-3.5, 3.5, -6, 6], cmap='Blues')
    ax.set_title(f'bw_method={bw}')
    fig.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

## Colormaps

### Different Colormaps for Density

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x = np.random.multivariate_normal(mean, cov, 10000)
kde = stats.gaussian_kde(x.T)

x_ = np.linspace(-3.5, 3.5, 80)
y_ = np.linspace(-6, 6, 80)
X, Y = np.meshgrid(x_, y_)
Z = kde.evaluate(np.vstack([X.ravel(), Y.ravel()])).reshape(X.shape)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
cmaps = ['Blues', 'viridis', 'hot', 'YlOrRd', 'magma', 'coolwarm']

for ax, cmap in zip(axes.flat, cmaps):
    im = ax.imshow(Z, origin='lower', aspect='auto',
                   extent=[-3.5, 3.5, -6, 6], cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")
    fig.colorbar(im, ax=ax, shrink=0.8)

plt.tight_layout()
plt.show()
```

## Return Value

### AxesImage Object

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

fig, ax = plt.subplots()
im = ax.imshow(Z, origin='lower', aspect='auto',
               extent=[-3.5, 3.5, -6, 6], cmap='Blues')

print(f"Type: {type(im)}")  # AxesImage
print(f"Array shape: {im.get_array().shape}")

plt.colorbar(im, label='density')
plt.show()
```

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

# Overlay scatter with transparency
ax.scatter(x[::20, 0], x[::20, 1], c='navy', s=3, alpha=0.2)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_title('Kernel Density Estimation', fontsize=14)

cbar = fig.colorbar(im, ax=ax, label='Density')
plt.tight_layout()
plt.show()
```
