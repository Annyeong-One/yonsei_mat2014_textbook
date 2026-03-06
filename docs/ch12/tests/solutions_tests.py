"""
Solutions 03: Statistical Hypothesis Tests
==========================================
Detailed solutions with interpretations.
"""

import numpy as np
from scipy import stats

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*80)
    print("SOLUTIONS: STATISTICAL TESTS")
    print("="*80)
    print()

    # Solution 1
    print("Solution 1: Comparing Two Teaching Methods")
    print("-" * 40)

    method_A = np.array([78, 82, 75, 88, 72, 90, 85, 77, 83, 79])
    method_B = np.array([85, 88, 91, 84, 89, 92, 87, 90, 86, 93])

    print("Step 1: State hypotheses")
    print("  H₀: μ_A = μ_B (no difference)")
    print("  H₁: μ_A ≠ μ_B (significant difference)\n")

    # Part a: t-test
    t_stat, p_value = stats.ttest_ind(method_A, method_B)
    print(f"a) Two-sample t-test:")
    print(f"   t-statistic = {t_stat:.4f}")
    print(f"   p-value = {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print(f"   Decision: Reject H₀ (p < {alpha})")
        print(f"   Conclusion: Method B produces significantly higher scores\n")
    else:
        print(f"   Decision: Fail to reject H₀\n")

    # Part b: Effect size
    mean_diff = np.mean(method_B) - np.mean(method_A)
    pooled_std = np.sqrt(((len(method_A)-1)*np.var(method_A, ddof=1) +
                          (len(method_B)-1)*np.var(method_B, ddof=1)) /
                         (len(method_A) + len(method_B) - 2))
    cohens_d = mean_diff / pooled_std

    print(f"b) Cohen\'s d = {cohens_d:.4f}")
    if abs(cohens_d) > 0.8:
        print(f"   Interpretation: Large effect size\n")

    # Part c: Confidence interval
    se_diff = pooled_std * np.sqrt(1/len(method_A) + 1/len(method_B))
    df = len(method_A) + len(method_B) - 2
    t_critical = stats.t.ppf(0.975, df)
    margin = t_critical * se_diff

    print(f"c) 95% CI for difference: [{mean_diff - margin:.2f}, {mean_diff + margin:.2f}]")
    print(f"   We are 95% confident the true difference is in this range\n")

    # Detailed solutions continue...
    print("="*80)
