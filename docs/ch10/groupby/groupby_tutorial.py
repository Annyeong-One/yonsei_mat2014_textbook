# Pandas Tutorial: GroupBy and Aggregation
# This file covers groupby operations, aggregation functions, and split-apply-combine

import pandas as pd
import numpy as np

print("="*70)
print("GROUPBY AND AGGREGATION")
print("="*70)

# Create sample sales data
np.random.seed(42)
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=20, freq='D'),
    'Product': np.random.choice(['A', 'B', 'C'], 20),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 20),
    'Sales': np.random.randint(100, 1000, 20),
    'Quantity': np.random.randint(1, 20, 20)
})

print("\nSample Data:")
print(df.head(10))

# Basic GroupBy
print("\n1. Group by Product and calculate mean:")
print(df.groupby('Product')['Sales'].mean())

print("\n2. Group by multiple columns:")
print(df.groupby(['Product', 'Region'])['Sales'].sum())

# Multiple aggregations
print("\n3. Multiple aggregation functions:")
print(df.groupby('Product').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Quantity': ['sum', 'mean']
}))

# Custom aggregation
print("\n4. Custom aggregation function:")
print(df.groupby('Product')['Sales'].agg(['sum', 'mean', lambda x: x.max() - x.min()]))

# Filter groups
print("\n5. Filter groups (sales > 5000):")
high_sales = df.groupby('Product').filter(lambda x: x['Sales'].sum() > 5000)
print(high_sales)

# Transform
print("\n6. Transform - normalize within groups:")
df['Sales_Normalized'] = df.groupby('Product')['Sales'].transform(lambda x: (x - x.mean()) / x.std())
print(df[['Product', 'Sales', 'Sales_Normalized']].head())

# Apply custom function
print("\n7. Apply custom function to groups:")
def get_stats(group):
    return pd.Series({
        'total': group['Sales'].sum(),
        'avg': group['Sales'].mean(),
        'transactions': len(group)
    })

print(df.groupby('Product').apply(get_stats))

print("\nKEY TAKEAWAYS:")
print("- Use groupby() to split data into groups")
print("- Common aggregations: sum(), mean(), count(), min(), max()")
print("- agg() for multiple functions")
print("- filter() to select groups")
print("- transform() to broadcast results back")
print("- apply() for custom group-wise operations")