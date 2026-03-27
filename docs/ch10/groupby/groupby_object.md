# GroupBy Object

The `groupby()` method creates a GroupBy object that represents a collection of DataFrame groups. It enables split-apply-combine operations.

## Creating GroupBy

Group a DataFrame by one or more columns.

### 1. Basic GroupBy

```python
import pandas as pd

data = {
    'day': ['1/1/20', '1/2/20', '1/1/20', '1/2/20', '1/1/20', '1/2/20'],
    'city': ['NY', 'NY', 'SF', 'SF', 'LA', 'LA'],
    'temperature': [21, 14, 25, 32, 36, 42],
    'humidity': [31, 15, 36, 22, 16, 29],
}
df = pd.DataFrame(data)
print(df)

dg = df.groupby("city")
print(dg)
```

```
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x...>
```

### 2. Lazy Evaluation

GroupBy object is lazy; no computation until aggregation.

### 3. Multiple Columns

```python
df.groupby(['city', 'day'])
```

## GroupBy Properties

Access information about groups.

### 1. Number of Groups

```python
print(dg.ngroups)  # 3 (NY, SF, LA)
```

### 2. Group Keys

```python
print(dg.groups.keys())  # dict_keys(['LA', 'NY', 'SF'])
```

### 3. Group Sizes

```python
print(dg.size())
```

```
city
LA    2
NY    2
SF    2
dtype: int64
```

## Split-Apply-Combine

The GroupBy paradigm.

### 1. Split

```python
# Data is split into groups based on key
# NY: rows 0, 1
# SF: rows 2, 3
# LA: rows 4, 5
```

### 2. Apply

```python
# A function is applied to each group
dg['temperature'].mean()
```

### 3. Combine

```python
# Results are combined into a new structure
```

```
city
LA    39.0
NY    17.5
SF    28.5
Name: temperature, dtype: float64
```

## Selecting Columns

Select specific columns from GroupBy.

### 1. Single Column

```python
dg['temperature']  # SeriesGroupBy
```

### 2. Multiple Columns

```python
dg[['temperature', 'humidity']]  # DataFrameGroupBy
```

### 3. Apply Aggregation

```python
dg['temperature'].mean()
dg[['temperature', 'humidity']].mean()
```

## as_index Parameter

Control index in result.

### 1. Default (as_index=True)

```python
df.groupby('city')['temperature'].mean()
# city is the index
```

### 2. as_index=False

```python
df.groupby('city', as_index=False)['temperature'].mean()
# city is a column
```

### 3. Equivalent to reset_index

```python
df.groupby('city')['temperature'].mean().reset_index()
```

---

## Runnable Example: `groupby_tutorial.py`

```python
"""
Pandas Tutorial: GroupBy and Aggregation.

Covers groupby operations, aggregation functions, and split-apply-combine.
"""

import pandas as pd
import numpy as np

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*70)
    print("GROUPBY AND AGGREGATION")
    print("="*70)

    # Create sample sales data
    np.random.seed(42)
    df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=20, freq='D'),
        'Product': np.random.choice(['A', 'B', 'C'], 20),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 20),
        'Sales': np.random.randint(100, 1000, 20),
        'Quantity': np.random.randint(1, 20, 20)
    })

    print("\nSample Data:")
    print(df.head(10))

    # Basic GroupBy
    print("\n1. Group by Product and calculate mean:")
    print(df.groupby('Product')['Sales'].mean())

    print("\n2. Group by multiple columns:")
    print(df.groupby(['Product', 'Region'])['Sales'].sum())

    # Multiple aggregations
    print("\n3. Multiple aggregation functions:")
    print(df.groupby('Product').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Quantity': ['sum', 'mean']
    }))

    # Custom aggregation
    print("\n4. Custom aggregation function:")
    print(df.groupby('Product')['Sales'].agg(['sum', 'mean', lambda x: x.max() - x.min()]))

    # Filter groups
    print("\n5. Filter groups (sales > 5000):")
    high_sales = df.groupby('Product').filter(lambda x: x['Sales'].sum() > 5000)
    print(high_sales)

    # Transform
    print("\n6. Transform - normalize within groups:")
    df['Sales_Normalized'] = df.groupby('Product')['Sales'].transform(lambda x: (x - x.mean()) / x.std())
    print(df[['Product', 'Sales', 'Sales_Normalized']].head())

    # Apply custom function
    print("\n7. Apply custom function to groups:")
    def get_stats(group):
        return pd.Series({
            'total': group['Sales'].sum(),
            'avg': group['Sales'].mean(),
            'transactions': len(group)
        })

    print(df.groupby('Product').apply(get_stats))

    print("\nKEY TAKEAWAYS:")
    print("- Use groupby() to split data into groups")
    print("- Common aggregations: sum(), mean(), count(), min(), max()")
    print("- agg() for multiple functions")
    print("- filter() to select groups")
    print("- transform() to broadcast results back")
    print("- apply() for custom group-wise operations")
```
