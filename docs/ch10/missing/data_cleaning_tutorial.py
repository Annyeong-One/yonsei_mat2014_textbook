"""
Pandas Tutorial 04: Data Cleaning and Preprocessing
===================================================

This tutorial covers essential data cleaning techniques.
We'll cover:
1. Handling missing data (advanced techniques)
2. Removing duplicates
3. Data validation
4. Outlier detection and handling
5. String cleaning
6. Data type conversions
7. Standardizing and normalizing data

Prerequisites: Tutorials 01-03
Difficulty: Beginner
"""

import pandas as pd
import numpy as np
import warnings

if __name__ == "__main__":
    warnings.filterwarnings('ignore')

    # ============================================================================
    # SECTION 1: COMPREHENSIVE MISSING DATA HANDLING
    # ============================================================================

    print("=" * 70)
    print("HANDLING MISSING DATA")
    print("=" * 70)

    # Create messy dataset with various missing data patterns
    df_missing = pd.DataFrame({
        'Name': ['Alice', 'Bob', None, 'David', 'Eve', '  ', 'Frank', np.nan],
        'Age': [25, np.nan, 35, 28, np.nan, 32, 45, 40],
        'Salary': [50000, 60000, np.nan, 55000, 65000, np.nan, 90000, 70000],
        'Department': ['HR', 'IT', 'Finance', None, 'HR', 'Finance', np.nan, 'IT'],
        'Years': [2, 5, np.nan, 3, np.nan, 7, 12, 8]
    })

    print("Original data with missing values:")
    print(df_missing)

    # Identify missing data
    print("\n1. Check for missing values:")
    print(df_missing.isnull().sum())

    print("\n2. Percentage of missing values per column:")
    print(df_missing.isnull().sum() / len(df_missing) * 100)

    # Replace empty strings and whitespace with NaN
    print("\n3. Replace empty strings with NaN:")
    df_missing = df_missing.replace(r'^\s*$', np.nan, regex=True)
    print(df_missing)

    # Different strategies for filling missing values
    print("\n4. Fill Age with median:")
    df_missing['Age'] = df_missing['Age'].fillna(df_missing['Age'].median())
    print(df_missing)

    print("\n5. Fill Department with mode (most common value):")
    mode_dept = df_missing['Department'].mode()[0]
    df_missing['Department'] = df_missing['Department'].fillna(mode_dept)
    print(df_missing)

    print("\n6. Interpolate Years (for numeric data with trend):")
    df_missing['Years'] = df_missing['Years'].interpolate()
    print(df_missing)

    print("\n7. Drop rows with remaining NaN values:")
    df_clean = df_missing.dropna()
    print(f"Rows before: {len(df_missing)}, after: {len(df_clean)}")
    print(df_clean)

    # ============================================================================
    # SECTION 2: HANDLING DUPLICATES
    # ============================================================================

    print("\n" + "=" * 70)
    print("HANDLING DUPLICATES")
    print("=" * 70)

    # Create data with duplicates
    df_duplicates = pd.DataFrame({
        'ID': [1, 2, 2, 3, 4, 4, 5],
        'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David', 'Eve'],
        'Score': [85, 92, 92, 78, 88, 88, 95]
    })

    print("Data with duplicates:")
    print(df_duplicates)

    print("\n1. Check for duplicate rows:")
    print(df_duplicates.duplicated())
    print(f"Number of duplicates: {df_duplicates.duplicated().sum()}")

    print("\n2. Show duplicate rows:")
    duplicate_rows = df_duplicates[df_duplicates.duplicated()]
    print(duplicate_rows)

    print("\n3. Remove duplicates (keep first occurrence):")
    df_no_dups = df_duplicates.drop_duplicates()
    print(df_no_dups)

    print("\n4. Remove duplicates based on specific column:")
    df_no_dups_id = df_duplicates.drop_duplicates(subset=['ID'])
    print(df_no_dups_id)

    print("\n5. Keep last occurrence instead of first:")
    df_keep_last = df_duplicates.drop_duplicates(keep='last')
    print(df_keep_last)

    # ============================================================================
    # SECTION 3: DATA VALIDATION
    # ============================================================================

    print("\n" + "=" * 70)
    print("DATA VALIDATION")
    print("=" * 70)

    # Create data with validation issues
    df_validate = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 150, 35, -5, 32],  # Invalid ages
        'Email': ['alice@email.com', 'bob@email', 'charlie@email.com', 
                  'invalid', 'eve@email.com'],  # Invalid emails
        'Salary': [50000, 60000, -10000, 55000, 65000]  # Negative salary
    })

    print("Data with validation issues:")
    print(df_validate)

    # Validate age range
    print("\n1. Validate Age (should be 18-65):")
    invalid_ages = df_validate[(df_validate['Age'] < 18) | (df_validate['Age'] > 65)]
    print(f"Invalid ages found:")
    print(invalid_ages[['Name', 'Age']])

    # Validate email format
    print("\n2. Validate Email format:")
    valid_email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    df_validate['Valid_Email'] = df_validate['Email'].str.match(valid_email_pattern)
    print(df_validate[['Name', 'Email', 'Valid_Email']])

    # Validate salary (must be positive)
    print("\n3. Validate Salary (must be positive):")
    invalid_salaries = df_validate[df_validate['Salary'] < 0]
    print(f"Invalid salaries found:")
    print(invalid_salaries[['Name', 'Salary']])

    # Fix invalid data
    print("\n4. Fix invalid data:")
    # Replace invalid ages with median
    median_age = df_validate[df_validate['Age'].between(18, 65)]['Age'].median()
    df_validate.loc[~df_validate['Age'].between(18, 65), 'Age'] = median_age

    # Replace negative salaries with mean
    mean_salary = df_validate[df_validate['Salary'] > 0]['Salary'].mean()
    df_validate.loc[df_validate['Salary'] < 0, 'Salary'] = mean_salary

    print("Fixed data:")
    print(df_validate)

    # ============================================================================
    # SECTION 4: OUTLIER DETECTION AND HANDLING
    # ============================================================================

    print("\n" + "=" * 70)
    print("OUTLIER DETECTION")
    print("=" * 70)

    # Create data with outliers
    np.random.seed(42)
    normal_data = np.random.normal(100, 15, 100)
    outliers = [200, 250, 300, -50, -100]  # Add extreme values
    df_outliers = pd.DataFrame({
        'Value': np.append(normal_data, outliers)
    })

    print(f"Data with {len(df_outliers)} values")
    print("\nStatistics:")
    print(df_outliers.describe())

    # Method 1: IQR (Interquartile Range) method
    print("\n1. Detect outliers using IQR method:")
    Q1 = df_outliers['Value'].quantile(0.25)
    Q3 = df_outliers['Value'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    print(f"Q1: {Q1:.2f}, Q3: {Q3:.2f}, IQR: {IQR:.2f}")
    print(f"Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")

    outlier_mask = (df_outliers['Value'] < lower_bound) | (df_outliers['Value'] > upper_bound)
    print(f"Number of outliers: {outlier_mask.sum()}")
    print(f"Outlier values: {df_outliers[outlier_mask]['Value'].tolist()}")

    # Method 2: Z-score method
    print("\n2. Detect outliers using Z-score method (|z| > 3):")
    mean = df_outliers['Value'].mean()
    std = df_outliers['Value'].std()
    df_outliers['Z_Score'] = (df_outliers['Value'] - mean) / std
    outliers_z = df_outliers[np.abs(df_outliers['Z_Score']) > 3]
    print(f"Number of outliers: {len(outliers_z)}")
    print(outliers_z)

    # Handling outliers
    print("\n3. Handle outliers by capping at boundaries:")
    df_capped = df_outliers.copy()
    df_capped['Value_Capped'] = df_capped['Value'].clip(lower=lower_bound, upper=upper_bound)
    print("Before and after capping:")
    print(df_capped[outlier_mask][['Value', 'Value_Capped']])

    print("\n4. Remove outliers:")
    df_no_outliers = df_outliers[~outlier_mask]
    print(f"Original size: {len(df_outliers)}, After removing outliers: {len(df_no_outliers)}")

    # ============================================================================
    # SECTION 5: STRING CLEANING
    # ============================================================================

    print("\n" + "=" * 70)
    print("STRING CLEANING")
    print("=" * 70)

    # Create data with messy strings
    df_strings = pd.DataFrame({
        'Name': ['  Alice  ', 'BOB', 'charlie', '  DAVID  ', 'eve'],
        'Email': ['ALICE@EMAIL.COM', 'bob@email.com  ', '  charlie@EMAIL.com', 
                  'david@email.COM', 'eve@Email.COM'],
        'Phone': ['(123) 456-7890', '123-456-7890', '123.456.7890', 
                  '1234567890', '(987)654-3210']
    })

    print("Messy string data:")
    print(df_strings)

    # Clean strings
    print("\n1. Strip whitespace:")
    df_strings['Name'] = df_strings['Name'].str.strip()
    df_strings['Email'] = df_strings['Email'].str.strip()
    print(df_strings)

    print("\n2. Standardize case:")
    df_strings['Name'] = df_strings['Name'].str.title()  # Title case
    df_strings['Email'] = df_strings['Email'].str.lower()  # Lowercase
    print(df_strings)

    print("\n3. Standardize phone numbers:")
    # Remove all non-digit characters and format
    df_strings['Phone_Clean'] = df_strings['Phone'].str.replace(r'\D', '', regex=True)
    df_strings['Phone_Formatted'] = df_strings['Phone_Clean'].apply(
        lambda x: f"({x[:3]}) {x[3:6]}-{x[6:]}" if len(x) == 10 else x
    )
    print(df_strings[['Phone', 'Phone_Formatted']])

    print("\n4. Remove special characters from names:")
    messy_names = pd.Series(['Alice#123', 'Bob$$$', 'Charlie@@@', 'David!!!'])
    clean_names = messy_names.str.replace(r'[^a-zA-Z\s]', '', regex=True)
    print(f"Before: {messy_names.tolist()}")
    print(f"After: {clean_names.tolist()}")

    # ============================================================================
    # SECTION 6: DATA TYPE CONVERSIONS
    # ============================================================================

    print("\n" + "=" * 70)
    print("DATA TYPE CONVERSIONS")
    print("=" * 70)

    # Create data with wrong types
    df_types = pd.DataFrame({
        'ID': ['1', '2', '3', '4', '5'],
        'Age': ['25', '30', '35', '28', '32'],
        'Salary': ['50000.50', '60000.75', '75000.25', '55000.00', '65000.99'],
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'Active': ['True', 'False', 'True', 'True', 'False']
    })

    print("Data with string types:")
    print(df_types.dtypes)

    print("\n1. Convert to numeric:")
    df_types['ID'] = pd.to_numeric(df_types['ID'])
    df_types['Age'] = pd.to_numeric(df_types['Age'])
    df_types['Salary'] = pd.to_numeric(df_types['Salary'])
    print("After conversion:")
    print(df_types.dtypes)

    print("\n2. Convert to datetime:")
    df_types['Date'] = pd.to_datetime(df_types['Date'])
    print(df_types.dtypes)

    print("\n3. Convert to boolean:")
    df_types['Active'] = df_types['Active'].map({'True': True, 'False': False})
    print(df_types.dtypes)

    print("\nFinal DataFrame:")
    print(df_types)

    # Handle conversion errors
    print("\n4. Handle conversion errors:")
    messy_numbers = pd.Series(['1', '2', 'three', '4', 'five'])
    # errors='coerce' converts errors to NaN
    clean_numbers = pd.to_numeric(messy_numbers, errors='coerce')
    print(f"Original: {messy_numbers.tolist()}")
    print(f"Converted: {clean_numbers.tolist()}")

    # ============================================================================
    # SECTION 7: STANDARDIZING AND NORMALIZING
    # ============================================================================

    print("\n" + "=" * 70)
    print("STANDARDIZING AND NORMALIZING")
    print("=" * 70)

    # Create sample data
    df_norm = pd.DataFrame({
        'Height_cm': [160, 170, 180, 150, 175],
        'Weight_kg': [60, 70, 80, 50, 75],
        'Age': [25, 30, 35, 20, 32]
    })

    print("Original data:")
    print(df_norm)

    # Min-Max Normalization (scale to 0-1)
    print("\n1. Min-Max Normalization (0-1):")
    df_norm['Height_Normalized'] = (df_norm['Height_cm'] - df_norm['Height_cm'].min()) / \
                                   (df_norm['Height_cm'].max() - df_norm['Height_cm'].min())
    print(df_norm[['Height_cm', 'Height_Normalized']])

    # Standardization (Z-score normalization)
    print("\n2. Standardization (Z-score):")
    df_norm['Weight_Standardized'] = (df_norm['Weight_kg'] - df_norm['Weight_kg'].mean()) / \
                                     df_norm['Weight_kg'].std()
    print(df_norm[['Weight_kg', 'Weight_Standardized']])

    # Robust scaling (using median and IQR)
    print("\n3. Robust Scaling:")
    median = df_norm['Age'].median()
    Q1 = df_norm['Age'].quantile(0.25)
    Q3 = df_norm['Age'].quantile(0.75)
    IQR = Q3 - Q1
    df_norm['Age_Robust'] = (df_norm['Age'] - median) / IQR
    print(df_norm[['Age', 'Age_Robust']])

    # ============================================================================
    # SECTION 8: COMPLETE CLEANING PIPELINE
    # ============================================================================

    print("\n" + "=" * 70)
    print("COMPLETE CLEANING PIPELINE")
    print("=" * 70)

    # Create a messy dataset
    messy_data = pd.DataFrame({
        'Name': ['  Alice  ', 'BOB', 'charlie', 'Alice', '  DAVID  '],
        'Age': ['25', '150', '35', '25', '-5'],
        'Email': ['alice@email.com', 'bob@email', 'charlie@email.com', 
                  'alice@email.com', 'david@email.com'],
        'Salary': ['50000', '60000', None, '50000', '-10000']
    })

    print("Messy data:")
    print(messy_data)

    def clean_dataframe(df):
        """Complete data cleaning pipeline"""
        df = df.copy()

        # 1. Strip whitespace from strings
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()

        # 2. Standardize case
        if 'Name' in df.columns:
            df['Name'] = df['Name'].str.title()
        if 'Email' in df.columns:
            df['Email'] = df['Email'].str.lower()

        # 3. Convert data types
        if 'Age' in df.columns:
            df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        if 'Salary' in df.columns:
            df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

        # 4. Validate and fix ages
        if 'Age' in df.columns:
            median_age = df[df['Age'].between(18, 100)]['Age'].median()
            df.loc[~df['Age'].between(18, 100), 'Age'] = median_age

        # 5. Handle negative salaries
        if 'Salary' in df.columns:
            df.loc[df['Salary'] < 0, 'Salary'] = np.nan

        # 6. Fill missing values
        if 'Salary' in df.columns:
            df['Salary'] = df['Salary'].fillna(df['Salary'].median())

        # 7. Remove duplicates
        df = df.drop_duplicates()

        return df

    print("\nCleaned data:")
    cleaned_data = clean_dataframe(messy_data)
    print(cleaned_data)
    print("\nData types:")
    print(cleaned_data.dtypes)

    # ============================================================================
    # SECTION 9: SUMMARY
    # ============================================================================

    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)

    summary = """
    1. Missing Data:
       - Use isnull() to identify
       - Fill with fillna(), interpolate(), or drop with dropna()
       - Choose strategy based on data type and pattern

    2. Duplicates:
       - Identify with duplicated()
       - Remove with drop_duplicates()
       - Consider which occurrence to keep

    3. Data Validation:
       - Check ranges, formats, and business rules
       - Use boolean indexing to find invalid data
       - Fix or remove invalid entries

    4. Outliers:
       - Detect using IQR or Z-score methods
       - Handle by capping, removing, or transforming
       - Consider domain knowledge

    5. String Cleaning:
       - Use str.strip(), str.lower(), str.title()
       - Remove special characters with str.replace()
       - Standardize formats

    6. Data Types:
       - Convert with pd.to_numeric(), pd.to_datetime()
       - Handle errors with errors='coerce'
       - Validate conversions

    7. Normalization:
       - Min-Max: Scale to [0, 1]
       - Standardization: Z-score (mean=0, std=1)
       - Robust: Use median and IQR

    8. Create a cleaning pipeline for consistency

    Next Steps:
    -----------
    - Practice with real messy datasets
    - Try the exercise file: exercises/05_cleaning_exercises.py
    - Move on to intermediate topics
    """

    print(summary)
