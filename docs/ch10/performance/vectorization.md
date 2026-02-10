# Vectorization

Vectorization is the practice of applying operations to entire arrays at once, rather than iterating through elements. Vectorized operations in pandas are typically 10-100x faster than loops.

## Why Vectorization Matters

### The Problem with Loops

```python
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({
    'A': np.random.randn(100000),
    'B': np.random.randn(100000)
})

# Slow: iterating with a loop
def slow_sum(df):
    result = []
    for i in range(len(df)):
        result.append(df.iloc[i]['A'] + df.iloc[i]['B'])
    return result

# Even slower: iterrows
def slower_sum(df):
    result = []
    for idx, row in df.iterrows():
        result.append(row['A'] + row['B'])
    return result
```

### The Vectorized Solution

```python
# Fast: vectorized operation
df['C'] = df['A'] + df['B']
```

## Performance Comparison

```python
n = 100000
df = pd.DataFrame({
    'A': np.random.randn(n),
    'B': np.random.randn(n)
})

# Method 1: iterrows (slowest)
start = time.time()
result = []
for idx, row in df.iterrows():
    result.append(row['A'] + row['B'])
iterrows_time = time.time() - start

# Method 2: apply (slow)
start = time.time()
result = df.apply(lambda row: row['A'] + row['B'], axis=1)
apply_time = time.time() - start

# Method 3: vectorized (fast)
start = time.time()
result = df['A'] + df['B']
vector_time = time.time() - start

print(f"iterrows: {iterrows_time:.3f}s")
print(f"apply:    {apply_time:.3f}s")
print(f"vectorized: {vector_time:.6f}s")
```

Typical results:
```
iterrows: 4.521s
apply:    1.234s
vectorized: 0.001s
```

## Common Vectorized Operations

### Arithmetic

```python
# Element-wise operations
df['sum'] = df['A'] + df['B']
df['diff'] = df['A'] - df['B']
df['product'] = df['A'] * df['B']
df['ratio'] = df['A'] / df['B']
df['power'] = df['A'] ** 2
```

### Comparisons

```python
# Returns boolean Series
mask = df['A'] > 0
mask = df['A'] >= df['B']
mask = (df['A'] > 0) & (df['B'] < 0)
mask = (df['A'] > 0) | (df['B'] > 0)
```

### String Operations (with .str accessor)

```python
df = pd.DataFrame({'text': ['hello', 'world', 'python']})

# Vectorized string operations
df['upper'] = df['text'].str.upper()
df['length'] = df['text'].str.len()
df['contains_o'] = df['text'].str.contains('o')
```

### Datetime Operations (with .dt accessor)

```python
df = pd.DataFrame({'date': pd.date_range('2024-01-01', periods=100)})

# Vectorized datetime operations
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.dayofweek
```

## Replacing Loops with Vectorization

### Conditional Assignment

```python
# Instead of:
for i in range(len(df)):
    if df.loc[i, 'A'] > 0:
        df.loc[i, 'result'] = 'positive'
    else:
        df.loc[i, 'result'] = 'negative'

# Use:
df['result'] = np.where(df['A'] > 0, 'positive', 'negative')
```

### Multiple Conditions

```python
# Instead of complex if-elif-else in loop:
conditions = [
    df['A'] > 1,
    df['A'] > 0,
    df['A'] > -1
]
choices = ['high', 'medium', 'low']
df['category'] = np.select(conditions, choices, default='very_low')
```

### Cumulative Operations

```python
# Instead of loop with running total:
df['cumsum'] = df['A'].cumsum()
df['cumprod'] = df['A'].cumprod()
df['cummax'] = df['A'].cummax()
df['cummin'] = df['A'].cummin()
```

### Shifting and Differencing

```python
# Instead of loop comparing to previous row:
df['prev_A'] = df['A'].shift(1)
df['change'] = df['A'].diff()
df['pct_change'] = df['A'].pct_change()
```

### Rolling Operations

```python
# Instead of loop calculating moving average:
df['rolling_mean'] = df['A'].rolling(window=5).mean()
df['rolling_std'] = df['A'].rolling(window=5).std()
df['rolling_sum'] = df['A'].rolling(window=5).sum()
```

## When apply() Is Acceptable

Sometimes `apply()` is necessary, but optimize the function:

```python
# Slow: complex logic in apply
def complex_calculation(row):
    if row['A'] > 0 and row['B'] > 0:
        return row['A'] * row['B']
    elif row['A'] < 0 and row['B'] < 0:
        return -row['A'] * row['B']
    else:
        return 0

# Faster: vectorize the logic
mask1 = (df['A'] > 0) & (df['B'] > 0)
mask2 = (df['A'] < 0) & (df['B'] < 0)

df['result'] = 0  # default
df.loc[mask1, 'result'] = df.loc[mask1, 'A'] * df.loc[mask1, 'B']
df.loc[mask2, 'result'] = -df.loc[mask2, 'A'] * df.loc[mask2, 'B']
```

## Using NumPy Functions

NumPy functions work directly on pandas objects:

```python
# Math functions
df['abs_A'] = np.abs(df['A'])
df['sqrt_abs'] = np.sqrt(np.abs(df['A']))
df['log_abs'] = np.log(np.abs(df['A']) + 1)
df['exp_A'] = np.exp(df['A'])

# Trigonometric
df['sin_A'] = np.sin(df['A'])
df['cos_A'] = np.cos(df['A'])

# Rounding
df['floor'] = np.floor(df['A'])
df['ceil'] = np.ceil(df['A'])
df['round'] = np.round(df['A'], 2)
```

## Practical Example: Financial Calculations

```python
# Stock price data
np.random.seed(42)
prices = pd.DataFrame({
    'close': 100 + np.cumsum(np.random.randn(10000) * 0.5)
})

# All vectorized calculations
prices['return'] = prices['close'].pct_change()
prices['log_return'] = np.log(prices['close'] / prices['close'].shift(1))
prices['sma_20'] = prices['close'].rolling(20).mean()
prices['sma_50'] = prices['close'].rolling(50).mean()
prices['std_20'] = prices['return'].rolling(20).std()
prices['upper_band'] = prices['sma_20'] + 2 * prices['std_20'] * prices['close']
prices['lower_band'] = prices['sma_20'] - 2 * prices['std_20'] * prices['close']
prices['signal'] = np.where(prices['sma_20'] > prices['sma_50'], 1, -1)
```

## Performance Tips

### 1. Avoid iterrows()

```python
# Never do this for large DataFrames
for idx, row in df.iterrows():
    # process row
    pass
```

### 2. Minimize apply()

```python
# Try to replace apply with vectorized operations
# Bad
df['result'] = df.apply(lambda x: x['A'] + x['B'], axis=1)

# Good
df['result'] = df['A'] + df['B']
```

### 3. Use eval() for Complex Expressions

```python
# For complex arithmetic on large DataFrames
df.eval('result = (A + B) * (C - D) / E', inplace=True)
```

### 4. Batch Operations

```python
# Instead of multiple separate operations
df['A'] = df['A'] * 2
df['B'] = df['B'] + 1
df['C'] = df['A'] + df['B']

# Consider eval for batch
df.eval('''
    A = A * 2
    B = B + 1
    C = A + B
''', inplace=True)
```

## Summary

| Method | Speed | Use Case |
|--------|-------|----------|
| Vectorized ops | ⚡ Fastest | Arithmetic, comparisons |
| NumPy functions | ⚡ Fast | Math operations |
| eval() | ⚡ Fast | Complex expressions |
| apply(axis=0) | 🔶 Moderate | Column-wise operations |
| apply(axis=1) | 🔴 Slow | Row-wise operations |
| iterrows() | 🔴 Slowest | Avoid if possible |

**Rule of thumb**: If you're writing a loop over DataFrame rows, there's almost always a vectorized alternative.
