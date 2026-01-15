# Boolean Indexing

Filter DataFrame rows using boolean conditions and masks.

## Basic Comparison

Filter using comparison operators.

### 1. Single Condition

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'salary': [50000, 60000, 70000, 80000]
})

# Filter age > 30
result = df[df['age'] > 30]
print(result)
```

```
      name  age  salary
2  Charlie   35   70000
3    David   40   80000
```

### 2. Boolean Mask

```python
mask = df['age'] > 30
print(mask)
```

```
0    False
1    False
2     True
3     True
Name: age, dtype: bool
```

### 3. Apply Mask

```python
result = df[mask]
```

## Multiple Conditions

Combine conditions with logical operators.

### 1. AND Condition (&)

```python
# Age > 30 AND salary > 60000
result = df[(df['age'] > 30) & (df['salary'] > 60000)]
```

### 2. OR Condition (|)

```python
# Age > 35 OR salary < 55000
result = df[(df['age'] > 35) | (df['salary'] < 55000)]
```

### 3. NOT Condition (~)

```python
# NOT age > 30
result = df[~(df['age'] > 30)]
```

## Parentheses Required

Always use parentheses with multiple conditions.

### 1. Correct Syntax

```python
# Correct - parentheses around each condition
df[(df['age'] > 30) & (df['salary'] > 60000)]
```

### 2. Incorrect Syntax

```python
# Wrong - will raise error
# df[df['age'] > 30 & df['salary'] > 60000]
```

### 3. Operator Precedence

`&` has higher precedence than comparison operators.

## loc with Boolean

Use loc for boolean indexing with column selection.

### 1. Filter and Select

```python
result = df.loc[df['age'] > 30, ['name', 'salary']]
print(result)
```

```
      name  salary
2  Charlie   70000
3    David   80000
```

### 2. Modify Values

```python
df.loc[df['age'] > 30, 'bonus'] = 5000
```

### 3. Multiple Conditions

```python
df.loc[(df['age'] > 30) & (df['salary'] > 60000), 'level'] = 'Senior'
```

## LeetCode Example: Employees Earning More Than Manager

Self-merge and filter comparison.

### 1. Sample Data

```python
employee = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['John', 'Doe', 'Jane', 'Smith'],
    'salary': [50000, 40000, 60000, 30000],
    'managerId': [None, 1, 1, 2]
})
```

### 2. Self Merge

```python
merged = pd.merge(
    employee, employee,
    left_on='managerId', right_on='id',
    suffixes=('_emp', '_mgr')
)
```

### 3. Filter Comparison

```python
higher_salary = merged[merged['salary_emp'] > merged['salary_mgr']]
result = higher_salary[['name_emp']].rename(columns={'name_emp': 'Employee'})
```

## LeetCode Example: Not Boring Movies

Filter with multiple conditions.

### 1. Sample Data

```python
cinema = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'movie': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'description': ['thrilling', 'boring', 'exciting', 'boring doc', 'great'],
    'rating': [4.5, 3.0, 4.7, 2.1, 4.9]
})
```

### 2. Odd ID and Not Boring

```python
filtered = cinema[
    (cinema['id'] % 2 != 0) & 
    (~cinema['description'].str.contains('boring', case=False))
]
```

### 3. Result

```python
print(filtered)
```

## Missing Value Handling

Filter based on null values.

### 1. Filter Non-null

```python
result = df[df['salary'].notna()]
```

### 2. Filter Null

```python
result = df[df['salary'].isna()]
```

### 3. Any Row with Missing

```python
# Rows with any missing value
result = df[df.isna().any(axis=1)]
```

## Date Filtering

Filter by date conditions.

### 1. Date Range

```python
df['date'] = pd.to_datetime(df['date'])

result = df[
    (df['date'] >= '2019-06-28') & 
    (df['date'] <= '2019-07-27')
]
```

### 2. Year Filter

```python
result = df[df['date'].dt.year == 2020]
```

### 3. Month Filter

```python
result = df[df['date'].dt.month.isin([1, 2, 3])]  # Q1
```
