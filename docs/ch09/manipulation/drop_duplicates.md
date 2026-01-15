# drop_duplicates Method

The `drop_duplicates()` method removes duplicate rows from a DataFrame.

## Basic Usage

Remove duplicate rows.

### 1. Remove All Duplicates

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 1, 2, 2, 3],
    'B': ['a', 'a', 'b', 'b', 'c']
})

result = df.drop_duplicates()
print(result)
```

```
   A  B
0  1  a
2  2  b
4  3  c
```

### 2. Keep First (Default)

First occurrence is kept, duplicates removed.

### 3. Returns New DataFrame

```python
# Original unchanged
new_df = df.drop_duplicates()
```

## subset Parameter

Check specific columns for duplicates.

### 1. Single Column

```python
df = pd.DataFrame({
    'id': [1, 2, 1, 3],
    'name': ['Alice', 'Bob', 'Alice', 'Charlie']
})

result = df.drop_duplicates(subset='id')
print(result)
```

```
   id     name
0   1    Alice
1   2      Bob
3   3  Charlie
```

### 2. Multiple Columns

```python
result = df.drop_duplicates(subset=['id', 'name'])
```

### 3. All Columns (Default)

```python
# subset=None checks all columns
result = df.drop_duplicates()  # Uses all columns
```

## keep Parameter

Control which duplicate to keep.

### 1. Keep First (Default)

```python
df.drop_duplicates(keep='first')
# Keeps first occurrence
```

### 2. Keep Last

```python
df.drop_duplicates(keep='last')
# Keeps last occurrence
```

### 3. Keep None (Remove All)

```python
df.drop_duplicates(keep=False)
# Removes ALL duplicates, keeps only unique rows
```

## LeetCode Example: Delete Duplicate Emails

Keep first occurrence by email.

### 1. Sample Data

```python
person = pd.DataFrame({
    'id': [1, 2, 3],
    'email': ['a@example.com', 'b@example.com', 'a@example.com']
})
```

### 2. Remove Duplicates

```python
person.drop_duplicates(subset='email', inplace=True)
print(person)
```

```
   id          email
0   1  a@example.com
1   2  b@example.com
```

### 3. Sorted First

```python
# Sort to control which row is kept
person = person.sort_values('id')
person.drop_duplicates(subset='email', keep='first', inplace=True)
```

## LeetCode Example: Second Highest Salary

Get unique sorted values.

### 1. Unique Salaries

```python
employee = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'salary': [100, 200, 200, 300]
})

unique_salaries = employee['salary'].drop_duplicates()
```

### 2. Sort Descending

```python
sorted_salaries = unique_salaries.sort_values(ascending=False)
print(sorted_salaries)
```

```
3    300
1    200
0    100
```

### 3. Get Second Highest

```python
if len(sorted_salaries) >= 2:
    second_highest = sorted_salaries.iloc[1]
else:
    second_highest = None
```

## LeetCode Example: Consecutive Numbers

Drop duplicates after filtering.

### 1. Find Consecutive

```python
logs = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'num': [1, 1, 1, 2, 2, 2]
})
```

### 2. Filter and Drop

```python
# After filtering for consecutive numbers
consecutive = logs[
    (logs['num'] == logs['num'].shift(1)) &
    (logs['num'] == logs['num'].shift(2))
]

# Drop duplicate numbers
result = consecutive.drop_duplicates('num')
```

### 3. Unique Values Only

```python
unique_nums = result[['num']].rename(columns={'num': 'ConsecutiveNums'})
```

## LeetCode Example: Investments in 2016

keep=False for removing all duplicates.

### 1. Sample Data

```python
insurance = pd.DataFrame({
    'pid': [1, 2, 3, 4],
    'lat': [10.0, 10.0, 20.0, 20.0],
    'lon': [5.0, 5.0, 15.0, 25.0],
    'tiv_2016': [100, 200, 300, 400]
})
```

### 2. Remove All Duplicates

```python
# Keep only unique lat/lon combinations
unique_locations = insurance.drop_duplicates(
    subset=['lat', 'lon'],
    keep=False
)
```

### 3. Result

```python
print(unique_locations)
```

```
   pid   lat   lon  tiv_2016
2    3  20.0  15.0       300
3    4  20.0  25.0       400
```

## inplace Parameter

Modify DataFrame directly.

### 1. Without inplace

```python
result = df.drop_duplicates()
# df unchanged
```

### 2. With inplace

```python
df.drop_duplicates(inplace=True)
# df modified directly
```

### 3. Reassignment Preferred

```python
df = df.drop_duplicates()
```

## ignore_index Parameter

Reset index after dropping.

### 1. Keep Original Index

```python
result = df.drop_duplicates()
# Keeps original index values
```

### 2. Reset Index

```python
result = df.drop_duplicates(ignore_index=True)
# Index is 0, 1, 2, ...
```

### 3. Equivalent To

```python
result = df.drop_duplicates().reset_index(drop=True)
```
