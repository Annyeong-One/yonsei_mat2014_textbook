# Companion Matrix

Companion matrices encode polynomial coefficients.

## linalg.companion

```python
import numpy as np
from scipy import linalg

def main():
    # p(x) = x^3 - 6x^2 + 11x - 6
    coeffs = [1, -6, 11, -6]
    
    C = linalg.companion(coeffs)
    print("Companion matrix:")
    print(C)
    
    # Eigenvalues are polynomial roots
    roots = np.linalg.eigvals(C)
    print(f"Roots: {roots.real}")

if __name__ == "__main__":
    main()
```

Polynomial roots = eigenvalues of companion matrix.
