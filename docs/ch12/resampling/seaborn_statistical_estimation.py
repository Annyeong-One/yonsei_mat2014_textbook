"""
Tutorial 08: Statistical Estimation
Error bars, confidence intervals, bootstrapping
Level: Advanced
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
tips = sns.load_dataset('tips')

# Barplot with confidence intervals (default 95%)
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='tip', ci=95, capsize=0.1)
plt.title('Mean with 95% Confidence Interval', fontsize=14, fontweight='bold')
plt.ylabel('Average Tip ($)')
plt.show()

# Pointplot - show means and CIs with lines
plt.figure(figsize=(10, 6))
sns.pointplot(data=tips, x='day', y='tip', hue='time', ci=95, markers=['o', 's'], linestyles=['-', '--'])
plt.title('Point Plot with Confidence Intervals', fontsize=14, fontweight='bold')
plt.legend(title='Time of Day')
plt.show()

# Custom bootstrap example
np.random.seed(42)
sample_data = pd.DataFrame({
    'group': ['A']*50 + ['B']*50,
    'value': np.concatenate([np.random.normal(10, 2, 50), np.random.normal(12, 2, 50)])
})

plt.figure(figsize=(10, 6))
sns.barplot(data=sample_data, x='group', y='value', ci=95, capsize=0.1, errwidth=2)
plt.title('Bootstrapped Confidence Intervals', fontsize=14, fontweight='bold')
plt.ylabel('Mean Value')
plt.show()

print("Tutorial 08 demonstrates statistical estimation visualization")
print("Key concept: confidence intervals via bootstrapping")
