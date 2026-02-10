# Basic Bar Chart

Bar charts display categorical data with rectangular bars, where bar length represents the value for each category.

## Simple Bar Chart

Create a basic vertical bar chart with `ax.bar()`.

### 1. Import and Setup

```python
import matplotlib.pyplot as plt
import numpy as np
```

### 2. Define Categories and Values

```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
```

### 3. Create Bar Chart

```python
fig, ax = plt.subplots()
ax.bar(categories, values)
ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Basic Bar Chart')
plt.show()
```

## Horizontal Bar Chart

Use `ax.barh()` for horizontal orientation.

### 1. Basic Horizontal Bars

```python
fig, ax = plt.subplots()
ax.barh(categories, values)
ax.set_xlabel('Value')
ax.set_ylabel('Category')
plt.show()
```

### 2. Long Category Names

```python
categories = ['Category Alpha', 'Category Beta', 'Category Gamma', 
              'Category Delta', 'Category Epsilon']
values = [23, 45, 56, 78, 32]

fig, ax = plt.subplots()
ax.barh(categories, values)
plt.tight_layout()
plt.show()
```

### 3. Reversed Order

```python
fig, ax = plt.subplots()
ax.barh(categories[::-1], values[::-1])
plt.show()
```

## Pandas Plot Method

Use DataFrame's built-in plotting for quick visualizations.

### 1. Single Column

```python
import pandas as pd

data = {'Courses': ['Language', 'History', 'Math', 'Chemistry', 'Physics'],
        'Number of Teachers': [7, 3, 9, 3, 4]}
df = pd.DataFrame(data).set_index('Courses')

fig, ax = plt.subplots(figsize=(12, 3))
df.plot(kind='bar', ax=ax)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
```

### 2. Multiple Columns

```python
data = {'Student': ['Brandon', 'Vanessa', 'Daniel', 'Kevin', 'William'],
        'Midterm': [85, 60, 60, 65, 100],
        'Final': [90, 90, 65, 80, 95]}
df = pd.DataFrame(data).set_index('Student')

fig, ax = plt.subplots(figsize=(12, 3))
df.plot(kind='bar', ax=ax)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
```

### 3. Horizontal with Pandas

```python
fig, ax = plt.subplots(figsize=(12, 3))
df.plot(kind='barh', ax=ax)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.show()
```

## Numeric X-Axis

Use numeric positions instead of categorical labels.

### 1. Integer Positions

```python
x = np.arange(5)
values = [23, 45, 56, 78, 32]

fig, ax = plt.subplots()
ax.bar(x, values)
ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])
plt.show()
```

### 2. Custom Spacing

```python
x = [0, 1, 3, 4, 6]  # Non-uniform spacing
values = [23, 45, 56, 78, 32]

fig, ax = plt.subplots()
ax.bar(x, values, width=0.8)
plt.show()
```

### 3. Centered Labels

```python
x = np.arange(5)
fig, ax = plt.subplots()
ax.bar(x, values)
ax.set_xticks(x)
ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'], ha='center')
plt.show()
```

## Data Sources

Various ways to provide data to bar charts.

### 1. Lists

```python
categories = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
values = [10, 25, 15, 30, 20]
ax.bar(categories, values)
```

### 2. NumPy Arrays

```python
x = np.arange(5)
values = np.array([10, 25, 15, 30, 20])
ax.bar(x, values)
```

### 3. Pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'sales': [10, 25, 15, 30, 20]
})

fig, ax = plt.subplots()
ax.bar(df['day'], df['sales'])
plt.show()
```

## Adding Value Labels

Display values on top of bars.

### 1. Text Annotation

```python
fig, ax = plt.subplots()
bars = ax.bar(categories, values)

for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            str(value), ha='center', va='bottom')

plt.show()
```

### 2. Using bar_label

```python
fig, ax = plt.subplots()
bars = ax.bar(categories, values)
ax.bar_label(bars)
plt.show()
```

### 3. Formatted Labels

```python
fig, ax = plt.subplots()
bars = ax.bar(categories, values)
ax.bar_label(bars, fmt='%.1f', padding=3)
plt.show()
```

## Sorted Bar Charts

Order bars by value for better visualization.

### 1. Ascending Order

```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

sorted_idx = np.argsort(values)
sorted_categories = [categories[i] for i in sorted_idx]
sorted_values = [values[i] for i in sorted_idx]

fig, ax = plt.subplots()
ax.barh(sorted_categories, sorted_values)
plt.show()
```

### 2. Descending Order

```python
sorted_idx = np.argsort(values)[::-1]
sorted_categories = [categories[i] for i in sorted_idx]
sorted_values = [values[i] for i in sorted_idx]

fig, ax = plt.subplots()
ax.barh(sorted_categories, sorted_values)
plt.show()
```

### 3. Pandas Sorting

```python
df = pd.DataFrame({'category': categories, 'value': values})
df_sorted = df.sort_values('value', ascending=True)

fig, ax = plt.subplots()
ax.barh(df_sorted['category'], df_sorted['value'])
plt.show()
```

## Practical Example

Create a complete bar chart with styling.

### 1. Prepare Data

```python
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [150, 230, 180, 310, 275]
```

### 2. Create Styled Chart

```python
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(products, sales, color='steelblue', edgecolor='navy', linewidth=1.5)

ax.set_xlabel('Product', fontsize=12)
ax.set_ylabel('Sales ($K)', fontsize=12)
ax.set_title('Quarterly Sales by Product', fontsize=14)
ax.set_ylim(0, max(sales) * 1.15)
```

### 3. Add Annotations

```python
ax.bar_label(bars, fmt='$%.0fK', padding=3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```
