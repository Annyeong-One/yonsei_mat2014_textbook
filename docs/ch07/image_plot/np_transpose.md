# np.transpose

The `np.transpose()` function rearranges the axes of an array.

## Basic Concept

### Transpose for 2D Arrays

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(f"Original shape: {arr.shape}")  # (2, 3)

transposed = arr.T  # or np.transpose(arr)
print(f"Transposed shape: {transposed.shape}")  # (3, 2)
```

## Image Transpose

### Channel-by-Channel Transpose

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

    # Transpose each channel separately
    img_T = np.empty((img.shape[1], img.shape[0], 3), dtype=np.uint8)
    img_T[:, :, 0] = img[:, :, 0].T
    img_T[:, :, 1] = img[:, :, 1].T
    img_T[:, :, 2] = img[:, :, 2].T

    fig, ax = plt.subplots()
    ax.imshow(img_T)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

## Comparison

### Original vs Transposed

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

# Transpose RGB channels
img_T = np.empty((img.shape[1], img.shape[0], img.shape[2]), dtype=np.uint8)
for i in range(img.shape[2]):
    img_T[:, :, i] = img[:, :, i].T

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(img)
axes[0].set_title(f'Original: {img.shape}')

axes[1].imshow(img_T)
axes[1].set_title(f'Transposed: {img_T.shape}')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Using np.transpose

### Axis Reordering

```python
import numpy as np

# Image shape: (height, width, channels)
img = np.random.randint(0, 256, (100, 150, 3), dtype=np.uint8)
print(f"Original: {img.shape}")  # (100, 150, 3)

# Swap height and width, keep channels
img_transposed = np.transpose(img, (1, 0, 2))
print(f"Transposed: {img_transposed.shape}")  # (150, 100, 3)
```

### Common Axis Permutations

```python
import numpy as np

img = np.random.randint(0, 256, (100, 150, 3), dtype=np.uint8)

# (H, W, C) -> (W, H, C): Transpose spatial dimensions
hwc_to_whc = np.transpose(img, (1, 0, 2))

# (H, W, C) -> (C, H, W): Channel first (for PyTorch)
hwc_to_chw = np.transpose(img, (2, 0, 1))

# (C, H, W) -> (H, W, C): Channel last (from PyTorch)
chw = np.random.randint(0, 256, (3, 100, 150), dtype=np.uint8)
chw_to_hwc = np.transpose(chw, (1, 2, 0))

print(f"HWC: {img.shape}")
print(f"WHC: {hwc_to_whc.shape}")
print(f"CHW: {hwc_to_chw.shape}")
print(f"Back to HWC: {chw_to_hwc.shape}")
```

## Deep Learning Format Conversion

### PyTorch (CHW) to NumPy (HWC)

```python
import numpy as np

# Simulated PyTorch tensor shape
tensor_chw = np.random.rand(3, 224, 224)  # (C, H, W)

# Convert to HWC for visualization
img_hwc = np.transpose(tensor_chw, (1, 2, 0))  # (H, W, C)

print(f"PyTorch format: {tensor_chw.shape}")
print(f"NumPy/Matplotlib format: {img_hwc.shape}")
```

### Batch Processing

```python
import numpy as np

# Batch of images: (N, C, H, W) - PyTorch format
batch_nchw = np.random.rand(32, 3, 224, 224)

# Convert to (N, H, W, C) for visualization
batch_nhwc = np.transpose(batch_nchw, (0, 2, 3, 1))

print(f"PyTorch batch: {batch_nchw.shape}")
print(f"Visualization batch: {batch_nhwc.shape}")
```

## Methods Comparison

### .T vs np.transpose

```python
import numpy as np

# 2D array: .T works directly
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D transpose: {arr_2d.T.shape}")

# 3D array: .T reverses all axes
arr_3d = np.random.rand(2, 3, 4)
print(f"3D .T: {arr_3d.T.shape}")  # (4, 3, 2)

# np.transpose: specific axis control
print(f"3D transpose(1,0,2): {np.transpose(arr_3d, (1, 0, 2)).shape}")  # (3, 2, 4)
```

## Visualization Grid

### All Transpose Variations

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))[:, :, :3]  # Remove alpha

fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Original
axes[0, 0].imshow(img)
axes[0, 0].set_title(f'Original: {img.shape}')

# Spatial transpose (swap H and W)
img_spatial_T = np.transpose(img, (1, 0, 2))
axes[0, 1].imshow(img_spatial_T)
axes[0, 1].set_title(f'Spatial Transpose: {img_spatial_T.shape}')

# Horizontal flip for comparison
img_hflip = img[:, ::-1]
axes[1, 0].imshow(img_hflip)
axes[1, 0].set_title('Horizontal Flip')

# Combined: transpose + flip
img_combined = np.transpose(img[:, ::-1], (1, 0, 2))
axes[1, 1].imshow(img_combined)
axes[1, 1].set_title('Flip + Transpose')

for ax in axes.flat:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Practical Applications

### 90° Rotation

```python
import matplotlib.pyplot as plt
import numpy as np

def rotate_90_cw(img):
    """Rotate image 90 degrees clockwise."""
    return np.transpose(img, (1, 0, 2))[:, ::-1]

def rotate_90_ccw(img):
    """Rotate image 90 degrees counter-clockwise."""
    return np.transpose(img, (1, 0, 2))[::-1]

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img)
axes[0].set_title('Original')

axes[1].imshow(rotate_90_cw(img))
axes[1].set_title('90° Clockwise')

axes[2].imshow(rotate_90_ccw(img))
axes[2].set_title('90° Counter-clockwise')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Image Mirroring

```python
import matplotlib.pyplot as plt
import numpy as np

# Mirror effect using transpose
def mirror_diagonal(img):
    """Create diagonal mirror effect."""
    return np.transpose(img, (1, 0, 2))

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(img)
axes[0].set_title('Original')

axes[1].imshow(mirror_diagonal(img))
axes[1].set_title('Diagonal Mirror')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```
