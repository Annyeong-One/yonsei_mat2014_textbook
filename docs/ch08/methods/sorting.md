# Sorting Arrays

## Method sort

### 1. In-Place Sorting

The `.sort()` method sorts the array in place (modifies original).

```python
import numpy as np

def main():
    a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    
    print(f"Before: {a}")
    
    a.sort()  # modifies a in place
    
    print(f"After:  {a}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Before: [3 1 4 1 5 9 2 6]
After:  [1 1 2 3 4 5 6 9]
```

### 2. With axis Parameter

```python
import numpy as np

def main():
    a = np.array([[3, 1, 4],
                  [1, 5, 9]])
    
    print("Original:")
    print(a)
    print()
    
    # Sort along last axis (default)
    b = a.copy()
    b.sort()  # same as b.sort(axis=-1)
    print("sort() (along rows):")
    print(b)
    print()
    
    # Sort along axis=0
    c = a.copy()
    c.sort(axis=0)
    print("sort(axis=0) (along columns):")
    print(c)

if __name__ == "__main__":
    main()
```

### 3. Plotting Use Case

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.random.uniform(-1, 1, size=(100,))
    x.sort()  # in-place sort
    y = x**2
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Parabola (sorted x)')
    plt.show()

if __name__ == "__main__":
    main()
```

## np.sort

### 1. Returns Sorted Copy

`np.sort` returns a new sorted array (original unchanged).

```python
import numpy as np

def main():
    a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    
    b = np.sort(a)  # returns new array
    
    print(f"Original a: {a}")
    print(f"Sorted b:   {b}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Original a: [3 1 4 1 5 9 2 6]
Sorted b:   [1 1 2 3 4 5 6 9]
```

### 2. With axis Parameter

```python
import numpy as np

def main():
    a = np.array([[3, 1, 4],
                  [1, 5, 9]])
    
    print("Original:")
    print(a)
    print()
    
    print("np.sort(a, axis=0):")
    print(np.sort(a, axis=0))
    print()
    
    print("np.sort(a, axis=1):")
    print(np.sort(a, axis=1))
    print()
    
    print("np.sort(a, axis=None) (flattened):")
    print(np.sort(a, axis=None))

if __name__ == "__main__":
    main()
```

### 3. Plotting Use Case

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.random.uniform(-1, 1, size=(100,))
    x = np.sort(x)  # returns sorted copy
    y = x**2
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title('Parabola (sorted x)')
    plt.show()

if __name__ == "__main__":
    main()
```

## np.argsort

### 1. Returns Indices

`np.argsort` returns the indices that would sort the array.

```python
import numpy as np

def main():
    a = np.array([30, 10, 40, 20])
    
    indices = np.argsort(a)
    
    print(f"Original: {a}")
    print(f"Indices:  {indices}")
    print(f"Sorted:   {a[indices]}")

if __name__ == "__main__":
    main()
```

**Output:**

```
Original: [30 10 40 20]
Indices:  [1 3 0 2]
Sorted:   [10 20 30 40]
```

### 2. Sort Related Arrays

Sort one array and apply same ordering to another.

```python
import numpy as np

def main():
    names = np.array(['Alice', 'Bob', 'Carol', 'David'])
    scores = np.array([85, 92, 78, 88])
    
    # Sort by scores
    order = np.argsort(scores)
    
    sorted_names = names[order]
    sorted_scores = scores[order]
    
    print("Original:")
    for n, s in zip(names, scores):
        print(f"  {n}: {s}")
    print()
    
    print("Sorted by score:")
    for n, s in zip(sorted_names, sorted_scores):
        print(f"  {n}: {s}")

if __name__ == "__main__":
    main()
```

### 3. Plotting Use Case

```python
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.random.uniform(-1, 1, size=(50,))
    y = x**2
    
    # Sort x and reorder y accordingly
    order = np.argsort(x)
    x_sorted = x[order]
    y_sorted = y[order]
    
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))
    
    ax0.set_title("Without Sort", fontsize=15)
    ax0.plot(x, y)
    
    ax1.set_title("With Sort (using argsort)", fontsize=15)
    ax1.plot(x_sorted, y_sorted)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

## sort vs argsort

### 1. Comparison

```python
import numpy as np

def main():
    a = np.array([3, 1, 4, 1, 5])
    
    print(f"Original: {a}")
    print()
    
    # np.sort: returns sorted values
    print(f"np.sort(a): {np.sort(a)}")
    
    # np.argsort: returns indices
    idx = np.argsort(a)
    print(f"np.argsort(a): {idx}")
    
    # Using indices to sort
    print(f"a[np.argsort(a)]: {a[idx]}")

if __name__ == "__main__":
    main()
```

### 2. Descending Order

```python
import numpy as np

def main():
    a = np.array([3, 1, 4, 1, 5])
    
    # Ascending (default)
    print(f"Ascending:  {np.sort(a)}")
    
    # Descending (reverse the result)
    print(f"Descending: {np.sort(a)[::-1]}")
    
    # Descending with argsort
    desc_idx = np.argsort(a)[::-1]
    print(f"Desc indices: {desc_idx}")
    print(f"Desc values:  {a[desc_idx]}")

if __name__ == "__main__":
    main()
```

### 3. When to Use Each

```python
import numpy as np

def main():
    """
    Use np.sort when:
    - You only need sorted values
    - Original array order doesn't matter
    
    Use np.argsort when:
    - You need to apply same ordering to other arrays
    - You need the original positions
    - You want to sort by one key, apply to another
    """
    
    # Example: top 3 scores with names
    names = np.array(['A', 'B', 'C', 'D', 'E'])
    scores = np.array([72, 95, 88, 65, 91])
    
    # Get top 3 indices (descending order)
    top3_idx = np.argsort(scores)[::-1][:3]
    
    print("Top 3 performers:")
    for i in top3_idx:
        print(f"  {names[i]}: {scores[i]}")

if __name__ == "__main__":
    main()
```
