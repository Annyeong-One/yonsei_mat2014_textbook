# DatetimeIndex

pandas provides rich support for time series data through the **DatetimeIndex**, which enables label-based time alignment and slicing.

---

## 1. Creating a DatetimeIndex

```python
import pandas as pd

dates = pd.date_range("2020-01-01", periods=5, freq="D")
```

DatetimeIndex stores timestamps with nanosecond precision.

---

## 2. Converting to datetime

```python
pd.to_datetime(["2021-01-01", "2021-01-05"])
```

This is commonly used when loading data from CSV files.

---

## 3. Indexing with dates

```python
s = pd.Series(range(5), index=dates)
s["2020-01-02":"2020-01-04"]
```

Date-based slicing is inclusive.

---

## 4. Time zone handling

```python
dates.tz_localize("UTC")
dates.tz_convert("US/Eastern")
```

Time zones are essential for global financial data.

---

## 5. Financial context

DatetimeIndex underlies:
- price time series,
- returns and volatilities,
- event studies.

---

## Key takeaways

- DatetimeIndex enables time-aware indexing.
- `to_datetime` standardizes timestamps.
- Time zones must be handled explicitly.
