# Image Compression

Understanding image compression techniques and their effects on image quality.

[JPEG 디지털 풍화 원인 설명 (Korean)](https://www.youtube.com/watch?v=tHvZngU14jE)

## Compression Types

### Lossless vs Lossy

| Type | Description | Formats | Use Case |
|------|-------------|---------|----------|
| Lossless | No data loss | PNG, BMP, TIFF | Graphics, screenshots |
| Lossy | Some data discarded | JPEG, WebP | Photos, web images |

## JPEG Compression

### Quality Comparison

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Load original image
img = Image.open('image.jpg')

# Save at different quality levels
qualities = [10, 30, 50, 70, 90]
compressed_images = []

for q in qualities:
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=q)
    buffer.seek(0)
    compressed_images.append(Image.open(buffer))

# Display comparison
fig, axes = plt.subplots(1, 5, figsize=(20, 4))

for ax, comp_img, q in zip(axes, compressed_images, qualities):
    ax.imshow(comp_img)
    ax.set_title(f'Quality: {q}')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

### File Size vs Quality

```python
import matplotlib.pyplot as plt
from PIL import Image
import io

img = Image.open('image.jpg')

qualities = range(10, 101, 10)
sizes = []

for q in qualities:
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=q)
    sizes.append(len(buffer.getvalue()) / 1024)  # KB

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(qualities, sizes, 'bo-', linewidth=2, markersize=8)
ax.set_xlabel('JPEG Quality')
ax.set_ylabel('File Size (KB)')
ax.set_title('JPEG Quality vs File Size')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## PNG Compression

### Compression Levels

```python
import matplotlib.pyplot as plt
from PIL import Image
import io

img = Image.open('image.png')

# PNG compression levels (0-9)
compression_levels = [0, 3, 6, 9]
sizes = []

for level in compression_levels:
    buffer = io.BytesIO()
    img.save(buffer, format='PNG', compress_level=level)
    sizes.append(len(buffer.getvalue()) / 1024)

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(compression_levels, sizes, color='steelblue')
ax.set_xlabel('Compression Level')
ax.set_ylabel('File Size (KB)')
ax.set_title('PNG Compression Level vs File Size')
plt.tight_layout()
plt.show()
```

## Compression Artifacts

### JPEG Artifacts Visualization

```python
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# Create image with sharp edges (prone to artifacts)
gradient = np.zeros((100, 200, 3), dtype=np.uint8)
gradient[:, :100] = [255, 0, 0]   # Red
gradient[:, 100:] = [0, 0, 255]  # Blue

img = Image.fromarray(gradient)

# Heavy compression
buffer = io.BytesIO()
img.save(buffer, format='JPEG', quality=5)
buffer.seek(0)
compressed = Image.open(buffer)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].imshow(img)
axes[0].set_title('Original')
axes[0].axis('off')

axes[1].imshow(compressed)
axes[1].set_title('JPEG Quality=5 (Artifacts visible)')
axes[1].axis('off')

plt.tight_layout()
plt.show()
```

### Generational Loss

```python
import matplotlib.pyplot as plt
from PIL import Image
import io

def recompress_jpeg(img, quality, generations):
    """Simulate multiple JPEG saves (generational loss)."""
    current = img
    for _ in range(generations):
        buffer = io.BytesIO()
        current.save(buffer, format='JPEG', quality=quality)
        buffer.seek(0)
        current = Image.open(buffer)
    return current

img = Image.open('image.jpg')

generations = [1, 5, 10, 20]

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

for ax, gen in zip(axes, generations):
    degraded = recompress_jpeg(img.copy(), quality=70, generations=gen)
    ax.imshow(degraded)
    ax.set_title(f'{gen} generations')
    ax.axis('off')

plt.suptitle('JPEG Generational Loss (Quality=70)', fontsize=14)
plt.tight_layout()
plt.show()
```

## Format Comparison

### Same Image, Different Formats

```python
import matplotlib.pyplot as plt
from PIL import Image
import io

img = Image.open('image.png').convert('RGB')

formats = {
    'JPEG (Q=85)': ('JPEG', {'quality': 85}),
    'JPEG (Q=50)': ('JPEG', {'quality': 50}),
    'PNG': ('PNG', {}),
    'WebP (Q=85)': ('WEBP', {'quality': 85})
}

results = {}
for name, (fmt, kwargs) in formats.items():
    buffer = io.BytesIO()
    img.save(buffer, format=fmt, **kwargs)
    size_kb = len(buffer.getvalue()) / 1024
    buffer.seek(0)
    results[name] = (Image.open(buffer), size_kb)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

for ax, (name, (comp_img, size)) in zip(axes.flat, results.items()):
    ax.imshow(comp_img)
    ax.set_title(f'{name}\n{size:.1f} KB')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

## Matplotlib Save Compression

### Saving Figures with Compression

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample plot
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), 'b-', linewidth=2)
ax.set_title('Sample Plot')

# Save with different settings
fig.savefig('plot_low.jpg', dpi=72, quality=50)
fig.savefig('plot_high.jpg', dpi=150, quality=95)
fig.savefig('plot.png', dpi=150)

plt.show()
```

### DPI and Quality Settings

```python
import matplotlib.pyplot as plt
import numpy as np
import os

# Create figure
fig, ax = plt.subplots()
ax.plot(np.random.randn(100).cumsum())
ax.set_title('Random Walk')

# Save with various settings
settings = [
    ('low_quality.jpg', {'dpi': 72, 'quality': 30}),
    ('med_quality.jpg', {'dpi': 100, 'quality': 70}),
    ('high_quality.jpg', {'dpi': 150, 'quality': 95}),
    ('vector.pdf', {'dpi': 150}),
]

for filename, kwargs in settings:
    fig.savefig(filename, **kwargs)
    size = os.path.getsize(filename) / 1024
    print(f"{filename}: {size:.1f} KB")

plt.show()
```

## Practical Guidelines

### Choosing Format

| Content Type | Recommended Format | Reason |
|--------------|-------------------|--------|
| Photographs | JPEG (Q=80-90) | Good compression, acceptable loss |
| Screenshots | PNG | Sharp edges preserved |
| Graphics/Logos | PNG or SVG | No artifacts |
| Web photos | WebP | Best compression ratio |
| Scientific figures | PDF/SVG | Vector, scalable |

### Quality Recommendations

```python
# JPEG Quality Guidelines
quality_guide = {
    '90-100': 'Maximum quality, large files',
    '80-90': 'High quality, good for printing',
    '60-80': 'Good quality, web standard',
    '40-60': 'Medium quality, smaller files',
    '20-40': 'Low quality, thumbnails',
    '1-20': 'Very low, visible artifacts'
}

for quality_range, description in quality_guide.items():
    print(f"Quality {quality_range}: {description}")
```

## Image Optimization Workflow

### Complete Example

```python
import matplotlib.pyplot as plt
from PIL import Image
import io
import os

def optimize_image(input_path, output_path, max_size_kb=100, min_quality=30):
    """Optimize image to target file size."""
    img = Image.open(input_path)
    
    # Convert to RGB if necessary
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # Binary search for quality
    low, high = min_quality, 95
    best_quality = high
    
    while low <= high:
        mid = (low + high) // 2
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=mid)
        size_kb = len(buffer.getvalue()) / 1024
        
        if size_kb <= max_size_kb:
            best_quality = mid
            low = mid + 1
        else:
            high = mid - 1
    
    # Save with best quality
    img.save(output_path, format='JPEG', quality=best_quality)
    final_size = os.path.getsize(output_path) / 1024
    
    return best_quality, final_size

# Usage
quality, size = optimize_image('large_image.jpg', 'optimized.jpg', max_size_kb=200)
print(f"Optimized to quality={quality}, size={size:.1f}KB")
```
