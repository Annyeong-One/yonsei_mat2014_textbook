# Axes Method - imread

The `plt.imread()` function reads image files from disk into NumPy arrays.

## Basic Usage

### Reading Local Images

```python
import matplotlib.pyplot as plt

def main():
    img = plt.imread('img/mewtwo.jpg')
    
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()
```

## Supported Formats

### Common Image Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| PNG | .png | Lossless, supports transparency |
| JPEG | .jpg, .jpeg | Lossy compression |
| GIF | .gif | Limited colors |
| TIFF | .tiff, .tif | High quality |
| BMP | .bmp | Uncompressed |

### Format-Specific Behavior

```python
import matplotlib.pyplot as plt
import numpy as np

# PNG: Returns float32 (0.0-1.0) or uint8 (0-255)
img_png = plt.imread('image.png')
print(f"PNG dtype: {img_png.dtype}")

# JPEG: Returns uint8 (0-255)
img_jpg = plt.imread('image.jpg')
print(f"JPEG dtype: {img_jpg.dtype}")
```

## Image Properties

### Inspecting Loaded Images

```python
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('img/mewtwo.jpg')

print(f"Type: {type(img)}")
print(f"Shape: {img.shape}")
print(f"Dtype: {img.dtype}")
print(f"Min: {img.min()}, Max: {img.max()}")
```

### RGB vs Grayscale

```python
import matplotlib.pyplot as plt

# RGB image: shape = (height, width, 3)
img_rgb = plt.imread('color_image.jpg')
print(f"RGB shape: {img_rgb.shape}")

# Grayscale: shape = (height, width)
img_gray = plt.imread('gray_image.png')
print(f"Grayscale shape: {img_gray.shape}")
```

## Multiple Images

### Loading and Displaying Multiple Files

```python
import matplotlib.pyplot as plt
import os

image_dir = 'img/'
image_files = ['cat.jpg', 'dog.jpg', 'bird.jpg']

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for ax, filename in zip(axes, image_files):
    filepath = os.path.join(image_dir, filename)
    img = plt.imread(filepath)
    ax.imshow(img)
    ax.set_title(filename)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

### Directory Batch Loading

```python
import matplotlib.pyplot as plt
import os
import glob

def load_images_from_directory(directory, extension='*.jpg'):
    images = []
    filenames = []
    for filepath in glob.glob(os.path.join(directory, extension)):
        img = plt.imread(filepath)
        images.append(img)
        filenames.append(os.path.basename(filepath))
    return images, filenames

images, names = load_images_from_directory('img/')
print(f"Loaded {len(images)} images")
```

## Error Handling

### Safe Image Loading

```python
import matplotlib.pyplot as plt
import os

def safe_imread(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return None
    try:
        return plt.imread(filepath)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

img = safe_imread('img/mewtwo.jpg')
if img is not None:
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
```

## Comparison with PIL

### imread vs PIL.Image.open

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filepath = 'img/mewtwo.jpg'

# Using plt.imread
img_mpl = plt.imread(filepath)

# Using PIL
img_pil = np.array(Image.open(filepath))

print(f"plt.imread shape: {img_mpl.shape}, dtype: {img_mpl.dtype}")
print(f"PIL shape: {img_pil.shape}, dtype: {img_pil.dtype}")
print(f"Arrays equal: {np.array_equal(img_mpl, img_pil)}")
```

## Data Type Considerations

### Normalizing Image Data

```python
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('image.png')

# If uint8 (0-255), normalize to float (0-1)
if img.dtype == np.uint8:
    img_normalized = img / 255.0

# If already float (0-1), use directly
elif img.dtype in [np.float32, np.float64]:
    img_normalized = img

print(f"Normalized range: [{img_normalized.min():.2f}, {img_normalized.max():.2f}]")
```

## Practical Example

### Image Gallery

```python
import matplotlib.pyplot as plt
import os

def create_image_gallery(image_dir, ncols=4):
    files = [f for f in os.listdir(image_dir) 
             if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    nrows = (len(files) + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(3*ncols, 3*nrows))
    axes = axes.flatten() if nrows > 1 else [axes] if ncols == 1 else axes
    
    for ax, filename in zip(axes, files):
        img = plt.imread(os.path.join(image_dir, filename))
        ax.imshow(img)
        ax.set_title(filename, fontsize=8)
        ax.axis('off')
    
    # Hide empty subplots
    for ax in axes[len(files):]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show()

create_image_gallery('img/')
```
