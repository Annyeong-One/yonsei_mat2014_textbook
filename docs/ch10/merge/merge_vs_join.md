# merge vs join

pandas provides two methods for combining DataFrames: `merge()` and `join()`. Understanding their differences is essential for data wrangling.

## Key Differences

merge and join serve different purposes.

### 1. merge Uses Columns

```python
import pandas as pd

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['A', 'B', 'D'],
    'value2': [4, 5, 6]
})

# merge on column
pd.merge(df1, df2, on='key')
```

### 2. join Uses Index

```python
df1 = pd.DataFrame({
    'value1': [1, 2, 3]
}, index=['A', 'B', 'C'])

df2 = pd.DataFrame({
    'value2': [4, 5, 6]
}, index=['A', 'B', 'D'])

# join on index
df1.join(df2)
```

### 3. Comparison Table

| Feature | merge | join |
|---------|-------|------|
| Join key | Column values | Index labels |
| Syntax | `pd.merge(df1, df2)` | `df1.join(df2)` |
| Default | Inner join | Left join |
| Flexibility | More options | Simpler API |

## When to Use merge

Choose merge for column-based joins.

### 1. Foreign Key Relationships

```python
orders = pd.DataFrame({
    'order_id': [1, 2, 3],
    'customer_id': [101, 102, 101],
    'amount': [100, 200, 150]
})

customers = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'name': ['Alice', 'Bob', 'Carol']
})

pd.merge(orders, customers, on='customer_id')
```

### 2. Different Column Names

```python
pd.merge(df1, df2, left_on='id', right_on='customer_id')
```

### 3. Multiple Join Keys

```python
pd.merge(df1, df2, on=['key1', 'key2'])
```

## When to Use join

Choose join for index-based operations.

### 1. Time Series Alignment

```python
import yfinance as yf

aapl = yf.Ticker('AAPL').history(period='1y')[['Close']].rename(
    columns={'Close': 'AAPL'}
)
msft = yf.Ticker('MSFT').history(period='1y')[['Close']].rename(
    columns={'Close': 'MSFT'}
)

portfolio = aapl.join(msft, how='inner')
```

### 2. Multiple DataFrames

```python
# Join multiple DataFrames by index
df1.join([df2, df3, df4])
```

### 3. Suffix Handling

```python
df1.join(df2, lsuffix='_left', rsuffix='_right')
```

## Four Join Types

Both methods support the same join types.

### 1. Inner Join

```python
pd.merge(df1, df2, on='key', how='inner')  # Only matching
df1.join(df2, how='inner')
```

### 2. Left Join

```python
pd.merge(df1, df2, on='key', how='left')   # All from left
df1.join(df2, how='left')  # Default for join
```

### 3. Right Join

```python
pd.merge(df1, df2, on='key', how='right')  # All from right
df1.join(df2, how='right')
```

### 4. Outer Join

```python
pd.merge(df1, df2, on='key', how='outer')  # All rows
df1.join(df2, how='outer')
```

## Visual Comparison

Four ways of combining two DataFrames.

### 1. Sample DataFrames

```python
df1 = pd.DataFrame({'city': ['NY', 'SF', 'LA'], 'temp': [21, 14, 35]})
df2 = pd.DataFrame({'city': ['SF', 'NY', 'ICN'], 'humidity': [65, 68, 75]})
```

### 2. Inner (Intersection)

```python
pd.merge(df1, df2, on='city', how='inner')
# Only NY and SF
```

### 3. Outer (Union)

```python
pd.merge(df1, df2, on='city', how='outer')
# NY, SF, LA, ICN (with NaN for missing)
```

## Practical Guidelines

Choose the right method for your use case.

### 1. Use merge When

- Joining on column values (foreign keys)
- Column names differ between DataFrames
- Need fine-grained control over join

### 2. Use join When

- DataFrames share a meaningful index
- Combining time series data
- Simple index-based combination

### 3. Performance

Both methods have similar performance; choose based on data structure.
