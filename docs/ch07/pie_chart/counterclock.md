# Keyword - counterclock

The `counterclock` parameter controls the direction in which pie chart slices are drawn. When `True` (default), slices are drawn counterclockwise; when `False`, slices are drawn clockwise.

## Default Direction

By default, pie charts draw slices counterclockwise from the starting angle.

### 1. Default Behavior (Counterclockwise)

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
ax.pie(vals, labels=labels, autopct='%1.1f%%', counterclock=True)
plt.show()
```

## Clockwise Direction

Set `counterclock=False` to draw slices in clockwise order.

### 1. Basic Clockwise

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', counterclock=False)
plt.show()
```

### 2. Direction Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals, labels=labels, autopct='%1.1f%%', counterclock=True)
axes[0].set_title('counterclock=True (default)')

axes[1].pie(vals, labels=labels, autopct='%1.1f%%', counterclock=False)
axes[1].set_title('counterclock=False')

plt.tight_layout()
plt.show()
```

## Combined with startangle

The interaction between `counterclock` and `startangle` determines the final layout.

### 1. Top Start, Counterclockwise

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=True
)
plt.show()
```

### 2. Top Start, Clockwise

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False
)
plt.show()
```

### 3. Four Combinations

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: startangle=0, counterclockwise
axes[0, 0].pie(vals, labels=labels, autopct='%1.1f%%', startangle=0, counterclock=True)
axes[0, 0].set_title('startangle=0, counterclock=True')

# Top-right: startangle=0, clockwise
axes[0, 1].pie(vals, labels=labels, autopct='%1.1f%%', startangle=0, counterclock=False)
axes[0, 1].set_title('startangle=0, counterclock=False')

# Bottom-left: startangle=90, counterclockwise
axes[1, 0].pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=True)
axes[1, 0].set_title('startangle=90, counterclock=True')

# Bottom-right: startangle=90, clockwise
axes[1, 1].pie(vals, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
axes[1, 1].set_title('startangle=90, counterclock=False')

plt.tight_layout()
plt.show()
```

## Combined with explode

Exploded slices follow the same directional rules.

### 1. Counterclockwise with Explode

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.2],
    counterclock=True
)
plt.show()
```

### 2. Clockwise with Explode

```python
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.5,
    explode=[0, 0, 0, 0.1, 0.2],
    counterclock=False
)
plt.show()
```

### 3. Explode Direction Comparison

```python
explode = [0, 0, 0, 0.1, 0.2]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.2,
    explode=explode,
    counterclock=True
)
axes[0].set_title('Counterclockwise with Explode')

axes[1].pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.2,
    explode=explode,
    counterclock=False
)
axes[1].set_title('Clockwise with Explode')

plt.tight_layout()
plt.show()
```

## Full Customization

Combine all positioning parameters for complete control.

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
    counterclock=True,
    startangle=45
)
ax.set_title('Complete Customization')
plt.show()
```

### 2. Professional Layout

```python
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    vals,
    labels=labels,
    colors=colors,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.3,
    explode=[0.05, 0, 0, 0.1, 0.15],
    counterclock=False,
    startangle=90
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

ax.set_title('Monthly Budget Breakdown', fontsize=14, fontweight='bold')
plt.show()
```

### 3. Comparison Grid

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

configs = [
    {'startangle': 0, 'counterclock': True},
    {'startangle': 0, 'counterclock': False},
    {'startangle': 90, 'counterclock': True},
    {'startangle': 90, 'counterclock': False}
]

for ax, config in zip(axes.flat, configs):
    ax.pie(
        vals,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        explode=[0.05, 0, 0, 0.1, 0.15],
        **config
    )
    ax.set_title(f"startangle={config['startangle']}, counterclock={config['counterclock']}")

plt.tight_layout()
plt.show()
```

## Practical Applications

### 1. Reading Order (Top to Bottom, Clockwise)

For Western reading conventions, start at top and go clockwise.

```python
quarterly_sales = [250, 320, 280, 310]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    quarterly_sales,
    labels=quarters,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False,
    colors=['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
)
ax.set_title('Quarterly Sales Distribution')
plt.show()
```

### 2. Clock-Style Layout

Arrange data like clock positions.

```python
monthly_data = [100, 120, 90, 110, 130, 95, 105, 115, 125, 140, 135, 150]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(
    monthly_data,
    labels=months,
    autopct='%1.0f%%',
    startangle=90,
    counterclock=False,
    pctdistance=0.75
)
ax.set_title('Monthly Performance')
plt.show()
```

### 3. Survey Results

Standard presentation format.

```python
responses = [45, 30, 15, 10]
categories = ['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree']
colors = ['#27ae60', '#82e0aa', '#f5b7b1', '#e74c3c']

fig, ax = plt.subplots(figsize=(9, 7))
ax.pie(
    responses,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False,
    explode=[0.05, 0, 0, 0]
)
ax.set_title('Customer Satisfaction Survey')
plt.show()
```
