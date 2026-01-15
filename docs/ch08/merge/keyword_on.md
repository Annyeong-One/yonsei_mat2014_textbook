# Keyword - on

The `on` parameter specifies which column(s) to use as the join key when both DataFrames share the same column name.

## Single Column

Join on a single shared column.

### 1. Basic Usage

```python
import pandas as pd

df1 = pd.DataFrame({
    'city': ['NY', 'SF', 'LA'],
    'temperature': [21, 14, 35]
})

df2 = pd.DataFrame({
    'city': ['SF', 'NY', 'ICN'],
    'humidity': [65, 68, 75]
})

df = pd.merge(df1, df2, on='city')
print(df)
```

```
  city  temperature  humidity
0   NY           21        68
1   SF           14        65
```

### 2. Column Must Exist

```python
# Column must exist in both DataFrames
# pd.merge(df1, df2, on='nonexistent')  # KeyError
```

### 3. Case Sensitive

```python
# Column names are case-sensitive
# 'City' != 'city'
```

## Multiple Columns

Join on multiple columns.

### 1. List of Columns

```python
df1 = pd.DataFrame({
    'year': [2023, 2023, 2024],
    'month': [1, 2, 1],
    'sales': [100, 150, 200]
})

df2 = pd.DataFrame({
    'year': [2023, 2023, 2024],
    'month': [1, 2, 1],
    'expenses': [80, 90, 120]
})

df = pd.merge(df1, df2, on=['year', 'month'])
print(df)
```

### 2. All Keys Must Match

```python
# A row matches only if ALL specified columns match
```

### 3. Order Independence

```python
# on=['year', 'month'] same as on=['month', 'year']
```

## LeetCode Example: Student Examinations

Join on multiple columns for student-subject pairs.

### 1. Sample Data

```python
student_subject = pd.DataFrame({
    'student_id': [1, 1, 2, 2],
    'student_name': ['Alice', 'Alice', 'Bob', 'Bob'],
    'subject_name': ['Math', 'Science', 'Math', 'Science']
})

examination_count = pd.DataFrame({
    'student_id': [1, 1, 2],
    'subject_name': ['Math', 'Science', 'Math'],
    'attended_exams': [2, 1, 3]
})
```

### 2. Multi-column Join

```python
result = pd.merge(
    student_subject,
    examination_count,
    on=['student_id', 'subject_name'],
    how='left'
)
print(result)
```

### 3. Result

```
   student_id student_name subject_name  attended_exams
0           1        Alice         Math             2.0
1           1        Alice      Science             1.0
2           2          Bob         Math             3.0
3           2          Bob      Science             NaN
```

## Default Behavior

When `on=None`, merge auto-detects common columns.

### 1. Auto Detection

```python
# Finds all columns with same name in both DataFrames
pd.merge(df1, df2)  # Uses all common columns
```

### 2. Explicit is Better

```python
# Prefer explicit on parameter for clarity
pd.merge(df1, df2, on='common_column')
```

### 3. Avoid Surprises

```python
# Auto-detection may join on unintended columns
# Always specify on for production code
```

## Error Handling

Common issues with the `on` parameter.

### 1. Column Not Found

```python
# KeyError if column doesn't exist in both
try:
    pd.merge(df1, df2, on='missing_col')
except KeyError as e:
    print(f"Error: {e}")
```

### 2. No Common Columns

```python
# MergeError if on=None and no common columns
# Solution: use left_on and right_on
```

### 3. Type Mismatch

```python
# Columns should have compatible types
# int and float usually work
# str and int will not match
```
