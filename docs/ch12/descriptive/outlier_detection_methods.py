"""
Data Cleaning & Preprocessing - Tutorial 04
Topic: Outlier Detection and Treatment (Intermediate)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)

print("="*80)
print("TUTORIAL 04: OUTLIER DETECTION AND TREATMENT")
print("="*80)

# Generate data with outliers
data = np.concatenate([np.random.normal(50, 10, 95), [150, 160, 155, -20, -15]])
df = pd.DataFrame({'value': data})

print("\nDataset statistics:")
print(df.describe())

# Method 1: Z-score
print("\n--- Z-Score Method ---")
z_scores = np.abs((df['value'] - df['value'].mean()) / df['value'].std())
outliers_z = df[z_scores > 3]
print(f"Outliers (|z| > 3): {len(outliers_z)} found")
print(outliers_z)

# Method 2: IQR
print("\n--- IQR Method ---")
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
print(f"IQR bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
print(f"Outliers: {len(outliers_iqr)} found")
print(outliers_iqr)

# Method 3: Modified Z-score (MAD)
print("\n--- Modified Z-Score (MAD) ---")
median = df['value'].median()
mad = np.median(np.abs(df['value'] - median))
modified_z = 0.6745 * (df['value'] - median) / mad
outliers_mad = df[np.abs(modified_z) > 3.5]
print(f"Outliers (robust method): {len(outliers_mad)} found")

# Treatment strategies
print("\n--- Treatment Strategies ---")

# Strategy 1: Remove outliers
df_removed = df[z_scores <= 3]
print(f"1. Removal: {len(df)} → {len(df_removed)} rows")

# Strategy 2: Cap/Winsorize
df_capped = df.copy()
df_capped['value'] = df_capped['value'].clip(lower=lower_bound, upper=upper_bound)
print(f"2. Capping: outliers clipped to [{lower_bound:.2f}, {upper_bound:.2f}]")

# Strategy 3: Log transformation
df_log = df[df['value'] > 0].copy()  # Only positive values
df_log['value_log'] = np.log1p(df_log['value'])
print(f"3. Log transform applied to {len(df_log)} positive values")

print("\nKEY TAKEAWAYS:")
print("- Z-score: assumes normal distribution, sensitive to extreme outliers")
print("- IQR: robust, works for any distribution")
print("- MAD: most robust, resistant to outliers")
print("- Always investigate outliers before removing!")
print("\nNEXT: 05_intermediate_encoding.py")
print("="*80)
