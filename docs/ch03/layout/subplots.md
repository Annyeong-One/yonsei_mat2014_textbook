# Subplots and Grids

Complex visualizations often require arranging multiple plots in a single figure. Matplotlib provides flexible tools for creating **subplots and grids**.

---

## 1. Basic subplots

The simplest way to create multiple plots is `plt.subplots`:

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
```

This creates a 2×2 grid of Axes.

---

## 2. Indexing Axes

```python
axs[0, 0].plot([1, 2, 3])
axs[1, 1].plot([3, 2, 1])
```

Each Axes can be customized independently.

---

## 3. Shared axes

Sharing axes improves comparability:

```python
fig, axs = plt.subplots(2, 1, sharex=True)
```

Useful for time-series panels.

---

## 4. GridSpec (advanced layouts)

For fine control:

```python
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(gs[:, 0])
ax2 = plt.subplot(gs[0, 1:])
ax3 = plt.subplot(gs[1, 1:])
```

---

## 5. Best practices

- Align axes when comparing plots.
- Avoid overcrowding.
- Use shared labels where possible.

---

## Key takeaways

- `plt.subplots` is the workhorse for layouts.
- Axes can share scales.
- GridSpec enables custom layouts.
