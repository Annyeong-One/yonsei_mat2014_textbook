# dropna Method

The `dropna()` method removes rows or columns containing missing values. It is useful when missing data cannot be reliably imputed.

## Basic Usage

Drop rows with any missing values.

### 1. Drop Rows

```python
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/codebasics/py/master/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv"
df = pd.read_csv(url, index_col='day', parse_dates=True)
print(df)

dg = df.dropna()
print(dg)
```

### 2. Drop Columns

```python
df.dropna(axis=1)  # Drop columns with any NaN
```

### 3. Return Copy

```python
# dropna returns a new DataFrame
dg = df.dropna()
# Original df is unchanged
```

## LeetCode Example: Student Names

Drop students with missing names.

### 1. Problem Data

```python
students = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', None, 'Bob', None, 'Charlie'],
    'grade': ['A', 'B', 'B+', 'A-', 'C']
})
```

### 2. Drop Missing Names

```python
result = students.dropna(subset=['name'])
print(result)
```

### 3. Result

```
   id     name grade
0   1    Alice     A
2   3      Bob    B+
4   5  Charlie     C
```

## LeetCode Example: Employee Data

Drop employees with any missing values.

### 1. Problem Data

```python
filtered_employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'manager_id': [2.0, None, None, 2.0, 3.0],
    'salary': [25000, 35000, 28000, None, 32000]
})
```

### 2. Drop All NaN Rows

```python
cleaned_employees = filtered_employees.dropna()
print(cleaned_employees)
```

### 3. Result

Only rows with complete data remain:

```
   employee_id  manager_id  salary
0            1         2.0   25000
4            5         3.0   32000
```

## Practical Considerations

When to use dropna vs fillna.

### 1. Use dropna When

- Missing data is random and limited
- Filling would introduce bias
- Sufficient data remains after dropping

### 2. Avoid dropna When

- Missing data is systematic
- Dropping loses too much information
- Missing values can be reasonably estimated

### 3. Check Impact

```python
print(f"Before: {len(df)} rows")
print(f"After: {len(df.dropna())} rows")
print(f"Dropped: {len(df) - len(df.dropna())} rows")
```
