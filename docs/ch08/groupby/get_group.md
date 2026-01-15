# get_group Method

The `get_group()` method retrieves a specific group from a GroupBy object by its key.

## Basic Usage

Access a single group by name.

### 1. Get Single Group

```python
import pandas as pd

data = {
    'day': ['1/1/20', '1/2/20', '1/1/20', '1/2/20', '1/1/20', '1/2/20'],
    'city': ['NY', 'NY', 'SF', 'SF', 'LA', 'LA'],
    'temperature': [21, 14, 25, 32, 36, 42],
    'humidity': [31, 15, 36, 22, 16, 29],
}
df = pd.DataFrame(data)

dg = df.groupby("city")
print(dg.get_group("NY"))
```

```
      day city  temperature  humidity
0  1/1/20   NY           21        31
1  1/2/20   NY           14        15
```

### 2. Returns DataFrame

The result is a DataFrame containing only rows for that group.

### 3. Original Index Preserved

Row indices from the original DataFrame are kept.

## Multiple Group Keys

Access groups with compound keys.

### 1. Tuple Key

```python
grouped = df.groupby(['city', 'day'])
ny_jan1 = grouped.get_group(('NY', '1/1/20'))
print(ny_jan1)
```

### 2. Key Must Match

```python
# Must provide all grouping columns
# grouped.get_group('NY')  # Error: need both city and day
```

### 3. Order Matters

```python
# Tuple order must match groupby column order
grouped.get_group(('NY', '1/1/20'))  # Correct
# grouped.get_group(('1/1/20', 'NY'))  # Wrong order
```

## Use Cases

When to use get_group.

### 1. Inspect Specific Group

```python
# Debug or examine one group
ny_data = df.groupby('city').get_group('NY')
print(ny_data.describe())
```

### 2. Filter by Group

```python
# Alternative to boolean indexing
# These are equivalent:
df[df['city'] == 'NY']
df.groupby('city').get_group('NY')
```

### 3. Compare Groups

```python
grouped = df.groupby('city')
ny = grouped.get_group('NY')
sf = grouped.get_group('SF')

print(f"NY mean: {ny['temperature'].mean()}")
print(f"SF mean: {sf['temperature'].mean()}")
```

## Error Handling

Handle missing groups.

### 1. KeyError for Missing

```python
try:
    df.groupby('city').get_group('Tokyo')
except KeyError:
    print("Group 'Tokyo' not found")
```

### 2. Check Available Groups

```python
grouped = df.groupby('city')
print(list(grouped.groups.keys()))
# ['LA', 'NY', 'SF']
```

### 3. Safe Access

```python
grouped = df.groupby('city')
if 'Tokyo' in grouped.groups:
    tokyo_data = grouped.get_group('Tokyo')
else:
    print("No data for Tokyo")
```

## Performance

get_group vs boolean indexing.

### 1. Single Access

```python
# Similar performance for single access
df[df['city'] == 'NY']
df.groupby('city').get_group('NY')
```

### 2. Multiple Accesses

```python
# GroupBy is faster for multiple accesses
grouped = df.groupby('city')  # Create once
ny = grouped.get_group('NY')
sf = grouped.get_group('SF')
la = grouped.get_group('LA')
```

### 3. Best Practice

```python
# Create GroupBy object once, reuse for multiple operations
```
