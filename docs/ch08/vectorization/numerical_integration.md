# Numerical Integration

Vectorization enables efficient numerical integration via Riemann sums.

## Riemann Sum

### 1. Mathematical Form

$$\int_a^b f(x) \, dx \approx \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

### 2. Discretization

Divide $[a, b]$ into $n$ subintervals of width $\Delta x = \frac{b-a}{n}$.

### 3. Left Endpoint Rule

Use left endpoint of each subinterval for evaluation.

## Basic Example

### 1. Target Integral

$$\int_0^1 x^3 \, dx = \frac{1}{4} = 0.25$$

### 2. Implementation

```python
import numpy as np

def f(x):
    return x ** 3

def main():
    n = 1000
    
    x = np.linspace(0, 1, n + 1)[:-1]  # Left endpoints
    dx = x[1] - x[0]
    y = f(x)
    
    integral = np.sum(y * dx)
    
    print(f"Numerical: {integral:.6f}")
    print(f"Exact:     0.250000")
    print(f"Error:     {abs(integral - 0.25):.6f}")

if __name__ == "__main__":
    main()
```

### 3. Vectorized Computation

The entire sum is computed in one NumPy call.

## Convergence

### 1. Visualization Code

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 3

def main():
    n_values = []
    integral_values = []
    
    for n in range(10, 1000, 10):
        x = np.linspace(0, 1, n + 1)[:-1]
        dx = x[1] - x[0]
        y = f(x)
        numerical = np.sum(y * dx)
        
        n_values.append(n)
        integral_values.append(numerical)
    
    fig, ax = plt.subplots(figsize=(6.5, 4))
    
    ax.set_title(r'Numerical Integration of $\int_0^1 x^3 dx$', fontsize=15)
    ax.plot(n_values, integral_values, '-*', markersize=3)
    ax.axhline(0.25, color='r', linestyle='--', label='Exact = 0.25')
    ax.set_xlabel('Number of Subintervals')
    ax.set_ylabel('Numerical Value')
    ax.legend()
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Convergence Rate

Error decreases as $O(1/n)$ for left Riemann sum.

### 3. Accuracy vs Cost

More subintervals improve accuracy but increase computation.

## Vectorized vs Loop

### 1. Loop Version

```python
import numpy as np
import time

def f(x):
    return x ** 3

def main():
    n = 100000
    a, b = 0, 1
    dx = (b - a) / n
    
    tic = time.time()
    total = 0
    for i in range(n):
        x_i = a + i * dx
        total += f(x_i) * dx
    loop_time = time.time() - tic
    
    print(f"Loop result: {total:.6f}")
    print(f"Loop time:   {loop_time:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Vectorized Version

```python
import numpy as np
import time

def f(x):
    return x ** 3

def main():
    n = 100000
    
    tic = time.time()
    x = np.linspace(0, 1, n + 1)[:-1]
    dx = x[1] - x[0]
    result = np.sum(f(x) * dx)
    vec_time = time.time() - tic
    
    print(f"Vec result:  {result:.6f}")
    print(f"Vec time:    {vec_time:.6f} sec")

if __name__ == "__main__":
    main()
```

### 3. Speedup

Vectorized version is typically 50-100× faster.

## Other Functions

### 1. Gaussian Integral

```python
import numpy as np

def main():
    n = 10000
    a, b = -5, 5
    
    x = np.linspace(a, b, n + 1)[:-1]
    dx = x[1] - x[0]
    
    # Standard normal PDF (unnormalized)
    y = np.exp(-x ** 2 / 2)
    integral = np.sum(y * dx)
    
    exact = np.sqrt(2 * np.pi)
    print(f"Numerical: {integral:.6f}")
    print(f"Exact:     {exact:.6f}")

if __name__ == "__main__":
    main()
```

### 2. Trigonometric

```python
import numpy as np

def main():
    n = 10000
    
    x = np.linspace(0, np.pi, n + 1)[:-1]
    dx = x[1] - x[0]
    
    integral = np.sum(np.sin(x) * dx)
    
    print(f"∫sin(x)dx from 0 to π")
    print(f"Numerical: {integral:.6f}")
    print(f"Exact:     2.000000")

if __name__ == "__main__":
    main()
```

### 3. Custom Functions

Any vectorized function works with this pattern.

## scipy.integrate

For production-quality numerical integration, `scipy.integrate` provides adaptive quadrature methods that are far more accurate and robust than simple Riemann sums.

### Basic Usage: quad

The `quad` function integrates a callable over a finite or infinite interval and returns both the result and an error estimate:

```python
import numpy as np
from scipy.integrate import quad

def f(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

result, error = quad(f, -3, 3)
print(f"Result: {result:.10f}")   # ≈ 0.9973002040
print(f"Error:  {error:.2e}")
```

### Infinite Integration Domains

Replace finite bounds with `np.inf` or `-np.inf` for improper integrals:

```python
result, error = quad(f, -np.inf, np.inf)
print(f"Result: {result:.10f}")   # ≈ 1.0 (standard normal integrates to 1)
```

### Functions with Extra Parameters

Pass additional arguments via the `args` tuple:

```python
def f(x, mu, sigma):
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / np.sqrt(2 * np.pi * sigma**2)

mu, sigma = 3, 2
result, error = quad(f, -np.inf, np.inf, args=(mu, sigma))
print(f"Result: {result:.10f}")   # ≈ 1.0
```

### Controlling Precision

The `epsabs` parameter trades accuracy for speed. Reducing precision can halve computation time when integrating repeatedly:

```python
import time

n = 10_000
t1 = time.perf_counter()
[quad(f, -np.inf, np.inf, args=(mu, sigma)) for _ in range(n)]
t2 = time.perf_counter()
print(f"Default precision: {t2 - t1:.2f} sec")

t1 = time.perf_counter()
[quad(f, -np.inf, np.inf, args=(mu, sigma), epsabs=1e-4) for _ in range(n)]
t2 = time.perf_counter()
print(f"Reduced precision: {t2 - t1:.2f} sec")
```

### Difficult Integrands: the points Parameter

When a function has sharp peaks far from the origin, `quad` may miss them. The `points` parameter directs the adaptive algorithm to examine specific locations:

```python
def f(x):
    return np.exp(-(x - 700)**2) + np.exp(-(x + 700)**2)

# Without guidance — may return 0 (misses the peaks)
result, _ = quad(f, -np.inf, np.inf)

# With guidance — finds both peaks (cannot use infinite bounds with points)
result, _ = quad(f, -800, 800, points=[-700, 700])
print(f"Result: {result:.10f}")   # ≈ 2√π ≈ 3.5449077
```

### Vectorized Integration: quad_vec

When you need to evaluate the same integral for many parameter values, `quad_vec` is dramatically faster than looping over `quad`:

```python
from scipy.integrate import quad_vec

def f(x, alpha):
    return np.exp(-alpha * x**2)

alphas = np.linspace(1, 2, 10_000)

# quad_vec: single call, vectorized over alpha (100x+ faster)
result, error = quad_vec(f, -1, 3, args=(alphas,))
print(f"Mean result: {result.mean():.10f}")
```

The speedup comes from evaluating the integrand at all parameter values simultaneously for each quadrature point, rather than running separate adaptive integrations.

### quad_vec with Multiple Parameters

For parameter grids, use `np.meshgrid` to create broadcast-compatible arrays:

```python
import matplotlib.pyplot as plt
from scipy.integrate import quad_vec

def f(x, a, b):
    return np.exp(-a * (x - b)**2)

a = np.arange(1, 20, 1)
b = np.linspace(0, 5, 100)
av, bv = np.meshgrid(a, b)

integral = quad_vec(f, -1, 3, args=(av, bv))[0]

plt.pcolormesh(av, bv, integral, shading='auto')
plt.xlabel('$a$')
plt.ylabel('$b$')
plt.colorbar(label='Integral value')
plt.show()
```

### Combining Interpolation with Integration

A powerful pattern is to interpolate discrete data with `scipy.interpolate.interp1d` and then integrate the smooth interpolant:

```python
from scipy.interpolate import interp1d
from scipy.integrate import quad

x = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.662, 0.8, 1., 1.25,
              1.5, 2., 3., 4., 5., 6., 8., 10.])
y = np.array([0., 0.032, 0.06, 0.086, 0.109, 0.131, 0.151, 0.185,
              0.212, 0.238, 0.257, 0.274, 0.256, 0.205, 0.147, 0.096, 0.029, 0.002])

f = interp1d(x, y, 'cubic')
numerator = quad(lambda t: t * f(t), x.min(), x.max())[0]
denominator = quad(f, x.min(), x.max())[0]
mean = numerator / denominator   # Weighted mean ≈ 3.38
```

This technique is directly applicable to computing expected values from empirical probability distributions — a common task in financial mathematics.

### When to Use Each

- **Riemann sums** (earlier sections): Educational, quick vectorized estimates, full control over grid
- **quad**: Single integrals requiring high accuracy, supports infinite bounds and singularities
- **quad_vec**: Batch evaluation of parameterized integrals, orders of magnitude faster than looping `quad`
