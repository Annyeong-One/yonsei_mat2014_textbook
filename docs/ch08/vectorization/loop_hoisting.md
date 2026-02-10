# Loop Hoisting

Loop hoisting moves invariant computations outside inner loops for better performance.

## Concept

### 1. What is Hoisting

Moving calculations that don't depend on the loop variable outside the loop.

### 2. Why It Helps

Avoids redundant recomputation on every iteration.

### 3. Common Pattern

```python
# Before hoisting
for i in range(n):
    for j in range(m):
        val = expensive(i)  # Doesn't depend on j
        result[i, j] = val + something(j)

# After hoisting
for i in range(n):
    val = expensive(i)  # Computed once per i
    for j in range(m):
        result[i, j] = val + something(j)
```

## Image Normalization

### 1. Problem Setup

Normalize each row of an image by its mean and standard deviation.

```python
import numpy as np

def main():
    # Simulated image: (height, width, channels)
    img = np.random.randint(0, 256, size=(100, 150, 3), dtype=np.uint8)
    print(f"Image shape: {img.shape}")

if __name__ == "__main__":
    main()
```

### 2. Normalization Formula

For each pixel $(i, j)$:

$$\text{normalized}_{i,j} = \frac{\text{pixel}_{i,j} - \mu_i}{\sigma_i + \epsilon}$$

where $\mu_i$ and $\sigma_i$ are the mean and std of row $i$.

### 3. Key Observation

Row statistics $\mu_i$ and $\sigma_i$ don't depend on column $j$.

## Naive Implementation

### 1. Code

```python
import numpy as np
import time

def main():
    np.random.seed(42)
    img = np.random.randint(0, 256, size=(400, 600, 3), dtype=np.uint8)
    img_float = img.astype(np.float64)
    result = np.empty_like(img_float)
    
    ep = 1e-6
    
    tic = time.time()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            row_mean = np.mean(img[i, :, :], axis=0)  # Recomputed!
            row_std = np.std(img[i, :, :], axis=0)   # Recomputed!
            result[i, j, :] = (img_float[i, j, :] - row_mean) / (row_std + ep)
    toc = time.time()
    
    print(f"Naive Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Problem

`row_mean` and `row_std` are recalculated for every pixel in the row.

### 3. Redundant Work

For a 400×600 image, statistics are computed 600× more than necessary per row.

## Loop Hoisting

### 1. Code

```python
import numpy as np
import time

def main():
    np.random.seed(42)
    img = np.random.randint(0, 256, size=(400, 600, 3), dtype=np.uint8)
    img_float = img.astype(np.float64)
    result = np.empty_like(img_float)
    
    ep = 1e-6
    
    tic = time.time()
    for i in range(img.shape[0]):
        row_mean = np.mean(img[i, :, :], axis=0)  # Hoisted!
        row_std = np.std(img[i, :, :], axis=0)   # Hoisted!
        for j in range(img.shape[1]):
            result[i, j, :] = (img_float[i, j, :] - row_mean) / (row_std + ep)
    toc = time.time()
    
    print(f"Hoisted Time: {toc - tic:.4f} sec")

if __name__ == "__main__":
    main()
```

### 2. Improvement

Statistics computed once per row, not once per pixel.

### 3. Typical Speedup

5-10× faster than naive implementation.

## Full Vectorization

### 1. Code

```python
import numpy as np
import time

def main():
    np.random.seed(42)
    img = np.random.randint(0, 256, size=(400, 600, 3), dtype=np.uint8)
    img_float = img.astype(np.float64)
    
    ep = 1e-6
    
    tic = time.time()
    # keepdims=True enables broadcasting
    mean = np.mean(img_float, axis=1, keepdims=True)  # (400, 1, 3)
    std = np.std(img_float, axis=1, keepdims=True)    # (400, 1, 3)
    result = (img_float - mean) / (std + ep)
    toc = time.time()
    
    print(f"Vectorized Time: {toc - tic:.6f} sec")
    print(f"mean shape: {mean.shape}")
    print(f"std shape: {std.shape}")

if __name__ == "__main__":
    main()
```

### 2. Key Technique

`keepdims=True` preserves dimensions for broadcasting.

### 3. Typical Speedup

100-1000× faster than naive, 10-100× faster than hoisted.

## Comparison

### 1. Full Benchmark

```python
import numpy as np
import time

def main():
    np.random.seed(42)
    img = np.random.randint(0, 256, size=(200, 300, 3), dtype=np.uint8)
    img_float = img.astype(np.float64)
    ep = 1e-6
    
    # Naive
    result1 = np.empty_like(img_float)
    tic = time.time()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            row_mean = np.mean(img[i, :, :], axis=0)
            row_std = np.std(img[i, :, :], axis=0)
            result1[i, j, :] = (img_float[i, j, :] - row_mean) / (row_std + ep)
    naive_time = time.time() - tic
    
    # Hoisted
    result2 = np.empty_like(img_float)
    tic = time.time()
    for i in range(img.shape[0]):
        row_mean = np.mean(img[i, :, :], axis=0)
        row_std = np.std(img[i, :, :], axis=0)
        for j in range(img.shape[1]):
            result2[i, j, :] = (img_float[i, j, :] - row_mean) / (row_std + ep)
    hoisted_time = time.time() - tic
    
    # Vectorized
    tic = time.time()
    mean = np.mean(img_float, axis=1, keepdims=True)
    std = np.std(img_float, axis=1, keepdims=True)
    result3 = (img_float - mean) / (std + ep)
    vec_time = time.time() - tic
    
    print(f"Naive:      {naive_time:.4f} sec")
    print(f"Hoisted:    {hoisted_time:.4f} sec (×{naive_time/hoisted_time:.1f})")
    print(f"Vectorized: {vec_time:.6f} sec (×{naive_time/vec_time:.0f})")
    
    # Verify results match
    print(f"\nResults match: {np.allclose(result1, result3)}")

if __name__ == "__main__":
    main()
```

### 2. Sample Output

```
Naive:      8.2341 sec
Hoisted:    1.0234 sec (×8.0)
Vectorized: 0.0089 sec (×925)

Results match: True
```

### 3. Lessons Learned

- Loop hoisting: Easy optimization, moderate speedup
- Full vectorization: Best performance, requires rethinking the problem

## General Strategy

### 1. Identify Invariants

Find computations that don't depend on inner loop variables.

### 2. Hoist First

Move invariants outside inner loops as a quick win.

### 3. Vectorize Fully

Eliminate loops entirely using NumPy broadcasting and `keepdims`.
