# Subplots and Grids

Create multiple plots in a single figure using `plt.subplots()` for organized, comparative visualizations.

## Basic Subplots

Create a grid of axes with `plt.subplots()`.

### 1. Single Row

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, np.sin(x))
axes[0].set_title('Sine')

axes[1].plot(x, np.cos(x))
axes[1].set_title('Cosine')

axes[2].plot(x, np.tan(x))
axes[2].set_ylim(-5, 5)
axes[2].set_title('Tangent')

plt.show()
```

### 2. Single Column

```python
fig, axes = plt.subplots(3, 1, figsize=(6, 10))

axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
axes[2].plot(x, x**2)

plt.show()
```

### 3. Grid Layout

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].plot(x, np.exp(x/10))
axes[1, 1].plot(x, np.log(x + 1))

plt.show()
```

## Axes Indexing

Access individual axes in different grid configurations.

### 1. 1D Array (Single Row or Column)

```python
fig, axes = plt.subplots(1, 3)
# axes is 1D: axes[0], axes[1], axes[2]

fig, axes = plt.subplots(3, 1)
# axes is 1D: axes[0], axes[1], axes[2]
```

### 2. 2D Array (Grid)

```python
fig, axes = plt.subplots(2, 3)
# axes is 2D: axes[row, col]
# axes[0, 0], axes[0, 1], axes[0, 2]
# axes[1, 0], axes[1, 1], axes[1, 2]
```

### 3. Flatten for Iteration

```python
fig, axes = plt.subplots(2, 3)

for ax in axes.flat:
    ax.plot(np.random.randn(50))

plt.show()
```

## Figure Size

Control overall figure dimensions.

### 1. figsize Parameter

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # Width, Height in inches
```

### 2. Aspect Ratio

```python
# Square figure
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

# Wide figure
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

# Tall figure
fig, axes = plt.subplots(4, 1, figsize=(6, 12))
```

### 3. DPI Setting

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=100)
# Total pixels: 800 x 800
```

## Shared Axes

Link axes across subplots for consistent scales.

### 1. Share X-Axis

```python
fig, axes = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
axes[2].plot(x, np.sin(x) * np.cos(x))

# Only bottom subplot shows x-tick labels
plt.show()
```

### 2. Share Y-Axis

```python
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
axes[2].plot(x, np.sin(2*x))

# Only left subplot shows y-tick labels
plt.show()
```

### 3. Share Both

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)

for ax in axes.flat:
    ax.plot(np.random.randn(50).cumsum())

plt.show()
```

## Spacing Control

Adjust space between subplots.

### 1. Default Spacing

```python
fig, axes = plt.subplots(2, 2)
# Default spacing applied
```

### 2. Tight Layout

```python
fig, axes = plt.subplots(2, 2)
for ax in axes.flat:
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
fig.tight_layout()
plt.show()
```

### 3. Constrained Layout

```python
fig, axes = plt.subplots(2, 2, constrained_layout=True)
for ax in axes.flat:
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
plt.show()
```

## Adding Titles

Add titles to figure and subplots.

### 1. Subplot Titles

```python
fig, axes = plt.subplots(2, 2)

axes[0, 0].set_title('Plot A')
axes[0, 1].set_title('Plot B')
axes[1, 0].set_title('Plot C')
axes[1, 1].set_title('Plot D')

plt.show()
```

### 2. Figure Super Title

```python
fig, axes = plt.subplots(2, 2)
fig.suptitle('Main Title', fontsize=16)

fig.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for suptitle
plt.show()
```

### 3. Combined Titles

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Comparison of Functions', fontsize=16, fontweight='bold')

titles = ['Sine', 'Cosine', 'Exponential', 'Logarithm']
for ax, title in zip(axes.flat, titles):
    ax.set_title(title)

fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
```

## Removing Empty Subplots

Handle grids with fewer plots than cells.

### 1. Turn Off Unused Axes

```python
fig, axes = plt.subplots(2, 3)

# Only use 5 subplots
for i, ax in enumerate(axes.flat[:5]):
    ax.plot(np.random.randn(50))

# Turn off the 6th
axes.flat[5].axis('off')

plt.show()
```

### 2. Remove Completely

```python
fig, axes = plt.subplots(2, 3)

for i, ax in enumerate(axes.flat[:5]):
    ax.plot(np.random.randn(50))

fig.delaxes(axes.flat[5])
fig.tight_layout()
plt.show()
```

### 3. Set Visibility

```python
axes.flat[5].set_visible(False)
```

## Practical Example

Create a complete multi-panel figure.

### 1. Setup Figure

```python
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
fig.suptitle('Data Analysis Dashboard', fontsize=16)

x = np.linspace(0, 10, 100)
```

### 2. Populate Subplots

```python
# Row 1
axes[0, 0].plot(x, np.sin(x), 'b-')
axes[0, 0].set_title('Sine Wave')
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Amplitude')

axes[0, 1].hist(np.random.randn(1000), bins=30, color='green', alpha=0.7)
axes[0, 1].set_title('Distribution')

axes[0, 2].scatter(np.random.rand(50), np.random.rand(50), c='red')
axes[0, 2].set_title('Scatter')

# Row 2
axes[1, 0].bar(['A', 'B', 'C', 'D'], [23, 45, 56, 78])
axes[1, 0].set_title('Categories')

axes[1, 1].plot(x, np.cumsum(np.random.randn(100)), 'purple')
axes[1, 1].set_title('Random Walk')

axes[1, 2].imshow(np.random.rand(10, 10), cmap='viridis')
axes[1, 2].set_title('Heatmap')
```

### 3. Finalize Layout

```python
fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
```
