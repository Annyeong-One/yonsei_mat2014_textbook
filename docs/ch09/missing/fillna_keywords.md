# fillna Keywords

The `fillna()` method accepts several keyword arguments that control how missing values are filled.

## method Keyword

Propagate non-null values forward or backward.

### 1. Forward Fill (ffill)

```python
import pandas as pd

url = "https://raw.githubusercontent.com/codebasics/py/master/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv"
df = pd.read_csv(url, index_col='day', parse_dates=True)
print(df)

dg = df.fillna(method='ffill')
print(dg)
```

Forward fill propagates the last valid observation forward.

### 2. Backward Fill (bfill)

```python
dg = df.fillna(method='bfill')
print(dg)
```

Backward fill uses the next valid observation to fill gaps.

### 3. pad Alias

```python
df.fillna(method='pad')    # Same as ffill
df.fillna(method='backfill')  # Same as bfill
```

## axis Keyword

Specify the axis along which to fill missing values.

### 1. Fill Along Rows (axis=0)

```python
dg = df.fillna(method='ffill', axis=0)
print(dg)
```

Default behavior: fill down columns.

### 2. Fill Along Columns (axis=1)

```python
dg = df.fillna(method='ffill', axis=1)
print(dg)
```

Fill across rows from left to right.

### 3. Numeric vs String Columns

When filling along axis=1, be aware that mixed types may cause issues.

## limit Keyword

Limit the number of consecutive NaN values to fill.

### 1. Limit Forward Fill

```python
dg = df.fillna(method='ffill', limit=1)
print(dg)
```

Only fills up to 1 consecutive NaN value.

### 2. Preventing Over-filling

```python
# If there are 3 consecutive NaNs and limit=2
# Only the first 2 will be filled
```

### 3. Use Case

```python
# In time series, limit prevents filling across
# long gaps where forward fill may be inappropriate
df['price'].fillna(method='ffill', limit=5)
```

## Combined Keywords

Use multiple keywords together for precise control.

### 1. Forward Fill with Limit

```python
df.fillna(method='ffill', axis=0, limit=2)
```

### 2. Backward Fill with Limit

```python
df.fillna(method='bfill', axis=0, limit=1)
```

### 3. Fill Strategy

```python
# First forward fill, then backward fill remaining
df_filled = df.fillna(method='ffill').fillna(method='bfill')
```

## Modern Syntax

In recent pandas versions, prefer explicit methods over the `method` keyword.

### 1. ffill Method

```python
df.ffill()           # Forward fill
df.ffill(limit=2)    # With limit
```

### 2. bfill Method

```python
df.bfill()           # Backward fill
df.bfill(limit=1)    # With limit
```

### 3. Deprecation Note

The `method` parameter in `fillna` is deprecated in newer pandas versions:

```python
# Deprecated
df.fillna(method='ffill')

# Preferred
df.ffill()
```
