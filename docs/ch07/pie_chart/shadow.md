# Keyword - shadow

The `shadow` parameter adds a shadow effect beneath the pie chart, creating a 3D-like appearance that adds visual depth.

## Basic Shadow

Enable shadow with a simple boolean parameter.

### 1. Shadow Enabled

```python
import matplotlib.pyplot as plt

vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True)
plt.show()
```

### 2. No Shadow (Default)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=False)
plt.show()
```

### 3. Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals, labels=labels)
axes[0].set_title('shadow=False (default)')

axes[1].pie(vals, labels=labels, shadow=True)
axes[1].set_title('shadow=True')

plt.tight_layout()
plt.show()
```

## Shadow with Percentage Labels

Combine shadow with autopct for labeled slices.

### 1. Basic Combination

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%1.1f%%')
plt.show()
```

### 2. Styled Percentages

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%'
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)

plt.show()
```

## Shadow with Explode

Combine shadow with exploded slices for emphasis.

### 1. Single Exploded Slice

```python
explode = [0.1, 0, 0, 0, 0]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, explode=explode, autopct='%1.1f%%')
plt.show()
```

### 2. Multiple Exploded Slices

```python
explode = [0.05, 0.05, 0.05, 0.05, 0.05]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, explode=explode, autopct='%1.1f%%')
plt.show()
```

### 3. Highlight Maximum

```python
max_idx = vals.index(max(vals))
explode = [0.1 if i == max_idx else 0 for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, explode=explode, autopct='%1.1f%%')
plt.show()
```

## Shadow with Colors

Combine shadow with custom color schemes.

### 1. Custom Colors

```python
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, colors=colors, autopct='%1.1f%%')
plt.show()
```

### 2. Colormap

```python
import numpy as np

cmap = plt.cm.Pastel1
colors = [cmap(i) for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, colors=colors, autopct='%1.1f%%')
plt.show()
```

### 3. Dark Theme

```python
colors = ['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f39c12']

fig, ax = plt.subplots()
fig.patch.set_facecolor('#2c3e50')
ax.pie(vals, labels=labels, shadow=True, colors=colors, autopct='%1.1f%%',
       textprops={'color': 'white'})
plt.show()
```

## Shadow with Radius

Adjust pie size while maintaining shadow effect.

### 1. Larger Radius

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, radius=1.5, autopct='%1.1f%%')
plt.show()
```

### 2. Smaller Radius

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, radius=0.7, autopct='%1.1f%%')
plt.show()
```

### 3. Radius Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
radii = [0.7, 1.0, 1.3]

for ax, r in zip(axes, radii):
    ax.pie(vals, labels=labels, shadow=True, radius=r, autopct='%1.1f%%')
    ax.set_title(f'radius = {r}')

plt.tight_layout()
plt.show()
```

## Shadow with Start Angle

Position slices with shadow effect.

### 1. Start from Top

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, startangle=90, autopct='%1.1f%%')
plt.show()
```

### 2. Custom Angle

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, startangle=45, autopct='%1.1f%%')
plt.show()
```

## Shadow with Edge Styling

Combine shadow with wedge properties.

### 1. White Edges

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%1.1f%%',
       wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.show()
```

### 2. Dark Edges

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%1.1f%%',
       wedgeprops={'edgecolor': 'black', 'linewidth': 1})
plt.show()
```

## Multiple Pie Charts with Shadow

Compare data across multiple pies.

### 1. Side-by-Side Comparison

```python
vals1 = [1400, 600, 300, 410, 250]
vals2 = [1200, 800, 350, 380, 300]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals1, labels=labels, shadow=True, autopct='%1.1f%%')
axes[0].set_title('Month 1')

axes[1].pie(vals2, labels=labels, shadow=True, autopct='%1.1f%%')
axes[1].set_title('Month 2')

plt.tight_layout()
plt.show()
```

### 2. Grid of Pies

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
data = [
    [30, 25, 20, 15, 10],
    [28, 27, 22, 13, 10],
    [32, 23, 18, 17, 10],
    [35, 22, 20, 14, 9]
]

for ax, quarter, values in zip(axes.flat, quarters, data):
    ax.pie(values, labels=labels, shadow=True, autopct='%1.0f%%')
    ax.set_title(quarter)

plt.tight_layout()
plt.show()
```

## Practical Example

Complete styled pie chart with shadow.

### 1. Budget Visualization

```python
vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
explode = [0.02] * len(vals)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    shadow=True,
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax.set_title('Monthly Expense Breakdown', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 2. Survey Results

```python
responses = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']
counts = [45, 30, 15, 7, 3]
colors = ['#27ae60', '#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    counts,
    labels=responses,
    autopct='%1.1f%%',
    colors=colors,
    shadow=True,
    startangle=140
)

ax.set_title('Customer Satisfaction Survey', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```
