# Labels and Legends

Labels and legends help viewers understand what data is being displayed.

---

## Adding Labels

Use the `label` parameter in `plot()`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(15, 4))
ax.plot(x, y_sin, label='sin')
ax.plot(x, y_cos, label='cos')
ax.legend()
plt.show()
```

---

## Alternative: Labels in legend()

Pass labels directly to `legend()`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(["sin", "cos"])
plt.show()
```

---

## Legend Location (loc)

Control legend placement:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.legend(loc='upper right')
plt.show()
```

Location options:

| Value | Description |
|-------|-------------|
| `'best'` | Auto-select best location (default) |
| `'upper right'` | Top right |
| `'upper left'` | Top left |
| `'lower left'` | Bottom left |
| `'lower right'` | Bottom right |
| `'right'` | Right side |
| `'center left'` | Left center |
| `'center right'` | Right center |
| `'lower center'` | Bottom center |
| `'upper center'` | Top center |
| `'center'` | Center |

Numeric codes (0-10) also work.

---

## Legend Font Size

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.legend(fontsize=20)
plt.show()
```

---

## Legend Shadow

Add a shadow effect:

```python
ax.legend(shadow=True)
```

---

## Legend Frame

Remove the frame border:

```python
ax.legend(frameon=False)
```

---

## Multiple Columns (ncol)

Arrange legend entries in columns:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)

fig, ax = plt.subplots(figsize=(12, 3))

for beta in range(1, 9):
    ax.plot(x, beta * x, label=f"y(x)={beta}*x")

ax.legend(ncol=4)
plt.show()
```

---

## Legend Outside Plot (bbox_to_anchor)

Place legend outside the axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)

fig, ax = plt.subplots(figsize=(12, 3))

for beta in range(1, 9):
    ax.plot(x, beta * x, label=f"y(x)={beta}*x")

ax.legend(ncol=4, loc='lower left', bbox_to_anchor=(0, 1))
plt.show()
```

The `bbox_to_anchor` parameter takes `(x, y)` coordinates in axes fraction.

---

## Comprehensive Legend Example

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

fig, ax = plt.subplots(figsize=(15, 4))

for beta in range(1, 9):
    ax.plot(x, beta * x, label=f"y(x)={beta}*x")

ax.legend(
    fontsize=15,
    shadow=True,
    ncol=4,
    loc='lower right'
)
plt.show()
```

---

## Legend Title

Add a title to the legend:

```python
ax.legend(title='Functions', title_fontsize=14)
```

---

## Selective Legend Entries

Only include specific lines in the legend:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

line1, = ax.plot(x, np.sin(x), label='sin')
line2, = ax.plot(x, np.cos(x), label='cos')
ax.plot(x, x/10)  # No label, won't appear in legend

ax.legend()  # Only shows sin and cos
plt.show()
```

---

## Key Takeaways

- Add `label` parameter to `plot()` calls
- Call `ax.legend()` to display the legend
- Use `loc` to position the legend
- Use `ncol` for multi-column layouts
- Use `bbox_to_anchor` for legends outside the plot
- `frameon=False` removes the border
- `shadow=True` adds a drop shadow
