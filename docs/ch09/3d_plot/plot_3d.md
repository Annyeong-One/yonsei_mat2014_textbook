# Axes Method - plot (3D Lines)

The `ax.plot` method on 3D axes creates line plots in three-dimensional space. This is equivalent to `ax.plot3D` - both methods are interchangeable.

## Basic Usage

### 1. Simple 3D Line

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)
z = t

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
```

### 2. plot vs plot3D

Both methods produce identical results:

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})

axes[0].plot(x, y, z, 'blue')
axes[0].set_title('ax.plot')

axes[1].plot3D(x, y, z, 'blue')
axes[1].set_title('ax.plot3D')

plt.tight_layout()
plt.show()
```

### 3. With Color Argument

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'red')
plt.show()
```

---

## Line Styling

### 1. Colors

```python
t = np.linspace(0, 4 * np.pi, 200)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

colors = ['blue', 'green', 'red']

for ax, color in zip(axes, colors):
    ax.plot(np.cos(t), np.sin(t), t, color=color, linewidth=2)
    ax.set_title(f"color='{color}'")

plt.tight_layout()
plt.show()
```

### 2. Line Styles

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

styles = ['-', '--', ':']
titles = ['Solid', 'Dashed', 'Dotted']

for ax, style, title in zip(axes, styles, titles):
    ax.plot(np.cos(t), np.sin(t), t, linestyle=style, linewidth=2)
    ax.set_title(title)

plt.tight_layout()
plt.show()
```

### 3. Line Width

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

widths = [0.5, 2, 4]

for ax, lw in zip(axes, widths):
    ax.plot(np.cos(t), np.sin(t), t, linewidth=lw)
    ax.set_title(f'linewidth={lw}')

plt.tight_layout()
plt.show()
```

### 4. Alpha Transparency

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for offset in range(5):
    ax.plot(np.cos(t), np.sin(t) + offset, t, alpha=0.3 + offset * 0.15)

ax.set_title('Varying Alpha')
plt.show()
```

---

## Multiple Lines

### 1. Multiple Helices

```python
t = np.linspace(0, 4 * np.pi, 200)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot(np.cos(t), np.sin(t), t, 'b-', label='Helix 1')
ax.plot(np.cos(t + np.pi), np.sin(t + np.pi), t, 'r-', label='Helix 2')

ax.legend()
ax.set_title('Double Helix')
plt.show()
```

### 2. Parallel Lines

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for i, color in enumerate(['blue', 'green', 'red', 'purple', 'orange']):
    ax.plot(np.cos(t), np.sin(t), t + i * 5, color=color, label=f'z offset = {i*5}')

ax.legend()
plt.show()
```

### 3. Radial Lines

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    x = np.cos(t + angle)
    y = np.sin(t + angle)
    ax.plot(x, y, t, alpha=0.7)

ax.set_title('Radial Helix Array')
plt.show()
```

---

## Parametric Curves

### 1. Helix

```python
t = np.linspace(0, 6 * np.pi, 500)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(np.cos(t), np.sin(t), t, 'b-', linewidth=1.5)
ax.set_title('Helix: $(\\cos t, \\sin t, t)$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
```

### 2. Conical Helix

```python
t = np.linspace(0, 6 * np.pi, 500)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t * np.cos(t) / 10, t * np.sin(t) / 10, t, 'g-', linewidth=1.5)
ax.set_title('Conical Helix')
plt.show()
```

### 3. Trefoil Knot

```python
t = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(t) + 2 * np.sin(2 * t)
y = np.cos(t) - 2 * np.cos(2 * t)
z = -np.sin(3 * t)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'purple', linewidth=2)
ax.set_title('Trefoil Knot')
plt.show()
```

### 4. Lissajous 3D

```python
t = np.linspace(0, 2 * np.pi, 1000)
x = np.sin(3 * t)
y = np.sin(4 * t)
z = np.sin(5 * t)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'darkorange', linewidth=1.5)
ax.set_title('3D Lissajous Curve')
plt.show()
```

### 5. Parametric Curve Gallery

```python
t = np.linspace(0, 4 * np.pi, 500)

fig, axes = plt.subplots(2, 2, figsize=(12, 10), subplot_kw={'projection': '3d'})

# Helix
axes[0, 0].plot(np.cos(t), np.sin(t), t, 'blue')
axes[0, 0].set_title('Helix')

# Conical Helix
axes[0, 1].plot(t * np.cos(t) / 10, t * np.sin(t) / 10, t, 'green')
axes[0, 1].set_title('Conical Helix')

# Lissajous
t2 = np.linspace(0, 2 * np.pi, 1000)
axes[1, 0].plot(np.sin(3*t2), np.sin(4*t2), np.sin(5*t2), 'orange')
axes[1, 0].set_title('3D Lissajous')

# Trefoil Knot
axes[1, 1].plot(
    np.sin(t2) + 2*np.sin(2*t2),
    np.cos(t2) - 2*np.cos(2*t2),
    -np.sin(3*t2),
    'purple'
)
axes[1, 1].set_title('Trefoil Knot')

plt.tight_layout()
plt.show()
```

---

## Lines on Planes

### 1. XY Plane (z = constant)

```python
t = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(np.cos(t), np.sin(t), np.zeros_like(t), 'b-', linewidth=2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Circle on XY Plane')
plt.show()
```

### 2. Multiple Horizontal Slices

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

for z_level in np.linspace(0, 10, 6):
    ax.plot(np.cos(t), np.sin(t), np.ones_like(t) * z_level, alpha=0.7)

ax.set_title('Circles at Different Heights')
plt.show()
```

### 3. XZ and YZ Planes

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

t = np.linspace(0, 2 * np.pi, 100)

# XY plane
axes[0].plot(np.cos(t), np.sin(t), np.zeros_like(t), 'b-', linewidth=2)
axes[0].set_title('XY Plane (z=0)')

# XZ plane
axes[1].plot(np.cos(t), np.zeros_like(t), np.sin(t), 'g-', linewidth=2)
axes[1].set_title('XZ Plane (y=0)')

# YZ plane
axes[2].plot(np.zeros_like(t), np.cos(t), np.sin(t), 'r-', linewidth=2)
axes[2].set_title('YZ Plane (x=0)')

plt.tight_layout()
plt.show()
```

---

## View Control

### 1. view_init Parameters

```python
t = np.linspace(0, 4 * np.pi, 200)
x, y, z = np.cos(t), np.sin(t), t

fig, axes = plt.subplots(2, 2, figsize=(12, 10), subplot_kw={'projection': '3d'})

views = [(30, -60), (90, 0), (0, 0), (30, 45)]
titles = ['Default', 'Top', 'Side', 'Isometric']

for ax, (elev, azim), title in zip(axes.flat, views, titles):
    ax.plot(x, y, z, 'blue', linewidth=1.5)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(f'{title}\n(elev={elev}°, azim={azim}°)')

plt.tight_layout()
plt.show()
```

### 2. Rotating Views

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw={'projection': '3d'})

azimuths = [0, 60, 120, 180, 240, 300]

for ax, azim in zip(axes.flat, azimuths):
    ax.plot(x, y, z, 'blue', linewidth=1.5)
    ax.view_init(elev=30, azim=azim)
    ax.set_title(f'azim={azim}°')

plt.tight_layout()
plt.show()
```

---

## 3D Axes Customization

### 1. Labels and Title

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'blue', linewidth=2)
ax.set_xlabel('X axis', fontsize=12)
ax.set_ylabel('Y axis', fontsize=12)
ax.set_zlabel('Z axis', fontsize=12)
ax.set_title('3D Helix', fontsize=14)
plt.show()
```

### 2. Custom Ticks

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'blue', linewidth=2)
ax.set_xticks([-1, 0, 1])
ax.set_yticks([-1, 0, 1])
ax.set_zticks([0, 5, 10])
plt.show()
```

### 3. Pane Colors

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(x, y, z, 'blue', linewidth=2)

# White panes
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

ax.set_title('White Background Panes')
plt.show()
```

### 4. Grid Control

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})

axes[0].plot(x, y, z, 'blue', linewidth=2)
axes[0].grid(True)
axes[0].set_title('Grid On')

axes[1].plot(x, y, z, 'blue', linewidth=2)
axes[1].grid(False)
axes[1].set_title('Grid Off')

plt.tight_layout()
plt.show()
```

---

## Combined 2D and 3D

### 1. Mixed Subplots

```python
t = np.linspace(0, 4 * np.pi, 200)

fig = plt.figure(figsize=(14, 5))

# 2D projection
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(np.cos(t), np.sin(t), 'b-')
ax1.set_title('XY Projection')
ax1.set_aspect('equal')
ax1.grid(alpha=0.3)

# Another 2D view
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(t, np.cos(t), 'r-', label='x(t)')
ax2.plot(t, np.sin(t), 'g-', label='y(t)')
ax2.set_title('Components vs Time')
ax2.legend()
ax2.grid(alpha=0.3)

# 3D view
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.plot(np.cos(t), np.sin(t), t, 'purple', linewidth=1.5)
ax3.set_title('3D Helix')

plt.tight_layout()
plt.show()
```

---

## Practical Applications

### 1. Space Curve with Projections

```python
t = np.linspace(0, 4 * np.pi, 300)
x = np.cos(t)
y = np.sin(t)
z = t

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Main curve
ax.plot(x, y, z, 'blue', linewidth=2, label='Space curve')

# Projections
ax.plot(x, y, np.zeros_like(z), 'r--', alpha=0.5, label='XY projection')
ax.plot(x, np.ones_like(y) * y.max() * 1.2, z, 'g--', alpha=0.5, label='XZ projection')
ax.plot(np.ones_like(x) * x.max() * 1.2, y, z, 'm--', alpha=0.5, label='YZ projection')

ax.legend()
ax.set_title('Space Curve with Projections')
plt.show()
```

### 2. Multiple Time Series

```python
np.random.seed(42)
t = np.linspace(0, 10, 200)

fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': '3d'})

n_series = 5
colors = plt.cm.viridis(np.linspace(0, 1, n_series))

for i, color in enumerate(colors):
    y = np.sin(t + i * 0.5) + np.random.randn(len(t)) * 0.1
    ax.plot(t, np.ones_like(t) * i, y, color=color, linewidth=1.5)

ax.set_xlabel('Time')
ax.set_ylabel('Series')
ax.set_zlabel('Value')
ax.set_title('Multiple Time Series')
ax.view_init(20, -50)
plt.show()
```

### 3. Publication-Quality Figure

```python
t = np.linspace(0, 4 * np.pi, 400)
x = np.cos(t)
y = np.sin(t)
z = t / (2 * np.pi)

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

ax.plot(x, y, z, 'steelblue', linewidth=2)

ax.set_xlabel('$x = \\cos(t)$', fontsize=12, labelpad=10)
ax.set_ylabel('$y = \\sin(t)$', fontsize=12, labelpad=10)
ax.set_zlabel('$z = t/2\\pi$', fontsize=12, labelpad=10)
ax.set_title('Helix: $(\\cos t, \\sin t, t/2\\pi)$', fontsize=14, fontweight='bold')

ax.view_init(25, -60)
ax.tick_params(labelsize=10)

ax.w_xaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))
ax.w_yaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))
ax.w_zaxis.set_pane_color((0.98, 0.98, 0.98, 1.0))

plt.tight_layout()
plt.show()
```

---

## Summary

| Feature | Syntax |
|---------|--------|
| Basic plot | `ax.plot(x, y, z)` |
| Color | `ax.plot(x, y, z, color='red')` |
| Line style | `ax.plot(x, y, z, linestyle='--')` |
| Line width | `ax.plot(x, y, z, linewidth=2)` |
| Alpha | `ax.plot(x, y, z, alpha=0.5)` |
| Label | `ax.plot(x, y, z, label='curve')` |
| View angle | `ax.view_init(elev=30, azim=-60)` |
| Pane color | `ax.w_xaxis.set_pane_color((1,1,1,1))` |
