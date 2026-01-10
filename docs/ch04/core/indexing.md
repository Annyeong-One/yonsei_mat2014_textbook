# Indexing and

Indexing is one of pandas’ most powerful (and subtle) features. Understanding selection rules is essential for correct analysis.

---

## Label-based

```python
df.loc[0]              # row with label 0
df.loc[:, "price"]     # all rows, column "price"
```

`loc` uses **labels**, not integer positions.

---

## Position-based

```python
df.iloc[0]             # first row
df.iloc[:, 0]          # first column
```

`iloc` uses zero-based integer positions.

---

## Boolean indexing

```python
df[df["price"] > 100]
```

Boolean masks must align with the index.

---

## Chained indexing

```python
df[df["price"] > 100]["volume"]
```

This can lead to ambiguous behavior and warnings.

Prefer:

```python
df.loc[df["price"] > 100, "volume"]
```

---

## Best practices

- Use `loc` / `iloc` explicitly.
- Avoid chained indexing.
- Be clear about labels vs positions.

---

## Key takeaways

- `loc` = label-based.
- `iloc` = position-based.
- Clear indexing prevents subtle bugs.
