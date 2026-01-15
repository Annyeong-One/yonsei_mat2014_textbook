# Box Plot Keywords

The `ax.boxplot()` method accepts numerous keyword arguments to control appearance and behavior.

## Labels

The `labels` keyword assigns names to each box on the x-axis.

### 1. Basic Labels

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data_a = np.random.normal(100, 10, 200)
data_b = np.random.normal(90, 20, 200)
data_c = np.random.normal(110, 15, 200)

fig, ax = plt.subplots()
ax.boxplot([data_a, data_b, data_c], labels=['Group A', 'Group B', 'Group C'])
plt.show()
```

### 2. LaTeX Labels

```python
ax.boxplot([data_a, data_b, data_c], 
           labels=[r'$10^4$', r'$5 \cdot 10^4$', r'$10^5$'])
```

### 3. Numeric Labels

```python
ax.boxplot([data_a, data_b, data_c], labels=['N=100', 'N=500', 'N=1000'])
```

## Widths

The `widths` keyword controls the width of each box.

### 1. Uniform Width

```python
ax.boxplot([data_a, data_b, data_c], widths=0.5)  # All boxes same width
```

### 2. Variable Widths

```python
ax.boxplot([data_a, data_b, data_c], widths=[0.2, 0.4, 0.6])
```

### 3. Proportional to Sample Size

```python
sizes = [100, 500, 1000]
widths = [np.sqrt(s) / np.sqrt(max(sizes)) * 0.8 for s in sizes]
ax.boxplot([data_a, data_b, data_c], widths=widths)
```

## Orientation

The `vert` keyword controls vertical or horizontal orientation.

### 1. Vertical (Default)

```python
ax.boxplot(data, vert=True)
```

### 2. Horizontal

```python
fig, ax = plt.subplots()
ax.boxplot([data_a, data_b, data_c], vert=False)
ax.set_yticklabels(['A', 'B', 'C'])
ax.set_xlabel('Value')
plt.show()
```

### 3. Use Case

Horizontal orientation works well when labels are long or when comparing many groups.

## Notch

The `notch` keyword adds confidence interval notches around the median.

### 1. Enable Notches

```python
ax.boxplot(data, notch=True)
```

### 2. Interpretation

Non-overlapping notches between two boxes suggest the medians differ significantly at approximately the 95% confidence level.

### 3. Notch Calculation

```python
# Notch extent approximation
notch_extent = 1.57 * IQR / np.sqrt(n)
```

## Patch Artist

The `patch_artist` keyword enables filled boxes for color customization.

### 1. Enable Patch Artist

```python
bp = ax.boxplot(data, patch_artist=True)
```

### 2. Access Box Patches

```python
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')
```

### 3. Required for Fill Colors

Without `patch_artist=True`, boxes are drawn as lines only and cannot be filled.

## Show Statistics

Keywords control which statistical markers appear.

### 1. Show Mean

```python
ax.boxplot(data, showmeans=True)
```

### 2. Show Fliers (Outliers)

```python
ax.boxplot(data, showfliers=True)   # Default
ax.boxplot(data, showfliers=False)  # Hide outliers
```

### 3. Mean Line Instead of Point

```python
ax.boxplot(data, showmeans=True, meanline=True)
```

## Whisker Range

The `whis` keyword controls whisker extent.

### 1. Default (1.5 IQR)

```python
ax.boxplot(data, whis=1.5)
```

### 2. Custom Multiplier

```python
ax.boxplot(data, whis=2.0)  # Fewer outliers shown
```

### 3. Percentile Range

```python
ax.boxplot(data, whis=[5, 95])  # Whiskers at 5th and 95th percentiles
```
