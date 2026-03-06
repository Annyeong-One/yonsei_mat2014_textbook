"""
03_array_indexing.py - Indexing and Slicing

🔗 CRITICAL: Slices return VIEWS not COPIES! (Topic #24)
"""

import numpy as np

if __name__ == "__main__":

    print("="*80)
    print("ARRAY INDEXING AND SLICING")
    print("="*80)
    print("\n🔗 Views vs Copies - Critical concept from Topic #24!")

    # ============================================================================
    # 1D Indexing (like Python lists)
    # ============================================================================

    print("\n" + "="*80)
    print("1D Indexing")
    print("="*80)

    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"  arr[0] = {arr[0]}")  # First element
    print(f"  arr[-1] = {arr[-1]}")  # Last element
    print(f"  arr[1:4] = {arr[1:4]}")  # Slicing

    # ============================================================================
    # CRITICAL: Slices are VIEWS! (Topic #24)
    # ============================================================================

    print("\n" + "="*80)
    print("CRITICAL: Slices Return VIEWS (Topic #24)")
    print("="*80)

    arr = np.array([1, 2, 3, 4, 5])
    view = arr[1:4]  # Elements at index 1, 2, 3

    print(f"Original: {arr}")
    print(f"View: {view}")
    print(f"\nview.base is arr: {view.base is arr} ← It's a VIEW!")

    # Modify the view
    view[0] = 999
    print(f"\nAfter view[0] = 999:")
    print(f"  Original: {arr} ← CHANGED!")
    print(f"  View: {view}")

    print("""
    This is DIFFERENT from Python lists!
    Python: slice_copy = my_list[1:4]  # Creates COPY
    NumPy:  view = arr[1:4]            # Creates VIEW

    Why? Memory efficiency (Topic #24)!
    Views share memory, no copying needed.
    """)

    # Want an independent copy? Use .copy()
    arr = np.array([1, 2, 3, 4, 5])
    independent = arr[1:4].copy()
    independent[0] = 888

    print(f"\nUsing .copy():")
    print(f"  Original: {arr} ← Unchanged")
    print(f"  Copy: {independent}")

    # ============================================================================
    # Multi-dimensional Indexing
    # ============================================================================

    print("\n" + "="*80)
    print("2D Indexing")
    print("="*80)

    matrix = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]])
    print(f"Matrix:\n{matrix}\n")

    print(f"matrix[0, 0] = {matrix[0, 0]}  ← Row 0, Col 0")
    print(f"matrix[1, 2] = {matrix[1, 2]}  ← Row 1, Col 2")
    print(f"matrix[-1, -1] = {matrix[-1, -1]}  ← Last row, last col")

    # Slicing rows and columns
    print(f"\nmatrix[0, :] = {matrix[0, :]}  ← First row (all cols)")
    print(f"matrix[:, 0] = {matrix[:, 0]}  ← First column (all rows)")
    print(f"matrix[1:, 1:] = \n{matrix[1:, 1:]}  ← Bottom-right 2x2")

    # ============================================================================
    # Boolean Indexing (returns COPY!)
    # ============================================================================

    print("\n" + "="*80)
    print("Boolean Indexing")
    print("="*80)

    arr = np.array([10, 15, 20, 25, 30])
    mask = arr > 18  # Boolean array
    print(f"Array: {arr}")
    print(f"Mask (arr > 18): {mask}")
    print(f"arr[mask] = {arr[mask]}  ← Elements where mask is True")

    print("""
    \nNote: Boolean indexing creates a COPY, not a view!
    Why? Selected elements may not be contiguous in memory.
    """)

    print("""
    \n🎯 KEY TAKEAWAYS:
    1. Slicing returns VIEWS (shares memory!)
    2. Use .copy() for independent arrays
    3. Boolean indexing returns COPIES
    4. .base attribute checks if it's a view

    🔜 NEXT: 04_basic_operations.py
    """)
