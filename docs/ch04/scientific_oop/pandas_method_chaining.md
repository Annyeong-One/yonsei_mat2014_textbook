# Method Chaining

## Fluent Interface

### 1. Concept

Method chaining returns self or new object:

```python
import pandas as pd

df = (pd.read_csv('data.csv')
      .dropna()
      .query('age > 25')
      .sort_values('name')
      .reset_index(drop=True))
```

### 2. Benefits

- Readable pipeline
- No intermediate variables
- Functional style

### 3. Design Pattern

Methods return DataFrame/Series:

```python
class DataFrame:
    def dropna(self):
        # ... operation
        return new_dataframe
```

## Common Chains

### 1. Cleaning Pipeline

```python
df_clean = (df
    .drop_duplicates()
    .dropna(subset=['key_column'])
    .replace({'old': 'new'})
    .reset_index(drop=True))
```

### 2. Transformation

```python
result = (df
    .assign(total=lambda x: x['a'] + x['b'])
    .pipe(lambda x: x[x['total'] > 10])
    .groupby('category')['total']
    .mean())
```

### 3. Aggregation

```python
summary = (df
    .groupby(['year', 'month'])
    .agg({'sales': 'sum', 'profit': 'mean'})
    .round(2))
```

## Pipe Method

### 1. Custom Functions

```python
def remove_outliers(df, column):
    mean = df[column].mean()
    std = df[column].std()
    return df[abs(df[column] - mean) < 2*std]

result = (df
    .pipe(remove_outliers, 'price')
    .pipe(remove_outliers, 'quantity'))
```

### 2. Lambda Functions

```python
result = (df
    .pipe(lambda x: x[x['age'] > 18])
    .pipe(lambda x: x.assign(adult=True)))
```

### 3. Method Injection

```python
df.pipe(print)  # Debug intermediate state
```
