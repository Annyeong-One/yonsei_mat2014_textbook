# MultiIndex Hierarchy

## Hierarchical Indexing

### 1. Definition

MultiIndex enables multiple index levels:

```python
import pandas as pd

arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]
index = pd.MultiIndex.from_arrays(arrays, names=['letter', 'number'])
s = pd.Series([10, 20, 30, 40], index=index)
```

### 2. From Tuples

```python
tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
index = pd.MultiIndex.from_tuples(tuples)
```

### 3. From Product

```python
index = pd.MultiIndex.from_product([['A', 'B'], [1, 2]])
```

## Accessing Data

### 1. Level Selection

```python
s['A']  # All entries with level 0 = 'A'
s['A', 1]  # Specific entry
```

### 2. Cross-section

```python
df = s.unstack()  # Pivot to DataFrame
# letter  A   B
# number       
# 1      10  30
# 2      20  40
```

### 3. Slicing

```python
s.loc[('A', 1):('B', 1)]  # Range
```

## DataFrame with MultiIndex

### 1. Rows and Columns

```python
df = pd.DataFrame(
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    index=pd.MultiIndex.from_tuples([('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]),
    columns=['col1', 'col2']
)
```

### 2. Selecting

```python
df.loc['A']  # All rows where first level = 'A'
df.loc[('A', 'x')]  # Specific row
```

### 3. Stacking

```python
stacked = df.stack()  # Add column as index level
unstacked = stacked.unstack()  # Remove level
```
