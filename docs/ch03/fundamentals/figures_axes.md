# Figures and Axes

Matplotlib organizes plots around two core objects: **Figure** and **Axes**. Understanding this structure is key to creating clear and flexible visualizations.

---

## 1. The Figure

A **Figure** represents the entire drawing canvas.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
```

It can contain one or more Axes objects.

---

## 2. Axes

An **Axes** represents a single plot area with:
- x-axis and y-axis,
- ticks and labels,
- plotted data.

The most common way to create a figure and axes together:

```python
fig, ax = plt.subplots()
```

---

## 3. Plotting on Axes

```python
import numpy as np

x = np.linspace(0, 1, 100)
y = x**2

ax.plot(x, y)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Simple plot")
```

This object-oriented style is recommended.

---

## 4. Multiple Axes

```python
fig, axs = plt.subplots(2, 2)
```

This creates a grid of Axes for comparative plots.

---

## 5. Why the object-oriented API matters

- More explicit control
- Easier customization
- Better for complex figures

---

## Key takeaways

- Figure = whole canvas
- Axes = individual plot
- Prefer `fig, ax = plt.subplots()`
