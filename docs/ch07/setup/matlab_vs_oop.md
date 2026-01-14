# MATLAB Style vs OOP Style

Matplotlib supports two plotting interfaces: the MATLAB-style (stateful) interface and the object-oriented (OOP) interface.

---

## MATLAB Style Interface

The MATLAB style uses `plt` functions that operate on the "current" figure and axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 3))

plt.subplot(121)
plt.plot(x, y_sin)
plt.title("sin")

plt.subplot(122)
plt.plot(x, y_cos)
plt.title("cos")

plt.tight_layout()
plt.show()
```

**Limitation**: You cannot easily go back and forth between axes once you move to a new subplot.

---

## OOP Style Interface

The OOP style explicitly creates and references Figure and Axes objects:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

# You can go back and forth between axes
axes[0].plot(x, y_sin)
axes[1].plot(x, y_cos)

# You can go back and forth between axes
axes[0].set_title("sin")
axes[1].set_title("cos")

plt.tight_layout()
plt.show()
```

**Advantage**: Full control over each axes object at any point.

---

## Method Name Changes

When switching from MATLAB style to OOP style, method names change:

| MATLAB Style | OOP Style |
|--------------|-----------|
| `plt.title` | `ax.set_title` |
| `plt.xlabel` | `ax.set_xlabel` |
| `plt.ylabel` | `ax.set_ylabel` |
| `plt.xlim` | `ax.set_xlim` |
| `plt.ylim` | `ax.set_ylim` |
| `plt.xticks` | `ax.set_xticks` |
| `plt.yticks` | `ax.set_yticks` |
| `plt.xticklabels` | `ax.set_xticklabels` |
| `plt.yticklabels` | `ax.set_yticklabels` |

---

## When to Use Each

**MATLAB Style**:

- Quick exploratory plots
- Simple single-axis figures
- Interactive REPL sessions

**OOP Style**:

- Complex multi-panel figures
- Production-quality visualizations
- When you need to modify axes after creation
- Reusable plotting functions

---

## Recommendation

The OOP style is recommended for most use cases because it provides:

- More explicit control
- Easier customization
- Better for complex figures
- Clearer code structure

---

## Key Takeaways

- MATLAB style: implicit "current" axes, simpler but limited
- OOP style: explicit axes references, more powerful
- Use OOP style for anything beyond simple plots
- Method names add `set_` prefix in OOP style
