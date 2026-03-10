# Statistics Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## mean and np.mean

### 1. Basic Usage

Compute the arithmetic mean.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{a.mean() = }")
    print(f"{a.mean(axis=0) = }")
    print(f"{a.mean(axis=1) = }")

if __name__ == "__main__":
    main()
```

**Output:**

```
a =
[[1 2 3]
 [4 5 6]]

a.mean() = 3.5
a.mean(axis=0) = array([2.5, 3.5, 4.5])
a.mean(axis=1) = array([2., 5.])
```

### 2. Output Shape

```python
import numpy as np

def main():
    a = np.random.standard_normal((2, 3))
    
    print(f"{a.mean().shape = }")
    print(f"{a.mean(axis=0).shape = }")
    print(f"{a.mean(axis=1).shape = }")

if __name__ == "__main__":
    main()
```

**Output:**

```
a.mean().shape = ()
a.mean(axis=0).shape = (3,)
a.mean(axis=1).shape = (2,)
```

### 3. Function Syntax

```python
import numpy as np

def main():
    a = np.random.standard_normal((2, 3))
    
    print(f"{np.mean(a).shape = }")
    print(f"{np.mean(a, axis=0).shape = }")
    print(f"{np.mean(a, axis=1).shape = }")

if __name__ == "__main__":
    main()
```

## std and np.std

### 1. Basic Usage

Compute the standard deviation.

```python
import numpy as np

def main():
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{a.std() = :.4f}")
    print(f"{a.std(axis=0) = }")
    print(f"{a.std(axis=1) = }")

if __name__ == "__main__":
    main()
```

### 2. Output Shape

```python
import numpy as np

def main():
    a = np.random.standard_normal((2, 3))
    
    print(f"{a.std().shape = }")
    print(f"{a.std(axis=0).shape = }")
    print(f"{a.std(axis=1).shape = }")

if __name__ == "__main__":
    main()
```

### 3. ddof Parameter

The `ddof` (delta degrees of freedom) parameter controls the divisor: `N - ddof`.

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5])
    
    # Population std (ddof=0, default)
    pop_std = a.std(ddof=0)
    
    # Sample std (ddof=1)
    sample_std = a.std(ddof=1)
    
    print(f"Data: {a}")
    print(f"Population std (ddof=0): {pop_std:.4f}")
    print(f"Sample std (ddof=1): {sample_std:.4f}")

if __name__ == "__main__":
    main()
```

## var and np.var

### 1. Basic Usage

Compute the variance (square of standard deviation).

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{a.var() = }")
    print(f"{a.var(axis=0) = }")
    print(f"{a.var(axis=1) = }")

if __name__ == "__main__":
    main()
```

### 2. Function Syntax

```python
import numpy as np

def main():
    a = np.array([[1, 2],
                  [3, 1],
                  [2, 3]])
    
    print("a =")
    print(a)
    print()
    
    print(f"{np.var(a) = }")
    print(f"{np.var(a, axis=0) = }")
    print(f"{np.var(a, axis=1) = }")

if __name__ == "__main__":
    main()
```

### 3. std vs var

```python
import numpy as np

def main():
    a = np.array([1, 2, 3, 4, 5])
    
    variance = a.var()
    std_dev = a.std()
    
    print(f"Variance: {variance:.4f}")
    print(f"Std Dev:  {std_dev:.4f}")
    print(f"sqrt(var) = std: {np.sqrt(variance):.4f}")

if __name__ == "__main__":
    main()
```

## np.median

### 1. Basic Usage

Compute the median (middle value).

```python
import numpy as np

def main():
    # Odd number of elements
    a = np.array([1, 3, 2, 5, 4])
    print(f"a = {a}")
    print(f"np.median(a) = {np.median(a)}")
    print()
    
    # Even number of elements (average of two middle)
    b = np.array([1, 3, 2, 5, 4, 6])
    print(f"b = {b}")
    print(f"np.median(b) = {np.median(b)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
a = [1 3 2 5 4]
np.median(a) = 3.0

b = [1 3 2 5 4 6]
np.median(b) = 3.5
```

### 2. No Method Version

Unlike mean/std/var, median is only a function (not a method).

```python
import numpy as np

def main():
    sample_data = np.array([1.5, 2.5, 4, 2, 1, 1])
    
    # np.median() is a function only
    population_median = np.median(sample_data)
    print(f"{population_median = }")
    
    # No method version
    # sample_data.median()  # AttributeError

if __name__ == "__main__":
    main()
```

### 3. With axis Parameter

```python
import numpy as np

def main():
    a = np.array([[1, 5, 3],
                  [2, 4, 6]])
    
    print("a =")
    print(a)
    print()
    
    print(f"np.median(a) = {np.median(a)}")
    print(f"np.median(a, axis=0) = {np.median(a, axis=0)}")
    print(f"np.median(a, axis=1) = {np.median(a, axis=1)}")

if __name__ == "__main__":
    main()
```

## np.quantile

### 1. Basic Usage

Compute quantiles (percentiles as fractions).

```python
import numpy as np

def main():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    q25 = np.quantile(data, 0.25)
    q50 = np.quantile(data, 0.50)
    q75 = np.quantile(data, 0.75)
    
    print(f"Data: {data}")
    print(f"Q1 (25%): {q25}")
    print(f"Q2 (50%): {q50}")
    print(f"Q3 (75%): {q75}")

if __name__ == "__main__":
    main()
```

### 2. Five Number Summary

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = np.array([1, 2, 0, 0, 0, 1, 3, 1, 2, 1, 2, 4, 5, -1, -2, 0, 8])
    
    quantiles = {
        "Min": 0,
        "Q1": 0.25,
        "Median": 0.5,
        "Q3": 0.75,
        "Max": 1
    }
    
    print("Five Number Summary:")
    for label, q in quantiles.items():
        quantile_value = np.quantile(data, q)
        print(f"  {label:6} : {quantile_value}")
    
    fig, ax = plt.subplots(figsize=(2, 3))
    ax.boxplot(data)
    ax.set_title("Boxplot")
    plt.show()

if __name__ == "__main__":
    main()
```

### 3. Multiple Quantiles

```python
import numpy as np

def main():
    data = np.random.randn(1000)
    
    # Compute multiple quantiles at once
    qs = [0.1, 0.25, 0.5, 0.75, 0.9]
    values = np.quantile(data, qs)
    
    print("Quantiles:")
    for q, v in zip(qs, values):
        print(f"  {q*100:5.1f}%: {v:+.3f}")

if __name__ == "__main__":
    main()
```

## scipy.stats

### 1. Skewness

Skewness measures asymmetry of the distribution.

$$\text{Skewness}(X) = E\left(\frac{X-\mu}{\sigma}\right)^3$$

```python
import numpy as np
from scipy import stats

def main():
    x = np.random.normal(size=(1000,))
    
    skewness = stats.skew(x)
    print(f"{stats.skew(x) = :.4f}")
    
    # Positive skew: right tail longer
    # Negative skew: left tail longer
    # Near 0: symmetric

if __name__ == "__main__":
    main()
```

### 2. Kurtosis

Kurtosis measures the "tailedness" of the distribution.

$$\text{Kurtosis}(X) = E\left(\frac{X-\mu}{\sigma}\right)^4$$

$$\text{Excess Kurtosis}(X) = \text{Kurtosis}(X) - 3$$

```python
import numpy as np
from scipy import stats

def main():
    x = np.random.normal(size=(1000,))
    
    # scipy returns excess kurtosis (normal = 0)
    kurt = stats.kurtosis(x)
    print(f"{stats.kurtosis(x) = :.4f}")
    
    # Positive: heavier tails than normal
    # Negative: lighter tails than normal
    # Near 0: similar to normal

if __name__ == "__main__":
    main()
```

### 3. Complete Summary

```python
import numpy as np
from scipy import stats

def main():
    np.random.seed(42)
    data = np.random.normal(loc=5, scale=2, size=1000)
    
    print("Descriptive Statistics:")
    print(f"  Mean:     {np.mean(data):.4f}")
    print(f"  Std:      {np.std(data):.4f}")
    print(f"  Var:      {np.var(data):.4f}")
    print(f"  Median:   {np.median(data):.4f}")
    print(f"  Skewness: {stats.skew(data):.4f}")
    print(f"  Kurtosis: {stats.kurtosis(data):.4f}")

if __name__ == "__main__":
    main()
```
