# Index Objects

Index objects provide axis labels for pandas data structures. Understanding indexes is fundamental to effective pandas usage.

## Index Purpose

Index serves as an immutable container for axis labels.

### 1. Label Container

```python
import pandas as pd

idx = pd.Index(['a', 'b', 'c', 'd'])
s = pd.Series([10, 20, 30, 40], index=idx)
print(s)
```

```
a    10
b    20
c    30
d    40
dtype: int64
```

### 2. Immutability

Indexes cannot be modified in place:

```python
idx = pd.Index(['a', 'b', 'c'])
# idx[0] = 'x'  # TypeError: Index does not support mutable operations
```

### 3. Index Types

```python
pd.Index         # Generic index
pd.RangeIndex    # Memory-efficient integer range
pd.DatetimeIndex # Datetime labels
pd.MultiIndex    # Hierarchical index
pd.CategoricalIndex  # Categorical data
```

## Index Operations

Index supports set-like operations for data alignment.

### 1. Set Union

```python
idx1 = pd.Index(['a', 'b', 'c'])
idx2 = pd.Index(['b', 'c', 'd'])

print(idx1.union(idx2))
# Index(['a', 'b', 'c', 'd'], dtype='object')
```

### 2. Set Intersection

```python
print(idx1.intersection(idx2))
# Index(['b', 'c'], dtype='object')
```

### 3. Set Difference

```python
print(idx1.difference(idx2))
# Index(['a'], dtype='object')
```

## Automatic Alignment

pandas automatically aligns data based on index labels during operations.

### 1. Series Alignment

```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20], index=['b', 'c'])
result = s1 + s2
print(result)
```

```
a     NaN
b    12.0
c    23.0
dtype: float64
```

### 2. DataFrame Alignment

```python
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'A': [10, 20]}, index=['y', 'z'])
print(df1 + df2)
```

### 3. Fill Value

```python
result = s1.add(s2, fill_value=0)
```

## Reindexing

Change the index of a Series or DataFrame with `reindex`.

### 1. Basic Reindexing

```python
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s_new = s.reindex(['a', 'b', 'c', 'd'])
print(s_new)
```

```
a    1.0
b    2.0
c    3.0
d    NaN
dtype: float64
```

### 2. Fill Missing Values

```python
s_new = s.reindex(['a', 'b', 'c', 'd'], fill_value=0)
```

### 3. Forward Fill

```python
s_new = s.reindex(['a', 'b', 'c', 'd'], method='ffill')
```

## RangeIndex

Default integer index optimized for memory efficiency.

### 1. Automatic Creation

```python
s = pd.Series([10, 20, 30])
print(s.index)
# RangeIndex(start=0, stop=3, step=1)
```

### 2. Reset Index

```python
df = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df_reset = df.reset_index(drop=True)
print(df_reset.index)
# RangeIndex(start=0, stop=3, step=1)
```

### 3. Memory Efficiency

RangeIndex stores only start, stop, and step, not individual values.
