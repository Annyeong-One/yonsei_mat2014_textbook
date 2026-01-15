# Arrays vs DataFrames

## Data Structure

### 1. NumPy Array

Homogeneous, n-dimensional:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.dtype)  # All elements same type
print(arr.shape)  # (2, 3)
```

### 2. Pandas DataFrame

Heterogeneous, labeled, tabular:

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'score': [85.5, 92.0]
})
print(df.dtypes)  # Different types per column
```

### 3. Key Difference

Array: Single dtype, unlabeled
DataFrame: Multiple dtypes, labeled

## When to Use Each

### 1. Use NumPy When

```python
# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A @ B  # Matrix multiplication

# Numerical computation
data = np.random.randn(1000, 100)
result = data.mean(axis=0)
```

### 2. Use Pandas When

```python
# Heterogeneous data
df = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=10),
    'category': ['A', 'B'] * 5,
    'value': np.random.rand(10)
})

# Data analysis
summary = df.groupby('category')['value'].mean()
```

### 3. Conversion

```python
# DataFrame to array
arr = df.values  # or df.to_numpy()

# Array to DataFrame
df = pd.DataFrame(arr, columns=['col1', 'col2'])
```

## Real-World Example

### 1. Financial Data

```python
import yfinance as yf

# Returns DataFrame (heterogeneous)
df = yf.download("AAPL", start="2023-01-01")
print(df.dtypes)

# Extract for numpy (homogeneous numerical)
close_prices = df['Close'].values
returns = np.diff(close_prices) / close_prices[:-1]
```

### 2. Image Processing

```python
from PIL import Image

# Load as array (homogeneous)
img = np.array(Image.open('photo.jpg'))
print(img.shape)  # (height, width, 3)

# Process
img_gray = img.mean(axis=2)
```

### 3. Time Series

```python
# Use DataFrame for labeled time series
df = pd.DataFrame({
    'timestamp': pd.date_range('2023-01-01', periods=100, freq='H'),
    'temperature': np.random.randn(100) + 20
}).set_index('timestamp')

# Use array for computation
temps = df['temperature'].values
ma = np.convolve(temps, np.ones(5)/5, mode='valid')
```
