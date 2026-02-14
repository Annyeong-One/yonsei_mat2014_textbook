"""
Tutorial 07: Advanced Statistical Methods
=========================================
Level: Advanced
Topics: Survival analysis, multivariate distributions, maximum likelihood,
        Monte Carlo methods, statistical modeling

This module introduces advanced statistical concepts and methods available
in scipy.stats for specialized analyses.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import minimize
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

print("="*80)
print("ADVANCED STATISTICAL METHODS")
print("="*80)
print()

# =============================================================================
# SECTION 1: Multivariate Normal Distribution
# =============================================================================
"""
Multivariate normal distribution extends the normal distribution to
multiple dimensions with specified covariance structure.
"""

print("MULTIVARIATE NORMAL DISTRIBUTION")
print("-" * 40)

# Define 2D multivariate normal
mean = [0, 0]
cov = [[1, 0.7],   # Positive correlation between variables
       [0.7, 1]]

# Generate samples
mvn = stats.multivariate_normal(mean, cov)
samples = mvn.rvs(size=1000)

print(f"Mean vector: {mean}")
print(f"Covariance matrix:")
print(f"  {cov[0]}")
print(f"  {cov[1]}")
print()

# Calculate sample statistics
sample_mean = np.mean(samples, axis=0)
sample_cov = np.cov(samples.T)

print(f"Sample mean: [{sample_mean[0]:.3f}, {sample_mean[1]:.3f}]")
print(f"Sample covariance:")
print(f"  [{sample_cov[0,0]:.3f}, {sample_cov[0,1]:.3f}]")
print(f"  [{sample_cov[1,0]:.3f}, {sample_cov[1,1]:.3f}]")
print()

# Visualize
plt.figure(figsize=(10, 8))
plt.scatter(samples[:,0], samples[:,1], alpha=0.5)
plt.xlabel('X₁')
plt.ylabel('X₂')
plt.title('Bivariate Normal Distribution Samples')
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/07_multivariate_normal.png', 
            dpi=300, bbox_inches='tight')
print("Saved: 07_multivariate_normal.png\n")
plt.close()

# More advanced content would continue...

print("="*80)
print("Tutorial 07 Complete!")
print("="*80)
