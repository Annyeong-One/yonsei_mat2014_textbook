# Line Styles and Colors

Matplotlib provides extensive control over line appearance through style and color parameters.

---

## Line Style (linestyle / ls)

Common line styles:

| Style | Abbreviation | Description |
|-------|--------------|-------------|
| `'-'` | solid | Solid line (default) |
| `'--'` | dashed | Dashed line |
| `':'` | dotted | Dotted line |
| `'-.'` | dashdot | Dash-dot pattern |

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y, linestyle='--')
plt.show()
```

Short form:

```python
ax.plot(x, y, ls='--')
```

---

## Line Width (linewidth / lw)

Control line thickness:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y, linestyle='--', linewidth=10)
plt.show()
```

Short form:

```python
ax.plot(x, y, ls='--', lw=10)
```

---

## Color (color / c)

Specify colors in multiple ways:

**Named colors:**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y_sin, color='red')
ax.plot(x, y_cos, color='blue')
plt.show()
```

**Single-letter codes:**
```python
ax.plot(x, y_sin, c='r')  # red
ax.plot(x, y_cos, c='b')  # blue
```

| Code | Color |
|------|-------|
| `'b'` | Blue |
| `'g'` | Green |
| `'r'` | Red |
| `'c'` | Cyan |
| `'m'` | Magenta |
| `'y'` | Yellow |
| `'k'` | Black |
| `'w'` | White |

**Hex codes:**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y_sin, c='#e32b2b')  # Custom red
ax.plot(x, y_cos, c='#3b81f1')  # Custom blue
plt.show()
```

---

## Alpha (Transparency)

Control opacity with alpha (0 = transparent, 1 = opaque):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(15, 4))
ax.plot(x, y_sin, alpha=0.8)
ax.plot(x, y_cos, alpha=0.2)
plt.show()
```

---

## MATLAB-Style Format Strings

Combine style, color, and marker in a single string:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 10)
y = np.sin(x)

plt.plot(x, y, '--*r', ms=20)  # dashed, star markers, red
plt.show()
```

Format: `'[marker][line][color]'` or `'[line][marker][color]'`

Examples:

- `'--*r'`: dashed line, star markers, red
- `'-ob'`: solid line, circle markers, blue
- `':sg'`: dotted line, square markers, green

---

## Using Keyword Dictionaries

Pass multiple style options via dictionary:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(15, 3))
ax.plot(x, y, **{'ls': '--', 'lw': 10})
plt.show()
```

---

## Complete Example

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 4))

ax.plot(x, y_sin, 
        linestyle='--', 
        linewidth=2, 
        color='#e74c3c', 
        alpha=0.8,
        label='sin(x)')

ax.plot(x, y_cos, 
        ls=':', 
        lw=3, 
        c='#3498db', 
        alpha=0.8,
        label='cos(x)')

ax.legend()
ax.set_title('Trigonometric Functions')
plt.show()
```

---

## Key Takeaways

- Use `linestyle` or `ls` for line pattern
- Use `linewidth` or `lw` for thickness
- Use `color` or `c` for color
- Colors can be names, single letters, or hex codes
- `alpha` controls transparency (0-1)
- Format strings combine options: `'--or'`
