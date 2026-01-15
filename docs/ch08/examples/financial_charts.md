# Financial Charts

Create professional financial visualizations with Matplotlib.

---

## Stock Price Chart

Basic price chart with volume:

```python
import matplotlib.pyplot as plt
import yfinance as yf

def download(ticker, start=None, end=None):
    if start is None:
        return yf.Ticker(ticker).history(period="max")
    else:
        return yf.Ticker(ticker).history(start=start, end=end)

def main():
    df = download('AAPL', start='2020-07-01', end='2020-12-31')

    DATE = df.index[50:]
    y_price = df['Close'].loc[DATE]
    y_volume = df['Volume'].loc[DATE]

    fig, ax = plt.subplots(figsize=(15, 4))

    ax.plot(DATE, y_price, label='AAPL', color='b')
    ax.set_xlabel('DATE')
    ax.set_ylabel('STOCK PRICE')
    ax.set_title('AAPL')

    ax2 = ax.twinx()
    ax2.fill_between(DATE, y_volume, color='gray', alpha=0.3)
    ax2.set_ylim([0.0, 1e9])
    ax2.set_ylabel('VOLUME')

    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Moving Average Crossover

```python
import matplotlib.pyplot as plt
import yfinance as yf

def download(ticker, start=None, end=None):
    if start is None:
        return yf.Ticker(ticker).history(period="max")
    else:
        return yf.Ticker(ticker).history(start=start, end=end)

def main():
    df = download('AAPL', start='2020-07-01', end='2020-12-31')
    df['M15'] = df['Close'].rolling(15).mean()
    df['M50'] = df['Close'].rolling(50).mean()

    DATE = df.index[50:]
    y = df['Close'].loc[DATE]
    y_15 = df['M15'].loc[DATE]
    y_50 = df['M50'].loc[DATE]

    fig, ax = plt.subplots(figsize=(15, 4))

    ax.plot(DATE, y, label='AAPL', color='b')
    ax.plot(DATE, y_15, label='MA15', color='g')
    ax.plot(DATE, y_50, label='MA50', color='r')

    ax.fill_between(DATE, y_15, y_50,
                    where=(y_15 > y_50), interpolate=True,
                    color='green', alpha=0.3, label='Bullish')
    ax.fill_between(DATE, y_15, y_50,
                    where=(y_15 <= y_50), interpolate=True,
                    color='red', alpha=0.3, label='Bearish')

    ax.set_xlabel('DATE')
    ax.set_ylabel('STOCK PRICE')
    ax.set_title('AAPL - Moving Average Crossover')
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()
```

---

## Marking Events

Highlight specific dates on a chart:

```python
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def download_stock_prices(ticker, start, end):
    return yf.download(ticker, start=start, end=end)

def display_stock_prices(data, ticker, event_date=None):
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(data['Close'], label=ticker)

    if event_date:
        date = pd.to_datetime(event_date)
        ax.plot(date, data.loc[date, 'Close'], 'ro', ms=10)
        ax.annotate(f'{event_date}',
                    xy=(date, data.loc[date, 'Close']),
                    xytext=(date, data.loc[date, 'Close'] + 5),
                    fontsize=10, ha='center',
                    arrowprops=dict(arrowstyle='->', color='red'))

    ax.set_xlabel('Date')
    ax.set_ylabel('Price (USD)')
    ax.legend()
    plt.show()

def main():
    ticker = 'AAPL'
    data = download_stock_prices(ticker, '2023-01-01', '2024-12-31')
    display_stock_prices(data, ticker, event_date='2023-12-20')

if __name__ == "__main__":
    main()
```

---

## Multi-Asset Comparison

```python
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

def main():
    tickers = ['AAPL', 'GOOGL', 'MSFT']
    start = '2023-01-01'
    end = '2024-01-01'

    fig, ax = plt.subplots(figsize=(12, 4))

    for ticker in tickers:
        data = yf.download(ticker, start=start, end=end)
        # Normalize to starting price
        normalized = data['Close'] / data['Close'].iloc[0] * 100
        ax.plot(normalized, label=ticker)

    ax.set_xlabel('Date')
    ax.set_ylabel('Normalized Price (Base=100)')
    ax.set_title('Tech Stock Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.show()

if __name__ == "__main__":
    main()
```

---

## Price with Date Formatting

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import yfinance as yf

def main():
    df = yf.Ticker('AAPL').history(start='2020-07-01', end='2020-12-31')

    fig, ax = plt.subplots(figsize=(15, 4))
    ax.plot(df.index, df['Close'])

    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')
    ax.set_title('AAPL Stock Price')

    # Format dates
    date_format = mpl_dates.DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(mpl_dates.MonthLocator())

    fig.autofmt_xdate()
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- Use `twinx()` for price and volume on same chart
- `fill_between()` visualizes moving average crossovers
- Mark events with `annotate()`
- Normalize prices for multi-asset comparison
- Use `DateFormatter` for proper date display
- `autofmt_xdate()` prevents label overlap
