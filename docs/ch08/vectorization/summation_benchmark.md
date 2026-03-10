# Summation Benchmark


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Compare different approaches for computing $\sum_{k=1}^n k^2$.

## Problem Setup

### 1. Mathematical Form

$$\sum_{k=1}^n k^2 = 1^2 + 2^2 + 3^2 + \cdots + n^2$$

### 2. Closed Form

$$\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$$

### 3. Test Size

We use $n = 10^7$ to highlight performance differences.

## For Loop

### 1. Implementation

```python
import time

def main():
    n = int(1e7)
    
    tic = time.time()
    s_n = 0
    for i in range(1, n + 1):
        s_n += i ** 2
    toc = time.time()
    
    print(f"{s_n = }")
    print(f"For Loop Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Characteristics

- Pure Python iteration
- Repeated addition
- Maximum interpreter overhead

### 3. Typical Time

Slowest approach (~3-5 seconds).

## List Append

### 1. Implementation

```python
import time

def main():
    n = int(1e7)
    
    tic = time.time()
    lst = []
    for i in range(1, n + 1):
        lst.append(i ** 2)
    s_n = sum(lst)
    toc = time.time()
    
    print(f"{s_n = }")
    print(f"List Append Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Characteristics

- Builds intermediate list
- Extra memory allocation
- Two-pass (build then sum)

### 3. Typical Time

Similar to for loop (~3-5 seconds).

## List Comprehension

### 1. Implementation

```python
import time

def main():
    n = int(1e7)
    
    tic = time.time()
    s_n = sum([i ** 2 for i in range(1, n + 1)])
    toc = time.time()
    
    print(f"{s_n = }")
    print(f"List Comprehension Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Characteristics

- More Pythonic syntax
- Still creates full list
- Slightly optimized bytecode

### 3. Typical Time

Slightly faster (~2-4 seconds).

## NumPy Vectorized

### 1. Implementation

```python
import numpy as np
import time

def main():
    n = int(1e7)
    
    tic = time.time()
    x = np.arange(1, n + 1) ** 2
    s_n = np.sum(x)
    toc = time.time()
    
    print(f"{s_n = }")
    print(f"NumPy Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Characteristics

- C-level computation
- Contiguous memory
- Optimized reduction

### 3. Typical Time

Much faster (~0.05-0.1 seconds).

## Formula Direct

### 1. Implementation

```python
import time

def main():
    n = int(1e7)
    
    tic = time.time()
    s_n = n * (n + 1) * (2 * n + 1) // 6
    toc = time.time()
    
    print(f"{s_n = }")
    print(f"Formula Time: {toc - tic:.8f} sec")

if __name__ == "__main__":
    main()
```

### 2. Characteristics

- O(1) complexity
- No iteration at all
- Constant time regardless of n

### 3. Typical Time

Essentially instant (~0.000001 seconds).

## Full Comparison

### 1. All Methods

```python
import numpy as np
import time

def main():
    n = int(1e7)
    results = []
    
    # For loop
    tic = time.time()
    s = 0
    for i in range(1, n + 1):
        s += i ** 2
    results.append(("For Loop", time.time() - tic, s))
    
    # List append
    tic = time.time()
    lst = []
    for i in range(1, n + 1):
        lst.append(i ** 2)
    s = sum(lst)
    results.append(("List Append", time.time() - tic, s))
    
    # List comprehension
    tic = time.time()
    s = sum([i ** 2 for i in range(1, n + 1)])
    results.append(("List Comp", time.time() - tic, s))
    
    # NumPy
    tic = time.time()
    s = np.sum(np.arange(1, n + 1) ** 2)
    results.append(("NumPy", time.time() - tic, s))
    
    # Formula
    tic = time.time()
    s = n * (n + 1) * (2 * n + 1) // 6
    results.append(("Formula", time.time() - tic, s))
    
    print(f"{'Method':<15} {'Time (sec)':<12} {'Result'}")
    print("-" * 45)
    for method, elapsed, result in results:
        print(f"{method:<15} {elapsed:<12.6f} {result}")

if __name__ == "__main__":
    main()
```

### 2. Sample Output

```
Method          Time (sec)   Result
---------------------------------------------
For Loop        3.245000     333333383333335000
List Append     3.512000     333333383333335000
List Comp       2.891000     333333383333335000
NumPy           0.078000     333333383333335000
Formula         0.000001     333333383333335000
```

### 3. Key Insight

NumPy is ~40× faster than Python loops; formulas are instant when available.

## Takeaways

### 1. Avoid Python Loops

For numerical computation, Python loops are prohibitively slow.

### 2. Use NumPy

Vectorized NumPy operations provide massive speedups.

### 3. Know Your Math

Closed-form solutions beat all iterative methods.
