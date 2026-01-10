# Merge and Join

Merging and joining combine datasets based on keys, similar to SQL joins. pandas provides flexible and explicit tools for this.

---

## 1. Merge vs join

- `merge`: column-based joins
- `join`: index-based joins

```python
pd.merge(left, right, on="key")
```

---

## 2. Join types

Supported joins:
- `inner`
- `left`
- `right`
- `outer`

```python
pd.merge(df1, df2, on="id", how="left")
```

---

## 3. Handling overlapping columns

```python
pd.merge(df1, df2, on="id", suffixes=("_x", "_y"))
```

Always inspect results carefully.

---

## 4. Index-based joins

```python
df1.join(df2)
```

Useful for time-series alignment.

---

## 5. Financial applications

Merges are common for:
- joining prices with fundamentals,
- combining signals,
- aligning market and reference data.

---

## Key takeaways

- `merge` is explicit and flexible.
- Join type controls row retention.
- Correct joins are critical for data integrity.
