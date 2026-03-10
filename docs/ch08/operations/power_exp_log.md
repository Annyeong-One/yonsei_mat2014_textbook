# Power Exp Log


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

NumPy provides element-wise power, exponential, and logarithmic functions.

## Power Operations

### 1. Using ** Operator

```python
import numpy as np

def main():
    a = np.array([[1, 2], [3, 4]])
    
    print("a =")
    print(a)
    print()
    print("a ** 2 =")
    print(a ** 2)

if __name__ == "__main__":
    main()
```

### 2. Using np.power

```python
import numpy as np

def main():
    a = np.array([[1, 2], [3, 4]])
    
    # Equivalent to a ** 2
    b = np.power(a, 2)
    
    print("np.power(a, 2) =")
    print(b)

if __name__ == "__main__":
    main()
```

### 3. Base as Array

```python
import numpy as np

def main():
    a = np.array([[1, 2], [3, 4]])
    
    # 2 raised to each element
    b = 2 ** a
    c = np.power(2, a)
    
    print("2 ** a =")
    print(b)
    print()
    print("np.power(2, a) =")
    print(c)

if __name__ == "__main__":
    main()
```

## Square Root

### 1. np.sqrt

```python
import numpy as np

def main():
    a = np.array([1, 4, 9, 16, 25])
    
    print(f"a = {a}")
    print(f"np.sqrt(a) = {np.sqrt(a)}")
    print(f"a ** 0.5 = {a ** 0.5}")

if __name__ == "__main__":
    main()
```

### 2. Cube Root

```python
import numpy as np

def main():
    a = np.array([1, 8, 27, 64])
    
    print(f"a = {a}")
    print(f"np.cbrt(a) = {np.cbrt(a)}")
    print(f"a ** (1/3) = {a ** (1/3)}")

if __name__ == "__main__":
    main()
```

### 3. Negative Values

```python
import numpy as np

def main():
    a = np.array([-1, -4, -9])
    
    # sqrt of negative returns nan
    print(f"np.sqrt({a}) = {np.sqrt(a)}")
    
    # Use complex dtype
    a_complex = a.astype(complex)
    print(f"np.sqrt({a_complex}) = {np.sqrt(a_complex)}")

if __name__ == "__main__":
    main()
```

## Exponential

### 1. np.exp

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3])
    
    print(f"x = {x}")
    print(f"np.exp(x) = {np.exp(x)}")
    print(f"e^0 = {np.exp(0):.4f}")
    print(f"e^1 = {np.exp(1):.4f}")

if __name__ == "__main__":
    main()
```

### 2. np.exp2

```python
import numpy as np

def main():
    x = np.array([0, 1, 2, 3, 4])
    
    print(f"x = {x}")
    print(f"np.exp2(x) = {np.exp2(x)}")  # 2^x
    print(f"2 ** x = {2 ** x}")

if __name__ == "__main__":
    main()
```

### 3. np.expm1

```python
import numpy as np

def main():
    # exp(x) - 1, more accurate for small x
    x = np.array([1e-10, 1e-5, 0.1, 1.0])
    
    print("x          exp(x)-1          expm1(x)")
    for val in x:
        print(f"{val:.0e}      {np.exp(val)-1:.10f}    {np.expm1(val):.10f}")

if __name__ == "__main__":
    main()
```

## Logarithm

### 1. Natural Log (ln)

```python
import numpy as np

def main():
    x = np.array([1, np.e, np.e**2, np.e**3])
    
    print(f"x = {x}")
    print(f"np.log(x) = {np.log(x)}")

if __name__ == "__main__":
    main()
```

### 2. Log Base 10

```python
import numpy as np

def main():
    x = np.array([1, 10, 100, 1000])
    
    print(f"x = {x}")
    print(f"np.log10(x) = {np.log10(x)}")

if __name__ == "__main__":
    main()
```

### 3. Log Base 2

```python
import numpy as np

def main():
    x = np.array([1, 2, 4, 8, 16])
    
    print(f"x = {x}")
    print(f"np.log2(x) = {np.log2(x)}")

if __name__ == "__main__":
    main()
```

## np.log1p

### 1. Log of 1+x

```python
import numpy as np

def main():
    # log(1+x), more accurate for small x
    x = np.array([1e-10, 1e-5, 0.1, 1.0])
    
    print("x          log(1+x)          log1p(x)")
    for val in x:
        print(f"{val:.0e}      {np.log(1+val):.10f}    {np.log1p(val):.10f}")

if __name__ == "__main__":
    main()
```

### 2. Why Use log1p

For very small x, `log(1+x)` loses precision due to floating point.

### 3. Inverse Relationship

```python
import numpy as np

def main():
    x = np.array([0.1, 0.5, 1.0])
    
    # expm1 and log1p are inverses
    print(f"x = {x}")
    print(f"log1p(expm1(x)) = {np.log1p(np.expm1(x))}")
    print(f"expm1(log1p(x)) = {np.expm1(np.log1p(x))}")

if __name__ == "__main__":
    main()
```

## Visualization

### 1. Exp and Log Curves

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x_log = np.linspace(0.1, 10, 100)
    y_log = np.log(x_log)
    
    x_exp = np.linspace(-2, 2, 100)
    y_exp = np.exp(x_exp)
    
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax0.plot(x_log, y_log, 'r-', linewidth=2)
    ax0.axhline(0, linestyle='--', alpha=0.3, color='blue')
    ax0.axvline(0, linestyle='--', alpha=0.3, color='blue')
    ax0.set_title('y = ln(x)')
    ax0.set_xlabel('x')
    ax0.set_ylabel('y')
    ax0.grid(True, alpha=0.3)
    
    ax1.plot(x_exp, y_exp, 'r-', linewidth=2)
    ax1.axhline(0, linestyle='--', alpha=0.3, color='blue')
    ax1.axvline(0, linestyle='--', alpha=0.3, color='blue')
    ax1.set_title('y = exp(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

### 2. Power Functions

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0, 3, 100)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for n in [0.5, 1, 2, 3]:
        ax.plot(x, x ** n, label=f'x^{n}')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Power Functions')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 10)
    
    plt.show()

if __name__ == "__main__":
    main()
```

## Applications

### 1. Compound Interest

```python
import numpy as np

def main():
    principal = 1000
    rate = 0.05
    years = np.arange(1, 11)
    
    # A = P * e^(rt) for continuous compounding
    amount = principal * np.exp(rate * years)
    
    print("Continuous Compounding at 5%")
    print("Year | Amount")
    print("-" * 20)
    for y, a in zip(years, amount):
        print(f"  {y:2} | ${a:.2f}")

if __name__ == "__main__":
    main()
```

### 2. Decibels

```python
import numpy as np

def main():
    # Power ratios
    ratios = np.array([0.1, 0.5, 1, 2, 10, 100])
    
    # Convert to decibels
    db = 10 * np.log10(ratios)
    
    print("Ratio | dB")
    print("-" * 20)
    for r, d in zip(ratios, db):
        print(f"{r:5.1f} | {d:+.1f} dB")

if __name__ == "__main__":
    main()
```

### 3. Softmax Function

```python
import numpy as np

def softmax(x):
    # Subtract max for numerical stability
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)

def main():
    logits = np.array([2.0, 1.0, 0.1])
    
    probs = softmax(logits)
    
    print(f"Logits: {logits}")
    print(f"Softmax: {probs}")
    print(f"Sum: {probs.sum():.4f}")

if __name__ == "__main__":
    main()
```

## Summary Table

### 1. Power Functions

| Function | Description |
|:---------|:------------|
| `a ** b` | Power operator |
| `np.power(a, b)` | Element-wise power |
| `np.sqrt(a)` | Square root |
| `np.cbrt(a)` | Cube root |
| `np.square(a)` | Square (a²) |

### 2. Exponential Functions

| Function | Description |
|:---------|:------------|
| `np.exp(x)` | e^x |
| `np.exp2(x)` | 2^x |
| `np.expm1(x)` | e^x - 1 (accurate for small x) |

### 3. Logarithm Functions

| Function | Description |
|:---------|:------------|
| `np.log(x)` | Natural log (ln) |
| `np.log10(x)` | Log base 10 |
| `np.log2(x)` | Log base 2 |
| `np.log1p(x)` | ln(1+x) (accurate for small x) |
