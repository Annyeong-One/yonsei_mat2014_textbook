# arange and linspace


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy provides two primary functions for generating sequences of numbers: `np.arange` for integer steps and `np.linspace` for evenly spaced floats.


## np.arange Function

Generates values within a half-open interval `[start, stop)` with a given step.

### 1. Single Argument

```python
import numpy as np

def main():
    a = np.arange(9)
    print("np.arange(9)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.arange(9)
[0 1 2 3 4 5 6 7 8]
```

### 2. Two Arguments

```python
import numpy as np

def main():
    a = np.arange(1, 9)
    print("np.arange(1, 9)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.arange(1, 9)
[1 2 3 4 5 6 7 8]
```

### 3. Three Arguments

```python
import numpy as np

def main():
    a = np.arange(1, 9, 2)
    print("np.arange(1, 9, 2)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.arange(1, 9, 2)
[1 3 5 7]
```


## np.linspace Function

Generates evenly spaced numbers over a closed interval `[start, stop]`.

### 1. Default Samples

```python
import numpy as np

def main():
    a = np.linspace(-1, 2)
    print("np.linspace(-1, 2)")
    print(a)

if __name__ == "__main__":
    main()
```

Default is 50 evenly spaced samples.

### 2. Custom Samples

```python
import numpy as np

def main():
    a = np.linspace(-1, 2, 4)
    print("np.linspace(-1, 2, 4)")
    print(a)

if __name__ == "__main__":
    main()
```

Output:

```
np.linspace(-1, 2, 4)
[-1.  0.  1.  2.]
```


## Key Differences

Understanding when to use each function is essential.

### 1. Endpoint Inclusion

`np.arange` excludes the endpoint; `np.linspace` includes it by default.

### 2. Parameter Meaning

`np.arange` specifies step size; `np.linspace` specifies number of samples.

### 3. Typical Use Cases

Use `np.arange` for integer sequences and `np.linspace` for continuous intervals.


## Floating Point Caution

Using `np.arange` with floats can produce unexpected results.

### 1. Rounding Issues

```python
import numpy as np

a = np.arange(0, 1, 0.1)
print(len(a))  # May vary due to floating-point precision
```

### 2. Recommendation

For floating-point sequences, prefer `np.linspace` to guarantee exact sample count.


## Scientific Computing

Both functions are essential for numerical computations.

### 1. Plotting Curves

```python
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
```

### 2. Index Arrays

```python
import numpy as np

indices = np.arange(len(data))
```

### 3. Grid Generation

`np.linspace` combined with `np.meshgrid` creates 2D coordinate grids.
