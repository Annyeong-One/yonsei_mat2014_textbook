# Detecting Missing Values

Missing data is inevitable in real-world datasets. pandas provides methods to detect and identify missing values.

## isnull Method

The `isnull()` method returns a boolean mask indicating missing values.

### 1. Series Detection

```python
import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, 3, None, 5])
print(s.isnull())
```

```
0    False
1     True
2    False
3     True
4    False
dtype: bool
```

### 2. DataFrame Detection

```python
df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan]
})
print(df.isnull())
```

```
       A      B
0  False  False
1   True  False
2  False   True
```

### 3. Count Missing Values

```python
print(df.isnull().sum())  # Per column
print(df.isnull().sum().sum())  # Total
```

## notnull Method

The `notnull()` method is the inverse of `isnull()`.

### 1. Basic Usage

```python
print(s.notnull())
```

```
0     True
1    False
2     True
3    False
4     True
dtype: bool
```

### 2. Filter Non-null Values

```python
s[s.notnull()]  # Keep only non-null values
```

### 3. Alias isna and notna

```python
s.isna()    # Same as isnull()
s.notna()   # Same as notnull()
```

## Missing Value Types

pandas treats several values as missing.

### 1. NaN (Not a Number)

```python
np.nan           # NumPy NaN
float('nan')     # Python NaN
pd.NA            # pandas NA
```

### 2. None

```python
s = pd.Series([1, None, 3])
print(s.isnull())  # None is treated as NaN
```

### 3. NaT (Not a Time)

```python
dates = pd.Series([pd.Timestamp('2024-01-01'), pd.NaT])
print(dates.isnull())
```

## Visualizing Missing Data

Understand missing data patterns.

### 1. Missing Percentage

```python
def missing_report(df):
    total = df.isnull().sum()
    percent = 100 * total / len(df)
    return pd.DataFrame({
        'Missing': total,
        'Percent': percent
    })
```

### 2. Missing Heatmap

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.imshow(df.isnull(), aspect='auto', cmap='gray')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.title('Missing Data Pattern')
```

### 3. Per-row Missing Count

```python
df['missing_count'] = df.isnull().sum(axis=1)
```

## Practical Example

Detect missing values in weather data.

### 1. Load Data

```python
url = "https://raw.githubusercontent.com/codebasics/py/master/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv"
df = pd.read_csv(url, index_col='day', parse_dates=True)
print(df)
```

### 2. Identify Missing

```python
print(df.isnull())
print(f"Total missing: {df.isnull().sum().sum()}")
```

### 3. Missing by Column

```python
print(df.isnull().sum())
```
