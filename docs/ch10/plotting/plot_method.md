# The plot() Method

Pandas provides built-in plotting capabilities through the `plot()` method available on both Series and DataFrame objects. This method is a convenient wrapper around matplotlib that simplifies common visualization tasks.

## Basic Usage

### Series.plot()

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a Series
s = pd.Series([1, 3, 2, 4, 3, 5], index=pd.date_range('2024-01-01', periods=6))

# Simple line plot
s.plot()
plt.show()
```

### DataFrame.plot()

```python
# Create a DataFrame
df = pd.DataFrame({
    'A': np.random.randn(10).cumsum(),
    'B': np.random.randn(10).cumsum(),
    'C': np.random.randn(10).cumsum()
}, index=pd.date_range('2024-01-01', periods=10))

# Plot all columns
df.plot()
plt.show()
```

Each column becomes a separate line with automatic legend.

## Selecting Columns to Plot

### Single Column

```python
df['A'].plot()
# or
df.plot(y='A')
```

### Multiple Columns

```python
df[['A', 'B']].plot()
# or
df.plot(y=['A', 'B'])
```

## Real-World Example: Stock Prices

```python
import yfinance as yf

# Download stock data
ticker = 'WMT'
df = yf.Ticker(ticker).history(start='2020-01-01', end='2020-12-31')

# Plot High and Low prices
fig, ax = plt.subplots(figsize=(12, 4))
df[['High', 'Low']].plot(title=f'{ticker} High/Low Prices', ax=ax)
plt.show()
```

## Using x and y Parameters

For DataFrames with non-index x-axis data:

```python
import yfinance as yf

# Get options data
ticker = 'AAPL'
company = yf.Ticker(ticker)
maturity = company.options[0]
calls = company.option_chain(maturity).calls

# Plot strike price vs last price
fig, ax = plt.subplots(figsize=(10, 4))
calls.plot(x='strike', y='lastPrice', ax=ax)
ax.set_title(f'{ticker} Call Options - {maturity}')
plt.show()
```

## Index as X-Axis

By default, the DataFrame index is used as the x-axis:

```python
# DatetimeIndex becomes x-axis automatically
df = pd.DataFrame({
    'price': [100, 102, 101, 105, 103]
}, index=pd.date_range('2024-01-01', periods=5))

df.plot()  # Dates on x-axis
plt.show()
```

## Multiple Subplots with subplots=True

Plot each column in a separate subplot:

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
df[['Open', 'High', 'Low', 'Close']].plot(subplots=True, ax=axes.flatten())
plt.tight_layout()
plt.show()
```

Or let pandas create the subplots:

```python
df[['Open', 'High', 'Low', 'Close']].plot(subplots=True, figsize=(12, 8), layout=(2, 2))
plt.tight_layout()
plt.show()
```

## Why Use pandas plot()?

| Feature | pandas plot() | matplotlib directly |
|---------|---------------|---------------------|
| Setup | Minimal | More boilerplate |
| Legend | Automatic | Manual |
| Index handling | Automatic | Manual |
| Column iteration | Automatic | Manual loop |
| Quick exploration | ✅ Ideal | Overkill |
| Fine customization | Limited | Full control |

**Use pandas plot() for:**
- Quick data exploration
- Simple visualizations
- Prototyping before detailed plots

**Use matplotlib directly for:**
- Publication-quality figures
- Complex layouts
- Fine-grained control

## Method Signature

```python
DataFrame.plot(
    x=None,           # Column for x-axis
    y=None,           # Column(s) for y-axis
    kind='line',      # Plot type
    ax=None,          # Matplotlib axes object
    subplots=False,   # Separate subplot per column
    figsize=None,     # Figure size (width, height)
    title=None,       # Plot title
    grid=False,       # Show grid
    legend=True,      # Show legend
    **kwargs          # Additional matplotlib kwargs
)
```

## Summary

The `plot()` method provides quick visualization directly from pandas objects:

```python
# Series
s.plot()

# DataFrame - all columns
df.plot()

# DataFrame - selected columns
df[['A', 'B']].plot()

# DataFrame - specify x and y
df.plot(x='col1', y='col2')

# Multiple subplots
df.plot(subplots=True)
```
