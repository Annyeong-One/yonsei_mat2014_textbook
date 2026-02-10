# apply Method

The `apply()` method applies a function along an axis of a DataFrame or to elements of a Series. It is one of the most versatile pandas methods.

## Series apply

Apply a function to each element of a Series.

### 1. Lambda Function

```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url, index_col='PassengerId')

bool_mask = df.Sex.apply(lambda x: x == "female")
print(bool_mask.head())
```

```
PassengerId
1    False
2     True
3     True
4     True
5    False
Name: Sex, dtype: bool
```

### 2. Named Function

```python
def classify_age(age):
    if pd.isna(age):
        return 'Unknown'
    elif age < 18:
        return 'Child'
    elif age < 65:
        return 'Adult'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].apply(classify_age)
```

### 3. String Methods Alternative

```python
# Instead of apply for simple string operations:
df['Name'].apply(lambda x: x.upper())

# Use vectorized string methods:
df['Name'].str.upper()
```

## DataFrame apply

Apply a function along rows or columns.

### 1. Column-wise (axis=0)

```python
df[['Age', 'Fare']].apply(lambda x: x.mean())
```

```
Age     29.699118
Fare    32.204208
dtype: float64
```

### 2. Row-wise (axis=1)

```python
bool_mask = df.apply(lambda x: x.Sex == "female", axis=1)
print(bool_mask.head())
```

### 3. Multiple Columns

```python
df['Total'] = df.apply(
    lambda row: row['Quantity'] * row['Price'],
    axis=1
)
```

## LeetCode Example: Class Attendance

Count students per class using apply.

### 1. Sample Data

```python
courses = pd.DataFrame({
    'class': ['Math', 'Science', 'Math', 'History', 
              'Math', 'Science', 'Math', 'History'],
    'student': ['Alice', 'Bob', 'Carol', 'Dave', 
                'Eve', 'Frank', 'Grace', 'Helen']
})
```

### 2. GroupBy with apply

```python
result = courses.groupby('class')['student'].apply(len)
print(result)
```

```
class
History    2
Math       4
Science    2
Name: student, dtype: int64
```

### 3. Alternative with size

```python
courses.groupby('class').size()
```

## LeetCode Example: Triangle Judgement

Convert boolean to Yes/No string.

### 1. Apply with Lambda

```python
triangle = pd.DataFrame({
    'x': [3, 1, 5],
    'y': [4, 2, 10],
    'z': [5, 3, 7],
    'is_valid': [True, False, True]
})

triangle["result"] = triangle["is_valid"].apply(
    lambda x: "Yes" if x else "No"
)
print(triangle)
```

### 2. Result

```
   x   y   z  is_valid result
0  3   4   5      True    Yes
1  1   2   3     False     No
2  5  10   7      True    Yes
```

### 3. Alternative with map

```python
triangle["result"] = triangle["is_valid"].map({True: "Yes", False: "No"})
```

## LeetCode Example: Special Bonus

Apply with multiple conditions.

### 1. Bonus Criteria Function

```python
def bonus_criteria(employee_id, name):
    return employee_id % 2 != 0 and not name.startswith('M')
```

### 2. Apply Row-wise

```python
employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Mike', 'Molly', 'Eve'],
    'salary': [50000, 60000, 70000, 80000, 90000]
})

employees['bonus'] = employees.apply(
    lambda row: row['salary'] if bonus_criteria(row['employee_id'], row['name']) else 0,
    axis=1
)
print(employees)
```

### 3. Result

```
   employee_id   name  salary  bonus
0            1  Alice   50000  50000
1            2    Bob   60000      0
2            3   Mike   70000      0
3            4  Molly   80000      0
4            5    Eve   90000  90000
```

## Performance Considerations

When to use and avoid apply.

### 1. Prefer Vectorized Operations

```python
# Slow
df['double'] = df['value'].apply(lambda x: x * 2)

# Fast
df['double'] = df['value'] * 2
```

### 2. Avoid Row-wise When Possible

```python
# Slow (iterates rows)
df.apply(lambda row: row['a'] + row['b'], axis=1)

# Fast (vectorized)
df['a'] + df['b']
```

### 3. Use apply When Necessary

- Complex logic that cannot be vectorized
- Custom aggregation functions
- Operations requiring multiple columns with conditions
