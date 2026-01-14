# Markers

Markers highlight individual data points on a line plot.

---

## Basic Marker Usage

Add markers with the `marker` parameter:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
plt.show()
```

---

## Common Marker Types

| Marker | Description |
|--------|-------------|
| `'o'` | Circle |
| `'s'` | Square |
| `'^'` | Triangle up |
| `'v'` | Triangle down |
| `'*'` | Star |
| `'+'` | Plus |
| `'x'` | X |
| `'D'` | Diamond |
| `'p'` | Pentagon |
| `'H'` | Hexagon |
| `'.'` | Point |
| `','` | Pixel |

---

## Marker Size (markersize / ms)

Control marker size:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 5)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, marker='p', markersize=15)
plt.show()
```

Short form:

```python
ax.plot(x, y, marker='p', ms=15)
```

---

## Marker Colors

**Edge color (markeredgecolor / mec):**
```python
ax.plot(x, y, marker='o', markeredgecolor='red')
# Short: mec='red'
```

**Face color (markerfacecolor / mfc):**
```python
ax.plot(x, y, marker='o', markerfacecolor='blue')
# Short: mfc='blue'
```

---

## Marker Edge Width (markeredgewidth / mew)

Control the thickness of the marker border:

```python
ax.plot(x, y, marker='o', markeredgewidth=4)
# Short: mew=4
```

---

## Complete Marker Customization

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 5)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y,
        marker='p',           # Pentagon marker
        markersize=15,        # Size
        markeredgecolor='red',   # Edge color
        markeredgewidth=4,    # Edge width
        markerfacecolor='blue')  # Fill color
plt.show()
```

Short form:

```python
ax.plot(x, y, marker='p', ms=15, mec='red', mew=4, mfc='blue')
```

---

## MATLAB-Style Format Strings

Combine marker with line and color:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 10)
y = np.sin(x)

plt.plot(x, y, '--*r', ms=20)  # dashed line, star marker, red
plt.show()
```

Common combinations:

- `'-o'`: solid line with circles
- `'--s'`: dashed line with squares
- `':^'`: dotted line with triangles
- `'-.D'`: dash-dot line with diamonds

---

## Comprehensive Example

```python
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3]
y = [1, 5, 2]

plt.plot(x, y, 
         ls="--",       # Line style
         c='k',         # Color (black)
         marker="H",    # Hexagon marker
         ms=20,         # Marker size
         mec="r",       # Edge color (red)
         mfc="b",       # Face color (blue)
         mew=4,         # Edge width
         lw=5,          # Line width
         alpha=0.5)     # Transparency
plt.show()
```

---

## Markers Without Lines

Use empty line style to show only markers:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(20)
y = np.random.rand(20)

plt.plot(x, y, 'o', ms=10)  # Only circles, no line
plt.show()
```

Or explicitly:

```python
plt.plot(x, y, marker='o', linestyle='', ms=10)
```

---

## Marker Every N Points

For dense data, mark every nth point:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, marker='o', markevery=10)  # Mark every 10th point
plt.show()
```

---

## Key Takeaways

- `marker` sets the marker type (`'o'`, `'s'`, `'*'`, etc.)
- `markersize` (`ms`) controls size
- `markeredgecolor` (`mec`) sets border color
- `markerfacecolor` (`mfc`) sets fill color
- `markeredgewidth` (`mew`) sets border thickness
- Format strings combine marker, line, and color: `'--or'`
- Use `markevery` for dense data
