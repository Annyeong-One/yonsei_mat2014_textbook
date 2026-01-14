# Keyword - radius

The `radius` parameter controls the size of a pie chart by specifying the radius of the pie. The default value is 1.

## Basic Usage

The radius value scales the pie chart relative to the axes.

### 1. Default Radius

```python
import matplotlib.pyplot as plt

vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 2. Explicit Default

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1)
plt.show()
```

### 3. Larger Radius

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%1.1f%%', radius=1.5)
plt.show()
```

## Radius Values

Different radius values change the pie chart size.

### 1. Small Radius

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=0.5)
plt.show()
```

### 2. Large Radius

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=2.0)
plt.show()
```

### 3. Radius Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

radii = [0.5, 1.0, 1.5]

for ax, r in zip(axes, radii):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=r)
    ax.set_title(f'radius={r}')

plt.tight_layout()
plt.show()
```

### 4. Extended Range

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

radii = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8]

for ax, r in zip(axes.flat, radii):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=r)
    ax.set_title(f'radius={r}')

plt.tight_layout()
plt.show()
```

## Combined with Shadow

Shadow effects work with any radius size.

### 1. Small with Shadow

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=0.7, shadow=True)
plt.show()
```

### 2. Large with Shadow

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.5, shadow=True)
plt.show()
```

### 3. Shadow Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals, labels=labels, autopct='%1.1f%%', radius=1.3, shadow=False)
axes[0].set_title('radius=1.3, shadow=False')

axes[1].pie(vals, labels=labels, autopct='%1.1f%%', radius=1.3, shadow=True)
axes[1].set_title('radius=1.3, shadow=True')

plt.tight_layout()
plt.show()
```

## Combined with Explode

Larger radius provides more space for exploded slices.

### 1. Small Radius with Explode

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    radius=0.8,
    explode=[0.1, 0, 0, 0, 0]
)
plt.show()
```

### 2. Large Radius with Explode

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.2]
)
plt.show()
```

### 3. Radius-Explode Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

radii = [0.7, 1.0, 1.4]

for ax, r in zip(axes, radii):
    ax.pie(
        vals,
        labels=labels,
        autopct='%1.1f%%',
        radius=r,
        explode=[0.15, 0, 0, 0.1, 0]
    )
    ax.set_title(f'radius={r}')

plt.tight_layout()
plt.show()
```

## Combined with pctdistance

The `pctdistance` parameter positions percentage labels relative to the radius.

### 1. Default pctdistance

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.3)
plt.show()
```

### 2. Adjusted pctdistance

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.3, pctdistance=0.5)
plt.show()
```

### 3. pctdistance Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

distances = [0.4, 0.6, 0.8]

for ax, d in zip(axes, distances):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.2, pctdistance=d)
    ax.set_title(f'pctdistance={d}')

plt.tight_layout()
plt.show()
```

## Combined with labeldistance

The `labeldistance` parameter positions labels relative to the radius.

### 1. Labels Inside

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.5, labeldistance=0.7)
plt.show()
```

### 2. Labels Far Outside

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.0, labeldistance=1.3)
plt.show()
```

### 3. labeldistance Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

distances = [0.8, 1.1, 1.4]

for ax, d in zip(axes, distances):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.0, labeldistance=d)
    ax.set_title(f'labeldistance={d}')

plt.tight_layout()
plt.show()
```

## Figure Size Coordination

Coordinate radius with figure size for optimal display.

### 1. Small Figure, Small Radius

```python
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=0.8)
plt.show()
```

### 2. Large Figure, Large Radius

```python
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.5)
plt.show()
```

### 3. Figure-Radius Combinations

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

configs = [
    {'figsize_note': 'Subplot', 'radius': 0.7},
    {'figsize_note': 'Subplot', 'radius': 1.0},
    {'figsize_note': 'Subplot', 'radius': 1.3}
]

for ax, config in zip(axes, configs):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=config['radius'])
    ax.set_title(f"radius={config['radius']}")

plt.tight_layout()
plt.show()
```

## Donut Charts

Use radius with nested pie charts to create donut charts.

### 1. Basic Donut

```python
fig, ax = plt.subplots()

# Outer ring
ax.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.2, 
       wedgeprops=dict(width=0.4))

plt.show()
```

### 2. Nested Rings

```python
outer_vals = [1400, 600, 300, 410, 250]
inner_vals = [800, 600, 500, 400, 660]

fig, ax = plt.subplots(figsize=(9, 9))

ax.pie(outer_vals, radius=1.3, wedgeprops=dict(width=0.3),
       autopct='%1.0f%%', pctdistance=0.85)
ax.pie(inner_vals, radius=1.0, wedgeprops=dict(width=0.3),
       autopct='%1.0f%%', pctdistance=0.75)

ax.set_title('Nested Donut Chart')
plt.show()
```

### 3. Donut Width Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

widths = [0.2, 0.4, 0.6]

for ax, w in zip(axes, widths):
    ax.pie(vals, radius=1.2, wedgeprops=dict(width=w), autopct='%1.1f%%')
    ax.set_title(f'width={w}')

plt.tight_layout()
plt.show()
```

## Multiple Pie Charts

Consistent radius ensures uniform appearance across subplots.

### 1. Uniform Radius

```python
data_sets = [
    [30, 25, 25, 20],
    [40, 30, 20, 10],
    [35, 35, 15, 15]
]
titles = ['Q1', 'Q2', 'Q3']
categories = ['A', 'B', 'C', 'D']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, data, title in zip(axes, data_sets, titles):
    ax.pie(data, labels=categories, autopct='%1.0f%%', radius=1.0)
    ax.set_title(title)

plt.tight_layout()
plt.show()
```

### 2. Varying Radius by Importance

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

radii = [0.8, 1.2, 0.8]
titles = ['Secondary', 'Primary', 'Secondary']

for ax, data, r, title in zip(axes, data_sets, radii, titles):
    ax.pie(data, labels=categories, autopct='%1.0f%%', radius=r)
    ax.set_title(f'{title} (radius={r})')

plt.tight_layout()
plt.show()
```

## Full Customization

Combine radius with all other parameters.

### 1. Complete Example

```python
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.2],
    startangle=90,
    counterclock=False
)
ax.set_title('Complete Customization')
plt.show()
```

### 2. Professional Layout

```python
colors = ['#e74c3c', '#3498db', '#9b59b6', '#f39c12', '#2ecc71']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    colors=colors,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.4,
    explode=[0.05, 0, 0, 0.08, 0.12],
    startangle=90,
    counterclock=False,
    pctdistance=0.6,
    labeldistance=1.15
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax.set_title('Monthly Budget Distribution', fontsize=14, fontweight='bold')
plt.show()
```

## Practical Applications

### 1. Dashboard Layout

```python
fig = plt.figure(figsize=(12, 8))

# Main chart (larger)
ax1 = fig.add_subplot(121)
ax1.pie(vals, labels=labels, autopct='%1.1f%%', radius=1.3, shadow=True)
ax1.set_title('Overall Budget', fontsize=12)

# Secondary chart (smaller)
ax2 = fig.add_subplot(222)
ax2.pie([60, 40], labels=['Fixed', 'Variable'], autopct='%1.0f%%', radius=0.9)
ax2.set_title('Cost Type', fontsize=10)

ax3 = fig.add_subplot(224)
ax3.pie([70, 30], labels=['Essential', 'Optional'], autopct='%1.0f%%', radius=0.9)
ax3.set_title('Priority', fontsize=10)

plt.tight_layout()
plt.show()
```

### 2. Comparison Panel

```python
this_year = [1400, 600, 300, 410, 250]
last_year = [1200, 700, 350, 380, 300]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].pie(last_year, labels=labels, autopct='%1.1f%%', radius=1.2)
axes[0].set_title('Last Year')

axes[1].pie(this_year, labels=labels, autopct='%1.1f%%', radius=1.2)
axes[1].set_title('This Year')

plt.suptitle('Year-over-Year Budget Comparison', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 3. Hierarchical Display

```python
fig, ax = plt.subplots(figsize=(10, 10))

# Outer: Categories
outer_vals = [2000, 700, 260]
outer_labels = ['Housing', 'Living', 'Utilities']
outer_colors = ['#3498db', '#2ecc71', '#e74c3c']

# Inner: Subcategories
inner_vals = [1400, 600, 300, 410, 250, 10]
inner_colors = ['#5dade2', '#85c1e9', '#58d68d', '#82e0aa', '#f1948a', '#f5b7b1']

ax.pie(outer_vals, labels=outer_labels, colors=outer_colors,
       radius=1.4, wedgeprops=dict(width=0.3), labeldistance=1.1)
ax.pie(inner_vals, colors=inner_colors,
       radius=1.1, wedgeprops=dict(width=0.4))

ax.set_title('Budget Hierarchy', fontsize=14)
plt.show()
```
