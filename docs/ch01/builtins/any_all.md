
# any() and all()

Python provides `any()` and `all()` to test whether any or all elements in an iterable satisfy a condition, which is useful for validating collections of boolean values in a single expression.

```mermaid
flowchart LR
    A[Iterable]
    A --> B[any()]
    A --> C[all()]
```

## any()

Returns True if **any element is True**.

```python
values = [False, False, True]

print(any(values))
```

Output:

```
True
```

## all()

Returns True if **all elements are True**.

```python
values = [True, True, True]

print(all(values))
```

Output:

```
True
```
