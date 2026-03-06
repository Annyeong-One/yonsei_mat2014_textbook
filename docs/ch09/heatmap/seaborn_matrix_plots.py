"""
Tutorial 06: Matrix Plots
Heatmaps, cluster maps, correlation matrices
Level: Intermediate
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    sns.set_style("white")
    tips = sns.load_dataset('tips')

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    numeric_cols = tips.select_dtypes(include=[np.number])
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, square=True, linewidths=1)
    plt.title('Correlation Heatmap', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Pivot table heatmap
    pivot_data = tips.pivot_table(values='tip', index='day', columns='time', aggfunc='mean')
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='YlOrRd')
    plt.title('Average Tip: Day vs Time', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Clustermap - with hierarchical clustering
    plt.figure(figsize=(10, 8))
    sns.clustermap(corr, cmap='coolwarm', center=0, linewidths=1, annot=True)
    plt.show()

    print("Tutorial 06 demonstrates matrix visualizations")
    print("Key functions: heatmap(), clustermap()")
