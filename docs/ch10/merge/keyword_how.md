# Keyword - how

The `how` parameter specifies the type of join to perform. It determines which rows are included in the result based on key matching.

## Inner Join

Keep only rows with matching keys in both DataFrames.

### 1. Default Behavior

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

df = pd.merge(df1, df2, on='city', how='inner')
print(df)
```

```
  city  temperature  humidity
0   NY           21        68
1   SF           14        65
```

### 2. Intersection of Keys

Only SF and NY exist in both DataFrames.

### 3. Most Restrictive

Inner join produces the smallest result set.

## Left Join

Keep all rows from the left DataFrame.

### 1. Left Join Example

```python
df = pd.merge(df1, df2, on='city', how='left')
print(df)
```

```
  city  temperature  humidity
0   NY           21      68.0
1   SF           14      65.0
2   LA           35       NaN
```

### 2. NaN for Missing

LA has no match in df2, so humidity is NaN.

### 3. Preserve Left Rows

All rows from df1 are preserved.

## Right Join

Keep all rows from the right DataFrame.

### 1. Right Join Example

```python
df = pd.merge(df1, df2, on='city', how='right')
print(df)
```

```
  city  temperature  humidity
0   SF         14.0        65
1   NY         21.0        68
2  ICN          NaN        75
```

### 2. NaN for Missing

ICN has no match in df1, so temperature is NaN.

### 3. Preserve Right Rows

All rows from df2 are preserved.

## Outer Join

Keep all rows from both DataFrames.

### 1. Outer Join Example

```python
df = pd.merge(df1, df2, on='city', how='outer')
print(df)
```

```
  city  temperature  humidity
0   NY         21.0      68.0
1   SF         14.0      65.0
2   LA         35.0       NaN
3  ICN          NaN      75.0
```

### 2. Union of Keys

All unique cities from both DataFrames.

### 3. Most Inclusive

Outer join produces the largest result set.

## Visual Comparison

Side-by-side comparison of join types.

### 1. Sample Data

```python
left = pd.DataFrame({'key': ['A', 'B', 'C'], 'left_val': [1, 2, 3]})
right = pd.DataFrame({'key': ['B', 'C', 'D'], 'right_val': [4, 5, 6]})
```

### 2. Results Summary

| how | Keys in Result | Missing Values |
|-----|---------------|----------------|
| inner | B, C | None |
| left | A, B, C | right_val for A |
| right | B, C, D | left_val for D |
| outer | A, B, C, D | Both sides |

### 3. Row Counts

```python
print(len(pd.merge(left, right, how='inner')))  # 2
print(len(pd.merge(left, right, how='left')))   # 3
print(len(pd.merge(left, right, how='right')))  # 3
print(len(pd.merge(left, right, how='outer')))  # 4
```

## Practical Guidelines

Choosing the right join type.

### 1. Use Inner When

- Only need matched records
- Data quality requires both sides present
- Computing ratios or comparisons

### 2. Use Left When

- Preserving primary table structure
- Optional enrichment data
- Most common in practice

### 3. Use Outer When

- Need complete picture of both sources
- Finding mismatches
- Data reconciliation
