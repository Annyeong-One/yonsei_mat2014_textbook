# Series vs DataFrame

Understanding the relationship between Series and DataFrame is fundamental to working effectively with pandas. This document clarifies when to use each and how they interact.

## Structural Comparison

```
┌─────────────────────────────────────────────────────────────┐
│                        DataFrame                             │
│  ┌─────────┬─────────┬─────────┬─────────┐                  │
│  │ Series  │ Series  │ Series  │ Series  │  ← Columns       │
│  │ (col A) │ (col B) │ (col C) │ (col D) │                  │
│  ├─────────┼─────────┼─────────┼─────────┤                  │
│  │   1.0   │  'foo'  │  True   │  100    │  ← Row 0        │
│  │   2.0   │  'bar'  │  False  │  200    │  ← Row 1        │
│  │   3.0   │  'baz'  │  True   │  300    │  ← Row 2        │
│  └─────────┴─────────┴─────────┴─────────┘                  │
│      ↑          ↑          ↑          ↑                      │
│   float64    object      bool      int64    ← dtype per col │
└─────────────────────────────────────────────────────────────┘
```

| Aspect | Series | DataFrame |
|--------|--------|-----------|
| Dimensions | 1D (single column) | 2D (multiple columns) |
| Data types | Single dtype | Different dtype per column |
| Analogy | Excel column | Excel spreadsheet |
| NumPy equivalent | 1D array | 2D array (but heterogeneous) |

## Type Transitions

Understanding how operations change the type is crucial.

### DataFrame to Series

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Single column selection -> Series
col_a = df['A']
print(type(col_a))  # <class 'pandas.core.series.Series'>

# Single row selection -> Series
row_0 = df.iloc[0]
print(type(row_0))  # <class 'pandas.core.series.Series'>

# Aggregation -> Series
col_means = df.mean()
print(type(col_means))  # <class 'pandas.core.series.Series'>
```

### Preserving DataFrame Type

```python
# Double brackets preserve DataFrame
col_a_df = df[['A']]
print(type(col_a_df))  # <class 'pandas.core.frame.DataFrame'>
print(col_a_df.shape)  # (3, 1)

# Multiple column selection -> DataFrame
subset = df[['A', 'B']]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

### Series to DataFrame

```python
s = pd.Series([1, 2, 3], name='values')

# to_frame() method
df = s.to_frame()
print(type(df))  # <class 'pandas.core.frame.DataFrame'>

# reset_index() also creates DataFrame
df = s.reset_index()
print(df.columns)  # Index(['index', 'values'])
```

## Shape Differences

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Full DataFrame
print(df.shape)                  # (891, 12)

# Multiple columns -> DataFrame
print(df[["Survived", "Sex"]].shape)  # (891, 2)

# Single column with double brackets -> DataFrame
print(df[["Survived"]].shape)    # (891, 1)

# Single column with single brackets -> Series
print(df["Survived"].shape)      # (891,) - Note: 1D tuple
```

## Access Patterns

### Equivalent Operations

| Operation | DataFrame Syntax | Series Syntax |
|-----------|------------------|---------------|
| Get element | `df.loc[row, col]` | `s[label]` or `s.loc[label]` |
| Get by position | `df.iloc[i, j]` | `s.iloc[i]` |
| Boolean filter | `df[df['A'] > 0]` | `s[s > 0]` |
| Get values | `df.values` | `s.values` |

### Column-wise vs Element-wise

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# DataFrame aggregation is column-wise by default
print(df.sum())
# A     6
# B    15
# dtype: int64

s = pd.Series([1, 2, 3])

# Series aggregation is element-wise
print(s.sum())  # 6
```

## Method Behavior Differences

### Aggregations

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
s = pd.Series([1, 2, 3])

# DataFrame.mean() returns Series (one value per column)
print(df.mean())
# A    2.0
# B    5.0
# dtype: float64

# Series.mean() returns scalar
print(s.mean())  # 2.0
```

### Apply Behavior

```python
# DataFrame apply works on columns (axis=0) or rows (axis=1)
df.apply(sum, axis=0)  # Sum each column
df.apply(sum, axis=1)  # Sum each row

# Series apply works element-wise
s.apply(lambda x: x ** 2)  # Square each element
```

## Common Conversion Patterns

### Aggregation Results

```python
# groupby returns Series by default
result = df.groupby('category')['value'].sum()
print(type(result))  # Series

# Convert to DataFrame with reset_index
result_df = df.groupby('category')['value'].sum().reset_index()
print(type(result_df))  # DataFrame

# Or use to_frame with custom column name
result_df = df.groupby('category')['value'].sum().to_frame(name='total')
```

### Value Counts

```python
s = pd.Series(['a', 'b', 'a', 'c', 'a', 'b'])

# value_counts returns Series
counts = s.value_counts()
print(type(counts))  # Series

# Convert to DataFrame
counts_df = s.value_counts().reset_index()
counts_df.columns = ['value', 'count']
```

## Practical Guidelines

### When to Use Series

1. Working with a single variable
2. Time series of one measurement
3. Result of column extraction
4. Input to plotting functions expecting 1D data

```python
# Time series analysis
prices = df['Close']  # Series
returns = prices.pct_change()
rolling_mean = prices.rolling(20).mean()
```

### When to Use DataFrame

1. Multiple variables that should stay aligned
2. Tabular data with different column types
3. Data requiring row-wise operations
4. Input/output for file operations

```python
# Multi-asset analysis
portfolio = df[['AAPL', 'MSFT', 'GOOGL']]  # DataFrame
correlations = portfolio.corr()
portfolio_returns = portfolio.pct_change()
```

### Avoiding Common Mistakes

```python
# WRONG: Expecting DataFrame, getting Series
col = df['price']  # This is a Series!
col.columns  # AttributeError: 'Series' object has no attribute 'columns'

# RIGHT: Keep as DataFrame if needed
col = df[['price']]  # This is a DataFrame
col.columns  # Index(['price'], dtype='object')

# WRONG: Chained assignment warning
df[df['A'] > 0]['B'] = 1  # May not work as expected

# RIGHT: Use loc for assignment
df.loc[df['A'] > 0, 'B'] = 1
```

## Performance Considerations

| Operation | Series | DataFrame |
|-----------|--------|-----------|
| Memory | Lower (single dtype) | Higher (metadata per column) |
| Iteration | Faster | Slower |
| Vectorized ops | Optimal | Optimal |
| Type consistency | Guaranteed | Per-column |

For large-scale numerical operations, extracting to NumPy arrays may provide additional performance benefits:

```python
# Extract for numerical operations
arr = df['price'].values  # NumPy array
result = np.sqrt(arr)     # Fast NumPy operation

# Put back into pandas if needed
df['price_sqrt'] = result
```
