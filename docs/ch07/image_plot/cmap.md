# Keyword - cmap

The `cmap` parameter specifies the colormap used to map scalar data to colors.

[Official Documentation](https://matplotlib.org/stable/tutorials/colors/colormaps.html)

## Basic Usage

### Applying Colormaps

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(data, cmap='viridis')
axes[0].set_title('viridis')

axes[1].imshow(data, cmap='plasma')
axes[1].set_title('plasma')

axes[2].imshow(data, cmap='gray')
axes[2].set_title('gray')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Colormap Categories

### Perceptually Uniform Sequential

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50)
cmaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, cmap in zip(axes, cmaps):
    ax.imshow(data, cmap=cmap)
    ax.set_title(cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Sequential

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50)
cmaps = ['Greys', 'Blues', 'Greens', 'Oranges', 'Reds']

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, cmap in zip(axes, cmaps):
    ax.imshow(data, cmap=cmap)
    ax.set_title(cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Diverging

```python
import matplotlib.pyplot as plt
import numpy as np

# Diverging data centered at 0
data = np.random.randn(50, 50)
cmaps = ['RdBu', 'RdYlGn', 'coolwarm', 'bwr', 'seismic']

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, cmap in zip(axes, cmaps):
    im = ax.imshow(data, cmap=cmap, vmin=-2, vmax=2)
    ax.set_title(cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Qualitative

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(0, 10, (10, 10))
cmaps = ['Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3']

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, cmap in zip(axes, cmaps):
    ax.imshow(data, cmap=cmap)
    ax.set_title(cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Cyclic

```python
import matplotlib.pyplot as plt
import numpy as np

# Cyclic data (e.g., angles)
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(x, y)
data = np.arctan2(Y, X)

cmaps = ['twilight', 'twilight_shifted', 'hsv']

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, cmap in zip(axes, cmaps):
    ax.imshow(data, cmap=cmap)
    ax.set_title(cmap)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Using plt.cm

### Colormap Object Access

```python
import matplotlib.pyplot as plt
import numpy as np

# Access colormap via plt.cm
cmap = plt.cm.gray
cmap = plt.cm.viridis
cmap = plt.cm.hot

# Use in imshow
data = np.random.rand(50, 50)
fig, ax = plt.subplots()
ax.imshow(data, cmap=plt.cm.gray)
plt.show()
```

## Grayscale Images

### MNIST/FashionMNIST

```python
import matplotlib.pyplot as plt
import numpy as np

# Simulated grayscale digit
digit = np.random.rand(28, 28)

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

axes[0].imshow(digit, cmap='gray')
axes[0].set_title('gray')

axes[1].imshow(digit, cmap='binary')
axes[1].set_title('binary')

axes[2].imshow(digit, cmap='gray_r')
axes[2].set_title('gray_r (reversed)')

axes[3].imshow(digit, cmap='binary_r')
axes[3].set_title('binary_r')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Reversed Colormaps

### Adding _r Suffix

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50)

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

cmaps = ['viridis', 'hot', 'Blues']
for i, cmap in enumerate(cmaps):
    axes[0, i].imshow(data, cmap=cmap)
    axes[0, i].set_title(cmap)
    axes[0, i].axis('off')
    
    axes[1, i].imshow(data, cmap=cmap + '_r')
    axes[1, i].set_title(cmap + '_r')
    axes[1, i].axis('off')

plt.tight_layout()
plt.show()
```

## Value Range Control

### vmin and vmax

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50) * 100  # Range 0-100

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Default range
axes[0].imshow(data, cmap='viridis')
axes[0].set_title('Default range')

# Custom range
axes[1].imshow(data, cmap='viridis', vmin=25, vmax=75)
axes[1].set_title('vmin=25, vmax=75')

# Clipped range
axes[2].imshow(data, cmap='viridis', vmin=0, vmax=50)
axes[2].set_title('vmin=0, vmax=50')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Colorbar

### Adding Colorbar

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50)

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='viridis')
fig.colorbar(im, ax=ax, label='Value')
ax.set_title('Image with Colorbar')
plt.show()
```

### Multiple Subplots with Colorbars

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(50, 50)
cmaps = ['viridis', 'plasma', 'inferno']

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, cmap in zip(axes, cmaps):
    im = ax.imshow(data, cmap=cmap)
    fig.colorbar(im, ax=ax, shrink=0.8)
    ax.set_title(cmap)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Common Use Cases

### Scientific Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

# Heatmap data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Temperature-like
axes[0].imshow(Z, cmap='coolwarm', extent=[-3, 3, -3, 3])
axes[0].set_title('coolwarm (diverging)')

# Intensity
axes[1].imshow(Z**2, cmap='hot', extent=[-3, 3, -3, 3])
axes[1].set_title('hot (sequential)')

# Terrain
axes[2].imshow(Z, cmap='terrain', extent=[-3, 3, -3, 3])
axes[2].set_title('terrain')

plt.tight_layout()
plt.show()
```

## Complete Colormap Reference

### All Built-in Colormaps

```python
import matplotlib.pyplot as plt
import numpy as np

cmaps_list = {
    'Perceptually Uniform': ['viridis', 'plasma', 'inferno', 'magma', 'cividis'],
    'Sequential': ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds'],
    'Diverging': ['PiYG', 'PRGn', 'BrBG', 'RdBu', 'coolwarm', 'bwr'],
    'Cyclic': ['twilight', 'twilight_shifted', 'hsv'],
}

gradient = np.linspace(0, 1, 256).reshape(1, -1)

fig, axes = plt.subplots(len(cmaps_list), 1, figsize=(12, 8))

for ax, (category, cmaps) in zip(axes, cmaps_list.items()):
    ax.set_title(category, loc='left', fontweight='bold')
    # Create combined gradient
    combined = np.vstack([gradient] * len(cmaps))
    ax.imshow(combined, aspect='auto', 
              cmap=plt.cm.get_cmap(cmaps[0]))
    ax.set_yticks(range(len(cmaps)))
    ax.set_yticklabels(cmaps)
    ax.set_xticks([])

plt.tight_layout()
plt.show()
```
