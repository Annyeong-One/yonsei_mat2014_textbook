# Toeplitz and Circulant

Special matrices with constant diagonals.

## linalg.toeplitz

```python
import numpy as np
from scipy import linalg

def main():
    c = [1, 2, 3, 4]  # First column
    r = [1, 5, 6, 7]  # First row
    
    T = linalg.toeplitz(c, r)
    print(T)

if __name__ == "__main__":
    main()
```

## linalg.circulant

```python
import numpy as np
from scipy import linalg

def main():
    c = [1, 2, 3, 4]
    C = linalg.circulant(c)
    print(C)

if __name__ == "__main__":
    main()
```

Circulant matrices diagonalize via FFT: $O(n \log n)$ multiply.
