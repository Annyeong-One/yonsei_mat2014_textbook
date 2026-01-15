# pivot vs melt

`pivot` and `melt` are inverse operations for reshaping DataFrames between wide and long formats.

## Conceptual Relationship

pivot and melt transform data in opposite directions.

### 1. melt: Wide to Long

```python
import pandas as pd

# Wide format
wide = pd.DataFrame({
    'month': ['Jan', 'Feb'],
    'New York': [5, 3],
    'Los Angeles': [15, 17]
})
print("Wide format:")
print(wide)
```

```
  month  New York  Los Angeles
0   Jan         5           15
1   Feb         3           17
```

### 2. Apply melt

```python
long = pd.melt(
    wide,
    id_vars=['month'],
    var_name='city',
    value_name='temperature'
)
print("Long format (after melt):")
print(long)
```

```
  month         city  temperature
0   Jan     New York            5
1   Feb     New York            3
2   Jan  Los Angeles           15
3   Feb  Los Angeles           17
```

### 3. Apply pivot

```python
back_to_wide = long.pivot(
    index='month',
    columns='city',
    values='temperature'
)
print("Back to wide (after pivot):")
print(back_to_wide)
```

```
city   Los Angeles  New York
month                       
Feb             17         3
Jan             15         5
```

## When to Use Each

Guidelines for choosing between pivot and melt.

### 1. Use melt When

```python
# Converting columns to rows
# Preparing data for visualization (seaborn, plotly)
# Normalizing for database storage
# Input for groupby operations
```

### 2. Use pivot When

```python
# Creating summary tables
# Converting rows to columns
# Preparing data for comparison
# Creating cross-tabulation
```

### 3. Format Characteristics

| Format | Rows | Columns | Use Case |
|--------|------|---------|----------|
| Wide | Few | Many | Display, comparison |
| Long | Many | Few | Analysis, storage |

## Complete Round-trip

Transform and reverse without data loss.

### 1. Start with Wide

```python
original = pd.DataFrame({
    'product': ['A', 'B'],
    'Q1': [100, 150],
    'Q2': [200, 250]
})
```

### 2. Melt to Long

```python
long_form = original.melt(
    id_vars=['product'],
    var_name='quarter',
    value_name='sales'
)
```

### 3. Pivot Back to Wide

```python
wide_again = long_form.pivot(
    index='product',
    columns='quarter',
    values='sales'
).reset_index()

wide_again.columns.name = None  # Remove column name
```

## Practical Example

Temperature data transformation.

### 1. Original Wide Data

```python
temps = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-02'],
    'city_A': [20, 22],
    'city_B': [15, 17],
    'city_C': [25, 27]
})
```

### 2. Melt for Analysis

```python
temps_long = temps.melt(
    id_vars=['date'],
    var_name='city',
    value_name='temperature'
)

# Now can easily compute:
temps_long.groupby('city')['temperature'].mean()
```

### 3. Pivot for Display

```python
temps_wide = temps_long.pivot(
    index='date',
    columns='city',
    values='temperature'
)
# Good for side-by-side comparison
```

## Key Differences

Summary of differences.

### 1. Direction

```python
# melt: columns → rows (wide to long)
# pivot: rows → columns (long to wide)
```

### 2. Data Volume

```python
# melt: increases row count
# pivot: decreases row count (typically)
```

### 3. Required Parameters

```python
# melt: id_vars (optional), var_name, value_name
# pivot: index, columns, values
```
