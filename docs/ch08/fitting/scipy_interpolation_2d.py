"""
2D Surface Interpolation with scipy.interpolate
================================================
Level: Intermediate
Topics: interp2d, 3D surface plots, grid interpolation,
        meshgrid, surface visualization

This module demonstrates 2D interpolation for constructing smooth
surfaces from scattered data points — applicable to volatility
surfaces and yield curve grids in financial mathematics.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

# =============================================================================
# SECTION 1: Create Sample Data on a Regular Grid
# =============================================================================
"""
In practice, market data often comes on a discrete grid:
- Options: strike prices × maturities
- Bonds: tenors × dates
- Rates: maturities × currencies

Here we use z = x² + y² as a known function to verify interpolation.
"""

# 5×5 grid of known data points
x = np.array([0., 0.25, 0.5, 0.75, 1.,
              0., 0.25, 0.5, 0.75, 1.,
              0., 0.25, 0.5, 0.75, 1.,
              0., 0.25, 0.5, 0.75, 1.,
              0., 0.25, 0.5, 0.75, 1.])

y = np.array([0., 0., 0., 0., 0.,
              0.25, 0.25, 0.25, 0.25, 0.25,
              0.5, 0.5, 0.5, 0.5, 0.5,
              0.75, 0.75, 0.75, 0.75, 0.75,
              1., 1., 1., 1., 1.])

z = np.array([0., 0.0625, 0.25, 0.5625, 1.,
              0.0625, 0.125, 0.3125, 0.625, 1.0625,
              0.25, 0.3125, 0.5, 0.8125, 1.25,
              0.5625, 0.625, 0.8125, 1.125, 1.5625,
              1., 1.0625, 1.25, 1.5625, 2.])

print("=" * 60)
print("2D Surface Interpolation")
print("=" * 60)
print(f"Data points: {len(x)}")
print(f"Grid: 5×5 = 25 points")
print()

# =============================================================================
# SECTION 2: Build the Interpolant
# =============================================================================

f = interp2d(x, y, z, kind='cubic')

# =============================================================================
# SECTION 3: Evaluate on Fine Grid
# =============================================================================

x_fine = np.linspace(0, 1, 100)
y_fine = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x_fine, y_fine)
Z = f(x_fine, y_fine)  # Returns (100, 100) array

print(f"Fine grid: {Z.shape[0]}×{Z.shape[1]} = {Z.size} points")
print(f"Interpolation range: x=[{x_fine.min():.1f}, {x_fine.max():.1f}], "
      f"y=[{y_fine.min():.1f}, {y_fine.max():.1f}]")
print()

# =============================================================================
# SECTION 4: Verify Against Known Function
# =============================================================================

Z_exact = X**2 + Y**2
max_error = np.max(np.abs(Z - Z_exact))
print(f"Maximum interpolation error: {max_error:.6e}")
print()

# =============================================================================
# SECTION 5: 3D Visualization
# =============================================================================

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': '3d'})

# Interpolated surface
ax.plot_surface(X, Y, Z, alpha=0.8, cmap='viridis')

# Original data points
for xx, yy, zz in zip(x, y, z):
    ax.plot(xx, yy, zz, 'or', markersize=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('2D Cubic Interpolation: Surface from 25 Data Points')
plt.tight_layout()
plt.show()

# =============================================================================
# SECTION 6: Financial Application — Volatility Surface
# =============================================================================
"""
In practice, a volatility surface is constructed from
implied volatilities at discrete (strike, maturity) pairs.
The interp2d function fills in the gaps, producing a smooth
surface that can be queried at any (strike, maturity) combination.

Example: If we have implied vols at strikes [90, 95, 100, 105, 110]
and maturities [1M, 3M, 6M, 1Y], interp2d gives us vols at
any intermediate strike and maturity.
"""

print("=" * 60)
print("Application: Volatility Surface (Simulated)")
print("=" * 60)

# Simulated implied volatility data
strikes = np.array([90, 95, 100, 105, 110])
maturities = np.array([0.083, 0.25, 0.5, 1.0])  # In years

# Simulated smile: higher vol at extremes, lower at ATM
S, M = np.meshgrid(strikes, maturities)
vol_data = 0.20 + 0.001 * (S - 100)**2 + 0.05 / np.sqrt(M)

# Build interpolant
vol_surface = interp2d(S.ravel(), M.ravel(), vol_data.ravel(), kind='cubic')

# Query at non-grid points
strike_query = 97.5
maturity_query = 0.375
vol_interp = vol_surface(strike_query, maturity_query)[0]
print(f"Implied vol at K={strike_query}, T={maturity_query}Y: {vol_interp:.4f}")

print("\nDone!")
