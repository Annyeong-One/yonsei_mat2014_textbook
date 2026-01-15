# Figure-Axes-Artist

## Composite Pattern

### 1. Hierarchy

```
Figure
  └── Axes
        └── Artists (Line2D, Text, Patch, etc.)
```

### 2. Figure Object

Top-level container:

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
print(type(fig))  # <class 'matplotlib.figure.Figure'>
```

### 3. Axes Object

Plotting region with coordinate system:

```python
fig, ax = plt.subplots()
print(type(ax))  # <class 'matplotlib.axes._axes.Axes'>
```

## Components

### 1. Figure Properties

```python
fig = plt.figure(figsize=(12, 8), dpi=100)
fig.suptitle('Main Title')
fig.tight_layout()
fig.savefig('output.png')
```

### 2. Axes Properties

```python
fig, ax = plt.subplots()
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Axes Title')
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
ax.grid(True)
```

### 3. Artist Objects

```python
line, = ax.plot([0, 1, 2], [0, 1, 0])
print(type(line))  # <class 'matplotlib.lines.Line2D'>
line.set_color('red')
line.set_linewidth(2)
```

## Multiple Axes

### 1. Subplots

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot([1, 2, 3])
ax2.scatter([1, 2, 3], [4, 5, 6])
```

### 2. GridSpec

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, :])  # Top row, all columns
ax2 = fig.add_subplot(gs[1:, 0:2])  # Bottom 2 rows, first 2 cols
ax3 = fig.add_subplot(gs[1:, 2])  # Bottom 2 rows, last col
```

### 3. Nested Axes

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3])

# Inset axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
ax_inset = inset_axes(ax, width="30%", height="30%", loc='upper right')
ax_inset.plot([1, 2, 3], [3, 2, 1])
```
