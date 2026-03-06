"""
Pandas Tutorial: Merging, Joining, and Concatenating DataFrames.

Covers different ways to combine DataFrames.
"""

import pandas as pd
import numpy as np

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*70)
    print("MERGING, JOINING, AND CONCATENATING")
    print("="*70)

    # Create sample DataFrames
    df1 = pd.DataFrame({
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28]
    })

    df2 = pd.DataFrame({
        'ID': [1, 2, 3, 5],
        'Department': ['HR', 'IT', 'Finance', 'Marketing'],
        'Salary': [50000, 60000, 75000, 55000]
    })

    print("\nDataFrame 1 (Employees):")
    print(df1)
    print("\nDataFrame 2 (Departments):")
    print(df2)

    # Inner join (default)
    print("\n1. Inner Join (intersection):")
    inner_merged = pd.merge(df1, df2, on='ID', how='inner')
    print(inner_merged)

    # Left join
    print("\n2. Left Join (keep all from left):")
    left_merged = pd.merge(df1, df2, on='ID', how='left')
    print(left_merged)

    # Right join
    print("\n3. Right Join (keep all from right):")
    right_merged = pd.merge(df1, df2, on='ID', how='right')
    print(right_merged)

    # Outer join
    print("\n4. Outer Join (keep all from both):")
    outer_merged = pd.merge(df1, df2, on='ID', how='outer')
    print(outer_merged)

    # Merge on different column names
    df3 = pd.DataFrame({
        'EmpID': [1, 2, 3],
        'Project': ['A', 'B', 'C']
    })

    print("\n5. Merge on different column names:")
    merged_diff = pd.merge(df1, df3, left_on='ID', right_on='EmpID')
    print(merged_diff)

    # Concatenate DataFrames vertically
    df_top = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df_bottom = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

    print("\n6. Concatenate vertically (stack rows):")
    print("Top:")
    print(df_top)
    print("Bottom:")
    print(df_bottom)
    print("Result:")
    vertical_concat = pd.concat([df_top, df_bottom], ignore_index=True)
    print(vertical_concat)

    # Concatenate horizontally
    df_left = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_right = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

    print("\n7. Concatenate horizontally (add columns):")
    horizontal_concat = pd.concat([df_left, df_right], axis=1)
    print(horizontal_concat)

    # Join (using index)
    df_indexed1 = df1.set_index('ID')
    df_indexed2 = df2.set_index('ID')

    print("\n8. Join using index:")
    joined = df_indexed1.join(df_indexed2, how='inner')
    print(joined)

    print("\nKEY TAKEAWAYS:")
    print("- merge(): SQL-style joins on columns")
    print("- concat(): Stack DataFrames vertically or horizontally")
    print("- join(): Merge on index")
    print("- Join types: inner, left, right, outer")
    print("- Use on= for same column names, left_on=/right_on= for different names")
