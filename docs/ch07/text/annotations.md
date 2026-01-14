# Annotations

Annotations combine text with arrows to highlight specific features in your plot.

---

## Basic Annotation

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 3))

ax.grid(True)
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.05, 0.25)
ax.axhline(0, xmin=-0.5, xmax=3.5)

# Plot a point
ax.plot(1, 0, "o")

# Annotate the point
ax.annotate(
    "Annotation",                    # Text
    fontsize=14,
    family="serif",
    xy=(1, 0),                       # Point to annotate
    xytext=(+20, +50),               # Text position offset
    textcoords="offset points",      # Offset in points from xy
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.5")
)

plt.show()
```

---

## annotate() Parameters

Key parameters:

```python
ax.annotate(
    text,                    # Annotation text
    xy=(x, y),               # Point to annotate
    xytext=(x, y),           # Text position
    xycoords='data',         # Coordinate system for xy
    textcoords='data',       # Coordinate system for xytext
    fontsize=12,
    fontweight='bold',
    color='black',
    ha='center',             # Horizontal alignment
    va='center',             # Vertical alignment
    arrowprops=dict(...)     # Arrow properties
)
```

---

## Arrow Styles

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

arrow_styles = ['->', '-[', '|-|', '-|>', '<->', '<|-|>', 'fancy', 'simple', 'wedge']

for i, style in enumerate(arrow_styles):
    y = 9 - i
    ax.plot(2, y, 'ko', ms=5)
    ax.annotate(
        f"arrowstyle='{style}'",
        xy=(2, y),
        xytext=(5, y),
        fontsize=10,
        arrowprops=dict(arrowstyle=style, color='blue')
    )

plt.show()
```

---

## Connection Styles

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

connection_styles = [
    'arc3,rad=0',
    'arc3,rad=0.3',
    'arc3,rad=-0.3',
    'angle,angleA=0,angleB=90',
    'angle3,angleA=0,angleB=90',
    'arc,angleA=0,angleB=90,armA=30,armB=30,rad=0'
]

for i, style in enumerate(connection_styles):
    y = 9 - i * 1.5
    ax.plot(2, y, 'ko', ms=5)
    ax.annotate(
        style[:20] + '...' if len(style) > 20 else style,
        xy=(2, y),
        xytext=(6, y),
        fontsize=9,
        arrowprops=dict(
            arrowstyle='->',
            connectionstyle=style,
            color='green'
        )
    )

plt.show()
```

---

## Coordinate Systems

Different coordinate systems for `xycoords` and `textcoords`:

| Value | Description |
|-------|-------------|
| `'data'` | Data coordinates (default) |
| `'axes fraction'` | Fraction of axes (0-1) |
| `'figure fraction'` | Fraction of figure (0-1) |
| `'offset points'` | Offset in points from xy |
| `'offset pixels'` | Offset in pixels from xy |

---

## Practical Example: Statistical Plot

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

df = 5
chi2_statistic = 12.5

fig, ax = plt.subplots()

# Plot chi-square distribution
x = np.linspace(0, 20, 200)
y = stats.chi2(df).pdf(x)
ax.plot(x, y, 'b-', lw=2)
ax.fill_between(x, y, where=(x >= chi2_statistic), alpha=0.3, color='red')

# Annotate the p-value region
xy = ((chi2_statistic + 15.0) / 2, 0.01)
xytext = (16.5, 0.10)

ax.annotate(
    'p-value',
    xy=xy,
    xytext=xytext,
    fontsize=15,
    arrowprops=dict(color='k', width=0.2, headwidth=8)
)

ax.set_xlabel('$\\chi^2$')
ax.set_ylabel('Density')
ax.set_title(f'Chi-Square Distribution (df={df})')

plt.show()
```

---

## Financial Data Annotation

```python
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

def main():
    ticker = 'AAPL'
    data = yf.download(ticker, start='2023-01-01', end='2024-12-31')
    
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.plot(data['Close'], label=ticker)
    
    # Mark a specific date
    date_to_mark = pd.to_datetime('2023-12-20')
    price = data.loc[date_to_mark, 'Close']
    
    ax.plot(date_to_mark, price, 'ro', ms=10)
    ax.annotate(
        'Dec 20, 2023',
        xy=(date_to_mark, price),
        xytext=(date_to_mark, price + 10),
        fontsize=10,
        ha='center',
        arrowprops=dict(arrowstyle='->', color='red')
    )
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- `ax.annotate()` adds text with an arrow to a point
- `xy` is the point to annotate
- `xytext` is where the text appears
- `arrowprops` controls arrow appearance
- Use `arrowstyle` for arrow head style
- Use `connectionstyle` for arrow path shape
- `textcoords='offset points'` is useful for relative positioning
