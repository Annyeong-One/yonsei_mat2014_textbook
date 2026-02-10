# GridSpec

GridSpec provides fine-grained control over subplot layout, enabling complex arrangements with varying cell sizes and spans.

## Basic GridSpec

Create a grid and add subplots to each cell.

### 1. Import GridSpec

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
```

### 2. Create Grid

```python
x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()
gs = gridspec.GridSpec(2, 3)  # 2 rows, 3 columns
```

### 3. Add Subplots

```python
for i, g in enumerate(gs):
    ax = fig.add_subplot(g)
    if i % 2 == 0:
        ax.plot(x, y1)
    else:
        ax.plot(x, y2)

fig.tight_layout()
plt.show()
```

## Size Ratios

Control relative sizes of rows and columns.

### 1. Height Ratios

```python
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, height_ratios=[2, 1])  # Top row twice as tall

for i, g in enumerate(gs):
    ax = fig.add_subplot(g)
    ax.set_title(f'Cell {i}')

fig.tight_layout()
plt.show()
```

### 2. Width Ratios

```python
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, width_ratios=[1, 2, 1])  # Middle column wider

for i, g in enumerate(gs):
    ax = fig.add_subplot(g)

fig.tight_layout()
plt.show()
```

### 3. Combined Ratios

```python
fig = plt.figure()
gs = gridspec.GridSpec(2, 3, 
                       height_ratios=[2, 1], 
                       width_ratios=[1, 2, 1])

for i, g in enumerate(gs):
    ax = fig.add_subplot(g)
    ax.set_title(f'Cell {i}')

fig.tight_layout()
plt.show()
```

## Spanning Cells

Use slicing to span multiple rows or columns.

### 1. Span Columns

```python
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(3, 3)

# Full top row
ax1 = fig.add_subplot(gs[0, :])  # Row 0, all columns
ax1.set_title('Top Row (spans all columns)')

fig.tight_layout()
plt.show()
```

### 2. Span Rows

```python
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(3, 3)

# Left column, rows 1-2
ax2 = fig.add_subplot(gs[1:, 0])  # Rows 1-2, column 0
ax2.set_title('Left (spans 2 rows)')

fig.tight_layout()
plt.show()
```

### 3. Span Block

```python
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(3, 3)

ax1 = fig.add_subplot(gs[0, :])
ax1.set_title('Top Row')

ax2 = fig.add_subplot(gs[1:, 0])
ax2.set_title('Left Column')

ax3 = fig.add_subplot(gs[1:, 1:])  # 2x2 block
ax3.set_title('Right Block (2x2)')

x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
ax3.plot(x, np.tan(x))
ax3.set_ylim(-5, 5)

fig.tight_layout()
plt.show()
```

## Complex Layouts

Create sophisticated multi-panel figures.

### 1. Dashboard Layout

```python
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(4, 4)

# Main plot: upper-left 3x3
ax_main = fig.add_subplot(gs[:3, :3])
ax_main.set_title('Main Plot')

# Right sidebar: 3 small plots
ax_right1 = fig.add_subplot(gs[0, 3])
ax_right2 = fig.add_subplot(gs[1, 3])
ax_right3 = fig.add_subplot(gs[2, 3])

# Bottom bar: full width
ax_bottom = fig.add_subplot(gs[3, :])
ax_bottom.set_title('Timeline')
```

### 2. Add Data

```python
x = np.linspace(0, 10, 100)
ax_main.plot(x, np.sin(x), 'b-', linewidth=2)
ax_main.set_xlabel('x')
ax_main.set_ylabel('y')

ax_right1.hist(np.random.randn(100), bins=20)
ax_right2.hist(np.random.randn(100), bins=20)
ax_right3.hist(np.random.randn(100), bins=20)

ax_bottom.plot(x, np.random.randn(100).cumsum())

fig.tight_layout()
plt.show()
```

### 3. Scientific Figure Layout

```python
fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[3, 1], width_ratios=[2, 1])

ax_main = fig.add_subplot(gs[0, 0])
ax_hist = fig.add_subplot(gs[0, 1])
ax_resid = fig.add_subplot(gs[1, 0])
ax_stats = fig.add_subplot(gs[1, 1])

fig.tight_layout()
plt.show()
```

## Nested GridSpec

Create grids within grids for hierarchical layouts.

### 1. Outer Grid

```python
fig = plt.figure(figsize=(12, 6))
outer_gs = gridspec.GridSpec(1, 2, figure=fig)

ax_left = fig.add_subplot(outer_gs[0])
ax_left.set_title('Left Panel')
```

### 2. Inner Grid

```python
inner_gs = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer_gs[1])

ax1 = fig.add_subplot(inner_gs[0, 0])
ax2 = fig.add_subplot(inner_gs[0, 1])
ax3 = fig.add_subplot(inner_gs[1, 0])
ax4 = fig.add_subplot(inner_gs[1, 1])
```

### 3. Complete Example

```python
fig = plt.figure(figsize=(12, 6))
outer_gs = gridspec.GridSpec(1, 2, figure=fig)

ax_left = fig.add_subplot(outer_gs[0])
ax_left.set_title('Left Panel')

inner_gs = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=outer_gs[1])
ax1 = fig.add_subplot(inner_gs[0, 0])
ax2 = fig.add_subplot(inner_gs[0, 1])
ax3 = fig.add_subplot(inner_gs[1, 0])
ax4 = fig.add_subplot(inner_gs[1, 1])

x = np.linspace(0, 5, 50)
ax_left.plot(x, x**2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
ax3.plot(x, np.exp(x/5))
ax4.plot(x, np.log(x + 1))

fig.tight_layout()
plt.show()
```

## GridSpec Parameters

Configure spacing and position.

### 1. Spacing Parameters

```python
gs = gridspec.GridSpec(2, 3,
                       wspace=0.3,   # Width space between subplots
                       hspace=0.3)   # Height space between subplots
```

### 2. Position Parameters

```python
gs = gridspec.GridSpec(2, 3,
                       left=0.1,     # Left edge position
                       right=0.9,    # Right edge position
                       bottom=0.1,   # Bottom edge position
                       top=0.9)      # Top edge position
```

### 3. Full Parameter List

```python
gs = gridspec.GridSpec(
    nrows=2,                    # Number of rows
    ncols=3,                    # Number of columns
    figure=fig,                 # Figure to attach to
    left=0.1,
    right=0.9,
    bottom=0.1,
    top=0.9,
    wspace=0.2,
    hspace=0.2,
    width_ratios=[1, 2, 1],
    height_ratios=[2, 1]
)
```
