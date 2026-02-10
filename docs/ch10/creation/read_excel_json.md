# Loading Excel and JSON

pandas supports loading data from Excel spreadsheets, JSON files, and other formats.

## pd.read_excel

Load Excel files (.xlsx, .xls).

### 1. Basic Load

```python
import pandas as pd

df = pd.read_excel('data.xlsx')
print(df.head())
```

### 2. From URL

```python
url = 'https://example.com/data.xlsx?raw=true'
df = pd.read_excel(url, sheet_name='Sheet1')
```

### 3. Specify Sheet

```python
# By name
df = pd.read_excel('data.xlsx', sheet_name='Sales')

# By index (0-based)
df = pd.read_excel('data.xlsx', sheet_name=0)
```

## Excel Keywords

Customize Excel loading.

### 1. Multiple Sheets

```python
# Load all sheets as dictionary
dfs = pd.read_excel('data.xlsx', sheet_name=None)
# dfs['Sheet1'], dfs['Sheet2'], etc.
```

### 2. Skip Rows

```python
df = pd.read_excel('data.xlsx', skiprows=2)
```

### 3. Use Columns

```python
df = pd.read_excel('data.xlsx', usecols='A:D')
# or
df = pd.read_excel('data.xlsx', usecols=[0, 1, 2, 3])
```

## pd.read_json

Load JSON files into DataFrames.

### 1. Basic Load

```python
df = pd.read_json('data.json')
print(df.head())
```

### 2. From URL

```python
url = 'https://raw.githubusercontent.com/example/data.json'
df = pd.read_json(url)
```

### 3. JSON Structure

```python
# JSON should be array of objects or object of arrays
# [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
```

## JSON Orientations

Different JSON structures.

### 1. Records Orient

```python
# JSON: [{"col1": 1, "col2": 2}, ...]
df = pd.read_json('data.json', orient='records')
```

### 2. Columns Orient

```python
# JSON: {"col1": [1, 2], "col2": [3, 4]}
df = pd.read_json('data.json', orient='columns')
```

### 3. Index Orient

```python
# JSON: {"row1": {"col1": 1}, "row2": {"col1": 2}}
df = pd.read_json('data.json', orient='index')
```

## pd.read_table

Load delimited files with read_table.

### 1. Pipe Delimiter

```python
df = pd.read_table('data.txt', sep='|')
```

### 2. With Header

```python
names = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
df = pd.read_table(
    'data.txt',
    sep='|',
    header=None,
    names=names
)
```

### 3. Select Columns

```python
df = pd.read_table(
    'data.txt',
    sep='|',
    usecols=['age', 'gender', 'occupation']
)
```

## pd.read_fwf

Load fixed-width formatted files.

### 1. Basic Load

```python
df = pd.read_fwf('data.txt')
print(df.head())
```

### 2. Specify Widths

```python
df = pd.read_fwf('data.txt', widths=[10, 5, 8, 12])
```

### 3. Column Positions

```python
df = pd.read_fwf('data.txt', colspecs=[(0, 10), (10, 15), (15, 23)])
```

## pd.HDFStore

Load HDF5 files for large datasets.

### 1. Open Store

```python
h5 = pd.HDFStore('data.h5', 'r')
print(h5.keys())
```

### 2. Read Data

```python
df = h5['/table_name']
# or
df = h5['table_name']
```

### 3. Close Store

```python
h5.close()

# Or use context manager
with pd.HDFStore('data.h5', 'r') as h5:
    df = h5['table_name']
```

## Comparison

When to use each format.

### 1. CSV

- Universal compatibility
- Human-readable
- Good for medium data

### 2. Excel

- Preserves formatting
- Multiple sheets
- Good for business users

### 3. JSON

- Web API responses
- Nested structures
- JavaScript integration

### 4. HDF5

- Large datasets
- Fast I/O
- Scientific computing
