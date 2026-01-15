# Series

A **Series** is a one-dimensional labeled array capable of holding any data type. It is the fundamental building block of pandas, representing a single column of data with an associated index.

## Conceptual Overview

```
2D NumPy Array    Matrix-like data structure with a single dtype
DataFrame         Excel-like data structure where each column may have different dtype
Series            One column of Excel-like data structure with a single dtype
```

A Series combines the power of NumPy arrays with labeled indexing, making it ideal for time-series data and tabular column operations.

## Creating a Series

### From a List

```python
import pandas as pd

# Basic creation with default integer index
s = pd.Series([3, 9, 1])
print(s)
```

```
0    3
1    9
2    1
dtype: int64
```

### With Custom Index and Name

```python
data = [3, 9, 1]
name = "data"
index = pd.date_range(start='2019-09-01', end='2019-09-03')

s = pd.Series(data, name=name, index=index)
print(s)
```

```
2019-09-01    3
2019-09-02    9
2019-09-03    1
Freq: D, Name: data, dtype: int64
```

### From a Dictionary

When creating from a dictionary, keys become the index labels.

```python
data_dict = {
    '2019-09-01': 3,
    '2019-09-02': 9,
    '2019-09-03': 1
}
s = pd.Series(data_dict, name="data")
print(s)
```

```
2019-09-01    3
2019-09-02    9
2019-09-03    1
Name: data, dtype: int64
```

### From a DataFrame Column

Extracting a column from a DataFrame returns a Series.

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Bracket notation (preferred)
survived_series = df["Survived"]

# Dot notation (use cautiously)
survived_series = df.Survived

print(type(survived_series))  # <class 'pandas.core.series.Series'>
```

## Series Attributes

### dtype

The data type of the Series elements. Pandas performs automatic type inference and upcasting.

```python
# String data -> object dtype
s = pd.Series(['Boat', 'Car', 'Bike'])
print(f"{s.dtype = }")  # s.dtype = dtype('O')

# Integer data -> int64 dtype
s = pd.Series([1, 55, 99])
print(f"{s.dtype = }")  # s.dtype = dtype('int64')

# Float data -> float64 dtype
s = pd.Series([1., 55., 99.])
print(f"{s.dtype = }")  # s.dtype = dtype('float64')

# Mixed int/float -> upcasted to float64
s = pd.Series([1., 55, 99])
print(f"{s.dtype = }")  # s.dtype = dtype('float64')
```

### index

The labels associated with each element.

```python
s = pd.Series([3, 9, 1], index=pd.date_range(start='2019-09-01', end='2019-09-03'))
print(f"{s.index = }")
# s.index = DatetimeIndex(['2019-09-01', '2019-09-02', '2019-09-03'], dtype='datetime64[ns]', freq='D')
```

### name

An optional name for the Series, useful when converting to DataFrame.

```python
s = pd.Series([3, 9, 1], name="data")
print(f"{s.name = }")  # s.name = 'data'
```

### shape

The dimensionality of the Series as a tuple.

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.shape)              # (891, 12) - DataFrame
print(df[["Survived"]].shape)  # (891, 1) - DataFrame with one column
print(df["Survived"].shape)    # (891,) - Series
```

### values

The underlying NumPy array.

```python
import yfinance as yf

df = yf.Ticker('WMT').history(start='2020-01-01', end='2020-12-31')
print(f"{type(df.Close.values) = }")  # <class 'numpy.ndarray'>
print(f"{df.Close.values.shape = }")  # (252,)
print(f"{df.Close.values.dtype = }")  # dtype('float64')
```

## Accessing Series Elements

### Label-based Access

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

s["a"]           # Single label -> 10
s[["a", "c"]]    # Multiple labels -> Series
s.loc["a"]       # Explicit label-based access
```

### Position-based Access

```python
s.iloc[0]        # First element -> 10
s.iloc[0:2]      # First two elements -> Series
s.iloc[-1]       # Last element -> 30
```

### Boolean Indexing

```python
s[s > 15]        # Elements greater than 15
```

## Common Series Methods

### Statistical Methods

```python
s = pd.Series([3, 9, 1, 5, 7])

s.mean()     # 5.0
s.median()   # 5.0
s.sum()      # 25
s.std()      # Standard deviation
s.min()      # 1
s.max()      # 9
```

### Conversion Methods

```python
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

s.tolist()       # [1, 2, 3] - Convert to Python list
s.to_frame()     # Convert to DataFrame
s.to_numpy()     # Convert to NumPy array
```

### Value Inspection

```python
s = pd.Series([1, 2, 2, 3, 3, 3])

s.value_counts()  # Count occurrences of each value
s.nunique()       # Number of unique values -> 3
s.unique()        # Array of unique values -> [1, 2, 3]
```

## Financial Example

```python
import pandas as pd
import yfinance as yf

# Download stock data
ticker = 'AAPL'
df = yf.Ticker(ticker).history(start='2024-01-01', end='2024-06-30')

# Close prices as Series
close_prices = df['Close']

print(f"Mean price: ${close_prices.mean():.2f}")
print(f"Max price: ${close_prices.max():.2f}")
print(f"Min price: ${close_prices.min():.2f}")
print(f"Volatility: {close_prices.pct_change().std() * (252**0.5):.2%}")
```

## Series vs NumPy Array

| Feature | NumPy Array | pandas Series |
|---------|-------------|---------------|
| Indexing | Integer only | Label or integer |
| Alignment | Manual | Automatic by index |
| Missing data | No native support | Native NaN handling |
| Metadata | None | name, index attributes |
| Operations | Element-wise | Index-aligned |
