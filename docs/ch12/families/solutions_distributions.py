"""
Solutions 02: Continuous and Discrete Distributions
===================================================
Detailed solutions with full explanations.
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("="*80)
print("SOLUTIONS: PROBABILITY DISTRIBUTIONS")
print("="*80)
print()

# Solution 1
print("Solution 1: Exponential Distribution")
print("-" * 40)

mean_time = 5  # minutes
expo_dist = stats.expon(scale=mean_time)

# Part a
prob_within_3 = expo_dist.cdf(3)
print(f"a) P(X ≤ 3) = {prob_within_3:.4f}")
print()

# Part b - Memoryless property
prob_within_2 = expo_dist.cdf(2)
print(f"b) P(X ≤ 6 | X > 4) = P(X ≤ 2) = {prob_within_2:.4f}")
print(f"   This equals P(X ≤ 2) due to memoryless property\n")

# Detailed solutions continue...
print("="*80)
