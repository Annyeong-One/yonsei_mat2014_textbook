# Limits and Ticks

Control the visible range and tick positions on your axes.

---

## Setting Axis Limits

Use `set_xlim` and `set_ylim`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.set_xlim((-3*np.pi, 3*np.pi))
ax.set_ylim((-2, 2))
plt.show()
```

---

## Getting Current Limits

```python
print(ax.get_xlim())  # Returns tuple: (-9.42..., 9.42...)
print(ax.get_ylim())  # Returns tuple: (-2.0, 2.0)
```

---

## Setting Ticks

Use `set_xticks` and `set_yticks`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.set_yticks(ticks=[-1, 0, 1])
ax.set_xticks(ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
plt.show()
```

---

## Removing Ticks

Pass an empty tuple to remove all ticks:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.set_xticks(())
ax.set_yticks(())
plt.show()
```

---

## Tick Labels

Set custom labels with the `labels` parameter:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.set_yticks(ticks=[-1, 0, 1])
ax.set_xticks(
    ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
    labels=["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"]
)
plt.show()
```

---

## Minor Ticks

Add minor ticks with `minor=True`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

# Major ticks
ax.set_yticks(ticks=[-1, 0, 1])
ax.set_xticks(
    ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
    labels=["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"]
)

# Minor ticks (no labels)
ax.set_xticks(
    ticks=np.linspace(-2*np.pi, 2*np.pi, 17),
    labels=[],
    minor=True
)

plt.show()
```

---

## Getting Current Ticks

```python
print(ax.get_xticks())
print(ax.get_yticks())
```

---

## Complete Example with Spines

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

# Set ticks and labels
ax.set_yticks(ticks=[-1, 0, 1])
ax.set_xticks(
    ticks=[-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
    labels=["$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$"]
)
ax.set_xticks(
    ticks=np.linspace(-2*np.pi, 2*np.pi, 17),
    labels=[],
    minor=True
)

# Move spines to origin
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()
```

---

## tick_params

Fine-tune tick appearance:

```python
ax.tick_params(
    axis='both',      # 'x', 'y', or 'both'
    which='major',    # 'major', 'minor', or 'both'
    direction='out',  # 'in', 'out', or 'inout'
    length=6,         # Tick length
    width=2,          # Tick width
    labelsize=10,     # Label font size
    rotation=45,      # Label rotation
    colors='blue'     # Tick and label color
)
```

---

## Key Takeaways

- `set_xlim()` and `set_ylim()` control visible range
- `set_xticks()` and `set_yticks()` set tick positions
- Use `labels` parameter for custom tick labels
- Use `minor=True` for minor ticks
- `tick_params()` provides fine-grained control
- Empty tuple `()` removes all ticks
