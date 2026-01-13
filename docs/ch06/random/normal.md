# Normal Distributions

NumPy provides multiple functions for generating samples from normal (Gaussian) distributions.


## np.random.randn

Generates samples from the standard normal distribution $\mathcal{N}(0, 1)$.

### 1. Basic Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    n_samples = 10_000
    data = np.random.randn(n_samples)
    
    fig, ax = plt.subplots()
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    mu = data.mean()
    sigma = data.std()
    pdf_at_bins_ = stats.norm(loc=mu, scale=sigma).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, '--r', linewidth=5)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Shape Argument

Pass dimensions as separate arguments: `np.random.randn(3, 2)` for a 3×2 array.


## np.random.normal

Generates samples from a general normal distribution $\mathcal{N}(\mu, \sigma^2)$.

### 1. Parameters

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    loc = 1      # mean
    scale = 2    # standard deviation
    n_samples = 10_000
    
    data = np.random.normal(loc=loc, scale=scale, size=(n_samples,))
    
    fig, ax = plt.subplots()
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    mu = data.mean()
    sigma = data.std()
    pdf_at_bins_ = stats.norm(loc=mu, scale=sigma).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, '--r', linewidth=5)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Scaling Relation

$X \sim \mathcal{N}(\mu, \sigma^2)$ is equivalent to $X = \mu + \sigma Z$ where $Z \sim \mathcal{N}(0, 1)$.


## np.random.standard_normal

Alternative syntax for standard normal samples.

### 1. Size Keyword

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    n_samples = 10_000
    data = np.random.standard_normal(size=(n_samples,))
    
    fig, ax = plt.subplots()
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    mu = data.mean()
    sigma = data.std()
    pdf_at_bins_ = stats.norm(loc=mu, scale=sigma).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, '--r', linewidth=5)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Difference from randn

Uses `size` keyword tuple instead of positional dimension arguments.


## Multivariate Normal

Generates samples from a multivariate normal distribution.

### 1. Covariance Matrix

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x = np.random.multivariate_normal(mean, cov, 10000)
    print(f"{x.shape = }")
    
    kde = stats.gaussian_kde(x.T)
    
    x_ = np.linspace(-3.5, 3.5, 40)
    y_ = np.linspace(-6, 6, 40)
    X, Y = np.meshgrid(x_, y_)
    XY = np.vstack([X.ravel(), Y.ravel()])
    
    Z = kde.evaluate(XY).reshape(X.shape)
    
    fig, ax = plt.subplots()
    a = ax.imshow(Z,
                  origin='lower',
                  aspect='auto',
                  extent=[-3.5, 3.5, -6, 6],
                  cmap='Blues')
    plt.colorbar(a, label="density")
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Correlation Structure

The covariance matrix determines the shape and orientation of the distribution.


## Chi-Square Distribution

A distribution derived from squared normal random variables.

### 1. Degrees of Freedom

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    np.random.seed(0)
    
    df = 10
    n_samples = 10_000
    
    data = np.random.chisquare(df=df, size=(n_samples,))
    
    fig, ax = plt.subplots(figsize=(12, 3))
    
    _, bins_, _ = ax.hist(data, bins=100, density=True)
    
    mu = data.mean()
    pdf_at_bins_ = stats.chi2(mu).pdf(bins_)
    ax.plot(bins_, pdf_at_bins_, label='pdf')
    
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Relation to Normal

$\chi^2_k = \sum_{i=1}^{k} Z_i^2$ where $Z_i \sim \mathcal{N}(0, 1)$.


## Function Comparison

Choose the right function for your needs.

### 1. randn Convenience

Use `randn` for quick standard normal samples with positional shape.

### 2. normal Flexibility

Use `normal` when you need to specify mean and standard deviation.

### 3. standard_normal Clarity

Use `standard_normal` when you prefer keyword arguments for shape.
