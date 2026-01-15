# apply with axis

The `axis` parameter in `apply()` determines whether the function is applied along rows or columns. Understanding axis behavior is crucial for correct DataFrame operations.

## axis=0 Column-wise

Apply function to each column (default behavior).

### 1. Default Behavior

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

result = df.apply(np.sum, axis=0)
print(result)
```

```
A     6
B    15
C    24
dtype: int64
```

### 2. Custom Function

```python
def column_stats(col):
    return pd.Series({
        'mean': col.mean(),
        'std': col.std(),
        'min': col.min(),
        'max': col.max()
    })

df.apply(column_stats, axis=0)
```

### 3. Column Normalization

```python
df.apply(lambda col: (col - col.mean()) / col.std(), axis=0)
```

## axis=1 Row-wise

Apply function to each row.

### 1. Row Sum

```python
result = df.apply(np.sum, axis=1)
print(result)
```

```
0    12
1    15
2    18
dtype: int64
```

### 2. Row Maximum

```python
df.apply(lambda row: row.max(), axis=1)
```

### 3. Conditional Row Logic

```python
df.apply(
    lambda row: 'High' if row['A'] > 2 else 'Low',
    axis=1
)
```

## Multiple Column Operations

Common patterns using axis=1.

### 1. Weighted Calculation

```python
df = pd.DataFrame({
    'quantity': [10, 20, 30],
    'price': [100, 200, 150],
    'discount': [0.1, 0.2, 0.15]
})

df['total'] = df.apply(
    lambda row: row['quantity'] * row['price'] * (1 - row['discount']),
    axis=1
)
```

### 2. String Concatenation

```python
df = pd.DataFrame({
    'first_name': ['John', 'Jane'],
    'last_name': ['Doe', 'Smith']
})

df['full_name'] = df.apply(
    lambda row: f"{row['first_name']} {row['last_name']}",
    axis=1
)
```

### 3. Conditional Assignment

```python
df['status'] = df.apply(
    lambda row: 'Pass' if row['score'] >= 60 else 'Fail',
    axis=1
)
```

## result_type Parameter

Control the output format when applying row-wise.

### 1. result_type='expand'

```python
def extract_parts(row):
    return [row['A'], row['B'], row['A'] + row['B']]

df.apply(extract_parts, axis=1, result_type='expand')
```

Returns a DataFrame with columns 0, 1, 2.

### 2. result_type='reduce'

```python
# Return a Series (default)
df.apply(lambda row: row.sum(), axis=1, result_type='reduce')
```

### 3. result_type='broadcast'

```python
# Same shape as original DataFrame
df.apply(lambda row: row - row.mean(), axis=1, result_type='broadcast')
```

## LeetCode Example: Quality Metrics

Calculate metrics with groupby and apply.

### 1. Sample Data

```python
queries = pd.DataFrame({
    'query_name': ['Query1', 'Query1', 'Query2', 'Query2'],
    'rating': [5, 4, 3, 2],
    'position': [2, 1, 3, 2]
})

queries['quality'] = queries['rating'] / queries['position']
queries['poor_query'] = (queries['rating'] < 3).astype(int) * 100
```

### 2. Round Function

```python
round2 = lambda x: round(x, 2)

result = (queries
    .groupby('query_name')[['quality', 'poor_query']]
    .mean()
    .apply(round2)
    .reset_index())
print(result)
```

### 3. Result

```
  query_name  quality  poor_query
0     Query1     3.25        0.00
1     Query2     1.00       50.00
```

## Performance Comparison

Row-wise apply vs vectorized operations.

### 1. Slow Row-wise

```python
%%timeit
df.apply(lambda row: row['A'] + row['B'], axis=1)
```

### 2. Fast Vectorized

```python
%%timeit
df['A'] + df['B']
```

### 3. When to Use axis=1

- Complex conditional logic
- Operations requiring multiple columns
- Non-vectorizable custom functions
