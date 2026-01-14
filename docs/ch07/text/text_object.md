# Text Object

Text objects in Matplotlib represent any text element including tick labels, axis labels, titles, and annotations.

---

## Text Objects in Axes

Every text element is a `Text` object:

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)
error = np.random.normal(size=(400,))
index = pd.date_range(start='2019-09-01', end='2020-01-01', freq='D')

mu = 50
data = [mu + 0.4*error[t-1] + 0.3*error[t-2] + error[t] 
        for t in range(2, len(index)+2)]
s = pd.Series(data, index)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(s)
ax.axhline(mu, linestyle='--', color='grey')

# Examine tick labels
for label in ax.get_xticklabels():
    print(f"Type: {type(label)}")
    break

plt.show()
```

Output:
```
Type: <class 'matplotlib.text.Text'>
```

---

## Accessing Text Elements

Get various text elements from an axes:

```python
# Tick labels
x_labels = ax.get_xticklabels()  # List of Text objects
y_labels = ax.get_yticklabels()  # List of Text objects

# Title
title = ax.title  # Text object

# Axis labels
xlabel = ax.xaxis.label  # Text object
ylabel = ax.yaxis.label  # Text object
```

---

## Text Properties

Common properties available on Text objects:

| Property | Description |
|----------|-------------|
| `text` | The string content |
| `fontsize` | Font size |
| `fontweight` | 'normal', 'bold', etc. |
| `fontstyle` | 'normal', 'italic', etc. |
| `fontfamily` | 'serif', 'sans-serif', etc. |
| `color` | Text color |
| `alpha` | Transparency |
| `rotation` | Rotation angle |
| `horizontalalignment` | 'left', 'center', 'right' |
| `verticalalignment` | 'top', 'center', 'bottom' |
| `backgroundcolor` | Background color |

---

## Text Methods

Set properties using setter methods:

```python
label.set_text('New Text')
label.set_fontsize(12)
label.set_fontweight('bold')
label.set_color('blue')
label.set_rotation(45)
label.set_horizontalalignment('right')
label.set_verticalalignment('top')
```

Get properties using getter methods:

```python
text = label.get_text()
size = label.get_fontsize()
weight = label.get_fontweight()
color = label.get_color()
```

---

## Example: Customizing Tick Labels

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(0)
error = np.random.normal(size=(400,))
index = pd.date_range(start='2019-09-01', end='2020-01-01', freq='D')

mu = 50
data = [mu + 0.4*error[t-1] + 0.3*error[t-2] + error[t] 
        for t in range(2, len(index)+2)]
s = pd.Series(data, index)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(s)
ax.axhline(mu, linestyle='--', color='grey')

for label in ax.get_xticklabels():
    label.set_horizontalalignment("right")
    label.set_rotation(45)

plt.show()
```

---

## Adding Background Box

Use `set_bbox()` to add a background:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 500)
y = np.sin(x) / x

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, linewidth=2)

# Move spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

ax.set_xticks([-10, -5, 5, 10])
ax.set_yticks([0.5, 1])

# Add white background to labels
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_bbox({'facecolor': 'white', 'edgecolor': 'white'})

plt.show()
```

---

## Key Takeaways

- All text in Matplotlib is a `Text` object
- Access with `get_xticklabels()`, `get_yticklabels()`, etc.
- Use setter methods to customize appearance
- `set_bbox()` adds a background box
- Text objects support rotation, alignment, and styling
