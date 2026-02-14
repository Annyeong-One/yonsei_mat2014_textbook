"""
01_performance.py - Writing Fast NumPy Code

Key: Vectorization eliminates Python loops!
"""

import numpy as np
import time

print("="*80)
print("PERFORMANCE OPTIMIZATION")
print("="*80)

# ============================================================================
# Vectorization Example
# ============================================================================

print("\nVectorization: Eliminate Loops!")
print("="*80)

n = 1000000
arr = np.random.rand(n)

# SLOW: Python loop
print(f"\nProcessing {n:,} elements...")
start = time.time()
result = np.zeros(n)
for i in range(n):
    result[i] = arr[i] ** 2 + 2 * arr[i] + 1
slow_time = time.time() - start

# FAST: Vectorized
start = time.time()
result_fast = arr**2 + 2*arr + 1
fast_time = time.time() - start

print(f"Python loop: {slow_time*1000:.0f} ms")
print(f"Vectorized:  {fast_time*1000:.0f} ms")
print(f"Speedup: {slow_time/fast_time:.0f}x faster!")

print("""
\nWhy vectorized is faster:
1. NumPy uses CPU SIMD instructions
2. No Python interpreter overhead per element
3. Contiguous memory (cache friendly)
4. Optimized C code underneath
""")

# ============================================================================
# Memory Efficiency
# ============================================================================

print("\n" + "="*80)
print("Memory Efficiency (Topic #24)")
print("="*80)

# Use appropriate dtype
arr_default = np.arange(1000)
arr_int16 = np.arange(1000, dtype=np.int16)

print(f"Default int: {arr_default.nbytes:,} bytes")
print(f"int16: {arr_int16.nbytes:,} bytes")
print(f"Savings: {100*(1 - arr_int16.nbytes/arr_default.nbytes):.0f}%")

# Reuse arrays instead of creating new ones
print("\nReuse arrays (avoid allocations):")
result = np.zeros(1000)
for i in range(100):
    result[:] = np.random.rand(1000) * 2  # Reuse memory!
print("  Use arr[:] = ... to reuse memory")

print("""
\n🎯 PERFORMANCE TIPS:
1. Use vectorization (eliminate loops!)
2. Choose appropriate dtype
3. Reuse arrays when possible
4. Use views instead of copies
5. Profile before optimizing!
""")
