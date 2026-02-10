# DataFrame Architecture

## Columnar Design

### 1. Structure

DataFrame is a dict-like container of Series:

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.0, 5.0, 6.0],
    'C': ['x', 'y', 'z']
})
```

### 2. Columns as Series

```python
col_a = df['A']
print(type(col_a))  # Series
print(col_a.dtype)  # int64

col_c = df['C']
print(col_c.dtype)  # object
```

### 3. Heterogeneous Types

Each column has its own dtype:

```python
print(df.dtypes)
# A     int64
# B   float64
# C    object
```

## Construction

### 1. From Dict

```python
data = {
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'salary': [50000, 60000]
}
df = pd.DataFrame(data)
```

### 2. From Lists

```python
data = [
    [1, 4, 'x'],
    [2, 5, 'y'],
    [3, 6, 'z']
]
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
```

### 3. From Records

```python
df = pd.DataFrame([
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
])
```

## Indexing

### 1. Column Selection

```python
df['A']          # Single column (Series)
df[['A', 'B']]   # Multiple columns (DataFrame)
```

### 2. Row Selection

```python
df.loc[0]        # By label
df.iloc[0]       # By position
df.loc[0:2]      # Slice by label
```

### 3. Boolean Indexing

```python
df[df['age'] > 25]  # Filter rows
```

## Operations

### 1. Column-wise

```python
df['D'] = df['A'] + df['B']  # New column
df.drop('D', axis=1, inplace=True)  # Remove column
```

### 2. Row-wise

```python
df.loc[3] = [4, 7, 'w']  # Add row
df = df.drop(3)  # Remove row
```

### 3. Aggregation

```python
df.sum()      # Sum each column
df.mean()     # Mean each column
df.describe() # Summary statistics
```
