# Keyword - explode

The `explode` parameter separates one or more slices from the center of a pie chart by specifying offset distances. This draws attention to specific data segments.

## Basic Usage

The `explode` parameter takes a sequence of values corresponding to each slice, where 0 means no offset and positive values indicate the fraction of the radius to offset.

### 1. Single Slice Exploded

```python
import matplotlib.pyplot as plt

vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]

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

### 2. Highlight First Slice

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0, 0]
)
plt.show()
```

### 3. Highlight Largest Segment

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.15, 0, 0, 0, 0]
)
ax.set_title('Highlighting Home Rent')
plt.show()
```

## Explode Values

The explode value represents the fraction of the pie radius to offset each slice.

### 1. Different Offset Levels

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

offsets = [0.05, 0.15, 0.3]

for ax, offset in zip(axes, offsets):
    ax.pie(
        vals,
        labels=labels,
        autopct='%1.1f%%',
        explode=[offset, 0, 0, 0, 0]
    )
    ax.set_title(f'explode={offset}')

plt.tight_layout()
plt.show()
```

### 2. Multiple Slices Exploded

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0.1, 0, 0.1]
)
ax.set_title('Alternating Exploded Slices')
plt.show()
```

### 3. All Slices Exploded

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.05, 0.05, 0.05, 0.05, 0.05]
)
ax.set_title('All Slices Slightly Separated')
plt.show()
```

## Combined with Shadow

Shadows enhance the visual effect of exploded slices.

### 1. Explode with Shadow

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0, 0],
    shadow=True
)
plt.show()
```

### 2. Shadow Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0.1, 0],
    shadow=False
)
axes[0].set_title('Explode without Shadow')

axes[1].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0.1, 0],
    shadow=True
)
axes[1].set_title('Explode with Shadow')

plt.tight_layout()
plt.show()
```

## Combined with Radius

Adjust radius to accommodate exploded slices.

### 1. Standard Radius

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0, 0, 0, 0.1, 0.2],
    radius=1.0
)
plt.show()
```

### 2. Larger Radius

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

### 3. Radius Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0, 0, 0, 0.1, 0.2],
    radius=1.0
)
axes[0].set_title('radius=1.0')

axes[1].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0, 0, 0, 0.1, 0.2],
    radius=1.5
)
axes[1].set_title('radius=1.5')

plt.tight_layout()
plt.show()
```

## Combined with startangle

Exploded slices rotate with the starting angle.

### 1. Explode with startangle

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.15, 0, 0, 0, 0],
    startangle=90
)
plt.show()
```

### 2. Startangle Comparison

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

angles = [0, 90, 180, 270]

for ax, angle in zip(axes.flat, angles):
    ax.pie(
        vals,
        labels=labels,
        autopct='%1.1f%%',
        explode=[0.15, 0, 0, 0, 0],
        startangle=angle
    )
    ax.set_title(f'startangle={angle}')

plt.tight_layout()
plt.show()
```

## Combined with counterclock

Direction affects which slice gets exploded based on index.

### 1. Direction Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.15, 0, 0, 0, 0],
    counterclock=True
)
axes[0].set_title('Counterclockwise')

axes[1].pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    explode=[0.15, 0, 0, 0, 0],
    counterclock=False
)
axes[1].set_title('Clockwise')

plt.tight_layout()
plt.show()
```

### 2. Combined with startangle

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

configs = [
    {'startangle': 90, 'counterclock': True},
    {'startangle': 90, 'counterclock': False},
    {'startangle': 0, 'counterclock': True},
    {'startangle': 0, 'counterclock': False}
]

for ax, config in zip(axes.flat, configs):
    ax.pie(
        vals,
        labels=labels,
        autopct='%1.1f%%',
        explode=[0.15, 0, 0, 0, 0],
        **config
    )
    ax.set_title(f"startangle={config['startangle']}, counterclock={config['counterclock']}")

plt.tight_layout()
plt.show()
```

## Dynamic Explode

Calculate explode values programmatically.

### 1. Explode Maximum Value

```python
max_idx = vals.index(max(vals))
explode = [0.1 if i == max_idx else 0 for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=explode)
ax.set_title('Largest Segment Highlighted')
plt.show()
```

### 2. Explode Minimum Value

```python
min_idx = vals.index(min(vals))
explode = [0.15 if i == min_idx else 0 for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=explode)
ax.set_title('Smallest Segment Highlighted')
plt.show()
```

### 3. Explode by Threshold

```python
threshold = 400
explode = [0.1 if v < threshold else 0 for v in vals]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=explode)
ax.set_title(f'Values Below {threshold} Highlighted')
plt.show()
```

### 4. Proportional Explode

```python
max_val = max(vals)
explode = [0.1 * (1 - v/max_val) for v in vals]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=explode)
ax.set_title('Smaller Slices More Exploded')
plt.show()
```

## Full Customization

Combine explode with all other pie chart parameters.

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
ax.set_title('Complete Pie Chart Customization')
plt.show()
```

### 2. Professional Presentation

```python
colors = ['#e74c3c', '#3498db', '#9b59b6', '#f39c12', '#2ecc71']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    colors=colors,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.3,
    explode=[0.08, 0, 0, 0.05, 0.1],
    startangle=90,
    counterclock=False,
    pctdistance=0.6
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax.set_title('Monthly Budget Distribution', fontsize=14, fontweight='bold')
plt.show()
```

## Practical Applications

### 1. Highlight Key Category

```python
market_share = [35, 28, 18, 12, 7]
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']

fig, ax = plt.subplots(figsize=(9, 7))
ax.pie(
    market_share,
    labels=companies,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0, 0],
    colors=['#e74c3c', '#95a5a6', '#95a5a6', '#95a5a6', '#bdc3c7'],
    startangle=90,
    counterclock=False
)
ax.set_title('Market Share - Company A Leads')
plt.show()
```

### 2. Emphasize Problem Areas

```python
budget_status = [60, 25, 10, 5]
categories = ['On Track', 'At Risk', 'Over Budget', 'Critical']
colors = ['#27ae60', '#f39c12', '#e67e22', '#e74c3c']
explode = [0, 0.05, 0.1, 0.15]

fig, ax = plt.subplots(figsize=(9, 7))
ax.pie(
    budget_status,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    startangle=90,
    counterclock=False
)
ax.set_title('Project Budget Status')
plt.show()
```

### 3. Survey Results Highlight

```python
responses = [45, 30, 15, 10]
categories = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied']
colors = ['#27ae60', '#82e0aa', '#f7dc6f', '#e74c3c']

fig, ax = plt.subplots(figsize=(9, 7))
ax.pie(
    responses,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    explode=[0.1, 0, 0, 0.1],
    startangle=90,
    counterclock=False
)
ax.set_title('Customer Satisfaction Survey')
plt.show()
```
