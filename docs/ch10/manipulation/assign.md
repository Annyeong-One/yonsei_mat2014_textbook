# assign Method

The `assign()` method adds new columns to a DataFrame, returning a new DataFrame with the additions.

## Basic Usage

Add new columns.

### 1. Single Column

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'salary': [50000, 60000, 70000]
})

df = df.assign(bonus=5000)
print(df)
```

```
      name  salary  bonus
0    Alice   50000   5000
1      Bob   60000   5000
2  Charlie   70000   5000
```

### 2. Multiple Columns

```python
df = df.assign(
    bonus=5000,
    tax_rate=0.25
)
```

### 3. Returns New DataFrame

```python
# Original unchanged unless reassigned
new_df = df.assign(bonus=5000)
```

## Computed Columns

Create columns based on existing data.

### 1. From Other Columns

```python
df = df.assign(
    total_comp=df['salary'] + 5000
)
```

### 2. Using Lambda

```python
df = df.assign(
    total_comp=lambda x: x['salary'] + 5000
)
```

### 3. Multiple Computed

```python
df = df.assign(
    bonus=lambda x: x['salary'] * 0.1,
    tax=lambda x: x['salary'] * 0.25,
    net=lambda x: x['salary'] - x['salary'] * 0.25
)
```

## Lambda Advantage

Lambda functions access the DataFrame being created.

### 1. Chain Dependencies

```python
df = df.assign(
    bonus=lambda x: x['salary'] * 0.1,
    total=lambda x: x['salary'] + x['bonus']  # Uses bonus just created
)
```

### 2. Order Matters

```python
# This works because bonus is created first
df.assign(
    bonus=df['salary'] * 0.1,
    total=lambda x: x['salary'] + x['bonus']
)
```

### 3. Without Lambda Issue

```python
# This fails if bonus column doesn't exist yet
# df.assign(
#     bonus=df['salary'] * 0.1,
#     total=df['salary'] + df['bonus']  # Error!
# )
```

## LeetCode Example: Restaurant Growth

Calculate rolling sums and averages.

### 1. Sample Data

```python
df = pd.DataFrame({
    'visited_on': pd.date_range('2024-07-15', periods=7),
    'amount': [30.0, 20.0, 40.0, 10.0, 50.0, 20.0, 60.0]
})
df = df.set_index('visited_on')
```

### 2. Rolling Calculation

```python
rolling_sum = df['amount'].rolling('7D').sum()
```

### 3. Assign Multiple Columns

```python
df = df.assign(
    amount=rolling_sum,
    average_amount=round(rolling_sum / 7, 2)
)
print(df)
```

```
            amount  average_amount
visited_on                        
2024-07-15    30.0            4.29
2024-07-16    50.0            7.14
2024-07-17    90.0           12.86
2024-07-18   100.0           14.29
2024-07-19   150.0           21.43
2024-07-20   170.0           24.29
2024-07-21   230.0           32.86
```

## Method Chaining

assign works well in method chains.

### 1. Chain Operations

```python
result = (
    df
    .assign(bonus=lambda x: x['salary'] * 0.1)
    .assign(total=lambda x: x['salary'] + x['bonus'])
    .query('total > 60000')
)
```

### 2. Multiple assigns

```python
result = (
    df
    .assign(year=lambda x: x['date'].dt.year)
    .assign(month=lambda x: x['date'].dt.month)
    .groupby(['year', 'month'])
    .sum()
)
```

### 3. With Other Methods

```python
result = (
    df
    .dropna()
    .assign(calculated=lambda x: x['a'] + x['b'])
    .sort_values('calculated')
)
```

## Overwriting Columns

assign can replace existing columns.

### 1. Replace Column

```python
df = df.assign(salary=df['salary'] * 1.1)  # 10% raise
```

### 2. Transform Column

```python
df = df.assign(name=df['name'].str.upper())
```

### 3. Multiple Transforms

```python
df = df.assign(
    salary=lambda x: x['salary'] * 1.1,
    name=lambda x: x['name'].str.title()
)
```

## vs Direct Assignment

Compare assign to direct column assignment.

### 1. Direct Assignment

```python
df['bonus'] = 5000  # Modifies df in place
```

### 2. assign Method

```python
df = df.assign(bonus=5000)  # Returns new DataFrame
```

### 3. When to Use Each

```python
# Direct: quick modifications
# assign: method chaining, functional style
```
