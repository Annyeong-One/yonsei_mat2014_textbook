# Dtype Basics

The `dtype` attribute specifies how array bytes are interpreted.


## Dtype Reference

NumPy supports many data types with different precision and range.

| Data type     | Description |
|:--------------|:------------|
| `bool_`       | Boolean (True or False) stored as a byte |
| `int_`        | Default integer type (int64 or int32) |
| `int8`        | Byte (-128 to 127) |
| `int16`       | Integer (-32768 to 32767) |
| `int32`       | Integer (-2147483648 to 2147483647) |
| `int64`       | Integer (-9223372036854775808 to 9223372036854775807) |
| `uint8`       | Unsigned integer (0 to 255) |
| `uint16`      | Unsigned integer (0 to 65535) |
| `uint32`      | Unsigned integer (0 to 4294967295) |
| `uint64`      | Unsigned integer (0 to 18446744073709551615) |
| `float16`     | Half precision (sign, 5-bit exp, 10-bit mantissa) |
| `float32`     | Single precision (sign, 8-bit exp, 23-bit mantissa) |
| `float64`     | Double precision (sign, 11-bit exp, 52-bit mantissa) |
| `complex64`   | Complex with two 32-bit floats |
| `complex128`  | Complex with two 64-bit floats |


## Checking Dtype

The `dtype` attribute reveals an array's data type.

### 1. Basic Examples

```python
import numpy as np

def main():
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3], dtype='uint8')
    z = np.array([1, 2, 3], dtype='float32')
    w = np.array([1., 2, 3])
    print(x.dtype)
    print(y.dtype)
    print(z.dtype)
    print(w.dtype)

if __name__ == "__main__":
    main()
```

Output:

```
int64
uint8
float32
float64
```

### 2. Float Inference

Including a decimal point (`1.`) triggers float64 inference.


## Default Dtypes

Some functions have specific default dtypes.

### 1. zeros and ones

```python
import numpy as np

def main():
    a = np.zeros((2, 3))
    b = np.ones((2, 3))
    print(f"{a.dtype = }")
    print(f"{b.dtype = }")

if __name__ == "__main__":
    main()
```

Output:

```
a.dtype = dtype('float64')
b.dtype = dtype('float64')
```

### 2. float64 Default

`np.zeros` and `np.ones` default to `float64`, not integers.


## MNIST Example

Image datasets commonly use `uint8` for efficiency.

### 1. Loading MNIST

```python
import numpy as np
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torchvision.datasets import MNIST

def main():
    train_dataset = MNIST(root='data/', train=True,
                          transform=transforms.ToTensor(),
                          download=True)

    fig, ax = plt.subplots(figsize=(9, 6))
    fig.suptitle(f'{train_dataset.data.dtype = }', fontsize=15)

    img = np.empty((28 * 10, 28 * 15))
    for i in range(10):
        for j in range(15):
            img[i*28:(i+1)*28, j*28:(j+1)*28] = train_dataset.data[i*15+j]
    ax.imshow(img, cmap='binary')
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Why uint8

8-bit unsigned integers (0-255) perfectly represent pixel intensities.


## Framework Comparison

Different frameworks have different default integer types.

### 1. NumPy Default

```python
import numpy as np

a = np.array([1, 2, 3])      # int64
b = np.array([1., 2, 3])     # float64
c = a + b
print(c)
```

### 2. PyTorch Default

```python
import torch

a = torch.tensor([1, 2, 3])    # int64 (or int32)
b = torch.tensor([1., 2, 3])   # float32
# c = a + b  # Error: different types
```

### 3. TensorFlow Default

```python
import tensorflow as tf

a = tf.constant([1, 2, 3])     # int32
b = tf.constant([1., 2, 3])    # float32
# c = a + b  # Error: different types
```

NumPy promotes types automatically; PyTorch and TensorFlow require explicit conversion.
