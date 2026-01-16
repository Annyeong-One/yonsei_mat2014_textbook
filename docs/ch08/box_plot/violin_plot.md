# Violin Plot

Violin plots combine box plot statistics with kernel density estimation, showing the full distribution shape of data.

## Basic Violin Plot

### Simple Example

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

fig, ax = plt.subplots()
ax.violinplot(data)
ax.set_xlabel('Dataset')
ax.set_ylabel('Value')
ax.set_title('Basic Violin Plot')
plt.show()
```

### With Custom Positions

```python
fig, ax = plt.subplots()
positions = [1, 2, 4, 5]  # Custom x positions
ax.violinplot(data, positions=positions)
ax.set_xticks(positions)
ax.set_xticklabels(['A', 'B', 'C', 'D'])
plt.show()
```

## Anatomy of a Violin Plot

```
    ___
   /   \     ← Kernel density estimate (distribution shape)
  |     |
  |  ─  |    ← Median (if showmedians=True)
  |  │  |    ← Interquartile range
  |  ─  |    ← Q1 and Q3 markers
   \___/
     │       ← Extrema lines (min/max)
```

## Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `dataset` | Data to plot | Required |
| `positions` | X positions | [1, 2, ...] |
| `widths` | Width of violins | 0.5 |
| `showmeans` | Show mean line | False |
| `showmedians` | Show median line | False |
| `showextrema` | Show min/max lines | True |
| `quantiles` | Quantile lines | None |
| `vert` | Vertical orientation | True |

## Displaying Statistics

### Show Median and Mean

```python
fig, ax = plt.subplots()
ax.violinplot(data, showmeans=True, showmedians=True)
plt.show()
```

### Show Quantiles

```python
fig, ax = plt.subplots()
# Show 25th, 50th, and 75th percentiles
ax.violinplot(data, quantiles=[[0.25, 0.5, 0.75]] * len(data))
plt.show()
```

### Hide Extrema

```python
fig, ax = plt.subplots()
ax.violinplot(data, showextrema=False, showmedians=True)
plt.show()
```

## Styling Violin Plots

### Accessing Violin Components

```python
fig, ax = plt.subplots()
parts = ax.violinplot(data, showmedians=True)

# 'parts' is a dictionary with keys:
# 'bodies': list of PolyCollection (violin shapes)
# 'cmeans': LineCollection (mean lines, if shown)
# 'cmedians': LineCollection (median lines, if shown)
# 'cbars': LineCollection (center bars)
# 'cmins': LineCollection (min lines)
# 'cmaxes': LineCollection (max lines)
```

### Custom Colors

```python
fig, ax = plt.subplots()
parts = ax.violinplot(data, showmedians=True)

# Color the violin bodies
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
for i, body in enumerate(parts['bodies']):
    body.set_facecolor(colors[i])
    body.set_edgecolor('black')
    body.set_alpha(0.7)

# Color the median lines
parts['cmedians'].set_color('red')
parts['cmedians'].set_linewidth(2)

plt.show()
```

### Consistent Styling Function

```python
def style_violins(parts, body_color='lightblue', edge_color='black', 
                  median_color='red', alpha=0.7):
    """Apply consistent styling to violin plot parts."""
    for body in parts['bodies']:
        body.set_facecolor(body_color)
        body.set_edgecolor(edge_color)
        body.set_alpha(alpha)
    
    if 'cmedians' in parts:
        parts['cmedians'].set_color(median_color)
        parts['cmedians'].set_linewidth(2)
    
    for key in ['cbars', 'cmins', 'cmaxes']:
        if key in parts:
            parts[key].set_color(edge_color)
```

## Horizontal Violin Plots

```python
fig, ax = plt.subplots()
ax.violinplot(data, vert=False, showmedians=True)
ax.set_ylabel('Dataset')
ax.set_xlabel('Value')
plt.show()
```

## Practical Examples

### 1. Comparing Distributions

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Different distributions
normal = np.random.normal(0, 1, 200)
uniform = np.random.uniform(-2, 2, 200)
bimodal = np.concatenate([np.random.normal(-1, 0.5, 100),
                          np.random.normal(1, 0.5, 100)])
skewed = np.random.exponential(1, 200) - 1

data = [normal, uniform, bimodal, skewed]
labels = ['Normal', 'Uniform', 'Bimodal', 'Skewed']

fig, ax = plt.subplots(figsize=(10, 6))
parts = ax.violinplot(data, showmedians=True)

# Style
for body in parts['bodies']:
    body.set_facecolor('steelblue')
    body.set_alpha(0.6)

ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(labels)
ax.set_ylabel('Value')
ax.set_title('Comparing Different Distributions')
plt.show()
```

### 2. Split Violin (Comparison)

```python
import matplotlib.pyplot as plt
import numpy as np

def half_violin(ax, data1, data2, positions, colors=['lightblue', 'lightcoral']):
    """Create split violin plot for comparison."""
    
    # Left half
    parts1 = ax.violinplot(data1, positions=positions, showmedians=True)
    for body in parts1['bodies']:
        # Get the paths and modify to show only left half
        m = np.mean(body.get_paths()[0].vertices[:, 0])
        body.get_paths()[0].vertices[:, 0] = np.clip(
            body.get_paths()[0].vertices[:, 0], -np.inf, m)
        body.set_facecolor(colors[0])
        body.set_alpha(0.7)
    
    # Right half
    parts2 = ax.violinplot(data2, positions=positions, showmedians=True)
    for body in parts2['bodies']:
        m = np.mean(body.get_paths()[0].vertices[:, 0])
        body.get_paths()[0].vertices[:, 0] = np.clip(
            body.get_paths()[0].vertices[:, 0], m, np.inf)
        body.set_facecolor(colors[1])
        body.set_alpha(0.7)
    
    return parts1, parts2

# Example usage
np.random.seed(42)
data1 = [np.random.normal(0, std, 100) for std in [1, 1.5, 2]]
data2 = [np.random.normal(0.5, std, 100) for std in [1, 1.5, 2]]

fig, ax = plt.subplots()
half_violin(ax, data1, data2, [1, 2, 3])
ax.legend(['Group A', 'Group B'])
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Low', 'Medium', 'High'])
plt.show()
```

### 3. Violin with Box Plot Overlay

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = [np.random.normal(0, std, 200) for std in range(1, 5)]

fig, ax = plt.subplots()

# Violin plot
parts = ax.violinplot(data, showextrema=False)
for body in parts['bodies']:
    body.set_facecolor('lightblue')
    body.set_alpha(0.5)

# Box plot overlay
bp = ax.boxplot(data, widths=0.15, patch_artist=True,
                boxprops=dict(facecolor='white', edgecolor='black'),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                flierprops=dict(marker='o', markersize=4))

ax.set_title('Violin Plot with Box Plot Overlay')
plt.show()
```

### 4. Grouped Violin Plots

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# Generate data for two groups across three categories
group1 = [np.random.normal(10, 2, 100),
          np.random.normal(15, 3, 100),
          np.random.normal(12, 2.5, 100)]

group2 = [np.random.normal(12, 2, 100),
          np.random.normal(14, 2.5, 100),
          np.random.normal(16, 3, 100)]

fig, ax = plt.subplots(figsize=(10, 6))

# Positions for each group
pos1 = [1, 3, 5]
pos2 = [1.6, 3.6, 5.6]

# Plot both groups
parts1 = ax.violinplot(group1, positions=pos1, widths=0.5, showmedians=True)
parts2 = ax.violinplot(group2, positions=pos2, widths=0.5, showmedians=True)

# Style group 1
for body in parts1['bodies']:
    body.set_facecolor('steelblue')
    body.set_alpha(0.7)

# Style group 2
for body in parts2['bodies']:
    body.set_facecolor('coral')
    body.set_alpha(0.7)

ax.set_xticks([1.3, 3.3, 5.3])
ax.set_xticklabels(['Category A', 'Category B', 'Category C'])

# Custom legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='steelblue', alpha=0.7, label='Group 1'),
                   Patch(facecolor='coral', alpha=0.7, label='Group 2')]
ax.legend(handles=legend_elements)

ax.set_ylabel('Value')
ax.set_title('Grouped Violin Plots')
plt.show()
```

### 5. Financial Data Distribution

```python
import matplotlib.pyplot as plt
import numpy as np

# Simulated daily returns for different assets
np.random.seed(42)
stocks = np.random.normal(0.0005, 0.02, 252)  # ~12.5% annual return
bonds = np.random.normal(0.0002, 0.005, 252)  # ~5% annual return
commodities = np.random.normal(0, 0.03, 252)  # High volatility

data = [stocks * 100, bonds * 100, commodities * 100]  # Convert to percentage

fig, ax = plt.subplots(figsize=(8, 6))
parts = ax.violinplot(data, showmedians=True, showmeans=True)

colors = ['green', 'blue', 'orange']
for i, body in enumerate(parts['bodies']):
    body.set_facecolor(colors[i])
    body.set_alpha(0.6)

ax.axhline(y=0, color='black', linestyle='--', alpha=0.5)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Stocks', 'Bonds', 'Commodities'])
ax.set_ylabel('Daily Return (%)')
ax.set_title('Distribution of Daily Returns')
plt.show()
```

## Violin Plot vs Box Plot

| Feature | Box Plot | Violin Plot |
|---------|----------|-------------|
| Shows quartiles | ✅ | ❌ (without overlay) |
| Shows distribution shape | ❌ | ✅ |
| Shows multimodality | ❌ | ✅ |
| Compact display | ✅ | ❌ |
| Shows outliers | ✅ | ❌ |
| Sample size indication | ❌ | Via width |

## Width and Scaling

### Fixed Widths

```python
ax.violinplot(data, widths=0.8)  # All same width
```

### Variable Widths

```python
widths = [0.5, 0.7, 0.9, 1.0]  # Different widths
ax.violinplot(data, widths=widths)
```

### Scale by Sample Size

```python
# Width proportional to sqrt of sample size
sample_sizes = [len(d) for d in data]
widths = [0.5 * np.sqrt(n) / np.sqrt(max(sample_sizes)) for n in sample_sizes]
ax.violinplot(data, widths=widths)
```

## Common Pitfalls

### 1. Small Sample Sizes

```python
# Violin plots need sufficient data for meaningful KDE
# Minimum recommended: 30-50 points per group
small_data = np.random.randn(10)  # Too few points
# Consider using box plot or jittered strip plot instead
```

### 2. Missing Labels

```python
# violinplot doesn't automatically set x-tick labels
fig, ax = plt.subplots()
ax.violinplot(data)
# Must set labels manually
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['A', 'B', 'C', 'D'])
```

### 3. Comparing with Different Scales

```python
# Use same axis limits for fair comparison
ax.set_ylim(-5, 5)  # Consistent scale across subplots
```
