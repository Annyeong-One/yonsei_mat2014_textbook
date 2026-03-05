"""
Three Ways: Pure Python vs NumPy vs Pandas for Data Analysis

This tutorial solves the same sales data analysis problem three ways,
showing why NumPy and Pandas exist and how they simplify data work.

Problem: Analyze monthly sales data across 5 regions.
Tasks:
1. Monthly total sales
2. Month-over-month growth rate
3. Annual sales by region (sorted)
4. Find peak sales (month + region)
5. Find most volatile region (variance)

Based on Python-100-Days Day66-80 day01.ipynb cells.
"""

import numpy as np
import pandas as pd


# =============================================================================
# Setup: Sales Data (12 months x 5 regions, in millions)
# =============================================================================

months = [f'{i:>2d}' for i in range(1, 13)]
regions = ['East', 'West', 'North', 'South', 'Central']
sales_data = [
    [32, 17, 12, 20, 28],
    [41, 30, 17, 15, 35],
    [35, 18, 13, 11, 24],
    [12, 42, 44, 21, 34],
    [29, 11, 42, 32, 50],
    [10, 15, 11, 12, 26],
    [16, 28, 48, 22, 28],
    [31, 40, 45, 30, 39],
    [25, 41, 47, 42, 47],
    [47, 21, 13, 49, 48],
    [41, 36, 17, 36, 22],
    [22, 25, 15, 20, 37],
]


# =============================================================================
# Way 1: Pure Python (loops and comprehensions)
# =============================================================================

def pure_python_analysis():
    """Analyze sales data using only Python builtins."""
    print("=" * 50)
    print("WAY 1: Pure Python")
    print("=" * 50)

    # Task 1: Monthly totals
    monthly_totals = [sum(row) for row in sales_data]
    print("\n--- Monthly Totals ---")
    for m, total in zip(months, monthly_totals):
        print(f"  Month {m}: {total}M")

    # Task 2: Month-over-month growth
    print("\n--- Month-over-Month Growth ---")
    for i in range(1, len(monthly_totals)):
        growth = (monthly_totals[i] - monthly_totals[i-1]) / monthly_totals[i-1]
        print(f"  Month {months[i]}: {growth:>+.2%}")

    # Task 3: Annual sales by region (sorted)
    region_totals = {}
    for j, region in enumerate(regions):
        region_totals[region] = sum(sales_data[i][j] for i in range(12))
    sorted_regions = sorted(region_totals, key=lambda r: region_totals[r], reverse=True)
    print("\n--- Annual Sales by Region (sorted) ---")
    for r in sorted_regions:
        print(f"  {r}: {region_totals[r]}M")

    # Task 4: Peak sales
    max_val, max_month, max_region = 0, 0, 0
    for i in range(len(months)):
        for j in range(len(regions)):
            if sales_data[i][j] > max_val:
                max_val = sales_data[i][j]
                max_month, max_region = i, j
    print(f"\n--- Peak Sales ---")
    print(f"  Month {months[max_month]}, {regions[max_region]}: {max_val}M")

    # Task 5: Most volatile region (population variance)
    print("\n--- Most Volatile Region ---")
    max_var, most_volatile = 0, ""
    for j, region in enumerate(regions):
        values = [sales_data[i][j] for i in range(12)]
        avg = sum(values) / len(values)
        var = sum((x - avg) ** 2 for x in values) / len(values)
        if var > max_var:
            max_var, most_volatile = var, region
    print(f"  {most_volatile} (variance: {max_var:.1f})")
    print()


# =============================================================================
# Way 2: NumPy (vectorized operations with axis)
# =============================================================================

def numpy_analysis():
    """Same analysis using NumPy - vectorized, no loops."""
    print("=" * 50)
    print("WAY 2: NumPy")
    print("=" * 50)

    data = np.array(sales_data)
    print(f"\nArray shape: {data.shape}  (12 months x 5 regions)")

    # Task 1: Monthly totals - sum along axis=1 (columns)
    monthly_totals = data.sum(axis=1)
    print(f"\n--- Monthly Totals (axis=1) ---")
    print(f"  {monthly_totals}")

    # Task 2: Month-over-month growth
    mom = np.diff(monthly_totals) / monthly_totals[:-1]
    print(f"\n--- MoM Growth ---")
    print(f"  {np.round(mom * 100, 1)}%")

    # Task 3: Annual by region - sum along axis=0 (rows)
    region_totals = data.sum(axis=0)
    sorted_idx = np.argsort(region_totals)[::-1]
    print(f"\n--- Annual Sales by Region (sorted) ---")
    for idx in sorted_idx:
        print(f"  {regions[idx]}: {region_totals[idx]}M")

    # Task 4: Peak sales - argmax on flattened then unravel
    flat_idx = data.argmax()
    peak_month, peak_region = np.unravel_index(flat_idx, data.shape)
    print(f"\n--- Peak Sales ---")
    print(f"  Month {months[peak_month]}, {regions[peak_region]}: "
          f"{data[peak_month, peak_region]}M")

    # Task 5: Most volatile - variance along axis=0
    variances = data.var(axis=0)
    most_volatile = np.argmax(variances)
    print(f"\n--- Most Volatile Region ---")
    print(f"  {regions[most_volatile]} (variance: {variances[most_volatile]:.1f})")
    print(f"  All variances: {np.round(variances, 1)}")
    print()


# =============================================================================
# Way 3: Pandas (labeled data, built-in methods)
# =============================================================================

def pandas_analysis():
    """Same analysis using Pandas - labeled, expressive, chainable."""
    print("=" * 50)
    print("WAY 3: Pandas")
    print("=" * 50)

    df = pd.DataFrame(sales_data, columns=regions,
                      index=[f'Month {m}' for m in months])
    print(f"\n{df}\n")

    # Task 1: Monthly totals
    print("--- Monthly Totals (df.sum(axis=1)) ---")
    print(df.sum(axis=1))
    print()

    # Task 2: Month-over-month with pct_change()
    print("--- MoM Growth (pct_change()) ---")
    print(df.sum(axis=1).pct_change().dropna().map('{:.2%}'.format))
    print()

    # Task 3: Annual by region (sorted)
    print("--- Annual Sales by Region (sorted) ---")
    print(df.sum().sort_values(ascending=False))
    print()

    # Task 4: Peak sales with idxmax on stacked DataFrame
    stacked = df.stack()
    peak_idx = stacked.idxmax()
    print(f"--- Peak Sales ---")
    print(f"  {peak_idx[0]}, {peak_idx[1]}: {stacked[peak_idx]}M")
    print()

    # Task 5: Most volatile
    print("--- Most Volatile Region (var()) ---")
    variances = df.var(ddof=0)
    print(f"  {variances.idxmax()} (variance: {variances.max():.1f})")
    print(f"  All variances:\n{variances.round(1)}")
    print()


# =============================================================================
# Comparison Summary
# =============================================================================

def comparison_summary():
    """Compare the three approaches."""
    print("=" * 50)
    print("COMPARISON SUMMARY")
    print("=" * 50)
    print("""
    Pure Python:
      + No dependencies
      + Easy to understand
      - Verbose (many loops)
      - Slow on large data

    NumPy:
      + Fast (vectorized C operations)
      + Concise (axis-based operations)
      - Integer indexing only (no labels)
      - Homogeneous dtype

    Pandas:
      + Labeled data (named rows/columns)
      + Rich methods (pct_change, describe, groupby)
      + Handles mixed types and missing values
      + Great for tabular data
      - More memory overhead
      - Learning curve for API
    """)


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    pure_python_analysis()
    numpy_analysis()
    pandas_analysis()
    comparison_summary()
