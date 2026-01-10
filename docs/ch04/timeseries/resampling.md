# Resampling and

Resampling and rolling operations summarize time series over different horizons, which is central to financial analysis.

---

## Resampling

Resampling changes the frequency of a time series.

```python
s.resample("M").mean()
```

Common frequencies:
- `"D"` daily
- `"W"` weekly
- `"M"` monthly

---

## OHLC aggregation

```python
prices.resample("D").ohlc()
```

This is standard for financial price data.

---

## Rolling windows

Rolling operations compute statistics over moving windows.

```python
returns.rolling(20).std()
```

This computes a 20-period rolling volatility.

---

## Expanding windows

```python
returns.expanding().mean()
```

Expanding windows include all data up to the current point.

---

## Practical

- Rolling windows introduce NaNs.
- Window size affects smoothness.
- Align windows carefully in backtests.

---

## Key takeaways

- Resampling changes time frequency.
- Rolling windows capture local behavior.
- Essential for time-series finance.
