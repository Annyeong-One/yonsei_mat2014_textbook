# Basic Pie Chart

Pie charts display proportional data as slices of a circle, where each slice represents a category's contribution to the whole.

## Simple Pie Chart

Create a basic pie chart with `ax.pie()`.

### 1. Import and Setup

```python
import matplotlib.pyplot as plt
import numpy as np
```

### 2. Define Categories and Values

```python
vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]
```

### 3. Create Pie Chart

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)
plt.show()
```

## Percentage Labels

Display percentage values on each slice.

### 1. Auto Percentage

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 2. Integer Percentage

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%d%%')
plt.show()
```

### 3. Custom Format Function

```python
def make_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n(${val:,})'
    return autopct

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct=make_autopct(vals))
plt.show()
```

## Exploded Slices

Separate one or more slices from the center.

### 1. Single Exploded Slice

```python
explode = [0.1, 0, 0, 0, 0]  # Explode first slice

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%')
plt.show()
```

### 2. Multiple Exploded Slices

```python
explode = [0.1, 0, 0.1, 0, 0]  # Explode first and third slices

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%')
plt.show()
```

### 3. Highlight Maximum Value

```python
max_idx = vals.index(max(vals))
explode = [0.1 if i == max_idx else 0 for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%')
plt.show()
```

## Start Angle and Direction

Control the starting position and rotation direction.

### 1. Custom Start Angle

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, startangle=90)  # Start from top
plt.show()
```

### 2. Clockwise Direction

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, startangle=90, counterclock=False)
plt.show()
```

### 3. Start from Right

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, startangle=0)  # Start from right (default)
plt.show()
```

## Colors and Styling

Customize the appearance of pie slices.

### 1. Custom Colors

```python
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()
```

### 2. Colormap

```python
cmap = plt.cm.Pastel1
colors = [cmap(i) for i in range(len(vals))]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, colors=colors, autopct='%1.1f%%')
plt.show()
```

### 3. Edge Colors

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%',
                                   wedgeprops={'edgecolor': 'white', 'linewidth': 2})
plt.show()
```

## Shadow Effect

Add shadow for 3D-like appearance.

### 1. Basic Shadow

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%1.1f%%')
plt.show()
```

### 2. Shadow with Explode

```python
explode = [0.05] * len(vals)

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
plt.show()
```

## Label Positioning

Control where labels appear.

### 1. Label Distance

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, labeldistance=1.15, autopct='%1.1f%%')
plt.show()
```

### 2. Percentage Distance

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', pctdistance=0.6)
plt.show()
```

### 3. Rotated Labels

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%')

for text in texts:
    text.set_rotation(45)
    
plt.show()
```

## Legend Instead of Labels

Use legend for cleaner appearance.

### 1. Basic Legend

```python
fig, ax = plt.subplots()
wedges, texts = ax.pie(vals)
ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
```

### 2. Legend with Percentages

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, autopct='%1.1f%%')
ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
```

### 3. Legend with Values

```python
legend_labels = [f'{label}: ${val:,}' for label, val in zip(labels, vals)]

fig, ax = plt.subplots()
wedges, texts = ax.pie(vals)
ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()
```

## Data Sources

Various ways to provide data to pie charts.

### 1. Lists

```python
categories = ['A', 'B', 'C', 'D']
values = [30, 25, 25, 20]
ax.pie(values, labels=categories)
```

### 2. NumPy Arrays

```python
values = np.array([30, 25, 25, 20])
ax.pie(values)
```

### 3. Pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'category': ['Home Rent', 'Food', 'Phone/Internet Bill', 'Car', 'Other Utilities'],
    'amount': [1400, 600, 300, 410, 250]
})

fig, ax = plt.subplots()
ax.pie(df['amount'], labels=df['category'], autopct='%1.1f%%')
plt.show()
```

### 4. Pandas Series

```python
expenses = pd.Series([1400, 600, 300, 410, 250],
                     index=['Home Rent', 'Food', 'Phone/Internet Bill', 'Car', 'Other Utilities'])

fig, ax = plt.subplots()
ax.pie(expenses, labels=expenses.index, autopct='%1.1f%%')
plt.show()
```

## Text Styling

Customize label and percentage text appearance.

### 1. Text Properties

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%')

for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('white')

plt.show()
```

### 2. Using textprops

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%',
       textprops={'fontsize': 10, 'fontweight': 'bold'})
plt.show()
```

## Practical Example

Create a complete pie chart with styling.

### 1. Prepare Data

```python
expenses = {
    'Home Rent': 1400,
    'Food': 600,
    'Phone/Internet Bill': 300,
    'Car': 410,
    'Other Utilities': 250
}
labels = list(expenses.keys())
vals = list(expenses.values())
```

### 2. Create Styled Chart

```python
fig, ax = plt.subplots(figsize=(10, 8))

colors = plt.cm.Set3(np.linspace(0, 1, len(vals)))
explode = [0.02] * len(vals)

wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode,
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)
```

### 3. Add Title and Styling

```python
ax.set_title('Monthly Expense Breakdown', fontsize=14, fontweight='bold')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.show()
```
