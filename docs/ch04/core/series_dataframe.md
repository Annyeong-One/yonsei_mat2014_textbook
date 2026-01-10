# Series and DataFrame

pandas provides two core data structures for tabular and time-series data: **Series** and **DataFrame**. They are built on top of NumPy arrays with rich indexing and metadata.

---

## Series

A **Series** is a one-dimensional labeled array.

```python
import pandas as pd

s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
```

Key properties:
- values (NumPy array)
- index (labels)
- dtype

---

## Accessing Series

```python
s["a"]     # label-based
s.iloc[0]  # position-based
```

Labels and positions are distinct concepts.

---

## DataFrame

A **DataFrame** is a two-dimensional table of labeled columns.

```python
df = pd.DataFrame({
    "price": [100, 101, 102],
    "volume": [10, 12, 9],
})
```

Each column is a Series sharing a common index.

---

## Column access

```python
df["price"]
df.price    # attribute access (use cautiously)
```

---

## Financial context

DataFrames are used for:
- price histories,
- factor data,
- returns and risk metrics,
- panel-style datasets.

---

## Key takeaways

- Series = labeled 1D data.
- DataFrame = labeled 2D data.
- Indexing is central to pandas.
