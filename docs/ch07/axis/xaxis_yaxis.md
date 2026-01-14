# XAxis and YAxis Objects

The `XAxis` and `YAxis` objects provide fine-grained control over axis behavior, including tick positions, labels, and formatting.

---

## Accessing Axis Objects

Access via the axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Access axis objects
xaxis = ax.xaxis
yaxis = ax.yaxis

print(type(xaxis))  # <class 'matplotlib.axis.XAxis'>
print(type(yaxis))  # <class 'matplotlib.axis.YAxis'>
```

---

## set_ticks_position and get_ticks_position

Control where ticks appear:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('right')
plt.show()
```

Options: `'top'`, `'bottom'`, `'left'`, `'right'`, `'both'`, `'none'`, `'default'`

Get current position:

```python
print(ax.xaxis.get_ticks_position())  # 'top'
print(ax.yaxis.get_ticks_position())  # 'right'
```

---

## Tick Locators

Control where tick marks appear using locator objects:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

# Set major tick locators
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))

# Set minor tick locators
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

plt.show()
```

Get current locators:

```python
print(ax.xaxis.get_major_locator())
print(ax.yaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())
print(ax.yaxis.get_minor_locator())
```

---

## Tick Formatters

Control how tick labels are displayed:

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import yfinance as yf

df = yf.Ticker('AAPL').history(start='2020-07-01', end='2020-12-31')

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(df.index, df['Close'])

# Set date formatter
date_format = mpl_dates.DateFormatter('%b, %d %Y')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()
plt.show()
```

Get current formatters:

```python
print(ax.xaxis.get_major_formatter())
print(ax.yaxis.get_major_formatter())
```

---

## Axis Label

Set the axis label through the axis object:

```python
ax.xaxis.set_label_text('Time')
ax.yaxis.set_label_text('Value')
```

This is equivalent to:

```python
ax.set_xlabel('Time')
ax.set_ylabel('Value')
```

---

## Axis Visibility

Hide an entire axis:

```python
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
```

---

## get_ticklocs and get_ticklabels

Get current tick positions and labels:

```python
# Get tick locations
print(ax.xaxis.get_ticklocs())
print(ax.yaxis.get_ticklocs())

# Get tick labels (list of Text objects)
print(ax.xaxis.get_ticklabels())
print(ax.yaxis.get_ticklabels())
```

---

## Complete Example

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x) * np.exp(-x**2/20)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y)

# Configure x-axis
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(np.pi))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(np.pi/4))
ax.xaxis.set_ticks_position('bottom')

# Configure y-axis
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
ax.yaxis.set_ticks_position('left')

# Add grid for both major and minor ticks
ax.grid(which='major', linestyle='-', linewidth=0.5)
ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Damped Sine Wave')

plt.show()
```

---

## Key Takeaways

- Access axis objects via `ax.xaxis` and `ax.yaxis`
- `set_ticks_position()` controls tick placement
- `set_major_locator()` and `set_minor_locator()` control tick positions
- `set_major_formatter()` and `set_minor_formatter()` control label format
- `get_ticklocs()` and `get_ticklabels()` retrieve current values
