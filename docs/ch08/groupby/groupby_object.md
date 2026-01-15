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
