# join Method

The `join()` method combines DataFrames based on their index. It provides a simpler syntax than merge for index-based operations.

## Basic Usage

Join two DataFrames by index.

### 1. Simple Join

```python
import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3]
}, index=['a', 'b', 'c'])

df2 = pd.DataFrame({
    'B': [4, 5, 6]
}, index=['a', 'b', 'd'])

result = df1.join(df2)
print(result)
```

```
     A    B
a  1.0  4.0
b  2.0  5.0
c  3.0  NaN
```

### 2. Default Left Join

join defaults to left join, keeping all left DataFrame rows.

### 3. Method vs Function

```python
df1.join(df2)           # Method syntax
# No pd.join() function  # Unlike merge
```

## Financial Example

Combine stock price data by date index.

### 1. Download Data

```python
import yfinance as yf

def download(ticker):
    return yf.Ticker(ticker).history(period="max")

tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
```

### 2. Iterative Join

```python
for i, ticker in enumerate(tickers):
    if i == 0:
        df = download(ticker).rename(columns={'Close': ticker})[[ticker]]
    else:
        dg = download(ticker).rename(columns={'Close': ticker})[[ticker]]
        df = df.join(dg, how="inner")

print(df.head(3))
print(df.tail(3))
```

### 3. Result

FAANG closing prices aligned by date.

## Joining Multiple DataFrames

Join several DataFrames at once.

### 1. List of DataFrames

```python
df1.join([df2, df3, df4])
```

### 2. Sequential Join

```python
result = df1.join(df2).join(df3).join(df4)
```

### 3. With Different How

```python
# All must use same how parameter
df1.join([df2, df3], how='outer')
```

## Suffix Handling

Handle overlapping column names.

### 1. lsuffix and rsuffix

```python
df1 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df2 = pd.DataFrame({'A': [3, 4]}, index=['x', 'y'])

df1.join(df2, lsuffix='_left', rsuffix='_right')
```

```
   A_left  A_right
x       1        3
y       2        4
```

### 2. Required for Overlaps

```python
# Without suffixes, overlapping columns raise error
# df1.join(df2)  # ValueError: columns overlap
```

### 3. Clear Naming

```python
df1.join(df2, lsuffix='_2023', rsuffix='_2024')
```

## Index Alignment

join aligns on index, not columns.

### 1. Different Index Types

```python
# Works with any compatible index types
# DatetimeIndex, RangeIndex, string index
```

### 2. Partial Overlap

```python
# Unmatched indices get NaN (or excluded in inner join)
```

### 3. on Parameter

```python
# Join left's column to right's index
df1.join(df2, on='key_column')
```
