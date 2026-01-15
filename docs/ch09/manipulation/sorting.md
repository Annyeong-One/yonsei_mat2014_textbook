# Sorting by Index and Values

pandas provides methods to sort DataFrames and Series by their index labels or column values.

## sort_index Method

Sort by row or column labels.

### 1. Sort Rows by Index

```python
import pandas as pd

df = pd.DataFrame({
    'A': [3, 1, 2],
    'B': [6, 4, 5]
}, index=['c', 'a', 'b'])

df.sort_index()
```

```
   A  B
a  1  4
b  2  5
c  3  6
```

### 2. Descending Order

```python
df.sort_index(ascending=False)
```

```
   A  B
c  3  6
b  2  5
a  1  4
```

### 3. Sort Columns

```python
df = pd.DataFrame({
    'C': [1, 2],
    'A': [3, 4],
    'B': [5, 6]
})

df.sort_index(axis=1)  # Sort columns alphabetically
```

## sort_values Method

Sort by values in specified columns.

### 1. Single Column

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [30, 25, 35]
})

df.sort_values(by='Age')
```

```
    Name  Age
1    Bob   25
0  Alice   30
2  Carol   35
```

### 2. Multiple Columns

```python
df = pd.DataFrame({
    'Dept': ['A', 'B', 'A', 'B'],
    'Name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'Salary': [50000, 60000, 55000, 60000]
})

df.sort_values(by=['Dept', 'Salary'])
```

### 3. Mixed Order

```python
df.sort_values(
    by=['Dept', 'Salary'],
    ascending=[True, False]  # Dept ascending, Salary descending
)
```

## Series Sorting

Sort Series by index or values.

### 1. Sort by Values

```python
s = pd.Series([3, 1, 4, 1, 5], index=['a', 'b', 'c', 'd', 'e'])
s.sort_values()
```

```
b    1
d    1
a    3
c    4
e    5
dtype: int64
```

### 2. Sort by Index

```python
s.sort_index()
```

### 3. Get Sorted Index

```python
s.argsort()  # Returns positions for sorting
```

## Handling NaN

Control how missing values are sorted.

### 1. NaN at End (Default)

```python
df = pd.DataFrame({
    'A': [3, None, 1, 2]
})

df.sort_values(by='A')  # NaN at end
```

### 2. NaN at Beginning

```python
df.sort_values(by='A', na_position='first')
```

### 3. Drop NaN Before Sorting

```python
df.dropna().sort_values(by='A')
```

## Ranking

Assign ranks to values.

### 1. Basic Ranking

```python
df = pd.DataFrame({
    'Score': [85, 90, 85, 95]
})

df['Rank'] = df['Score'].rank(ascending=False)
```

### 2. Ranking Methods

```python
# method='average' (default): average rank for ties
# method='min': lowest rank for ties
# method='max': highest rank for ties
# method='first': ranks by order of appearance
# method='dense': like 'min', but ranks always increase by 1
```

### 3. Dense Ranking Example

```python
df['DenseRank'] = df['Score'].rank(ascending=False, method='dense')
```

## Practical Examples

Common sorting scenarios.

### 1. Top N Values

```python
# Top 3 highest salaries
df.sort_values('Salary', ascending=False).head(3)

# Using nlargest
df.nlargest(3, 'Salary')
```

### 2. Bottom N Values

```python
df.sort_values('Salary').head(3)

# Using nsmallest
df.nsmallest(3, 'Salary')
```

### 3. Reset Index After Sort

```python
df_sorted = df.sort_values('Age').reset_index(drop=True)
```

## Key Parameter

Custom sort using a key function.

### 1. Case-insensitive Sort

```python
df.sort_values(by='Name', key=lambda x: x.str.lower())
```

### 2. String Length Sort

```python
df.sort_values(by='Name', key=lambda x: x.str.len())
```

### 3. Custom Transform

```python
df.sort_values(by='Value', key=lambda x: abs(x))
```
