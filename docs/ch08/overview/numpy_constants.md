# NumPy Constants


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy provides fundamental mathematical constants and special values.


## Version Check

Verify the installed NumPy version.

### 1. Check Version

```python
import numpy as np

def main():
    print(f'{np.__version__ = }')

if __name__ == "__main__":
    main()
```

### 2. Compatibility

Different versions may have different features and behaviors.


## Mathematical Constants

NumPy includes commonly used mathematical constants.

### 1. Pi Constant

```python
import numpy as np

def main():
    print(f'{np.pi = }')

if __name__ == "__main__":
    main()
```

Output:

```
np.pi = 3.141592653589793
```

### 2. Euler's Number

```python
import numpy as np

def main():
    print(f'{np.e = }')

if __name__ == "__main__":
    main()
```

Output:

```
np.e = 2.718281828459045
```


## Trigonometric Plot

Use constants for precise mathematical visualizations.

### 1. Sine and Cosine

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(-np.pi, np.pi, 100)
    sin = np.sin(x)
    cos = np.cos(x)

    fig, ax = plt.subplots(figsize=(6.5, 4))

    ax.plot(x, sin, label='sin(x)')
    ax.plot(x, cos, label='cos(x)')

    ax.legend()

    ax.set_xticks((-np.pi, -np.pi/2, 0, np.pi/2, np.pi))
    ax.set_xticklabels(("-$\pi$", "-$\pi$/2", "0", "$\pi$/2", "$\pi$"))

    ax.set_yticks((-1, 1))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Axis Styling

Position spines at center and hide top/right borders for clean mathematical plots.


## Special Value np.nan

Represent missing or undefined numerical data.

### 1. Creating NaN Arrays

```python
import numpy as np

def main():
    x = np.array([
        [93., 84., 73., 68.],
        [97., 67., 57., np.nan],
        [87., 87., np.nan, 77.]
    ])
    print(x)

if __name__ == "__main__":
    main()
```

Output:

```
[[93. 84. 73. 68.]
 [97. 67. 57. nan]
 [87. 87. nan 77.]]
```

### 2. NaN Properties

```python
import numpy as np

print(np.nan == np.nan)      # False
print(np.isnan(np.nan))      # True
```

### 3. NaN Propagation

Any arithmetic with `np.nan` produces `np.nan`.


## Infinity Values

NumPy supports positive and negative infinity.

### 1. Infinity Constant

```python
import numpy as np

print(f'{np.inf = }')
print(f'{-np.inf = }')
print(f'{np.inf > 1e308 = }')
```

### 2. Checking Infinity

```python
import numpy as np

print(np.isinf(np.inf))      # True
print(np.isfinite(np.inf))   # False
print(np.isfinite(1.0))      # True
```


## Practical Usage

Constants enable precise scientific computing.

### 1. Circle Area

```python
import numpy as np

radius = 5
area = np.pi * radius ** 2
```

### 2. Exponential Decay

```python
import numpy as np

t = np.linspace(0, 5, 100)
decay = np.e ** (-t)
```

### 3. Missing Data

```python
import numpy as np

data = np.array([1, 2, np.nan, 4])
mean = np.nanmean(data)  # Ignores NaN
```
