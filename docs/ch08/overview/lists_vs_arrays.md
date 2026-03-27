# Lists vs Arrays

## Performance

### 1. Speed Comparison

```python
import numpy as np
import time

n = 1000000

# Python list
x_list = list(range(n))
start = time.time()
y_list = [xi**2 for xi in x_list]
list_time = time.time() - start

# NumPy array
x_array = np.arange(n)
start = time.time()
y_array = x_array**2
array_time = time.time() - start

print(f"List: {list_time:.3f}s")
print(f"Array: {array_time:.3f}s")
print(f"Speedup: {list_time/array_time:.1f}x")
```

### 2. Memory

```python
import sys

# List overhead
lst = [1, 2, 3, 4, 5]
print(sys.getsizeof(lst))  # 104 bytes

# Array efficiency
arr = np.array([1, 2, 3, 4, 5])
print(arr.nbytes)  # 40 bytes (8 bytes × 5)
```

### 3. Operations

```python
# List - element-wise requires loop
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
result = [a + b for a, b in zip(lst1, lst2)]

# Array - vectorized
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2  # Fast, single operation
```

## Type Flexibility

### 1. Lists - Heterogeneous

```python
mixed = [1, 'hello', 3.14, [1, 2], {'key': 'value'}]
```

### 2. Arrays - Homogeneous

```python
arr = np.array([1, 2, 3])  # All int64
# arr = np.array([1, 'hello'])  # Converts all to str
```

### 3. Trade-offs

Lists: Flexible but slow
Arrays: Fast but rigid types

## Use Cases

### 1. Use Lists When

- Heterogeneous data
- Dynamic resizing
- General collections
- Small datasets

### 2. Use Arrays When

- Numerical computation
- Linear algebra
- Large datasets
- Performance critical

### 3. Example

```python
# List - collection
students = ['Alice', 'Bob', 'Charlie']

# Array - numerical data
scores = np.array([85, 92, 78])
mean_score = scores.mean()
```

---

## Runnable Example: `arrays_vs_lists_tutorial.py`

```python
"""
01_arrays_vs_lists.py - Why NumPy? Memory and Performance

🔗 CRITICAL CONNECTIONS:
- Topic #24: Memory Deep Dive (contiguous memory, views vs copies)
- Topic #25: List Internals (over-allocation, pointer overhead)

This tutorial shows WHY NumPy exists and connects to previous memory topics!
"""

import numpy as np
import sys
import time

if __name__ == "__main__":

    print("="*80)
    print("NUMPY VS PYTHON LISTS: MEMORY & PERFORMANCE")
    print("="*80)
    print("\n🔗 Connects to: Topic #24 (Memory) & Topic #25 (Lists)")

    # ============================================================================
    # SECTION 1: Review Python List Internals (Topic #25)
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 1: Python List Memory Layout (Review Topic #25)")
    print("="*80)

    print("""
    FROM TOPIC #25 - Python List Internals:
    ---------------------------------------
    Lists are arrays of POINTERS to PyObjects:

    python_list = [1, 2, 3]

    Memory Structure:
      List object: 56+ bytes (header)
      Pointer array: 8 bytes × capacity
      Each integer: 28+ bytes (PyObject overhead!)

    Over-allocation: Lists allocate MORE space than needed
      - Avoid frequent reallocations
      - But wastes memory!

    Result: ~100+ bytes for just 3 integers!
    """)

    # Demonstrate list memory
    python_list = [1, 2, 3]
    print(f"Python list [1,2,3]: {sys.getsizeof(python_list)} bytes")
    print("(Plus ~84 bytes for the integer objects themselves)")

    # Show over-allocation
    empty = []
    print(f"\nEmpty list: {sys.getsizeof(empty)} bytes")
    for i in range(1, 11):
        empty.append(i)
        capacity = (sys.getsizeof(empty) - 56) // 8
        print(f"  After {i:2} appends: {sys.getsizeof(empty):3}B (capacity: {capacity})")

    print("\nNotice the JUMPS? That's over-allocation!")

    # ============================================================================
    # SECTION 2: NumPy's Contiguous Memory (Topic #24)
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 2: NumPy's Contiguous Memory (Topic #24)")
    print("="*80)

    print("""
    FROM TOPIC #24 - NumPy uses CONTIGUOUS memory:
    ----------------------------------------------
    NumPy arrays store data in a SINGLE memory block:

    numpy_array = np.array([1, 2, 3], dtype=np.int32)

    Memory Structure:
      Array metadata: Small overhead
      Data buffer: [1][2][3] ← Contiguous!
      Each integer: 4 bytes (no PyObject!)

    Total: ~12 bytes for 3 integers

    Benefits (Topic #24):
    1. Cache-friendly: CPU loads multiple elements
    2. Fast iteration: Sequential memory access  
    3. No pointer chasing
    4. Vectorization possible (SIMD instructions)
    """)

    arr = np.array([1, 2, 3], dtype=np.int32)
    print(f"NumPy array [1,2,3] (int32): {arr.nbytes} bytes")
    print(f"Memory efficiency: {sys.getsizeof(python_list) / arr.nbytes:.1f}x better!")

    # ============================================================================
    # SECTION 3: Memory Comparison at Scale
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 3: Memory Comparison (10,000 elements)")
    print("="*80)

    size = 10000
    py_list = list(range(size))
    np_arr_i8 = np.arange(size, dtype=np.int8)
    np_arr_i32 = np.arange(size, dtype=np.int32)
    np_arr_i64 = np.arange(size, dtype=np.int64)

    print(f"\nPython List:")
    print(f"  Structure: {sys.getsizeof(py_list):,} bytes")
    print(f"  Est. total: ~{sys.getsizeof(py_list) + 28*size:,} bytes\n")

    print(f"NumPy Arrays (same data):")
    print(f"  int8:  {np_arr_i8.nbytes:,} bytes (1 byte/element)")
    print(f"  int32: {np_arr_i32.nbytes:,} bytes (4 bytes/element)")  
    print(f"  int64: {np_arr_i64.nbytes:,} bytes (8 bytes/element)")

    efficiency = (sys.getsizeof(py_list) + 28*size) / np_arr_i64.nbytes
    print(f"\nNumPy is ~{efficiency:.1f}x more memory efficient!")

    # ============================================================================
    # SECTION 4: Speed Comparison
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 4: Speed Benchmarks")
    print("="*80)

    size = 100000
    py_list = list(range(size))
    np_arr = np.arange(size)

    # Test 1: Multiplication
    print("\nTEST 1: Multiply all elements by 2")
    t1 = time.time()
    result = [x * 2 for x in py_list]
    list_time = time.time() - t1

    t2 = time.time()
    result = np_arr * 2
    numpy_time = time.time() - t2

    print(f"  Python list: {list_time*1000:.2f} ms")
    print(f"  NumPy array: {numpy_time*1000:.2f} ms")
    print(f"  Speedup: {list_time/numpy_time:.0f}x faster!\n")

    print("  Why? Vectorization!")
    print("  - NumPy uses CPU SIMD instructions")
    print("  - No Python interpreter per element")
    print("  - Contiguous memory = cache friendly")

    # Test 2: Sum
    print("\nTEST 2: Sum all elements")
    t1 = time.time()
    result = sum(py_list)
    list_time = time.time() - t1

    t2 = time.time()
    result = np_arr.sum()
    numpy_time = time.time() - t2

    print(f"  Python sum(): {list_time*1000:.2f} ms")
    print(f"  NumPy .sum(): {numpy_time*1000:.2f} ms")
    print(f"  Speedup: {list_time/numpy_time:.0f}x faster!")

    # ============================================================================
    # SECTION 5: When to Use Each
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 5: Lists vs Arrays - Decision Guide")
    print("="*80)

    print("""
    USE PYTHON LISTS WHEN:
    ✓ Heterogeneous data (mixed types)
      Example: ['Alice', 42, 3.14, True]
    ✓ Small datasets (<1000 elements)
    ✓ Need dynamic resizing frequently
    ✓ General-purpose collections

    USE NUMPY ARRAYS WHEN:
    ✓ Large numerical datasets (>1000 elements)  
    ✓ Homogeneous data (same type)
    ✓ Need mathematical operations
    ✓ Performance is critical
    ✓ Memory efficiency matters
    """)

    # ============================================================================
    # SECTION 6: Homogeneous vs Heterogeneous
    # ============================================================================

    print("\n" + "="*80)
    print("SECTION 6: Homogeneous Constraint - The Trade-off")
    print("="*80)

    print("\nPython lists: Flexible (heterogeneous)")
    py_list = [1, 'two', 3.0, True, None]
    print(f"  {py_list}")
    print(f"  Types: {[type(x).__name__ for x in py_list]}")

    print("\nNumPy arrays: Restricted (homogeneous)")
    arr = np.array([1, 2, 3.5, 4])
    print(f"  From [1, 2, 3.5, 4]: {arr}")
    print(f"  dtype: {arr.dtype} ← All converted to float!")

    arr_str = np.array([1, 'two', 3])
    print(f"  From [1, 'two', 3]: {arr_str}")  
    print(f"  dtype: {arr_str.dtype} ← All converted to strings!")

    print("""
    KEY PRINCIPLE:
      Lists: Flexibility over performance
      Arrays: Performance over flexibility
    """)

    # ============================================================================
    # SUMMARY
    # ============================================================================

    print("\n" + "="*80)
    print("SUMMARY - KEY TAKEAWAYS")
    print("="*80)

    print("""
    1. MEMORY (connects to #24, #25):
       - Lists: Scattered, with PyObject overhead
       - Arrays: Contiguous, no per-element overhead
       - Arrays are 8-10x more memory efficient

    2. PERFORMANCE:
       - Arrays are 50-200x faster for math operations
       - Reason: Contiguous memory + vectorization + SIMD

    3. TRADE-OFF:
       - Lists: Flexible (any type) but slower
       - Arrays: Restricted (one type) but MUCH faster

    4. WHEN TO USE NUMPY:
       ✓ Large numerical data (>1000 elements)
       ✓ Math operations
       ✓ Performance/memory critical

    5. PREPARES FOR:
       - Pandas (Topic #40): Built on NumPy!
       - All data science in Python

    🔜 NEXT: 02_array_creation.py
    """)
```
