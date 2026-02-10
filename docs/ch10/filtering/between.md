# between Method

The `between()` method filters values within a range, inclusive of both endpoints.

## Basic Usage

Filter values in a range.

### 1. Numeric Range

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [22, 28, 35, 42, 55]
})

# Filter age between 25 and 40
result = df[df['age'].between(25, 40)]
print(result)
```

```
      name  age
1      Bob   28
2  Charlie   35
```

### 2. Inclusive by Default

Both endpoints are included (25 and 40).

### 3. Boolean Result

```python
mask = df['age'].between(25, 40)
print(mask)
```

```
0    False
1     True
2     True
3    False
4    False
Name: age, dtype: bool
```

## inclusive Parameter

Control endpoint inclusion.

### 1. Both Endpoints (Default)

```python
df['age'].between(25, 40, inclusive='both')
# Includes 25 and 40
```

### 2. Neither Endpoint

```python
df['age'].between(25, 40, inclusive='neither')
# Excludes 25 and 40
```

### 3. Left or Right Only

```python
df['age'].between(25, 40, inclusive='left')   # Includes 25 only
df['age'].between(25, 40, inclusive='right')  # Includes 40 only
```

## Date Ranges

Filter dates within a period.

### 1. Date between

```python
activity = pd.DataFrame({
    'activity_date': pd.to_datetime([
        '2019-06-27', '2019-06-28', '2019-07-01',
        '2019-07-27', '2019-07-28'
    ]),
    'user_id': [1, 2, 3, 4, 5]
})

# Filter 30-day period
result = activity[
    activity['activity_date'].between('2019-06-28', '2019-07-27')
]
print(result)
```

```
  activity_date  user_id
1    2019-06-28        2
2    2019-07-01        3
3    2019-07-27        4
```

### 2. String Dates

Pandas automatically converts string dates.

### 3. Datetime Objects

```python
from datetime import datetime

start = datetime(2019, 6, 28)
end = datetime(2019, 7, 27)
result = activity[activity['activity_date'].between(start, end)]
```

## LeetCode Example: User Activity

Filter activity within date range.

### 1. Sample Data

```python
activity = pd.DataFrame({
    'activity_date': pd.to_datetime([
        '2019-06-27', '2019-06-28', '2019-07-01',
        '2019-07-15', '2019-07-27', '2019-07-28', '2019-08-01'
    ]),
    'user_id': [1, 2, 3, 4, 5, 6, 7]
})
```

### 2. Filter with between

```python
filtered = activity[
    activity['activity_date'].between('2019-06-28', '2019-07-27')
]
```

### 3. Count Unique Users

```python
active_users = filtered['user_id'].nunique()
```

## vs Comparison Operators

Equivalent operations.

### 1. between Syntax

```python
df[df['age'].between(25, 40)]
```

### 2. Comparison Syntax

```python
df[(df['age'] >= 25) & (df['age'] <= 40)]
```

### 3. Advantages

- between: cleaner, more readable
- Comparison: more flexible (exclusive bounds, etc.)

## String Ranges

Filter string values alphabetically.

### 1. Alphabetic Range

```python
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve']})
result = df[df['name'].between('B', 'D')]
print(result)
```

```
     name
1     Bob
2  Charlie
```

### 2. Lexicographic Order

Strings are compared lexicographically.

### 3. Case Sensitivity

```python
# Uppercase letters come before lowercase in ASCII
# 'A' < 'Z' < 'a' < 'z'
```

## Numeric Precision

Handling float comparisons.

### 1. Float Range

```python
df = pd.DataFrame({'value': [0.1, 0.5, 1.0, 1.5, 2.0]})
result = df[df['value'].between(0.5, 1.5)]
```

### 2. Precision Issues

```python
# Be aware of floating point precision
# 0.1 + 0.2 != 0.3 in floating point
```

### 3. Round First

```python
df['value_rounded'] = df['value'].round(2)
result = df[df['value_rounded'].between(0.5, 1.5)]
```

## Combining with Other Filters

Use between with additional conditions.

### 1. AND Condition

```python
result = df[
    (df['age'].between(25, 40)) & 
    (df['city'] == 'NY')
]
```

### 2. OR Condition

```python
result = df[
    (df['age'].between(25, 40)) | 
    (df['salary'] > 100000)
]
```

### 3. Multiple between

```python
result = df[
    (df['age'].between(25, 40)) & 
    (df['salary'].between(50000, 80000))
]
```
