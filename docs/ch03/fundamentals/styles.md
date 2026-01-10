# Lines, Markers, and

Matplotlib provides extensive control over how data is displayed through line styles, markers, and colors.

---

## Basic line plotting

```python
ax.plot(x, y)
```

This draws a solid blue line by default.

---

## Line styles

```python
ax.plot(x, y, linestyle="--")
ax.plot(x, y, linestyle=":")
```

Common styles:
- `"-"` solid
- `"--"` dashed
- `":"` dotted
- `"-."` dash-dot

---

## Markers

```python
ax.plot(x, y, marker="o")
ax.plot(x, y, marker="x")
```

Markers are useful for discrete data points.

---

## Combining styles

```python
ax.plot(x, y, linestyle="--", marker="o")
```

Or shorthand:

```python
ax.plot(x, y, "--o")
```

---

## Visual clarity

Best practices:
- avoid clutter,
- use markers sparingly,
- ensure readability.

---

## Key takeaways

- Line styles control continuity.
- Markers highlight points.
- Styling improves interpretability.
