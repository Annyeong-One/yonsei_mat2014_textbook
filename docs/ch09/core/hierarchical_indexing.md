# Hierarchical Indexing

Hierarchical indexing (also called MultiIndex) enables you to store and manipulate data with multiple levels of indexing. This is essential for working with higher-dimensional data in a 2D DataFrame structure.

## Conceptual Overview

```
                        temperature  humidity
country  city                                
india    mumbai               32        70
         delhi                45        60
us       new york             21        68
         chicago              14        65
         ↑          ↑
      Level 0   Level 1
```

Hierarchical indexing allows you to:
- Represent 3D+ data in a 2D structure
- Perform grouped operations efficiently
- Select data at different levels of granularity

## Creating Hierarchical Indexes

### Using pd.concat with keys

```python
import pandas as pd

# Create separate DataFrames
india = pd.DataFrame({
    "city": ["mumbai", "delhi"],
    "temperature": [32, 45],
    "humidity": [70, 60],
}).set_index('city')

us = pd.DataFrame({
    "city": ["new york", "chicago"],
    "temperature": [21, 14],
    "humidity": [68, 65],
}).set_index('city')

# Concatenate with hierarchical keys
df = pd.concat([india, us], keys=["india", "us"])
print(df)
```

```
                  temperature  humidity
india mumbai              32        70
      delhi               45        60
us    new york            21        68
      chicago             14        65
```

### Using MultiIndex.from_tuples

```python
index = pd.MultiIndex.from_tuples([
    ('india', 'mumbai'),
    ('india', 'delhi'),
    ('us', 'new york'),
    ('us', 'chicago')
], names=['country', 'city'])

df = pd.DataFrame({
    'temperature': [32, 45, 21, 14],
    'humidity': [70, 60, 68, 65]
}, index=index)
```

### Using MultiIndex.from_product

Creates a MultiIndex from the Cartesian product of iterables.

```python
countries = ['india', 'us']
metrics = ['temperature', 'humidity']

index = pd.MultiIndex.from_product(
    [countries, metrics],
    names=['country', 'metric']
)
print(index)
```

```
MultiIndex([('india', 'temperature'),
            ('india', 'humidity'),
            ('us', 'temperature'),
            ('us', 'humidity')],
           names=['country', 'metric'])
```

### Using MultiIndex.from_arrays

```python
arrays = [
    ['india', 'india', 'us', 'us'],
    ['mumbai', 'delhi', 'new york', 'chicago']
]

index = pd.MultiIndex.from_arrays(arrays, names=['country', 'city'])
```

## Selecting Data with MultiIndex

### Using loc with Tuples (Recommended)

```python
df = pd.concat([india, us], keys=["india", "us"])

# Select specific country and city
print(df.loc[("us", "new york")])
```

```
temperature    21
humidity       68
Name: (us, new york), dtype: int64
```

### Selecting an Entire Level

```python
# Select all cities in 'us'
print(df.loc["us"])
```

```
          temperature  humidity
city                           
new york           21        68
chicago            14        65
```

### Avoid Chained Indexing

```python
# NOT RECOMMENDED - Chained indexing
df.loc["us"].loc["new york"]

# RECOMMENDED - Single tuple access
df.loc[("us", "new york")]
```

**Why avoid chained indexing?**
- `df.loc["us"]` creates an intermediate DataFrame
- pandas treats these as separate operations
- Can lead to unpredictable behavior with assignments
- Single tuple access is faster and clearer

## Hierarchical Columns

MultiIndex can also be applied to columns.

```python
df = pd.DataFrame(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    columns=pd.MultiIndex.from_product(
        [['one', 'two'], ['first', 'second']]
    )
)
print(df)
```

```
  one        two       
  first second first second
0     1      2     3      4
1     5      6     7      8
2     9     10    11     12
```

### Accessing Hierarchical Columns

```python
# Select top-level column group
print(df['one'])
```

```
   first  second
0      1       2
1      5       6
2      9      10
```

```python
# Select specific nested column - use tuple
print(df[('one', 'second')])
```

```
0     2
1     6
2    10
Name: (one, second), dtype: int64
```

### Avoid Chained Column Access

```python
# NOT RECOMMENDED
df['one']['second']

# RECOMMENDED
df.loc[:, ('one', 'second')]
```

## MultiIndex Operations

### Swapping Levels

```python
df = pd.concat([india, us], keys=["india", "us"])

# Swap the order of index levels
df_swapped = df.swaplevel()
print(df_swapped)
```

```
                  temperature  humidity
mumbai   india             32        70
delhi    india             45        60
new york us                21        68
chicago  us                14        65
```

### Sorting by Index

```python
# Sort by all levels
df_sorted = df.sort_index()

# Sort by specific level
df_sorted = df.sort_index(level='city')
```

### Resetting Index

```python
# Convert MultiIndex to columns
df_reset = df.reset_index()
print(df_reset)
```

```
  level_0    level_1  temperature  humidity
0   india     mumbai           32        70
1   india      delhi           45        60
2      us   new york           21        68
3      us    chicago           14        65
```

### Setting MultiIndex from Columns

```python
df_reset.set_index(['level_0', 'level_1'], inplace=True)
df_reset.index.names = ['country', 'city']
```

## Cross-Section Selection with xs

The `xs` method provides a convenient way to select data at a particular level.

```python
df = pd.concat([india, us], keys=["india", "us"])

# Select all rows where level 0 is 'india'
print(df.xs('india', level=0))
```

```
        temperature  humidity
city                         
mumbai           32        70
delhi            45        60
```

```python
# Select all rows where city is 'delhi' (level 1)
print(df.xs('delhi', level=1))
```

```
         temperature  humidity
country                       
india             45        60
```

## Aggregation with MultiIndex

### GroupBy on Index Levels

```python
# Aggregate by country (level 0)
print(df.groupby(level=0).mean())
```

```
         temperature  humidity
country                       
india           38.5      65.0
us              17.5      66.5
```

### Using level parameter in aggregations

```python
# Sum across level 0
print(df.sum(level=0))  # Deprecated in newer pandas

# Modern approach
print(df.groupby(level=0).sum())
```

## Financial Example: Multi-Asset Time Series

```python
import pandas as pd
import numpy as np

# Create multi-asset price data
dates = pd.date_range('2024-01-01', periods=5)
assets = ['AAPL', 'MSFT']
metrics = ['open', 'high', 'low', 'close']

# Create MultiIndex columns
columns = pd.MultiIndex.from_product([assets, metrics])

# Random price data
np.random.seed(42)
data = np.random.randn(5, 8).cumsum(axis=0) + 100

df = pd.DataFrame(data, index=dates, columns=columns)
print(df.round(2))
```

```
            AAPL                          MSFT                        
            open   high    low  close     open   high    low  close
2024-01-01 100.50 100.86 101.51 103.02  100.31  99.85  99.38 100.95
2024-01-02 101.27 100.58 101.99 103.81  100.82 100.00  99.97 101.12
...
```

### Selecting Asset Data

```python
# Get all AAPL data
aapl_data = df['AAPL']

# Get close prices for all assets
close_prices = df.xs('close', level=1, axis=1)
print(close_prices)
```

## Index Attributes

### names

```python
df = pd.concat([india, us], keys=["india", "us"])
print(df.index.names)  # [None, 'city']

# Set names
df.index.names = ['country', 'city']
```

### levels

```python
print(df.index.levels)
# FrozenList([['india', 'us'], ['chicago', 'delhi', 'mumbai', 'new york']])
```

### nlevels

```python
print(df.index.nlevels)  # 2
```

## Best Practices

1. **Use tuple indexing** instead of chained indexing for clarity and performance
2. **Name your index levels** for self-documenting code
3. **Sort the index** after creation for better performance with `loc`
4. **Consider alternatives** - sometimes separate columns are clearer than MultiIndex
5. **Use xs()** for cleaner cross-section selection

```python
# Good: Clear, named, sorted MultiIndex
df.index.names = ['country', 'city']
df = df.sort_index()
result = df.loc[('us', 'chicago'), 'temperature']

# Avoid: Unnamed, unsorted, chained access
result = df.loc['us'].loc['chicago']['temperature']
```
