"""
Business Analytics: GroupBy, Pivot Tables, and Visualization

A practical business analytics workflow using Pandas groupby,
pivot_table, and crosstab for multi-dimensional analysis.

Topics covered:
- GroupBy with multiple aggregation functions
- Pivot tables for cross-tabulation
- Month-over-month (MoM) calculations
- Percent-of-total calculations
- Summary statistics by category

Based on Python-100-Days Day66-80 day05.ipynb business analytics examples.
"""

import numpy as np
import pandas as pd


# =============================================================================
# Setup: Generate Sample Business Data
# =============================================================================

def create_sales_data() -> pd.DataFrame:
    """Create sample sales data for analytics."""
    np.random.seed(42)
    n = 200

    data = {
        'date': pd.date_range('2023-01-01', periods=n, freq='B'),
        'region': np.random.choice(['East', 'West', 'North', 'South'], n),
        'channel': np.random.choice(['Online', 'Retail', 'Wholesale'], n,
                                     p=[0.4, 0.35, 0.25]),
        'product': np.random.choice(['Widget A', 'Widget B', 'Widget C'], n),
        'units': np.random.randint(10, 200, n),
        'unit_price': np.random.choice([25.0, 45.0, 80.0], n),
    }
    df = pd.DataFrame(data)
    df['revenue'] = df['units'] * df['unit_price']
    df['cost'] = df['revenue'] * np.random.uniform(0.4, 0.7, n)
    df['profit'] = df['revenue'] - df['cost']
    df['month'] = df['date'].dt.to_period('M')
    return df


# =============================================================================
# Analysis 1: Monthly Revenue Summary
# =============================================================================

def monthly_summary(df: pd.DataFrame) -> None:
    """Summarize revenue by month with MoM growth."""
    print("=== Monthly Revenue Summary ===")

    monthly = df.groupby('month').agg(
        total_revenue=('revenue', 'sum'),
        total_profit=('profit', 'sum'),
        num_orders=('revenue', 'count'),
        avg_order_value=('revenue', 'mean'),
    ).round(0)

    # Month-over-month growth
    monthly['revenue_mom'] = monthly['total_revenue'].pct_change()
    monthly['profit_margin'] = monthly['total_profit'] / monthly['total_revenue']

    print(monthly.to_string())
    print()


# =============================================================================
# Analysis 2: Region x Channel Pivot Table
# =============================================================================

def region_channel_analysis(df: pd.DataFrame) -> None:
    """Pivot table: revenue by region and channel."""
    print("=== Revenue by Region x Channel ===")

    pivot = pd.pivot_table(
        df,
        values='revenue',
        index='region',
        columns='channel',
        aggfunc='sum',
        margins=True,           # Add row/column totals
        margins_name='Total',
    ).round(0)

    print(pivot.to_string())
    print()

    # Percent of total
    print("--- Percent of Total ---")
    total = pivot.loc['Total', 'Total']
    pct = (pivot / total * 100).round(1)
    print(pct.to_string())
    print()


# =============================================================================
# Analysis 3: Product Performance
# =============================================================================

def product_performance(df: pd.DataFrame) -> None:
    """Analyze performance by product."""
    print("=== Product Performance ===")

    product_stats = df.groupby('product').agg(
        total_units=('units', 'sum'),
        total_revenue=('revenue', 'sum'),
        total_profit=('profit', 'sum'),
        avg_price=('unit_price', 'mean'),
        num_orders=('revenue', 'count'),
    )
    product_stats['profit_margin'] = (
        product_stats['total_profit'] / product_stats['total_revenue']
    )
    product_stats['revenue_per_order'] = (
        product_stats['total_revenue'] / product_stats['num_orders']
    )

    # Sort by total revenue
    product_stats = product_stats.sort_values('total_revenue', ascending=False)

    print(product_stats.round(1).to_string())
    print()


# =============================================================================
# Analysis 4: Cross-Tabulation
# =============================================================================

def channel_region_crosstab(df: pd.DataFrame) -> None:
    """Cross-tabulation of order counts by channel and region."""
    print("=== Order Count: Channel x Region (crosstab) ===")

    ct = pd.crosstab(
        df['channel'],
        df['region'],
        margins=True,
        margins_name='Total',
    )
    print(ct.to_string())
    print()

    # Normalize by row (channel distribution across regions)
    print("--- Channel Distribution Across Regions (%) ---")
    ct_pct = pd.crosstab(
        df['channel'],
        df['region'],
        normalize='index',
    ).round(3) * 100
    print(ct_pct.to_string())
    print()


# =============================================================================
# Analysis 5: Multi-Level Grouping
# =============================================================================

def multi_level_grouping(df: pd.DataFrame) -> None:
    """Group by multiple columns with multiple aggregations."""
    print("=== Multi-Level Grouping: Region + Product ===")

    result = df.groupby(['region', 'product']).agg({
        'revenue': ['sum', 'mean', 'count'],
        'profit': ['sum'],
        'units': ['sum'],
    }).round(0)

    # Flatten column MultiIndex
    result.columns = ['_'.join(col).strip() for col in result.columns]

    # Top 5 by revenue
    print("Top 5 by Total Revenue:")
    print(result.nlargest(5, 'revenue_sum').to_string())
    print()


# =============================================================================
# Analysis 6: Transform and Rank within Groups
# =============================================================================

def group_transform_rank(df: pd.DataFrame) -> None:
    """Use transform and rank within groups."""
    print("=== Transform: Percent of Regional Revenue ===")

    # Each order's revenue as % of its region's total
    df_copy = df[['region', 'channel', 'revenue']].copy()
    df_copy['region_total'] = df_copy.groupby('region')['revenue'].transform('sum')
    df_copy['pct_of_region'] = (df_copy['revenue'] / df_copy['region_total'] * 100).round(2)

    # Rank within region
    df_copy['rank_in_region'] = df_copy.groupby('region')['revenue'].rank(
        ascending=False, method='dense'
    ).astype(int)

    print(df_copy.head(10).to_string(index=False))
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == '__main__':
    df = create_sales_data()
    print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")
    print(f"Columns: {df.columns.tolist()}")
    print()

    monthly_summary(df)
    region_channel_analysis(df)
    product_performance(df)
    channel_region_crosstab(df)
    multi_level_grouping(df)
    group_transform_rank(df)
