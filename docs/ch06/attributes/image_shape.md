# Image Shape Examples

Images loaded as NumPy arrays have shapes that encode height, width, and color channels.


## RGB Image Shape

RGB images have shape `(H, W, 3)` for height, width, and three color channels.

### 1. Starry Night

```python
import numpy as np
import matplotlib.pyplot as plt
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1513px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    print(f"{type(img) = }")
    print(f"{img.shape = }")
    print(f"{img.dtype = }")

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

Output:

```
type(img) = <class 'numpy.ndarray'>
img.shape = (1198, 1513, 3)
img.dtype = dtype('uint8')
```

### 2. Shape Interpretation

- `1198` is height (rows)
- `1513` is width (columns)
- `3` is RGB channels (Red, Green, Blue)


## RGBA Image Shape

RGBA images have shape `(H, W, 4)` with an additional alpha channel for transparency.

### 1. Mewtwo PNG

```python
import numpy as np
import matplotlib.pyplot as plt
import PIL
import urllib

def main():
    url = "https://upload.wikimedia.org/wikipedia/en/4/43/Pok%C3%A9mon_Mewtwo_art.png"
    img = np.array(PIL.Image.open(urllib.request.urlopen(url)))
    print(f"{type(img) = }")
    print(f"{img.shape = }")
    print(f"{img.dtype = }")

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

Output:

```
type(img) = <class 'numpy.ndarray'>
img.shape = (227, 185, 4)
img.dtype = dtype('uint8')
```

### 2. Alpha Channel

The fourth channel (alpha) controls transparency: 0 is fully transparent, 255 is fully opaque.


## Grayscale Images

Grayscale images have shape `(H, W)` with no channel dimension.

### 1. 2D Shape

A grayscale image is simply a 2D array of intensity values.

### 2. Channel Expansion

To convert grayscale to RGB-compatible shape, repeat the channel: `img[:, :, np.newaxis]`.


## Common Patterns

Image shapes follow consistent conventions across libraries.

### 1. NumPy/PIL Order

`(H, W, C)` — Height first, then Width, then Channels.

### 2. PyTorch Order

`(C, H, W)` — Channels first, requiring transpose when converting.

### 3. Batch Dimension

Batched images add a leading dimension: `(N, H, W, C)` or `(N, C, H, W)`.
