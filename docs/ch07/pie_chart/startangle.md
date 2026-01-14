# Keyword - startangle

The `startangle` parameter controls where the first slice of a pie chart begins, measured in degrees counterclockwise from the positive x-axis (3 o'clock position).

## Default Start Position

By default, pie charts begin at 0 degrees (3 o'clock position).

### 1. Default Behavior

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
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=0)
plt.show()
```

## Common Start Angles

Different starting positions create different visual effects.

### 1. Start from Top (90°)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()
```

### 2. Start from Left (180°)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=180)
plt.show()
```

### 3. Start from Bottom (270°)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=270)
plt.show()
```

## Custom Angles

Use any degree value for precise positioning.

### 1. 45 Degree Start

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.2],
    counterclock=True,
    startangle=45
)
plt.show()
```

### 2. 135 Degree Start

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=135)
plt.show()
```

### 3. Negative Angles

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=-45)  # Same as 315°
plt.show()
```

## Comparing Start Angles

Visualize how different angles affect pie orientation.

### 1. Side-by-Side Comparison

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
angles = [0, 90, 180, 270]

for ax, angle in zip(axes.flat, angles):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=angle)
    ax.set_title(f'startangle = {angle}°')

plt.tight_layout()
plt.show()
```

### 2. Fine-Grained Comparison

```python
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
angles = [0, 30, 60, 90, 120, 150]

for ax, angle in zip(axes.flat, angles):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=angle)
    ax.set_title(f'startangle = {angle}°')

plt.tight_layout()
plt.show()
```

## Interaction with counterclock

The `startangle` works together with `counterclock` to control slice direction.

### 1. Counterclockwise (Default)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=True)
ax.set_title('startangle=90, counterclock=True')
plt.show()
```

### 2. Clockwise Direction

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
ax.set_title('startangle=90, counterclock=False')
plt.show()
```

### 3. Combined Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=True)
axes[0].set_title('counterclock=True (default)')

axes[1].pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
axes[1].set_title('counterclock=False')

plt.tight_layout()
plt.show()
```

## Positioning Largest Slice

Use `startangle` to position the largest slice prominently.

### 1. Largest Slice at Top

```python
import numpy as np

# Calculate angle to position largest slice at top
total = sum(vals)
max_idx = vals.index(max(vals))
angle_before = sum(vals[:max_idx]) / total * 360
slice_half = (vals[max_idx] / total * 360) / 2
start = 90 + angle_before + slice_half

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=start)
ax.set_title('Largest Slice Centered at Top')
plt.show()
```

### 2. Highlight with Explode

```python
max_idx = vals.index(max(vals))
explode = [0.1 if i == max_idx else 0 for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
plt.show()
```

## Practical Example

Complete pie chart with custom start angle and styling.

### 1. Monthly Budget Chart

```python
vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = [0.05, 0, 0, 0, 0]

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=90,
    shadow=True,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

for autotext in autotexts:
    autotext.set_fontweight('bold')

ax.set_title('Monthly Budget Breakdown', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

### 2. Market Share Chart

```python
companies = ['Company A', 'Company B', 'Company C', 'Company D', 'Others']
shares = [35, 25, 20, 12, 8]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    shares,
    labels=companies,
    autopct='%1.1f%%',
    startangle=140,
    counterclock=False,
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
)
ax.set_title('Market Share Distribution')
plt.show()
```
