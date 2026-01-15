# Index Objects

## Index Purpose

### 1. Label Container

Index provides axis labels:

```python
import pandas as pd

idx = pd.Index(['a', 'b', 'c', 'd'])
s = pd.Series([10, 20, 30, 40], index=idx)
```

### 2. Immutability

Indexes are immutable:

```python
idx = pd.Index(['a', 'b', 'c'])
# idx[0] = 'x'  # TypeError
```

### 3. Types

```python
pd.Index        # Generic
pd.RangeIndex   # Efficient range
pd.DatetimeIndex  # Datetime labels
pd.MultiIndex   # Hierarchical
```

## Index Operations

### 1. Set Operations

```python
idx1 = pd.Index(['a', 'b', 'c'])
idx2 = pd.Index(['b', 'c', 'd'])

print(idx1.union(idx2))  # ['a', 'b', 'c', 'd']
print(idx1.intersection(idx2))  # ['b', 'c']
print(idx1.difference(idx2))  # ['a']
```

### 2. Alignment

```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20], index=['b', 'c'])
result = s1 + s2  # Aligns on index
```

### 3. Reindexing

```python
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s_new = s.reindex(['a', 'b', 'c', 'd'], fill_value=0)
```

## Datetime Index

### 1. Creation

```python
dates = pd.date_range('2023-01-01', periods=5)
s = pd.Series([10, 20, 30, 40, 50], index=dates)
```

### 2. Selection

```python
s['2023-01-01']  # Single date
s['2023-01-02':'2023-01-04']  # Range
```

### 3. Frequency

```python
dates = pd.date_range('2023-01-01', periods=10, freq='D')
```
