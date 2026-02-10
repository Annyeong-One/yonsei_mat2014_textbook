# Mathematical Functions

Create publication-quality mathematical function plots.

---

## Basic Function Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_title(r'$y = \sin(x)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.grid(True, alpha=0.3)
plt.show()
```

---

## Centered Axes Style

Create math-textbook style plots:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x, y, 'b-', linewidth=2)

# Configure ticks
ax.set_yticks([-1, 0, 1])
ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_xticklabels([r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])

# Minor ticks
ax.set_xticks(np.linspace(-2*np.pi, 2*np.pi, 17), minor=True)

# Move spines to origin
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.set_title(r'$y = \sin(x)$', pad=20)
plt.show()
```

---

## Riemann Sum Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**3 - x**2 + x + 1

x = np.linspace(0, np.pi, 100)
y = f(x)

n_grid = 20
x_grid = np.linspace(0, np.pi, n_grid + 1)
y_grid = f(x_grid)

def draw_box(x0, x1, y0, ax, color="b"):
    ax.plot([x0, x1], [0, 0], color=color)
    ax.plot([x0, x1], [y0, y0], color=color)
    ax.plot([x0, x0], [0, y0], color=color)
    ax.plot([x1, x1], [0, y0], color=color)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, y, 'r-', linewidth=2, label=r'$f(x) = x^3 - x^2 + x + 1$')

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")

integral_val = 0
for x0, x1, y0 in zip(x_grid[:-1], x_grid[1:], y_grid[:-1]):
    draw_box(x0, x1, y0, ax)
    integral_val += (x1 - x0) * y0

ax.set_title(f"Riemann Sum Approximation: {integral_val:.2f}")
ax.legend()
plt.show()
```

---

## Star Polygon (Procedural)

```python
import matplotlib.pyplot as plt
import numpy as np

n = 10
skip = 3

thetas = np.linspace(0, 2*np.pi, n, endpoint=False) + np.pi/2
d_theta = thetas[1] - thetas[0]

def draw_line(theta, skip, ax, color="b"):
    x0 = np.cos(theta)
    y0 = np.sin(theta)
    x1 = np.cos(theta + d_theta * skip)
    y1 = np.sin(theta + d_theta * skip)
    ax.plot([x0, x1], [y0, y1], color=color)

fig, ax = plt.subplots(figsize=(4, 4))
for theta in thetas:
    draw_line(theta, skip, ax)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(f'{n}-point star (skip={skip})')
plt.show()
```

---

## Star Polygon (Object-Oriented)

```python
import matplotlib.pyplot as plt
import numpy as np

class Star:
    def __init__(self, n, skip):
        self.n = n
        self.skip = skip
        self.thetas = np.linspace(0, 2*np.pi, n, endpoint=False) + np.pi/2
        self.d_theta = self.thetas[1] - self.thetas[0]
    
    def draw_line(self, theta, ax, color="b"):
        x0 = np.cos(theta)
        y0 = np.sin(theta)
        x1 = np.cos(theta + self.d_theta * self.skip)
        y1 = np.sin(theta + self.d_theta * self.skip)
        ax.plot([x0, x1], [y0, y1], color=color)
    
    def draw_star(self):
        fig, ax = plt.subplots(figsize=(4, 4))
        for theta in self.thetas:
            self.draw_line(theta, ax)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(f'{self.n}-point star (skip={self.skip})')
        plt.show()

# Create different stars
Star(10, 2).draw_star()
Star(10, 3).draw_star()
Star(12, 5).draw_star()
```

---

## Derivative Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 2, 100)
y1 = x**3 + 5*x**2 + 10        # f(x)
y2 = 3*x**2 + 10*x              # f'(x)
y3 = 6*x + 10                   # f''(x)

# Critical points (where f'(x) = 0)
x_0 = 0
x_1 = -10/3

# Function values at critical points
y1_0 = x_0**3 + 5*x_0**2 + 10
y1_1 = x_1**3 + 5*x_1**2 + 10

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y1, color="blue", label=r"$f(x) = x^3 + 5x^2 + 10$", lw=2)
ax.plot(x, y2, color="red", label=r"$f'(x) = 3x^2 + 10x$", lw=2)
ax.plot(x, y3, color="green", label=r"$f''(x) = 6x + 10$", lw=2)

# Mark critical points
ax.scatter([x_0, x_1], [y1_0, y1_1], color='k', s=50, zorder=5)
ax.plot([x_0, x_0], [y1_0, 0], color='k', lw=1, ls='--')
ax.plot([x_1, x_1], [y1_1, 0], color='k', lw=1, ls='--')

ax.axhline(0, color='k', lw=1)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_xticks([-4, -2, 0, 2])
ax.set_yticks([-10, 0, 10, 20, 30])

ax.spines['bottom'].set_position(('data', -15))
ax.spines['left'].set_bounds(low=-15, high=41)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(ncol=3, loc='upper left', frameon=False)
ax.set_title('Function and Its Derivatives')

plt.show()
```

---

## Multiple Functions Grid

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 1, 100)
functions = [
    (x**2, r'$x^2$'),
    (np.sin(x), r'$\sin(x)$'),
    (np.exp(x), r'$e^x$'),
    (np.log(x), r'$\ln(x)$'),
    (np.sin(x)/np.exp(x), r'$\frac{\sin(x)}{e^x}$'),
    (np.log(x)/np.exp(x), r'$\frac{\ln(x)}{e^x}$')
]

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

for ax, (y, title) in zip(axes.flat, functions):
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Key Takeaways

- Use centered spines for textbook-style plots
- LaTeX notation in `$...$` for mathematical labels
- `set_aspect('equal')` for geometric figures
- Visualize derivatives and critical points
- Grid layouts compare multiple functions
