# Indexing and Selection

Indexing is one of pandas' most powerful features. Understanding the difference between label-based and position-based selection is essential.

## Label-based Selection

The `loc` accessor selects by labels.

### 1. Single Row by Label

```python
import pandas as pd

df = pd.DataFrame({
    "price": [100, 101, 102],
    "volume": [10, 12, 9]
}, index=['day1', 'day2', 'day3'])

print(df.loc['day1'])
```

```
price     100
volume     10
Name: day1, dtype: int64
```

### 2. Row and Column Selection

```python
df.loc['day1', 'price']       # Single value
df.loc['day1':'day2', 'price']  # Slice (inclusive)
df.loc[:, 'price']            # All rows, one column
```

### 3. Multiple Labels

```python
df.loc[['day1', 'day3'], ['price', 'volume']]
```

## Position-based Selection

The `iloc` accessor selects by integer positions.

### 1. Single Row by Position

```python
df.iloc[0]  # First row
```

### 2. Row and Column by Position

```python
df.iloc[0, 0]      # First row, first column
df.iloc[0:2, 0]    # First two rows, first column
df.iloc[:, 0]      # All rows, first column
```

### 3. Integer Slicing

```python
df.iloc[0:2]       # First two rows (exclusive end)
df.iloc[-1]        # Last row
```

## Boolean Indexing

Select rows based on conditions.

### 1. Single Condition

```python
df[df["price"] > 100]
```

### 2. Multiple Conditions

```python
df[(df["price"] > 100) & (df["volume"] > 10)]
df[(df["price"] > 102) | (df["volume"] < 10)]
```

### 3. Using Query

```python
df.query("price > 100 and volume > 10")
```

## Chained Indexing

Avoid chained indexing to prevent unexpected behavior.

### 1. Problematic Pattern

```python
# This can cause SettingWithCopyWarning
df[df["price"] > 100]["volume"] = 20
```

### 2. Correct Approach

```python
df.loc[df["price"] > 100, "volume"] = 20
```

### 3. Copy vs View

Chained indexing may return a view or copy unpredictably.

## Setting Values

Use `loc` and `iloc` for assignment.

### 1. Single Value

```python
df.loc['day1', 'price'] = 105
```

### 2. Multiple Values

```python
df.loc['day1', ['price', 'volume']] = [105, 15]
```

### 3. Conditional Assignment

```python
df.loc[df['price'] > 100, 'flag'] = True
```

## Best Practices

Follow these guidelines for clean indexing code.

### 1. Explicit Selection

Always use `loc` or `iloc` explicitly:

```python
# Preferred
df.loc[0]     # If 0 is a label
df.iloc[0]    # If 0 is a position

# Avoid
df[0]         # Ambiguous
```

### 2. Avoid Mixed Indexing

```python
# Don't mix labels and positions
# Use loc for labels, iloc for positions
```

### 3. Check Index Type

```python
print(df.index)       # Understand your index
print(type(df.index)) # Know the index type
```
