# rank Method

The `rank()` method assigns ranks to values within each group, useful for identifying top performers or creating rankings.

## Basic Ranking

Rank values within groups.

### 1. Simple Rank

```python
import pandas as pd

df = pd.DataFrame({
    'dept': ['A', 'A', 'A', 'B', 'B', 'B'],
    'employee': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'],
    'salary': [5000, 6000, 4000, 4500, 5500, 4500]
})

df['rank'] = df.groupby('dept')['salary'].rank(ascending=False)
print(df)
```

```
  dept employee  salary  rank
0    A    Alice    5000   2.0
1    A      Bob    6000   1.0
2    A    Carol    4000   3.0
3    B     Dave    4500   2.5
4    B      Eve    5500   1.0
5    B    Frank    4500   2.5
```

### 2. ascending Parameter

```python
# ascending=False: highest value gets rank 1
# ascending=True: lowest value gets rank 1
```

### 3. Tie Handling

Default: tied values get average rank (2.5 for Dave and Frank).

## LeetCode Example: Department Top Salaries

Find top 3 salaries per department.

### 1. Sample Data

```python
employee = pd.DataFrame({
    'departmentId': [1, 1, 1, 2, 2, 2],
    'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank'],
    'salary': [5000, 6000, 4000, 4500, 5500, 4500]
})
```

### 2. Dense Ranking

```python
employee['rank'] = employee.groupby('departmentId')['salary'].rank(
    ascending=False,
    method='dense'
)
print(employee)
```

### 3. Filter Top 3

```python
top_3 = employee[employee['rank'] <= 3]
```

## method Parameter

Control how ties are handled.

### 1. method='average' (Default)

```python
# Ties get average of ranks they would occupy
# [100, 100, 80] → [1.5, 1.5, 3.0]
```

### 2. method='min'

```python
# Ties get lowest rank
# [100, 100, 80] → [1, 1, 3]
```

### 3. method='dense'

```python
# Ties get same rank, next rank is consecutive
# [100, 100, 80] → [1, 1, 2]
```

## Ranking Examples

Common ranking patterns.

### 1. Percentile Rank

```python
df['percentile'] = df.groupby('dept')['salary'].rank(pct=True)
```

### 2. Row Number

```python
df['row_num'] = df.groupby('dept').cumcount() + 1
```

### 3. First/Last in Group

```python
df['is_top'] = df.groupby('dept')['salary'].rank(ascending=False) == 1
```

## Comparison with SQL

Equivalent SQL window functions.

### 1. RANK()

```python
df.groupby('dept')['salary'].rank(method='min', ascending=False)
```

### 2. DENSE_RANK()

```python
df.groupby('dept')['salary'].rank(method='dense', ascending=False)
```

### 3. ROW_NUMBER()

```python
df.groupby('dept').cumcount() + 1
```
