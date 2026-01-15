# transform Method

The `transform()` method applies a function to each group and returns a result with the same shape as the original DataFrame.

## Basic Concept

Transform preserves the original index.

### 1. Difference from agg

```python
import pandas as pd

df = pd.DataFrame({
    'group': ['A', 'A', 'B', 'B'],
    'value': [1, 2, 3, 4]
})

# agg: returns one value per group
df.groupby('group')['value'].mean()
# group
# A    1.5
# B    3.5

# transform: returns same-length Series
df.groupby('group')['value'].transform('mean')
# 0    1.5
# 1    1.5
# 2    3.5
# 3    3.5
```

### 2. Same Shape Output

Transform output aligns with original DataFrame.

### 3. Broadcast Group Values

Each row gets its group's aggregated value.

## LeetCode Example: First Activity Date

Find each player's first login date.

### 1. Sample Data

```python
activity = pd.DataFrame({
    'player_id': [1, 1, 2, 2],
    'event_date': pd.to_datetime([
        '2024-01-01', '2024-01-02',
        '2024-01-03', '2024-01-04'
    ])
})
```

### 2. Transform with min

```python
activity["first"] = activity.groupby("player_id")["event_date"].transform('min')
print(activity)
```

```
   player_id event_date      first
0          1 2024-01-01 2024-01-01
1          1 2024-01-02 2024-01-01
2          2 2024-01-03 2024-01-03
3          2 2024-01-04 2024-01-03
```

### 3. Each Row Gets Group Min

Every row for player 1 shows their first date.

## Common Use Cases

Typical transform applications.

### 1. Group Normalization

```python
df['normalized'] = df.groupby('group')['value'].transform(
    lambda x: (x - x.mean()) / x.std()
)
```

### 2. Percent of Group Total

```python
df['pct_of_group'] = df.groupby('group')['value'].transform(
    lambda x: x / x.sum()
)
```

### 3. Rank Within Group

```python
df['group_rank'] = df.groupby('group')['value'].transform('rank')
```

## transform vs apply

Key differences between methods.

### 1. Output Shape

```python
# transform: must return same shape
# apply: can return any shape
```

### 2. Function Requirements

```python
# transform: function must return same-length Series
# apply: more flexible
```

### 3. Performance

```python
# transform: often faster for built-in functions
# apply: more flexible but potentially slower
```

## Multiple Columns

Transform multiple columns at once.

### 1. Same Function

```python
df[['value1', 'value2']] = df.groupby('group')[['value1', 'value2']].transform('mean')
```

### 2. Different Functions

```python
# Use apply for different functions per column
```

### 3. Preserving Original

```python
# Create new columns instead of overwriting
df['value_mean'] = df.groupby('group')['value'].transform('mean')
```
