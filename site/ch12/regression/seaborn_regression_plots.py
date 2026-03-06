"""
Tutorial 05: Regression Plots
Learn linear regression visualization, regplot, lmplot, residplot
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

    sns.set_style("whitegrid")
    tips = sns.load_dataset('tips')

    # regplot - simple regression
    plt.figure(figsize=(10, 6))
    sns.regplot(data=tips, x='total_bill', y='tip')
    plt.title('Linear Regression Plot', fontsize=14, fontweight='bold')
    plt.show()

    # lmplot - figure-level with faceting
    g = sns.lmplot(data=tips, x='total_bill', y='tip', hue='time', height=5, aspect=1.5)
    plt.show()

    # residplot - check model assumptions
    plt.figure(figsize=(10, 6))
    sns.residplot(data=tips, x='total_bill', y='tip')
    plt.title('Residual Plot', fontsize=14, fontweight='bold')
    plt.show()

    print("Tutorial 05 demonstrates regression visualizations")
    print("Key functions: regplot(), lmplot(), residplot()")
