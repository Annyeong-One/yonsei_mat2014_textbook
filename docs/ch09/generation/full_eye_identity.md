# Full and Identity

NumPy provides functions for creating constant-filled arrays and identity matrices commonly used in linear algebra.


## np.full Function

Creates an array filled with a specified constant value.

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.full((2, 5), 7)
    print("np.full((2, 5), 7)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.full((2, 5), 7)
[[7 7 7 7 7]
 [7 7 7 7 7]]
```

### 2. Any Fill Value

The fill value can be any scalar: integer, float, or complex.


## np.eye Function

Creates a 2D array with ones on the diagonal and zeros elsewhere.

### 1. Square Matrix

```python
import numpy as np

def main():
    a = np.eye(3)
    print("np.eye(3)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.eye(3)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### 2. Rectangular Matrix

```python
import numpy as np

def main():
    a = np.eye(3, 5)
    print("np.eye(3, 5)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.eye(3, 5)
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]]
```


## np.identity Function

Creates a square identity matrix.

### 1. Basic Usage

```python
import numpy as np

def main():
    a = np.identity(3)
    print("np.identity(3)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.identity(3)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

### 2. Square Only

```python
import numpy as np

def main():
    try:
        a = np.identity(3, 5)
    except TypeError as e:
        print(e)
        print("np.identity only creates square matrices.")

if __name__ == "__main__":
    main()
```

Use `np.eye` for non-square matrices with diagonal ones.


## eye vs identity

Both create identity-like matrices but differ in flexibility.

### 1. np.eye Flexibility

`np.eye(N, M)` accepts two shape parameters for rectangular output.

### 2. np.identity Simplicity

`np.identity(N)` only accepts one parameter, always producing square matrices.

### 3. Recommendation

Prefer `np.eye` for its greater flexibility in all cases.


## Linear Algebra Use

Identity matrices are fundamental in matrix operations.

### 1. Matrix Inverse

$A \cdot A^{-1} = I$ where $I$ is the identity matrix.

### 2. Eigenvalue Problems

$A \cdot v = \lambda \cdot v$ can be rewritten as $(A - \lambda I) \cdot v = 0$.

### 3. Basis Vectors

The columns of an identity matrix form the standard basis vectors.

---

## Exercises

**Exercise 1.**
Create a 4x4 matrix filled with the value `np.pi` using `np.full`. Print the matrix and confirm that every element equals `np.pi`.

??? success "Solution to Exercise 1"

        import numpy as np

        M = np.full((4, 4), np.pi)
        print(M)
        print(f"All pi: {np.all(M == np.pi)}")

---

**Exercise 2.**
Create a 3x5 rectangular identity-like matrix using `np.eye(3, 5)`. Then verify that multiplying a `(3, 5)` matrix by this identity-like matrix (transposed to `(5, 3)`) and then by the original produces a `(3, 3)` result. Print the shapes at each step.

??? success "Solution to Exercise 2"

        import numpy as np

        E = np.eye(3, 5)
        A = np.random.randn(3, 5)
        result = A @ E.T
        print(f"E shape: {E.shape}")         # (3, 5)
        print(f"A shape: {A.shape}")         # (3, 5)
        print(f"A @ E.T shape: {result.shape}") # (3, 3)

---

**Exercise 3.**
Using `np.eye` with the `k` parameter, create a 5x5 matrix with ones on the first superdiagonal (`k=1`). Then create another with ones on the first subdiagonal (`k=-1`). Add both to the standard identity matrix `np.eye(5)` to form a tridiagonal matrix of ones. Print the result.

??? success "Solution to Exercise 3"

        import numpy as np

        I = np.eye(5)
        upper = np.eye(5, k=1)
        lower = np.eye(5, k=-1)
        tridiag = I + upper + lower
        print(tridiag)
