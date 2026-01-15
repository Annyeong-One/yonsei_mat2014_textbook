# merge Method

The `merge()` function combines DataFrames based on column values, similar to SQL joins. It is the most flexible method for combining datasets.

## Basic Syntax

Merge two DataFrames on a common column.

### 1. Simple Merge

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

### 2. Default Inner Join

By default, merge performs an inner join, keeping only matching rows.

### 3. Method Syntax

```python
# Function syntax
pd.merge(df1, df2, on='key')

# Method syntax (equivalent)
df1.merge(df2, on='key')
```

## LeetCode Example: Person and Address

Combine person information with address.

### 1. Sample Data

```python
person = pd.DataFrame({
    'personId': [1, 2, 3],
    'firstName': ['John', 'Jane', 'Jake'],
    'lastName': ['Doe', 'Smith', 'Brown']
})

address = pd.DataFrame({
    'personId': [1, 3],
    'city': ['New York', 'Los Angeles'],
    'state': ['NY', 'CA']
})
```

### 2. Left Merge

```python
merged_df = person.merge(address, on='personId', how='left')
print(merged_df)
```

### 3. Result

```
   personId firstName lastName         city state
0         1      John      Doe     New York    NY
1         2      Jane    Smith          NaN   NaN
2         3      Jake    Brown  Los Angeles    CA
```

## LeetCode Example: Project Employees

Join projects with employee experience.

### 1. Sample Data

```python
project = pd.DataFrame({
    'project_id': [101, 102, 103],
    'project_name': ['Project A', 'Project B', 'Project C']
})

employee = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'project_id': [101, 101, 102, 102, 103],
    'experience_years': [5, 7, 3, 4, 6]
})
```

### 2. Merge with Default

```python
merged_df = pd.merge(project, employee, how='left')
print(merged_df)
```

### 3. Auto-detected Key

When `on=None`, merge uses common column names automatically.

## Common Column Detection

Merge automatically finds common columns when `on` is not specified.

### 1. Auto Detection

```python
# Both DataFrames have 'project_id' column
pd.merge(project, employee)  # on='project_id' inferred
```

### 2. Multiple Common Columns

```python
# If both have ['key1', 'key2'], merges on both
pd.merge(df1, df2)
```

### 3. No Common Columns

```python
# Raises ValueError if no common columns exist
# Must specify left_on and right_on
```

## Merge Result Structure

Understanding the output DataFrame.

### 1. Column Order

```python
# Left DataFrame columns first, then right
# Common column appears once (unless using suffixes)
```

### 2. Row Order

```python
# Order depends on join type and matching
```

### 3. Index Reset

```python
# Merge resets index to RangeIndex
# Original indices are discarded
```
