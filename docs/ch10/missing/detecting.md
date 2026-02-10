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

pandas treats several values as missing, but they behave differently.

### The Three Main Missing Types

| Type | Package | Works With | Propagates |
|------|---------|------------|------------|
| `np.nan` | NumPy | float only | Yes |
| `None` | Python | object dtype | Yes |
| `pd.NA` | pandas | All nullable dtypes | Yes |

### 1. np.nan (NumPy NaN)

The traditional missing value, but only works with float dtype.

```python
import numpy as np
import pandas as pd

# np.nan is a float
print(type(np.nan))  # <class 'float'>

# Integer column with np.nan converts to float!
s = pd.Series([1, 2, np.nan])
print(s.dtype)  # float64 (not int!)
print(s)
```

```
0    1.0
1    2.0
2    NaN
dtype: float64
```

**Key behaviors:**
```python
# NaN is not equal to itself
print(np.nan == np.nan)  # False

# Arithmetic with NaN propagates
print(1 + np.nan)  # nan

# Use isna() to detect
print(pd.isna(np.nan))  # True
```

### 2. None (Python None)

Python's built-in null, stored in object dtype.

```python
s = pd.Series([1, None, 3])
print(s.dtype)  # object (not numeric!)
print(s)
```

```
0       1
1    None
2       3
dtype: object
```

**Behavior in different contexts:**
```python
# In numeric Series, None becomes np.nan
s = pd.Series([1.0, None, 3.0])
print(s.dtype)  # float64
print(s[1])     # nan (converted from None)

# In string Series, stays as None but detected as missing
s = pd.Series(['a', None, 'c'])
print(s.isnull())  # [False, True, False]
```

### 3. pd.NA (pandas NA) - Recommended

Introduced in pandas 1.0, works with all nullable dtypes.

```python
# pd.NA works with nullable integer dtype
s = pd.Series([1, 2, pd.NA], dtype='Int64')  # Note capital I
print(s.dtype)  # Int64
print(s)
```

```
0       1
1       2
2    <NA>
dtype: Int64
```

**Why pd.NA is better:**
```python
# Integer column stays integer!
s = pd.Series([1, 2, pd.NA], dtype='Int64')
print(s.dtype)  # Int64 (preserved!)

# Boolean column stays boolean
b = pd.Series([True, False, pd.NA], dtype='boolean')
print(b.dtype)  # boolean

# String column with proper type
st = pd.Series(['a', 'b', pd.NA], dtype='string')
print(st.dtype)  # string
```

### 4. NaT (Not a Time)

Special missing value for datetime types.

```python
dates = pd.Series([pd.Timestamp('2024-01-01'), pd.NaT, pd.Timestamp('2024-01-03')])
print(dates)
print(dates.isnull())
```

```
0   2024-01-01
1          NaT
2   2024-01-03
dtype: datetime64[ns]

0    False
1     True
2    False
dtype: bool
```

### Comparison Table

```python
# Create Series with different missing types
s_nan = pd.Series([1, np.nan, 3])           # float64
s_none = pd.Series([1, None, 3])            # object  
s_na = pd.Series([1, pd.NA, 3], dtype='Int64')  # Int64

print("np.nan Series:")
print(f"  dtype: {s_nan.dtype}, missing: {s_nan.isnull().sum()}")

print("None Series:")
print(f"  dtype: {s_none.dtype}, missing: {s_none.isnull().sum()}")

print("pd.NA Series:")
print(f"  dtype: {s_na.dtype}, missing: {s_na.isnull().sum()}")
```

### Nullable Dtypes

Use nullable dtypes to maintain proper types with missing values:

| Standard dtype | Nullable dtype |
|---------------|----------------|
| int64 | Int64 |
| float64 | Float64 |
| bool | boolean |
| object (str) | string |

```python
# Convert to nullable dtypes
df = pd.DataFrame({
    'int_col': [1, 2, None],
    'float_col': [1.0, None, 3.0],
    'str_col': ['a', None, 'c'],
    'bool_col': [True, None, False]
})

# Convert all to nullable dtypes
df = df.convert_dtypes()
print(df.dtypes)
```

```
int_col      Int64
float_col    Float64
str_col      string
bool_col     boolean
dtype: object
```

### Best Practice Recommendations

1. **For new code**: Use `pd.NA` with nullable dtypes
2. **For compatibility**: `np.nan` is still widely used
3. **For databases**: `None` may appear from SQL NULLs
4. **For datetime**: `pd.NaT` is automatically used

```python
# Recommended: Use convert_dtypes() for automatic handling
df = pd.read_csv('data.csv').convert_dtypes()
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
