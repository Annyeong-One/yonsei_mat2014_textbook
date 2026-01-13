# Diagonal Matrices

The `np.diag` function provides bidirectional conversion between diagonal components and diagonal matrices.


## Core Concept

`np.diag` works in two directions depending on input dimensionality.

$$
\text{diagonal components}
\quad\stackrel{\text{np.diag}}{\longleftrightarrow}\quad
\text{diagonal matrix}
$$


## Components to Matrix

Convert a 1D array of diagonal values into a 2D diagonal matrix.

### 1. Basic Conversion

```python
import numpy as np

def main():
    a = np.diag([1, 2, 3])
    print("np.diag([1, 2, 3])")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.diag([1, 2, 3])
[[1 0 0]
 [0 2 0]
 [0 0 3]]
```

### 2. Input Requirements

The input must be a 1D array or list of diagonal values.


## Diagonal Offset

The `k` parameter shifts the diagonal position.

### 1. Main Diagonal

```python
import numpy as np

def main():
    a = np.diag([1, 2, 3])
    print("np.diag([1, 2, 3])")
    print(a)

if __name__ == "__main__":
    main()
```

Default `k=0` places values on the main diagonal.

### 2. Upper Diagonals

```python
import numpy as np

def main():
    a = np.diag([1, 2, 3], k=1)
    print("np.diag([1, 2, 3], k=1)")
    print(a)
    
    a = np.diag([1, 2, 3], k=2)
    print("np.diag([1, 2, 3], k=2)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.diag([1, 2, 3], k=1)
[[0 1 0 0]
 [0 0 2 0]
 [0 0 0 3]
 [0 0 0 0]]

np.diag([1, 2, 3], k=2)
[[0 0 1 0 0]
 [0 0 0 2 0]
 [0 0 0 0 3]
 [0 0 0 0 0]
 [0 0 0 0 0]]
```

### 3. Lower Diagonals

```python
import numpy as np

def main():
    a = np.diag([1, 2, 3], k=-1)
    print("np.diag([1, 2, 3], k=-1)")
    print(a)
    
    a = np.diag([1, 2, 3], k=-2)
    print("np.diag([1, 2, 3], k=-2)")
    print(a)

if __name__ == "__main__":
    main()
```

Negative `k` shifts the diagonal below the main diagonal.


## Matrix to Components

Extract diagonal values from a 2D matrix.

### 1. Extract Main Diagonal

```python
import numpy as np

def main():
    A = np.array([[1, 4, 0],
                  [0, 2, 5],
                  [0, 0, 3]])
    
    print(f'{np.diag(A) = }')

if __name__ == "__main__":
    main()
```

Output:

```
np.diag(A) = array([1, 2, 3])
```

### 2. Extract Off-Diagonals

```python
import numpy as np

def main():
    A = np.array([[1, 4, 0],
                  [0, 2, 5],
                  [0, 0, 3]])
    
    print(f'{np.diag(A, k=1) = }')
    print(f'{np.diag(A, k=-1) = }')

if __name__ == "__main__":
    main()
```

Output:

```
np.diag(A, k=1) = array([4, 5])
np.diag(A, k=-1) = array([0, 0])
```


## Visual Geometry

Diagonal matrices have a distinctive visual pattern.

### 1. Visualization Code

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    a = np.diag(range(15))
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(a, cmap='Blues')
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Pattern Recognition

Non-zero values appear only along a single diagonal line.


## Linear Algebra Role

Diagonal matrices have special computational properties.

### 1. Easy Inversion

The inverse of a diagonal matrix is simply the reciprocal of each diagonal element.

### 2. Eigenvalues

The eigenvalues of a diagonal matrix are its diagonal elements.

### 3. Matrix Powers

$D^n$ is computed by raising each diagonal element to the $n$-th power.
