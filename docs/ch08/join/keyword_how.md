# Keyword - how

The `how` parameter in `join()` specifies the type of join, controlling which rows are included based on index matching.

## Left Join (Default)

Keep all rows from the calling DataFrame.

### 1. Default Behavior

```python
import pandas as pd
import yfinance as yf

def download(ticker):
    return yf.Ticker(ticker).history(period="max")

tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']

for i, ticker in enumerate(tickers):
    if i == 0:
        df = download(ticker).rename(columns={'Close': ticker})[[ticker]]
    else:
        dg = download(ticker).rename(columns={'Close': ticker})[[ticker]]
        df = df.join(dg, how="left")  # Default

print(df.head(3))
```

### 2. Preserves Left Index

All dates from the first stock are kept.

### 3. NaN for Missing

Stocks without data for certain dates have NaN.

## Right Join

Keep all rows from the passed DataFrame.

### 1. Right Join Example

```python
for i, ticker in enumerate(tickers):
    if i == 0:
        df = download(ticker).rename(columns={'Close': ticker})[[ticker]]
    else:
        dg = download(ticker).rename(columns={'Close': ticker})[[ticker]]
        df = df.join(dg, how="right")

print(df.head(3))
```

### 2. Preserves Right Index

All dates from the joined stock are kept.

### 3. Use Case

When the right DataFrame has the authoritative index.

## Inner Join

Keep only rows with matching indices.

### 1. Inner Join Example

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

### 2. Intersection of Indices

Only dates present in all stocks.

### 3. No Missing Values

Inner join produces complete data without NaN.

## Outer Join

Keep all rows from both DataFrames.

### 1. Outer Join Example

```python
for i, ticker in enumerate(tickers):
    if i == 0:
        df = download(ticker).rename(columns={'Close': ticker})[[ticker]]
    else:
        dg = download(ticker).rename(columns={'Close': ticker})[[ticker]]
        df = df.join(dg, how="outer")

print(df.head(3))
print(df.tail(3))
```

### 2. Union of Indices

All dates from any stock are included.

### 3. Most Missing Values

Outer join may have many NaN values.

## Comparison

Summary of join types.

### 1. Row Counts

```python
# Given df1 (100 dates) and df2 (80 dates) with 60 overlap:
# how='left':  100 rows (all from df1)
# how='right':  80 rows (all from df2)
# how='inner':  60 rows (intersection)
# how='outer': 120 rows (union)
```

### 2. Best Practices

```python
# Inner: When you need complete data
# Left: When preserving primary DataFrame structure
# Outer: When you need all dates for analysis
```

### 3. Financial Context

```python
# Inner join for synchronized analysis
# Outer join for data completeness check
# Left join for preserving benchmark dates
```
