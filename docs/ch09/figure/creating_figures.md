# Creating Figures

The Figure object is the top-level container for all plot elements in Matplotlib.

---

## Using plt.figure

Create an empty figure:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.show()
```

With size specification:

```python
fig = plt.figure(figsize=(10, 4))
```

The `figsize` parameter takes `(width, height)` in inches.

---

## Using plt.subplots

The most common way to create a figure with axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
plt.show()
```

---

## Adding Axes with fig.add_axes

For precise axes positioning, use `fig.add_axes`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x**2)

fig = plt.figure()

# Axes coordinates: [left, bottom, width, height] (0 to 1)
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes((left, bottom, width, height))

ax.plot(x, y1 * y2)
ax.plot(x, y2, 'g')
ax.plot(x, -y2, 'g')
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
```

---

## Adding Axes with fig.add_subplot

Add subplots one at a time:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure(figsize=(12, 6))

for s in range(11):
    ax = fig.add_subplot(3, 4, s + 1)
    if s % 2 == 0:
        ax.plot(y1, label=f"state {s}")
    else:
        ax.plot(y2, label=f"state {s}")

plt.show()
```

---

## Creating Inset Axes

Use multiple `add_axes` calls for inset plots:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 50)
y1 = x ** 2
y2 = np.sqrt(x)

fig = plt.figure()

ax0 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # Main axes
ax1 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # Inset axes

ax0.plot(x, y1)  # Main figure
ax1.plot(y1, x)  # Inset

plt.show()
```

---

## Figure Keywords

Common `plt.figure` parameters:

```python
fig = plt.figure(
    figsize=(8, 6),        # Size in inches
    dpi=100,               # Dots per inch
    facecolor='#f1f1f1',   # Background color
    edgecolor='black',     # Border color
    linewidth=2            # Border width
)
```

---

## Figure Title

Add a title to the entire figure (spanning all subplots):

```python
import matplotlib.pyplot as plt

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))
fig.suptitle("My Figure Title", fontsize=20)

ax0.plot([1, 2, 3])
ax1.plot([3, 2, 1])

plt.show()
```

---

## Key Takeaways

- `plt.figure()` creates an empty figure
- `plt.subplots()` creates figure and axes together
- `fig.add_axes()` gives precise position control
- `fig.add_subplot()` adds subplots one at a time
- `figsize=(width, height)` sets size in inches
