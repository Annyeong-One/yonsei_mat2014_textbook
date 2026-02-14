"""
01_list_internals.py

TOPIC: Python List Implementation Internals
LEVEL: Advanced
DURATION: 60-75 minutes

PREREQUISITES:
- Topic #24: Memory Deep Dive (mutable types, references, memory management)

LEARNING OBJECTIVES:
1. Understand list memory layout
2. Learn about over-allocation strategy
3. Explore capacity vs length
4. Understand why lists are fast for certain operations

This is ADVANCED implementation details - builds on memory concepts from #24
"""

import sys

print("=" * 70)
print("PYTHON LIST INTERNALS")
print("=" * 70)

# ============================================================================
# SECTION 1: List Memory Layout
# ============================================================================

print("\nSECTION 1: How Lists Are Structured")
print("-" * 70)

print("""
PYTHON LIST STRUCTURE (CPython):

┌─────────────────────────────────────────┐
│ PyListObject                            │
├─────────────────────────────────────────┤
│ ob_refcnt: reference count              │
│ ob_type: pointer to list type           │
│ ob_size: number of elements (LENGTH)    │  ← What len() returns
│ allocated: capacity (slots)             │  ← Total allocated space
│ ob_item: pointer to array of pointers   │  ← Points to actual data
└─────────────────────────────────────────┘
           │
           ↓
    ┌──────────────────────┐
    │ Array of Pointers    │
    ├──────────────────────┤
    │ [0] → Object 1       │
    │ [1] → Object 2       │
    │ [2] → Object 3       │
    │ [3] → Object 4       │
    │ [4] → (unused)       │  ← OVER-ALLOCATION
    │ [5] → (unused)       │  ← Extra capacity
    └──────────────────────┘

KEY INSIGHT:
- Lists store POINTERS to objects, not objects themselves
- ob_size (length) ≤ allocated (capacity)
- Extra capacity allows fast appends!
""")

# ============================================================================
# SECTION 2: Length vs Capacity
# ============================================================================

print("\nSECTION 2: Length vs Capacity")
print("-" * 70)

# Create empty list
my_list = []
print(f"Empty list: {my_list}")
print(f"  len() = {len(my_list)}")  # ob_size
print(f"  sys.getsizeof() = {sys.getsizeof(my_list)} bytes")  # includes allocated capacity

# Add one element
my_list.append(1)
print(f"\nAfter append(1): {my_list}")
print(f"  len() = {len(my_list)}")
print(f"  sys.getsizeof() = {sys.getsizeof(my_list)} bytes")

# Add more elements
sizes = [sys.getsizeof([])]
for i in range(2, 20):
    my_list.append(i)
    size = sys.getsizeof(my_list)
    if size > sizes[-1]:
        print(f"\nAfter append({i}): len={len(my_list)}, size={size} bytes (RESIZED!)")
        sizes.append(size)
    else:
        print(f"After append({i}): len={len(my_list)}, size={size} bytes")

print("""
OBSERVATIONS:
- Size doesn't increase with EVERY append
- Size increases in JUMPS (when capacity is exceeded)
- This is OVER-ALLOCATION strategy
- Trade-off: waste some memory for faster appends
""")

# ============================================================================
# SECTION 3: Over-Allocation Strategy
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 3: Why Over-Allocation?")
print("-" * 70)

print("""
WITHOUT OVER-ALLOCATION (naive approach):
───────────────────────────────────────
lst = []           # Allocate 0 slots
lst.append(1)      # Allocate 1 slot, copy 0 items
lst.append(2)      # Allocate 2 slots, copy 1 item
lst.append(3)      # Allocate 3 slots, copy 2 items
lst.append(4)      # Allocate 4 slots, copy 3 items
...
lst.append(n)      # Allocate n slots, copy n-1 items

Total copies: 0 + 1 + 2 + ... + (n-1) = O(n²)  ← TERRIBLE!

WITH OVER-ALLOCATION (Python's approach):
───────────────────────────────────────
lst = []           # Allocate 0 slots
lst.append(1)      # Allocate 4 slots (over-allocate!)
lst.append(2)      # Use existing capacity
lst.append(3)      # Use existing capacity
lst.append(4)      # Use existing capacity
lst.append(5)      # Allocate 8 slots, copy 4 items
lst.append(6)      # Use existing capacity
...

Total copies: Much fewer! = O(n)  ← MUCH BETTER!

GROWTH PATTERN (approximately):
0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...

Formula (approximately): new_capacity = old_capacity + (old_capacity >> 3) + 6
Which is roughly: new_capacity ≈ 1.125 * old_capacity + 6
""")

# ============================================================================
# SECTION 4: Performance Implications
# ============================================================================

print("\nSECTION 4: Performance Analysis")
print("-" * 70)

print("""
OPERATION PERFORMANCE:

FAST (O(1) amortized):
✓ append() - usually fits in capacity
✓ Access by index: lst[i]
✓ Modify by index: lst[i] = x
✓ len(lst)
✓ pop() - remove last element

SLOW (O(n)):
✗ insert(0, x) - shift all elements right
✗ pop(0) - shift all elements left
✗ remove(x) - search then shift
✗ Concatenation: lst1 + lst2

WHY append() is O(1) amortized:
- Most appends use existing capacity: O(1)
- Occasional resize: O(n)
- But resizes become increasingly rare
- Average over many operations: O(1)
""")

# Demonstrate fast append
import time

n = 100000
start = time.time()
test_list = []
for i in range(n):
    test_list.append(i)
append_time = time.time() - start

print(f"\nAppending {n} elements: {append_time:.4f} seconds")
print(f"Average per append: {append_time/n*1000000:.2f} microseconds")

# ============================================================================
# SECTION 5: Memory Trade-offs
# ============================================================================

print("\n" + "=" * 70)
print("SECTION 5: Memory Trade-offs")
print("-" * 70)

# Show wasted space
test_list = list(range(100))
actual_size = sys.getsizeof(test_list)
ptr_size = 8  # 64-bit system
base_size = sys.getsizeof([])
used_size = base_size + (100 * ptr_size)

print(f"List with 100 elements:")
print(f"  Total memory: {actual_size} bytes")
print(f"  Base overhead: {base_size} bytes")
print(f"  Used for data: {100 * ptr_size} bytes (100 pointers × 8 bytes)")
print(f"  Estimated waste: {actual_size - used_size} bytes (~{(actual_size-used_size)/actual_size*100:.1f}%)")

print("""
TRADE-OFF:
- Waste ~10-30% of memory (varies with size)
- Gain O(1) amortized append performance
- For most applications: speed > memory

WHEN TO CARE:
- Creating MANY small lists → use tuples if immutable
- Memory-constrained environments
- Lists that rarely grow after creation
""")

# ============================================================================
# SECTION 6: Practical Implications
# ============================================================================

print("\nSECTION 6: Practical Programming Implications")
print("-" * 70)

print("""
BEST PRACTICES:

1. Pre-allocate if you know size:
   ✓ lst = [None] * 1000  # Better than 1000 appends

2. Use list comprehensions:
   ✓ [x**2 for x in range(1000)]  # Optimized

3. Avoid repeated insertions at beginning:
   ✗ for x in data: lst.insert(0, x)  # O(n²)
   ✓ Use collections.deque for queue operations

4. Don't pre-allocate unnecessarily:
   ✗ lst = [None] * 1000000  # Wastes memory if not all used

5. Concatenation alternatives:
   ✗ result = []
      for lst in many_lists:
          result = result + lst  # Creates new list each time!
   ✓ result = []
      for lst in many_lists:
          result.extend(lst)  # Modifies in place
""")

# ============================================================================
# SECTION 7: Comparison to Other Data Structures
# ============================================================================

print("\nSECTION 7: When NOT to Use Lists")
print("-" * 70)

print("""
USE THESE INSTEAD:

collections.deque:
- Fast O(1) operations at both ends
- Use for queues, stacks
- Slower random access

array.array:
- Compact storage for numeric data
- No over-allocation waste
- Only homogeneous types

numpy.ndarray:
- Multi-dimensional arrays
- Vectorized operations
- Scientific computing

tuple:
- Immutable, no over-allocation
- Slightly faster, less memory
- Use when size fixed
""")

# ============================================================================
# SECTION 8: Key Takeaways
# ============================================================================

print("\nKEY TAKEAWAYS")
print("-" * 70)

print("""
1. Lists use OVER-ALLOCATION for performance
2. Length (ob_size) ≤ Capacity (allocated)
3. append() is O(1) amortized due to over-allocation
4. Occasional resize operations are O(n)
5. Growth pattern: ~1.125x + constant
6. Trades memory (10-30% waste) for speed
7. insert(0) and pop(0) are O(n) - avoid for queues
8. Pre-allocate if size known
9. Use deque for queue operations
10. Understanding internals helps choose right data structure

CONNECTS TO #24 MEMORY CONCEPTS:
- Mutable type behavior
- Reference storage
- Memory allocation patterns
- Performance vs memory trade-offs
""")

print("\nSee exercises.py for practice!")
