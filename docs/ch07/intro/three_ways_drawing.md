# Three Ways of Drawing

Matplotlib behaves differently depending on where you run your code: Jupyter Notebook, Python files, or the terminal.

---

## Jupyter Notebook

In Jupyter notebooks, plots render automatically inline.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
# No plt.show() needed - displays automatically
```

**Key points:**

- Neither `plt.show()` nor `plt.draw()` are required
- Plots appear below the cell
- Use `%matplotlib inline` for static images
- Use `%matplotlib notebook` for interactive plots

### Magic Commands

```python
%matplotlib inline    # Static images (default in modern Jupyter)
%matplotlib notebook  # Interactive (zoom, pan)
%matplotlib widget    # Interactive in JupyterLab
```

---

## Python File (.py)

When running Python scripts, you must explicitly display plots.

```python
# script.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()  # Required - opens interactive window
```

**Key points:**

- `plt.show()` starts an event loop
- Opens one or more interactive windows
- Script blocks until windows are closed
- Looks for all active figure objects

### Running the Script

```bash
python script.py
```

A window will open displaying the plot. The script continues after you close the window.

---

## Terminal (Interactive Python)

In an interactive Python session, use `plt.draw()` for updates.

```python
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> 
>>> plt.ion()  # Turn on interactive mode
>>> x = np.linspace(0, 10, 100)
>>> plt.plot(x, np.sin(x))
>>> plt.draw()  # Updates the figure
```

**Key points:**

- `plt.ion()` enables interactive mode
- `plt.draw()` updates the figure without blocking
- `plt.ioff()` disables interactive mode
- Useful for dynamic updates

---

## Comparison

| Environment | Display Method | Blocking | Interactive |
|-------------|----------------|----------|-------------|
| Jupyter | Automatic | No | Optional |
| Python file | `plt.show()` | Yes | Yes |
| Terminal | `plt.draw()` | No | Yes |

---

## plt.show() vs plt.draw()

### plt.show()

- Starts the event loop
- Blocks execution until window closed
- Displays all pending figures
- Used in scripts

```python
plt.plot([1, 2, 3])
plt.show()  # Blocks here
print("After show")  # Runs after window closed
```

### plt.draw()

- Redraws the current figure
- Non-blocking
- Used for animations and updates
- Requires interactive mode

```python
plt.ion()
plt.plot([1, 2, 3])
plt.draw()  # Non-blocking
print("Continues immediately")
```

---

## Best Practices

1. **Jupyter**: Let automatic display work; use magic commands for interactivity
2. **Scripts**: Always end with `plt.show()`
3. **Interactive**: Use `plt.ion()` and `plt.draw()` for dynamic updates
4. **Saving**: Use `plt.savefig()` before `plt.show()` in scripts

---

## Key Takeaways

- Jupyter: automatic display, no `show()` needed
- Python files: `plt.show()` required, blocks until closed
- Terminal: `plt.draw()` for non-blocking updates
- `plt.ion()` enables interactive mode
- Choose the right approach for your environment
