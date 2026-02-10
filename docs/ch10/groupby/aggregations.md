# GroupBy Aggregations

GroupBy objects support various aggregation methods to summarize grouped data.

## Basic Aggregations

Apply single aggregation functions.

### 1. Mean per Group

```python
import pandas as pd

df = pd.DataFrame({
    'asset': ['A', 'A', 'B', 'B'],
    'return': [0.01, -0.02, 0.03, 0.01],
})

df.groupby('asset')['return'].mean()
```

```
asset
A    -0.005
B     0.020
Name: return, dtype: float64
```

### 2. Common Aggregations

```python
df.groupby('asset')['return'].sum()
df.groupby('asset')['return'].count()
df.groupby('asset')['return'].std()
df.groupby('asset')['return'].min()
df.groupby('asset')['return'].max()
```

### 3. Multiple Methods

```python
df.groupby('asset')['return'].agg(['mean', 'std', 'count'])
```

## LeetCode Example: Duplicate Emails

Count email occurrences.

### 1. Sample Data

```python
person = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'email': ['a@ex.com', 'b@ex.com', 'a@ex.com', 'b@ex.com', 'c@ex.com']
})
```

### 2. GroupBy Count

```python
email_counts = person.groupby('email')['id'].count().reset_index(name='count')
print(email_counts)
```

```
      email  count
0  a@ex.com      2
1  b@ex.com      2
2  c@ex.com      1
```

### 3. Find Duplicates

```python
duplicates = email_counts[email_counts['count'] > 1]['email']
```

## LeetCode Example: Customer Orders

Find customer with most orders.

### 1. Sample Data

```python
orders = pd.DataFrame({
    'order_number': [101, 102, 103, 104, 105],
    'customer_number': [1, 1, 2, 3, 2]
})
```

### 2. Count per Customer

```python
order_counts = orders.groupby('customer_number')['order_number'].count().reset_index()
print(order_counts)
```

### 3. Find Maximum

```python
max_orders = order_counts.loc[order_counts['order_number'].idxmax()]
```

## Named Aggregations

Create descriptive column names.

### 1. Named Syntax

```python
df.groupby('asset').agg(
    mean_return=('return', 'mean'),
    std_return=('return', 'std'),
    count=('return', 'count')
)
```

### 2. Dictionary Syntax

```python
df.groupby('asset').agg({
    'return': ['mean', 'std', 'count']
})
```

### 3. Custom Functions

```python
df.groupby('asset').agg(
    range=('return', lambda x: x.max() - x.min())
)
```

## reset_index

Convert index to columns.

### 1. Default Result

```python
result = df.groupby('asset')['return'].mean()
# asset is index
```

### 2. With reset_index

```python
result = df.groupby('asset')['return'].mean().reset_index()
# asset is column
```

### 3. as_index=False

```python
result = df.groupby('asset', as_index=False)['return'].mean()
# Equivalent to reset_index()
```
