# concat Method

The `concat()` function concatenates pandas objects along a particular axis, stacking DataFrames vertically or horizontally.

## Basic Usage

Concatenate DataFrames vertically.

### 1. Vertical Concatenation

```python
import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df1)

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print(df2)

df = pd.concat([df1, df2])
print(df)
```

```
   A  B
0  1  2
1  3  4
0  5  6
1  7  8
```

### 2. List of DataFrames

```python
pd.concat([df1, df2, df3, df4])
```

### 3. Index Preserved

Original indices are kept (may have duplicates).

## LeetCode Example: Friend Requests

Concatenate two columns into one Series.

### 1. Sample Data

```python
request_accepted = pd.DataFrame({
    'requester_id': [1, 2, 3, 4, 1, 2],
    'accepter_id': [2, 3, 4, 1, 3, 4]
})
```

### 2. Concatenate Columns

```python
combined_ids = pd.concat([
    request_accepted['requester_id'],
    request_accepted['accepter_id']
])
print(combined_ids)
```

```
0    1
1    2
2    3
3    4
4    1
5    2
0    2
1    3
2    4
3    1
4    3
5    4
dtype: int64
```

### 3. Count Occurrences

```python
friend_counts = combined_ids.value_counts()
```

## Horizontal Concatenation

Stack DataFrames side by side.

### 1. axis=1

```python
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('CD'))

dg = pd.concat([df1, df2], axis=1)
print(dg)
```

```
   A  B  C  D
0  1  2  5  6
1  3  4  7  8
```

### 2. Index Alignment

```python
# When indices differ, NaN fills missing values
```

### 3. Use join Parameter

```python
pd.concat([df1, df2], axis=1, join='inner')  # Only matching indices
```

## Handling Mismatched Columns

Concat with different column structures.

### 1. Union of Columns

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]})

result = pd.concat([df1, df2])
# Columns: A, B, C with NaN where missing
```

### 2. join='inner'

```python
result = pd.concat([df1, df2], join='inner')
# Only column B (common to both)
```

### 3. Specify Columns

```python
# Ensure same columns before concat
df2 = df2.reindex(columns=df1.columns)
```

## keys Parameter

Add hierarchical index to identify sources.

### 1. Label Sources

```python
result = pd.concat([df1, df2], keys=['first', 'second'])
```

### 2. MultiIndex Result

```python
print(result.index)
# MultiIndex([('first', 0), ('first', 1), ...])
```

### 3. Access by Key

```python
result.loc['first']  # Get first DataFrame's rows
```
