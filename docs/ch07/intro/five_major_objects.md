# Five Major Objects

Matplotlib is built around five major object types that form a hierarchy. Understanding these objects is essential for effective plotting.

---

## Object Hierarchy

```
Figure
  └── Axes (AxesSubplot)
        ├── XAxis
        ├── YAxis
        ├── Spine (top, bottom, left, right)
        └── Text (labels, titles, tick labels)
```

---

## 1. Figure

The **Figure** is the top-level container—the entire window or canvas.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
print(type(fig))  # <class 'matplotlib.figure.Figure'>
```

**Responsibilities:**

- Contains all plot elements
- Controls figure size and DPI
- Manages multiple Axes
- Handles saving to files

---

## 2. Axes (AxesSubplot)

The **Axes** is the actual plotting area where data is drawn.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>

ax.plot(x, y)
plt.show()
```

**Responsibilities:**

- Contains the plotted data
- Manages axis limits and scales
- Holds title and labels
- Contains XAxis, YAxis, and Spines

---

## 3. Spine

**Spines** are the lines forming the plot borders.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

print(type(ax.spines['top']))  # <class 'matplotlib.spines.Spine'>

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()
```

**Four spines:**

- `ax.spines['top']`
- `ax.spines['bottom']`
- `ax.spines['left']`
- `ax.spines['right']`

---

## 4. Axis (XAxis and YAxis)

**Axis** objects control tick marks, tick labels, and axis labels.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

print(type(ax.xaxis))  # <class 'matplotlib.axis.XAxis'>
print(type(ax.yaxis))  # <class 'matplotlib.axis.YAxis'>

# Customize axis
ax.set_xticks(
    ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
    labels=["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"]
)
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('right')

plt.show()
```

**Responsibilities:**

- Tick positions (locators)
- Tick labels (formatters)
- Axis labels
- Tick position (top/bottom, left/right)

---

## 5. Text

**Text** objects represent all text elements including labels and tick labels.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

# Access tick labels (Text objects)
for label in ax.get_xticklabels():
    print(type(label))  # <class 'matplotlib.text.Text'>
    label.set_rotation(45)

plt.show()
```

**Text elements:**

- Tick labels
- Axis labels
- Title
- Annotations
- Any added text

---

## Complete Example

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 100+1)
    y = np.sin(x)

    # 1. Figure
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    print(f"{type(fig) = }")  # matplotlib.figure.Figure

    # 2. Axes
    print(f"{type(ax) = }")   # matplotlib.axes._subplots.AxesSubplot
    ax.plot(x, y)
    ax2.plot(y, x)

    # 3. Spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    print(f"{type(ax.spines['top']) = }")  # matplotlib.spines.Spine

    # 4. Axis
    ax.set_xticks(
        ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
        labels=["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"]
    )
    ax.xaxis.set_ticks_position('top')
    ax.yaxis.set_ticks_position('right')
    print(f"{type(ax.xaxis) = }")  # matplotlib.axis.XAxis
    print(f"{type(ax.yaxis) = }")  # matplotlib.axis.YAxis

    # 5. Text
    for label in ax.get_xticklabels():
        label.set_rotation(45)
    print(f"{type(label) = }")  # matplotlib.text.Text

    plt.show()

if __name__ == '__main__':
    main()
```

---

## Summary Table

| Object | Type | Purpose |
|--------|------|---------|
| Figure | `matplotlib.figure.Figure` | Top-level container |
| Axes | `matplotlib.axes.AxesSubplot` | Plotting area |
| Spine | `matplotlib.spines.Spine` | Border lines |
| Axis | `matplotlib.axis.XAxis/YAxis` | Tick and label control |
| Text | `matplotlib.text.Text` | All text elements |

---

## Key Takeaways

- Figure is the top-level container
- Axes is where data is plotted
- Spines are the four border lines
- Axis (XAxis/YAxis) controls ticks and labels
- Text represents all text elements
- Understanding this hierarchy enables full customization
