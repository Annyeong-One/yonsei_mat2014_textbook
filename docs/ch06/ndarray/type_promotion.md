# Type Promotion

NumPy follows similar type promotion rules to Python, automatically upcasting array dtypes in mixed-type operations.


## Array Dtype Upcasting

When operating on arrays with different dtypes, NumPy promotes to the more general type.

```python
import numpy as np

# int64 + float64 → float64
a = np.array([1, 1])
b = np.array([2., 2.])

result = a + b
print(result)        # [3. 3.]
print(result.dtype)  # float64
```


## Mixed Dtype Within Arrays

Arrays with mixed types during creation are upcast to accommodate all values.

```python
import numpy as np

# Mixed int and float → float64
arr = np.array([1, 2, 3.])
print(arr)           # [1. 2. 3.]
print(arr.dtype)     # float64
```


## Upcasting with Arithmetic Operators

All arithmetic operations follow the same promotion rules.

### Addition

```python
import numpy as np

int_arr = np.array([1, 1])
float_arr = np.array([2., 2.])

print(int_arr + float_arr)  # [3. 3.]
```

### Subtraction

```python
import numpy as np

print(np.array([1, 1]) - np.array([2., 2.]))  # [-1. -1.]
```

### Multiplication

```python
import numpy as np

print(np.array([1, 1]) * np.array([2., 2.]))  # [2. 2.]
```

### Division

```python
import numpy as np

print(np.array([1, 1]) / np.array([2., 2.]))  # [0.5 0.5]
```


## Boolean Arrays in Numeric Context

Boolean arrays are promoted to integers in arithmetic operations.

```python
import numpy as np

bool_arr = np.array([True, False, True])
int_arr = np.array([1, 2, 3])

print(bool_arr + int_arr)  # [2 2 4]
print(bool_arr * 10)       # [10  0 10]
```


## Plotting Boolean Data

Matplotlib implicitly converts boolean arrays to numeric for plotting.

```python
import numpy as np
import matplotlib.pyplot as plt

y = np.zeros((100,), dtype=bool)
y[40:60] = True

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(y)
ax.set_title("Boolean Array Plot")
plt.show()
```

The boolean values `True`/`False` are plotted as `1`/`0`.


## Checking Result Dtype

Always verify the dtype after operations to understand promotion behavior.

```python
import numpy as np

a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1., 2., 3.], dtype=np.float32)

result = a + b
print(result.dtype)  # float64 (promoted to default float)
```


## Controlling Dtype Explicitly

Override automatic promotion with explicit dtype specification.

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([1., 2., 3.])

# Force result to float32
result = (a + b).astype(np.float32)
print(result.dtype)  # float32
```


## NumPy Promotion Hierarchy

NumPy's type promotion follows a similar hierarchy to Python.

```
bool → int8 → int16 → int32 → int64 → float32 → float64 → complex64 → complex128
```

The result dtype is determined by the "smallest" type that can safely hold all values.

```python
import numpy as np

# int32 + float32 → float64 (safe promotion)
a = np.array([1], dtype=np.int32)
b = np.array([1.], dtype=np.float32)

print((a + b).dtype)  # float64
```
