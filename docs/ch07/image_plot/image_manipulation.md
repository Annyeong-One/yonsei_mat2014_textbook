# Image Manipulation

Manipulate images using NumPy array indexing and slicing operations.

## Basic Indexing and Slicing

### Image as 3D Array

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    print(img.shape)  # (height, width, channels)

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

## Common Transformations

### Multiple Transformations Demo

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    
    imgs = (
        img,              # Original
        img[::-1],        # Vertical flip
        img[:, ::-1],     # Horizontal flip
        img[:, :, ::-1],  # Channel reverse (RGB to BGR)
        img[::7, ::7],    # Downsampling
        img[50:-50, 50:-50]  # Cropping
    )
    
    imgs_title = (
        "img",
        "img[::-1]",
        "img[:, ::-1]",
        "img[:, :, ::-1]",
        "img[::7, ::7]",
        "img[50:-50, 50:-50]"
    )

    fig, axes = plt.subplots(2, 3, figsize=(5*1.61803398875, 5))
    for ax, img_to_plot, img_title in zip(axes.reshape((-1,)), imgs, imgs_title):
        ax.set_title(img_title, fontsize=15)
        ax.imshow(img_to_plot)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Transformation Reference

### Vertical Flip

```python
# Reverse rows
flipped_vertical = img[::-1]
```

### Horizontal Flip

```python
# Reverse columns
flipped_horizontal = img[:, ::-1]
```

### Both Flips (180° Rotation)

```python
# Reverse both rows and columns
rotated_180 = img[::-1, ::-1]
```

### Channel Manipulation

```python
# Reverse channel order (RGB → BGR)
bgr = img[:, :, ::-1]

# Extract single channel
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]
```

### Downsampling

```python
# Take every nth pixel
downsampled = img[::n, ::n]

# Example: 7x downsampling
small = img[::7, ::7]
```

### Cropping

```python
# Crop by specifying bounds
cropped = img[y_start:y_end, x_start:x_end]

# Crop from edges
cropped = img[50:-50, 50:-50]  # Remove 50 pixels from each edge
```

## Image Grid Overlay

### Drawing Grid Lines

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(4*1.61803398875, 4))

    ax0.imshow(img)

    spacing = 50
    img_copy = img.copy()
    img_copy[spacing:-1:spacing, :] = [255, 0, 0, 1]  # Horizontal red lines
    img_copy[:, spacing:-1:spacing] = [255, 0, 0, 1]  # Vertical red lines
    ax1.imshow(img_copy)

    for ax in (ax0, ax1):
        ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## Channel Operations

### Visualize Individual Channels

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(img)
axes[0].set_title('Original')

axes[1].imshow(img[:, :, 0], cmap='Reds')
axes[1].set_title('Red Channel')

axes[2].imshow(img[:, :, 1], cmap='Greens')
axes[2].set_title('Green Channel')

axes[3].imshow(img[:, :, 2], cmap='Blues')
axes[3].set_title('Blue Channel')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Swap Channels

```python
import matplotlib.pyplot as plt
import numpy as np

# Original RGB
img_rgb = img.copy()

# Create different channel arrangements
img_rbg = img[:, :, [0, 2, 1]]  # R, B, G
img_grb = img[:, :, [1, 0, 2]]  # G, R, B
img_gbr = img[:, :, [1, 2, 0]]  # G, B, R
img_brg = img[:, :, [2, 0, 1]]  # B, R, G
img_bgr = img[:, :, [2, 1, 0]]  # B, G, R

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
arrangements = [img_rgb, img_rbg, img_grb, img_gbr, img_brg, img_bgr]
titles = ['RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR']

for ax, arr, title in zip(axes.flat, arrangements, titles):
    ax.imshow(arr)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Regions of Interest

### Extract and Highlight ROI

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

# Define region of interest
y_start, y_end = 100, 200
x_start, x_end = 50, 150

# Extract ROI
roi = img[y_start:y_end, x_start:x_end]

# Create highlighted version
img_highlight = img.copy()
img_highlight[y_start:y_end, x_start:x_end, 0] = 255  # Add red tint

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img)
axes[0].set_title('Original')

axes[1].imshow(img_highlight)
axes[1].set_title('Highlighted ROI')

axes[2].imshow(roi)
axes[2].set_title('Extracted ROI')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Practical Applications

### Image Tiling

```python
import matplotlib.pyplot as plt
import numpy as np

def tile_image(img, rows, cols):
    """Tile an image into a grid."""
    return np.tile(img, (rows, cols, 1))

# Create 2x3 tiled image
tiled = tile_image(img, 2, 3)

fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(tiled)
ax.axis('off')
plt.show()
```

### Image Borders

```python
import matplotlib.pyplot as plt
import numpy as np

def add_border(img, size=10, color=[255, 0, 0]):
    """Add a colored border to an image."""
    bordered = img.copy()
    bordered[:size, :] = color      # Top
    bordered[-size:, :] = color     # Bottom
    bordered[:, :size] = color      # Left
    bordered[:, -size:] = color     # Right
    return bordered

bordered = add_border(img, size=20, color=[255, 0, 0])

fig, ax = plt.subplots()
ax.imshow(bordered)
ax.axis('off')
plt.show()
```
