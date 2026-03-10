# Axes Basics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The Axes object is the core component for plotting in Matplotlib. It contains most plot elements including the data, axes, ticks, labels, and title.

---

## What is an Axes Object

An Axes object encapsulates all elements of an individual (sub-)plot:

- X-axis and Y-axis (`Axis` objects)
- Ticks and tick labels
- Plot elements (`Line2D`, `Text`, `Polygon`, etc.)
- Coordinate system

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
```

---

## Axes vs Figure

| Figure | Axes |
|--------|------|
| The whole canvas | A single plot area |
| Can contain multiple Axes | Contains one coordinate system |
| Top-level container | Where data is plotted |

```python
import matplotlib.pyplot as plt

# One figure, one axes
fig, ax = plt.subplots()

# One figure, four axes
fig, axes = plt.subplots(2, 2)
```

---

## Axes is a NumPy Array

When creating multiple subplots, `plt.subplots` returns a NumPy array of Axes:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

print(type(axes))   # <class 'numpy.ndarray'>
print(axes.shape)   # (2, 2)
print(axes.dtype)   # object
print(type(axes[0, 0]))  # AxesSubplot
```

---

## Accessing Individual Axes

Access axes using NumPy indexing:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos")

axes[1, 0].plot(x, np.sinh(x))
axes[1, 0].set_title("sinh")

axes[1, 1].plot(x, np.cosh(x))
axes[1, 1].set_title("cosh")

plt.tight_layout()
plt.show()
```

---

## Key Axes Properties

Important attributes of an Axes object:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0, 1, 10)
ax.plot(x, x**2)

# Access components
print(ax.xaxis)      # XAxis object
print(ax.yaxis)      # YAxis object
print(ax.spines)     # Dictionary of Spine objects
print(ax.lines)      # List of Line2D objects
print(ax.patches)    # List of Patch objects
print(ax.texts)      # List of Text objects

plt.show()
```

---

## OOP Style Benefits

Using explicit Axes objects provides:

1. **Clear references**: Know exactly which plot you're modifying
2. **Flexibility**: Modify any axes at any time
3. **Reusability**: Pass axes to functions
4. **Complex layouts**: Handle multi-panel figures easily

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_sine(ax, frequency=1):
    """Reusable plotting function that takes an axes."""
    x = np.linspace(0, 2*np.pi, 100)
    ax.plot(x, np.sin(frequency * x))
    ax.set_title(f"sin({frequency}x)")

fig, axes = plt.subplots(1, 3, figsize=(12, 3))

for i, ax in enumerate(axes):
    plot_sine(ax, frequency=i+1)

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- Axes is the main plotting area within a Figure
- `plt.subplots` returns a NumPy array of Axes objects
- Use NumPy indexing to access individual Axes
- OOP style with explicit Axes provides more control
- Each Axes contains its own coordinate system
