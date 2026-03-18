
# min(), max(), sum()

These built-ins perform basic numeric aggregation.

```mermaid
flowchart LR
    A[Numbers]
    A --> B[min()]
    A --> C[max()]
    A --> D[sum()]
````

---

## min()

Returns smallest value.

```python
numbers = [5,2,9,1]

print(min(numbers))
```

Output

```
1
```

---

## max()

Returns largest value.

```python
print(max(numbers))
```

Output

```
9
```

---

## sum()

Computes total.

```python
print(sum(numbers))
```

Output

```
17
```