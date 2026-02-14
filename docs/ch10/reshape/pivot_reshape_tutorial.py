# Pandas Tutorial: Pivot Tables and Reshaping Data
# Covers pivot, pivot_table, melt, stack, and unstack

import pandas as pd
import numpy as np

print("="*70)
print("PIVOT TABLES AND RESHAPING")
print("="*70)

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=12, freq='M'),
    'Product': ['A', 'B'] * 6,
    'Region': ['North', 'North', 'South', 'South'] * 3,
    'Sales': np.random.randint(100, 1000, 12)
})

print("\nOriginal Data:")
print(data)

# Pivot
print("\n1. Pivot (reshape from long to wide):")
pivoted = data.pivot(index='Date', columns='Product', values='Sales')
print(pivoted.head())

# Pivot table (with aggregation)
print("\n2. Pivot Table with aggregation:")
pivot_table = data.pivot_table(values='Sales', 
                                index='Product', 
                                columns='Region',
                                aggfunc='mean')
print(pivot_table)

# Multiple aggregation functions
print("\n3. Pivot table with multiple functions:")
pivot_multi = data.pivot_table(values='Sales',
                               index='Product',
                               columns='Region',
                               aggfunc=['sum', 'mean', 'count'])
print(pivot_multi)

# Melt (reshape from wide to long)
wide_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 92, 78],
    'Science': [88, 95, 82],
    'English': [90, 87, 85]
})

print("\n4. Wide format data:")
print(wide_data)

print("\n5. Melt (reshape to long format):")
melted = pd.melt(wide_data, 
                 id_vars=['ID', 'Name'],
                 value_vars=['Math', 'Science', 'English'],
                 var_name='Subject',
                 value_name='Score')
print(melted)

# Stack and Unstack
df_multi = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['X', 'Y', 'Z'])

print("\n6. Original DataFrame:")
print(df_multi)

print("\n7. Stack (columns to rows):")
stacked = df_multi.stack()
print(stacked)

print("\n8. Unstack (rows to columns):")
unstacked = stacked.unstack()
print(unstacked)

# Cross-tabulation
df_survey = pd.DataFrame({
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Age_Group': ['Young', 'Young', 'Old', 'Old', 'Young', 'Old'],
    'Response': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
})

print("\n9. Cross-tabulation:")
crosstab = pd.crosstab(df_survey['Gender'], 
                       df_survey['Response'],
                       margins=True)
print(crosstab)

print("\nKEY TAKEAWAYS:")
print("- pivot(): Reshape data (needs unique index/column combinations)")
print("- pivot_table(): Pivot with aggregation")
print("- melt(): Convert wide to long format")
print("- stack(): Pivot columns to row index")
print("- unstack(): Pivot row index to columns")
print("- crosstab(): Compute frequency table")