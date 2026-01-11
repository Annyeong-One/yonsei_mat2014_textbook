# Series Object

## Core Structure

### 1. Definition

A Series is a 1D labeled array:

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(type(s))  # <class 'pandas.core.series.Series'>
```

### 2. Components

```python
print(s.values)  # NumPy array [10 20 30]
print(s.index)   # Index(['a', 'b', 'c'])
print(s.dtype)   # dtype('int64')
```

### 3. vs NumPy Array

Series = Values (ndarray) + Index + Name

## Construction

### 1. From List

```python
s = pd.Series([1, 2, 3, 4])
print(s.index)  # RangeIndex(0, 4)
```

### 2. From Dict

```python
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
```

### 3. From Scalar

```python
s = pd.Series(5, index=['a', 'b', 'c'])
# a    5
# b    5
# c    5
```

## Indexing

### 1. Label-based

```python
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])  # 10
print(s[['a', 'c']])  # Multiple labels
```

### 2. Position-based

```python
print(s.iloc[0])  # 10
print(s.iloc[0:2])  # First two
```

### 3. Boolean Indexing

```python
print(s[s > 15])  # Elements > 15
```

## Operations

### 1. Arithmetic

```python
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'd'])
result = s1 + s2
# Aligns on index, NaN for 'c' and 'd'
```

### 2. Methods

```python
s = pd.Series([1, 2, 3, 4, 5])
print(s.mean())  # 3.0
print(s.std())   # 1.58
print(s.sum())   # 15
```

### 3. String Methods

```python
s = pd.Series(['hello', 'world', 'pandas'])
print(s.str.upper())
print(s.str.len())
```
