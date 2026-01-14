# Keyword - autopct

The `autopct` parameter automatically calculates and displays percentage values on pie chart slices. It accepts either a format string or a callable function.

## Format String Syntax

The format string follows Python's old-style string formatting:

$$\begin{array}{cccccccccccccccccc}
\text{autopct}&=&\text{'}&\text{%}&4&.&1&\text{f}&\text{%%}&\text{'}\\
&&&\uparrow&\uparrow&&\uparrow&\uparrow&\uparrow&\\
&&&\text{Initial Format}&\text{Total String}&&\text{Number of Digits}&\text{Data Type}&\text{First \% - Escape Character (Old Style)}&\\
&&&\text{Symbol}&\text{Length of Number}&&\text{after Decimal}&\text{Specifier}&\text{Second \% - Percentage Symbol}&\\
\end{array}$$

### Format String Components

| Component | Description | Example |
|-----------|-------------|---------|
| `%` | Initial format symbol | Required |
| Width | Minimum total string length | `4` means at least 4 characters |
| `.precision` | Digits after decimal point | `.1` means 1 decimal place |
| Type | Data type specifier | `f` for float, `d` for integer |
| `%%` | Literal percent symbol | First `%` escapes, second displays |

## Basic Usage

Display percentage values on pie slices.

### 1. Simple Percentage

```python
import matplotlib.pyplot as plt

vals = [1400, 600, 300, 410, 250]
labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car", "Other Utilities"]

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 2. With Shadow

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, shadow=True, autopct='%4.1f%%')
plt.show()
```

### 3. Integer Percentage

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.0f%%')
plt.show()
```

## Decimal Precision

Control the number of decimal places displayed.

### 1. No Decimal Places

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.0f%%')
plt.show()
```

### 2. One Decimal Place

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.1f%%')
plt.show()
```

### 3. Two Decimal Places

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.2f%%')
plt.show()
```

### 4. Precision Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

precisions = ['%.0f%%', '%.1f%%', '%.2f%%']
titles = ['No Decimal', 'One Decimal', 'Two Decimals']

for ax, fmt, title in zip(axes, precisions, titles):
    ax.pie(vals, labels=labels, autopct=fmt)
    ax.set_title(f"{title}: autopct='{fmt}'")

plt.tight_layout()
plt.show()
```

## Width Specifier

Set minimum width for alignment.

### 1. Narrow Width

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 2. Wide Width

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%5.1f%%')
plt.show()
```

### 3. Width Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

widths = ['%1.1f%%', '%4.1f%%', '%6.1f%%']
titles = ['Width 1', 'Width 4', 'Width 6']

for ax, fmt, title in zip(axes, widths, titles):
    ax.pie(vals, labels=labels, autopct=fmt)
    ax.set_title(f"{title}: autopct='{fmt}'")

plt.tight_layout()
plt.show()
```

## Data Type Specifiers

Different type specifiers for various display formats.

### 1. Float Type (f)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%')
plt.show()
```

### 2. Integer Display

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.0f%%')
plt.show()
```

### 3. Scientific Notation (e)

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.1e%%')
plt.show()
```

### 4. Type Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

formats = ['%.1f%%', '%.0f%%', '%.2e%%']
titles = ['Float', 'Integer', 'Scientific']

for ax, fmt, title in zip(axes, formats, titles):
    ax.pie(vals, labels=labels, autopct=fmt)
    ax.set_title(f'{title}: {fmt}')

plt.tight_layout()
plt.show()
```

## Custom Format Strings

Add text around the percentage value.

### 1. Parentheses

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='(%.1f%%)')
plt.show()
```

### 2. Brackets

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='[%.1f%%]')
plt.show()
```

### 3. Custom Text

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%.1f pct')
plt.show()
```

### 4. Format Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

formats = ['%.1f%%', '(%.1f%%)', '[%.0f]']
titles = ['Standard', 'Parentheses', 'Brackets']

for ax, fmt, title in zip(axes, formats, titles):
    ax.pie(vals, labels=labels, autopct=fmt)
    ax.set_title(title)

plt.tight_layout()
plt.show()
```

## Callable Function

Use a function for complete control over formatting.

### 1. Simple Function

```python
def format_pct(pct):
    return f'{pct:.1f}%'

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct=format_pct)
plt.show()
```

### 2. Conditional Formatting

```python
def conditional_pct(pct):
    if pct > 20:
        return f'{pct:.1f}%'
    else:
        return ''

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct=conditional_pct)
plt.show()
```

### 3. Show Absolute Values

```python
def make_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{val:d}'
    return autopct

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct=make_autopct(vals))
plt.show()
```

### 4. Combined Percentage and Value

```python
def make_autopct_combined(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n(${val:,})'
    return autopct

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(vals, labels=labels, autopct=make_autopct_combined(vals))
plt.show()
```

### 5. Threshold Display

```python
def threshold_autopct(pct, threshold=10):
    if pct >= threshold:
        return f'{pct:.1f}%'
    return ''

fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct=lambda p: threshold_autopct(p, 15))
plt.show()
```

## Combined with pctdistance

Position percentage labels within slices.

### 1. Center Position

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', pctdistance=0.5)
plt.show()
```

### 2. Near Edge

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', pctdistance=0.8)
plt.show()
```

### 3. pctdistance Comparison

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

distances = [0.4, 0.6, 0.8]

for ax, d in zip(axes, distances):
    ax.pie(vals, labels=labels, autopct='%1.1f%%', pctdistance=d)
    ax.set_title(f'pctdistance={d}')

plt.tight_layout()
plt.show()
```

## Combined with textprops

Style the percentage text.

### 1. Font Size

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', 
       textprops={'fontsize': 12})
plt.show()
```

### 2. Font Weight

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%',
       textprops={'fontweight': 'bold'})
plt.show()
```

### 3. Font Color

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%',
       textprops={'color': 'white'})
plt.show()
```

### 4. Multiple Properties

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%',
       textprops={'fontsize': 11, 'fontweight': 'bold', 'color': 'navy'})
plt.show()
```

## Styling Returned Text Objects

Access and modify text objects after creation.

### 1. Style Percentage Labels

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%')

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

plt.show()
```

### 2. Different Colors per Slice

```python
colors = ['#e74c3c', '#3498db', '#9b59b6', '#f39c12', '#2ecc71']
text_colors = ['white', 'white', 'white', 'black', 'white']

fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%', colors=colors)

for autotext, color in zip(autotexts, text_colors):
    autotext.set_color(color)
    autotext.set_fontweight('bold')

plt.show()
```

### 3. Conditional Styling

```python
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(vals, labels=labels, autopct='%1.1f%%')

for autotext in autotexts:
    pct = float(autotext.get_text().replace('%', ''))
    if pct > 20:
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')
    else:
        autotext.set_fontsize(9)

plt.show()
```

## Combined with Explode

Percentage labels follow exploded slices.

### 1. Basic Explode

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=[0.1, 0, 0, 0, 0])
plt.show()
```

### 2. Multiple Exploded Slices

```python
fig, ax = plt.subplots()
ax.pie(vals, labels=labels, autopct='%1.1f%%', explode=[0.1, 0, 0.15, 0, 0.1])
plt.show()
```

### 3. Explode Comparison

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(vals, labels=labels, autopct='%1.1f%%')
axes[0].set_title('Without Explode')

axes[1].pie(vals, labels=labels, autopct='%1.1f%%', explode=[0.1, 0, 0.1, 0, 0])
axes[1].set_title('With Explode')

plt.tight_layout()
plt.show()
```

## Full Customization

Combine autopct with all other parameters.

### 1. Complete Example

```python
fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    vals,
    labels=labels,
    shadow=True,
    autopct='%1.1f%%',
    radius=1.3,
    explode=[0, 0, 0, 0.1, 0.15],
    startangle=90,
    counterclock=False
)
ax.set_title('Monthly Budget Distribution')
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
    explode=[0.05, 0, 0, 0.08, 0.1],
    startangle=90,
    pctdistance=0.6,
    labeldistance=1.15
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')
    autotext.set_fontsize(10)

ax.set_title('Monthly Budget Distribution', fontsize=14, fontweight='bold')
plt.show()
```

## Practical Applications

### 1. Sales Report

```python
def make_sales_autopct(values):
    def autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n(${val:,})'
    return autopct

sales = [45000, 32000, 28000, 15000]
regions = ['North', 'South', 'East', 'West']

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(sales, labels=regions, autopct=make_sales_autopct(sales),
       shadow=True, startangle=90)
ax.set_title('Regional Sales Distribution', fontsize=14)
plt.show()
```

### 2. Survey Results

```python
responses = [156, 89, 45, 23]
categories = ['Strongly Agree', 'Agree', 'Disagree', 'Strongly Disagree']

def survey_autopct(pct):
    total = sum(responses)
    count = int(round(pct * total / 100.0))
    return f'{pct:.0f}%\n(n={count})'

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(responses, labels=categories, autopct=survey_autopct, startangle=90)
ax.set_title('Customer Satisfaction Survey', fontsize=14)
plt.show()
```

### 3. Resource Allocation

```python
resources = [40, 25, 20, 15]
departments = ['Engineering', 'Marketing', 'Operations', 'Admin']
colors = ['#2ecc71', '#3498db', '#f39c12', '#9b59b6']

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    resources,
    labels=departments,
    colors=colors,
    autopct=lambda p: f'{p:.0f}%' if p > 10 else '',
    startangle=90,
    explode=[0.05, 0, 0, 0]
)

for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax.set_title('Budget Allocation by Department', fontsize=14)
plt.show()
```
