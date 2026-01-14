# Tick Formatters

Tick formatters control how tick labels are displayed.

---

## Using Formatters

Apply a formatter to an axis:

```python
import matplotlib as mpl

ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_minor_formatter(formatter)
ax.yaxis.set_minor_formatter(formatter)
```

---

## NullFormatter

Remove tick labels while keeping ticks:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x) * np.exp(-x**2/20)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.xaxis.set_major_formatter(mpl.ticker.NullFormatter())

plt.show()
```

---

## FuncFormatter

Custom formatting with a function:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def format_func(value, tick_number):
    # Convert to multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return "$\\pi/2$"
    elif N == -1:
        return "$-\\pi/2$"
    elif N == 2:
        return "$\\pi$"
    elif N == -2:
        return "$-\\pi$"
    elif N % 2 > 0:
        return f"${N}\\pi/2$"
    else:
        return f"${N // 2}\\pi$"

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(np.pi / 4))
ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(format_func))

plt.show()
```

---

## DateFormatter

Format datetime tick labels:

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import yfinance as yf

df = yf.Ticker('AAPL').history(start='2020-07-01', end='2020-12-31')

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(df.index, df['Close'])

# Date formatting
date_format = mpl_dates.DateFormatter('%b, %d %Y')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()
plt.show()
```

Date format codes:

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | Year (4 digit) | 2024 |
| `%y` | Year (2 digit) | 24 |
| `%m` | Month (number) | 01-12 |
| `%b` | Month (abbrev) | Jan |
| `%B` | Month (full) | January |
| `%d` | Day | 01-31 |
| `%H` | Hour (24h) | 00-23 |
| `%M` | Minute | 00-59 |
| `%S` | Second | 00-59 |

---

## StrMethodFormatter

Format using string format specification:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1, 100)
y = x ** 2 * 1000

fig, ax = plt.subplots()
ax.plot(x, y)

# Format with commas and 0 decimals
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.show()
```

---

## PercentFormatter

Format as percentages:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)

# xmax=1.0 means 1.0 = 100%
ax.yaxis.set_major_formatter(mpl.ticker.PercentFormatter(xmax=1.0))

plt.show()
```

---

## ScalarFormatter

Default formatter with scientific notation control:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1, 100)
y = x * 1e6

fig, ax = plt.subplots()
ax.plot(x, y)

formatter = mpl.ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-2, 2))
ax.yaxis.set_major_formatter(formatter)

plt.show()
```

---

## LogFormatter

For logarithmic scales:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(1, 100, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_yscale('log')

ax.yaxis.set_major_formatter(mpl.ticker.LogFormatterSciNotation())

plt.show()
```

---

## Common Formatters Summary

| Formatter | Description |
|-----------|-------------|
| `NullFormatter()` | No labels |
| `FuncFormatter(func)` | Custom function |
| `StrMethodFormatter(fmt)` | String format |
| `PercentFormatter(xmax)` | Percentage |
| `ScalarFormatter()` | Default with options |
| `LogFormatter()` | For log scales |
| `DateFormatter(fmt)` | Date/time |

---

## Complete Example

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mpl_dates
import numpy as np
import pandas as pd

# Create sample time series
dates = pd.date_range('2024-01-01', periods=100, freq='D')
values = np.cumsum(np.random.randn(100)) * 1000 + 50000

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(dates, values)

# Date formatter for x-axis
ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mpl_dates.MonthLocator())

# Currency formatter for y-axis
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('${x:,.0f}'))

ax.set_title('Portfolio Value')
fig.autofmt_xdate()
plt.show()
```

---

## Key Takeaways

- Formatters control how tick labels are displayed
- `NullFormatter` removes labels
- `FuncFormatter` allows custom formatting functions
- `DateFormatter` formats datetime values
- `StrMethodFormatter` uses Python string formatting
- `PercentFormatter` displays percentages
