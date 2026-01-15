# Basic Aggregations

Aggregation functions summarize data by computing statistics like sum, mean, and count. They reduce multiple values to a single result.

## Column Aggregations

Apply aggregations to DataFrame columns.

### 1. Single Column Mean

```python
import pandas as pd

df = pd.DataFrame({
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
})

print(df['Age'].mean())  # 32.5
```

### 2. Single Column Sum

```python
print(df['Salary'].sum())  # 260000
```

### 3. Multiple Aggregations

```python
print(df['Age'].min())    # 25
print(df['Age'].max())    # 40
print(df['Age'].std())    # 6.45
print(df['Age'].count())  # 4
```

## DataFrame Aggregations

Apply aggregations across the entire DataFrame.

### 1. All Columns Mean

```python
print(df.mean())
```

```
Age          32.5
Salary    65000.0
dtype: float64
```

### 2. All Columns Sum

```python
print(df.sum())
```

### 3. Summary Statistics

```python
print(df.describe())
```

```
             Age        Salary
count   4.000000      4.000000
mean   32.500000  65000.000000
std     6.454972  12909.944487
min    25.000000  50000.000000
25%    28.750000  57500.000000
50%    32.500000  65000.000000
75%    36.250000  72500.000000
max    40.000000  80000.000000
```

## Common Aggregation Methods

Methods available on Series and DataFrame.

### 1. Central Tendency

```python
df['Age'].mean()    # Arithmetic mean
df['Age'].median()  # Middle value
df['Age'].mode()    # Most frequent value
```

### 2. Dispersion

```python
df['Age'].std()     # Standard deviation
df['Age'].var()     # Variance
df['Age'].sem()     # Standard error of mean
```

### 3. Quantiles

```python
df['Age'].quantile(0.25)       # First quartile
df['Age'].quantile([0.25, 0.75])  # Multiple quantiles
```

## Numeric Only Aggregations

Handle mixed data types.

### 1. numeric_only Parameter

```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Salary': [50000, 60000]
})

df.mean(numeric_only=True)  # Exclude 'Name'
```

### 2. Select Numeric Columns

```python
df.select_dtypes(include='number').mean()
```

### 3. Specific Columns

```python
df[['Age', 'Salary']].mean()
```

## Axis Parameter

Aggregate along rows or columns.

### 1. axis=0 (Default)

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df.sum(axis=0)  # Sum each column
```

```
A     6
B    15
dtype: int64
```

### 2. axis=1

```python
df.sum(axis=1)  # Sum each row
```

```
0    5
1    7
2    9
dtype: int64
```

### 3. Row Mean

```python
df['RowMean'] = df.mean(axis=1)
```

## Handling Missing Values

Aggregation methods handle NaN by default.

### 1. skipna=True (Default)

```python
import numpy as np

s = pd.Series([1, 2, np.nan, 4])
s.mean()  # 2.333... (ignores NaN)
```

### 2. skipna=False

```python
s.mean(skipna=False)  # NaN (includes NaN)
```

### 3. Count Non-NaN

```python
s.count()  # 3 (only non-NaN values)
len(s)     # 4 (all values including NaN)
```
