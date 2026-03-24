# concat vs append vs merge

Pandas provides multiple functions for combining DataFrames, and choosing the wrong one can produce incorrect results or unnecessary performance overhead. The three main options — `pd.concat`, `DataFrame.append`, and `pd.merge` — serve different purposes. This page clarifies when to use each and how they differ in behavior, performance, and API design.

```python
import pandas as pd
```

---

## Quick Comparison

| Feature | `pd.concat` | `DataFrame.append` | `pd.merge` |
|---------|------------|-------------------|-----------|
| Purpose | Stack along an axis | Shortcut for vertical concat | Join on columns/index |
| Axis | Row or column | Row only | N/A (column-based join) |
| Input | List of DataFrames | Single DataFrame or dict | Two DataFrames |
| Join type | Outer/inner (on the other axis) | Outer/inner | Left/right/outer/inner |
| Key columns | No (uses index alignment) | No | Yes (`on`, `left_on`, `right_on`) |
| Status | Active | Deprecated since pandas 1.4 | Active |

---

## pd.concat — Stacking DataFrames

`pd.concat` stacks multiple DataFrames along a specified axis. It aligns on the **other** axis using index or column labels.

```python
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

# Vertical stacking (axis=0, the default)
result = pd.concat([df1, df2], ignore_index=True)
print(result)
```

```
   A  B
0  1  3
1  2  4
2  5  7
3  6  8
```

Use `pd.concat` when you need to stack two or more DataFrames that share the same columns (vertical) or the same index (horizontal).

---

## DataFrame.append — Deprecated Shortcut

`DataFrame.append` was a convenience wrapper around `pd.concat` for vertical stacking of a single DataFrame. It was deprecated in pandas 1.4 and removed in pandas 2.0.

```python
# Before pandas 2.0 (deprecated)
# result = df1.append(df2, ignore_index=True)

# Equivalent using pd.concat (recommended)
result = pd.concat([df1, df2], ignore_index=True)
```

!!! warning "append Is Removed in pandas 2.0"
    If you encounter `DataFrame.append` in existing code, replace it with `pd.concat`. The behavior is identical for single-DataFrame appends: `df1.append(df2)` is equivalent to `pd.concat([df1, df2])`.

### Why append Was Deprecated

Each call to `append` created a new DataFrame by copying all data. In a loop, this leads to quadratic time complexity because each iteration copies all previously appended rows.

```python
# Slow: O(n²) due to repeated copying
result = pd.DataFrame()
for chunk in data_chunks:
    result = pd.concat([result, chunk])  # still copies each time

# Fast: O(n) — collect first, concat once
result = pd.concat(data_chunks, ignore_index=True)
```

---

## pd.merge — Joining on Keys

`pd.merge` performs database-style joins on column values or index labels. Unlike `pd.concat`, it matches rows based on shared key values rather than stacking by position.

```python
orders = pd.DataFrame({
    "order_id": [1, 2, 3],
    "product_id": [101, 102, 103]
})

products = pd.DataFrame({
    "product_id": [101, 102, 104],
    "name": ["Widget", "Gadget", "Doohickey"]
})

# Inner join on product_id
result = pd.merge(orders, products, on="product_id")
print(result)
```

```
   order_id  product_id    name
0         1         101  Widget
1         2         102  Gadget
```

Use `pd.merge` when you need to combine DataFrames based on matching values in one or more key columns, similar to SQL JOIN operations.

---

## Side-by-Side Example

The following example uses the same two DataFrames to show how concat and merge produce different results.

```python
df_left = pd.DataFrame({
    "key": ["a", "b", "c"],
    "value_left": [1, 2, 3]
})

df_right = pd.DataFrame({
    "key": ["b", "c", "d"],
    "value_right": [4, 5, 6]
})
```

### concat (vertical stack)

```python
stacked = pd.concat([df_left, df_right], ignore_index=True)
print(stacked)
```

```
  key  value_left  value_right
0   a         1.0          NaN
1   b         2.0          NaN
2   c         3.0          NaN
3   b         NaN          4.0
4   c         NaN          5.0
5   d         NaN          6.0
```

Concat stacks the rows without matching on the `key` column. Missing columns are filled with `NaN`.

### merge (join on key)

```python
joined = pd.merge(df_left, df_right, on="key")
print(joined)
```

```
  key  value_left  value_right
0   b           2            4
1   c           3            5
```

Merge matches rows where `key` values agree, discarding non-matching rows (inner join by default).

---

## Decision Guide

Use the following rules to choose between the three operations.

1. **Stacking rows with the same columns** — use `pd.concat` with `axis=0`
2. **Stacking columns with the same index** — use `pd.concat` with `axis=1`
3. **Joining on shared key columns** — use `pd.merge`
4. **`DataFrame.append`** — do not use; replace with `pd.concat`

!!! tip "Performance Rule"
    When combining many DataFrames in a loop, collect them in a list first and call `pd.concat` once at the end. Repeated concatenation inside a loop copies all previous data on every iteration.

---

## Summary

| Operation | When to Use |
|-----------|-------------|
| `pd.concat([df1, df2])` | Stack DataFrames vertically or horizontally by position |
| `pd.merge(df1, df2, on=...)` | Join DataFrames on matching key column values |
| `df1.append(df2)` | Never — deprecated and removed; use `pd.concat` instead |

**Key Takeaways**:

- `pd.concat` stacks by position along an axis; `pd.merge` matches rows by key values
- `DataFrame.append` was removed in pandas 2.0 — always use `pd.concat` instead
- Collect DataFrames in a list and concat once to avoid quadratic copying overhead
- Choose `merge` for database-style joins and `concat` for simple stacking operations
