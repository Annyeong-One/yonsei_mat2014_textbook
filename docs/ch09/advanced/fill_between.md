# Fill and Fill Between


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Fill regions in your plots to highlight areas of interest.

---

## ax.fill()

Fill a closed polygon:

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = 5
chi2_statistics = 12.5

fig, ax = plt.subplots()

# Area before statistic
x = np.linspace(0, chi2_statistics, 100)
y = stats.chi2(df).pdf(x)
x = np.concatenate([[0], x, [chi2_statistics], [0]])
y = np.concatenate([[0], y, [0], [0]])
ax.fill(x, y, color='b', alpha=0.3)
ax.plot(x, y, color='b', linewidth=3)

# Area after statistic (p-value region)
x = np.linspace(chi2_statistics, 20, 100)
y = stats.chi2(df).pdf(x)
x = np.concatenate([[chi2_statistics], x, [20], [chi2_statistics]])
y = np.concatenate([[0], y, [0], [0]])
ax.fill(x, y, color='r', alpha=0.3)
ax.plot(x, y, color='r', linewidth=3)

ax.annotate('p value', 
            xy=((chi2_statistics + 15.0) / 2, 0.01),
            xytext=(16.5, 0.10),
            fontsize=15,
            arrowprops=dict(color='k', width=0.2, headwidth=8))

ax.set_title(f'Chi-Square Distribution (df={df})')
plt.show()
```

---

## ax.fill_between()

Fill the area between two curves or between a curve and a baseline:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'b-', linewidth=2)
ax.fill_between(x, y, alpha=0.3)
ax.axhline(0, color='black', linewidth=0.5)
plt.show()
```

---

## Filling Between Two Curves

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(x) * 0.5

fig, ax = plt.subplots()
ax.plot(x, y1, 'b-', label='sin(x)')
ax.plot(x, y2, 'r-', label='0.5*sin(x)')
ax.fill_between(x, y1, y2, alpha=0.3, color='green')
ax.legend()
plt.show()
```

---

## Conditional Filling with where

Use the `where` parameter to fill only specific regions:

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

    fig, ax = plt.subplots(figsize=(15, 3))

    ax.plot(DATE, y, label='AAPL', color='b')
    ax.plot(DATE, y_15, label='M15', color='g')
    ax.plot(DATE, y_50, label='M50', color='r')

    # Fill where M15 > M50 (bullish)
    ax.fill_between(DATE, y_15, y_50,
                    where=(y_15 > y_50), 
                    interpolate=True, 
                    color='r',
                    alpha=0.3)
    
    # Fill where M15 <= M50 (bearish)
    ax.fill_between(DATE, y_15, y_50,
                    where=(y_15 <= y_50), 
                    interpolate=True, 
                    color='b',
                    alpha=0.3)

    ax.set_xlabel('DATE')
    ax.set_ylabel('STOCK PRICE')
    ax.set_title('AAPL - Moving Average Crossover')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```

---

## fill_between Parameters

```python
ax.fill_between(
    x,                    # x coordinates
    y1,                   # First y boundary
    y2=0,                 # Second y boundary (default: 0)
    where=None,           # Boolean array for conditional filling
    interpolate=False,    # Interpolate at boundaries
    step=None,            # 'pre', 'post', 'mid' for step functions
    color='blue',         # Fill color
    alpha=0.5,            # Transparency
    label='label'         # For legend
)
```

---

## fill_betweenx()

Fill horizontally (between x values for given y):

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 2*np.pi, 100)
x = np.sin(y)

fig, ax = plt.subplots()
ax.plot(x, y, 'b-')
ax.fill_betweenx(y, x, alpha=0.3)
ax.axvline(0, color='black', linewidth=0.5)
plt.show()
```

---

## Confidence Intervals

Common use case for uncertainty visualization:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)
y_err = 0.2 + 0.1 * np.random.randn(50)

fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label='Mean')
ax.fill_between(x, y - y_err, y + y_err, alpha=0.3, label='±1 std')
ax.legend()
ax.set_title('Confidence Interval')
plt.show()
```

---

## Key Takeaways

- `ax.fill()` fills closed polygons
- `ax.fill_between()` fills between curves
- Use `where` for conditional filling
- Set `interpolate=True` for smooth boundaries
- `fill_betweenx()` fills horizontally
- Great for confidence intervals and crossover signals
