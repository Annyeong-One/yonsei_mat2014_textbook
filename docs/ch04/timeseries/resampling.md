# Resampling and Rolling

Resampling and rolling operations summarize time series over different horizons, which is central to financial analysis.

---

## 1. Resampling

Resampling changes the frequency of a time series.

```python
s.resample("M").mean()
```

Common frequencies:
- `"D"` daily
- `"W"` weekly
- `"M"` monthly

---

## 2. OHLC aggregation

```python
prices.resample("D").ohlc()
```

This is standard for financial price data.

---

## 3. Rolling windows

Rolling operations compute statistics over moving windows.

```python
returns.rolling(20).std()
```

This computes a 20-period rolling volatility.

---

## 4. Expanding windows

```python
returns.expanding().mean()
```

Expanding windows include all data up to the current point.

---

## 5. Practical considerations

- Rolling windows introduce NaNs.
- Window size affects smoothness.
- Align windows carefully in backtests.

---

## Key takeaways

- Resampling changes time frequency.
- Rolling windows capture local behavior.
- Essential for time-series finance.
