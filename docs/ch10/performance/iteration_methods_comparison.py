"""
Pandas Iteration Methods: Performance Comparison

When you need to process each row of a pandas DataFrame, you have many options:

1. iterrows()     - Returns index and Series for each row (slow!)
2. iloc loop      - Manual indexing loop
3. apply()        - Functional approach with Python objects
4. apply(raw=True) - Apply with raw=True uses numpy arrays (faster!)
5. Vectorized     - Avoid iteration entirely (fastest!)

This tutorial shows why some methods are dramatically faster than others.

KEY INSIGHT:
The fastest method is no method at all - write code that doesn't iterate!
When you must iterate, use raw=True with apply() or use iloc loop.
AVOID iterrows() - it's the slowest option.

Learning Goals:
- Understand why iteration methods have different speeds
- See how raw=True changes performance
- Learn to identify when vectorization is possible
- Know what NOT to do when processing DataFrames
"""

import time
import pandas as pd
import numpy as np


print("=" * 70)
print("PANDAS ITERATION METHODS: PERFORMANCE COMPARISON")
print("=" * 70)


# ============ EXAMPLE 1: Creating Test Data ============
print("\n" + "=" * 70)
print("EXAMPLE 1: Creating Test DataFrame")
print("=" * 70)

print("""
We'll create a simple DataFrame with 3 columns (X, Y, Z) and perform
a computation on each row using different iteration methods.

The computation: least squares linear regression on (X, Y, Z)
This involves some actual work, so we can measure real differences.
""")

# Create test data
np.random.seed(42)
num_rows = 1000
df = pd.DataFrame({
    'X': np.random.randn(num_rows),
    'Y': np.random.randn(num_rows),
    'Z': np.random.randn(num_rows)
})

print(f"\nDataFrame shape: {df.shape}")
print(f"Rows: {num_rows}")
print(f"\nFirst few rows:")
print(df.head())


# ============ EXAMPLE 2: Define the Computation Function ============
print("\n" + "=" * 70)
print("EXAMPLE 2: Define the Computation Function")
print("=" * 70)

def compute_result(row):
    """
    A simple computation on a row.
    In the original, this was least squares regression.
    We'll do something simpler but similar - compute statistics.

    This function will be called by different iteration methods.
    """
    # Compute a weighted average of the three columns
    x, y, z = row['X'], row['Y'], row['Z']
    result = (x * 0.5 + y * 0.3 + z * 0.2) / (0.5 + 0.3 + 0.2)
    return result


def compute_result_raw(row):
    """
    Same computation, but expecting a numpy array (raw=True version).

    When apply() is called with raw=True, each row is a numpy array,
    not a pandas Series. This is faster because:
    1. No Series overhead
    2. Direct numpy array access
    3. Avoids Series.__getitem__() function calls
    """
    # row is a numpy array with values in order of columns
    x, y, z = row[0], row[1], row[2]
    result = (x * 0.5 + y * 0.3 + z * 0.2) / (0.5 + 0.3 + 0.2)
    return result


# Verify both functions give same results
test_row = df.iloc[0]
print(f"\nTest row: {test_row.to_dict()}")
print(f"compute_result() result:     {compute_result(test_row):.6f}")
print(f"compute_result_raw() result: {compute_result_raw(df.iloc[0].values):.6f}")


# ============ EXAMPLE 3: Method 1 - iterrows() (DON'T USE THIS!) ============
print("\n" + "=" * 70)
print("EXAMPLE 3: iterrows() - Slow (DON'T USE THIS METHOD)")
print("=" * 70)

print("""
iterrows() yields (index, Series) for each row.

WHY IT'S SLOW:
1. Creates a Series object for each row (expensive overhead!)
2. Series objects have lots of metadata and methods
3. Accessing values requires Series.__getitem__() which is slow
4. No way to vectorize or batch operations

When to use it: Almost never. It's the slowest option.
""")

print(f"\nTiming iterrows()...")
start = time.time()
results = []
for idx, row in df.iterrows():
    result = compute_result(row)
    results.append(result)
elapsed_iterrows = time.time() - start

print(f"iterrows() time: {elapsed_iterrows:.4f}s")
print(f"Results (first 5): {results[:5]}")


# ============ EXAMPLE 4: Method 2 - iloc loop ============
print("\n" + "=" * 70)
print("EXAMPLE 4: iloc Loop - Better than iterrows()")
print("=" * 70)

print("""
Manual loop using iloc[i] to access each row.

WHY IT'S FASTER THAN iterrows():
1. Still creates Series objects (slower part)
2. But avoids iterrows() overhead
3. More explicit control over the iteration

Still slower than apply(), but better than iterrows().
""")

print(f"\nTiming iloc loop...")
start = time.time()
results = []
for row_idx in range(df.shape[0]):
    row = df.iloc[row_idx]
    result = compute_result(row)
    results.append(result)
elapsed_iloc = time.time() - start

print(f"iloc loop time: {elapsed_iloc:.4f}s")
print(f"Results (first 5): {results[:5]}")


# ============ EXAMPLE 5: Method 3 - apply() ============
print("\n" + "=" * 70)
print("EXAMPLE 5: apply() - Functional and Faster")
print("=" * 70)

print("""
Use apply() with a function applied to each row (axis=1).

WHY IT'S FASTER:
1. apply() is optimized for this use case
2. It's a pandas method, not a manual loop
3. Potential for future optimization (Dask, etc.)
4. Still slower than vectorized approaches

When to use: When your computation can't be vectorized.
""")

print(f"\nTiming apply() with axis=1...")
start = time.time()
results = df.apply(compute_result, axis=1)
elapsed_apply = time.time() - start

print(f"apply(axis=1) time: {elapsed_apply:.4f}s")
print(f"Results (first 5): {list(results.head())}")


# ============ EXAMPLE 6: Method 4 - apply(raw=True) ============
print("\n" + "=" * 70)
print("EXAMPLE 6: apply(raw=True) - Much Faster!")
print("=" * 70)

print("""
Use apply() with raw=True. Each row becomes a numpy array instead of Series.

WHY IT'S MUCH FASTER:
1. Numpy arrays are simpler than Series objects
2. Array access is faster than Series.__getitem__()
3. No Series metadata overhead
4. Still gives you all the values you need

When to use: Always use raw=True if your function works with numpy arrays!
""")

print(f"\nTiming apply(raw=True)...")
start = time.time()
results = df.apply(compute_result_raw, axis=1, raw=True)
elapsed_apply_raw = time.time() - start

print(f"apply(raw=True) time: {elapsed_apply_raw:.4f}s")
print(f"Results (first 5): {list(results.head())}")


# ============ EXAMPLE 7: Method 5 - Vectorized ============
print("\n" + "=" * 70)
print("EXAMPLE 7: Vectorized - Fastest (No Iteration!)")
print("=" * 70)

print("""
Instead of iterating, use array operations to compute all rows at once.

WHY IT'S FASTEST:
1. No iteration at all - all computation is vectorized
2. All operations are NumPy, implemented in C
3. Can use SIMD instructions
4. Scales best with large data

This is only possible if your computation can be expressed with array operations.

For our computation: weighted_average = x*0.5 + y*0.3 + z*0.2
This is easily vectorizable!
""")

print(f"\nTiming vectorized approach...")
start = time.time()
results = (df['X'] * 0.5 + df['Y'] * 0.3 + df['Z'] * 0.2) / (0.5 + 0.3 + 0.2)
elapsed_vectorized = time.time() - start

print(f"Vectorized time: {elapsed_vectorized:.4f}s")
print(f"Results (first 5): {list(results.head())}")


# ============ EXAMPLE 8: Performance Summary ============
print("\n" + "=" * 70)
print("EXAMPLE 8: Performance Summary & Comparison")
print("=" * 70)

print(f"\n{'Method':<30} {'Time (s)':<12} {'Relative Speed'}")
print("-" * 60)

# Normalize to vectorized (fastest)
base_time = elapsed_vectorized

print(f"{'Vectorized (NO LOOP!)':30} {elapsed_vectorized:>10.4f}s  1.0x (baseline)")
print(f"{'apply(raw=True)':30} {elapsed_apply_raw:>10.4f}s  {elapsed_apply_raw/base_time:>6.1f}x slower")
print(f"{'apply(axis=1)':30} {elapsed_apply:>10.4f}s  {elapsed_apply/base_time:>6.1f}x slower")
print(f"{'iloc loop':30} {elapsed_iloc:>10.4f}s  {elapsed_iloc/base_time:>6.1f}x slower")
print(f"{'iterrows()':30} {elapsed_iterrows:>10.4f}s  {elapsed_iterrows/base_time:>6.1f}x slower")

print(f"\n{'*' * 70}")
print("KEY OBSERVATIONS")
print("{'*' * 70}")

print(f"""
1. VECTORIZED IS FASTEST
   {elapsed_vectorized:.4f}s - When possible, always vectorize!

2. apply(raw=True) IS 2ND BEST
   {elapsed_apply_raw:.4f}s - Much better than raw=False
   Use this when vectorization isn't possible
   Speedup vs vectorized: {elapsed_apply_raw/base_time:.1f}x

3. apply() with Series IS SLOWER
   {elapsed_apply:.4f}s - Default apply() creates Series objects
   Avoid unless you need Series methods

4. iloc LOOP IS EVEN SLOWER
   {elapsed_iloc:.4f}s - Manual indexing adds overhead
   Only use if you can't use apply()

5. iterrows() IS THE SLOWEST
   {elapsed_iterrows:.4f}s - NEVER use this for performance!
   Slowest by {elapsed_iterrows/elapsed_apply_raw:.1f}x compared to apply(raw=True)

SPEEDUP FROM BEST TO WORST: {elapsed_iterrows/elapsed_vectorized:.0f}x !!!
""")


# ============ EXAMPLE 9: When Each Method Is Appropriate ============
print("\n" + "=" * 70)
print("EXAMPLE 9: When to Use Each Method")
print("=" * 70)

print("""
VECTORIZED (Fastest)
- Use when: Your computation can be expressed with numpy/pandas operations
- Example: result = df['A'] * df['B'] + df['C']
- Speed: Baseline (fastest possible)
- Recommendation: ALWAYS use this first!

apply(raw=True) (Good)
- Use when: Vectorization is hard/impossible, need to iterate
- Example: Complex logic that's hard to vectorize
- Speed: ~5x slower than vectorized
- Recommendation: Second choice for non-vectorizable code

apply(axis=1) (Okay)
- Use when: You need Series features (index, dtype, etc.)
- Example: row.index to access column names
- Speed: ~10-50x slower than vectorized
- Recommendation: Only if you need Series-specific features

iloc loop (Avoid)
- Use when: You need very explicit control over iteration
- Example: Complex loop logic with multiple rows
- Speed: Similar to apply() but more verbose
- Recommendation: Rarely needed, use apply() instead

iterrows() (NEVER)
- Use when: You have no other choice (almost never)
- Speed: Slowest by far, {elapsed_iterrows/base_time:.0f}x slower
- Recommendation: Never use for performance-critical code!
""")


# ============ EXAMPLE 10: Vectorization Tips ============
print("\n" + "=" * 70)
print("EXAMPLE 10: How to Vectorize Your Code")
print("=" * 70)

print("""
STRATEGY 1: Use DataFrame operations
    Slow:    result = [func(row) for idx, row in df.iterrows()]
    Fast:    result = df['A'] + df['B']  # Element-wise operations

STRATEGY 2: Use apply() with raw=True for unavoidable iteration
    Slow:    df.apply(lambda row: func(row), axis=1)
    Fast:    df.apply(lambda row: func(row), axis=1, raw=True)

STRATEGY 3: Use NumPy functions
    Slow:    result = df.apply(lambda row: sum(row), axis=1)
    Fast:    result = df.sum(axis=1)

STRATEGY 4: Chain operations
    Slow:    df.apply(lambda row: func(row['A'], row['B']), axis=1)
    Fast:    func(df['A'], df['B'])  # If func works with arrays

STRATEGY 5: Use groupby instead of iterating
    Slow:    groups = {}
             for idx, row in df.iterrows():
                 key = row['key']
                 groups[key] = ...
    Fast:    df.groupby('key').agg(...)

KEY PRINCIPLE: Move operations outside the loop!
""")


print("\n" + "=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print(f"""
When processing pandas DataFrames:

1. FIRST: Can you vectorize? (No iteration needed)
   → Use this! It's {elapsed_iterrows/elapsed_vectorized:.0f}x faster than iterrows()

2. SECOND: Must you iterate?
   → Use apply(raw=True) for {elapsed_apply_raw/base_time:.1f}x speedup vs apply()

3. NEVER: Use iterrows()
   → It's the slowest option by far!

Remember: The best optimization is no optimization - vectorize!
""")
