# Array I/O: save, load, savez

NumPy provides efficient binary formats for saving and loading arrays. These are faster and more compact than text formats like CSV.

```python
import numpy as np
```

---

## Why Use NumPy's Binary Format?

| Format | Speed | Size | Preserves dtype | Multiple arrays |
|--------|-------|------|-----------------|-----------------|
| `.npy` | Fast | Compact | Yes | No |
| `.npz` | Fast | Compact | Yes | Yes |
| CSV | Slow | Large | No | No |
| Pickle | Medium | Medium | Yes | Yes |

```python
# Comparison: 1 million floats
arr = np.random.randn(1_000_000)

# Binary: ~8 MB, loads in milliseconds
np.save('data.npy', arr)

# CSV: ~25 MB, loads in seconds
np.savetxt('data.csv', arr)
```

---

## np.save() — Save Single Array

Save one array to a `.npy` file:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Save to file
np.save('my_array.npy', arr)

# File extension .npy is added automatically if missing
np.save('my_array', arr)  # Creates my_array.npy
```

### Parameters

```python
np.save(
    file,           # Filename or file object
    arr,            # Array to save
    allow_pickle=True,  # Allow pickling objects
    fix_imports=True    # Python 2/3 compatibility
)
```

---

## np.load() — Load Array

Load arrays from `.npy` or `.npz` files:

```python
# Load single array
arr = np.load('my_array.npy')
print(arr)
# [[1 2 3]
#  [4 5 6]]

# dtype is preserved
print(arr.dtype)  # int64
```

### Security Warning

```python
# allow_pickle=False is safer for untrusted files
arr = np.load('untrusted.npy', allow_pickle=False)

# Default changed in NumPy 1.16.3 for security
# Pickle can execute arbitrary code!
```

---

## np.savez() — Save Multiple Arrays

Save multiple arrays to a single `.npz` file (uncompressed):

```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([[1, 2], [3, 4]])

# Save with automatic names (arr_0, arr_1, arr_2)
np.savez('arrays.npz', x, y, z)

# Save with custom names (recommended)
np.savez('arrays.npz', x_data=x, y_data=y, matrix=z)
```

### Loading .npz Files

```python
# Load returns NpzFile object (dict-like)
data = np.load('arrays.npz')

# Access by name
print(data['x_data'])  # [1 2 3]
print(data['y_data'])  # [4 5 6]
print(data['matrix'])  # [[1 2] [3 4]]

# List available arrays
print(data.files)  # ['x_data', 'y_data', 'matrix']

# Close when done (or use context manager)
data.close()
```

### Context Manager (Recommended)

```python
# Automatically closes file
with np.load('arrays.npz') as data:
    x = data['x_data']
    y = data['y_data']
    print(x + y)  # [5 7 9]
```

---

## np.savez_compressed() — Compressed Archive

Same as `savez()` but with compression:

```python
large_array = np.random.randn(1000, 1000)

# Uncompressed: ~8 MB
np.savez('uncompressed.npz', data=large_array)

# Compressed: ~6 MB (varies by data)
np.savez_compressed('compressed.npz', data=large_array)
```

### When to Compress

| Scenario | Recommendation |
|----------|----------------|
| Large arrays, infrequent access | Compress |
| Small arrays | Don't compress (overhead) |
| Frequent loading | Don't compress (slower) |
| Limited disk space | Compress |
| Random/incompressible data | Don't compress (no benefit) |

---

## Practical Examples

### Save Model Weights

```python
# Save neural network weights
weights = {
    'layer1': np.random.randn(784, 256),
    'layer2': np.random.randn(256, 128),
    'layer3': np.random.randn(128, 10),
    'biases1': np.zeros(256),
    'biases2': np.zeros(128),
    'biases3': np.zeros(10),
}

np.savez_compressed('model_weights.npz', **weights)

# Load weights
with np.load('model_weights.npz') as data:
    w1 = data['layer1']
    b1 = data['biases1']
```

### Checkpoint Training Progress

```python
def save_checkpoint(epoch, weights, optimizer_state, loss_history):
    np.savez(
        f'checkpoint_epoch_{epoch}.npz',
        weights=weights,
        optimizer_state=optimizer_state,
        loss_history=np.array(loss_history),
        epoch=np.array(epoch)
    )

def load_checkpoint(filename):
    with np.load(filename, allow_pickle=True) as data:
        return {
            'weights': data['weights'],
            'optimizer_state': data['optimizer_state'],
            'loss_history': data['loss_history'].tolist(),
            'epoch': int(data['epoch'])
        }
```

### Save Preprocessed Data

```python
# Preprocess once, save for reuse
def preprocess_and_save(raw_data_path, output_path):
    raw = np.loadtxt(raw_data_path, delimiter=',')
    
    # Normalize
    mean = raw.mean(axis=0)
    std = raw.std(axis=0)
    normalized = (raw - mean) / std
    
    # Save data and parameters
    np.savez(
        output_path,
        data=normalized,
        mean=mean,
        std=std
    )

# Load preprocessed data
with np.load('preprocessed.npz') as f:
    data = f['data']
    mean = f['mean']
    std = f['std']
```

---

## Text Alternatives

For human-readable or interoperability needs:

### np.savetxt() / np.loadtxt()

```python
arr = np.array([[1.5, 2.5], [3.5, 4.5]])

# Save as text
np.savetxt('data.csv', arr, delimiter=',', header='col1,col2')

# Load from text
loaded = np.loadtxt('data.csv', delimiter=',')
```

### np.genfromtxt() — Handle Missing Values

```python
# More flexible than loadtxt
data = np.genfromtxt(
    'data.csv',
    delimiter=',',
    missing_values='NA',
    filling_values=0.0
)
```

---

## Memory-Mapped Files

For arrays too large to fit in memory:

```python
# Create memory-mapped file
large = np.memmap('large_array.dat', dtype='float64', 
                   mode='w+', shape=(10000, 10000))
large[:] = np.random.randn(10000, 10000)
large.flush()  # Write to disk

# Load as memory-mapped (doesn't load into RAM)
mapped = np.memmap('large_array.dat', dtype='float64',
                    mode='r', shape=(10000, 10000))
print(mapped[0, 0])  # Access without loading entire array
```

---

## Common Issues

### Issue 1: File Not Found

```python
# Always use raw strings or forward slashes for paths
np.save(r'C:\data\array.npy', arr)  # Raw string
np.save('C:/data/array.npy', arr)   # Forward slashes
```

### Issue 2: Pickle Security

```python
# Untrusted .npy files can contain pickled objects
# Always use allow_pickle=False for untrusted sources
try:
    arr = np.load('untrusted.npy', allow_pickle=False)
except ValueError:
    print("File contains pickled objects - potentially unsafe!")
```

### Issue 3: Version Compatibility

```python
# Old NumPy versions may not read new files
# Check NumPy version if sharing files
print(np.__version__)
```

---

## Summary

| Function | Purpose | File Type |
|----------|---------|-----------|
| `np.save()` | Save single array | `.npy` |
| `np.load()` | Load `.npy` or `.npz` | Both |
| `np.savez()` | Save multiple arrays | `.npz` |
| `np.savez_compressed()` | Save compressed | `.npz` |
| `np.savetxt()` | Save as text | `.csv`, `.txt` |
| `np.loadtxt()` | Load from text | `.csv`, `.txt` |
| `np.memmap()` | Memory-mapped I/O | `.dat` |

**Key Takeaways**:

- Use `.npy` for single arrays, `.npz` for multiple
- Binary format is faster and preserves dtypes
- Use `savez_compressed()` for large arrays with limited disk space
- Use context manager (`with`) when loading `.npz` files
- Set `allow_pickle=False` for untrusted files
- Use memory mapping for arrays too large for RAM
