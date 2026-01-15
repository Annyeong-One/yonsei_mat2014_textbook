# DatetimeIndex

pandas provides rich support for time series data through the **DatetimeIndex**, which enables label-based time alignment and slicing.

## Creating DatetimeIndex

Generate datetime indices for time series.

### 1. date_range Function

```python
import pandas as pd

dates = pd.date_range("2020-01-01", periods=5, freq="D")
print(dates)
```

```
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05'],
              dtype='datetime64[ns]', freq='D')
```

### 2. With End Date

```python
dates = pd.date_range(start="2024-01-01", end="2024-01-10")
```

### 3. Nanosecond Precision

DatetimeIndex stores timestamps with nanosecond precision.

## Converting to Datetime

Parse strings and other formats to datetime.

### 1. to_datetime Function

```python
pd.to_datetime(["2021-01-01", "2021-01-05"])
```

### 2. Common with CSV Loading

```python
df = pd.read_csv('data.csv', parse_dates=['date_column'])
```

### 3. Format Specification

```python
pd.to_datetime("01-15-2024", format="%m-%d-%Y")
```

## Date Range Frequencies

Common frequency strings.

### 1. Daily and Sub-daily

```python
pd.date_range("2024-01-01", periods=5, freq="D")   # Daily
pd.date_range("2024-01-01", periods=5, freq="H")   # Hourly
pd.date_range("2024-01-01", periods=5, freq="T")   # Minute
```

### 2. Weekly and Monthly

```python
pd.date_range("2024-01-01", periods=5, freq="W")   # Weekly
pd.date_range("2024-01-01", periods=5, freq="M")   # Month end
pd.date_range("2024-01-01", periods=5, freq="MS")  # Month start
```

### 3. Business Days

```python
pd.date_range("2024-01-01", periods=5, freq="B")   # Business days
```

## Indexing with Dates

Date-based slicing and selection.

### 1. String-based Selection

```python
s = pd.Series(range(5), index=pd.date_range("2020-01-01", periods=5))
s["2020-01-02":"2020-01-04"]  # Inclusive slicing
```

### 2. Partial String Indexing

```python
s["2020-01"]  # All of January 2020
s["2020"]     # All of 2020
```

### 3. loc with Dates

```python
s.loc["2020-01-02"]
s.loc["2020-01-02":"2020-01-04"]
```

## Time Zone Handling

Work with time zones.

### 1. Localize to UTC

```python
dates = pd.date_range("2020-01-01", periods=5)
dates_utc = dates.tz_localize("UTC")
```

### 2. Convert Time Zone

```python
dates_eastern = dates_utc.tz_convert("US/Eastern")
```

### 3. Financial Data

Time zones are essential for global financial data.

## Financial Context

DatetimeIndex underlies financial analysis.

### 1. Price Time Series

```python
prices = pd.Series([100, 101, 102], index=pd.date_range("2024-01-01", periods=3))
```

### 2. Returns Calculation

```python
returns = prices.pct_change()
```

### 3. Event Studies

```python
# Select specific date ranges for analysis
event_window = prices["2024-01-01":"2024-01-31"]
```
