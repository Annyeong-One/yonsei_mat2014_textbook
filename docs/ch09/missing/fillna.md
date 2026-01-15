# fillna Method

The `fillna()` method replaces missing values with specified values. It is one of the most common approaches to handling missing data.

## Single Value Fill

Replace all NaN values with a single value.

### 1. Constant Value

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'temperature': [21, np.nan, 25, np.nan],
    'humidity': [65, 68, np.nan, 75]
})

dg = df.fillna(0)
print(dg)
```

```
   temperature  humidity
0         21.0      65.0
1          0.0      68.0
2         25.0       0.0
3          0.0      75.0
```

### 2. Mean Fill

```python
df['temperature'].fillna(df['temperature'].mean())
```

### 3. Median Fill

```python
df['temperature'].fillna(df['temperature'].median())
```

## Column-specific Fill

Use a dictionary to specify different fill values per column.

### 1. Dictionary Mapping

```python
url = "https://raw.githubusercontent.com/codebasics/py/master/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv"
df = pd.read_csv(url, index_col='day', parse_dates=True)

dg = df.fillna({
    "temperature": 30,
    "windspeed": df.windspeed.mean(),
    "event": "No Event",
})
print(dg)
```

### 2. Computed Values

```python
fill_values = {
    'temperature': df['temperature'].mean(),
    'humidity': df['humidity'].median()
}
df.fillna(fill_values)
```

### 3. Conditional Fill

```python
df['temperature'] = df['temperature'].fillna(
    df.groupby('region')['temperature'].transform('mean')
)
```

## inplace Parameter

Modify the DataFrame directly without creating a copy.

### 1. Without inplace

```python
dg = df.fillna(0)  # Returns new DataFrame
# df is unchanged
```

### 2. With inplace

```python
df.fillna(0, inplace=True)  # Modifies df directly
```

### 3. Modern Practice

Prefer reassignment over `inplace=True`:

```python
df = df.fillna(0)  # More explicit
```

## LeetCode Example

Fill referee_id with 0 for customers without referrer.

### 1. Problem Context

```python
customer = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'referee_id': [1.0, 2.0, np.nan, 3.0, np.nan]
})
```

### 2. Fill NaN Values

```python
customer["referee_id"].fillna(0)
```

### 3. Result

```
0    1.0
1    2.0
2    0.0
3    3.0
4    0.0
Name: referee_id, dtype: float64
```

## Dictionary Fill Example

Fill missing prices with 0.0 in sales data.

### 1. Sample Data

```python
sold_with_prices = pd.DataFrame({
    'product_id': [1, 1, 2],
    'purchase_date': ['2024-01-15', '2024-05-10', '2024-07-01'],
    'units': [10, 5, 8],
    'price': [100, None, 180]
})
```

### 2. Fill with Dictionary

```python
sold_with_prices.fillna({'price': 0.0}, inplace=True)
```

### 3. Resulting DataFrame

```
   product_id purchase_date  units  price
0           1    2024-01-15     10  100.0
1           1    2024-05-10      5    0.0
2           2    2024-07-01      8  180.0
```
