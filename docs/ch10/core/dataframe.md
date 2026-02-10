# DataFrame

A **DataFrame** is a two-dimensional labeled data structure with columns of potentially different types. It is the primary pandas data structure for tabular data, analogous to a spreadsheet or SQL table.

## Conceptual Overview

A DataFrame can be thought of as:
- A dictionary of Series objects sharing the same index
- A 2D NumPy array with row and column labels
- An Excel spreadsheet with named columns

```python
import pandas as pd

df = pd.DataFrame({
    "price": [100, 101, 102],
    "volume": [10, 12, 9],
})
print(df)
```

```
   price  volume
0    100      10
1    101      12
2    102       9
```

## Creating a DataFrame

### From a Dictionary of Lists

The most common creation method. Keys become column names, values become column data.

```python
df = pd.DataFrame({
    "city": ["mumbai", "delhi"],
    "temperature": [32, 45],
    "humidity": [70, 60],
})
print(df)
```

```
     city  temperature  humidity
0  mumbai           32        70
1   delhi           45        60
```

### From a List of Dictionaries

Each dictionary represents a row. Keys become column names.

```python
df = pd.DataFrame([
    {'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'name': 'Bob', 'age': 30, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35}  # Missing 'city' becomes NaN
])
print(df)
```

```
      name  age city
0    Alice   25  NYC
1      Bob   30   LA
2  Charlie   35  NaN
```

### With Custom Index

```python
df = pd.DataFrame(
    {"price": [100, 101, 102]},
    index=["day1", "day2", "day3"]
)
print(df)
```

```
      price
day1    100
day2    101
day3    102
```

### From NumPy Array

```python
import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(data, columns=['A', 'B'], index=['x', 'y', 'z'])
print(df)
```

```
   A  B
x  1  2
y  3  4
z  5  6
```

## DataFrame Attributes

### shape

Returns the dimensionality as (rows, columns).

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print(df.shape)  # (891, 12)
```

### columns

The column labels as an Index object.

```python
print(df.columns)
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', ...])
```

### index

The row labels.

```python
print(df.index)
# RangeIndex(start=0, stop=891, step=1)
```

### dtypes

Data types of each column.

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

### values

The underlying data as a NumPy array.

```python
print(type(df.values))  # <class 'numpy.ndarray'>
print(df.values.shape)  # (891, 12)
```

## Column Access

### Bracket Notation (Recommended)

```python
# Single column -> returns Series
price_series = df["price"]
print(type(price_series))  # <class 'pandas.core.series.Series'>

# Multiple columns -> returns DataFrame
subset = df[["price", "volume"]]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

### Attribute Access (Use Cautiously)

```python
# Works for simple column names
df.price

# Fails if column name:
# - Contains spaces
# - Starts with a number
# - Conflicts with DataFrame methods (e.g., 'count', 'mean')
```

### Adding New Columns

```python
# Direct assignment
df["return"] = df["price"].pct_change()

# Using assign() for method chaining
df = df.assign(
    return_pct=lambda x: x["price"].pct_change(),
    volume_ma=lambda x: x["volume"].rolling(3).mean()
)
```

## Row Access

### Using loc (Label-based)

```python
df = pd.DataFrame(
    {"price": [100, 101, 102]},
    index=["day1", "day2", "day3"]
)

df.loc["day1"]           # Single row as Series
df.loc[["day1", "day3"]] # Multiple rows as DataFrame
df.loc["day1", "price"]  # Specific cell
```

### Using iloc (Position-based)

```python
df.iloc[0]        # First row as Series
df.iloc[0:2]      # First two rows as DataFrame
df.iloc[0, 0]     # First cell
df.iloc[-1]       # Last row
```

### Slicing Rows

```python
df[0:2]           # First two rows (position-based slicing)
df["day1":"day2"] # Label-based slicing (inclusive)
```

## DataFrame Operations

### Arithmetic Operations

Operations align by index and column labels.

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})

print(df1 + df2)
```

```
    A   B
0  11  33
1  22  44
```

### Broadcasting with Series

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
s = pd.Series([10, 100], index=['A', 'B'])

print(df * s)  # Multiplies each column by corresponding Series value
```

```
    A    B
0  10  400
1  20  500
2  30  600
```

## Financial Context

DataFrames are the standard structure for financial data analysis.

### Price Histories

```python
import pandas as pd

prices = pd.DataFrame({
    "AAPL": [150, 151, 152, 153, 154],
    "MSFT": [300, 301, 302, 303, 304],
    "GOOGL": [140, 141, 142, 143, 144]
}, index=pd.date_range("2024-01-01", periods=5))

print(prices)
```

```
            AAPL  MSFT  GOOGL
2024-01-01   150   300    140
2024-01-02   151   301    141
2024-01-03   152   302    142
2024-01-04   153   303    143
2024-01-05   154   304    144
```

### Returns Calculation

```python
# Daily returns
returns = prices.pct_change()

# Cumulative returns
cumulative_returns = (1 + returns).cumprod() - 1
```

### Risk Metrics

```python
import numpy as np

# Annualized volatility
volatility = returns.std() * np.sqrt(252)

# Correlation matrix
correlation = returns.corr()

# Covariance matrix
covariance = returns.cov() * 252  # Annualized
```

### Portfolio Analysis

```python
# Portfolio weights
weights = pd.Series({'AAPL': 0.4, 'MSFT': 0.35, 'GOOGL': 0.25})

# Portfolio return
portfolio_return = (returns * weights).sum(axis=1)

# Portfolio volatility
portfolio_vol = np.sqrt(weights @ covariance @ weights)
```

## DataFrame vs Series

| Aspect | Series | DataFrame |
|--------|--------|-----------|
| Dimensions | 1D | 2D |
| Access single item | `s['label']` | `df.loc[row, col]` |
| Selecting subset | Returns Series | Returns Series or DataFrame |
| Typical use | Single variable | Multiple variables |
| Column relationship | N/A | Each column is a Series |
