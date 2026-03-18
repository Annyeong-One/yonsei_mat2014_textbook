
# any() and all()

Logical built-ins evaluate collections of boolean values.

```mermaid
flowchart LR
    A[Iterable]
    A --> B[any()]
    A --> C[all()]
````

---

## any()

Returns True if **any element is True**.

```python
values = [False, False, True]

print(any(values))
```

Output

```
True
```

---

## all()

Returns True if **all elements are True**.

```python
values = [True, True, True]

print(all(values))
```

Output

```
True
```