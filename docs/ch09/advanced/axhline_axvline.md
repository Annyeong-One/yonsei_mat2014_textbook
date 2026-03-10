# Axhline and Axvline


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Add horizontal and vertical reference lines that span the entire axes.

---

## ax.axhline()

Add a horizontal line across the axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.axhline(0, color='black', linewidth=0.5)
ax.axhline(0.5, color='red', linestyle='--', label='y=0.5')
ax.axhline(-0.5, color='blue', linestyle='--', label='y=-0.5')
ax.legend()
plt.show()
```

---

## axhline Parameters

```python
ax.axhline(
    y=0,              # Y position of the line
    xmin=0,           # Starting x position (0-1, axes fraction)
    xmax=1,           # Ending x position (0-1, axes fraction)
    color='black',    # Line color
    linestyle='-',    # Line style
    linewidth=1,      # Line width
    alpha=1.0,        # Transparency
    label='label'     # For legend
)
```

---

## ax.axvline()

Add a vertical line across the axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.axvline(0, color='black', linewidth=0.5)
ax.axvline(np.pi/2, color='red', linestyle='--', label='x=π/2')
ax.axvline(-np.pi/2, color='blue', linestyle='--', label='x=-π/2')
ax.legend()
plt.show()
```

---

## axvline Parameters

```python
ax.axvline(
    x=0,              # X position of the line
    ymin=0,           # Starting y position (0-1, axes fraction)
    ymax=1,           # Ending y position (0-1, axes fraction)
    color='black',    # Line color
    linestyle='-',    # Line style
    linewidth=1,      # Line width
    alpha=1.0,        # Transparency
    label='label'     # For legend
)
```

---

## Partial Lines

Draw lines that don't span the entire axes:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Full width horizontal line
ax.axhline(5, color='blue', label='Full width')

# Partial horizontal line (30% to 70% of axes width)
ax.axhline(3, xmin=0.3, xmax=0.7, color='red', linewidth=2, label='Partial')

plt.legend()
plt.show()
```

---

## Mean and Threshold Lines

Common use case for statistical visualization:

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.normal(100, 15, 200)
x = range(len(data))

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, data, 'b-', alpha=0.7)

# Mean line
mean = np.mean(data)
ax.axhline(mean, color='green', linestyle='-', linewidth=2, label=f'Mean: {mean:.1f}')

# Standard deviation bands
std = np.std(data)
ax.axhline(mean + std, color='orange', linestyle='--', label=f'+1σ: {mean+std:.1f}')
ax.axhline(mean - std, color='orange', linestyle='--', label=f'-1σ: {mean-std:.1f}')

ax.axhline(mean + 2*std, color='red', linestyle=':', label=f'+2σ: {mean+2*std:.1f}')
ax.axhline(mean - 2*std, color='red', linestyle=':', label=f'-2σ: {mean-2*std:.1f}')

ax.legend(loc='upper right')
ax.set_title('Process Control Chart')
plt.show()
```

---

## Event Markers

Mark specific events with vertical lines:

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sample stock-like data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')
prices = 100 + np.cumsum(np.random.randn(100))

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(dates, prices)

# Mark earnings dates
earnings_dates = [dates[25], dates[55], dates[85]]
for date in earnings_dates:
    ax.axvline(date, color='red', linestyle='--', alpha=0.7)

ax.set_title('Stock Price with Earnings Dates')
plt.show()
```

---

## ax.hlines() and ax.vlines()

For lines at specific data coordinates (not axes fractions):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Horizontal line from x=2 to x=8 at y=0.5
ax.hlines(y=0.5, xmin=2, xmax=8, color='red', linewidth=2)

# Vertical line from y=-0.5 to y=0.5 at x=5
ax.vlines(x=5, ymin=-0.5, ymax=0.5, color='green', linewidth=2)

plt.show()
```

---

## Key Takeaways

- `axhline` adds horizontal lines spanning the axes
- `axvline` adds vertical lines spanning the axes
- `xmin/xmax` and `ymin/ymax` control partial line extent (0-1 range)
- Use for reference lines, thresholds, and event markers
- `hlines` and `vlines` use data coordinates for extent
