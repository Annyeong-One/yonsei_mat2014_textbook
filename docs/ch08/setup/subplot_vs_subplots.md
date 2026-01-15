# plt.subplot vs plt.subplots

Understanding the difference between `plt.subplot` (singular) and `plt.subplots` (plural) is essential for effective Matplotlib usage.

---

## plt.subplot (MATLAB Style)

`plt.subplot` creates a single subplot in a grid layout:

```python
import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)  # Create the first subplot in a 2x2 grid
plt.plot([1, 2, 3, 4])

plt.subplot(2, 2, 2)  # Create the second subplot
plt.plot([4, 3, 2, 1])

plt.subplot(2, 2, 3)  # Create the third subplot
plt.plot([1, 1, 1, 1])

plt.subplot(2, 2, 4)  # Create the fourth subplot
plt.plot([1, 2, 1, 2])

plt.show()
```

**Syntax**: `plt.subplot(nrows, ncols, index)`

- Index starts at 1 (not 0)
- Counts left-to-right, top-to-bottom

---

## plt.subplots (OOP Style)

`plt.subplots` creates a Figure and all Axes objects at once:

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(4, 4))

axes[0, 0].plot([1, 2, 3, 4])
axes[0, 1].plot([4, 3, 2, 1])
axes[1, 0].plot([1, 1, 1, 1])
axes[1, 1].plot([1, 2, 1, 2])

plt.show()

print(type(axes))   # numpy.ndarray
print(axes.shape)   # (2, 2)
print(axes.dtype)   # object
```

**Returns**: A Figure object and a NumPy array of Axes objects.

---

## Unpacking Axes

You can unpack the axes array for cleaner code:

```python
import matplotlib.pyplot as plt

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(2, 2, figsize=(4, 4))

ax0.plot([1, 2, 3, 4])
ax1.plot([4, 3, 2, 1])
ax2.plot([1, 1, 1, 1])
ax3.plot([1, 2, 1, 2])

plt.show()
```

---

## Axes Shape Behavior

The returned axes array shape depends on the grid dimensions:

```python
# Single axes returns an Axes object, not an array
fig, ax = plt.subplots()
print(type(ax))  # AxesSubplot

# 1xN or Nx1 returns a 1D array
fig, axes = plt.subplots(1, 3)
print(axes.shape)  # (3,)

# NxM returns a 2D array
fig, axes = plt.subplots(2, 3)
print(axes.shape)  # (2, 3)
```

---

## The squeeze Keyword

Use `squeeze=False` to always get a 2D array:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 1, 100)

# Without squeeze=False: shape is (3,)
fig, axs = plt.subplots(1, 3, figsize=(12, 3))
axs[0].plot(x, x**2)
axs[1].plot(x, np.sin(x))
axs[2].plot(x, np.exp(x))

# With squeeze=False: shape is (1, 3)
fig, axs = plt.subplots(1, 3, figsize=(12, 3), squeeze=False)
axs[0, 0].plot(x, x**2)
axs[0, 1].plot(x, np.sin(x))
axs[0, 2].plot(x, np.exp(x))

plt.tight_layout()
plt.show()
```

---

## Comparison Summary

| Feature | plt.subplot | plt.subplots |
|---------|-------------|--------------|
| Style | MATLAB | OOP |
| Returns | Axes | (Figure, Axes array) |
| Index starts at | 1 | 0 |
| Creates | One axes at a time | All axes at once |
| Flexibility | Limited | High |

---

## Key Takeaways

- `plt.subplot`: singular, MATLAB style, 1-based indexing
- `plt.subplots`: plural, OOP style, returns Figure and Axes array
- Use `plt.subplots` for new code
- Use `squeeze=False` for consistent array shapes
