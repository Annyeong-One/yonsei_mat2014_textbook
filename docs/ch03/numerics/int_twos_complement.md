# Storage & Two's Complement


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Understanding how integers are stored in memory and how negative numbers are represented.

---

## Python Storage

Python integers are stored differently from languages like C.

### 1. Dynamic Typing

Python integers are dynamically typed with no fixed size.

### 2. Arbitrary Precision

Python's `int` type uses a variable-length structure (Big Integer implementation).

### 3. Memory Structure

Python's integer contains:
- Reference count
- Type information
- Actual integer value

In CPython, an `int` is represented as a C struct:

```c
struct _longobject {
    PyObject_VAR_HEAD
    digit ob_digit[1];
};
```

- `PyObject_VAR_HEAD`: Metadata (reference count, type)
- `ob_digit`: Array storing the actual value

---

## C Storage

C integers use fixed-size storage.

### 1. Static Typing

`int` in C is of fixed size, typically **4 bytes (32-bit)** or **8 bytes (64-bit)**.

### 2. Raw Memory

Stored directly in memory without extra overhead.

### 3. C Example

```c
int a = 10; // Typically occupies 4 bytes in memory
```

Stored as binary: `00000000 00000000 00000000 00001010`

---

## Key Differences

Comparison of Python and C integer implementations.

### 1. Comparison Table

| Feature           | Python `int`  | C `int` |
|------------------|--------------|---------|
| **Typing** | Dynamically typed | Statically typed |
| **Size** | Variable-length (arbitrary precision) | Fixed-length (e.g., 4 bytes) |
| **Storage** | Heap-allocated with metadata | Stack/heap-allocated as raw binary |
| **Performance** | Slower due to dynamic handling | Faster due to direct operations |
| **Overflow Handling** | No overflow (can grow infinitely) | Can overflow (limited by size) |
| **Memory Usage** | More overhead (object structure) | Minimal overhead |

### 2. Memory Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sys

# Define a range of large integer values
large_int_values = [10**i for i in range(1, 20)]

# Memory usage for Python int (variable size)
large_python_memory_usage = [sys.getsizeof(i) for i in large_int_values]

# Memory usage for C int (assuming 4 bytes)
large_c_memory_usage = [4] * len(large_int_values)

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot memory usage
ax.plot(large_int_values, large_c_memory_usage, label="C int (4 bytes)", marker="o", linestyle="--")
ax.plot(large_int_values, large_python_memory_usage, label="Python int (variable size)", marker="s", linestyle="-")

# Set log scale for x-axis only
ax.set_xscale("log")

# Set linear scale for y-axis
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())

# Labels and title
ax.set_xlabel("Integer Value")
ax.set_ylabel("Memory Usage (bytes)")
ax.set_title("Memory Usage of int in Python vs. C")

ax.set_ylim( (0, 38) )
ax.legend()

plt.show()
```

---

## Consequences

Understanding the practical implications of these differences.

### 1. Performance Overhead

Python's `int` operations are slower because they involve:
- Memory allocation
- Reference counting
- Dynamic type checking

### 2. Overflow Safety

**Python:** Avoids overflow by automatically expanding size.

```python
a = 2147483647
b = a + 1
print(b)  # No overflow, outputs 2147483648
```

**C:** Fixed size can cause overflow.

```c
#include <stdio.h>

int main() {
    int a = 2147483647; // Maximum 32-bit int
    int b = a + 1; // Causes overflow
    printf("%d\n", b); // Undefined behavior
    return 0;
}
```

### 3. Memory Usage

- **C** is much more memory-efficient (stores only the raw value)
- **Python** requires more memory due to object overhead

### 4. Use Cases

- **C**: Performance-critical applications (system programming, embedded systems)
- **Python**: Large numbers, dynamic typing beneficial (scientific computing, cryptography)

---

## Two's Complement

Two's complement is the standard method for representing signed integers in binary.

### 1. Definition

In an **N-bit** system:
- **Most significant bit (MSB)** is the sign bit:
  - `0` = positive
  - `1` = negative
- Positive numbers: standard binary
- Negative numbers: invert all bits and add 1

### 2. Example (8-bit)

**Positive Number (5):**

```
00000101  (Binary for 5)
```

**Negative Number (-5):**

1. Binary of `5`: `00000101`
2. Invert bits: `11111010`
3. Add `1`: `11111011`

Thus, `11111011` represents `-5` in two's complement.

### 3. Logic Behind MSB

The MSB contributes a large negative weight.

In 8-bit:
- MSB in `11111011` has weight `-128`
- Remaining bits: `64 + 32 + 16 + 8 + 2 + 1 = 123`
- Total: `-128 + 123 = -5`

### 4. Range (N-bit)

For an N-bit system:

$$
-2^{(N-1)} \text{ to } 2^{(N-1)} - 1
$$

For 8-bit:

$$
-128 \text{ to } 127
$$

---

## Python Representation

Python does not use two's complement internally.

### 1. Sign-Magnitude

Python uses sign-magnitude with arbitrary-length representation, not two's complement.

### 2. Comparison

| Feature | Two's Complement | Python's Integer |
|---------|----------------|--------------------|
| Fixed Bit-Length | Yes (e.g., 8-bit, 16-bit) | No (arbitrary precision) |
| Negative Representation | MSB indicates sign, bitwise inversion + 1 | Sign-magnitude with arbitrary-length |
| Overflow | Yes (limited by bit-width) | No (expands dynamically) |
| Arithmetic Simplicity | Simple addition/subtraction | Slightly more overhead |

### 3. Does Python Use Two's Complement?

**Answer:** No, Python does not use two's complement for representing negative integers. Python uses a sign-magnitude representation.

**Sign-magnitude representation:**
- Leftmost bit indicates sign: `0` for positive, `1` for negative
- Remaining bits represent the magnitude

Example with 8-bit integers:
- Positive 5: `00000101`
- Negative 5: `10000101`

**Two's complement (used in C/C++):**
- Negative numbers are represented by inverting bits and adding 1
- Simplifies arithmetic operations
- No separate sign bit needed

Python's approach maintains human-readability and avoids hardware-level complexities, though two's complement remains crucial for low-level systems.

[ChatGPT](https://openai.com/blog/chatgpt)

---

## Pros and Cons

Evaluating the trade-offs of each representation.

### 1. Two's Complement

**Pros:**
- Simple arithmetic operations
- Efficient in hardware with fixed bit-width
- Single representation for zero

**Cons:**
- Overflow issues due to fixed bit-width
- Limited range of values

### 2. Python's Approach

**Pros:**
- No overflow due to dynamic sizing
- Handles very large numbers

**Cons:**
- Slightly higher memory usage
- More computational overhead

---

## Conclusion

**C `int`** is faster and memory-efficient but suffers from fixed size and overflow issues.

**Python `int`** is slower and consumes more memory but is safe from overflow and supports arbitrary precision.

**Trade-off:** C is better for efficiency, while Python is better for flexibility and safety.

Two's complement remains crucial for low-level systems and embedded computing, while Python's approach is advantageous for applications requiring precision without fixed bit-width constraints.
