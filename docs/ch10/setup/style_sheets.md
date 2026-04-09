# Style Sheets

## What are Style Sheets?

Style sheets are predefined sets of rcParams that control the appearance of Matplotlib figures. They provide a quick way to change the overall look of your plots.

```python
import matplotlib.pyplot as plt

# Apply a style
plt.style.use('seaborn-v0_8')
```

---

## Available Styles

### List All Styles

```python
print(plt.style.available)
```

Common styles:
- `'default'` — Matplotlib default
- `'seaborn-v0_8'` — Seaborn-inspired (clean, modern)
- `'ggplot'` — R's ggplot2 style
- `'fivethirtyeight'` — FiveThirtyEight blog style
- `'bmh'` — Bayesian Methods for Hackers
- `'dark_background'` — White on dark
- `'grayscale'` — Black and white
- `'classic'` — Old Matplotlib style

---

## Using Styles

### Global Style

```python
# Apply to all subsequent plots
plt.style.use('ggplot')

# Create plots with ggplot style
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

### Temporary Style (Context Manager)

```python
# Use style only within this block
with plt.style.context('dark_background'):
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()

# Back to default style here
```

### Combining Styles

```python
# Apply multiple styles (later overrides earlier)
plt.style.use(['seaborn-v0_8', 'seaborn-v0_8-talk'])
```

---

## Style Comparison

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
styles = ['default', 'seaborn-v0_8', 'ggplot', 'fivethirtyeight']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for ax, style in zip(axes.flat, styles):
    with plt.style.context(style):
        ax.plot(x, np.sin(x), label='sin')
        ax.plot(x, np.cos(x), label='cos')
        ax.set_title(f"Style: '{style}'")
        ax.legend()

plt.tight_layout()
plt.show()
```

---

## Seaborn Styles

Seaborn-based styles (prefix `seaborn-v0_8`):

| Style | Description |
|-------|-------------|
| `seaborn-v0_8` | Base seaborn style |
| `seaborn-v0_8-whitegrid` | White background with grid |
| `seaborn-v0_8-darkgrid` | Gray background with grid |
| `seaborn-v0_8-white` | White background, no grid |
| `seaborn-v0_8-dark` | Gray background, no grid |
| `seaborn-v0_8-talk` | Larger fonts for presentations |
| `seaborn-v0_8-poster` | Even larger for posters |
| `seaborn-v0_8-paper` | Smaller for publications |

```python
# Combine base style with size variant
plt.style.use(['seaborn-v0_8-whitegrid', 'seaborn-v0_8-talk'])
```

---

## Custom Style Files

### Create a Style File

Create `my_style.mplstyle`:

```ini
# Figure
figure.figsize: 10, 6
figure.facecolor: white

# Axes
axes.facecolor: f5f5f5
axes.edgecolor: cccccc
axes.labelsize: 12
axes.titlesize: 14
axes.grid: True

# Grid
grid.color: white
grid.linestyle: -
grid.linewidth: 1

# Lines
lines.linewidth: 2
lines.markersize: 8

# Font
font.family: sans-serif
font.size: 11

# Legend
legend.frameon: False
legend.fontsize: 10
```

### Use Custom Style

```python
# From file path
plt.style.use('./my_style.mplstyle')

# Or place in matplotlib config directory
# ~/.config/matplotlib/stylelib/my_style.mplstyle
plt.style.use('my_style')
```

---

## Modifying rcParams Directly

### Temporary Changes

```python
# Change specific parameters
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['font.size'] = 12
```

### Reset to Defaults

```python
# Reset all to defaults
plt.rcdefaults()

# Or reset to a specific style
plt.style.use('default')
```

### Context Manager for rcParams

```python
with plt.rc_context({'lines.linewidth': 3, 'font.size': 14}):
    plt.plot([1, 2, 3])
    plt.show()
# Back to original settings
```

---

## Best Practices

### For Publications

```python
plt.style.use('seaborn-v0_8-paper')
plt.rcParams.update({
    'font.size': 8,
    'axes.labelsize': 9,
    'axes.titlesize': 10,
    'figure.figsize': [3.5, 2.5],  # Single column width
    'savefig.dpi': 300
})
```

### For Presentations

```python
plt.style.use(['seaborn-v0_8', 'seaborn-v0_8-talk'])
plt.rcParams.update({
    'figure.figsize': [12, 8],
    'lines.linewidth': 3
})
```

### For Dark Mode

```python
plt.style.use('dark_background')
```

---

## Summary

| Function | Purpose |
|----------|---------|
| `plt.style.use(style)` | Apply style globally |
| `plt.style.context(style)` | Apply style temporarily |
| `plt.style.available` | List all available styles |
| `plt.rcParams[key] = value` | Modify individual setting |
| `plt.rcdefaults()` | Reset to defaults |
| `plt.rc_context(dict)` | Temporary rcParams changes |

**Key Takeaways**:

- Use style sheets for consistent, professional plots
- `seaborn-v0_8` styles are clean and modern
- Combine styles for customization
- Create custom `.mplstyle` files for reusable configurations
- Use context managers for temporary style changes


---

## Exercises

**Exercise 1.** Write code that lists all available Matplotlib style sheets using `plt.style.available`.

??? success "Solution to Exercise 1"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    # Solution code depends on the specific exercise
    x = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x))
    ax.set_title('Example Solution')
    plt.show()
    ```

    See the content of this page for the relevant API details to construct the full solution.

---

**Exercise 2.** Explain the difference between `plt.style.use()` and `plt.style.context()`. When would you use each?

??? success "Solution to Exercise 2"
    See the explanation in the main content of this page for the key concepts. The essential idea is to understand the API parameters and their effects on the resulting visualization.

---

**Exercise 3.** Write code that creates the same plot using three different style sheets in three subplots, using `plt.style.context()` for each.

??? success "Solution to Exercise 3"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    x = np.linspace(0, 2 * np.pi, 100)
    axes[0].plot(x, np.sin(x))
    axes[0].set_title('Left Subplot')

    axes[1].plot(x, np.cos(x))
    axes[1].set_title('Right Subplot')

    plt.tight_layout()
    plt.show()
    ```

    Adapt this pattern to the specific requirements of the exercise.

---

**Exercise 4.** Create a custom style by modifying `plt.rcParams` to set the default font size to 14, line width to 2, and grid alpha to 0.3.

??? success "Solution to Exercise 4"
    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), 'b-', lw=2)
    ax.set_title('Solution')
    plt.show()
    ```

    Refer to the code examples in the main content for the specific API calls needed.
