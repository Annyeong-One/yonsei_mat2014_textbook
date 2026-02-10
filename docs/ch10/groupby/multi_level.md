# Multi-Level Grouping

Group by multiple columns to create hierarchical aggregations.

## Basic Multi-Level

Group by multiple columns.

### 1. Two-Level Grouping

```python
import pandas as pd

df = pd.DataFrame({
    'region': ['East', 'East', 'West', 'West'],
    'product': ['A', 'B', 'A', 'B'],
    'sales': [100, 150, 200, 250]
})

result = df.groupby(['region', 'product'])['sales'].sum()
print(result)
```

```
region  product
East    A          100
        B          150
West    A          200
        B          250
Name: sales, dtype: int64
```

### 2. MultiIndex Result

The result has a hierarchical index.

### 3. Access Levels

```python
result['East']      # All products in East
result['East', 'A']  # Specific combination
```

## reset_index

Flatten the hierarchical result.

### 1. Convert to DataFrame

```python
result = df.groupby(['region', 'product'])['sales'].sum().reset_index()
print(result)
```

```
  region product  sales
0   East       A    100
1   East       B    150
2   West       A    200
3   West       B    250
```

### 2. as_index=False

```python
df.groupby(['region', 'product'], as_index=False)['sales'].sum()
```

### 3. Equivalent Results

Both approaches produce a flat DataFrame.

## Aggregations with Multiple Columns

Apply aggregations to grouped data.

### 1. Single Aggregation

```python
df.groupby(['region', 'product']).agg({'sales': 'sum'})
```

### 2. Multiple Aggregations

```python
df.groupby(['region', 'product']).agg({
    'sales': ['sum', 'mean', 'count']
})
```

### 3. Named Aggregations

```python
df.groupby(['region', 'product']).agg(
    total_sales=('sales', 'sum'),
    avg_sales=('sales', 'mean')
)
```

## unstack Method

Reshape grouped results.

### 1. Basic unstack

```python
result = df.groupby(['region', 'product'])['sales'].sum().unstack()
print(result)
```

```
product    A    B
region           
East     100  150
West     200  250
```

### 2. Pivot-like Output

unstack moves inner index level to columns.

### 3. Fill Missing

```python
result.unstack(fill_value=0)
```

## Practical Example

Financial sector analysis.

### 1. Sample Data

```python
df = pd.DataFrame({
    'sector': ['Tech', 'Tech', 'Finance', 'Finance'],
    'ticker': ['AAPL', 'MSFT', 'JPM', 'GS'],
    'per': [25.5, 30.2, 12.1, 10.8],
    'market_cap': [2800, 2400, 450, 120]
})
```

### 2. Grouped Statistics

```python
stats = df.groupby('sector').agg({
    'per': ['mean', 'min', 'max'],
    'market_cap': 'sum'
})
print(stats)
```

### 3. Reset and Flatten

```python
stats.columns = ['_'.join(col) for col in stats.columns]
stats = stats.reset_index()
```
