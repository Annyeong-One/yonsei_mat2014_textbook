# Optimization Methods

SciPy's `minimize()` function supports numerous optimization algorithms. Each has different strengths, weaknesses, and computational costs. Understanding these differences is crucial for solving optimization problems efficiently.

---

## Gradient-Free Methods

These methods do not require gradient information and often work well on noisy or non-smooth functions.

### Nelder-Mead Simplex Method

The Nelder-Mead method maintains a simplex (a geometric shape in $n$-dimensional space) and iteratively moves away from the worst point.

**Characteristics:**
- No gradient required
- Works reasonably well in low dimensions (< 10)
- Slower convergence than gradient-based methods
- Robust to noise and non-smoothness
- Default method in older SciPy versions

```python
from scipy import optimize
import numpy as np

def noisy_function(x):
    """Function with some noise."""
    return (x[0] - 2)**2 + (x[1] - 3)**2 + 0.01 * np.random.randn()

# Nelder-Mead
result = optimize.minimize(
    noisy_function,
    x0=[0, 0],
    method='Nelder-Mead',
    options={'maxiter': 5000}
)

print(f"Nelder-Mead result: {result.x}")
print(f"Iterations: {result.nit}")
print(f"Function evaluations: {result.nfev}")
```

**When to use:**
- Noisy objective functions
- Non-smooth functions
- Low-dimensional problems
- When you have no gradient information

### Powell's Method

Powell's method uses conjugate direction methods and performs line searches along successive dimensions.

**Characteristics:**
- No gradient required
- Good for smooth functions
- Often faster than Nelder-Mead
- Works well for dimension < 100
- Can be sensitive to poor starting points

```python
from scipy import optimize

def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

# Powell's method
result = optimize.minimize(
    rosenbrock,
    x0=[0, 0],
    method='Powell'
)

print(f"Powell result: {result.x}")
print(f"Function value: {result.fun:.2e}")
print(f"Iterations: {result.nit}")
print(f"Function evaluations: {result.nfev}")
```

**When to use:**
- Smooth but gradient-free optimization
- Medium dimensions
- Image registration and alignment
- When you need good speed without gradient computation

---

## Gradient-Based Methods

These methods use the gradient (first derivative) to guide the search. They're usually faster but require either analytical gradients or numerical gradient estimation.

### Gradient Descent (Steepest Descent)

The simplest gradient-based method: move in the direction opposite to the gradient.

**Characteristics:**
- Slow convergence
- Requires gradient
- Simple to understand
- Not typically recommended (BFGS is usually better)

```python
from scipy.optimize import minimize
import numpy as np

def quadratic(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

def quadratic_grad(x):
    return np.array([2*(x[0] - 2), 2*(x[1] - 3)])

# Gradient descent
result = minimize(
    quadratic,
    x0=[0, 0],
    method='BFGS',  # Default is BFGS, not pure gradient descent
    jac=quadratic_grad
)

print(f"Result: {result.x}")
```

### BFGS (Broyden-Fletcher-Goldfarb-Shanno)

BFGS is a quasi-Newton method that approximates the inverse Hessian (second derivatives).

**Characteristics:**
- Uses first-order derivatives (gradients)
- Excellent convergence for smooth problems
- Efficient: requires only gradients, not Hessians
- Default method for unconstrained optimization
- Robust and widely used
- Requires storing an $n \times n$ matrix (memory for large $n$)

```python
from scipy import optimize
import numpy as np

def quadratic(x):
    return (x[0] - 2)**2 + 3*(x[1] - 3)**2

def quadratic_grad(x):
    return np.array([2*(x[0] - 2), 6*(x[1] - 3)])

# With gradient
result = optimize.minimize(
    quadratic,
    x0=[0, 0],
    method='BFGS',
    jac=quadratic_grad
)

print(f"BFGS with gradient: {result.x}")
print(f"Iterations: {result.nit}")
print(f"Function evaluations: {result.nfev}")

# Without gradient (finite differences)
result2 = optimize.minimize(
    quadratic,
    x0=[0, 0],
    method='BFGS'
)

print(f"BFGS with finite differences: {result2.x}")
print(f"Function evaluations: {result2.nfev}")
```

**When to use:**
- Smooth, continuous objective functions
- When gradient is available or easily computed
- Medium to large-scale problems
- Generally the first choice for unconstrained optimization

### L-BFGS-B (Limited Memory BFGS with Bounds)

L-BFGS-B is BFGS with limited memory (useful for large problems) and built-in bounds support.

**Characteristics:**
- Limited memory version of BFGS (uses $\mathcal{O}(m \times n)$ memory instead of $\mathcal{O}(n^2)$)
- Handles bounds naturally
- Good for large-scale problems
- Can handle inequality constraints via bounds
- Typically requires about 5-10 previous iterations to approximate Hessian

```python
from scipy import optimize
import numpy as np

def f(x):
    return np.sum((x - np.arange(1, len(x) + 1))**2)

def grad_f(x):
    return 2 * (x - np.arange(1, len(x) + 1))

# Large problem
x0 = np.zeros(1000)

# L-BFGS-B is much more efficient than BFGS for this
result = optimize.minimize(
    f,
    x0,
    method='L-BFGS-B',
    jac=grad_f,
    bounds=[(0, None)] * 1000  # All parameters >= 0
)

print(f"Optimal value: {result.fun:.2e}")
print(f"Iterations: {result.nit}")
```

**When to use:**
- Large-scale problems (thousands of variables)
- When you need to constrain parameters to ranges
- Limited memory available
- Problems where BFGS runs out of memory

### Conjugate Gradient (CG)

CG uses conjugate directions to achieve faster convergence than steepest descent.

**Characteristics:**
- Requires gradient
- Good for large sparse problems
- Converges in $n$ iterations for quadratic functions
- Sensitive to numerical accuracy
- Memory efficient

```python
from scipy import optimize
import numpy as np

def quadratic(x):
    A = np.array([[10, 1], [1, 10]])
    return 0.5 * x @ A @ x

def quadratic_grad(x):
    A = np.array([[10, 1], [1, 10]])
    return A @ x

result = optimize.minimize(
    quadratic,
    x0=[1, 1],
    method='CG',
    jac=quadratic_grad
)

print(f"CG result: {result.x}")
print(f"Iterations: {result.nit}")
```

**When to use:**
- Very large-scale smooth problems
- When memory is limited
- Problems with sparse structure
- Quadratic or nearly quadratic functions

---

## Comparison of Methods

### Performance on Rosenbrock Function

```python
import numpy as np
from scipy import optimize
import time

def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def rosenbrock_grad(x):
    dfdx0 = 2*(x[0] - 1) + 100*2*(x[1] - x[0]**2)*(-2*x[0])
    dfdx1 = 100*2*(x[1] - x[0]**2)
    return np.array([dfdx0, dfdx1])

methods = ['Nelder-Mead', 'Powell', 'BFGS', 'L-BFGS-B', 'CG']
results_dict = {}

for method in methods:
    if method in ['BFGS', 'CG']:
        result = optimize.minimize(
            rosenbrock,
            [0, 0],
            method=method,
            jac=rosenbrock_grad
        )
    else:
        result = optimize.minimize(
            rosenbrock,
            [0, 0],
            method=method
        )

    results_dict[method] = {
        'x': result.x,
        'fun': result.fun,
        'nit': result.nit,
        'nfev': result.nfev
    }

print("Method Comparison on Rosenbrock Function")
print("=" * 70)
print(f"{'Method':<15} {'Function Value':<20} {'Iterations':<15} {'F-evals':<10}")
print("-" * 70)
for method, res in results_dict.items():
    print(f"{method:<15} {res['fun']:.2e}           {res['nit']:<15} {res['nfev']:<10}")
```

### Summary Table

| Method | Gradient | Bounds | Memory | Speed | Robustness |
|:-------|:--------:|:------:|:------:|:-----:|:----------:|
| Nelder-Mead | No | No | Low | Slow | High |
| Powell | No | No | Low | Medium | High |
| BFGS | Yes | No | $O(n^2)$ | Fast | High |
| L-BFGS-B | Yes | Yes | $O(mn)$ | Fast | High |
| CG | Yes | No | Low | Fast | Medium |

---

## Choosing a Method

### Decision Tree

```
Do you have gradient information?
├─ NO
│  ├─ Low dimensional (< 10)?
│  │  └─ Use: Nelder-Mead or Powell
│  └─ Higher dimensional?
│     └─ Use: Powell or differential_evolution
│
├─ YES
│  ├─ Need bounds?
│  │  └─ Use: L-BFGS-B
│  │
│  ├─ Very large problem (n > 10,000)?
│  │  └─ Use: CG or L-BFGS-B
│  │
│  └─ Medium problem, want best speed?
│     └─ Use: BFGS or L-BFGS-B
```

### Practical Recommendations

```python
from scipy import optimize
import numpy as np

# Example: Your optimization problem
def objective(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Decision 1: Do you have a gradient function?
has_gradient = False

# Decision 2: Do you need bounds on parameters?
needs_bounds = True
bounds = [(0, 5), (0, 5)]

# Decision 3: Dimension and problem size?
dimension = 2
large_scale = False

# Choice of method
if needs_bounds:
    method = 'L-BFGS-B'
elif large_scale:
    method = 'CG'
elif has_gradient:
    method = 'BFGS'
else:
    method = 'Powell'

result = optimize.minimize(
    objective,
    x0=[0, 0],
    method=method,
    bounds=bounds if needs_bounds else None
)

print(f"Using method: {method}")
print(f"Result: {result.x}")
```

---

## Providing Gradients

Providing analytical gradients can significantly speed up optimization:

```python
from scipy import optimize
import numpy as np
import time

def f(x):
    return np.sum(np.sin(x) * np.exp(-x**2))

def grad_f(x):
    return (np.cos(x) * np.exp(-x**2) -
            2*x * np.sin(x) * np.exp(-x**2))

x0 = np.array([1.0, 2.0, 3.0])

# With gradient
t1 = time.time()
result1 = optimize.minimize(f, x0, method='BFGS', jac=grad_f)
time1 = time.time() - t1

# Without gradient (finite differences)
t2 = time.time()
result2 = optimize.minimize(f, x0, method='BFGS')
time2 = time.time() - t2

print(f"With analytical gradient:")
print(f"  Time: {time1:.4f}s")
print(f"  Function evals: {result1.nfev}")
print(f"\nWith finite differences:")
print(f"  Time: {time2:.4f}s")
print(f"  Function evals: {result2.nfev}")
print(f"\nSpeedup: {time2/time1:.1f}x")
```

---

## Advanced: Hessian Information

Some methods can use second-order derivatives (Hessian matrix):

```python
from scipy import optimize
import numpy as np

def f(x):
    return x[0]**2 + 2*x[1]**2

def grad_f(x):
    return np.array([2*x[0], 4*x[1]])

def hess_f(x):
    """Hessian matrix."""
    return np.array([[2, 0],
                     [0, 4]])

# Newton-CG method uses Hessian
result = optimize.minimize(
    f,
    x0=[1, 1],
    method='Newton-CG',
    jac=grad_f,
    hess=hess_f
)

print(f"Result: {result.x}")
print(f"Iterations: {result.nit}")
```

---

## Summary

**Key Points:**

1. **Gradient-free methods** (Nelder-Mead, Powell) work on any function but are slower
2. **Gradient-based methods** (BFGS, L-BFGS-B) are faster but require smooth functions
3. **L-BFGS-B** is usually the best choice for constrained problems
4. **CG** is memory-efficient for very large problems
5. Providing analytical gradients can significantly improve speed
6. Choose based on: gradient availability, problem scale, constraints, and desired accuracy

The next section addresses the critical issue of local minima and strategies to find global optima.
