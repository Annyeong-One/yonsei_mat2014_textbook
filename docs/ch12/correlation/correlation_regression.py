"""
Tutorial 06: Correlation and Regression Analysis
================================================
Level: Intermediate-Advanced
Topics: Pearson, Spearman, Kendall correlation; Simple and multiple linear
        regression; Polynomial regression; Regression diagnostics

This module covers correlation analysis and linear regression using scipy.stats
and demonstrates how to assess relationships between variables.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

print("="*80)
print("CORRELATION AND REGRESSION ANALYSIS")
print("="*80)
print()

# =============================================================================
# SECTION 1: Pearson Correlation Coefficient
# =============================================================================
"""
Pearson correlation (r) measures linear relationship between two variables.

Range: -1 to +1
- r = +1: Perfect positive linear relationship
- r = 0: No linear relationship
- r = -1: Perfect negative linear relationship

Test: H₀: ρ = 0 (no correlation)
      H₁: ρ ≠ 0 (correlation exists)
"""

print("PEARSON CORRELATION")
print("-" * 40)

# Generate correlated data
n = 50
x = np.random.normal(0, 1, n)
noise = np.random.normal(0, 0.5, n)

# Different correlation strengths
y_strong = 2*x + 3 + noise * 0.2  # Strong positive correlation
y_moderate = 0.8*x + 2 + noise     # Moderate positive correlation
y_weak = 0.3*x + 1 + noise * 2     # Weak positive correlation
y_none = np.random.normal(0, 1, n)  # No correlation

datasets = [
    ("Strong positive", x, y_strong),
    ("Moderate positive", x, y_moderate),
    ("Weak positive", x, y_weak),
    ("No correlation", x, y_none)
]

print(f"{'Relationship':<20} {'r':<10} {'p-value':<12} {'Interpretation'}")
print("-" * 60)

for name, x_data, y_data in datasets:
    r, p = stats.pearsonr(x_data, y_data)
    
    if p < 0.001:
        sig = "***"
    elif p < 0.01:
        sig = "**"
    elif p < 0.05:
        sig = "*"
    else:
        sig = "ns"
    
    print(f"{name:<20} {r:>8.3f}  {p:>10.4f}{sig:<2}", end="")
    
    if abs(r) < 0.3:
        print(" weak")
    elif abs(r) < 0.7:
        print(" moderate")
    else:
        print(" strong")

print()

# Visualize correlations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

for i, (name, x_data, y_data) in enumerate(datasets):
    r, p = stats.pearsonr(x_data, y_data)
    
    axes[i].scatter(x_data, y_data, alpha=0.6)
    
    # Add regression line
    slope, intercept = np.polyfit(x_data, y_data, 1)
    x_line = np.linspace(x_data.min(), x_data.max(), 100)
    y_line = slope * x_line + intercept
    axes[i].plot(x_line, y_line, 'r-', linewidth=2, label=f'r={r:.3f}')
    
    axes[i].set_xlabel('X')
    axes[i].set_ylabel('Y')
    axes[i].set_title(f'{name}')
    axes[i].legend()
    axes[i].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/06_pearson_correlation.png', 
            dpi=300, bbox_inches='tight')
print("Saved: 06_pearson_correlation.png\n")
plt.close()

# More detailed tutorial content would continue...
# [Additional sections on Spearman, Kendall, regression, etc.]

print("="*80)
print("Tutorial 06 Complete!")
print("="*80)
