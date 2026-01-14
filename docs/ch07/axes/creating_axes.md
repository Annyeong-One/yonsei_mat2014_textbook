# Creating Axes

There are multiple ways to create Axes objects in Matplotlib, each suited for different use cases.

---

## plt.subplots

The most common method for creating figures with axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

With multiple subplots:

```python
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
```

---

## plt.axes

Create axes on the current figure:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.exp(x)

fig = plt.figure()
ax = plt.axes()
ax.plot(x, y)
plt.show()
```

With scale options:

```python
fig = plt.figure()
ax = plt.axes(yscale='log')  # Logarithmic y-axis
ax.plot(x, y)
plt.show()
```

---

## fig.add_axes

For precise positioning using normalized coordinates:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()

# [left, bottom, width, height] - values from 0 to 1
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y1)

plt.show()
```

---

## fig.add_subplot

Add subplots one at a time:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)

fig = plt.figure(figsize=(12, 6))

for s in range(12):
    ax = fig.add_subplot(3, 4, s + 1)
    ax.plot(x ** (s + 1))
    ax.set_title(f"x^{s+1}")

plt.tight_layout()
plt.show()
```

---

## plt.subplot2grid

Create subplots with varying sizes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

ax1.plot(x, y1)
ax2.plot(y1, x)
ax3.plot(x, y1)
ax4.plot(x, y2)
ax5.plot(y2, x)

fig.tight_layout()
plt.show()
```

Parameters:

- First tuple: grid shape `(nrows, ncols)`
- Second tuple: starting position `(row, col)`
- `colspan`: columns to span
- `rowspan`: rows to span

---

## GridSpec

For maximum control over subplot layout:

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()
gs = gridspec.GridSpec(2, 3, height_ratios=[2, 1], width_ratios=[1, 2, 1])

for i, g in enumerate(gs):
    ax = fig.add_subplot(g)
    if i % 2 == 0:
        ax.plot(x, y1)
    else:
        ax.plot(x, y2)

fig.tight_layout()
plt.show()
```

---

## Inset Axes

Create axes within axes for detail views:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()

ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Main axes
ax1 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # Inset axes

ax0.plot(x, y1)
ax1.plot(y1, x)

plt.show()
```

---

## Pandas Integration

Pandas can plot directly to a specified axes:

```python
import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'AAPL'
df = yf.Ticker(ticker).history(start='2020-01-01', end='2020-12-31')

fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=True)

df.Close.plot(ax=axes[0])
df.Volume.plot(ax=axes[1])

plt.show()
```

---

## Comparison Summary

| Method | Best For |
|--------|----------|
| `plt.subplots` | Regular grids, most common |
| `plt.axes` | Quick single axes |
| `fig.add_axes` | Precise positioning |
| `fig.add_subplot` | Adding axes dynamically |
| `plt.subplot2grid` | Spanning rows/columns |
| `GridSpec` | Complex custom layouts |

---

## Key Takeaways

- `plt.subplots` is the workhorse for most plots
- Use `fig.add_axes` for precise control
- `subplot2grid` and `GridSpec` handle complex layouts
- Inset axes are created with multiple `add_axes` calls
- Pandas plotting integrates via the `ax` parameter
