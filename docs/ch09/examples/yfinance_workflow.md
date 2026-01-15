# Financial Data Workflow

## Data Download

### 1. Single Ticker

```python
import yfinance as yf

df = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
print(type(df))  # DataFrame
print(df.columns)  # ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
```

### 2. Index Types

```python
print(type(df.index))  # DatetimeIndex
print(df.index[0])     # Timestamp('2023-01-03')
```

### 3. Access Patterns

```python
# By label
df.loc['2023-01-03', 'Close']

# By position
df.iloc[0, 3]

# Column
df['Close']
```

## Multi-Asset Analysis

### 1. Multiple Tickers

```python
tickers = ["AAPL", "MSFT", "GOOGL"]
df = yf.download(tickers, start="2023-01-01")
```

### 2. MultiIndex Columns

```python
print(df.columns)
# MultiIndex([('Open', 'AAPL'), ('Open', 'MSFT'), ...])

# Access
df['Close']['AAPL']  # Apple closing prices
df[('Close', 'AAPL')]  # Alternative
```

### 3. Comparison

```python
# Normalize to first day
normalized = df['Close'] / df['Close'].iloc[0]
normalized.plot(figsize=(12, 6))
```

## Visualization

### 1. Price Series

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))
df['Close'].plot(ax=ax)
ax.set_ylabel('Price ($)')
ax.set_title('AAPL Closing Price')
plt.show()
```

### 2. Multiple Assets

```python
fig, ax = plt.subplots(figsize=(12, 6))
for ticker in ['AAPL', 'MSFT', 'GOOGL']:
    (df['Close'][ticker] / df['Close'][ticker].iloc[0]).plot(ax=ax, label=ticker)
ax.legend()
ax.set_ylabel('Normalized Price')
plt.show()
```

### 3. Volume

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
df['Close'].plot(ax=ax1)
df['Volume'].plot(ax=ax2, color='gray', alpha=0.5)
ax1.set_ylabel('Price')
ax2.set_ylabel('Volume')
```

## Analysis

### 1. Returns

```python
# Daily returns
returns = df['Close'].pct_change()
returns.plot(kind='hist', bins=50, alpha=0.6)
```

### 2. Moving Averages

```python
df['MA20'] = df['Close'].rolling(20).mean()
df['MA50'] = df['Close'].rolling(50).mean()

fig, ax = plt.subplots(figsize=(12, 6))
df[['Close', 'MA20', 'MA50']].plot(ax=ax)
ax.set_title('Price with Moving Averages')
```

### 3. Volatility

```python
# 20-day rolling volatility
volatility = returns.rolling(20).std() * np.sqrt(252)
volatility.plot(figsize=(12, 4))
```
