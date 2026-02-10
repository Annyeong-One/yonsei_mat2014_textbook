# Figure Methods

The Figure object provides methods for managing subplots, layout, and overall figure properties.

---

## suptitle

Add a centered title to the entire figure:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))
fig.suptitle("Figure Super Title", fontsize=20)

ax0.hist(np.random.normal(size=1000), bins=30)
ax1.boxplot(np.random.normal(size=1000))

plt.show()
```

---

## subplots_adjust

Fine-tune spacing between subplots:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces().images

fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(mpl.ticker.NullLocator())
        ax[i, j].yaxis.set_major_locator(mpl.ticker.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")

plt.show()
```

Parameters:

- `left`, `right`, `bottom`, `top`: Subplot boundaries (0 to 1)
- `wspace`: Width space between subplots
- `hspace`: Height space between subplots

---

## tight_layout

Automatically adjust subplot parameters:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

fig, axes = plt.subplots(2, 2, figsize=(8, 6))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("y")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos(x)")

axes[1, 0].plot(x, np.sinh(x))
axes[1, 0].set_title("sinh(x)")

axes[1, 1].plot(x, np.cosh(x))
axes[1, 1].set_title("cosh(x)")

fig.tight_layout()
plt.show()
```

---

## autofmt_xdate

Automatically format date labels to prevent overlap:

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import yfinance as yf

df = yf.Ticker('AAPL').history(start='2020-07-01', end='2020-12-31')

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(df.index, df['Close'])

date_format = mpl_dates.DateFormatter('%b, %d %Y')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()
plt.show()
```

---

## savefig

Save the figure to a file:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(15, 4))
ax.plot(x, y_sin)
ax.plot(x, y_cos)

fig.savefig("sin_cos_graph.png", facecolor="#f1f1f1", transparent=True)
plt.show()
```

---

## get_size_inches and set_size_inches

Get or modify figure size after creation:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Get current size
print(fig.get_size_inches())  # [6.4, 4.8]

# Change size
fig.set_size_inches(12, 4)
print(fig.get_size_inches())  # [12., 4.]

plt.show()
```

---

## get_axes

Get a list of all Axes in the figure:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

all_axes = fig.get_axes()
print(len(all_axes))  # 4

for ax in all_axes:
    ax.plot([1, 2, 3])

plt.show()
```

---

## clear

Clear the entire figure:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3])

fig.clear()  # Removes all axes and content

ax_new = fig.add_subplot(111)
ax_new.plot([3, 2, 1])

plt.show()
```

---

## Key Takeaways

- `suptitle()` adds a title above all subplots
- `subplots_adjust()` controls subplot spacing manually
- `tight_layout()` automatically adjusts spacing
- `autofmt_xdate()` formats date labels
- `savefig()` exports the figure to a file
