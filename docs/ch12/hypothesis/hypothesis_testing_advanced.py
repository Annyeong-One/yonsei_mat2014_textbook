"""
Tutorial 05: Advanced Hypothesis Testing and Power Analysis
===========================================================
Level: Intermediate-Advanced
Topics: Type I/II errors, power analysis, multiple testing correction,
        effect sizes, confidence intervals, bootstrapping

This module covers advanced concepts in hypothesis testing including
power analysis, multiple comparison corrections, and modern resampling methods.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import bootstrap
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

# =============================================================================
# SECTION 1: Type I and Type II Errors
# =============================================================================
"""
Type I Error (α - False Positive):
- Rejecting H₀ when it's actually true
- "False alarm" - finding an effect that doesn't exist
- Controlled by significance level (typically α = 0.05)

Type II Error (β - False Negative):  
- Failing to reject H₀ when it's actually false
- "Miss" - failing to detect a real effect
- Related to statistical power: Power = 1 - β

Statistical Power:
- Probability of correctly rejecting a false H₀
- Typically aim for power ≥ 0.80 (80%)
- Affected by: sample size, effect size, significance level
"""

print("="*80)
print("TYPE I AND TYPE II ERRORS")
print("="*80)
print()

# Simulation to demonstrate Type I error rate
def simulate_type1_error(n_simulations=10000, alpha=0.05, n_samples=30):
    """
    Simulate Type I errors by testing samples from the same distribution.
    H₀ is true (both samples have same mean), but we may reject it by chance.
    """
    type1_errors = 0
    
    for _ in range(n_simulations):
        # Both samples from same distribution (H₀ is true)
        sample1 = np.random.normal(0, 1, n_samples)
        sample2 = np.random.normal(0, 1, n_samples)
        
        # Perform t-test
        _, p_value = stats.ttest_ind(sample1, sample2)
        
        # Count Type I errors (false positives)
        if p_value < alpha:
            type1_errors += 1
    
    return type1_errors / n_simulations

observed_alpha = simulate_type1_error()
print(f"Type I Error Rate Simulation (n=10,000 tests):")
print(f"  Nominal α = 0.05")
print(f"  Observed error rate = {observed_alpha:.4f}")
print(f"  These should be approximately equal!")
print()

# Simulation to demonstrate Type II error and Power
def simulate_power(effect_size, n_samples=30, n_simulations=10000, alpha=0.05):
    """
    Calculate statistical power by simulation.
    H₀ is false (samples have different means), so rejections are correct.
    """
    correct_rejections = 0
    
    for _ in range(n_simulations):
        # Samples from different distributions (H₀ is false)
        sample1 = np.random.normal(0, 1, n_samples)
        sample2 = np.random.normal(effect_size, 1, n_samples)
        
        # Perform t-test
        _, p_value = stats.ttest_ind(sample1, sample2)
        
        # Count correct rejections (true positives)
        if p_value < alpha:
            correct_rejections += 1
    
    power = correct_rejections / n_simulations
    beta = 1 - power  # Type II error rate
    
    return power, beta

print("Power Analysis Simulation:")
effect_sizes = [0.2, 0.5, 0.8, 1.0]
for effect in effect_sizes:
    power, beta = simulate_power(effect, n_samples=30)
    print(f"  Effect size d={effect:.1f}: Power={power:.3f}, β={beta:.3f}")

print()
print("Interpretation:")
print("  - Small effect (d=0.2): Low power, high chance of missing real effect")
print("  - Medium effect (d=0.5): Moderate power")
print("  - Large effect (d=0.8): Good power, low chance of missing effect")
print()

# =============================================================================
# SECTION 2: Statistical Power Analysis
# =============================================================================
"""
Power analysis answers questions like:
1. Given sample size and effect size, what's the power?
2. Given desired power and effect size, what sample size is needed?
3. Given sample size and power, what effect size can be detected?
"""

print("="*80)
print("POWER ANALYSIS FOR TWO-SAMPLE t-TEST")
print("="*80)
print()

def calculate_power_ttest(effect_size, n_per_group, alpha=0.05):
    """Calculate power for two-sample t-test."""
    # Non-centrality parameter
    ncp = effect_size * np.sqrt(n_per_group / 2)
    
    # Critical value from t-distribution
    df = 2 * n_per_group - 2
    t_critical = stats.t.ppf(1 - alpha/2, df)
    
    # Power = P(|T| > t_critical | H₁ is true)
    # Under H₁, T follows non-central t-distribution
    power = 1 - stats.nct.cdf(t_critical, df, ncp) + stats.nct.cdf(-t_critical, df, ncp)
    
    return power

# Power curves for different sample sizes
effect_sizes = np.linspace(0, 1.5, 50)
sample_sizes = [10, 20, 30, 50, 100]

plt.figure(figsize=(14, 10))

# Plot 1: Power curves vs effect size
plt.subplot(2, 2, 1)
for n in sample_sizes:
    powers = [calculate_power_ttest(d, n) for d in effect_sizes]
    plt.plot(effect_sizes, powers, label=f'n={n}', linewidth=2)

plt.axhline(y=0.80, color='r', linestyle='--', label='80% power', alpha=0.5)
plt.xlabel('Effect Size (Cohen\'s d)')
plt.ylabel('Statistical Power')
plt.title('Power Curves: Effect of Sample Size')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Required sample size for 80% power
plt.subplot(2, 2, 2)
def required_sample_size(effect_size, desired_power=0.80, alpha=0.05, max_n=500):
    """Find minimum sample size to achieve desired power."""
    for n in range(2, max_n):
        power = calculate_power_ttest(effect_size, n, alpha)
        if power >= desired_power:
            return n
    return max_n

effect_range = np.linspace(0.2, 1.5, 50)
required_n = [required_sample_size(d) for d in effect_range]

plt.plot(effect_range, required_n, linewidth=2)
plt.xlabel('Effect Size (Cohen\'s d)')
plt.ylabel('Required Sample Size (per group)')
plt.title('Sample Size Needed for 80% Power')
plt.grid(True, alpha=0.3)

# Plot 3: Power vs sample size for fixed effect
plt.subplot(2, 2, 3)
fixed_effects = [0.2, 0.5, 0.8]
sample_range = np.arange(10, 101, 5)

for effect in fixed_effects:
    powers = [calculate_power_ttest(effect, n) for n in sample_range]
    plt.plot(sample_range, powers, label=f'd={effect}', linewidth=2)

plt.axhline(y=0.80, color='r', linestyle='--', alpha=0.5)
plt.xlabel('Sample Size (per group)')
plt.ylabel('Statistical Power')
plt.title('Power vs Sample Size')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 4: Power vs alpha (significance level)
plt.subplot(2, 2, 4)
alpha_range = np.linspace(0.01, 0.20, 50)
fixed_n = 30
fixed_d = 0.5

powers_vs_alpha = [calculate_power_ttest(fixed_d, fixed_n, a) for a in alpha_range]
plt.plot(alpha_range, powers_vs_alpha, linewidth=2)
plt.axvline(x=0.05, color='r', linestyle='--', label='α=0.05', alpha=0.5)
plt.xlabel('Significance Level (α)')
plt.ylabel('Statistical Power')
plt.title(f'Power vs α (n={fixed_n}, d={fixed_d})')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/05_power_analysis.png', dpi=300, bbox_inches='tight')
print("Saved: 05_power_analysis.png\n")
plt.close()

# Sample size recommendations
print("Sample Size Recommendations for 80% Power:")
print(f"{'Effect Size':<15} {'Description':<15} {'n per group':<15}")
print("-" * 45)
for d, desc in [(0.2, 'Small'), (0.5, 'Medium'), (0.8, 'Large')]:
    n = required_sample_size(d)
    print(f"{d:<15.1f} {desc:<15} {n:<15}")
print()

# =============================================================================
# SECTION 3: Multiple Testing Problem
# =============================================================================
"""
When performing multiple hypothesis tests, the probability of at least
one Type I error increases.

If conducting k independent tests at α=0.05:
P(at least one Type I error) = 1 - (1-α)^k

Example: 20 tests → P(at least one false positive) ≈ 64%!

Solutions:
1. Bonferroni correction: α_new = α / k
2. Holm-Bonferroni: Step-down procedure
3. Benjamini-Hochberg: Control False Discovery Rate (FDR)
4. Sidak correction: α_new = 1 - (1-α)^(1/k)
"""

print("="*80)
print("MULTIPLE TESTING CORRECTIONS")
print("="*80)
print()

# Example: Testing 10 hypotheses
n_tests = 10
p_values = np.array([0.001, 0.008, 0.015, 0.032, 0.045, 
                     0.068, 0.123, 0.234, 0.456, 0.678])

alpha = 0.05

print(f"Testing {n_tests} hypotheses with α={alpha}")
print(f"Observed p-values: {p_values}")
print()

# Without correction
significant_uncorrected = np.sum(p_values < alpha)
print(f"Without correction: {significant_uncorrected} tests significant")
print(f"  (Risk of false positives!)")
print()

# 1. Bonferroni Correction
alpha_bonferroni = alpha / n_tests
significant_bonferroni = np.sum(p_values < alpha_bonferroni)
print(f"Bonferroni correction: α_new = {alpha_bonferroni:.4f}")
print(f"  {significant_bonferroni} tests significant")
print(f"  (Very conservative, low power)")
print()

# 2. Holm-Bonferroni (Step-down)
sorted_indices = np.argsort(p_values)
sorted_p_values = p_values[sorted_indices]
holm_threshold = alpha / (n_tests - np.arange(n_tests))

significant_holm = 0
for i, (p, threshold) in enumerate(zip(sorted_p_values, holm_threshold)):
    if p < threshold:
        significant_holm += 1
    else:
        break  # Stop at first non-significant

print(f"Holm-Bonferroni (step-down):")
print(f"  {significant_holm} tests significant")
print(f"  (Less conservative than Bonferroni)")
print()

# 3. Benjamini-Hochberg (FDR control)
fdr_level = 0.05
bh_threshold = (np.arange(n_tests) + 1) / n_tests * fdr_level

significant_bh = 0
for i in range(n_tests-1, -1, -1):
    if sorted_p_values[i] <= bh_threshold[i]:
        significant_bh = i + 1
        break

print(f"Benjamini-Hochberg (FDR = {fdr_level}):")
print(f"  {significant_bh} tests significant")
print(f"  (Controls False Discovery Rate, more powerful)")
print()

# Visualize corrections
plt.figure(figsize=(12, 6))

x_pos = np.arange(n_tests)
colors = ['red' if p < alpha else 'gray' for p in sorted_p_values]

plt.subplot(1, 2, 1)
plt.bar(x_pos, sorted_p_values, color=colors, alpha=0.7, edgecolor='black')
plt.axhline(y=alpha, color='black', linestyle='-', linewidth=2, label=f'α={alpha} (uncorrected)')
plt.axhline(y=alpha_bonferroni, color='blue', linestyle='--', linewidth=2, label='Bonferroni')
plt.plot(x_pos, holm_threshold, 'g--', linewidth=2, label='Holm-Bonferroni')
plt.plot(x_pos, bh_threshold, 'm--', linewidth=2, label='Benjamini-Hochberg')
plt.xlabel('Test (sorted by p-value)')
plt.ylabel('P-value')
plt.title('Multiple Testing Corrections')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Family-wise error rate vs number of tests
plt.subplot(1, 2, 2)
n_tests_range = np.arange(1, 51)
fwer_uncorrected = 1 - (1 - alpha)**n_tests_range
fwer_bonferroni = np.minimum(n_tests_range * alpha, 1)  # Approximation

plt.plot(n_tests_range, fwer_uncorrected, label='Uncorrected', linewidth=2)
plt.plot(n_tests_range, fwer_bonferroni, label='Bonferroni (approx)', linewidth=2)
plt.axhline(y=alpha, color='red', linestyle='--', label=f'Target α={alpha}', alpha=0.5)
plt.xlabel('Number of Tests')
plt.ylabel('Family-Wise Error Rate')
plt.title('Growth of Type I Error with Multiple Tests')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/05_multiple_testing.png', dpi=300, bbox_inches='tight')
print("Saved: 05_multiple_testing.png\n")
plt.close()

# =============================================================================
# SECTION 4: Effect Sizes
# =============================================================================
"""
Effect size measures the magnitude of a difference or relationship.
Unlike p-values, effect sizes are independent of sample size.

Common effect sizes:
1. Cohen's d: Standardized mean difference
   - d = (μ₁ - μ₂) / σ_pooled
   - Small: 0.2, Medium: 0.5, Large: 0.8

2. Pearson's r: Correlation coefficient
   - Small: 0.1, Medium: 0.3, Large: 0.5

3. η² (eta-squared): Proportion of variance explained (ANOVA)
   - Small: 0.01, Medium: 0.06, Large: 0.14

4. Odds ratio: Ratio of odds (2x2 tables)
   - OR=1: no effect, OR>1: positive association, OR<1: negative association
"""

print("="*80)
print("EFFECT SIZES")
print("="*80)
print()

# Example datasets with different effect sizes
np.random.seed(42)
n = 50

# Small effect (d ≈ 0.2)
group1_small = np.random.normal(0, 1, n)
group2_small = np.random.normal(0.2, 1, n)

# Medium effect (d ≈ 0.5)
group1_medium = np.random.normal(0, 1, n)
group2_medium = np.random.normal(0.5, 1, n)

# Large effect (d ≈ 0.8)
group1_large = np.random.normal(0, 1, n)
group2_large = np.random.normal(0.8, 1, n)

def cohens_d(group1, group2):
    """Calculate Cohen's d effect size."""
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1 + n2 - 2))
    return (np.mean(group2) - np.mean(group1)) / pooled_std

datasets = [
    ("Small effect", group1_small, group2_small),
    ("Medium effect", group1_medium, group2_medium),
    ("Large effect", group1_large, group2_large)
]

print(f"{'Comparison':<20} {'Cohen\'s d':<12} {'p-value':<12} {'Interpretation':<30}")
print("-" * 74)

for name, g1, g2 in datasets:
    d = cohens_d(g1, g2)
    t_stat, p_val = stats.ttest_ind(g1, g2)
    
    if p_val < 0.001:
        sig = "***"
    elif p_val < 0.01:
        sig = "**"
    elif p_val < 0.05:
        sig = "*"
    else:
        sig = "ns"
    
    print(f"{name:<20} {d:>10.3f}  {p_val:>10.4f}{sig:<2}", end="")
    
    if abs(d) < 0.2:
        print("Negligible effect")
    elif abs(d) < 0.5:
        print("Small effect")
    elif abs(d) < 0.8:
        print("Medium effect")
    else:
        print("Large effect")

print()
print("Note: Even small effects can be 'significant' with large samples!")
print("      Effect size indicates practical importance.")
print()

# Visualize effect sizes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, (name, g1, g2) in zip(axes, datasets):
    d = cohens_d(g1, g2)
    
    # Combined data for visualization
    data = [g1, g2]
    positions = [1, 2]
    
    bp = ax.boxplot(data, positions=positions, widths=0.6, patch_artist=True,
                    labels=['Group 1', 'Group 2'])
    bp['boxes'][0].set_facecolor('lightblue')
    bp['boxes'][1].set_facecolor('lightcoral')
    
    ax.set_ylabel('Value')
    ax.set_title(f'{name}\n(d = {d:.2f})')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/05_effect_sizes.png', dpi=300, bbox_inches='tight')
print("Saved: 05_effect_sizes.png\n")
plt.close()

# =============================================================================
# SECTION 5: Confidence Intervals
# =============================================================================
"""
Confidence intervals provide a range of plausible values for a parameter.

95% CI interpretation:
- If we repeated the experiment many times and computed a 95% CI each time,
  approximately 95% of those intervals would contain the true parameter value.
- NOT: "There's a 95% probability the true value is in this interval"
"""

print("="*80)
print("CONFIDENCE INTERVALS")
print("="*80)
print()

# Example: Confidence interval for mean
sample_data = np.random.normal(100, 15, 50)
n = len(sample_data)
mean = np.mean(sample_data)
sem = stats.sem(sample_data)  # Standard error of the mean

confidence_levels = [0.90, 0.95, 0.99]

print(f"Sample: n={n}, mean={mean:.2f}, SEM={sem:.2f}")
print()

for conf_level in confidence_levels:
    alpha = 1 - conf_level
    t_critical = stats.t.ppf(1 - alpha/2, n-1)
    margin_error = t_critical * sem
    ci_lower = mean - margin_error
    ci_upper = mean + margin_error
    
    print(f"{conf_level*100:.0f}% CI: [{ci_lower:.2f}, {ci_upper:.2f}]")
    print(f"  Margin of error: ±{margin_error:.2f}")
    print()

# Visualize CI coverage
def simulate_ci_coverage(true_mean=100, true_std=15, n_samples=50, 
                        n_simulations=100, confidence=0.95):
    """Simulate confidence intervals to demonstrate coverage."""
    alpha = 1 - confidence
    t_crit = stats.t.ppf(1 - alpha/2, n_samples-1)
    
    covers_true_mean = []
    intervals = []
    
    for _ in range(n_simulations):
        sample = np.random.normal(true_mean, true_std, n_samples)
        sample_mean = np.mean(sample)
        sample_sem = stats.sem(sample)
        margin = t_crit * sample_sem
        
        ci_lower = sample_mean - margin
        ci_upper = sample_mean + margin
        
        covers = (ci_lower <= true_mean <= ci_upper)
        covers_true_mean.append(covers)
        intervals.append((ci_lower, ci_upper, sample_mean, covers))
    
    coverage_rate = np.mean(covers_true_mean)
    return coverage_rate, intervals

coverage, intervals = simulate_ci_coverage(n_simulations=100)

print(f"Confidence Interval Coverage Simulation:")
print(f"  Expected coverage: 95%")
print(f"  Observed coverage: {coverage*100:.1f}% (from 100 simulations)")
print()

# Plot first 50 intervals
plt.figure(figsize=(12, 8))

true_mean = 100
n_to_plot = 50

for i, (lower, upper, mean, covers) in enumerate(intervals[:n_to_plot]):
    color = 'green' if covers else 'red'
    alpha_val = 0.7 if covers else 1.0
    plt.plot([lower, upper], [i, i], color=color, alpha=alpha_val, linewidth=2)
    plt.plot(mean, i, 'o', color=color, markersize=4)

plt.axvline(true_mean, color='blue', linestyle='--', linewidth=2, label='True mean')
plt.xlabel('Value')
plt.ylabel('Simulation Number')
plt.title(f'95% Confidence Intervals from {n_to_plot} Simulations\n'
          f'Green: Contains true mean, Red: Misses true mean')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/05_confidence_intervals.png', dpi=300, bbox_inches='tight')
print("Saved: 05_confidence_intervals.png\n")
plt.close()

# =============================================================================
# SECTION 6: Bootstrapping
# =============================================================================
"""
Bootstrap: Resampling method to estimate sampling distribution.

Procedure:
1. Resample data with replacement (many times)
2. Calculate statistic for each resample
3. Use distribution of statistics to estimate:
   - Standard error
   - Confidence intervals
   - Hypothesis tests

Advantages:
- Works for any statistic (mean, median, correlation, etc.)
- No distributional assumptions needed
- Provides empirical confidence intervals
"""

print("="*80)
print("BOOTSTRAP RESAMPLING")
print("="*80)
print()

# Example: Bootstrap confidence interval for median
data = stats.gamma.rvs(2, size=50)  # Skewed data

print(f"Original data: n={len(data)}")
print(f"  Mean: {np.mean(data):.3f}")
print(f"  Median: {np.median(data):.3f}")
print(f"  Std: {np.std(data, ddof=1):.3f}")
print()

# Bootstrap using scipy
rng = np.random.default_rng(42)
res = bootstrap((data,), np.median, n_resamples=10000, random_state=rng)

print(f"Bootstrap results for median (10,000 resamples):")
print(f"  Bootstrap standard error: {res.standard_error:.3f}")
print(f"  95% CI: [{res.confidence_interval.low:.3f}, {res.confidence_interval.high:.3f}]")
print()

# Manual bootstrap for demonstration
def manual_bootstrap(data, statistic_func, n_bootstrap=10000):
    """Perform bootstrap resampling manually."""
    n = len(data)
    bootstrap_stats = []
    
    for _ in range(n_bootstrap):
        # Resample with replacement
        resample = np.random.choice(data, size=n, replace=True)
        # Calculate statistic
        stat = statistic_func(resample)
        bootstrap_stats.append(stat)
    
    return np.array(bootstrap_stats)

# Bootstrap for various statistics
bootstrap_means = manual_bootstrap(data, np.mean, 10000)
bootstrap_medians = manual_bootstrap(data, np.median, 10000)
bootstrap_stds = manual_bootstrap(data, lambda x: np.std(x, ddof=1), 10000)

# Visualize bootstrap distributions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original data distribution
axes[0, 0].hist(data, bins=15, edgecolor='black', alpha=0.7)
axes[0, 0].axvline(np.mean(data), color='red', linestyle='--', linewidth=2, label='Mean')
axes[0, 0].axvline(np.median(data), color='blue', linestyle='--', linewidth=2, label='Median')
axes[0, 0].set_xlabel('Value')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Original Data Distribution')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Bootstrap distribution of mean
axes[0, 1].hist(bootstrap_means, bins=50, edgecolor='black', alpha=0.7)
axes[0, 1].axvline(np.mean(data), color='red', linestyle='--', linewidth=2, label='Observed mean')
ci_mean = np.percentile(bootstrap_means, [2.5, 97.5])
axes[0, 1].axvline(ci_mean[0], color='green', linestyle=':', linewidth=2)
axes[0, 1].axvline(ci_mean[1], color='green', linestyle=':', linewidth=2, label='95% CI')
axes[0, 1].set_xlabel('Mean')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Bootstrap Distribution of Mean')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Bootstrap distribution of median
axes[1, 0].hist(bootstrap_medians, bins=50, edgecolor='black', alpha=0.7)
axes[1, 0].axvline(np.median(data), color='blue', linestyle='--', linewidth=2, label='Observed median')
ci_median = np.percentile(bootstrap_medians, [2.5, 97.5])
axes[1, 0].axvline(ci_median[0], color='green', linestyle=':', linewidth=2)
axes[1, 0].axvline(ci_median[1], color='green', linestyle=':', linewidth=2, label='95% CI')
axes[1, 0].set_xlabel('Median')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Bootstrap Distribution of Median')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Bootstrap distribution of standard deviation
axes[1, 1].hist(bootstrap_stds, bins=50, edgecolor='black', alpha=0.7)
axes[1, 1].axvline(np.std(data, ddof=1), color='purple', linestyle='--', linewidth=2, label='Observed std')
ci_std = np.percentile(bootstrap_stds, [2.5, 97.5])
axes[1, 1].axvline(ci_std[0], color='green', linestyle=':', linewidth=2)
axes[1, 1].axvline(ci_std[1], color='green', linestyle=':', linewidth=2, label='95% CI')
axes[1, 1].set_xlabel('Standard Deviation')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Bootstrap Distribution of Std Dev')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/claude/scipy_stats_course/05_bootstrap.png', dpi=300, bbox_inches='tight')
print("Saved: 05_bootstrap.png\n")
plt.close()

print("Bootstrap 95% Confidence Intervals:")
print(f"  Mean: [{np.percentile(bootstrap_means, 2.5):.3f}, {np.percentile(bootstrap_means, 97.5):.3f}]")
print(f"  Median: [{np.percentile(bootstrap_medians, 2.5):.3f}, {np.percentile(bootstrap_medians, 97.5):.3f}]")
print(f"  Std Dev: [{np.percentile(bootstrap_stds, 2.5):.3f}, {np.percentile(bootstrap_stds, 97.5):.3f}]")
print()

# =============================================================================
# SECTION 7: Summary
# =============================================================================

print("="*80)
print("Tutorial 05 Complete!")
print("="*80)
print("\nKey Takeaways:")
print("1. Statistical power (1-β) is probability of detecting true effect")
print("2. Larger samples, larger effects, and higher α increase power")
print("3. Multiple testing inflates Type I error - use corrections")
print("4. Effect sizes measure practical significance, independent of sample size")
print("5. Confidence intervals quantify uncertainty in estimates")
print("6. Bootstrap provides empirical confidence intervals without assumptions")
print("7. Report both statistical significance (p-value) and effect size")
print("8. Power analysis should be conducted before data collection")
