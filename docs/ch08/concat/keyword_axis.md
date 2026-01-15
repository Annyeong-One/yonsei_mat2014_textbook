# Keyword - axis

The `axis` parameter determines whether to concatenate along rows (vertically) or columns (horizontally).

## axis=0 Vertical

Stack DataFrames on top of each other.

### 1. Default Behavior

```python
import pandas as pd

df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))

df = pd.concat([df1, df2])
print("axis = 0 (default): append top-down using index")
print(df)
```

```
   A  B
0  1  2
1  3  4
0  5  6
1  7  8
```

### 2. Row Count Increases

```python
print(len(df))  # 4 (2 + 2)
```

### 3. Index Concatenation

Row indices from both DataFrames are preserved.

## axis=1 Horizontal

Stack DataFrames side by side.

### 1. Horizontal Concatenation

```python
dg = pd.concat([df1, df2], axis=1)
print("axis = 1: append left-right using columns")
print(dg)
```

```
   A  B  A  B
0  1  2  5  6
1  3  4  7  8
```

### 2. Column Count Increases

```python
print(len(dg.columns))  # 4 (2 + 2)
```

### 3. Index Alignment

Rows are aligned by index; unmatched indices get NaN.

## Index Alignment Behavior

How indices are handled differs by axis.

### 1. Different Row Indices

```python
df1 = pd.DataFrame({'A': [1, 2]}, index=[0, 1])
df2 = pd.DataFrame({'B': [3, 4]}, index=[1, 2])

# axis=1 aligns on index
result = pd.concat([df1, df2], axis=1)
print(result)
```

```
     A    B
0  1.0  NaN
1  2.0  3.0
2  NaN  4.0
```

### 2. Different Columns

```python
df1 = pd.DataFrame({'A': [1], 'B': [2]})
df2 = pd.DataFrame({'B': [3], 'C': [4]})

# axis=0 creates union of columns
result = pd.concat([df1, df2])
print(result)
```

```
     A  B    C
0  1.0  2  NaN
0  NaN  3  4.0
```

### 3. Use join Parameter

```python
pd.concat([df1, df2], axis=0, join='inner')  # Only common columns
pd.concat([df1, df2], axis=1, join='inner')  # Only common indices
```

## Practical Examples

Common concatenation patterns.

### 1. Stack Multiple Files

```python
# Load and stack CSV files
dfs = [pd.read_csv(f'data_{year}.csv') for year in range(2020, 2024)]
combined = pd.concat(dfs, axis=0, ignore_index=True)
```

### 2. Add Calculated Columns

```python
original = pd.DataFrame({'A': [1, 2, 3]})
calculated = pd.DataFrame({'B': [10, 20, 30]})

result = pd.concat([original, calculated], axis=1)
```

### 3. Build Wide DataFrame

```python
# Combine time series side by side
prices = pd.concat([aapl, msft, googl], axis=1)
prices.columns = ['AAPL', 'MSFT', 'GOOGL']
```
