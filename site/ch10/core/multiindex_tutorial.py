"""
Pandas Tutorial: Multi-Index (Hierarchical Indexing).

Covers creating and working with multi-level indices.
"""

import pandas as pd
import numpy as np

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*70)
    print("MULTI-INDEX (HIERARCHICAL INDEXING)")
    print("="*70)

    # Create multi-index DataFrame
    np.random.seed(42)
    index = pd.MultiIndex.from_product([
        ['Store1', 'Store2', 'Store3'],
        ['Product A', 'Product B']
    ], names=['Store', 'Product'])

    df = pd.DataFrame({
        'Sales': np.random.randint(100, 1000, 6),
        'Quantity': np.random.randint(10, 100, 6)
    }, index=index)

    print("\nMulti-Index DataFrame:")
    print(df)

    # Selecting with multi-index
    print("\n1. Select by outer index (Store1):")
    print(df.loc['Store1'])

    print("\n2. Select by both indices (Store1, Product A):")
    print(df.loc[('Store1', 'Product A')])

    print("\n3. Select using slice:")
    print(df.loc[('Store1', slice(None)), :])

    # Stack/Unstack
    print("\n4. Unstack (inner index to columns):")
    unstacked = df.unstack()
    print(unstacked)

    print("\n5. Stack back:")
    stacked = unstacked.stack()
    print(stacked)

    # Swap levels
    print("\n6. Swap index levels:")
    swapped = df.swaplevel()
    print(swapped)

    # Sort by index
    print("\n7. Sort by index:")
    sorted_df = swapped.sort_index()
    print(sorted_df)

    # Reset index
    print("\n8. Reset multi-index to columns:")
    reset = df.reset_index()
    print(reset)

    # Set multi-index from columns
    print("\n9. Create multi-index from columns:")
    df_flat = pd.DataFrame({
        'Store': ['A', 'A', 'B', 'B'],
        'Product': ['X', 'Y', 'X', 'Y'],
        'Sales': [100, 200, 150, 250]
    })
    print("Flat DataFrame:")
    print(df_flat)

    df_multi = df_flat.set_index(['Store', 'Product'])
    print("\nWith Multi-Index:")
    print(df_multi)

    # Aggregation with multi-index
    print("\n10. Aggregation by level:")
    print("Sum by Store:")
    print(df.sum(level='Store'))

    print("\nMean by Product:")
    print(df.mean(level='Product'))

    print("\nKEY TAKEAWAYS:")
    print("- MultiIndex: Hierarchical row/column indices")
    print("- Create with from_product(), from_tuples(), from_arrays()")
    print("- Select with loc[] using tuples")
    print("- unstack(): Move index level to columns")
    print("- stack(): Move column level to index")
    print("- swaplevel(): Swap index levels")
    print("- Aggregate by specific levels")
