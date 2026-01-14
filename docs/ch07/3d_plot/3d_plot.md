# Axes Method - plot (3D)

The `ax.plot` method on 3D axes creates line plots in three-dimensional space. This is particularly useful for visualizing complex-valued functions where real and imaginary parts can be shown as separate dimensions.

## Characteristic Function

The characteristic function of a normal distribution $N(\mu, \sigma^2)$ is:

$$\varphi_{N(\mu,\sigma^2)}(t) = e^{i\mu t - \frac{1}{2}\sigma^2 t^2}$$

This complex-valued function can be visualized in 3D with time on one axis, real part on another, and imaginary part on the third.

## Basic Usage

Plot complex functions in 3D space.

### 1. Simple 3D Line

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4 * np.pi, 200)
x = np.cos(t)
y = np.sin(t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, x, y)
plt.show()
```

### 2. With Labels

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, x, y)
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y')
plt.show()
```

## Normal Distribution Visualization

Complete visualization of PDF, CDF, and characteristic function.

### 1. Complete Example

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

mu = 3.0
sigma = 2.6
x = np.linspace(-20, 20, 100)
t = np.linspace(-15, 15, 1000)

i = complex(0, 1)
chf = np.exp(i * mu * t - sigma * sigma * t**2 / 2.0)
pdf = stats.norm(mu, sigma).pdf(x)
cdf = stats.norm(mu, sigma).cdf(x)
chf_real = np.real(chf)
chf_imag = np.imag(chf)

fig = plt.figure(figsize=(12, 4))
ax0 = fig.add_subplot(1, 3, 1)
ax1 = fig.add_subplot(1, 3, 2)
ax2 = fig.add_subplot(1, 3, 3, projection='3d')

ax0.plot(x, pdf)
ax1.plot(x, cdf)
ax2.plot(t, chf_real, chf_imag, 'blue')

for ax, title in zip((ax0, ax1), ('PDF', 'CDF')):
    ax.grid()
    ax.set_xlabel('x')
    ax.set_title(title)

ax2.set_xlabel('time')
ax2.set_ylabel('real')
ax2.set_zlabel('imag')
ax2.set_title('Characteristic Function')
ax2.view_init(30, -120)

plt.tight_layout()
plt.show()
```

### 2. PDF Only

```python
mu = 0
sigma = 1
x = np.linspace(-4, 4, 100)

fig, ax = plt.subplots()
ax.plot(x, stats.norm(mu, sigma).pdf(x))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Normal PDF (μ={mu}, σ={sigma})')
ax.grid()
plt.show()
```

### 3. CDF Only

```python
fig, ax = plt.subplots()
ax.plot(x, stats.norm(mu, sigma).cdf(x))
ax.set_xlabel('x')
ax.set_ylabel('F(x)')
ax.set_title(f'Normal CDF (μ={mu}, σ={sigma})')
ax.grid()
plt.show()
```

### 4. Characteristic Function Only

```python
mu = 3.0
sigma = 2.6
t = np.linspace(-15, 15, 1000)

i = complex(0, 1)
chf = np.exp(i * mu * t - sigma**2 * t**2 / 2.0)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf), 'blue')
ax.set_xlabel('t')
ax.set_ylabel('Re(φ)')
ax.set_zlabel('Im(φ)')
ax.set_title('Characteristic Function')
ax.view_init(30, -120)
plt.show()
```

## Complex Function Visualization

Visualize complex-valued functions in 3D.

### 1. Complex Exponential

```python
t = np.linspace(0, 4 * np.pi, 500)
z = np.exp(1j * t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(z), np.imag(z), 'blue')
ax.set_xlabel('t')
ax.set_ylabel('Re(z)')
ax.set_zlabel('Im(z)')
ax.set_title('$e^{it}$')
plt.show()
```

### 2. Damped Complex Exponential

```python
t = np.linspace(0, 4 * np.pi, 500)
z = np.exp((-0.1 + 1j) * t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(z), np.imag(z), 'green')
ax.set_xlabel('t')
ax.set_ylabel('Re(z)')
ax.set_zlabel('Im(z)')
ax.set_title('$e^{(-0.1+i)t}$ (Damped)')
plt.show()
```

### 3. Growing Complex Exponential

```python
t = np.linspace(0, 2 * np.pi, 500)
z = np.exp((0.1 + 1j) * t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(z), np.imag(z), 'red')
ax.set_xlabel('t')
ax.set_ylabel('Re(z)')
ax.set_zlabel('Im(z)')
ax.set_title('$e^{(0.1+i)t}$ (Growing)')
plt.show()
```

### 4. Complex Exponential Comparison

```python
t = np.linspace(0, 4 * np.pi, 500)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

# Pure oscillation
z1 = np.exp(1j * t)
axes[0].plot(t, np.real(z1), np.imag(z1), 'blue')
axes[0].set_title('$e^{it}$ (Oscillating)')

# Damped
z2 = np.exp((-0.15 + 1j) * t)
axes[1].plot(t, np.real(z2), np.imag(z2), 'green')
axes[1].set_title('$e^{(-0.15+i)t}$ (Damped)')

# Growing
z3 = np.exp((0.1 + 1j) * t)
axes[2].plot(t, np.real(z3), np.imag(z3), 'red')
axes[2].set_title('$e^{(0.1+i)t}$ (Growing)')

for ax in axes:
    ax.set_xlabel('t')
    ax.set_ylabel('Re')
    ax.set_zlabel('Im')

plt.tight_layout()
plt.show()
```

## Characteristic Functions of Different Distributions

### 1. Standard Normal

```python
t = np.linspace(-10, 10, 500)
chf = np.exp(-t**2 / 2)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf), 'blue')
ax.set_xlabel('t')
ax.set_ylabel('Re(φ)')
ax.set_zlabel('Im(φ)')
ax.set_title('Standard Normal: $\\varphi(t) = e^{-t^2/2}$')
ax.view_init(30, -120)
plt.show()
```

### 2. Normal with Different Parameters

```python
t = np.linspace(-10, 10, 500)

fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

params = [(0, 1), (2, 1), (0, 2)]
titles = ['μ=0, σ=1', 'μ=2, σ=1', 'μ=0, σ=2']

for ax, (mu, sigma), title in zip(axes, params, titles):
    chf = np.exp(1j * mu * t - sigma**2 * t**2 / 2)
    ax.plot(t, np.real(chf), np.imag(chf), 'blue')
    ax.set_xlabel('t')
    ax.set_ylabel('Re')
    ax.set_zlabel('Im')
    ax.set_title(title)
    ax.view_init(30, -120)

plt.tight_layout()
plt.show()
```

### 3. Exponential Distribution

```python
# Characteristic function: φ(t) = λ / (λ - it)
lam = 1.0
t = np.linspace(-5, 5, 500)
chf = lam / (lam - 1j * t)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf), 'green')
ax.set_xlabel('t')
ax.set_ylabel('Re(φ)')
ax.set_zlabel('Im(φ)')
ax.set_title('Exponential: $\\varphi(t) = \\frac{\\lambda}{\\lambda - it}$')
ax.view_init(30, -120)
plt.show()
```

### 4. Cauchy Distribution

```python
# Characteristic function: φ(t) = e^{-|t|}
t = np.linspace(-5, 5, 500)
chf = np.exp(-np.abs(t))

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf), 'red')
ax.set_xlabel('t')
ax.set_ylabel('Re(φ)')
ax.set_zlabel('Im(φ)')
ax.set_title('Cauchy: $\\varphi(t) = e^{-|t|}$')
ax.view_init(30, -120)
plt.show()
```

## View Angle Control

Adjust viewing perspective for optimal visualization.

### 1. Default View

```python
t = np.linspace(-10, 10, 500)
mu, sigma = 2, 1.5
chf = np.exp(1j * mu * t - sigma**2 * t**2 / 2)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf))
ax.set_title('Default View')
plt.show()
```

### 2. Custom View

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf))
ax.view_init(30, -120)
ax.set_title('view_init(30, -120)')
plt.show()
```

### 3. View Comparison

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10), subplot_kw={'projection': '3d'})

views = [(30, -60), (30, -120), (60, -90), (15, -150)]

for ax, (elev, azim) in zip(axes.flat, views):
    ax.plot(t, np.real(chf), np.imag(chf), 'blue')
    ax.view_init(elev, azim)
    ax.set_title(f'elev={elev}, azim={azim}')
    ax.set_xlabel('t')
    ax.set_ylabel('Re')
    ax.set_zlabel('Im')

plt.tight_layout()
plt.show()
```

## Line Styling

Apply styling to 3D plots.

### 1. Color and Width

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot(t, np.real(chf), np.imag(chf), color='purple', linewidth=2)
ax.set_xlabel('t')
ax.set_ylabel('Re')
ax.set_zlabel('Im')
plt.show()
```

### 2. Line Styles

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})

styles = ['-', '--', ':']
titles = ['Solid', 'Dashed', 'Dotted']

for ax, style, title in zip(axes, styles, titles):
    ax.plot(t, np.real(chf), np.imag(chf), linestyle=style)
    ax.set_title(title)
    ax.view_init(30, -120)

plt.tight_layout()
plt.show()
```

### 3. Alpha Transparency

```python
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

# Multiple characteristic functions with transparency
for mu in [0, 1, 2, 3]:
    chf = np.exp(1j * mu * t - t**2 / 2)
    ax.plot(t, np.real(chf), np.imag(chf), alpha=0.7, label=f'μ={mu}')

ax.legend()
ax.set_xlabel('t')
ax.set_ylabel('Re')
ax.set_zlabel('Im')
ax.view_init(30, -120)
plt.show()
```

## Combined 2D and 3D Subplots

Mix 2D and 3D plots in the same figure.

### 1. Using add_subplot

```python
mu = 3.0
sigma = 2.6
x = np.linspace(-20, 20, 100)
t = np.linspace(-15, 15, 1000)

chf = np.exp(1j * mu * t - sigma**2 * t**2 / 2)
pdf = stats.norm(mu, sigma).pdf(x)
cdf = stats.norm(mu, sigma).cdf(x)

fig = plt.figure(figsize=(12, 4))

ax0 = fig.add_subplot(1, 3, 1)
ax0.plot(x, pdf)
ax0.set_title('PDF')
ax0.grid()

ax1 = fig.add_subplot(1, 3, 2)
ax1.plot(x, cdf)
ax1.set_title('CDF')
ax1.grid()

ax2 = fig.add_subplot(1, 3, 3, projection='3d')
ax2.plot(t, np.real(chf), np.imag(chf))
ax2.set_title('Characteristic Function')
ax2.view_init(30, -120)

plt.tight_layout()
plt.show()
```

### 2. Four-Panel Layout

```python
fig = plt.figure(figsize=(12, 10))

# PDF
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, pdf, 'b-')
ax1.fill_between(x, pdf, alpha=0.3)
ax1.set_title('Probability Density Function')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.grid()

# CDF
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, cdf, 'g-')
ax2.set_title('Cumulative Distribution Function')
ax2.set_xlabel('x')
ax2.set_ylabel('F(x)')
ax2.grid()

# Real and Imaginary parts
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(t, np.real(chf), 'b-', label='Real')
ax3.plot(t, np.imag(chf), 'r-', label='Imaginary')
ax3.set_title('Characteristic Function Components')
ax3.set_xlabel('t')
ax3.legend()
ax3.grid()

# 3D Characteristic Function
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot(t, np.real(chf), np.imag(chf), 'purple')
ax4.set_title('3D Characteristic Function')
ax4.set_xlabel('t')
ax4.set_ylabel('Re(φ)')
ax4.set_zlabel('Im(φ)')
ax4.view_init(30, -120)

plt.tight_layout()
plt.show()
```

## Practical Applications

### 1. Distribution Comparison Dashboard

```python
from scipy import stats

x = np.linspace(-5, 5, 200)
t = np.linspace(-5, 5, 500)

distributions = [
    ('Normal', stats.norm(0, 1), np.exp(-t**2 / 2)),
    ('Laplace', stats.laplace(0, 1), 1 / (1 + t**2)),
]

fig = plt.figure(figsize=(14, 5))

for idx, (name, dist, chf) in enumerate(distributions):
    # PDF
    ax1 = fig.add_subplot(2, 3, idx * 3 + 1)
    ax1.plot(x, dist.pdf(x))
    ax1.set_title(f'{name} PDF')
    ax1.grid()
    
    # CDF
    ax2 = fig.add_subplot(2, 3, idx * 3 + 2)
    ax2.plot(x, dist.cdf(x))
    ax2.set_title(f'{name} CDF')
    ax2.grid()
    
    # Characteristic Function
    ax3 = fig.add_subplot(2, 3, idx * 3 + 3, projection='3d')
    ax3.plot(t, np.real(chf), np.imag(chf))
    ax3.set_title(f'{name} CF')
    ax3.view_init(30, -120)

plt.tight_layout()
plt.show()
```

### 2. Publication-Quality Figure

```python
mu = 3.0
sigma = 2.6
x = np.linspace(-15, 20, 200)
t = np.linspace(-10, 10, 1000)

chf = np.exp(1j * mu * t - sigma**2 * t**2 / 2)
pdf = stats.norm(mu, sigma).pdf(x)
cdf = stats.norm(mu, sigma).cdf(x)

fig = plt.figure(figsize=(14, 4))

# PDF
ax0 = fig.add_subplot(1, 3, 1)
ax0.plot(x, pdf, 'steelblue', linewidth=2)
ax0.fill_between(x, pdf, alpha=0.3, color='steelblue')
ax0.set_xlabel('$x$', fontsize=12)
ax0.set_ylabel('$f(x)$', fontsize=12)
ax0.set_title(f'PDF: $N({mu}, {sigma}^2)$', fontsize=13)
ax0.grid(alpha=0.3)

# CDF
ax1 = fig.add_subplot(1, 3, 2)
ax1.plot(x, cdf, 'darkgreen', linewidth=2)
ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$F(x)$', fontsize=12)
ax1.set_title('Cumulative Distribution', fontsize=13)
ax1.grid(alpha=0.3)

# Characteristic Function
ax2 = fig.add_subplot(1, 3, 3, projection='3d')
ax2.plot(t, np.real(chf), np.imag(chf), 'darkviolet', linewidth=1.5)
ax2.set_xlabel('$t$', fontsize=11)
ax2.set_ylabel('$\\mathrm{Re}(\\varphi)$', fontsize=11)
ax2.set_zlabel('$\\mathrm{Im}(\\varphi)$', fontsize=11)
ax2.set_title('$\\varphi(t) = e^{i\\mu t - \\sigma^2 t^2/2}$', fontsize=13)
ax2.view_init(25, -130)

plt.suptitle(f'Normal Distribution: $\\mu={mu}$, $\\sigma={sigma}$', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

### 3. Interactive Parameter Exploration

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw={'projection': '3d'})

t = np.linspace(-10, 10, 500)

# Varying mu
mus = [0, 2, 4]
for ax, mu in zip(axes[0], mus):
    chf = np.exp(1j * mu * t - t**2 / 2)
    ax.plot(t, np.real(chf), np.imag(chf), 'blue')
    ax.set_title(f'μ = {mu}, σ = 1')
    ax.view_init(30, -120)

# Varying sigma
sigmas = [0.5, 1, 2]
for ax, sigma in zip(axes[1], sigmas):
    chf = np.exp(-sigma**2 * t**2 / 2)
    ax.plot(t, np.real(chf), np.imag(chf), 'green')
    ax.set_title(f'μ = 0, σ = {sigma}')
    ax.view_init(30, -120)

for ax in axes.flat:
    ax.set_xlabel('t')
    ax.set_ylabel('Re')
    ax.set_zlabel('Im')

plt.tight_layout()
plt.show()
```
