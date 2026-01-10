# GroupBy and Aggregation

Grouping and aggregation are central to data wrangling in pandas, allowing you to summarize and transform data efficiently.

---

## 1. The GroupBy concept

`groupby` splits data into groups, applies a function, and combines the results.

```python
import pandas as pd

df = pd.DataFrame({
    "asset": ["A", "A", "B", "B"],
    "return": [0.01, -0.02, 0.03, 0.01],
})
```

---

## 2. Basic aggregation

```python
df.groupby("asset")["return"].mean()
```

Common aggregations:
- `mean`
- `sum`
- `count`
- `std`

---

## 3. Multiple aggregations

```python
df.groupby("asset")["return"].agg(["mean", "std"])
```

Or across columns:

```python
df.groupby("asset").agg({"return": "mean"})
```

---

## 4. GroupBy objects

A GroupBy object is lazy:
- no computation until aggregation,
- supports chaining.

```python
g = df.groupby("asset")
g.mean()
```

---

## 5. Financial use cases

GroupBy is used for:
- asset-level returns,
- sector aggregation,
- factor portfolio construction.

---

## Key takeaways

- `groupby` enables split–apply–combine.
- Aggregations summarize data efficiently.
- Essential for financial data analysis.
