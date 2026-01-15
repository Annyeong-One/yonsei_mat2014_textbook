# filter Method

The `filter()` method removes groups that do not satisfy a condition, keeping or excluding entire groups.

## Basic Usage

Filter groups based on a condition.

### 1. Filter by Group Size

```python
import pandas as pd

df = pd.DataFrame({
    'group': ['A', 'A', 'A', 'B', 'B', 'C'],
    'value': [1, 2, 3, 4, 5, 6]
})

# Keep only groups with more than 2 members
result = df.groupby('group').filter(lambda x: len(x) > 2)
print(result)
```

```
  group  value
0     A      1
1     A      2
2     A      3
```

### 2. Filter Function

The function receives each group DataFrame and returns True/False.

### 3. All or Nothing

If condition is True, entire group is kept; otherwise, entire group is removed.

## Common Filtering Patterns

Typical filter conditions.

### 1. Minimum Group Size

```python
df.groupby('group').filter(lambda x: len(x) >= 5)
```

### 2. Value Threshold

```python
# Keep groups where mean exceeds threshold
df.groupby('group').filter(lambda x: x['value'].mean() > 10)
```

### 3. All Values Meet Condition

```python
# Keep groups where all values are positive
df.groupby('group').filter(lambda x: (x['value'] > 0).all())
```

## LeetCode Example: Classes with Students

Find classes with at least 5 students.

### 1. Sample Data

```python
courses = pd.DataFrame({
    'class': ['Math', 'Math', 'Math', 'Math', 'Math',
              'Art', 'Art', 'Music', 'Music', 'Music'],
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
})
```

### 2. Filter Large Classes

```python
large_classes = courses.groupby('class').filter(lambda x: len(x) >= 5)
print(large_classes)
```

### 3. Get Class Names

```python
# Get unique class names
classes = large_classes['class'].unique()
```

## Filter vs Boolean Indexing

Compare approaches.

### 1. Boolean Indexing

```python
# Filter individual rows
df[df['value'] > 5]
```

### 2. GroupBy Filter

```python
# Filter entire groups
df.groupby('group').filter(lambda x: x['value'].mean() > 5)
```

### 3. Key Difference

Boolean indexing filters rows; filter removes groups.

## dropna Parameter

Handle groups with missing values.

### 1. Default Behavior

```python
# dropna=True (default): ignore groups with NA
```

### 2. Include NA Groups

```python
df.groupby('group', dropna=False).filter(lambda x: len(x) > 1)
```

### 3. Filter NA Groups

```python
df.groupby('group').filter(lambda x: x['value'].notna().all())
```

## Performance Considerations

Optimize filter operations.

### 1. Simple Conditions First

```python
# Pre-filter when possible
valid_groups = df.groupby('group').size() >= 5
valid_group_names = valid_groups[valid_groups].index
df[df['group'].isin(valid_group_names)]
```

### 2. Avoid Lambda When Possible

```python
# Faster alternative for size filter
group_sizes = df.groupby('group').size()
valid = group_sizes[group_sizes >= 5].index
df[df['group'].isin(valid)]
```

### 3. Use Built-in Methods

Built-in aggregations are faster than custom lambdas.
