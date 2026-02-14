"""
Solutions 01: Basics of scipy.stats and Probability Distributions
=================================================================
Detailed solutions with explanations for all exercises.
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("="*80)
print("SOLUTIONS: BASICS AND DISTRIBUTIONS")
print("="*80)
print()

# Solution 1: Working with Normal Distribution
print("Solution 1: Normal Distribution")
print("-" * 40)
print("Given: μ=10.0 cm, σ=0.5 cm")
print()

# Create the distribution
normal_dist = stats.norm(loc=10.0, scale=0.5)

# Part a
prob_a = normal_dist.cdf(10.5) - normal_dist.cdf(9.5)
print(f"a) P(9.5 < X < 10.5) = {prob_a:.4f} = {prob_a*100:.2f}%")
print(f"   This is approximately 68% (μ ± σ rule)\n")

# Part b
percentile_95 = normal_dist.ppf(0.95)
print(f"b) 95th percentile = {percentile_95:.4f} cm")
print(f"   95% of parts are below this length\n")

# Part c - Using Central Limit Theorem
# Sample mean distribution: N(μ, σ²/n)
n = 100
mean_dist = stats.norm(loc=10.0, scale=0.5/np.sqrt(n))
prob_c = mean_dist.cdf(10.1) - mean_dist.cdf(9.9)
print(f"c) P(9.9 < X̄ < 10.1) = {prob_c:.4f}")
print(f"   Sample mean has smaller variance: σ/√n = {0.5/np.sqrt(n):.4f}\n")

print()

# Solution 2: Binomial Distribution
print("Solution 2: Binomial Distribution")
print("-" * 40)
print("Given: n=20 questions, p=0.25 (1 in 4 chance)")
print()

# Create the distribution
binom_dist = stats.binom(n=20, p=0.25)

# Part a
expected = binom_dist.mean()
print(f"a) Expected correct answers = np = {expected:.1f}")
print()

# Part b
prob_8 = binom_dist.pmf(8)
print(f"b) P(X = 8) = {prob_8:.4f}")
print()

# Part c
prob_pass = binom_dist.sf(11)  # P(X >= 12) = P(X > 11)
print(f"c) P(X ≥ 12) = {prob_pass:.4f}")
print(f"   Very low probability of passing by guessing!\n")

# Detailed explanation continues...
print("="*80)
