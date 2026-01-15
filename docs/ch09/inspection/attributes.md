# DataFrame Attributes

DataFrame attributes provide information about the structure and properties of your data.

## columns

Access column labels.

### 1. Get Columns

```python
import pandas as pd
import yfinance as yf

df = yf.Ticker('WMT').history(start='2020-01-01', end='2020-12-31')
print(df.columns)
```

```
Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'], dtype='object')
```

### 2. Access by Position

```python
print(df.columns[0])  # 'Open'
print(type(df.columns[0]))  # <class 'str'>
```

### 3. Convert to List

```python
col_list = df.columns.tolist()
```

## index

Access row labels.

### 1. Get Index

```python
print(df.index)
```

```
DatetimeIndex(['2020-01-02', '2020-01-03', ...], dtype='datetime64[ns]', name='Date', freq=None)
```

### 2. Access by Position

```python
print(df.index[0])  # Timestamp('2020-01-02 00:00:00')
print(type(df.index[0]))  # <class 'pandas._libs.tslibs.timestamps.Timestamp'>
```

### 3. Index Properties

```python
print(df.index.name)  # 'Date'
print(df.index.dtype)  # datetime64[ns]
```

## shape

Get DataFrame dimensions.

### 1. Basic Shape

```python
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.shape)  # (891, 12)
```

### 2. After Selection

```python
df_subset = df[['Survived', 'Sex']]
print(df_subset.shape)  # (891, 2)
```

### 3. DataFrame vs Series

```python
df_col = df[['Survived']]  # DataFrame
print(df_col.shape)  # (891, 1)

series = df['Survived']  # Series
print(series.shape)  # (891,)
```

## values

Get underlying NumPy array.

### 1. Access Values

```python
x = df.values
print(type(x))  # <class 'numpy.ndarray'>
print(x.shape)  # Same as df.shape
```

### 2. Slicing Values

```python
print(x[1:2, 2:3].shape)  # (1, 1)
print(x[1:2, 2].shape)    # (1,)
print(x[1, 2].shape)      # () scalar
```

### 3. Prefer to_numpy()

```python
# Modern pandas recommends to_numpy()
arr = df.to_numpy()
```

## dtypes

Get data types of each column.

### 1. All dtypes

```python
print(df.dtypes)
```

```
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
...
```

### 2. DataFrame vs Series

```python
# DataFrame has dtypes (plural)
print(df.dtypes)

# Series has dtype (singular)
print(df['Age'].dtype)  # float64
```

### 3. Common Error

```python
# This raises AttributeError
try:
    print(df.dtype)  # Wrong! Use dtypes
except AttributeError as e:
    print(e)
```

## size

Total number of elements.

### 1. Get Size

```python
print(df.size)  # rows × columns
```

### 2. Calculation

```python
# Equivalent to
print(df.shape[0] * df.shape[1])
```

### 3. vs len()

```python
print(len(df))  # Number of rows only
print(df.size)  # Total elements
```

## ndim

Number of dimensions.

### 1. DataFrame ndim

```python
print(df.ndim)  # 2
```

### 2. Series ndim

```python
print(df['Age'].ndim)  # 1
```

### 3. Use Case

```python
if data.ndim == 1:
    print("Series")
else:
    print("DataFrame")
```

## empty

Check if DataFrame is empty.

### 1. Check Empty

```python
print(df.empty)  # False
```

### 2. Empty DataFrame

```python
empty_df = pd.DataFrame()
print(empty_df.empty)  # True
```

### 3. Conditional Logic

```python
if not df.empty:
    process_data(df)
```

## T (Transpose)

Transpose rows and columns.

### 1. Transpose

```python
df_t = df.T
print(df_t.shape)  # Swapped dimensions
```

### 2. Use Case

```python
# Useful for displaying wide DataFrames
print(df.head().T)
```

### 3. Method Alternative

```python
df_transposed = df.transpose()
```
