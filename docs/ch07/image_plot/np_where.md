# np.where

The `np.where()` function performs element-wise conditional selection on arrays.

## Syntax

$$\begin{array}{ccccccccccccccc}
\text{c}&=&\text{np.where(}&\text{a==2}&,&\text{a}&,&\text{b}&\text{)}\\
&&&\uparrow&&\uparrow&&\uparrow&\\
&&&\text{Condition}&&\text{If Condition holds,}&&\text{If Condition does not hold,}&\\
&&&&&\text{take values}&&\text{take values}&\\
&&&&&\text{from this numpy array}&&\text{from this numpy array}&\\
\end{array}$$

## Basic Usage

### Conditional Selection

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

# Where a > 2, use a; otherwise use b
c = np.where(a > 2, a, b)
print(c)  # [10, 20, 3, 4, 5]
```

### Replace Values

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Replace values > 3 with 0
result = np.where(arr > 3, 0, arr)
print(result)  # [1, 2, 3, 0, 0]
```

## Image Noise Application

### Adding and Clipping Noise

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    
    # Add random noise (-100 to +100)
    img_noisy = img + np.random.randint(-100, 101, size=img.shape)
    
    # Clip values below 0
    img_noisy = np.where(img_noisy >= 0, img_noisy, 0)
    
    # Clip values above 255
    img_noisy = np.where(img_noisy <= 255, img_noisy, 255)

    fig, ax = plt.subplots()
    ax.imshow(img_noisy)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

## Image Thresholding

### Binary Threshold

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

# Convert to grayscale
gray = np.mean(img[:, :, :3], axis=2)

# Binary threshold
threshold = 128
binary = np.where(gray > threshold, 255, 0)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(img)
axes[0].set_title('Original')

axes[1].imshow(gray, cmap='gray')
axes[1].set_title('Grayscale')

axes[2].imshow(binary, cmap='gray')
axes[2].set_title(f'Binary (threshold={threshold})')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Multiple Thresholds

```python
import matplotlib.pyplot as plt
import numpy as np

thresholds = [64, 128, 192]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(gray, cmap='gray')
axes[0].set_title('Original Grayscale')

for ax, thresh in zip(axes[1:], thresholds):
    binary = np.where(gray > thresh, 255, 0)
    ax.imshow(binary, cmap='gray')
    ax.set_title(f'threshold={thresh}')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Color Replacement

### Replace Specific Color

```python
import matplotlib.pyplot as plt
import numpy as np

# Replace white pixels with red
mask = np.all(img[:, :, :3] > 240, axis=2)  # Find near-white pixels
img_modified = img.copy()
img_modified[mask] = [255, 0, 0, 255]  # Set to red

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img)
axes[0].set_title('Original')
axes[1].imshow(img_modified)
axes[1].set_title('White → Red')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

### Channel-Based Selection

```python
import matplotlib.pyplot as plt
import numpy as np

# Enhance red channel where it's low
red_channel = img[:, :, 0]
enhanced_red = np.where(red_channel < 100, red_channel + 50, red_channel)
enhanced_red = np.where(enhanced_red > 255, 255, enhanced_red)

img_enhanced = img.copy()
img_enhanced[:, :, 0] = enhanced_red

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img)
axes[0].set_title('Original')
axes[1].imshow(img_enhanced)
axes[1].set_title('Red Enhanced')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Masking Operations

### Create Mask

```python
import matplotlib.pyplot as plt
import numpy as np

# Create circular mask
h, w = img.shape[:2]
y, x = np.ogrid[:h, :w]
center_y, center_x = h // 2, w // 2
radius = min(h, w) // 3

mask = (x - center_x)**2 + (y - center_y)**2 <= radius**2

# Apply mask
masked = np.where(mask[:, :, np.newaxis], img, 0)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img)
axes[0].set_title('Original')
axes[1].imshow(masked)
axes[1].set_title('Circular Mask')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Value Clipping

### np.clip Alternative

```python
import numpy as np

# Using np.where for clipping
def clip_with_where(arr, min_val, max_val):
    arr = np.where(arr < min_val, min_val, arr)
    arr = np.where(arr > max_val, max_val, arr)
    return arr

# Equivalent to np.clip
clipped_where = clip_with_where(img_noisy, 0, 255)
clipped_numpy = np.clip(img_noisy, 0, 255)

print(f"Results equal: {np.array_equal(clipped_where, clipped_numpy)}")
```

## Comparison Visualization

### Before and After Noise

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Original
axes[0].imshow(img)
axes[0].set_title('Original')

# Noisy (unclipped - may have artifacts)
img_noisy_raw = img.astype(np.int16) + np.random.randint(-100, 101, size=img.shape)
axes[1].imshow(np.clip(img_noisy_raw, 0, 255).astype(np.uint8))
axes[1].set_title('Noisy (clipped)')

# Using np.where for clipping
img_noisy = img + np.random.randint(-100, 101, size=img.shape)
img_noisy = np.where(img_noisy >= 0, img_noisy, 0)
img_noisy = np.where(img_noisy <= 255, img_noisy, 255)
axes[2].imshow(img_noisy.astype(np.uint8))
axes[2].set_title('Noisy (np.where clipped)')

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()
```

## Practical Applications

### Brightness Adjustment

```python
import matplotlib.pyplot as plt
import numpy as np

def adjust_brightness(img, factor):
    """Adjust image brightness."""
    adjusted = img.astype(np.float32) * factor
    adjusted = np.where(adjusted > 255, 255, adjusted)
    adjusted = np.where(adjusted < 0, 0, adjusted)
    return adjusted.astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
factors = [0.5, 1.0, 1.5]
titles = ['Darker (0.5)', 'Original (1.0)', 'Brighter (1.5)']

for ax, factor, title in zip(axes, factors, titles):
    ax.imshow(adjust_brightness(img, factor))
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

### Contrast Enhancement

```python
import matplotlib.pyplot as plt
import numpy as np

def enhance_contrast(img, factor):
    """Enhance image contrast."""
    mean = img.mean()
    enhanced = (img - mean) * factor + mean
    enhanced = np.where(enhanced > 255, 255, enhanced)
    enhanced = np.where(enhanced < 0, 0, enhanced)
    return enhanced.astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
factors = [0.5, 1.0, 2.0]
titles = ['Low Contrast', 'Original', 'High Contrast']

for ax, factor, title in zip(axes, factors, titles):
    ax.imshow(enhance_contrast(img, factor))
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()
```
