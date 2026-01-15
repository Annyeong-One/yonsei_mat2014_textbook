# interpolate Method

The `interpolate()` method fills missing values using interpolation techniques, estimating values based on surrounding data points.

## Linear Interpolation

The default method performs linear interpolation between valid values.

### 1. Basic Usage

```python
import pandas as pd

url = "https://raw.githubusercontent.com/codebasics/py/master/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv"
df = pd.read_csv(url, index_col='day', parse_dates=True)
print(df)

dg = df.interpolate()
print(dg)
```

### 2. How Linear Works

For missing value at position i:

```
value[i] = value[i-1] + (value[i+1] - value[i-1]) / 2
```

### 3. Numeric Columns Only

Interpolation works on numeric columns; non-numeric columns are unchanged.

## method Keyword

Specify the interpolation technique.

### 1. Linear (Default)

```python
df.interpolate(method='linear')
```

Ignores the index and treats values as equally spaced.

### 2. Time-based

```python
dg = df.interpolate(method='time')
print(dg)
```

Uses actual time intervals for interpolation. Requires DatetimeIndex.

### 3. Index-based

```python
df.interpolate(method='index')
```

Uses the numerical values of the index.

## Scipy Methods

Advanced interpolation methods via scipy.

### 1. Polynomial

```python
df.interpolate(method='polynomial', order=2)
```

Fits a polynomial of specified order.

### 2. Spline

```python
df.interpolate(method='spline', order=3)
```

Cubic spline interpolation for smooth curves.

### 3. Other Methods

```python
# Available scipy methods:
# 'nearest', 'zero', 'slinear', 'quadratic', 'cubic'
# 'krogh', 'pchip', 'akima', 'cubicspline'
```

## Practical Comparison

Compare fillna with interpolate for time series data.

### 1. Forward Fill

```python
df_ffill = df.fillna(method='ffill')
# Repeats last known value
```

### 2. Linear Interpolation

```python
df_interp = df.interpolate()
# Estimates intermediate values
```

### 3. When to Use Each

```python
# Use ffill for categorical or step-like data
# Use interpolate for continuous measurements
```

## Time Series Example

Interpolate missing temperature readings.

### 1. Sample Data

```python
dates = pd.date_range('2024-01-01', periods=5, freq='D')
temps = pd.Series([20, None, None, 26, 28], index=dates)
print(temps)
```

### 2. Linear Interpolation

```python
temps.interpolate()
# Fills with 22 and 24 (evenly spaced)
```

### 3. Time Interpolation

```python
temps.interpolate(method='time')
# Same result for equally spaced dates
```

## Handling Edge Cases

Interpolation has limitations at boundaries.

### 1. Leading NaN

```python
s = pd.Series([None, None, 3, 4, 5])
s.interpolate()  # Leading NaN remain
```

### 2. Trailing NaN

```python
s = pd.Series([1, 2, 3, None, None])
s.interpolate()  # Trailing NaN remain
```

### 3. Combine with Fill

```python
# First interpolate, then fill edges
s.interpolate().fillna(method='bfill').fillna(method='ffill')
```
