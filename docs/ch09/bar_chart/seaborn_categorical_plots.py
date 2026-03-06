"""
Tutorial 04: Categorical Plots in Seaborn

This tutorial covers plots designed specifically for categorical data.
These plots help compare distributions and values across different categories.

Learning Objectives:
- Create box plots and violin plots
- Use strip plots and swarm plots
- Build point plots and count plots
- Understand when to use each categorical plot
- Combine multiple plot types

Author: Educational Python Package
Level: Intermediate
Prerequisites: Tutorial 01-03
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == "__main__":

    sns.set_style("whitegrid")
    sns.set_context("notebook")

    # =============================================================================
    # SECTION 1: BOX PLOTS - SHOWING DISTRIBUTION SUMMARY
    # =============================================================================

    """
    BOX PLOTS display the five-number summary:
    - Minimum (excluding outliers)
    - First quartile (Q1, 25th percentile)
    - Median (Q2, 50th percentile)
    - Third quartile (Q3, 75th percentile)
    - Maximum (excluding outliers)
    - Outliers shown as individual points

    Box anatomy:
    - Box: Interquartile range (IQR = Q3 - Q1)
    - Line in box: Median
    - Whiskers: Extend to 1.5 * IQR
    - Points beyond whiskers: Outliers

    Function: sns.boxplot()
    """

    print("="*80)
    print("SECTION 1: BOX PLOTS")
    print("="*80)

    tips = sns.load_dataset('tips')

    # Example 1.1: Basic box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x='day', y='total_bill')
    plt.title('Box Plot: Total Bill by Day', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Basic box plot created")

    # Example 1.2: Box plot with grouping
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
    plt.title('Box Plot with Grouping: Bill by Day and Time', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.legend(title='Time of Day')
    plt.tight_layout()
    plt.show()

    print("✓ Grouped box plot created")

    # Example 1.3: Horizontal box plot
    plt.figure(figsize=(10, 8))
    sns.boxplot(data=tips, y='day', x='total_bill', orient='h')
    plt.title('Horizontal Box Plot', fontsize=14, fontweight='bold')
    plt.ylabel('Day of Week', fontsize=12)
    plt.xlabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Horizontal box plot created")

    # Example 1.4: Customized box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=tips, 
        x='day', 
        y='total_bill',
        palette='Set2',
        linewidth=2.5,
        width=0.6,  # Width of boxes
        fliersize=5  # Size of outlier points
    )
    plt.title('Customized Box Plot', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Customized box plot created\n")

    # =============================================================================
    # SECTION 2: VIOLIN PLOTS - DISTRIBUTION SHAPE
    # =============================================================================

    """
    VIOLIN PLOTS combine box plots with KDE plots. They show:
    - Distribution shape (width of violin)
    - Quartiles and median (inner box)
    - Full data density

    Advantages over box plots:
    - Show bimodal distributions
    - Display distribution shape
    - More informative about data density

    Function: sns.violinplot()
    """

    print("="*80)
    print("SECTION 2: VIOLIN PLOTS")
    print("="*80)

    # Example 2.1: Basic violin plot
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=tips, x='day', y='total_bill')
    plt.title('Violin Plot: Total Bill by Day', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Basic violin plot created")

    # Example 2.2: Violin plot with inner representation options
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Box: Shows box plot inside
    sns.violinplot(data=tips, x='day', y='total_bill', inner='box', ax=axes[0, 0])
    axes[0, 0].set_title("inner='box' - Box plot inside")

    # Quartile: Shows quartile lines
    sns.violinplot(data=tips, x='day', y='total_bill', inner='quartile', ax=axes[0, 1])
    axes[0, 1].set_title("inner='quartile' - Quartile lines")

    # Point: Shows all data points
    sns.violinplot(data=tips, x='day', y='total_bill', inner='point', ax=axes[1, 0])
    axes[1, 0].set_title("inner='point' - All data points")

    # Stick: Shows each observation
    sns.violinplot(data=tips, x='day', y='total_bill', inner='stick', ax=axes[1, 1])
    axes[1, 1].set_title("inner='stick' - Individual observations")

    plt.tight_layout()
    plt.show()

    print("✓ Violin plots with different inner types created")

    # Example 2.3: Split violin plot (comparing two groups)
    plt.figure(figsize=(10, 6))
    sns.violinplot(
        data=tips, 
        x='day', 
        y='total_bill', 
        hue='sex',
        split=True,  # Split violin in half for comparison
        palette='Set2'
    )
    plt.title('Split Violin Plot: Comparing by Gender', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()

    print("✓ Split violin plot created\n")

    # =============================================================================
    # SECTION 3: STRIP AND SWARM PLOTS - INDIVIDUAL POINTS
    # =============================================================================

    """
    STRIP PLOTS show all individual data points, optionally with jitter.
    SWARM PLOTS arrange points to avoid overlap, showing density.

    When to use:
    - Strip: Simple, fast, good for small-medium datasets
    - Swarm: More informative about density, slower for large datasets

    Functions: sns.stripplot(), sns.swarmplot()
    """

    print("="*80)
    print("SECTION 3: STRIP AND SWARM PLOTS")
    print("="*80)

    # Example 3.1: Strip plot
    plt.figure(figsize=(10, 6))
    sns.stripplot(data=tips, x='day', y='total_bill', alpha=0.5)
    plt.title('Strip Plot: Individual Data Points', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Strip plot created")

    # Example 3.2: Strip plot with jitter
    plt.figure(figsize=(10, 6))
    sns.stripplot(
        data=tips, 
        x='day', 
        y='total_bill',
        jitter=True,  # Add random noise to x-position
        alpha=0.5,
        size=4
    )
    plt.title('Strip Plot with Jitter', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Strip plot with jitter created")

    # Example 3.3: Swarm plot
    plt.figure(figsize=(10, 6))
    sns.swarmplot(data=tips, x='day', y='total_bill', size=4)
    plt.title('Swarm Plot: Non-Overlapping Points', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Swarm plot created")

    # Example 3.4: Swarm plot with grouping
    plt.figure(figsize=(12, 6))
    sns.swarmplot(data=tips, x='day', y='total_bill', hue='time', size=4)
    plt.title('Swarm Plot with Grouping', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.legend(title='Time of Day')
    plt.tight_layout()
    plt.show()

    print("✓ Grouped swarm plot created\n")

    # =============================================================================
    # SECTION 4: COMBINING PLOT TYPES
    # =============================================================================

    """
    Combining different plot types gives the most complete picture.
    Common combinations:
    - Box + Strip: Shows summary and individual points
    - Violin + Swarm: Shows distribution and all data
    """

    print("="*80)
    print("SECTION 4: COMBINING PLOT TYPES")
    print("="*80)

    # Example 4.1: Box plot with strip plot overlay
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=tips, x='day', y='total_bill', color='lightgray', width=0.5)
    sns.stripplot(data=tips, x='day', y='total_bill', color='black', alpha=0.3, size=3)
    plt.title('Box Plot with Strip Plot Overlay', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Combined box and strip plot created")

    # Example 4.2: Violin plot with swarm plot overlay
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=tips, x='day', y='total_bill', inner=None, color='lightblue', alpha=0.6)
    sns.swarmplot(data=tips, x='day', y='total_bill', color='black', alpha=0.5, size=3)
    plt.title('Violin Plot with Swarm Plot Overlay', fontsize=14, fontweight='bold')
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Total Bill ($)', fontsize=12)
    plt.tight_layout()
    plt.show()

    print("✓ Combined violin and swarm plot created\n")

    # =============================================================================
    # KEY TAKEAWAYS
    # =============================================================================

    """
    🎯 KEY TAKEAWAYS:

    1. BOX PLOTS: Best for showing 5-number summary and outliers
    2. VIOLIN PLOTS: Show distribution shape, good for multimodal data
    3. STRIP PLOTS: Show all individual points, use jitter to reduce overlap
    4. SWARM PLOTS: Like strip plots but automatically avoid overlap
    5. COMBINE plots for comprehensive visualization
    6. Use 'hue' for grouping, 'split' for split violins
    7. Choose plot based on: data size, question, audience

    NEXT: Tutorial 05 - Regression Plots
    """

    print("="*80)
    print("TUTORIAL 04 COMPLETE!")
    print("="*80)
