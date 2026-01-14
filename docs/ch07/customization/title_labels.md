# Title and Labels

Titles and axis labels provide context for your plots.

---

## Setting Title

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.set_title("Sine Curve")
plt.show()
```

Get the current title:

```python
print(ax.get_title())  # "Sine Curve"
```

---

## Title Formatting

```python
ax.set_title("Sine Curve", fontsize=20, fontweight='bold', color='navy')
```

Position the title:

```python
ax.set_title('Title', loc='left')   # Left-aligned
ax.set_title('Title', loc='right')  # Right-aligned
ax.set_title('Title', pad=20)       # Add padding above
```

---

## Setting Axis Labels

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = x + x**2

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y, color='g')
ax.set_title('$y = x + x^2$', fontsize=20)
ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$y$', fontsize=20)
plt.show()
```

Get current labels:

```python
print(ax.get_xlabel())
print(ax.get_ylabel())
```

---

## LaTeX Support

Matplotlib supports LaTeX math notation using `$...$`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(r'$y = \sin(x)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
plt.show()
```

Complex equations:

```python
ax.set_title(r'$y = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$')
```

!!! tip
    Use raw strings (`r'...'`) to avoid escaping backslashes.

---

## Using set() for Multiple Properties

Set multiple properties at once:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 100)
y = x + x**2

fig, ax = plt.subplots()
ax.plot(x, y, color='g')
ax.set(
    title='$y = x + x^2$',
    xlabel='$x$',
    ylabel='$y$',
    xlim=[0, 1],
    ylim=(0, 2)
)
plt.show()
```

---

## Label Padding and Rotation

```python
ax.set_xlabel('Time (seconds)', labelpad=10)  # Add padding
ax.set_ylabel('Value', rotation=0, labelpad=15)  # Horizontal label
```

---

## Figure Super Title

For multi-subplot figures, use `suptitle`:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))
fig.suptitle("Figure Title", fontsize=20)

ax0.hist(np.random.normal(size=1000), bins=30)
ax0.set_title("Histogram")

ax1.boxplot(np.random.normal(size=1000))
ax1.set_title("Box Plot")

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- `ax.set_title()` sets the axes title
- `ax.set_xlabel()` and `ax.set_ylabel()` set axis labels
- Use `$...$` for LaTeX math notation
- Use `ax.set()` to set multiple properties at once
- `fig.suptitle()` adds a title above all subplots
- Get current values with `get_title()`, `get_xlabel()`, `get_ylabel()`
