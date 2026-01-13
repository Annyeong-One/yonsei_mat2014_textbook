# linspace and Trigonometry

NumPy's `linspace` function creates evenly spaced float arrays, commonly used with trigonometric functions for scientific computing and visualization.


## Creating Float Arrays with linspace

The `np.linspace()` function generates evenly spaced values over a specified interval.

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

print(x.shape)    # (100,)
print(x.dtype)    # float64
print(x[:5])      # [0.  0.0634  0.1269  0.1903  0.2538]
```

Key characteristics:

- Returns `float64` by default (64-bit precision)
- Includes both start and end values
- Evenly distributes points across the interval


## Element-wise Trigonometric Functions

NumPy's trigonometric functions operate element-wise on arrays.

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

sin = np.sin(x)
cos = np.cos(x)

print(sin.shape)    # (100,)
print(sin.dtype)    # float64
```

The output arrays maintain the same shape and dtype as the input.


## Visualizing Trigonometric Functions

Float arrays work seamlessly with Matplotlib for plotting smooth curves.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
sin = np.sin(x)
cos = np.cos(x)

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 3))

ax0.plot(x, sin)
ax0.set_title('sin')

ax1.plot(x, cos)
ax1.set_title('cos')

plt.show()
```

The 100 float values create smooth continuous curves when plotted.


## Why float64 is the Default

NumPy uses `float64` as the default dtype for floating-point operations:

```python
import numpy as np

x = np.linspace(0, 1, 5)
print(x.dtype)    # float64
```

Reasons for this choice:

- **Precision**: 64-bit floats provide approximately 15-17 significant decimal digits
- **Compatibility**: Matches Python's native `float` type
- **Scientific computing**: Sufficient precision for most numerical applications


## Checking Array Data Types

Verify the dtype of any NumPy array using the `dtype` attribute.

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
sin = np.sin(x)

print(x.dtype)      # float64
print(sin.dtype)    # float64
```


## Specifying Different Float Precision

Override the default dtype when memory efficiency matters.

```python
import numpy as np

# 32-bit floats (half the memory)
x32 = np.linspace(0, 2*np.pi, 100, dtype=np.float32)
print(x32.dtype)    # float32

# 64-bit floats (default)
x64 = np.linspace(0, 2*np.pi, 100, dtype=np.float64)
print(x64.dtype)    # float64
```

Trade-off: `float32` uses less memory but has reduced precision (~7 significant digits).
