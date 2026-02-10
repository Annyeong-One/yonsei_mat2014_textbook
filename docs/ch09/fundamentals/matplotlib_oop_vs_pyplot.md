# OOP vs Pyplot Style

Matplotlib supports two plotting interfaces: the pyplot (MATLAB-style) interface and the object-oriented (OOP) interface. Understanding both is essential for effective visualization.

---

## Two Paradigms

### Pyplot Style (Implicit State)

The pyplot style uses `plt` functions that operate on the "current" figure and axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 3))

plt.subplot(121)
plt.plot(x, np.sin(x))
plt.title("sin")
plt.xlabel("x")

plt.subplot(122)
plt.plot(x, np.cos(x))
plt.title("cos")
plt.xlabel("x")

plt.tight_layout()
plt.show()
```

Pyplot maintains a state machine with "current" figure and axes:

```python
plt.plot([1, 2, 3])   # Acts on current axes
plt.title('Title')    # Acts on current axes
```

**Limitation**: You cannot easily go back and modify previous subplots once you move to a new one.

---

### OOP Style (Explicit References)

The OOP style explicitly creates and references Figure and Axes objects:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].plot(x, np.sin(x))
axes[0].set_title("sin")
axes[0].set_xlabel("x")

axes[1].plot(x, np.cos(x))
axes[1].set_title("cos")
axes[1].set_xlabel("x")

# Can go back and modify any axes at any time
axes[0].set_ylabel("amplitude")

plt.tight_layout()
plt.show()
```

**Advantage**: Full control over each axes object at any point in your code.

---

## Method Name Differences

When switching from pyplot to OOP style, method names change (add `set_` prefix):

| Pyplot Style | OOP Style |
|--------------|-----------|
| `plt.title()` | `ax.set_title()` |
| `plt.xlabel()` | `ax.set_xlabel()` |
| `plt.ylabel()` | `ax.set_ylabel()` |
| `plt.xlim()` | `ax.set_xlim()` |
| `plt.ylim()` | `ax.set_ylim()` |
| `plt.xticks()` | `ax.set_xticks()` |
| `plt.yticks()` | `ax.set_yticks()` |
| `plt.legend()` | `ax.legend()` |
| `plt.grid()` | `ax.grid()` |

---

## When to Use Each

### Pyplot Style

Best for:
- Quick exploratory plots
- Simple single-axis figures
- Interactive REPL/notebook sessions
- MATLAB users transitioning to Python

```python
# Quick exploration
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### OOP Style

Best for:
- Complex multi-panel figures
- Production-quality visualizations
- Reusable plotting functions
- GUI integration
- When you need to modify axes after creation

```python
def plot_data(ax, data, title):
    """Reusable plotting function."""
    ax.plot(data)
    ax.set_title(title)
    ax.grid(True)
    return ax

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
plot_data(ax1, [1, 2, 3], "Dataset A")
plot_data(ax2, [3, 2, 1], "Dataset B")
plt.show()
```

---

## Mixing Styles (Caution)

You can mix styles, but it can lead to confusion:

```python
fig, ax = plt.subplots()     # OOP: create figure and axes
ax.plot([1, 2, 3])           # OOP: plot on axes
plt.title('Title')           # Pyplot: acts on "current" axes
plt.show()                   # Pyplot: display
```

This works because `plt.subplots()` sets the created axes as "current", but mixing styles makes code harder to follow.

---

## Best Practices

### 1. Prefer OOP for Functions

```python
# ✓ GOOD - Explicit axes parameter
def make_plot(ax, data):
    ax.plot(data)
    ax.set_title('Data')
    return ax

# ✗ BAD - Relies on implicit state
def make_plot(data):
    plt.plot(data)  # Which figure? Which axes?
    plt.title('Data')
```

### 2. Return Figure Objects

```python
def create_figure(data):
    """Create and return figure for caller to display."""
    fig, ax = plt.subplots()
    ax.plot(data)
    ax.set_title('Results')
    return fig  # Caller controls when to display

# Usage
fig = create_figure([1, 2, 3])
fig.savefig('plot.png')  # Save
plt.show()               # Display
```

### 3. Avoid plt.show() Inside Functions

```python
# ✓ GOOD - Let caller decide when to show
def plot_results(ax, results):
    ax.bar(range(len(results)), results)
    ax.set_xlabel('Index')
    # No plt.show() here

# ✗ BAD - Blocks execution and closes figure
def plot_results(results):
    plt.bar(range(len(results)), results)
    plt.show()  # Can't save or modify after this
```

### 4. Use Consistent Style

```python
# ✓ GOOD - All OOP
fig, axes = plt.subplots(2, 2)
for ax in axes.flat:
    ax.plot([1, 2, 3])
    ax.set_title('Plot')
fig.suptitle('Main Title')
plt.tight_layout()
plt.show()

# ✗ AVOID - Mixed styles
plt.figure()
ax = plt.subplot(221)
ax.plot([1, 2, 3])
plt.title('Plot')  # Mixing styles
```

---

## Quick Reference

```python
# Pyplot style
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Title')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig('plot.png')
plt.show()

# OOP style
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y)
ax.set_title('Title')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
fig.savefig('plot.png')
plt.show()
```

---

## Summary

| Aspect | Pyplot Style | OOP Style |
|--------|--------------|-----------|
| State | Implicit (current axes) | Explicit (ax reference) |
| Control | Limited | Full |
| Multi-panel | Awkward | Natural |
| Reusability | Poor | Excellent |
| Best for | Quick plots | Production code |

**Key Takeaways**:

- Pyplot maintains implicit "current" figure/axes state
- OOP style uses explicit `fig` and `ax` references
- Method names add `set_` prefix in OOP style
- **Prefer OOP style** for anything beyond simple exploratory plots
- Return figure objects from functions; let caller handle display
- Avoid mixing styles in the same codebase
