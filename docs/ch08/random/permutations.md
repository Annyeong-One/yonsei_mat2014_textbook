# Random Permutations

NumPy provides functions for randomly reordering array elements.


## np.random.shuffle

Shuffles an array in-place, modifying the original.

### 1. Returns None

```python
import numpy as np

def main():
    x = [1, 4, 9, 12, 15]
    result = np.random.shuffle(x)
    print(result)  # None

if __name__ == "__main__":
    main()
```

The function modifies the array in-place and returns `None`.

### 2. List Shuffle

```python
import numpy as np

def main():
    x = [1, 4, 9, 12, 15]
    np.random.shuffle(x)
    print(x)  # Shuffled list

if __name__ == "__main__":
    main()
```

### 3. Array Shuffle

```python
import numpy as np

def main():
    x = np.array([1, 4, 9, 12, 15])
    np.random.shuffle(x)
    print(x)

if __name__ == "__main__":
    main()
```


## 2D Array Shuffle

For multi-dimensional arrays, shuffle operates along the first axis.

### 1. Row Shuffling

```python
import numpy as np

def main():
    x = np.arange(9).reshape((3, 3))
    print("Before shuffle:")
    print(x)
    
    np.random.shuffle(x)
    print("After shuffle:")
    print(x)

if __name__ == "__main__":
    main()
```

### 2. Only First Axis

Rows are permuted, but elements within each row maintain their order.


## np.random.permutation

Returns a permuted copy, leaving the original unchanged.

### 1. From Integer

```python
import numpy as np

def main():
    x = np.random.permutation(10)
    print(x)  # Random permutation of 0-9

if __name__ == "__main__":
    main()
```

### 2. From List

```python
import numpy as np

def main():
    x = [1, 4, 9, 12, 15]
    y = np.random.permutation(x)
    print(y)
    print(x)  # Original unchanged

if __name__ == "__main__":
    main()
```

### 3. From Array

```python
import numpy as np

def main():
    x = np.array([1, 4, 9, 12, 15])
    y = np.random.permutation(x)
    print(y)

if __name__ == "__main__":
    main()
```


## 2D Permutation

Like shuffle, permutation operates along the first axis for 2D arrays.

### 1. Row Permutation

```python
import numpy as np

def main():
    x = np.arange(9).reshape((3, 3))
    y = np.random.permutation(x)
    print(y)

if __name__ == "__main__":
    main()
```

### 2. Non-Destructive

The original array `x` remains unchanged.


## shuffle vs permutation

Choose based on whether you need the original array.

### 1. Use shuffle

When you want to modify the array in-place to save memory.

### 2. Use permutation

When you need to preserve the original array or create an index array.

### 3. Memory Trade-off

`shuffle` is memory-efficient; `permutation` creates a copy.


## Common Applications

Random permutations are essential in many algorithms.

### 1. Data Shuffling

Randomize training data order before each epoch in machine learning.

### 2. Random Sampling

Create random indices for selecting subsets of data.

### 3. A/B Testing

Randomly assign subjects to control and treatment groups.
