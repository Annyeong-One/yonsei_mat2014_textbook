# Axes Method - pcolormesh

The `pcolormesh` method creates a pseudocolor plot with a non-regular rectangular grid. It is commonly used to visualize 2D scalar fields such as probability density functions, heatmaps, and gridded data.

## Basic Usage

Create pseudocolor plots from meshgrid data.

### 1. Simple pcolormesh

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)
plt.show()
```

### 2. With Colorbar

```python
fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z)
plt.colorbar(img, ax=ax)
plt.show()
```

### 3. With Shading

```python
fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='auto')
plt.colorbar(img, ax=ax)
plt.show()
```

## Standard Normal PDF

Visualize the bivariate standard normal probability density function.

### 1. Basic Normal PDF

```python
def f(X, Y):
    return np.exp(-X**2 / 2 - Y**2 / 2) / (2 * np.pi)

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(figsize=(4 * 1.61803398875, 4))
ax.set_title("Standard Normal PDF")
ax.axis('equal')
ax.axis('off')
img = ax.pcolormesh(X, Y, Z, shading='auto')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. With Axis Labels

```python
fig, ax = plt.subplots(figsize=(8, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Standard Normal PDF: $f(x,y) = \\frac{1}{2\\pi}e^{-(x^2+y^2)/2}$')
plt.colorbar(img, ax=ax, label='Density')
plt.show()
```

### 3. Equal Aspect Ratio

```python
fig, ax = plt.subplots(figsize=(7, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Standard Normal PDF')
plt.colorbar(img, ax=ax)
plt.show()
```

## Shading Options

Control how cell colors are interpolated.

### 1. shading='flat'

```python
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='flat')
ax.set_title("shading='flat'")
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. shading='auto'

```python
fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_title("shading='auto'")
plt.colorbar(img, ax=ax)
plt.show()
```

### 3. shading='gouraud'

```python
fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='gouraud')
ax.set_title("shading='gouraud'")
plt.colorbar(img, ax=ax)
plt.show()
```

### 4. Shading Comparison

```python
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

shadings = ['flat', 'auto', 'gouraud']

for ax, shading in zip(axes, shadings):
    img = ax.pcolormesh(X, Y, Z, shading=shading)
    ax.set_title(f"shading='{shading}'")
    ax.set_aspect('equal')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

## Colormap Options

Apply different colormaps to the visualization.

### 1. Sequential Colormaps

```python
x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

cmaps = ['viridis', 'plasma', 'inferno']

for ax, cmap in zip(axes, cmaps):
    img = ax.pcolormesh(X, Y, Z, shading='auto', cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")
    ax.set_aspect('equal')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

### 2. Diverging Colormaps

```python
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

cmaps = ['coolwarm', 'RdBu', 'seismic']

for ax, cmap in zip(axes, cmaps):
    img = ax.pcolormesh(X, Y, Z, shading='auto', cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")
    ax.set_aspect('equal')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

### 3. Perceptually Uniform

```python
Z = X**2 - Y**2

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

cmaps = ['cividis', 'magma', 'twilight']

for ax, cmap in zip(axes, cmaps):
    img = ax.pcolormesh(X, Y, Z, shading='auto', cmap=cmap)
    ax.set_title(f"cmap='{cmap}'")
    ax.set_aspect('equal')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

## Color Normalization

Control how data values map to colors.

### 1. Default Normalization

```python
x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2)

fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='auto')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. vmin and vmax

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

ranges = [(None, None), (0, 0.5), (0.2, 0.8)]
titles = ['Default', 'vmin=0, vmax=0.5', 'vmin=0.2, vmax=0.8']

for ax, (vmin, vmax), title in zip(axes, ranges, titles):
    img = ax.pcolormesh(X, Y, Z, shading='auto', vmin=vmin, vmax=vmax)
    ax.set_title(title)
    ax.set_aspect('equal')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

### 3. Logarithmic Normalization

```python
from matplotlib.colors import LogNorm

Z_pos = np.abs(Z) + 0.001  # Ensure positive values

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].set_title('Linear Scale')
img0 = axes[0].pcolormesh(X, Y, Z_pos, shading='auto')
axes[0].set_aspect('equal')
plt.colorbar(img0, ax=axes[0])

axes[1].set_title('Log Scale')
img1 = axes[1].pcolormesh(X, Y, Z_pos, shading='auto', norm=LogNorm())
axes[1].set_aspect('equal')
plt.colorbar(img1, ax=axes[1])

plt.tight_layout()
plt.show()
```

### 4. Symmetric Normalization

```python
from matplotlib.colors import TwoSlopeNorm

Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].set_title('Default')
img0 = axes[0].pcolormesh(X, Y, Z, shading='auto', cmap='RdBu')
axes[0].set_aspect('equal')
plt.colorbar(img0, ax=axes[0])

norm = TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
axes[1].set_title('TwoSlopeNorm (centered at 0)')
img1 = axes[1].pcolormesh(X, Y, Z, shading='auto', cmap='RdBu', norm=norm)
axes[1].set_aspect('equal')
plt.colorbar(img1, ax=axes[1])

plt.tight_layout()
plt.show()
```

## pcolormesh vs imshow

Compare the two methods for displaying gridded data.

### 1. imshow (Pixel-Based)

```python
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2)

fig, ax = plt.subplots()
img = ax.imshow(Z, extent=[-3, 3, -3, 3], origin='lower', aspect='equal')
ax.set_title('imshow')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. pcolormesh (Grid-Based)

```python
fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_title('pcolormesh')
ax.set_aspect('equal')
plt.colorbar(img, ax=ax)
plt.show()
```

### 3. Side-by-Side Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

img0 = axes[0].imshow(Z, extent=[-3, 3, -3, 3], origin='lower', aspect='equal')
axes[0].set_title('imshow')
plt.colorbar(img0, ax=axes[0])

img1 = axes[1].pcolormesh(X, Y, Z, shading='auto')
axes[1].set_title('pcolormesh')
axes[1].set_aspect('equal')
plt.colorbar(img1, ax=axes[1])

plt.tight_layout()
plt.show()
```

## Non-Regular Grids

pcolormesh handles non-uniform grids.

### 1. Non-Uniform Spacing

```python
x = np.array([0, 1, 2, 4, 8])
y = np.array([0, 1, 3, 6, 10])
X, Y = np.meshgrid(x, y)
Z = np.random.rand(4, 4)

fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='flat')
ax.set_title('Non-Uniform Grid')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. Polar-Like Grid

```python
r = np.linspace(0, 2, 30)
theta = np.linspace(0, 2 * np.pi, 60)
R, Theta = np.meshgrid(r, theta)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = R

fig, ax = plt.subplots(figsize=(7, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_aspect('equal')
ax.set_title('Polar-Like Grid')
plt.colorbar(img, ax=ax)
plt.show()
```

### 3. Warped Grid

```python
x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)

# Warp the grid
X_warp = X + 0.3 * np.sin(Y * np.pi)
Y_warp = Y + 0.3 * np.sin(X * np.pi)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

img0 = axes[0].pcolormesh(X, Y, Z, shading='auto')
axes[0].set_title('Regular Grid')
axes[0].set_aspect('equal')
plt.colorbar(img0, ax=axes[0])

img1 = axes[1].pcolormesh(X_warp, Y_warp, Z, shading='auto')
axes[1].set_title('Warped Grid')
axes[1].set_aspect('equal')
plt.colorbar(img1, ax=axes[1])

plt.tight_layout()
plt.show()
```

## Mathematical Functions

Visualize various mathematical functions.

### 1. Gaussian

```python
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

Z = np.exp(-(X**2 + Y**2))

fig, ax = plt.subplots(figsize=(7, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='hot')
ax.set_aspect('equal')
ax.set_title('Gaussian: $e^{-(x^2+y^2)}$')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. Saddle Function

```python
Z = X**2 - Y**2

fig, ax = plt.subplots(figsize=(7, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='coolwarm')
ax.set_aspect('equal')
ax.set_title('Saddle: $x^2 - y^2$')
plt.colorbar(img, ax=ax)
plt.show()
```

### 3. Sinusoidal

```python
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots(figsize=(7, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='RdBu')
ax.set_aspect('equal')
ax.set_title('Sinusoidal: $\\sin(x)\\cos(y)$')
plt.colorbar(img, ax=ax)
plt.show()
```

### 4. Function Gallery

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

functions = [
    (np.exp(-(X**2 + Y**2)), 'Gaussian', 'viridis'),
    (X**2 - Y**2, 'Saddle', 'coolwarm'),
    (np.sin(X) * np.cos(Y), 'sin(x)cos(y)', 'RdBu'),
    (np.sin(np.sqrt(X**2 + Y**2)), 'Ripple', 'plasma')
]

for ax, (Z, title, cmap) in zip(axes.flat, functions):
    img = ax.pcolormesh(X, Y, Z, shading='auto', cmap=cmap)
    ax.set_aspect('equal')
    ax.set_title(title)
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

## Edge Colors and Lines

Add edge lines to cells.

### 1. With Edge Colors

```python
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='flat', edgecolors='black', linewidth=0.5)
ax.set_aspect('equal')
ax.set_title('With Edge Colors')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. Edge Color Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

edge_configs = [
    {'edgecolors': 'none', 'linewidth': 0},
    {'edgecolors': 'black', 'linewidth': 0.5},
    {'edgecolors': 'white', 'linewidth': 1}
]
titles = ['No Edges', 'Black Edges', 'White Edges']

for ax, config, title in zip(axes, edge_configs, titles):
    img = ax.pcolormesh(X, Y, Z, shading='flat', **config)
    ax.set_aspect('equal')
    ax.set_title(title)
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

## Colorbar Customization

Configure the colorbar appearance.

### 1. Horizontal Colorbar

```python
x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2) / 2)

fig, ax = plt.subplots()
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_aspect('equal')
plt.colorbar(img, ax=ax, orientation='horizontal', label='Density')
plt.show()
```

### 2. Colorbar with Label

```python
fig, ax = plt.subplots(figsize=(8, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
cbar = plt.colorbar(img, ax=ax)
cbar.set_label('Probability Density', fontsize=12)
plt.show()
```

### 3. Custom Colorbar Ticks

```python
fig, ax = plt.subplots(figsize=(8, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto')
ax.set_aspect('equal')
cbar = plt.colorbar(img, ax=ax, ticks=[0, 0.05, 0.1, 0.15])
cbar.set_ticklabels(['0', '0.05', '0.10', '0.15'])
plt.show()
```

## Full Customization

### 1. Complete Example

```python
def f(X, Y):
    return np.exp(-X**2 / 2 - Y**2 / 2) / (2 * np.pi)

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots(figsize=(4 * 1.61803398875, 4))
ax.set_title("Standard Normal PDF")
ax.axis('equal')
ax.axis('off')
img = ax.pcolormesh(X, Y, Z, shading='auto')
plt.colorbar(img, ax=ax)
plt.show()
```

### 2. Publication-Quality Figure

```python
fig, ax = plt.subplots(figsize=(9, 7))

img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
ax.set_aspect('equal')
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$y$', fontsize=14)
ax.set_title('Standard Bivariate Normal PDF\n$f(x,y) = \\frac{1}{2\\pi}e^{-(x^2+y^2)/2}$', 
             fontsize=14)

cbar = plt.colorbar(img, ax=ax, shrink=0.8)
cbar.set_label('Probability Density', fontsize=12)

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.tick_params(labelsize=11)

plt.tight_layout()
plt.show()
```

## Practical Applications

### 1. Bivariate Normal with Correlation

```python
from scipy import stats

rho = 0.7
mean = [0, 0]
cov = [[1, rho], [rho, 1]]

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

rv = stats.multivariate_normal(mean, cov)
Z = rv.pdf(pos)

fig, ax = plt.subplots(figsize=(8, 6))
img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='Blues')
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Bivariate Normal (ρ = {rho})')
plt.colorbar(img, ax=ax, label='Density')
plt.show()
```

### 2. Correlation Comparison

```python
from scipy import stats

rhos = [-0.8, 0, 0.8]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

x = np.linspace(-3, 3, 80)
y = np.linspace(-3, 3, 80)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

for ax, rho in zip(axes, rhos):
    rv = stats.multivariate_normal([0, 0], [[1, rho], [rho, 1]])
    Z = rv.pdf(pos)
    img = ax.pcolormesh(X, Y, Z, shading='auto', cmap='viridis')
    ax.set_aspect('equal')
    ax.set_title(f'ρ = {rho}')
    plt.colorbar(img, ax=ax)

plt.tight_layout()
plt.show()
```

### 3. Heat Map Dashboard

```python
np.random.seed(42)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Temperature-like data
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)

Z1 = np.sin(X / 2) * np.cos(Y / 2) + np.random.randn(50, 50) * 0.1
img1 = axes[0, 0].pcolormesh(X, Y, Z1, shading='auto', cmap='coolwarm')
axes[0, 0].set_title('Temperature Field')
plt.colorbar(img1, ax=axes[0, 0])

Z2 = np.exp(-((X - 5)**2 + (Y - 5)**2) / 10)
img2 = axes[0, 1].pcolormesh(X, Y, Z2, shading='auto', cmap='hot')
axes[0, 1].set_title('Intensity Map')
plt.colorbar(img2, ax=axes[0, 1])

Z3 = np.random.rand(50, 50)
img3 = axes[1, 0].pcolormesh(X, Y, Z3, shading='auto', cmap='viridis')
axes[1, 0].set_title('Random Field')
plt.colorbar(img3, ax=axes[1, 0])

Z4 = np.sin(np.sqrt(X**2 + Y**2))
img4 = axes[1, 1].pcolormesh(X, Y, Z4, shading='auto', cmap='plasma')
axes[1, 1].set_title('Ripple Pattern')
plt.colorbar(img4, ax=axes[1, 1])

plt.tight_layout()
plt.show()
```
