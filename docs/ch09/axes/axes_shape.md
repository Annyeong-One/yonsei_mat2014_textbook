# Axes Shape Behavior

Understanding how `plt.subplots` returns different shaped arrays is crucial for writing robust plotting code.

---

## Single Axes

With no arguments or `(1, 1)`, a single Axes object is returned (not an array):

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>

fig, ax = plt.subplots(1, 1)
print(type(ax))  # <class 'matplotlib.axes._subplots.AxesSubplot'>
```

---

## 1D Arrays (1×N or N×1)

When creating a single row or column, the result is a 1D array:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

# 1 row, 2 columns -> shape (2,), not (1, 2)
fig, axes = plt.subplots(1, 2)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
plt.show()

print(type(axes))   # numpy.ndarray
print(axes.shape)   # (2,)
print(axes.dtype)   # object
```

```python
# 2 rows, 1 column -> shape (2,), not (2, 1)
fig, axes = plt.subplots(2, 1)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
plt.show()

print(axes.shape)   # (2,)
```

---

## 2D Arrays (N×M)

Only when both dimensions are greater than 1:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].plot(x, np.sinh(x))
axes[1, 1].plot(x, np.cosh(x))

plt.show()

print(type(axes))   # numpy.ndarray
print(axes.shape)   # (2, 2)
print(axes.dtype)   # object
```

---

## The squeeze Parameter

Use `squeeze=False` to always get a 2D array:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 1, 100)

# Without squeeze=False
fig, axs = plt.subplots(1, 3, figsize=(12, 3))
print(axs.shape)  # (3,)
axs[0].plot(x, x**2)
axs[1].plot(x, np.sin(x))
axs[2].plot(x, np.exp(x))

# With squeeze=False
fig, axs = plt.subplots(1, 3, figsize=(12, 3), squeeze=False)
print(axs.shape)  # (1, 3)
axs[0, 0].plot(x, x**2)
axs[0, 1].plot(x, np.sin(x))
axs[0, 2].plot(x, np.exp(x))

plt.tight_layout()
plt.show()
```

---

## Why Use squeeze=False?

Consistent array access is useful when:

1. **Looping over subplots**:
```python
fig, axes = plt.subplots(1, 3, squeeze=False)
for i in range(1):
    for j in range(3):
        axes[i, j].plot([1, 2, 3])
```

2. **Writing generic functions**:
```python
def setup_grid(nrows, ncols):
    fig, axes = plt.subplots(nrows, ncols, squeeze=False)
    # Always use axes[i, j] regardless of dimensions
    return fig, axes
```

---

## Shape Summary Table

| Subplots | Returns | Shape | Access |
|----------|---------|-------|--------|
| `plt.subplots()` | Axes | N/A | `ax` |
| `plt.subplots(1, 3)` | 1D array | `(3,)` | `axes[j]` |
| `plt.subplots(3, 1)` | 1D array | `(3,)` | `axes[i]` |
| `plt.subplots(2, 3)` | 2D array | `(2, 3)` | `axes[i, j]` |
| `plt.subplots(1, 3, squeeze=False)` | 2D array | `(1, 3)` | `axes[0, j]` |

---

## Practical Implications

Handle different cases in code:

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_functions(funcs, figsize=(12, 3)):
    n = len(funcs)
    fig, axes = plt.subplots(1, n, figsize=figsize, squeeze=False)
    
    x = np.linspace(0, 2*np.pi, 100)
    
    for j, func in enumerate(funcs):
        axes[0, j].plot(x, func(x))
    
    plt.tight_layout()
    return fig, axes

# Works for any number of functions
plot_functions([np.sin, np.cos, np.tan])
plt.show()
```

---

## Key Takeaways

- Single axes returns an Axes object, not an array
- 1×N or N×1 returns a 1D array with shape `(N,)`
- N×M (both > 1) returns a 2D array with shape `(N, M)`
- Use `squeeze=False` for consistent 2D array access
- Handle shape variations when writing generic plotting functions
