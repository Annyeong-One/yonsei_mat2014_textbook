# Keyword - indicator

The `indicator` parameter adds a column showing the source of each row, useful for debugging and understanding merge results.

## Basic Usage

Add a column indicating merge source.

### 1. Enable Indicator

```python
import pandas as pd

df1 = pd.DataFrame({
    'city': ['NY', 'SF', 'LA'],
    'temperature': [21, 14, 35]
})

df2 = pd.DataFrame({
    'city': ['SF', 'NY', 'ICN'],
    'humidity': [65, 68, 75]
})

df = pd.merge(df1, df2, on='city', how='outer', indicator=True)
print(df)
```

```
  city  temperature  humidity      _merge
0   NY         21.0      68.0        both
1   SF         14.0      65.0        both
2   LA         35.0       NaN   left_only
3  ICN          NaN      75.0  right_only
```

### 2. Indicator Values

- `both`: Key exists in both DataFrames
- `left_only`: Key exists only in left DataFrame
- `right_only`: Key exists only in right DataFrame

### 3. Column Name

Default column name is `_merge`.

## Custom Column Name

Specify indicator column name.

### 1. String Value

```python
df = pd.merge(
    df1, df2,
    on='city',
    how='outer',
    indicator='source'
)
print(df['source'])
```

```
0          both
1          both
2     left_only
3    right_only
Name: source, dtype: object
```

### 2. Descriptive Name

```python
df = pd.merge(
    df1, df2,
    on='city',
    how='outer',
    indicator='merge_status'
)
```

### 3. Avoid Conflicts

```python
# Name must not conflict with existing columns
```

## Filtering by Indicator

Use indicator to filter results.

### 1. Find Unmatched Left

```python
df = pd.merge(df1, df2, on='city', how='outer', indicator=True)
unmatched_left = df[df['_merge'] == 'left_only']
print(unmatched_left)
```

```
  city  temperature  humidity     _merge
2   LA         35.0       NaN  left_only
```

### 2. Find Unmatched Right

```python
unmatched_right = df[df['_merge'] == 'right_only']
```

### 3. Find Matched Only

```python
matched = df[df['_merge'] == 'both']
```

## Data Quality Checks

Use indicator for merge validation.

### 1. Count Match Types

```python
df = pd.merge(df1, df2, on='key', how='outer', indicator=True)
print(df['_merge'].value_counts())
```

```
both          100
left_only      15
right_only     20
Name: _merge, dtype: int64
```

### 2. Validate Complete Match

```python
unmatched = df[df['_merge'] != 'both']
if len(unmatched) > 0:
    print(f"Warning: {len(unmatched)} unmatched rows")
```

### 3. Data Reconciliation

```python
# Identify missing records in each source
missing_in_right = df[df['_merge'] == 'left_only']['key']
missing_in_left = df[df['_merge'] == 'right_only']['key']
```

## Drop Indicator Column

Remove indicator after use.

### 1. Drop Column

```python
df = pd.merge(df1, df2, on='city', how='outer', indicator=True)
# Use indicator for filtering
matched_df = df[df['_merge'] == 'both'].drop('_merge', axis=1)
```

### 2. Chain Operations

```python
matched_df = (
    pd.merge(df1, df2, on='city', how='outer', indicator=True)
    .query("_merge == 'both'")
    .drop('_merge', axis=1)
)
```

### 3. Select Columns

```python
result = df[['city', 'temperature', 'humidity']]
```

## Practical Applications

Real-world uses for indicator.

### 1. Find New Records

```python
# Find records added since last sync
new_records = merged[merged['_merge'] == 'right_only']
```

### 2. Find Deleted Records

```python
# Find records removed since last sync
deleted_records = merged[merged['_merge'] == 'left_only']
```

### 3. Debug Merge Issues

```python
# Understand why rows are missing
if merged['_merge'].value_counts().get('left_only', 0) > expected:
    print("Investigate: too many unmatched left rows")
```
