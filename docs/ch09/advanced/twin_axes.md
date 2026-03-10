# Twin Axes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Twin axes allow plotting data with different scales on the same figure.

---

## twinx()

Create a second y-axis sharing the same x-axis:

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

    fig, ax = plt.subplots(figsize=(15, 3))

    # Primary axis: price
    ax.plot(DATE, y_price, label='AAPL', color='b')
    ax.set_ylim([90, 140])
    ax.set_xlabel('DATE')
    ax.set_ylabel('STOCK PRICE')
    ax.set_title('AAPL')

    # Secondary axis: volume
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

## twiny()

Create a second x-axis sharing the same y-axis:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'b-')
ax.set_xlabel('Radians', color='blue')
ax.tick_params(axis='x', labelcolor='blue')

# Create twin axis for degrees
ax2 = ax.twiny()
ax2.plot(np.degrees(x), y, 'r-', alpha=0)  # Invisible line to set range
ax2.set_xlabel('Degrees', color='red')
ax2.tick_params(axis='x', labelcolor='red')

plt.show()
```

---

## Synchronizing Axes

When using twin axes, ensure they align logically:

```python
import matplotlib.pyplot as plt
import numpy as np

# Temperature conversion example
x = np.linspace(0, 100, 50)
celsius = x
fahrenheit = celsius * 9/5 + 32

fig, ax1 = plt.subplots()

# Celsius axis
ax1.plot(x, celsius, 'b-', label='Celsius')
ax1.set_xlabel('Sample')
ax1.set_ylabel('Temperature (°C)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Fahrenheit axis
ax2 = ax1.twinx()
ax2.plot(x, fahrenheit, 'r-', label='Fahrenheit')
ax2.set_ylabel('Temperature (°F)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
plt.show()
```

---

## Legend with Twin Axes

Combine legends from both axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax1 = plt.subplots()

line1, = ax1.plot(x, np.sin(x), 'b-', label='sin(x)')
ax1.set_ylabel('sin(x)', color='blue')

ax2 = ax1.twinx()
line2, = ax2.plot(x, np.exp(x/10), 'r-', label='exp(x/10)')
ax2.set_ylabel('exp(x/10)', color='red')

# Combine legends
lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left')

plt.show()
```

---

## Three Axes Example

Add a third axis using spine manipulation:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax1 = plt.subplots()
fig.subplots_adjust(right=0.75)

# First y-axis
ax1.plot(x, np.sin(x), 'b-')
ax1.set_ylabel('sin(x)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Second y-axis
ax2 = ax1.twinx()
ax2.plot(x, np.cos(x), 'r-')
ax2.set_ylabel('cos(x)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Third y-axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(x, np.tan(x), 'g-')
ax3.set_ylabel('tan(x)', color='green')
ax3.tick_params(axis='y', labelcolor='green')
ax3.set_ylim(-10, 10)

plt.show()
```

---

## Key Takeaways

- `ax.twinx()` creates a second y-axis
- `ax.twiny()` creates a second x-axis
- Color-code axes and labels for clarity
- Combine legends manually when using twin axes
- Adjust spine positions for additional axes
