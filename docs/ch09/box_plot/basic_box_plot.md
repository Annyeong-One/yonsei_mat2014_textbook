# Basic Box Plot

Box plots (box-and-whisker plots) visualize the distribution of data through quartiles, providing a compact summary of central tendency, spread, and outliers.

## Single Data Set

The simplest box plot displays one distribution using `ax.boxplot()`.

### 1. Import and Setup

```python
import matplotlib.pyplot as plt
import numpy as np
```

### 2. Generate Data

```python
np.random.seed(42)
data = np.random.normal(100, 15, 200)
```

### 3. Create Box Plot

```python
fig, ax = plt.subplots()
ax.boxplot(data)
ax.set_ylabel('Value')
ax.set_title('Basic Box Plot')
plt.show()
```

## Multiple Data Sets

Compare multiple distributions side by side by passing a list of arrays.

### 1. Prepare Multiple Arrays

```python
np.random.seed(42)
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(110, 15, 200)
```

### 2. Pass as List

```python
fig, ax = plt.subplots()
ax.boxplot([data1, data2, data3])
ax.set_xticklabels(['Group A', 'Group B', 'Group C'])
ax.set_ylabel('Value')
ax.set_title('Comparing Distributions')
plt.show()
```

### 3. Interpret Results

Each box represents one distribution. Boxes at different heights indicate different medians. Wider boxes (taller IQR) indicate greater variability.

## Method Signature

The `ax.boxplot()` method accepts various input formats.

### 1. Single Array

```python
ax.boxplot(data)  # One box
```

### 2. List of Arrays

```python
ax.boxplot([data1, data2, data3])  # Multiple boxes
```

### 3. 2D Array

```python
data_2d = np.random.randn(100, 4)
ax.boxplot(data_2d)  # Each column becomes a box
```
