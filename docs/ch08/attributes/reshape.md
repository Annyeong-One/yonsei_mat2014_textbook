# Reshaping Arrays

Reshaping changes an array's dimensions while preserving its data.


## Method reshape

The `reshape` method returns a new view with the specified shape.

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x.shape = }")
    print(x, end="\n\n")

    y = x.reshape((3, 2))
    print(f"{y.shape = }")
    print(y)

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (6,)
[0 1 2 3 4 5]

y.shape = (3, 2)
[[0 1]
 [2 3]
 [4 5]]
```

### 2. Total Size Rule

The product of new dimensions must equal the original total size.


## Function np.reshape

The `np.reshape` function provides the same functionality.

### 1. Function Syntax

```python
import numpy as np

def main():
    x = np.arange(6)
    print(f"{x.shape = }")
    print(x, end="\n\n")

    y = np.reshape(x, (3, 2))
    print(f"{y.shape = }")
    print(y)

if __name__ == "__main__":
    main()
```

### 2. Method vs Function

Both are equivalent; the method syntax is more common.


## The -1 Wildcard

Using `-1` lets NumPy infer one dimension automatically.

### 1. Flatten to 1D

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    y = x.reshape((-1,))
    print(f"{x.shape = }")
    print(f"{y.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
y.shape = (24,)
```

### 2. Keep First Axis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    z = x.reshape((2, -1))
    print(f"{x.shape = }")
    print(f"{z.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
z.shape = (2, 12)
```

### 3. Keep Last Axis

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    w = x.reshape((-1, 4))
    print(f"{x.shape = }")
    print(f"{w.shape = }")

if __name__ == "__main__":
    main()
```

Output:

```
x.shape = (2, 3, 4)
w.shape = (6, 4)
```


## Multiple Examples

Combining all `-1` examples in one block.

### 1. All Together

```python
import numpy as np

def main():
    x = np.zeros((2, 3, 4))
    y = x.reshape((-1,))
    z = x.reshape((2, -1))
    w = x.reshape((-1, 4))
    print(f"{x.shape = }")
    print(f"{y.shape = }")
    print(f"{z.shape = }")
    print(f"{w.shape = }")

if __name__ == "__main__":
    main()
```

### 2. Only One -1

You can only use `-1` for a single dimension per reshape call.

---

## Runnable Example: `shape_manipulation_tutorial.py`

```python
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
```
