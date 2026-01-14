# Axes Method - plot3D

The `plot3D` method creates 3D line plots. There is no difference between `ax.plot` and `ax.plot3D` when used on 3D axes - they are functionally equivalent.

## Basic Usage

Create 3D line plots with x, y, z coordinates.

### 1. Simple 3D Line

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t)
y = np.cos(t)
z = t

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(x, y, z)
plt.show()
```

### 2. Using ax.plot (Equivalent)

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z)
plt.show()
```

### 3. With Color

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(x, y, z, color='red')
plt.show()
```

## plot vs plot3D Equivalence

Both methods produce identical results on 3D axes.

### 1. Side-by-Side Comparison

```python
t = np.linspace(0, 4 * np.pi, 200)
x = np.sin(t)
y = np.cos(t)
z = t

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})

ax1.plot(x, y, z, color='blue')
ax1.set_title('ax.plot')

ax2.plot3D(x, y, z, color='blue')
ax2.set_title('ax.plot3D')

plt.tight_layout()
plt.show()
```

## Line Styles and Colors

Apply standard line styling to 3D plots.

### 1. Line Styles

```python
t = np.linspace(0, 2 * np.pi, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

styles = ['-', '--', ':']
titles = ['Solid', 'Dashed', 'Dotted']

for ax, style, title in zip(axes, styles, titles):
    ax.plot3D(np.sin(t), np.cos(t), t, linestyle=style)
    ax.set_title(title)

plt.tight_layout()
plt.show()
```

### 2. Colors

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

colors = ['red', 'green', 'blue']

for ax, color in zip(axes, colors):
    ax.plot3D(np.sin(t), np.cos(t), t, color=color)
    ax.set_title(f"color='{color}'")

plt.tight_layout()
plt.show()
```

### 3. Line Width

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

widths = [0.5, 2, 4]

for ax, lw in zip(axes, widths):
    ax.plot3D(np.sin(t), np.cos(t), t, linewidth=lw)
    ax.set_title(f'linewidth={lw}')

plt.tight_layout()
plt.show()
```

## Multiple Lines

Plot multiple 3D lines on the same axes.

### 1. Multiple Helices

```python
t = np.linspace(0, 4 * np.pi, 200)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot3D(np.sin(t), np.cos(t), t, color='blue', label='Helix 1')
ax.plot3D(np.sin(t + np.pi), np.cos(t + np.pi), t, color='red', label='Helix 2')

ax.legend()
plt.show()
```

### 2. Parallel Lines

```python
t = np.linspace(0, 10, 100)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for offset in range(5):
    ax.plot3D(t, np.sin(t) + offset * 2, np.zeros_like(t), label=f'y offset={offset * 2}')

ax.legend()
plt.show()
```

## Lines on Planes

Plot lines constrained to specific planes.

### 1. Lines on XY Plane (z=0)

```python
t = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.cos(t), np.sin(t), np.zeros_like(t), color='blue')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

### 2. Lines on XZ Plane (y=0)

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(t, np.zeros_like(t), np.sin(t), color='red')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

### 3. Lines on YZ Plane (x=0)

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.zeros_like(t), np.cos(t), np.sin(t), color='green')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

## Geometric Brownian Motion

Visualize stochastic processes in 3D with probability densities.

### 1. Path Generation Function

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def generate_X_and_S(num_paths, num_steps, T, r, sigma, S0):
    """
    dX = (r - 0.5 * sigma**2) * dt + sigma * dB
    S = exp(X)
    """
    Z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    X = np.ones((num_paths, num_steps + 1)) * np.log(S0)
    t = np.linspace(0, T, num_steps + 1)

    dt = t[1] - t[0]
    sqrt_dt = np.sqrt(dt)
    for i in range(num_steps):
        if num_paths > 1:
            Z[:, i] = (Z[:, i] - Z[:, i].mean()) / Z[:, i].std()
        X[:, i + 1] = X[:, i] + (r - 0.5 * sigma**2) * dt + sigma * sqrt_dt * Z[:, i]

    S = np.exp(X)
    return t, X, S
```

### 2. Log Process X(t)

```python
num_paths = 25
num_steps = 500
T = 1
r = 0.05
sigma = 0.4
S0 = 100

t, X, S = generate_X_and_S(num_paths, num_steps, T, r, sigma, S0)

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Plot paths
for i in range(num_paths):
    ax.plot3D(t, X[i], np.zeros_like(t), color='blue', alpha=0.5)

ax.set_xlabel('t')
ax.set_ylabel('X(t)')
ax.set_zlabel('density')
ax.set_title('Log Process X(t)')
plt.show()
```

### 3. Price Process S(t)

```python
fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Plot paths
for i in range(num_paths):
    ax.plot3D(t, S[i], np.zeros_like(t), color='blue', alpha=0.5)

ax.set_xlabel('t')
ax.set_ylabel('S(t)')
ax.set_zlabel('density')
ax.set_title('Price Process S(t)')
plt.show()
```

### 4. Complete Visualization with Densities

```python
num_paths = 25
num_steps = 500
T = 1
r = 0.05
sigma = 0.4
S0 = 100

t, X, S = generate_X_and_S(num_paths, num_steps, T, r, sigma, S0)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': '3d'})

# Plot paths
for i in range(num_paths):
    ax0.plot(t, X[i], np.zeros_like(t), color='blue', alpha=0.5)
    ax1.plot(t, S[i], np.zeros_like(t), color='blue', alpha=0.5)

# Plot densities for X(T)
Ti = np.linspace(0, T, 5)[1:]

pdf_norm = lambda x, ti: stats.norm.pdf(x, np.log(S0) + (r - 0.5 * sigma**2) * ti, np.sqrt(ti) * sigma)
y = np.linspace(3, 6, 100)
for ti in Ti:
    x = np.ones_like(y) * ti
    z = pdf_norm(y, ti)
    ax0.plot(x, y, z, 'red')

# Plot densities for S(T)
pdf_lognorm = lambda x, ti: stats.lognorm.pdf(
    x,
    scale=np.exp(np.log(S0) + (r - 0.5 * sigma**2) * ti),
    s=np.sqrt(ti) * sigma
)
y = np.linspace(0, 200, 100)
for ti in Ti:
    x = np.ones_like(y) * ti
    z = pdf_lognorm(y, ti)
    ax1.plot(x, y, z, 'red')

# Configure axes
ylabels = ("X(t)", "S(t)")
yticks = ([3, 4, 5, 6], [0, 50, 100, 150, 200])
zticks = ([0, 0.5, 1, 1.5, 2], [0, 0.005, 0.01, 0.015, 0.02, 0.025])

for ax, ylabel, ytick, ztick in zip((ax0, ax1), ylabels, yticks, zticks):
    ax.grid()
    ax.set_xlabel("t")
    ax.set_ylabel(ylabel)
    ax.set_zlabel('density', rotation=90)
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks(ytick)
    ax.set_zticks(ztick)
    ax.zaxis.set_rotate_label(False)
    ax.view_init(30, -150)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

plt.tight_layout()
plt.show()
```

## 3D Axes Customization

Configure axis labels, ticks, and appearance.

### 1. Axis Labels

```python
t = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.sin(t), np.cos(t), t)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
```

### 2. Custom Ticks

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.sin(t), np.cos(t), t)
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])
ax.set_zticks([0, np.pi, 2 * np.pi])
plt.show()
```

### 3. Z-Label Rotation

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.sin(t), np.cos(t), t)
ax.set_zlabel('Height', rotation=90)
ax.zaxis.set_rotate_label(False)  # Disable automatic rotation
plt.show()
```

### 4. Pane Colors

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.sin(t), np.cos(t), t)

# Set white background panes
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

plt.show()
```

### 5. Colored Panes

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.sin(t), np.cos(t), t)

ax.w_xaxis.set_pane_color((1.0, 0.9, 0.9, 0.5))  # Light red
ax.w_yaxis.set_pane_color((0.9, 1.0, 0.9, 0.5))  # Light green
ax.w_zaxis.set_pane_color((0.9, 0.9, 1.0, 0.5))  # Light blue

plt.show()
```

## Combined with view_init

Control viewing angle for 3D line plots.

### 1. Different Angles

```python
t = np.linspace(0, 4 * np.pi, 200)
x, y, z = np.sin(t), np.cos(t), t

fig, axes = plt.subplots(2, 2, figsize=(12, 10), subplot_kw={'projection': '3d'})

views = [(30, -60), (90, 0), (0, 0), (30, 45)]
titles = ['Default', 'Top', 'Side', 'Isometric']

for ax, (elev, azim), title in zip(axes.flat, views, titles):
    ax.plot3D(x, y, z, color='blue')
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(f'{title} (elev={elev}, azim={azim})')

plt.tight_layout()
plt.show()
```

## Parametric Curves

Create various 3D parametric curves.

### 1. Helix

```python
t = np.linspace(0, 6 * np.pi, 300)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(np.cos(t), np.sin(t), t, color='blue')
ax.set_title('Helix')
plt.show()
```

### 2. Conical Helix

```python
t = np.linspace(0, 6 * np.pi, 300)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(t * np.cos(t), t * np.sin(t), t, color='green')
ax.set_title('Conical Helix')
plt.show()
```

### 3. Trefoil Knot

```python
t = np.linspace(0, 2 * np.pi, 500)
x = np.sin(t) + 2 * np.sin(2 * t)
y = np.cos(t) - 2 * np.cos(2 * t)
z = -np.sin(3 * t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot3D(x, y, z, color='purple', linewidth=2)
ax.set_title('Trefoil Knot')
plt.show()
```

### 4. Curve Gallery

```python
t = np.linspace(0, 4 * np.pi, 300)

fig, axes = plt.subplots(2, 2, figsize=(12, 10), subplot_kw={'projection': '3d'})

# Helix
axes[0, 0].plot3D(np.cos(t), np.sin(t), t)
axes[0, 0].set_title('Helix')

# Conical Helix
axes[0, 1].plot3D(t * np.cos(t) / 10, t * np.sin(t) / 10, t)
axes[0, 1].set_title('Conical Helix')

# Lissajous 3D
axes[1, 0].plot3D(np.sin(2 * t), np.sin(3 * t), np.sin(5 * t))
axes[1, 0].set_title('3D Lissajous')

# Trefoil Knot
t_knot = np.linspace(0, 2 * np.pi, 500)
axes[1, 1].plot3D(
    np.sin(t_knot) + 2 * np.sin(2 * t_knot),
    np.cos(t_knot) - 2 * np.cos(2 * t_knot),
    -np.sin(3 * t_knot)
)
axes[1, 1].set_title('Trefoil Knot')

plt.tight_layout()
plt.show()
```

## Practical Applications

### 1. Time Series with Distribution

```python
np.random.seed(42)
n_series = 20
n_points = 200

t = np.linspace(0, 10, n_points)

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Plot random walks
for i in range(n_series):
    y = np.cumsum(np.random.randn(n_points)) * 0.1
    ax.plot3D(t, y, np.zeros_like(t), color='blue', alpha=0.4)

# Plot distribution at end
y_final = np.linspace(-5, 5, 100)
z_dist = stats.norm.pdf(y_final, 0, 1.5)
ax.plot3D(np.ones_like(y_final) * 10, y_final, z_dist, color='red', linewidth=2)

ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_zlabel('Density')
ax.view_init(25, -60)
plt.show()
```

### 2. Multi-Asset Paths

```python
np.random.seed(42)
n_assets = 3
n_paths = 10
n_steps = 200

t = np.linspace(0, 1, n_steps)
colors = ['blue', 'green', 'red']

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': '3d'})

for asset in range(n_assets):
    for path in range(n_paths):
        y = 100 * np.exp(np.cumsum(np.random.randn(n_steps) * 0.02))
        ax.plot3D(t, y, np.ones_like(t) * asset, color=colors[asset], alpha=0.5)

ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_zlabel('Asset')
ax.set_zticks([0, 1, 2])
ax.set_zticklabels(['Asset A', 'Asset B', 'Asset C'])
ax.view_init(20, -50)
plt.tight_layout()
plt.show()
```

### 3. Publication-Quality Figure

```python
num_paths = 25
num_steps = 500
T = 1
r = 0.05
sigma = 0.4
S0 = 100

t, X, S = generate_X_and_S(num_paths, num_steps, T, r, sigma, S0)

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Plot paths
for i in range(num_paths):
    ax.plot3D(t, S[i], np.zeros_like(t), color='steelblue', alpha=0.4, linewidth=0.8)

# Plot densities
Ti = [0.25, 0.5, 0.75, 1.0]
y = np.linspace(0, 250, 150)

for ti in Ti:
    pdf = stats.lognorm.pdf(
        y,
        scale=np.exp(np.log(S0) + (r - 0.5 * sigma**2) * ti),
        s=np.sqrt(ti) * sigma
    )
    ax.plot3D(np.ones_like(y) * ti, y, pdf, color='darkred', linewidth=1.5)

ax.set_xlabel('Time (years)', fontsize=11)
ax.set_ylabel('Stock Price ($)', fontsize=11)
ax.set_zlabel('Density', fontsize=11)
ax.set_title('Geometric Brownian Motion with Lognormal Densities', fontsize=13, fontweight='bold')

ax.view_init(25, -140)
ax.w_xaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))
ax.w_yaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))
ax.w_zaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```
