"""
Data Preprocessing Workflow: Cleaning Real-World Data

A practical workflow demonstrating common data cleaning operations
that are needed before analysis or machine learning.

Steps covered:
1. Handling missing values (detect, fill, drop)
2. Removing duplicates
3. String column splitting and extraction
4. Value replacement and mapping
5. Normalization (min-max scaling, z-score standardization)
6. Binning continuous variables

Based on Python-100-Days Day66-80 day04.ipynb data cleaning examples.
"""

import numpy as np
import pandas as pd


# =============================================================================
# Step 1: Create Sample Messy Data
# =============================================================================

def create_sample_data() -> pd.DataFrame:
    """Create a messy DataFrame that needs preprocessing."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Diana',
                 'Eve', 'Frank', None, 'Grace', 'Bob'],
        'age': [28, 35, None, 28, 42, 31, None, 29, 38, 35],
        'salary_range': ['50K-70K', '80K-100K', '60K-80K', '50K-70K',
                         '90K-120K', '70K-90K', '55K-75K', '65K-85K',
                         '100K-130K', '80K-100K'],
        'department': ['Engineering', 'Marketing', 'Engineering', 'Engineering',
                       'Management', 'marketing', 'engineering', 'Sales',
                       'Management', 'Marketing'],
        'score': [85, 92, 78, 85, 95, 88, 73, None, 91, 92],
        'join_date': ['2020-03-15', '2019-07-22', '2021-01-10', '2020-03-15',
                      '2018-11-05', '2020-08-17', '2022-02-28', '2021-06-12',
                      '2019-03-08', '2019-07-22'],
    }
    return pd.DataFrame(data)


# =============================================================================
# Step 2: Inspect and Report Issues
# =============================================================================

def inspect_data(df: pd.DataFrame) -> None:
    """Report data quality issues."""
    print("=== Data Inspection ===")
    print(f"Shape: {df.shape}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nDuplicate rows: {df.duplicated().sum()}")
    print(f"\nData types:\n{df.dtypes}")
    print()


# =============================================================================
# Step 3: Clean the Data
# =============================================================================

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply a sequence of cleaning operations."""
    df = df.copy()

    # --- Remove duplicates ---
    print("--- Removing Duplicates ---")
    before = len(df)
    df = df.drop_duplicates()
    print(f"  Removed {before - len(df)} duplicate rows")

    # --- Handle missing values ---
    print("\n--- Handling Missing Values ---")

    # Drop rows where name is missing (can't identify)
    df = df.dropna(subset=['name'])
    print(f"  Dropped rows with missing name")

    # Fill numeric missing values with median
    for col in ['age', 'score']:
        median_val = df[col].median()
        filled = df[col].isnull().sum()
        df[col] = df[col].fillna(median_val)
        print(f"  Filled {filled} missing {col} with median ({median_val})")

    # --- Standardize text columns ---
    print("\n--- Standardizing Text ---")
    df['department'] = df['department'].str.strip().str.title()
    print(f"  Departments: {df['department'].unique().tolist()}")

    # --- Parse dates ---
    print("\n--- Parsing Dates ---")
    df['join_date'] = pd.to_datetime(df['join_date'])
    print(f"  Converted join_date to datetime")

    # --- Extract salary range into min/max columns ---
    print("\n--- Extracting Salary Range ---")
    salary_split = df['salary_range'].str.replace('K', '').str.split('-', expand=True)
    df['salary_min'] = salary_split[0].astype(float) * 1000
    df['salary_max'] = salary_split[1].astype(float) * 1000
    df['salary_mid'] = (df['salary_min'] + df['salary_max']) / 2
    print(f"  Created salary_min, salary_max, salary_mid columns")

    return df


# =============================================================================
# Step 4: Normalize Numeric Columns
# =============================================================================

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply normalization techniques."""
    df = df.copy()

    print("\n--- Normalization ---")

    # Min-Max Scaling: scales to [0, 1]
    # formula: (x - min) / (max - min)
    col = 'score'
    min_val, max_val = df[col].min(), df[col].max()
    df['score_minmax'] = (df[col] - min_val) / (max_val - min_val)
    print(f"  Min-Max scaled '{col}': [{df['score_minmax'].min():.2f}, "
          f"{df['score_minmax'].max():.2f}]")

    # Z-Score Standardization: mean=0, std=1
    # formula: (x - mean) / std
    df['score_zscore'] = (df[col] - df[col].mean()) / df[col].std()
    print(f"  Z-Score '{col}': mean={df['score_zscore'].mean():.4f}, "
          f"std={df['score_zscore'].std():.4f}")

    return df


# =============================================================================
# Step 5: Bin Continuous Variables
# =============================================================================

def bin_data(df: pd.DataFrame) -> pd.DataFrame:
    """Create categorical bins from continuous variables."""
    df = df.copy()

    print("\n--- Binning ---")

    # Age bins
    bins = [0, 25, 35, 45, 100]
    labels = ['Junior', 'Mid-Level', 'Senior', 'Executive']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
    print(f"  Age groups:\n{df['age_group'].value_counts().to_string()}")

    # Salary quantile bins
    df['salary_quartile'] = pd.qcut(df['salary_mid'], q=4,
                                     labels=['Q1', 'Q2', 'Q3', 'Q4'])
    print(f"\n  Salary quartiles:\n{df['salary_quartile'].value_counts().to_string()}")

    return df


# =============================================================================
# Step 6: Final Report
# =============================================================================

def final_report(original: pd.DataFrame, cleaned: pd.DataFrame) -> None:
    """Show before/after comparison."""
    print("\n=== Final Report ===")
    print(f"Original: {original.shape[0]} rows, {original.shape[1]} columns")
    print(f"Cleaned:  {cleaned.shape[0]} rows, {cleaned.shape[1]} columns")
    print(f"\nMissing values remaining: {cleaned.isnull().sum().sum()}")
    print(f"\nCleaned columns: {cleaned.columns.tolist()}")
    print(f"\nSample (first 3 rows):")
    print(cleaned.head(3).to_string())


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    # Create and inspect
    raw_df = create_sample_data()
    print("=== Raw Data ===")
    print(raw_df.to_string())
    print()
    inspect_data(raw_df)

    # Clean
    cleaned_df = clean_data(raw_df)

    # Normalize
    cleaned_df = normalize_data(cleaned_df)

    # Bin
    cleaned_df = bin_data(cleaned_df)

    # Report
    final_report(raw_df, cleaned_df)
