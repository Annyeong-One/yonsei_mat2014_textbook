"""
Vector Norm Computation: Pure Python vs NumPy Vectorization

This tutorial demonstrates how vectorizing mathematical operations can lead to
dramatic performance improvements. We'll compute the L2 norm (Euclidean norm) of
a vector using two approaches:

1. Pure Python with explicit loops
2. NumPy with vectorized array operations

The key insight: NumPy operations are implemented in C and operate on entire
arrays at once, while pure Python loops iterate element-by-element, incurring
function call overhead for each iteration.

Learning Goals:
- Understand what vectorization means in practice
- See how NumPy leverages compiled code for speed
- Recognize patterns in your code that could be vectorized
- Measure the real-world performance difference
"""

import time
import numpy as np


print("=" * 70)
print("VECTOR NORM COMPUTATION: PURE PYTHON vs NUMPY VECTORIZATION")
print("=" * 70)


# ============ EXAMPLE 1: Pure Python Implementation ============
print("\n" + "=" * 70)
print("EXAMPLE 1: Pure Python with Explicit Loops")
print("=" * 70)

def norm_square_python(vector):
    """
    Compute the squared L2 norm using pure Python.

    The L2 norm (Euclidean norm) of a vector is: sqrt(sum(v_i^2))
    We compute the squared norm (without the sqrt) since sqrt is expensive
    and we often only care about relative magnitudes.

    Why this is slow:
    - Each iteration calls Python operations (addition, multiplication)
    - Python must interpret each operation
    - No knowledge of what comes next, so can't optimize
    """
    norm = 0
    for v in vector:
        norm += v * v
    return norm


# Create a test vector
test_vector_python = list(range(10000))

# Show what the function returns
result_python = norm_square_python(test_vector_python)
print(f"\nSquared norm of vector [0, 1, 2, ..., 9999]: {result_python}")
print(f"This equals: sum(i^2 for i in 0..9999) = 0^2 + 1^2 + 2^2 + ... + 9999^2")

# Time the pure Python version
num_iterations = 5
times_python = []
test_size = 1000000

test_vector_python = list(range(test_size))
print(f"\nTiming pure Python with vector of {test_size:,} elements ({num_iterations} runs):")

for i in range(num_iterations):
    start = time.time()
    norm_square_python(test_vector_python)
    elapsed = time.time() - start
    times_python.append(elapsed)
    print(f"  Run {i+1}: {elapsed:.6f}s")

min_time_python = min(times_python)
print(f"\nBest pure Python time: {min_time_python:.6f}s")


# ============ EXAMPLE 2: NumPy Vectorized Implementation ============
print("\n" + "=" * 70)
print("EXAMPLE 2: NumPy Vectorized Operations")
print("=" * 70)

def norm_square_numpy(vector):
    """
    Compute the squared L2 norm using NumPy.

    Why this is fast:
    - vector * vector: element-wise multiplication on entire array at once
    - np.sum(): single function call to sum all elements
    - Both operations are implemented in optimized C code
    - NumPy can use SIMD (Single Instruction Multiple Data) on modern CPUs
    - No Python loop overhead!

    The key vectorization principle:
    Instead of: for v in vector: norm += v * v
    Do this:   np.sum(vector * vector)
    """
    return np.sum(vector * vector)


# Create a test vector using NumPy
test_vector_numpy = np.arange(10000)

# Show what the function returns
result_numpy = norm_square_numpy(test_vector_numpy)
print(f"\nSquared norm of vector [0, 1, 2, ..., 9999]: {result_numpy}")
print(f"Note: Same result as pure Python (both should be {int(result_python)})")

# Time the NumPy version
times_numpy = []
test_vector_numpy = np.arange(test_size)
print(f"\nTiming NumPy with vector of {test_size:,} elements ({num_iterations} runs):")

for i in range(num_iterations):
    start = time.time()
    norm_square_numpy(test_vector_numpy)
    elapsed = time.time() - start
    times_numpy.append(elapsed)
    print(f"  Run {i+1}: {elapsed:.6f}s")

min_time_numpy = min(times_numpy)
print(f"\nBest NumPy time: {min_time_numpy:.6f}s")


# ============ EXAMPLE 3: Performance Comparison ============
print("\n" + "=" * 70)
print("EXAMPLE 3: Performance Comparison & Speedup Analysis")
print("=" * 70)

speedup = min_time_python / min_time_numpy
print(f"\nResults for {test_size:,}-element vector:")
print(f"  Pure Python: {min_time_python:.6f}s")
print(f"  NumPy:       {min_time_numpy:.6f}s")
print(f"  Speedup:     {speedup:.1f}x faster with NumPy")

print(f"\n{'*' * 70}")
print("WHY IS VECTORIZATION SO POWERFUL?")
print("{'*' * 70}")

print("""
1. ELIMINATION OF PYTHON LOOP OVERHEAD
   - Pure Python: 1,000,000 iterations through Python's interpreter
   - NumPy: One C function call that processes all data

2. COMPILED C IMPLEMENTATION
   - NumPy operations (*, sum) are written in C
   - C is orders of magnitude faster than interpreted Python
   - Direct memory access without Python's dynamic type checking

3. SIMD VECTORIZATION
   - Modern CPUs have instructions to process multiple values in one step
   - NumPy can use these (AVX, SSE) for additional speedup
   - Python loops cannot take advantage of this

4. MEMORY LAYOUT AWARENESS
   - NumPy arrays store data in continuous memory blocks
   - CPU caches work optimally with this layout
   - Python lists are scattered pointers, poor cache behavior

5. ALGORITHMIC OPTIMIZATION
   - NumPy's internals are battle-tested and optimized
   - Authors have spent years perfecting these algorithms
   - Your hand-written loops can't compete
""")


# ============ EXAMPLE 4: Correct NumPy Norm Using Built-in ============
print("\n" + "=" * 70)
print("EXAMPLE 4: Using NumPy's Built-in Norm Function")
print("=" * 70)

print("""
In real code, you'd use NumPy's norm function:
  norm = np.linalg.norm(vector)  # Computes sqrt(sum(v_i^2))

This is even more optimized and handles edge cases properly.
""")

# Demonstrate
vector_example = np.array([3.0, 4.0])
norm_result = np.linalg.norm(vector_example)
print(f"Example: norm([3, 4]) = {norm_result} (should be 5.0)")
print(f"  Verification: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5.0")


# ============ EXAMPLE 5: The Vectorization Pattern ============
print("\n" + "=" * 70)
print("EXAMPLE 5: Recognizing Vectorization Opportunities")
print("=" * 70)

print("""
When you see this pattern in Python:

    result = initial_value
    for element in collection:
        result = operation(result, element)

Consider if you can vectorize it with NumPy:

    1. Convert to NumPy array
    2. Use element-wise operations (*, +, etc.)
    3. Use aggregation functions (sum, mean, max, etc.)

Example transformations:

BEFORE (Pure Python):
    total = 0
    for x in values:
        total += x * x

AFTER (Vectorized):
    total = np.sum(values * values)

BEFORE (Pure Python):
    result = []
    for i, val in enumerate(my_list):
        result.append(val * 2)

AFTER (Vectorized):
    result = np.array(my_list) * 2

The principle: Avoid Python loops over numeric data when possible.
""")


print("\n" + "=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print(f"""
Vectorization with NumPy can provide {speedup:.0f}x+ speedup for numerical
operations. The main idea is to let compiled libraries (NumPy, using C code)
handle the iteration instead of Python's interpreter.

This is one of the most important optimization techniques for data-heavy
Python code. As a rule of thumb:
- Numerical operations on large arrays → Use NumPy
- File I/O or string processing → Optimize differently
- When speed matters, measure and vectorize
""")
