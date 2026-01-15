# pivot vs pivot_table

Both methods reshape data from long to wide format, but they have important differences in functionality and use cases.

## Key Differences

Summary of differences between pivot and pivot_table.

### 1. Duplicate Handling

```python
import pandas as pd

df = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-01', '2024-01-01'],
    'city': ['NY', 'NY', 'LA'],  # NY appears twice
    'temp': [30, 32, 70]
})

# pivot: fails with duplicates
# df.pivot(index='date', columns='city', values='temp')  # ValueError!

# pivot_table: aggregates duplicates
df.pivot_table(index='date', columns='city', values='temp', aggfunc='mean')
```

### 2. Aggregation Support

```python
# pivot: no aggregation
# pivot_table: aggfunc parameter for aggregation
```

### 3. Default Behavior

```python
# pivot: requires explicit values parameter
# pivot_table: can infer values from numeric columns
```

## Comparison Table

Side-by-side feature comparison.

### 1. Features

| Feature | pivot | pivot_table |
|---------|-------|-------------|
| Duplicates | Error | Aggregates |
| aggfunc | No | Yes |
| margins | No | Yes |
| fill_value | No | Yes |
| Multiple values | Manual | Automatic |

### 2. Syntax

```python
# pivot
df.pivot(index='row', columns='col', values='val')

# pivot_table
df.pivot_table(index='row', columns='col', values='val', aggfunc='mean')
```

### 3. Requirements

```python
# pivot: unique index-column combinations
# pivot_table: any data (aggregates if needed)
```

## When to Use Each

Guidelines for choosing.

### 1. Use pivot When

```python
# Data has unique index-column pairs
# No aggregation needed
# Simple reshape operation
df.pivot(index='date', columns='ticker', values='price')
```

### 2. Use pivot_table When

```python
# Data may have duplicates
# Aggregation is needed
# Need margins or fill_value
df.pivot_table(index='region', columns='product', values='sales', aggfunc='sum')
```

### 3. Default Choice

When in doubt, use pivot_table—it handles all cases.

## Example Comparison

Same data, different methods.

### 1. Unique Data

```python
# Both work the same
df_unique = pd.DataFrame({
    'date': ['Jan', 'Jan', 'Feb', 'Feb'],
    'city': ['NY', 'LA', 'NY', 'LA'],
    'sales': [100, 200, 150, 250]
})

# pivot
df_unique.pivot(index='date', columns='city', values='sales')

# pivot_table (same result)
df_unique.pivot_table(index='date', columns='city', values='sales')
```

### 2. Duplicate Data

```python
df_dup = pd.DataFrame({
    'date': ['Jan', 'Jan', 'Jan'],
    'city': ['NY', 'NY', 'LA'],  # NY duplicated
    'sales': [100, 120, 200]
})

# pivot: fails
# df_dup.pivot(...)  # ValueError

# pivot_table: aggregates
df_dup.pivot_table(index='date', columns='city', values='sales', aggfunc='mean')
# NY gets (100+120)/2 = 110
```

### 3. Multiple Aggregations

```python
# Only pivot_table supports this
df.pivot_table(
    index='date',
    columns='city',
    values='sales',
    aggfunc=['sum', 'mean', 'count']
)
```

## Performance

Considerations for large datasets.

### 1. Simple Cases

```python
# pivot is slightly faster for simple unique data
```

### 2. Complex Cases

```python
# pivot_table handles complexity better
```

### 3. Recommendation

Use the appropriate method for your data structure.
