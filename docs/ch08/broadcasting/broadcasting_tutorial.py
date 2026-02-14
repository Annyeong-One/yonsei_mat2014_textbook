"""
01_broadcasting.py - NumPy's Most Powerful Feature!

Broadcasting allows arrays of different shapes to work together.
This is what makes NumPy code so elegant and fast!
"""

import numpy as np

print("="*80)
print("BROADCASTING - NumPy's Superpower!")
print("="*80)

# ============================================================================
# What is Broadcasting?
# ============================================================================

print("\nBroadcasting: Operating on arrays of different shapes")
print("="*80)

# Simple example
arr = np.array([1, 2, 3])
print(f"arr = {arr}  (shape: {arr.shape})")
print(f"arr + 10 = {arr + 10}")
print("\nWhat happened? 10 was 'broadcast' to [10, 10, 10]!")

# ============================================================================
# Broadcasting Rules
# ============================================================================

print("\n" + "="*80)
print("The Three Broadcasting Rules")
print("="*80)

print("""
Rule 1: If arrays have different ndim, pad smaller with 1s on LEFT
  arr1.shape = (3, 4, 5)
  arr2.shape = (5,)      → becomes (1, 1, 5)

Rule 2: Dimensions with size 1 are stretched
  arr1.shape = (3, 1, 5)
  arr2.shape = (1, 4, 5) → both become (3, 4, 5)

Rule 3: Dimensions must match or be 1, else ERROR
  arr1.shape = (3, 4)
  arr2.shape = (3, 5)  ← ERROR! 4 != 5 and neither is 1
""")

# ============================================================================
# Common Patterns
# ============================================================================

print("="*80)
print("Common Broadcasting Patterns")
print("="*80)

# Pattern 1: Add row vector to matrix
print("\nPattern 1: Add vector to each row")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row_vec = np.array([10, 20, 30])

print(f"Matrix (3,3):\n{matrix}")
print(f"Vector (3,): {row_vec}")
result = matrix + row_vec
print(f"Result:\n{result}")
print("Each row gets the vector added!")

# Pattern 2: Add column vector to matrix
print("\nPattern 2: Add vector to each column")
col_vec = np.array([[100], [200], [300]])  # Shape (3, 1)
print(f"Column vector (3,1):\n{col_vec}")
result = matrix + col_vec
print(f"Result:\n{result}")
print("Each column gets the vector added!")

# Pattern 3: Outer product
print("\nPattern 3: Multiplication table (outer product)")
x = np.arange(1, 6).reshape(5, 1)  # (5, 1)
y = np.arange(1, 6).reshape(1, 5)  # (1, 5)
table = x * y
print(f"x (column):\n{x}")
print(f"y (row): {y}")
print(f"\nMultiplication table:\n{table}")

# ============================================================================
# Practical Example: Normalizing data
# ============================================================================

print("\n" + "="*80)
print("Practical: Normalizing Each Column")
print("="*80)

# Data: 5 samples, 3 features
data = np.random.randint(0, 100, (5, 3)).astype(float)
print(f"Data (5 samples, 3 features):\n{data}\n")

# Calculate mean of each column
means = data.mean(axis=0)  # Shape (3,)
print(f"Column means: {means}  (shape: {means.shape})")

# Subtract mean (broadcasting!)
centered = data - means  # (5,3) - (3,) broadcasts!
print(f"\nCentered data:\n{centered}")
print(f"\nNew column means: {centered.mean(axis=0)}")
print("  (Should be ~0 for each column)")

print("""
\nWhat happened?
  data.shape = (5, 3)
  means.shape = (3,)
  
Broadcasting:
  means is treated as shape (1, 3)
  Then stretched to (5, 3)
  So each row gets the same means subtracted!
""")

print("""
\n🎯 KEY TAKEAWAYS:
1. Broadcasting eliminates explicit loops
2. Works with arrays of different shapes
3. Memory efficient (no actual copying)
4. Master this for elegant NumPy code!

🔜 NEXT: 02_shape_manipulation.py
""")
