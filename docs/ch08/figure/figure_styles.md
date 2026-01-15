# Figure Styles

Matplotlib provides built-in style sheets for consistent and professional-looking plots.

---

## Available Styles

List all available styles:

```python
import matplotlib.pyplot as plt

print(plt.style.available)
```

Common styles include:

- `'seaborn-v0_8-darkgrid'`
- `'ggplot'`
- `'bmh'`
- `'fivethirtyeight'`
- `'dark_background'`

---

## Using plt.style.use

Apply a style globally:

```python
import matplotlib.pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6]
avg_t = [25, 28, 28, 26, 20, 22, 21]

plt.style.use("seaborn-v0_8-darkgrid")

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(days, avg_t, 'r--o')
plt.show()
```

---

## Temporary Style Context

Apply a style temporarily using a context manager:

```python
import matplotlib.pyplot as plt

with plt.style.context('ggplot'):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4])
    plt.show()

# Style reverts after the context
```

---

## The xkcd Style

Create hand-drawn style plots:

```python
import matplotlib.pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6]
avg_t = [25, 28, 28, 26, 20, 22, 21]

plt.xkcd()

fig, ax = plt.subplots(figsize=(12, 3))
ax.plot(days, avg_t, 'r--o')
plt.show()
```

!!! note
    The xkcd style requires the "Humor Sans" font for best results.

---

## Combining Multiple Styles

Styles can be combined by passing a list:

```python
plt.style.use(['seaborn-v0_8-darkgrid', 'seaborn-v0_8-talk'])
```

Later styles override earlier ones for conflicting settings.

---

## Creating Custom Styles

Create a custom style file (e.g., `mystyle.mplstyle`):

```
# mystyle.mplstyle
axes.facecolor: white
axes.edgecolor: black
axes.grid: True
grid.color: gray
grid.linestyle: --
lines.linewidth: 2
font.size: 12
```

Use it with:

```python
plt.style.use('./mystyle.mplstyle')
```

---

## Resetting to Default

Reset to Matplotlib defaults:

```python
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
```

Or use the default style:

```python
plt.style.use('default')
```

---

## Key Takeaways

- `plt.style.available` lists all built-in styles
- `plt.style.use()` applies a style globally
- Use context managers for temporary style changes
- `plt.xkcd()` creates hand-drawn style plots
- Custom styles can be saved as `.mplstyle` files
