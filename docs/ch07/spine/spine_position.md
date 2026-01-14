# Spine Position

Move spines to create math-style coordinate systems or custom layouts.

---

## set_position

Move a spine to a specific location:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
plt.show()
```

---

## Position Types

The `set_position()` method accepts different position types:

**'zero'**: Position at data coordinate 0
```python
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
```

**'center'**: Position at the center of the axes
```python
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('center')
```

**('data', value)**: Position at a specific data coordinate
```python
ax.spines['bottom'].set_position(('data', -15))
ax.spines['left'].set_position(('data', 0))
```

**('axes', fraction)**: Position as a fraction of axes (0 to 1)
```python
ax.spines['bottom'].set_position(('axes', 0.5))  # Middle of axes
```

**('outward', points)**: Position outward from data area
```python
ax.spines['left'].set_position(('outward', 10))  # 10 points outward
```

---

## Centered Axes (Math Style)

Create a coordinate system centered at the origin:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(x, y)

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Move bottom and left to zero
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

plt.show()
```

---

## set_bounds

Limit the extent of a spine:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 2, 100)
y1 = x**3 + 5*x**2 + 10
y2 = 3*x**2 + 10*x
y3 = 6*x + 10

fig, ax = plt.subplots()
ax.plot(x, y1, color="blue", label="y(x)", lw=2)
ax.plot(x, y2, color="red", label="y'(x)", lw=2)
ax.plot(x, y3, color="green", label='y"(x)', lw=2)

ax.axhline(0, color='k', lw=1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xticks([-4, -2, 0, 2])
ax.set_yticks([-10, 0, 10, 20, 30])

# Position and bound spines
ax.spines['bottom'].set_position(('data', -15))
ax.spines['left'].set_bounds(low=-15, high=41)
ax.spines['right'].set_bounds(low=-15, high=41)

ax.legend(ncol=3, loc=2, bbox_to_anchor=(0, 1), frameon=False)
plt.show()
```

---

## Complete Example: Mathematical Function Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y, 'b-', lw=2)

# Set up ticks
ax.set_yticks([-1, 0, 1])
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels(['$-2\\pi$', '$-\\pi$', '0', '$\\pi$', '$2\\pi$'])

# Minor ticks
ax.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 17), minor=True)

# Configure spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.set_title('$y = \\sin(x)$', pad=20)
plt.show()
```

---

## Arrow-Style Axis

Create arrows at the end of axes:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)

# Position spines at zero
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Add arrows (requires additional configuration)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

plt.show()
```

---

## Key Takeaways

- `set_position('zero')` moves spine to data coordinate 0
- `set_position('center')` moves spine to axes center
- `set_position(('data', value))` positions at specific data value
- `set_position(('axes', fraction))` positions as fraction of axes
- `set_bounds(low, high)` limits spine extent
- Combine with hidden spines for clean math-style plots
