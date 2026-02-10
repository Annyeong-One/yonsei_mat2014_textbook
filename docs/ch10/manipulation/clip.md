# clip Method

The `clip()` method constrains values to a specified range.

## Basic Usage

### Clipping with Lower and Upper Bounds

```python
import pandas as pd

s = pd.Series([1, 5, 10, 15, 20, 25])

# Clip values to range [5, 20]
clipped = s.clip(lower=5, upper=20)
print(clipped)
```

```
0     5
1     5
2    10
3    15
4    20
5    20
dtype: int64
```

### Only Lower or Upper Bound

```python
s.clip(lower=10)  # Values below 10 become 10
s.clip(upper=15)  # Values above 15 become 15
```

## DataFrame Clipping

### Clip All Columns

```python
df = pd.DataFrame({
    'A': [1, 5, 10, 15, 20],
    'B': [2, 8, 14, 22, 30]
})

clipped = df.clip(lower=5, upper=20)
print(clipped)
```

### Per-Column Clipping

```python
df = pd.DataFrame({'A': [1, 50, 100], 'B': [10, 500, 1000]})

# Different bounds for each column
clipped = df.clip(lower=[0, 100], upper=[80, 800], axis=1)
```

## Practical Examples

### 1. Outlier Capping

```python
def cap_outliers(df, columns):
    """Cap outliers at 1st and 99th percentiles."""
    df_capped = df.copy()
    for col in columns:
        lower = df[col].quantile(0.01)
        upper = df[col].quantile(0.99)
        df_capped[col] = df[col].clip(lower=lower, upper=upper)
    return df_capped
```

### 2. Normalizing to Range

```python
# Clip values to valid range before processing
scores = pd.Series([95, 105, 88, -5, 72])
valid_scores = scores.clip(lower=0, upper=100)
```

### 3. Financial Position Limits

```python
positions = pd.DataFrame({
    'ticker': ['AAPL', 'GOOGL', 'MSFT'],
    'weight': [0.45, 0.35, 0.20]
})

# Enforce max 40% position limit
positions['weight_capped'] = positions['weight'].clip(upper=0.40)
```

### 4. Signal Processing

```python
# Clip noisy sensor readings
readings = pd.Series([98, 102, 150, 95, 99, -10, 101])
clean_readings = readings.clip(lower=90, upper=110)
```

## Key Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `lower` | Minimum allowed value | None |
| `upper` | Maximum allowed value | None |
| `axis` | Align bounds along axis (0 or 1) | None |
| `inplace` | Modify in place | False |

## Notes

- At least one of `lower` or `upper` must be specified
- NaN values are not clipped (they remain NaN)
- Works with both Series and DataFrame
- Original data is not modified unless `inplace=True`
