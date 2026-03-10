# scipy.interpolate — Spline Interpolation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

While NumPy's `polyfit` fits a single polynomial to data, `scipy.interpolate` provides piecewise spline interpolation that avoids the oscillation problems of high-degree polynomials. Spline interpolation is essential in financial mathematics for constructing smooth yield curves, volatility surfaces, and forward rate curves from discrete market data.

---

## interp1d — 1D Interpolation

The `interp1d` function creates a callable interpolant from discrete $(x, y)$ data:

```python
import numpy as np
from scipy.interpolate import interp1d

x = np.array([0.1, 0.5, 1.0, 2.0, 5.0, 10.0])
y = np.array([0.0, 0.109, 0.212, 0.274, 0.147, 0.002])

f_linear = interp1d(x, y, kind='linear')
f_cubic = interp1d(x, y, kind='cubic')

# Evaluate at any point within the data range
x_fine = np.linspace(x.min(), x.max(), 200)
y_linear = f_linear(x_fine)
y_cubic = f_cubic(x_fine)
```

The `kind` parameter selects the interpolation method: `'linear'` (default), `'quadratic'`, `'cubic'`, or an integer specifying the spline order.

### Combining Interpolation with Integration

A powerful pattern is to interpolate discrete data and then integrate the smooth interpolant. This computes quantities like the expected value of an empirical distribution:

```python
from scipy.integrate import quad

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.662, 0.8, 1., 1.25,
              1.5, 2., 3., 4., 5., 6., 8., 10.])
y = np.array([0., 0.032, 0.06, 0.086, 0.109, 0.131, 0.151, 0.185,
              0.212, 0.238, 0.257, 0.274, 0.256, 0.205, 0.147, 0.096, 0.029, 0.002])

f = interp1d(x, y, 'cubic')

numerator = quad(lambda t: t * f(t), x.min(), x.max())[0]
denominator = quad(f, x.min(), x.max())[0]
mean = numerator / denominator  # ≈ 3.38
```

### Interpolation for ODE Solving

Tabulated data can be converted into smooth functions for use as coefficients in differential equations:

```python
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp

t_data = np.array([0., 0.25, 0.5, 0.75, 1.])
m_data = np.array([1., 0.99912, 0.97188, 0.78643, 0.1])

m = interp1d(t_data, m_data, 'cubic')
m_prime = m._spline.derivative(nu=1)

a, b = 0.78, 0.1
def dvdt(t, v):
    return -a - b * v**2 / m(t) - m_prime(t) / m(t)

sol = solve_ivp(dvdt, [1e-4, 1], y0=[0], t_eval=np.linspace(1e-4, 1, 1000))
```

## interp2d — 2D Surface Interpolation

For data defined on a 2D grid, `interp2d` constructs a smooth surface interpolant:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

# Scattered data on a 5×5 grid
x = np.array([0., 0.25, 0.5, 0.75, 1.] * 5)
y = np.repeat([0., 0.25, 0.5, 0.75, 1.], 5)
z = x**2 + y**2  # z = x² + y²

f = interp2d(x, y, z, kind='cubic')

# Evaluate on a fine grid
x_fine = np.linspace(0, 1, 100)
y_fine = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_fine, y_fine)
Z = f(x_fine, y_fine)

fig, ax = plt.subplots(figsize=(8, 6), subplot_kw={'projection': '3d'})
ax.plot_surface(X, Y, Z, alpha=0.8)
for xx, yy, zz in zip(x, y, z):
    ax.plot(xx, yy, zz, 'or')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
```

### Financial Application

2D interpolation is used extensively in quantitative finance for constructing volatility surfaces from discrete option market data (strike × maturity grid), interpolating yield curve surfaces across tenors and dates, and building smooth forward rate surfaces for interest rate modeling.

## Summary

`scipy.interpolate` provides spline-based interpolation that complements NumPy's polynomial fitting. Use `interp1d` for 1D curve interpolation and `interp2d` for 2D surface construction. The resulting callable objects integrate seamlessly with `scipy.integrate.quad` and `scipy.integrate.solve_ivp`.
