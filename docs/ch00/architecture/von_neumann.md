# Von Neumann Architecture

The Von Neumann architecture is the foundational design for nearly all modern computers. Understanding it explains why memory access dominates performance and why NumPy arrays are faster than Python lists.

## Definition

The **Von Neumann architecture** is a stored-program computer model where program instructions and data share the same memory space. A Von Neumann machine consists of a CPU (control unit, ALU, registers), memory, I/O devices, and a bus system connecting them.

The **Von Neumann bottleneck** arises because instructions and data compete for the same memory channel, causing the CPU to stall waiting for data as processor speeds outpace memory speeds.

## Explanation

Programs execute through the **fetch-decode-execute-writeback** cycle. The CPU fetches an instruction from the address in the Program Counter, decodes it, executes it via the ALU, and writes the result back to registers or memory. This repeats until the program terminates.

The bus system has three parts: the **address bus** (CPU specifies which memory location), the **data bus** (bidirectional data transfer), and the **control bus** (timing and coordination signals).

To mitigate the Von Neumann bottleneck, modern systems use a **memory hierarchy** -- registers (~1 cycle), L1 cache (~4 cycles), L2 cache (~12 cycles), L3 cache (~40 cycles), RAM (~200 cycles), SSD/disk (~100,000+ cycles). This hierarchy exploits **temporal locality** (reusing recent data) and **spatial locality** (accessing nearby addresses).

Most modern CPUs use a **modified Harvard architecture**: main memory is unified, but separate L1 instruction and data caches allow parallel access, reducing the bottleneck while preserving the stored-program model.

**Python implication**: Python lists store scattered heap objects (pointer chasing defeats cache locality). NumPy arrays store contiguous raw values, exploiting spatial locality and enabling efficient cache prefetching.

## Examples

```python
import sys

# Every Python integer is a full heap object with metadata
x = 42
print(sys.getsizeof(x))  # 28 bytes (reference count + type + value)
```

```python
import numpy as np

# NumPy: contiguous memory block -- cache-friendly
arr = np.zeros(1_000_000)

# Python list: scattered objects -- poor cache locality
lst = [0.0] * 1_000_000

print(sys.getsizeof(arr))                    # ~8 MB (raw data)
print(sys.getsizeof(lst) + 1_000_000 * 28)   # ~36 MB (pointers + objects)
```

```python
import numpy as np
import time

# Demonstrating the memory locality advantage
n = 1_000_000
arr = np.arange(n, dtype=np.float64)
lst = list(range(n))

start = time.perf_counter()
_ = np.sum(arr)
print(f"NumPy sum: {time.perf_counter() - start:.4f}s")

start = time.perf_counter()
_ = sum(lst)
print(f"List sum:  {time.perf_counter() - start:.4f}s")
```
