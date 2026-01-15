# Series and DataFrame

pandas provides two core data structures for tabular and time-series data: **Series** and **DataFrame**. They are built on top of NumPy arrays with rich indexing and metadata.

## Series

A **Series** is a one-dimensional labeled array capable of holding any data type.

### 1. Creating a Series

```python
import pandas as pd

s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
print(s)
```

```
a    1.0
b    2.0
c    3.0
dtype: float64
```

### 2. Key Properties

```python
print(s.values)  # NumPy array
print(s.index)   # Index object
print(s.dtype)   # Data type
print(s.name)    # Series name
```

### 3. From Dictionary

```python
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
```

## Accessing Series

Series supports both label-based and position-based access.

### 1. Label-based Access

```python
s["a"]           # Single label
s[["a", "c"]]    # Multiple labels
```

### 2. Position-based Access

```python
s.iloc[0]        # First element
s.iloc[0:2]      # First two elements
```

### 3. Boolean Indexing

```python
s[s > 1.5]       # Elements greater than 1.5
```

## DataFrame

A **DataFrame** is a two-dimensional table of labeled columns, where each column is a Series.

### 1. Creating a DataFrame

```python
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

### 2. From List of Dictionaries

```python
df = pd.DataFrame([
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
])
```

### 3. With Custom Index

```python
df = pd.DataFrame(
    {"price": [100, 101, 102]},
    index=["day1", "day2", "day3"]
)
```

## Column Access

Accessing columns returns a Series.

### 1. Bracket Notation

```python
df["price"]         # Single column (Series)
df[["price", "volume"]]  # Multiple columns (DataFrame)
```

### 2. Attribute Access

```python
df.price            # Works but use cautiously
```

Attribute access fails if column name conflicts with DataFrame methods.

### 3. Adding Columns

```python
df["return"] = df["price"].pct_change()
```

## Financial Context

DataFrames are the standard structure for financial data analysis.

### 1. Price Histories

```python
prices = pd.DataFrame({
    "AAPL": [150, 151, 152],
    "MSFT": [300, 301, 302]
}, index=pd.date_range("2024-01-01", periods=3))
```

### 2. Returns Calculation

```python
returns = prices.pct_change()
```

### 3. Risk Metrics

```python
volatility = returns.std() * np.sqrt(252)
```
