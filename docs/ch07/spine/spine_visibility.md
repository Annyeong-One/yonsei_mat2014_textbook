# Spine Visibility

Control which spines are displayed to create cleaner visualizations.

---

## set_visible

Hide or show individual spines:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
```

---

## set_color to 'none'

An alternative way to hide spines:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
plt.show()
```

---

## Common Visibility Patterns

**Clean two-spine (L-shape):**
```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

**Bottom only:**
```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
```

**No spines:**
```python
for spine in ax.spines.values():
    spine.set_visible(False)
```

---

## Spine Visibility with Different Plot Types

**For box plots:**
```python
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

fig, ax = plt.subplots()
ax.boxplot(data)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
```

**For bar charts:**
```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

fig, ax = plt.subplots()
ax.bar(categories, values)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.show()
```

---

## Images with No Spines

For images, hide all spines and ticks:

```python
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces().images

fig, ax = plt.subplots(5, 5, figsize=(5, 5))
fig.subplots_adjust(hspace=0, wspace=0)

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(mpl.ticker.NullLocator())
        ax[i, j].yaxis.set_major_locator(mpl.ticker.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")

plt.show()
```

---

## set_linewidth

Control spine thickness:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
```

---

## set_color

Change spine colors:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('blue')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
```

---

## Key Takeaways

- `set_visible(False)` hides a spine
- `set_color('none')` is an alternative way to hide
- Remove top/right spines for cleaner plots
- Remove all spines for image displays
- Use `set_linewidth()` and `set_color()` for styling
