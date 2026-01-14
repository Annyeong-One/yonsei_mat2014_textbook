# Spine Basics

Spines are the lines that form the borders of the plotting area. Understanding spines is essential for creating clean, publication-quality plots.

---

## What are Spines?

A plot has four spines:

- `'top'`: Upper border
- `'bottom'`: Lower border (x-axis line)
- `'left'`: Left border (y-axis line)
- `'right'`: Right border

Access spines through the `ax.spines` dictionary:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

print(type(ax.spines['top']))  # <class 'matplotlib.spines.Spine'>
print(ax.spines.keys())        # ['left', 'right', 'bottom', 'top']

plt.show()
```

---

## Spine Object

Each spine is a `Spine` object with methods for customization:

```python
spine = ax.spines['bottom']

# Available methods
dir(spine)  # set_visible, set_color, set_position, set_linewidth, etc.
```

---

## Default Appearance

By default, all four spines are visible and positioned at the edges of the plot:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()  # All four spines visible
```

---

## Common Spine Configurations

**Two-spine plot (clean look):**
```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

**Centered axes (math-style):**
```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
```

**No spines (for heatmaps, images):**
```python
for spine in ax.spines.values():
    spine.set_visible(False)
```

---

## Iterating Over Spines

Apply changes to all spines:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

for spine in ax.spines.values():
    spine.set_linewidth(2)
    spine.set_color('gray')

plt.show()
```

---

## Spines and Data Visualization

Removing unnecessary spines reduces visual clutter:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y_sin, label='sin(x)')
ax.plot(x, y_cos, label='cos(x)')

# Clean two-spine style
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
```

---

## Key Takeaways

- Four spines: top, bottom, left, right
- Access via `ax.spines['name']` or `ax.spines.values()`
- Each spine is a `Spine` object with customization methods
- Removing top/right spines is a common clean style
- Position spines at 'zero' for math-style centered axes
