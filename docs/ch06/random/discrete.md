# Discrete Distributions

NumPy provides functions for generating samples from discrete probability distributions.


## np.random.binomial

Generates samples from the binomial distribution $B(n, p)$.

### 1. Coin Flip Model

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    n = 10
    p = 0.5
    data = np.random.binomial(n, p, size=(1000,))
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    ax.set_title("Histogram of Binomial Samples", fontsize=15)
    bins = np.arange(n + 2) - 0.5
    ax.hist(data, bins=bins, density=True, alpha=0.4)
    ax.set_xticks(np.arange(n + 1))
    
    x = np.arange(n + 1)
    pmf = stats.binom(n, p).pmf(x)
    for x_loc, p_loc in zip(x, pmf):
        ax.plot((x_loc - 0.5, x_loc + 0.5), (p_loc, p_loc), 
                color='red', alpha=0.9, linestyle='--')
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Interpretation

Counts successes in $n$ independent Bernoulli trials with probability $p$.


## np.random.geometric

Generates samples from the geometric distribution.

### 1. Waiting Time

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    p = 0.5
    data = np.random.geometric(p, size=(1000,))
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    ax.set_title("Histogram of Geometric Samples", fontsize=15)
    bins = np.arange(10) - 0.5
    ax.hist(data, bins=bins, density=True)
    ax.set_xticks(np.arange(10))
    
    x = np.arange(9)
    pmf = stats.geom(p).pmf(x)
    for x_loc, p_loc in zip(x, pmf):
        ax.plot((x_loc - 0.5, x_loc + 0.5), (p_loc, p_loc),
                color='red', alpha=0.9, linestyle='--')
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Interpretation

Number of trials until the first success in Bernoulli experiments.


## np.random.poisson

Generates samples from the Poisson distribution $\text{Pois}(\lambda)$.

### 1. Event Counts

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    la = 10
    data = np.random.poisson(la, size=(1000,))
    
    fig, ax = plt.subplots(figsize=(10, 4))
    
    ax.set_title("Histogram of Poisson Samples", fontsize=15)
    bins = np.arange(30) - 0.5
    ax.hist(data, bins=bins, density=True)
    ax.set_xticks(np.arange(30))
    
    x = np.arange(29)
    pmf = stats.poisson(la).pmf(x)
    for x_loc, p_loc in zip(x, pmf):
        ax.plot((x_loc - 0.5, x_loc + 0.5), (p_loc, p_loc),
                color='red', alpha=0.9, linestyle='--')
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Interpretation

Models rare event counts over fixed intervals with rate $\lambda$.


## np.random.exponential

Generates samples from the exponential distribution.

### 1. Inter-Arrival Times

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def main():
    bt = 1 / 10  # scale = 1/lambda
    data = np.random.exponential(bt, size=(1000,))
    
    fig, ax = plt.subplots()
    
    ax.set_title("Histogram of Exponential Samples", fontsize=15)
    _, bins, _ = ax.hist(data, bins=100, density=True)
    ax.plot(bins, stats.expon(scale=bt).pdf(bins),
            color='red', linestyle='--', alpha=0.9)
    
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Poisson Connection

Time between events in a Poisson process follows exponential distribution.


## np.random.randint

Generates random integers from a discrete uniform distribution.

### 1. Fair Dice

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    np.random.seed(0)
    data = np.random.randint(low=1, high=7, size=(1_000,))
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_title("Histogram of Fair Dice Samples", fontsize=15)
    bins = np.arange(1, 8) - 0.5
    ax.hist(data, bins=bins, density=True, alpha=0.4, rwidth=0.9)
    ax.set_xticks(np.arange(1, 7))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Half-Open Interval

`randint(low, high)` samples from $[\text{low}, \text{high})$.


## np.random.choice

Samples from a custom discrete distribution.

### 1. Custom Weights

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    Omega = [-3, -1, 1, 2, 5]
    pmf = [0.1, 0.1, 0.1, 0.5, 0.2]
    sample = np.random.choice(Omega, p=pmf, size=(1_000,))
    
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.hist(sample, bins=np.arange(-3, 7) - 0.5, density=True)
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Uniform Sampling

```python
import numpy as np

def main():
    Omega = [1, 2, 3, 4, 5, 6]
    print(np.random.choice(Omega, size=(10,)))

if __name__ == "__main__":
    main()
```

### 3. Without Replacement

```python
import numpy as np

def main():
    Omega = [1, 2, 3, 4, 5, 6]
    print(np.random.choice(Omega, size=(5,), replace=False))

if __name__ == "__main__":
    main()
```

Set `replace=False` for sampling without replacement.
