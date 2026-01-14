# Axes Method - imshow

The `ax.imshow()` method displays image data on an Axes.

## Basic Usage

### Display NumPy Array as Image

```python
import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(100, 100, 3)

fig, ax = plt.subplots()
ax.imshow(img)
plt.show()
```

## FashionMNIST Example

### PyTorch DataLoader Visualization

```python
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

def main():
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor()
    )

    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor()
    )

    labels_map = {
        0: "T-Shirt",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle Boot",
    }

    train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
    test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

    fig, axes = plt.subplots(1, 10, figsize=(15, 5))

    for imgs, labels in train_dataloader:
        for i, (img, label) in enumerate(zip(imgs, labels)):
            axes[i].imshow(img.squeeze(), cmap='binary')
            axes[i].set_title(labels_map[label.item()])
            axes[i].axis('off')
            if i == 9:
                break
        break

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## MNIST Example

### TensorFlow/Keras Visualization

```python
import matplotlib.pyplot as plt
import tensorflow as tf

def main():
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    fig, axes = plt.subplots(nrows=2, ncols=10, figsize=(10, 2))
    for i in range(2):
        for j in range(10):
            axes[i, j].imshow(x_train[i*10+j], cmap=plt.cm.gray)
            axes[i, j].set_title('Label {}'.format(y_train[i*10+j]))
            axes[i, j].axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Image Data Types

### Different Input Types

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Float array (0-1)
img_float = np.random.rand(50, 50, 3)
axes[0].imshow(img_float)
axes[0].set_title('Float [0, 1]')

# Uint8 array (0-255)
img_uint8 = np.random.randint(0, 256, (50, 50, 3), dtype=np.uint8)
axes[1].imshow(img_uint8)
axes[1].set_title('Uint8 [0, 255]')

# Grayscale (2D array)
img_gray = np.random.rand(50, 50)
axes[2].imshow(img_gray, cmap='gray')
axes[2].set_title('Grayscale')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Tensor Handling

### PyTorch Tensor to Image

```python
import matplotlib.pyplot as plt
import torch

# PyTorch: (C, H, W) -> (H, W, C)
tensor = torch.rand(3, 64, 64)
img = tensor.permute(1, 2, 0).numpy()

fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')
plt.show()
```

### TensorFlow Tensor to Image

```python
import matplotlib.pyplot as plt
import tensorflow as tf

# TensorFlow: usually (H, W, C)
tensor = tf.random.uniform((64, 64, 3))
img = tensor.numpy()

fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')
plt.show()
```

### Batch Visualization

```python
import matplotlib.pyplot as plt
import torch

def show_batch(images, labels=None, ncols=8):
    """Display a batch of images.
    
    Args:
        images: Tensor of shape (N, C, H, W)
        labels: Optional labels
        ncols: Number of columns
    """
    n = len(images)
    nrows = (n + ncols - 1) // ncols
    
    fig, axes = plt.subplots(nrows, ncols, figsize=(2*ncols, 2*nrows))
    axes = axes.flatten()
    
    for i, (ax, img) in enumerate(zip(axes, images)):
        if img.dim() == 3:
            img = img.permute(1, 2, 0)
        ax.imshow(img.squeeze(), cmap='gray' if img.dim() == 2 else None)
        if labels is not None:
            ax.set_title(f'{labels[i]}')
        ax.axis('off')
    
    for ax in axes[n:]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()
```

## Key Parameters

### Common imshow Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `X` | Image data (array-like) | Required |
| `cmap` | Colormap | None |
| `norm` | Normalization | None |
| `aspect` | Aspect ratio | 'equal' |
| `interpolation` | Interpolation method | 'antialiased' |
| `alpha` | Transparency | None |
| `vmin`, `vmax` | Value range | Data min/max |
| `origin` | Origin position | 'upper' |

### Aspect Ratio

```python
import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(50, 100)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img, aspect='equal')
axes[0].set_title("aspect='equal'")

axes[1].imshow(img, aspect='auto')
axes[1].set_title("aspect='auto'")

axes[2].imshow(img, aspect=0.5)
axes[2].set_title("aspect=0.5")

plt.tight_layout()
plt.show()
```

### Interpolation Methods

```python
import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(10, 10)
methods = ['nearest', 'bilinear', 'bicubic', 'spline16']

fig, axes = plt.subplots(1, 4, figsize=(12, 3))

for ax, method in zip(axes, methods):
    ax.imshow(img, interpolation=method, cmap='viridis')
    ax.set_title(method)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

### Origin Position

```python
import matplotlib.pyplot as plt
import numpy as np

img = np.arange(25).reshape(5, 5)

fig, axes = plt.subplots(1, 2, figsize=(8, 4))

axes[0].imshow(img, origin='upper')
axes[0].set_title("origin='upper' (default)")

axes[1].imshow(img, origin='lower')
axes[1].set_title("origin='lower'")

plt.tight_layout()
plt.show()
```

## Return Value

### AxesImage Object

```python
import matplotlib.pyplot as plt
import numpy as np

img = np.random.rand(50, 50)

fig, ax = plt.subplots()
im = ax.imshow(img, cmap='viridis')

# Add colorbar using the AxesImage object
fig.colorbar(im, ax=ax)

plt.show()
```
