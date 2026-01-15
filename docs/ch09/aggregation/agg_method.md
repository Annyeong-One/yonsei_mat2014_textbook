# agg Method

The `agg()` method (short for aggregate) applies one or more aggregation functions to columns. It provides flexible control over which functions to apply.

## Basic Usage

Apply aggregation functions to a DataFrame.

### 1. Single Function

```python
import pandas as pd
import yfinance as yf

ticker = "WMT"
df = yf.Ticker(ticker).history(start="2020-01-30", end="2022-12-31")
df = df[["Open", "Close"]].pct_change()
print(df.head())

dg = df.agg('std')
print(dg)
```

```
Open     0.016482
Close    0.017234
dtype: float64
```

### 2. Multiple Functions

```python
dg = df.agg(['std', 'max', 'min'])
print(dg)
```

```
          Open     Close
std   0.016482  0.017234
max   0.109375  0.119760
min  -0.082456 -0.097674
```

### 3. Custom Function

```python
def max_minus_min(x):
    return x.max() - x.min()

dg = df.agg(['std', 'max', 'min', max_minus_min])
print(dg)
```

## Column-specific Aggregations

Apply different functions to different columns.

### 1. Dictionary Specification

```python
dg = df.agg({
    "Open": ['std'],
    "Close": ['std', max_minus_min]
})
print(dg)
```

```
                   Open     Close
std            0.016482  0.017234
max_minus_min       NaN  0.217434
```

### 2. Named Aggregations

```python
df.agg(
    open_std=('Open', 'std'),
    close_mean=('Close', 'mean'),
    close_max=('Close', 'max')
)
```

### 3. Multiple Functions per Column

```python
df.agg({
    'Open': ['mean', 'std', 'min', 'max'],
    'Close': ['mean', 'std']
})
```

## LeetCode Example: Trips Analysis

Aggregate trip data by date.

### 1. Sample Data

```python
merged_data = pd.DataFrame({
    'request_at': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'valid_request': [1, 1, 1, 1],
    'effective_cancellation': [0, 1, 0, 0]
})
```

### 2. GroupBy with agg

```python
result = merged_data.groupby('request_at').agg({
    'valid_request': 'sum',
    'effective_cancellation': 'sum'
})
print(result)
```

### 3. Result

```
            valid_request  effective_cancellation
request_at                                       
2024-01-01              2                       1
2024-01-02              2                       0
```

## String Function Names

Common aggregation function strings.

### 1. Statistical Functions

```python
# 'mean', 'sum', 'min', 'max', 'std', 'var', 'sem'
# 'median', 'first', 'last', 'count', 'nunique'
```

### 2. Example Usage

```python
df.agg(['mean', 'std', 'min', 'max'])
```

### 3. Alias Functions

```python
# 'prod' - product
# 'size' - length including NaN
# 'count' - length excluding NaN
```

## agg vs aggregate

The methods are identical.

### 1. Alias

```python
df.agg('mean')        # Shorthand
df.aggregate('mean')  # Full name
```

### 2. Same Functionality

Both accept the same parameters and return identical results.

### 3. Prefer agg

The `agg` shorthand is more common in practice.

## Returning DataFrames

Control output structure.

### 1. Single Function Returns Series

```python
result = df.agg('mean')
print(type(result))  # Series
```

### 2. Multiple Functions Return DataFrame

```python
result = df.agg(['mean', 'std'])
print(type(result))  # DataFrame
```

### 3. Dict Returns DataFrame

```python
result = df.agg({'A': 'mean', 'B': 'std'})
print(type(result))  # Series (single value per column)
```
