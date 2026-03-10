# CPU Basics

The Central Processing Unit executes every instruction your program generates. Understanding its core components explains why Python is slower per operation than C and why libraries like NumPy exist.

## Definition

The **CPU (Central Processing Unit)** is the hardware component that fetches, decodes, and executes machine instructions. Its architecture is defined at two levels:

- **ISA (Instruction Set Architecture)**: The software-visible interface -- registers, instructions, and memory model (e.g., x86-64, ARM).
- **Microarchitecture**: The hardware implementation -- pipelines, caches, branch predictors, and execution units.

## Explanation

Every instruction follows the **fetch-decode-execute-writeback** cycle. Modern CPUs expand this into 10-20+ pipeline stages and overlap many instructions simultaneously:

1. **Fetch**: Read the next instruction from the instruction cache.
2. **Decode**: Determine the operation and operands.
3. **Execute**: Perform computation via the ALU or other execution units.
4. **Writeback/Retire**: Commit results in program order.

The three core components in the classical model are:

| Component | Role |
|-----------|------|
| **Control Unit** | Orchestrates fetching, decoding, and dispatching |
| **ALU** | Performs arithmetic, logic, comparison, and bit-shift operations |
| **Registers** | Fastest storage (sub-nanosecond access), located inside the CPU |

CPUs access data through a memory hierarchy with increasing latency: L1 cache (~4 cycles), L2 (~12 cycles), L3 (~40 cycles), and RAM (~200 cycles). This gap explains why cache-friendly access patterns dramatically improve performance.

Python adds overhead because each operation (e.g., `x = a + b`) involves dictionary lookups, type checks, object allocation, and reference counting -- potentially thousands of machine instructions. NumPy bypasses this by delegating computation to compiled C code operating on contiguous arrays with SIMD instructions.

## Examples

```python
# A simple addition in Python triggers many CPU operations:
# 1. Namespace lookup for a and b
# 2. Type checking at runtime
# 3. Calling __add__ method
# 4. Heap allocation for the result object
# 5. Reference count updates
x = a + b  # In C, this would be a single ADD instruction
```

```python
import numpy as np

# NumPy moves the loop into compiled C with SIMD instructions
arr1 = np.array([1.0, 2.0, 3.0, 4.0])
arr2 = np.array([5.0, 6.0, 7.0, 8.0])
result = np.add(arr1, arr2)  # Single Python call, vectorized CPU execution
print(result)  # [6. 8. 10. 12.]
```
