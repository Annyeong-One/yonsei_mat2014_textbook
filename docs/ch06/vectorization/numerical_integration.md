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

### 1. Higher Accuracy

For production use, prefer `scipy.integrate`.

```python
import numpy as np
from scipy import integrate

def f(x):
    return x ** 3

def main():
    result, error = integrate.quad(f, 0, 1)
    
    print(f"Result: {result:.10f}")
    print(f"Error:  {error:.2e}")

if __name__ == "__main__":
    main()
```

### 2. Adaptive Methods

`scipy.integrate.quad` uses adaptive quadrature for better accuracy.

### 3. When to Use Each

- Simple Riemann: Educational, quick estimates
- scipy.integrate: Production, high accuracy needed
