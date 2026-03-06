"""
Pandas Tutorial: Performance Optimization.

Covers techniques for faster data processing.
"""

import pandas as pd
import numpy as np
import time

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    print("="*70)
    print("PERFORMANCE OPTIMIZATION")
    print("="*70)

    # Create large dataset
    n = 100000
    np.random.seed(42)
    df = pd.DataFrame({
        'A': np.random.randint(0, 100, n),
        'B': np.random.randint(0, 100, n),
        'C': np.random.choice(['X', 'Y', 'Z'], n),
        'D': np.random.random(n)
    })

    print(f"\nDataFrame with {len(df):,} rows")
    print(df.head())

    # 1. Vectorized operations vs loops
    print("\n1. Vectorized operations vs loops:")

    # Loop (slow)
    start = time.time()
    result_loop = []
    for val in df['A']:
        result_loop.append(val * 2)
    loop_time = time.time() - start

    # Vectorized (fast)
    start = time.time()
    result_vec = df['A'] * 2
    vec_time = time.time() - start

    print(f"Loop time: {loop_time:.4f}s")
    print(f"Vectorized time: {vec_time:.4f}s")
    print(f"Speedup: {loop_time/vec_time:.2f}x")

    # 2. Use categorical for repeated strings
    print("\n2. Memory optimization with categorical:")
    print(f"Original memory: {df['C'].memory_usage(deep=True):,} bytes")
    df['C_cat'] = df['C'].astype('category')
    print(f"Categorical memory: {df['C_cat'].memory_usage(deep=True):,} bytes")

    # 3. Query method (faster than boolean indexing for large datasets)
    print("\n3. Query method:")
    start = time.time()
    result1 = df[(df['A'] > 50) & (df['B'] < 30)]
    bool_time = time.time() - start

    start = time.time()
    result2 = df.query('A > 50 and B < 30')
    query_time = time.time() - start

    print(f"Boolean indexing: {bool_time:.4f}s")
    print(f"Query method: {query_time:.4f}s")

    # 4. Use appropriate dtypes
    print("\n4. Optimize data types:")
    df_types = pd.DataFrame({
        'int_col': [1, 2, 3, 4, 5] * 20000,
        'float_col': [1.5, 2.5, 3.5] * 33334
    })

    print("\nBefore optimization:")
    print(df_types.dtypes)
    print(f"Memory: {df_types.memory_usage(deep=True).sum():,} bytes")

    # Downcast to smaller types
    df_types['int_col'] = pd.to_numeric(df_types['int_col'], downcast='integer')
    df_types['float_col'] = pd.to_numeric(df_types['float_col'], downcast='float')

    print("\nAfter optimization:")
    print(df_types.dtypes)
    print(f"Memory: {df_types.memory_usage(deep=True).sum():,} bytes")

    # 5. Avoid chained indexing
    print("\n5. Avoid chained indexing:")
    print("❌ Bad: df[df['A'] > 50]['B'] = 100  (chained)")
    print("✅ Good: df.loc[df['A'] > 50, 'B'] = 100")

    # 6. Use inplace when appropriate (though not always faster)
    print("\n6. Inplace operations:")
    df_temp = df.copy()
    start = time.time()
    df_temp = df_temp.drop(columns=['D'])
    drop_time = time.time() - start

    df_temp2 = df.copy()
    start = time.time()
    df_temp2.drop(columns=['D'], inplace=True)
    inplace_time = time.time() - start

    print(f"Regular drop: {drop_time:.4f}s")
    print(f"Inplace drop: {inplace_time:.4f}s")

    print("\nKEY TAKEAWAYS:")
    print("1. Use vectorized operations instead of loops")
    print("2. Convert repeated strings to categorical")
    print("3. Use query() for complex boolean indexing")
    print("4. Optimize data types (downcast integers/floats)")
    print("5. Avoid chained indexing - use loc/iloc")
    print("6. Consider chunking for very large files")
    print("7. Use eval() for complex expressions")
    print("8. Avoid apply() when vectorization is possible")
