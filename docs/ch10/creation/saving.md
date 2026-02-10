# Saving DataFrames

Export DataFrames to various file formats for storage and sharing.

## to_csv

Save DataFrame to CSV file.

### 1. Basic Save

```python
import pandas as pd

df.to_csv('output.csv')
```

### 2. Without Index

```python
df.to_csv('output.csv', index=False)
```

### 3. Custom Separator

```python
df.to_csv('output.tsv', sep='\t')
```

## to_csv Keywords

Customize CSV output.

### 1. Select Columns

```python
df.to_csv('output.csv', columns=['Name', 'Age'])
```

### 2. Handle Missing

```python
df.to_csv('output.csv', na_rep='NULL')
```

### 3. Float Format

```python
df.to_csv('output.csv', float_format='%.2f')
```

## to_excel

Save DataFrame to Excel file.

### 1. Basic Save

```python
df.to_excel('output.xlsx')
```

### 2. Specify Sheet Name

```python
df.to_excel('output.xlsx', sheet_name='Data')
```

### 3. Without Index

```python
df.to_excel('output.xlsx', index=False)
```

## Multiple Sheets

Save multiple DataFrames to one Excel file.

### 1. ExcelWriter

```python
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
    df3.to_excel(writer, sheet_name='Sheet3')
```

### 2. Append Mode

```python
with pd.ExcelWriter('output.xlsx', mode='a') as writer:
    df_new.to_excel(writer, sheet_name='NewSheet')
```

### 3. Engine Selection

```python
# openpyxl for .xlsx, xlsxwriter for formatting
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
    df.to_excel(writer)
```

## to_json

Save DataFrame to JSON file.

### 1. Basic Save

```python
df.to_json('output.json')
```

### 2. Orient Options

```python
df.to_json('output.json', orient='records')  # List of dicts
df.to_json('output.json', orient='columns')  # Dict of lists
df.to_json('output.json', orient='index')    # Dict of dicts
```

### 3. Indent for Readability

```python
df.to_json('output.json', orient='records', indent=2)
```

## to_pickle

Save DataFrame in pickle format.

### 1. Save Pickle

```python
df.to_pickle('output.pkl')
```

### 2. Load Pickle

```python
df = pd.read_pickle('output.pkl')
```

### 3. Compression

```python
df.to_pickle('output.pkl.gz', compression='gzip')
```

## to_parquet

Save in Parquet format (efficient columnar storage).

### 1. Basic Save

```python
df.to_parquet('output.parquet')
```

### 2. Compression

```python
df.to_parquet('output.parquet', compression='snappy')
```

### 3. Read Back

```python
df = pd.read_parquet('output.parquet')
```

## Financial Example

Save stock data workflow.

### 1. Download and Save

```python
import yfinance as yf

ticker = 'WMT'
df = yf.Ticker(ticker).history(start='2020-01-01', end='2020-12-31')

# Save to CSV
df.to_csv(f'{ticker}.csv')

# Save to Excel
df.to_excel(f'{ticker}.xlsx', sheet_name='stocks')
```

### 2. Multiple Tickers

```python
tickers = ['AAPL', 'MSFT', 'GOOGL']

with pd.ExcelWriter('portfolio.xlsx') as writer:
    for ticker in tickers:
        df = yf.Ticker(ticker).history(period='1y')
        df.to_excel(writer, sheet_name=ticker)
```

### 3. Pickle for Speed

```python
# Faster save/load for large DataFrames
df.to_pickle('large_data.pkl')
df = pd.read_pickle('large_data.pkl')
```

## Format Comparison

Choose the right format.

### 1. CSV

- Pros: Universal, human-readable
- Cons: No type preservation, slow for large data

### 2. Excel

- Pros: Business-friendly, multiple sheets
- Cons: Slower, file size limits

### 3. Pickle

- Pros: Fast, preserves types
- Cons: Python-only, security concerns

### 4. Parquet

- Pros: Fast, compressed, columnar
- Cons: Less universal
