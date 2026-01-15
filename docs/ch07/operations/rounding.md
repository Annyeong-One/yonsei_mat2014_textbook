# Rounding Functions

NumPy provides several functions for rounding floating-point numbers.

## np.round

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.array([1.4, 1.5, 1.6, 2.5, 3.5])
    
    print(f"x = {x}")
    print(f"np.round(x) = {np.round(x)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
x = [1.4 1.5 1.6 2.5 3.5]
np.round(x) = [1. 2. 2. 2. 4.]
```

### 2. Decimal Places

```python
import numpy as np

def main():
    x = np.array([3.14159, 2.71828, 1.41421])
    
    print(f"Original: {x}")
    print(f"Round to 2: {np.round(x, 2)}")
    print(f"Round to 3: {np.round(x, 3)}")

if __name__ == "__main__":
    main()
```

### 3. Negative Decimals

```python
import numpy as np

def main():
    x = np.array([1234, 5678, 9012])
    
    print(f"Original: {x}")
    print(f"Round to -1: {np.round(x, -1)}")  # Tens
    print(f"Round to -2: {np.round(x, -2)}")  # Hundreds
    print(f"Round to -3: {np.round(x, -3)}")  # Thousands

if __name__ == "__main__":
    main()
```

## Banker's Rounding

### 1. Round Half to Even

```python
import numpy as np

def main():
    # NumPy uses "round half to even" (banker's rounding)
    x = np.array([0.5, 1.5, 2.5, 3.5, 4.5])
    
    print(f"x = {x}")
    print(f"np.round(x) = {np.round(x)}")
    
    # Note: 0.5 -> 0, 1.5 -> 2, 2.5 -> 2, 3.5 -> 4

if __name__ == "__main__":
    main()
```

### 2. Why Banker's Rounding

Reduces systematic bias in statistical calculations.

### 3. Traditional Rounding

```python
import numpy as np

def traditional_round(x):
    """Round half away from zero"""
    return np.sign(x) * np.floor(np.abs(x) + 0.5)

def main():
    x = np.array([0.5, 1.5, 2.5, 3.5, -0.5, -1.5])
    
    print(f"x = {x}")
    print(f"np.round (banker's): {np.round(x)}")
    print(f"Traditional round:   {traditional_round(x)}")

if __name__ == "__main__":
    main()
```

## np.floor

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.array([1.7, 2.3, -1.7, -2.3])
    
    print(f"x = {x}")
    print(f"np.floor(x) = {np.floor(x)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
x = [ 1.7  2.3 -1.7 -2.3]
np.floor(x) = [ 1.  2. -2. -3.]
```

### 2. Floor Rounds Toward -∞

```python
import numpy as np

def main():
    # Floor always rounds toward negative infinity
    print(f"floor(2.9) = {np.floor(2.9)}")   # 2
    print(f"floor(-2.1) = {np.floor(-2.1)}") # -3

if __name__ == "__main__":
    main()
```

## np.ceil

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.array([1.1, 2.9, -1.1, -2.9])
    
    print(f"x = {x}")
    print(f"np.ceil(x) = {np.ceil(x)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
x = [ 1.1  2.9 -1.1 -2.9]
np.ceil(x) = [ 2.  3. -1. -2.]
```

### 2. Ceil Rounds Toward +∞

```python
import numpy as np

def main():
    # Ceil always rounds toward positive infinity
    print(f"ceil(2.1) = {np.ceil(2.1)}")   # 3
    print(f"ceil(-2.9) = {np.ceil(-2.9)}") # -2

if __name__ == "__main__":
    main()
```

## np.trunc

### 1. Basic Usage

```python
import numpy as np

def main():
    x = np.array([1.7, 2.3, -1.7, -2.3])
    
    print(f"x = {x}")
    print(f"np.trunc(x) = {np.trunc(x)}")

if __name__ == "__main__":
    main()
```

**Output:**

```
x = [ 1.7  2.3 -1.7 -2.3]
np.trunc(x) = [ 1.  2. -1. -2.]
```

### 2. Truncate Toward Zero

```python
import numpy as np

def main():
    # Trunc removes decimal part (rounds toward zero)
    print(f"trunc(2.9) = {np.trunc(2.9)}")   # 2
    print(f"trunc(-2.9) = {np.trunc(-2.9)}") # -2

if __name__ == "__main__":
    main()
```

## np.fix

### 1. Equivalent to trunc

```python
import numpy as np

def main():
    x = np.array([1.7, 2.3, -1.7, -2.3])
    
    print(f"x = {x}")
    print(f"np.fix(x) = {np.fix(x)}")
    print(f"np.trunc(x) = {np.trunc(x)}")
    print(f"Equal: {np.array_equal(np.fix(x), np.trunc(x))}")

if __name__ == "__main__":
    main()
```

### 2. Historical Note

`np.fix` and `np.trunc` produce identical results; both exist for historical reasons.

## Comparison

### 1. All Functions

```python
import numpy as np

def main():
    x = np.array([1.5, 2.5, -1.5, -2.5])
    
    print(f"{'x':>8} {'round':>8} {'floor':>8} {'ceil':>8} {'trunc':>8}")
    print("-" * 44)
    
    for val in x:
        r = np.round(val)
        f = np.floor(val)
        c = np.ceil(val)
        t = np.trunc(val)
        print(f"{val:8.1f} {r:8.1f} {f:8.1f} {c:8.1f} {t:8.1f}")

if __name__ == "__main__":
    main()
```

### 2. Visualization

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(-2.5, 2.5, 201)
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    funcs = [
        ('np.round', np.round),
        ('np.floor', np.floor),
        ('np.ceil', np.ceil),
        ('np.trunc', np.trunc)
    ]
    
    for ax, (name, func) in zip(axes.flat, funcs):
        ax.plot(x, func(x), 'b.', markersize=2)
        ax.plot(x, x, 'r--', alpha=0.3, label='y=x')
        ax.axhline(0, color='gray', alpha=0.3)
        ax.axvline(0, color='gray', alpha=0.3)
        ax.set_title(name)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## 2D Arrays

### 1. Array Rounding

```python
import numpy as np

def main():
    x = np.array([[3.14159, 2.71828],
                  [1.41421, 1.73205]])
    
    print("Original:")
    print(x)
    print()
    print("np.round(x, 2):")
    print(np.round(x, 2))

if __name__ == "__main__":
    main()
```

### 2. With NaN Values

```python
import numpy as np

def main():
    x = np.array([[1.5, np.nan],
                  [2.5, 3.5]])
    
    print("Original:")
    print(x)
    print()
    print("np.round(x):")
    print(np.round(x))  # NaN preserved

if __name__ == "__main__":
    main()
```

## Applications

### 1. Discretization

```python
import numpy as np

def main():
    # Continuous values to discrete bins
    values = np.array([0.3, 1.7, 2.2, 3.8, 4.1])
    
    discrete = np.floor(values).astype(int)
    
    print(f"Continuous: {values}")
    print(f"Discrete:   {discrete}")

if __name__ == "__main__":
    main()
```

### 2. Price Rounding

```python
import numpy as np

def main():
    prices = np.array([19.994, 29.995, 39.996])
    
    # Round to cents
    rounded = np.round(prices, 2)
    
    print(f"Raw prices:     {prices}")
    print(f"Rounded prices: {rounded}")

if __name__ == "__main__":
    main()
```

### 3. Grid Snapping

```python
import numpy as np

def snap_to_grid(x, grid_size):
    """Snap values to nearest grid point"""
    return np.round(x / grid_size) * grid_size

def main():
    points = np.array([0.3, 1.7, 2.2, 3.8])
    grid_size = 0.5
    
    snapped = snap_to_grid(points, grid_size)
    
    print(f"Original: {points}")
    print(f"Snapped:  {snapped}")

if __name__ == "__main__":
    main()
```

## Summary Table

### 1. Rounding Directions

| Function | Direction | Example (2.7) | Example (-2.7) |
|:---------|:----------|:--------------|:---------------|
| `np.round` | Nearest (even) | 3.0 | -3.0 |
| `np.floor` | Toward -∞ | 2.0 | -3.0 |
| `np.ceil` | Toward +∞ | 3.0 | -2.0 |
| `np.trunc` | Toward 0 | 2.0 | -2.0 |

### 2. Key Differences

- `floor` vs `trunc`: Differ for negative numbers
- `round`: Uses banker's rounding (half to even)
- `fix` = `trunc`: Identical functions
