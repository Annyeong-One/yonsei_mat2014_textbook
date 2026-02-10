# Window with GroupBy

Combine window functions with groupby to apply rolling, expanding, or EWM calculations within groups.

## Rolling Within Groups

Apply rolling calculations per group.

### 1. Basic Pattern

```python
import pandas as pd

df = pd.DataFrame({
    'Ticker': ['AAPL', 'AAPL', 'AAPL', 'MSFT', 'MSFT', 'MSFT'],
    'Date': pd.date_range('2024-01-01', periods=3).tolist() * 2,
    'Close': [150, 152, 151, 350, 355, 353]
})

df['5D_MA'] = df.groupby('Ticker')['Close'].rolling(window=2).mean().reset_index(0, drop=True)
print(df)
```

### 2. Using transform

```python
df['MA'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.rolling(2).mean()
)
```

### 3. Preserves Original Index

The transform approach maintains alignment with original DataFrame.

## Expanding Within Groups

Cumulative calculations per group.

### 1. Cumulative Mean per Group

```python
df['Cum_Mean'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.expanding().mean()
)
```

### 2. Running Max per Group

```python
df['Running_Max'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.expanding().max()
)
```

### 3. Since-Inception Return per Asset

```python
df['Since_Start'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x / x.iloc[0] - 1
)
```

## EWM Within Groups

Exponentially weighted calculations per group.

### 1. EWMA per Asset

```python
df['EWMA'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.ewm(span=10).mean()
)
```

### 2. EWM Volatility per Asset

```python
returns = df.groupby('Ticker')['Close'].pct_change()
df['EWM_Vol'] = returns.groupby(df['Ticker']).transform(
    lambda x: x.ewm(span=20).std()
)
```

### 3. Independent Decay per Group

Each group's EWM is calculated independently.

## Practical Example

Multi-asset portfolio analysis.

### 1. Sample Data

```python
import numpy as np

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=50)
tickers = ['AAPL', 'MSFT', 'GOOGL']

data = []
for ticker in tickers:
    prices = 100 + np.cumsum(np.random.randn(50))
    for date, price in zip(dates, prices):
        data.append({'Ticker': ticker, 'Date': date, 'Close': price})

df = pd.DataFrame(data)
```

### 2. Add Rolling Stats per Asset

```python
df['MA20'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.rolling(20).mean()
)

df['Vol20'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.pct_change().rolling(20).std()
)
```

### 3. Cross-sectional Rank

```python
# Rank within each date
df['Rank'] = df.groupby('Date')['Close'].rank()
```

## Performance Tip

Efficient grouped window operations.

### 1. Single transform Call

```python
# Faster: single grouped operation
df['MA'] = df.groupby('Ticker')['Close'].transform(
    lambda x: x.rolling(20).mean()
)
```

### 2. Avoid Looping

```python
# Slower: don't loop over groups
# for ticker in df['Ticker'].unique():
#     ...
```

### 3. Use Built-in When Possible

GroupBy rolling is optimized internally.
