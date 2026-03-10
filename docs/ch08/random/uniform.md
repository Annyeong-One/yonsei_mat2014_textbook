# Uniform Distributions


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy provides functions for generating uniformly distributed random numbers over continuous intervals.


## np.random.rand

Generates samples uniformly distributed over $[0, 1)$.

### 1. Basic Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    n_samples = 10_000
    data = np.random.rand(n_samples)
    
    fig, ax = plt.subplots()
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    low_ = data.min()
    high_ = data.max()
    pdf_at_bins_ = stats.uniform(loc=low_, scale=high_ - low_).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, '--r', linewidth=5)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Shape Arguments

Pass dimensions as separate arguments: `np.random.rand(3, 2)` for a 3×2 array.


## np.random.uniform

Generates samples uniformly distributed over a specified interval.

### 1. Custom Interval

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    low = -1
    high = 1
    n_samples = 10_000
    
    data = np.random.uniform(low=low, high=high, size=(n_samples,))
    
    fig, ax = plt.subplots()
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    low_ = data.min()
    high_ = data.max()
    pdf_at_bins_ = stats.uniform(loc=low_, scale=high_ - low_).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, '--r', linewidth=5)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Half-Open Interval

Samples are drawn from $[\text{low}, \text{high})$, excluding the upper bound.


## Scaling Relation

Any uniform distribution can be derived from $U(0, 1)$.

### 1. Linear Transform

$X \sim U(a, b)$ is equivalent to $X = a + (b - a) \cdot U$ where $U \sim U(0, 1)$.

### 2. Practical Choice

Use `rand` for $[0, 1)$ and `uniform` for custom intervals.


## PDF Shape

The uniform distribution has constant probability density.

### 1. Flat Histogram

A properly normalized histogram of uniform samples appears flat.

### 2. Theoretical PDF

$$f(x) = \frac{1}{b - a} \quad \text{for } x \in [a, b)$$


## Common Applications

Uniform random numbers have many practical uses.

### 1. Random Selection

Uniformly sample indices or elements from arrays.

### 2. Monte Carlo

Uniform samples over $[0, 1)$ are the basis for many simulation methods.

### 3. Initialization

Neural network weights are often initialized from uniform distributions.
