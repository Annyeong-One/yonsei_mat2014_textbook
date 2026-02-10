# Loading CSV Files

The `pd.read_csv()` function loads comma-separated values files into DataFrames with extensive customization options.

## Basic Usage

Load a CSV file with default settings.

### 1. Simple Load

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
```

### 2. From URL

```python
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print(df.head())
```

### 3. Check Shape

```python
print(df.shape)  # (rows, columns)
```

## Keyword - index_col

Set a column as the DataFrame index.

### 1. First Column as Index

```python
df = pd.read_csv('data.csv', index_col=0)
```

### 2. Named Column as Index

```python
df = pd.read_csv('data.csv', index_col='Date')
```

### 3. Multiple Index Columns

```python
df = pd.read_csv('data.csv', index_col=[0, 1])  # MultiIndex
```

## Keyword - sep

Specify the delimiter character.

### 1. Semicolon Delimiter

```python
df = pd.read_csv('data.csv', sep=';')
```

### 2. Tab Delimiter

```python
df = pd.read_csv('data.tsv', sep='\t')
```

### 3. Custom Delimiter

```python
df = pd.read_csv('data.txt', sep='|')
```

## Keyword - header

Control which row becomes column names.

### 1. Default (Infer)

```python
df = pd.read_csv('data.csv')  # header='infer'
# First row becomes column names
```

### 2. No Header

```python
df = pd.read_csv('data.csv', header=None)
# Columns named 0, 1, 2, ...
```

### 3. Specific Row

```python
df = pd.read_csv('data.csv', header=2)
# Row 2 becomes header, rows 0-1 skipped
```

## Keyword - names

Provide custom column names.

### 1. Override Columns

```python
names = ['A', 'B', 'C', 'D']
df = pd.read_csv('data.csv', names=names, header=0)
```

### 2. With No Header

```python
df = pd.read_csv('data.csv', names=names, header=None)
```

### 3. Partial Names

```python
# Must provide names for all columns
```

## Keyword - skiprows

Skip rows at the beginning.

### 1. Skip N Rows

```python
df = pd.read_csv('data.csv', skiprows=3)
# Skips first 3 rows
```

### 2. Skip Specific Rows

```python
df = pd.read_csv('data.csv', skiprows=[0, 2, 4])
# Skips rows 0, 2, and 4
```

### 3. Skip with Function

```python
df = pd.read_csv('data.csv', skiprows=lambda x: x in [0, 1, 2])
```

## Keyword - usecols

Select specific columns to load.

### 1. By Name

```python
df = pd.read_csv('data.csv', usecols=['Name', 'Age', 'City'])
```

### 2. By Index

```python
df = pd.read_csv('data.csv', usecols=[0, 2, 4])
```

### 3. Memory Efficiency

```python
# Loading only needed columns saves memory
```

## Keyword - parse_dates

Parse columns as datetime.

### 1. Single Column

```python
df = pd.read_csv('data.csv', parse_dates=['Date'])
```

### 2. Multiple Columns

```python
df = pd.read_csv('data.csv', parse_dates=['Start', 'End'])
```

### 3. With Index

```python
df = pd.read_csv('data.csv', index_col='Date', parse_dates=True)
```

## Keyword - dayfirst

European date format (day before month).

### 1. Enable dayfirst

```python
# For dates like 31/12/2024 (day/month/year)
df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)
```

### 2. Default (Month First)

```python
# For dates like 12/31/2024 (month/day/year)
df = pd.read_csv('data.csv', parse_dates=['Date'])
```

### 3. Combined Usage

```python
df = pd.read_csv(
    'data.csv',
    index_col=0,
    parse_dates=True,
    dayfirst=True
)
```

## Real-World Example

Load financial data with multiple options.

### 1. Stock Data

```python
url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
names = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF']

df = pd.read_csv(
    url,
    index_col=0,
    parse_dates=True,
    dayfirst=True,
    sep=';',
    header=None,
    skiprows=4,
    names=names
)
```

### 2. Verify Load

```python
print(df.head())
print(df.index[:3])
print(df.columns)
```

### 3. Handle Inconsistent Data

```python
# Use skiprows with lambda for complex skip logic
df = pd.read_csv(
    url,
    skiprows=lambda x: (x in [0,1,2,3]) or (x >= 3886)
)
```
