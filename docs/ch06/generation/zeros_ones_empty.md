# Zeros, Ones, Empty

NumPy provides efficient functions for creating arrays initialized with specific values or uninitialized memory.


## np.zeros Function

Creates an array filled entirely with zeros.

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.zeros((1, 2, 3))
    print(a)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```

Output:

```
[[[0. 0. 0.]
  [0. 0. 0.]]]
shape: (1, 2, 3)
dtype: float64
```

### 2. Default dtype

The default dtype is `float64`. Specify `dtype=np.int64` for integers.


## np.ones Function

Creates an array filled entirely with ones.

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.ones((1, 2, 3))
    print(a)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```

Output:

```
[[[1. 1. 1.]
  [1. 1. 1.]]]
shape: (1, 2, 3)
dtype: float64
```

### 2. Scaling Pattern

Multiply `np.ones` by a constant to create uniform arrays of any value.


## np.empty Function

Allocates memory without initialization for maximum speed.

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.empty((1, 2, 3))
    print(a)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```

### 2. Caution Required

The values are arbitrary memory contents. Always fill before reading.


## Like Variants

Create arrays matching another array's shape and dtype.

### 1. np.zeros_like

```python
import numpy as np

def main():
    x = np.zeros((1, 2, 3))
    
    a = np.zeros_like(x)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```

### 2. np.ones_like

```python
import numpy as np

def main():
    x = np.zeros((1, 2, 3))
    
    a = np.ones_like(x)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```

### 3. np.empty_like

```python
import numpy as np

def main():
    x = np.zeros((1, 2, 3))
    
    a = np.empty_like(x)
    print(f'shape: {a.shape}')
    print(f'dtype: {a.dtype}')

if __name__ == "__main__":
    main()
```


## Practical Example

Zero-one encoding for detecting repetitive digits in an integer.

### 1. Problem Statement

Check whether a given integer contains any digit more than once.

### 2. Algorithm Design

```python
import numpy as np

def check_repetitive_digits(n):
    seen = np.zeros(10, dtype=np.uint8)
    quotient = n
    while quotient > 0:
        quotient, remainder = quotient // 10, quotient % 10
        if seen[remainder] == 1:
            print(f"{remainder} appears more than once in {n}.")
            break
        else:
            seen[remainder] += 1
    else:
        print(f"{n} has no repetitive digits.")
```

### 3. Example Output

```python
>>> check_repetitive_digits(67827)
7 appears more than once in 67827.

>>> check_repetitive_digits(12345)
12345 has no repetitive digits.
```


## When to Use Each

Choose the right function based on your initialization needs.

### 1. Use np.zeros

When you need guaranteed zero initialization, such as accumulators or counters.

### 2. Use np.ones

When building arrays that will be scaled or used as multiplicative identities.

### 3. Use np.empty

When you will immediately overwrite all values and need maximum allocation speed.
