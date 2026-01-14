# Reading Web Images

Load images from URLs directly into NumPy arrays for visualization and manipulation.

## PIL and urllib Approach

Use PIL (Pillow) and urllib to fetch and convert web images.

### Basic Example

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    print(f"{type(img) = }, {img.shape = }, {img.dtype = }")

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

Output:
```
type(img) = <class 'numpy.ndarray'>, img.shape = (Pokemon height, width, 4), img.dtype = dtype('uint8')
```

## Understanding Image Arrays

### Shape and Dimensions

```python
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

print(f"Shape: {img.shape}")      # (height, width, channels)
print(f"Dtype: {img.dtype}")      # uint8 (0-255)
print(f"Min value: {img.min()}")  # 0
print(f"Max value: {img.max()}")  # 255
```

### Channel Interpretation

| Channels | Format | Description |
|----------|--------|-------------|
| 1 | Grayscale | Single intensity value |
| 3 | RGB | Red, Green, Blue |
| 4 | RGBA | RGB + Alpha (transparency) |

## Multiple Images

### Loading Multiple URLs

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

def load_image(url):
    return np.array(PIL.Image.open(urllib.request.urlopen(url)))

urls = [
    "https://example.com/image1.png",
    "https://example.com/image2.png",
    "https://example.com/image3.png"
]

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for ax, url in zip(axes, urls):
    try:
        img = load_image(url)
        ax.imshow(img)
    except:
        ax.text(0.5, 0.5, 'Failed to load', ha='center', va='center')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Error Handling

### Robust Image Loading

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib
from urllib.error import URLError, HTTPError

def safe_load_image(url):
    try:
        img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
        return img
    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
        return None
    except URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = safe_load_image(url)

if img is not None:
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.show()
```

## Alternative: requests Library

### Using requests with PIL

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import Image
import requests
from io import BytesIO

def load_image_requests(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return np.array(img)

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = load_image_requests(url)

fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')
plt.show()
```

## Image Information Display

### Complete Image Analysis

```python
import matplotlib.pyplot as plt
import numpy as np
import PIL
import urllib

url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
img = np.array(PIL.Image.open(urllib.request.urlopen(url)))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Display image
axes[0].imshow(img)
axes[0].set_title('Original Image')
axes[0].axis('off')

# Display info
info_text = f"""
Shape: {img.shape}
Dtype: {img.dtype}
Size: {img.size} pixels
Memory: {img.nbytes / 1024:.1f} KB
Min: {img.min()}
Max: {img.max()}
Mean: {img.mean():.1f}
"""
axes[1].text(0.1, 0.5, info_text, fontsize=12, family='monospace',
             verticalalignment='center')
axes[1].axis('off')
axes[1].set_title('Image Information')

plt.tight_layout()
plt.show()
```
