# Line2D and Artists

## Artist Base Class

### 1. Hierarchy

All plot elements inherit from Artist:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line, = ax.plot([1, 2, 3])
print(isinstance(line, plt.Artist))  # True
```

### 2. Properties

```python
line.set_color('red')
line.set_linewidth(2)
line.set_linestyle('--')
line.set_marker('o')
line.set_markersize(8)
```

### 3. Visibility

```python
line.set_visible(False)
line.set_alpha(0.5)  # Transparency
```

## Line2D

### 1. Creation

```python
from matplotlib.lines import Line2D

line = Line2D([0, 1, 2], [0, 1, 0], color='blue', linewidth=2)
ax.add_line(line)
```

### 2. Properties

```python
line.set_xdata([0, 1, 2, 3])
line.set_ydata([0, 1, 0, 1])
line.set_label('Custom Line')
```

### 3. Markers

```python
line.set_marker('o')
line.set_markerfacecolor('yellow')
line.set_markeredgecolor('black')
line.set_markeredgewidth(1)
```

## Other Artists

### 1. Text

```python
text = ax.text(0.5, 0.5, 'Hello', fontsize=14)
text.set_color('red')
text.set_rotation(45)
```

### 2. Patch

```python
from matplotlib.patches import Rectangle

rect = Rectangle((0, 0), 1, 1, facecolor='lightblue', edgecolor='blue')
ax.add_patch(rect)
```

### 3. Collection

```python
from matplotlib.collections import LineCollection

segments = [[(0, 0), (1, 1)], [(1, 0), (0, 1)]]
lc = LineCollection(segments, colors='red', linewidths=2)
ax.add_collection(lc)
```
