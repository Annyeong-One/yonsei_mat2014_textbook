# Styling and Colors

Customize box plot appearance through color schemes, line styles, and component-specific properties.

## Box Colors

Use `patch_artist=True` to enable box filling with colors.

### 1. Single Color

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

fig, ax = plt.subplots()
bp = ax.boxplot(data, patch_artist=True)

for patch in bp['boxes']:
    patch.set_facecolor('lightblue')

plt.show()
```

### 2. Multiple Colors

```python
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink']

bp = ax.boxplot(data, patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
```

### 3. Colormap Colors

```python
import matplotlib.cm as cm

cmap = cm.get_cmap('viridis')
colors = [cmap(i / len(data)) for i in range(len(data))]

bp = ax.boxplot(data, patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
```

## Component Properties

Each box plot component can be styled individually using property dictionaries.

### 1. Box Properties

```python
boxprops = dict(facecolor='lightblue', edgecolor='navy', linewidth=2)
ax.boxplot(data, patch_artist=True, boxprops=boxprops)
```

### 2. Whisker Properties

```python
whiskerprops = dict(color='gray', linewidth=1.5, linestyle='--')
ax.boxplot(data, whiskerprops=whiskerprops)
```

### 3. Cap Properties

```python
capprops = dict(color='black', linewidth=2)
ax.boxplot(data, capprops=capprops)
```

## Median Styling

Customize the median line appearance.

### 1. Color and Width

```python
medianprops = dict(color='red', linewidth=2)
ax.boxplot(data, medianprops=medianprops)
```

### 2. Line Style

```python
medianprops = dict(color='darkred', linewidth=2, linestyle='-')
ax.boxplot(data, medianprops=medianprops)
```

### 3. Full Example

```python
fig, ax = plt.subplots()
bp = ax.boxplot(data, 
                patch_artist=True,
                medianprops=dict(color='white', linewidth=2))

for patch in bp['boxes']:
    patch.set_facecolor('steelblue')

plt.show()
```

## Mean Marker Styling

Customize the mean indicator appearance.

### 1. Mean Properties

```python
meanprops = dict(marker='D', 
                 markerfacecolor='red', 
                 markeredgecolor='darkred',
                 markersize=8)

ax.boxplot(data, showmeans=True, meanprops=meanprops)
```

### 2. Mean as Line

```python
meanprops = dict(color='green', linewidth=2, linestyle='--')
ax.boxplot(data, showmeans=True, meanline=True, meanprops=meanprops)
```

### 3. Diamond vs Triangle

```python
# Diamond marker
meanprops = dict(marker='D', markerfacecolor='red')

# Triangle marker
meanprops = dict(marker='^', markerfacecolor='green')
```

## Outlier Styling

Customize flier (outlier) point appearance.

### 1. Basic Flier Properties

```python
flierprops = dict(marker='o',
                  markerfacecolor='red',
                  markersize=8,
                  markeredgecolor='darkred')

ax.boxplot(data, flierprops=flierprops)
```

### 2. Different Marker Shapes

```python
# Circle
flierprops = dict(marker='o', markerfacecolor='red')

# Star
flierprops = dict(marker='*', markerfacecolor='gold', markersize=10)

# Diamond
flierprops = dict(marker='D', markerfacecolor='purple')
```

### 3. Transparent Outliers

```python
flierprops = dict(marker='o', 
                  markerfacecolor='none',
                  markeredgecolor='gray',
                  alpha=0.5)
```

## Complete Styled Example

Combine all styling options for a polished visualization.

### 1. Professional Style

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

fig, ax = plt.subplots(figsize=(8, 5))

bp = ax.boxplot(data,
                patch_artist=True,
                notch=True,
                widths=0.6,
                boxprops=dict(facecolor='steelblue', edgecolor='navy'),
                whiskerprops=dict(color='navy', linewidth=1.5),
                capprops=dict(color='navy', linewidth=1.5),
                medianprops=dict(color='white', linewidth=2),
                flierprops=dict(marker='o', markerfacecolor='coral', 
                               markeredgecolor='darkred', markersize=6))

ax.set_xticklabels([r'$\sigma=1$', r'$\sigma=2$', r'$\sigma=3$', r'$\sigma=4$'])
ax.set_ylabel('Value')
ax.set_title('Customized Box Plot')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

### 2. Return Value Dictionary

```python
# bp dictionary contains all artists
print(bp.keys())
# dict_keys(['whiskers', 'caps', 'boxes', 'medians', 'fliers', 'means'])
```

### 3. Post-Creation Modification

```python
bp = ax.boxplot(data, patch_artist=True)

# Modify after creation
bp['boxes'][0].set_facecolor('red')
bp['medians'][0].set_color('white')
bp['whiskers'][0].set_linestyle('--')
```
