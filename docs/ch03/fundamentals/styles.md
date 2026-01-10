# Lines, Markers, and Styles

Matplotlib provides extensive control over how data is displayed through line styles, markers, and colors.

---

## 1. Basic line plotting

```python
ax.plot(x, y)
```

This draws a solid blue line by default.

---

## 2. Line styles

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

## 3. Markers

```python
ax.plot(x, y, marker="o")
ax.plot(x, y, marker="x")
```

Markers are useful for discrete data points.

---

## 4. Combining styles

```python
ax.plot(x, y, linestyle="--", marker="o")
```

Or shorthand:

```python
ax.plot(x, y, "--o")
```

---

## 5. Visual clarity

Best practices:
- avoid clutter,
- use markers sparingly,
- ensure readability.

---

## Key takeaways

- Line styles control continuity.
- Markers highlight points.
- Styling improves interpretability.
