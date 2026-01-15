# Self Merge

A self merge joins a DataFrame with itself, useful for comparing rows within the same table or representing hierarchical relationships.

## Basic Concept

Merge a DataFrame with itself using different columns.

### 1. Employee-Manager Example

```python
import pandas as pd

employee = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['John', 'Doe', 'Jane', 'Smith'],
    'salary': [50000, 40000, 60000, 30000],
    'managerId': [None, 1, 1, 2]
})
print(employee)
```

```
   id   name  salary  managerId
0   1   John   50000        NaN
1   2    Doe   40000        1.0
2   3   Jane   60000        1.0
3   4  Smith   30000        2.0
```

### 2. Self Merge

```python
merged = pd.merge(
    left=employee,
    right=employee,
    left_on='managerId',
    right_on='id',
    how='inner',
    suffixes=('_employee', '_manager')
)
print(merged)
```

### 3. Result Interpretation

Each row pairs an employee with their manager.

## LeetCode Example: Higher Salary than Manager

Find employees earning more than their managers.

### 1. Self Merge

```python
merged = pd.merge(
    left=employee,
    right=employee,
    left_on='managerId',
    right_on='id',
    how='inner',
    suffixes=('_employee', '_manager')
)
```

### 2. Filter Condition

```python
higher_earners = merged[
    merged['salary_employee'] > merged['salary_manager']
]
```

### 3. Select Result

```python
result = higher_earners[['name_employee']].rename(
    columns={'name_employee': 'Employee'}
)
```

## Hierarchical Relationships

Self merge for parent-child relationships.

### 1. Category Hierarchy

```python
categories = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Electronics', 'Phones', 'Laptops', 'iPhone', 'MacBook'],
    'parent_id': [None, 1, 1, 2, 3]
})
```

### 2. Join Parent Info

```python
with_parent = pd.merge(
    categories,
    categories[['id', 'name']],
    left_on='parent_id',
    right_on='id',
    how='left',
    suffixes=('', '_parent')
)
```

### 3. Result

```python
# Shows each category with its parent category name
```

## Comparing Consecutive Rows

Self merge to compare rows.

### 1. Stock Data

```python
stock = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5),
    'price': [100, 102, 101, 105, 103]
})
stock['row_num'] = range(len(stock))
```

### 2. Join Consecutive Rows

```python
stock_comparison = pd.merge(
    stock,
    stock,
    left_on='row_num',
    right_on=stock['row_num'] + 1,
    suffixes=('_today', '_yesterday')
)
```

### 3. Calculate Change

```python
stock_comparison['change'] = (
    stock_comparison['price_today'] - stock_comparison['price_yesterday']
)
```

## Join Types in Self Merge

Choose appropriate join type.

### 1. Inner Join

```python
# Only rows with valid relationship
pd.merge(df, df, left_on='parent_id', right_on='id', how='inner')
# Excludes rows without parent (root nodes)
```

### 2. Left Join

```python
# Keep all original rows
pd.merge(df, df, left_on='parent_id', right_on='id', how='left')
# Root nodes have NaN for parent info
```

### 3. Use Case Selection

```python
# Inner: When relationship is required
# Left: When preserving all original rows matters
```

## Performance Considerations

Self merge creates more rows.

### 1. Cartesian Product Warning

```python
# Without proper keys, self merge creates N×N rows
# Always specify join columns carefully
```

### 2. Large DataFrames

```python
# Self merge can be memory-intensive
# Consider filtering before merge
```

### 3. Alternative Approaches

```python
# For simple comparisons, consider:
df['prev_value'] = df['value'].shift(1)
```
