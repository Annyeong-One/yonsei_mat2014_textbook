"""
scipy.integrate Tutorial: quad and quad_vec
============================================
Level: Beginner-Intermediate
Topics: Numerical integration, adaptive quadrature, infinite domains,
        parameterized integrals, vectorized batch integration

This module provides a comprehensive tutorial on scipy.integrate.quad
and scipy.integrate.quad_vec for numerical integration in Python.
"""

import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import quad, quad_vec

# =============================================================================
# SECTION 1: Basic quad Usage
# =============================================================================
"""
scipy.integrate.quad computes a definite integral using adaptive
Gauss-Kronrod quadrature. It returns (result, error_estimate).
"""

print("=" * 70)
print("SECTION 1: Basic quad Usage")
print("=" * 70)


def f(x):
    """Standard normal PDF (unnormalized by convention here)."""
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)


# Integrate the standard normal PDF from -3 to 3
result, error = quad(f, -3, 3)
print(f"∫ N(0,1) from -3 to 3:")
print(f"  Result: {result:.10f}")
print(f"  Error:  {error:.2e}")
print()

# =============================================================================
# SECTION 2: Infinite Integration Domains
# =============================================================================

print("=" * 70)
print("SECTION 2: Infinite Integration Domains")
print("=" * 70)

result, error = quad(f, -np.inf, np.inf)
print(f"∫ N(0,1) from -∞ to ∞:")
print(f"  Result: {result:.10f}")
print(f"  Error:  {error:.2e}")
print()

# =============================================================================
# SECTION 3: Functions with Extra Parameters
# =============================================================================

print("=" * 70)
print("SECTION 3: Extra Parameters via args")
print("=" * 70)


def f_params(x, mu, sigma):
    """General normal PDF with parameters."""
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / np.sqrt(2 * np.pi * sigma**2)


mu, sigma = 3, 2
result, error = quad(f_params, -np.inf, np.inf, args=(mu, sigma))
print(f"∫ N({mu},{sigma}) from -∞ to ∞:")
print(f"  Result: {result:.10f}")
print(f"  Error:  {error:.2e}")
print()

# =============================================================================
# SECTION 4: Controlling Precision for Speed
# =============================================================================

print("=" * 70)
print("SECTION 4: Precision vs Speed Trade-off")
print("=" * 70)

n = 10_000

t1 = time.perf_counter()
[quad(f_params, -np.inf, np.inf, args=(mu, sigma)) for _ in range(n)]
t2 = time.perf_counter()
print(f"Default precision ({n} integrals): {t2 - t1:.2f} sec")

t1 = time.perf_counter()
[quad(f_params, -np.inf, np.inf, args=(mu, sigma), epsabs=1e-4) for _ in range(n)]
t2 = time.perf_counter()
print(f"Reduced precision ({n} integrals): {t2 - t1:.2f} sec")
print()

# =============================================================================
# SECTION 5: Difficult Integrands — points Parameter
# =============================================================================

print("=" * 70)
print("SECTION 5: Guiding quad with points")
print("=" * 70)


def f_peaks(x):
    """Function with two sharp peaks far from the origin."""
    return np.exp(-(x - 700)**2) + np.exp(-(x + 700)**2)


# Without guidance — quad may miss the peaks entirely
result_naive, _ = quad(f_peaks, -np.inf, np.inf)
print(f"Without points: {result_naive:.10f}")

# With guidance — cannot use infinite bounds with points
result_guided, _ = quad(f_peaks, -800, 800, points=[-700, 700])
print(f"With points:    {result_guided:.10f}")
print(f"Exact (2√π):    {2 * np.sqrt(np.pi):.10f}")
print()

# =============================================================================
# SECTION 6: quad_vec — Vectorized Batch Integration
# =============================================================================

print("=" * 70)
print("SECTION 6: quad_vec — Massive Speedup")
print("=" * 70)


def f_alpha(x, alpha):
    """Gaussian with variable width parameter."""
    return np.exp(-alpha * x**2)


n_params = 10_000
alphas = np.linspace(1, 2, n_params)

# Method 1: Loop with quad (slow)
t1 = time.perf_counter()
results_loop = [quad(f_alpha, -1, 3, args=(a,)) for a in alphas]
t2 = time.perf_counter()
time_loop = t2 - t1
mean_loop = np.array([v for v, e in results_loop]).mean()
print(f"quad loop ({n_params} integrals):     {time_loop:.3f} sec, mean={mean_loop:.10f}")

# Method 2: quad_vec (fast)
t1 = time.perf_counter()
result_vec, error_vec = quad_vec(f_alpha, -1, 3, args=(alphas,))
t2 = time.perf_counter()
time_vec = t2 - t1
mean_vec = result_vec.mean()
print(f"quad_vec ({n_params} integrals):      {time_vec:.3f} sec, mean={mean_vec:.10f}")
print(f"Speedup: {time_loop / time_vec:.0f}x")
print()

# =============================================================================
# SECTION 7: quad_vec with Two Parameters
# =============================================================================

print("=" * 70)
print("SECTION 7: quad_vec with Parameter Grid")
print("=" * 70)


def f_ab(x, a, b):
    """Gaussian with variable width and center."""
    return np.exp(-a * (x - b)**2)


a = np.arange(1, 20, 1)
b = np.linspace(0, 5, 100)
av, bv = np.meshgrid(a, b)

integral_grid = quad_vec(f_ab, -1, 3, args=(av, bv))[0]
print(f"Computed {integral_grid.size} integrals in a single call")
print(f"Result shape: {integral_grid.shape}")

plt.figure(figsize=(8, 4))
plt.pcolormesh(av, bv, integral_grid, shading='auto')
plt.xlabel('$a$ (width parameter)')
plt.ylabel('$b$ (center parameter)')
plt.colorbar(label='Integral value')
plt.title(r'$\int_{-1}^{3} e^{-a(x-b)^2} dx$ over parameter grid')
plt.tight_layout()
plt.show()

# =============================================================================
# SECTION 8: quad_vec with Variable Integration Domains
# =============================================================================

print("=" * 70)
print("SECTION 8: Variable Domains via Indicator Functions")
print("=" * 70)


def f_variable_domain(x, a):
    """Use indicator function to implement variable bounds [-a, a]."""
    return (x >= -a) * (x <= a) * np.exp(-a * x**2)


a_vals = np.arange(1, 20, 1)
integral_variable = quad_vec(f_variable_domain, -np.inf, np.inf, args=(a_vals,))[0]

plt.figure(figsize=(8, 4))
plt.plot(a_vals, integral_variable, '--*')
plt.xlabel('$a$')
plt.ylabel('Integral value')
plt.title(r'$\int_{-a}^{a} e^{-ax^2} dx$ for various $a$')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print()
print("=" * 70)
print("Tutorial Complete!")
print("=" * 70)
print("\nKey Takeaways:")
print("1. quad: single integrals with adaptive quadrature")
print("2. Use args=(...) for parameterized integrands")
print("3. Use epsabs to trade accuracy for speed")
print("4. Use points=[...] for difficult integrands with sharp peaks")
print("5. quad_vec: batch integrals 100x+ faster than looping quad")
print("6. Use meshgrid for multi-parameter grids with quad_vec")
