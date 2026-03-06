"""
04_basic_operations.py - Vectorized Operations

Key concept: Eliminate Python loops with vectorization!
"""

import numpy as np

if __name__ == "__main__":

    print("="*80)
    print("VECTORIZED OPERATIONS - No Loops Needed!")
    print("="*80)

    # ============================================================================
    # Element-wise Arithmetic
    # ============================================================================

    print("\nElement-wise Arithmetic (Vectorization)")
    print("="*80)

    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"  arr + 10 = {arr + 10}  ← Add to all")
    print(f"  arr * 2 = {arr * 2}   ← Multiply all")
    print(f"  arr ** 2 = {arr ** 2}  ← Square all")
    print(f"  1 / arr = {1 / arr}  ← Reciprocal")

    print("""
    \nCompare to Python lists:
      # Python (SLOW - explicit loop):
      result = [x * 2 for x in my_list]

      # NumPy (FAST - vectorized):
      result = arr * 2

    Vectorization = C-speed loop hidden from Python!
    """)

    # Two arrays
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([10, 20, 30])
    print(f"\narr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print(f"  arr1 + arr2 = {arr1 + arr2}  ← Element-wise")
    print(f"  arr1 * arr2 = {arr1 * arr2}  ← Element-wise")

    # ============================================================================
    # Universal Functions (ufuncs)
    # ============================================================================

    print("\n" + "="*80)
    print("Universal Functions (ufuncs)")
    print("="*80)

    arr = np.array([1, 2, 3, 4])
    print(f"Array: {arr}")
    print(f"  np.sqrt(arr) = {np.sqrt(arr)}")
    print(f"  np.exp(arr) = {np.exp(arr)}")
    print(f"  np.log(arr) = {np.log(arr)}")
    print(f"  np.sin(arr) = {np.sin(arr)}")

    # ============================================================================
    # Comparison Operations
    # ============================================================================

    print("\n" + "="*80)
    print("Comparison Operations")
    print("="*80)

    arr = np.array([10, 15, 20, 25, 30])
    print(f"Array: {arr}")
    print(f"  arr > 18 = {arr > 18}  ← Boolean array")
    print(f"  arr == 20 = {arr == 20}")
    print(f"  (arr >= 15) & (arr <= 25) = {(arr >= 15) & (arr <= 25)}")

    # ============================================================================
    # Aggregation Functions
    # ============================================================================

    print("\n" + "="*80)
    print("Aggregation Functions")
    print("="*80)

    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"  arr.sum() = {arr.sum()}")
    print(f"  arr.mean() = {arr.mean()}")
    print(f"  arr.std() = {arr.std():.2f}")
    print(f"  arr.min() = {arr.min()}")
    print(f"  arr.max() = {arr.max()}")
    print(f"  arr.argmin() = {arr.argmin()} ← Index of min")
    print(f"  arr.argmax() = {arr.argmax()} ← Index of max")

    # 2D aggregations
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix:\n{matrix}")
    print(f"  matrix.sum() = {matrix.sum()} ← Total sum")
    print(f"  matrix.sum(axis=0) = {matrix.sum(axis=0)} ← Sum columns")
    print(f"  matrix.sum(axis=1) = {matrix.sum(axis=1)} ← Sum rows")

    print("""
    \n🎯 KEY TAKEAWAYS:
    1. Vectorization eliminates loops (50-200x faster!)
    2. Arithmetic works element-wise
    3. Universal functions (ufuncs) for math
    4. Aggregations: sum, mean, std, min, max
    5. axis parameter: 0=columns, 1=rows

    🔜 NEXT: Intermediate tutorials on broadcasting!
    """)
