# Unpacking Axes

Python's tuple unpacking provides a clean way to name individual axes when creating subplots.

---

## Unpacking a Single Axes

The most common pattern:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```

---

## Unpacking 1D Arrays

For single rows or columns:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Unpack 1x2 grid
fig, (ax0, ax1) = plt.subplots(1, 2)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.cos(x))
plt.show()
```

```python
# Unpack 2x1 grid
fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.cos(x))
plt.show()
```

```python
# Unpack 1x3 grid
fig, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(12, 3))
ax0.plot(x, x**2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.exp(x))
plt.tight_layout()
plt.show()
```

---

## Unpacking 2D Arrays

Use nested tuple unpacking for grids:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Unpack 2x2 grid
fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)

ax0.plot(x, np.sin(x))
ax0.set_title("sin")

ax1.plot(x, np.cos(x))
ax1.set_title("cos")

ax2.plot(x, np.sinh(x))
ax2.set_title("sinh")

ax3.plot(x, np.cosh(x))
ax3.set_title("cosh")

plt.tight_layout()
plt.show()
```

---

## 2×3 Grid Unpacking

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 1, 100)

fig, ((ax0, ax1, ax2), (ax3, ax4, ax5)) = plt.subplots(2, 3, figsize=(12, 6))

ax0.plot(x, x**2)
ax1.plot(x, np.sin(x))
ax2.plot(x, np.exp(x))
ax3.plot(x, np.log(x))
ax4.plot(x, np.sin(x) / np.exp(x))
ax5.plot(x, np.log(x) / np.exp(x))

plt.tight_layout()
plt.show()
```

---

## When to Use Array Indexing vs Unpacking

**Use unpacking when:**

- Fixed number of subplots
- Each subplot has distinct content
- Want descriptive variable names

```python
fig, (ax_price, ax_volume) = plt.subplots(2, 1, sharex=True)
ax_price.plot(dates, prices)
ax_volume.bar(dates, volume)
```

**Use array indexing when:**

- Dynamic number of subplots
- Applying the same operation to all
- Looping over subplots

```python
fig, axes = plt.subplots(3, 4)
for i, ax in enumerate(axes.flat):
    ax.plot(data[i])
```

---

## Combining Both Approaches

Sometimes a hybrid approach is clearest:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

# Create the grid
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# Unpack for clarity
(ax_sin, ax_cos), (ax_tan, ax_exp) = axes

ax_sin.plot(x, np.sin(x))
ax_sin.set_title("sin(x)")

ax_cos.plot(x, np.cos(x))
ax_cos.set_title("cos(x)")

ax_tan.plot(x, np.tan(x))
ax_tan.set_ylim(-5, 5)
ax_tan.set_title("tan(x)")

ax_exp.plot(x, np.exp(np.sin(x)))
ax_exp.set_title("exp(sin(x))")

plt.tight_layout()
plt.show()
```

---

## Using axes.flat

Iterate over all axes regardless of shape:

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

for i, ax in enumerate(axes.flat):
    x = np.linspace(0, 2*np.pi, 100)
    ax.plot(x, np.sin((i+1) * x))
    ax.set_title(f"sin({i+1}x)")

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- `fig, ax = plt.subplots()` for single axes
- `fig, (ax0, ax1) = plt.subplots(1, 2)` for 1D arrays
- `fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2)` for 2D arrays
- Use unpacking for fixed layouts with distinct content
- Use array indexing for dynamic or looped operations
- `axes.flat` flattens any shape for iteration
