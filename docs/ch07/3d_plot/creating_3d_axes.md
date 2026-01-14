# Creating 3D Axes

Create 3D plotting axes in Matplotlib using projection parameter.

## Method 1: plt.subplots with subplot_kw

### Basic 3D Subplot

```python
import matplotlib.pyplot as plt

def main():
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    plt.show()

if __name__ == "__main__":
    main()
```

### Multiple 3D Subplots

```python
import matplotlib.pyplot as plt

def main():
    fig, (ax0, ax1) = plt.subplots(1, 2, subplot_kw={'projection': '3d'})
    plt.show()

if __name__ == "__main__":
    main()
```

### Grid of 3D Subplots

```python
import matplotlib.pyplot as plt

def main():
    fig, axes = plt.subplots(2, 2, subplot_kw={'projection': '3d'}, 
                             figsize=(10, 10))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Method 2: fig.add_subplot

### Mixed 2D and 3D

```python
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax0 = fig.add_subplot(1, 2, 1, projection='3d')  # 3D
    ax1 = fig.add_subplot(1, 2, 2)                    # 2D
    plt.show()

if __name__ == "__main__":
    main()
```

### Multiple Mixed Subplots

```python
import matplotlib.pyplot as plt

def main():
    fig = plt.figure(figsize=(12, 8))
    
    # Row 1: 3D plots
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    
    # Row 2: 2D plots
    ax4 = fig.add_subplot(2, 3, 4)
    ax5 = fig.add_subplot(2, 3, 5)
    ax6 = fig.add_subplot(2, 3, 6)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Comparison

### When to Use Each Method

| Method | Use Case |
|--------|----------|
| `plt.subplots(subplot_kw={'projection': '3d'})` | All subplots are 3D |
| `fig.add_subplot(projection='3d')` | Mixed 2D and 3D subplots |

### Example Comparison

```python
import matplotlib.pyplot as plt

# Method 1: All 3D (subplot_kw)
fig1, axes1 = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(10, 4))
fig1.suptitle('Method 1: subplot_kw (all 3D)')

# Method 2: Mixed (add_subplot)
fig2 = plt.figure(figsize=(10, 4))
ax2_3d = fig2.add_subplot(1, 2, 1, projection='3d')
ax2_2d = fig2.add_subplot(1, 2, 2)
fig2.suptitle('Method 2: add_subplot (mixed)')

plt.show()
```

## 3D Axes Properties

### Axes3D Object

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

print(f"Type: {type(ax)}")
print(f"Is 3D: {hasattr(ax, 'zaxis')}")
```

### Available 3D Methods

| Method | Description |
|--------|-------------|
| `ax.plot3D()` | 3D line plot |
| `ax.scatter3D()` | 3D scatter plot |
| `ax.plot_surface()` | Surface plot |
| `ax.plot_wireframe()` | Wireframe plot |
| `ax.contour3D()` | 3D contour plot |
| `ax.bar3d()` | 3D bar chart |

## Basic 3D Plotting

### 3D Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    
    t = np.linspace(0, 10, 100)
    x = np.sin(t)
    y = np.cos(t)
    z = t
    
    ax.plot3D(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Helix')
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 3D Scatter Plot

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    
    n = 100
    x = np.random.randn(n)
    y = np.random.randn(n)
    z = np.random.randn(n)
    
    ax.scatter3D(x, y, z, c=z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Scatter')
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 3D Surface Plot

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Surface')
    
    plt.show()

if __name__ == "__main__":
    main()
```

## View Angle

### Setting View Angle

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': '3d'}, 
                             figsize=(15, 5))
    
    views = [(30, 45), (60, 45), (30, 135)]
    
    for ax, (elev, azim) in zip(axes, views):
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(f'elev={elev}, azim={azim}')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Figure Size

### Adjusting 3D Figure Size

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Single 3D plot with custom size
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'}, figsize=(10, 8))
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    ax.plot_surface(X, Y, Z, cmap='coolwarm')
    ax.set_title('3D Surface Plot')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Practical Example

### Dashboard with 2D and 3D

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig = plt.figure(figsize=(14, 10))
    
    # 3D Surface (top left, spans 2 columns)
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax1.set_title('3D Surface')
    
    # 3D Scatter (top right)
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    n = 100
    xs = np.random.randn(n)
    ys = np.random.randn(n)
    zs = np.random.randn(n)
    ax2.scatter3D(xs, ys, zs, c=zs, cmap='plasma')
    ax2.set_title('3D Scatter')
    
    # 2D Contour (bottom left)
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.contourf(X, Y, Z, levels=20, cmap='viridis')
    ax3.set_title('2D Contour (Top View)')
    ax3.set_aspect('equal')
    
    # 2D Line plot (bottom right)
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(x, np.sin(x), label='sin(x)')
    ax4.plot(x, np.cos(x), label='cos(x)')
    ax4.legend()
    ax4.set_title('2D Line Plot')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```
