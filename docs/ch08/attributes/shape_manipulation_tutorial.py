"""
02_shape_manipulation.py - Reshaping and Transforming

🔗 Topic #24: Most operations return VIEWS (no memory copy)!
"""

import numpy as np

if __name__ == "__main__":

    print("="*80)
    print("SHAPE MANIPULATION")
    print("="*80)
    print("\n🔗 Remember: Most operations return VIEWS (Topic #24)!")

    # ============================================================================
    # Reshape
    # ============================================================================

    print("\n" + "="*80)
    print("Reshape - Change Dimensions")
    print("="*80)

    arr = np.arange(12)
    print(f"Original: {arr}")
    print(f"Shape: {arr.shape}")

    matrix = arr.reshape(3, 4)
    print(f"\nReshaped to (3, 4):\n{matrix}")

    # CRITICAL: Reshape returns a VIEW!
    print(f"\nIs it a view? {matrix.base is arr}")
    matrix[0, 0] = 999
    print(f"After matrix[0,0]=999: original arr[0]={arr[0]}")
    print("They share memory! (Topic #24)")

    # ============================================================================
    # Transpose
    # ============================================================================

    print("\n" + "="*80)
    print("Transpose - Flip Dimensions")
    print("="*80)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Original (2,3):\n{matrix}")
    transposed = matrix.T
    print(f"\nTransposed (3,2):\n{transposed}")
    print(f"Is view? {transposed.base is matrix}")

    # ============================================================================
    # Ravel and Flatten
    # ============================================================================

    print("\n" + "="*80)
    print("Ravel vs Flatten")
    print("="*80)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Matrix:\n{matrix}")

    ravel = matrix.ravel()  # Returns view if possible
    flatten = matrix.flatten()  # Always returns copy

    print(f"\nravel(): {ravel}")
    print(f"Is view? {ravel.base is matrix}")

    print(f"\nflatten(): {flatten}")
    print(f"Is view? {flatten.base is matrix}")

    print("""
    \nravel(): Fast (view if possible)
    flatten(): Slower (always copies)
    """)

    print("""
    \n🎯 KEY TAKEAWAYS:
    1. reshape() returns views (fast!)
    2. .T (transpose) returns views
    3. ravel() tries to return view
    4. flatten() always copies
    5. Check .base to verify view vs copy

    🔜 NEXT: 03_mathematical_ops.py
    """)
