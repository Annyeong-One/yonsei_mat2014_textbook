# Quiver Plots


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Quiver plots visualize vector fields using arrows to show direction and magnitude.

## Basic Quiver Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 1)
y = np.arange(0, 5, 1)
X, Y = np.meshgrid(x, y)

U = np.ones_like(X)  # x-component
V = np.ones_like(Y)  # y-component

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_title('Basic Quiver Plot')
plt.show()
```

## Vector Field Example

```python
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Circular field: F = (-y, x)
U = -Y
V = X

fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_aspect('equal')
ax.set_title('Circular Vector Field')
plt.show()
```

## Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `X, Y` | Arrow positions | Required |
| `U, V` | Arrow components | Required |
| `scale` | Arrow length scaling | Auto |
| `width` | Arrow shaft width | 0.005 |
| `headwidth` | Head width | 3 |
| `headlength` | Head length | 5 |
| `color` | Arrow color | 'k' |

## Color by Magnitude

```python
x = np.linspace(-2, 2, 15)
y = np.linspace(-2, 2, 15)
X, Y = np.meshgrid(x, y)

U = -Y
V = X
magnitude = np.sqrt(U**2 + V**2)

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V, magnitude, cmap='viridis')
plt.colorbar(q, label='Magnitude')
ax.set_aspect('equal')
plt.show()
```

## Normalized Arrows (Direction Only)

```python
magnitude = np.sqrt(U**2 + V**2)
U_norm = U / magnitude
V_norm = V / magnitude

fig, ax = plt.subplots()
ax.quiver(X, Y, U_norm, V_norm)
ax.set_aspect('equal')
plt.show()
```

## Add Legend (quiverkey)

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=0.85, Y=1.05, U=2, label='2 units', labelpos='E')
plt.show()
```

## Practical Example: Gradient Field

```python
x = np.linspace(-3, 3, 15)
y = np.linspace(-3, 3, 15)
X, Y = np.meshgrid(x, y)

# Gradient of f(x,y) = x² + y²
U = 2 * X
V = 2 * Y

fig, ax = plt.subplots()

# Contours
contours = ax.contour(X, Y, X**2 + Y**2, levels=10, cmap='coolwarm')
ax.clabel(contours, inline=True, fontsize=8)

# Gradient vectors (normalized)
mag = np.sqrt(U**2 + V**2)
ax.quiver(X, Y, U/mag, V/mag, alpha=0.6)

ax.set_aspect('equal')
ax.set_title('Gradient Field')
plt.show()
```

## Streamplot Alternative

For smoother flow visualization:

```python
fig, ax = plt.subplots()
ax.streamplot(X, Y, U, V, density=1.5, color=magnitude, cmap='viridis')
ax.set_aspect('equal')
ax.set_title('Streamplot')
plt.show()
```

## Common Use Cases

- Fluid flow visualization
- Electric/magnetic fields
- Wind patterns
- Gradient visualization
- Force diagrams
