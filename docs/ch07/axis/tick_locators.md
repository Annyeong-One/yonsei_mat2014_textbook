# Tick Locators

Tick locators determine where tick marks appear on an axis.

---

## Using Locators

Apply a locator to an axis:

```python
import matplotlib as mpl

ax.xaxis.set_major_locator(locator)
ax.yaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(locator)
ax.yaxis.set_minor_locator(locator)
```

---

## MultipleLocator

Place ticks at multiples of a base value:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))

ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

plt.show()
```

---

## FixedLocator

Place ticks at specific locations:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x) * np.exp(-x**2/20)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.xaxis.set_major_locator(mpl.ticker.FixedLocator([-1, 0, 1]))
ax.yaxis.set_major_locator(mpl.ticker.FixedLocator([-0.2, 0, 0.2]))

plt.show()
```

---

## MaxNLocator

Automatically choose up to N tick locations:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig, axes = plt.subplots(2, 3, sharex=True, sharey=True, figsize=(12, 3))

for ax in axes.reshape((-1,)):
    ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(3))
    ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(3))
    ax.plot(np.random.randn(10))

plt.show()
```

---

## NullLocator

Remove all ticks:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 500)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.xaxis.set_major_locator(mpl.ticker.NullLocator())
ax.yaxis.set_major_locator(mpl.ticker.NullLocator())

plt.show()
```

Useful for image displays:

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

---

## AutoLocator

Default automatic tick placement:

```python
ax.xaxis.set_major_locator(mpl.ticker.AutoLocator())
```

---

## LogLocator

For logarithmic scales:

```python
ax.set_xscale('log')
ax.xaxis.set_major_locator(mpl.ticker.LogLocator(base=10))
```

---

## LinearLocator

Evenly spaced ticks:

```python
ax.xaxis.set_major_locator(mpl.ticker.LinearLocator(numticks=5))
```

---

## Common Locators Summary

| Locator | Description |
|---------|-------------|
| `MultipleLocator(base)` | Ticks at multiples of base |
| `FixedLocator(locs)` | Ticks at specified locations |
| `MaxNLocator(n)` | At most n ticks |
| `NullLocator()` | No ticks |
| `AutoLocator()` | Automatic (default) |
| `LogLocator()` | For log scales |
| `LinearLocator(n)` | Exactly n evenly spaced |
| `IndexLocator(base, offset)` | Ticks at base*i + offset |

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

# Major ticks every 3 units
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(3))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.3))

# Minor ticks every 1 unit
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

# Grid
ax.grid(which='major', linestyle='-', linewidth=0.8)
ax.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

plt.show()
```

---

## Key Takeaways

- Locators control where ticks appear
- `MultipleLocator` for regular intervals
- `FixedLocator` for specific positions
- `NullLocator` to remove all ticks
- `MaxNLocator` for automatic with maximum count
- Apply to major and minor ticks separately
