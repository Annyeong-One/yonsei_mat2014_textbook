
# sorted() and reversed()

These built-ins manipulate sequence order.

```mermaid2
flowchart TD
    A[Sequence]
    A --> B[sorted()]
    A --> C[reversed()]
````

---

## sorted()

Returns a **new sorted list**.

```python
numbers = [3,1,4,2]

print(sorted(numbers))
```

Output

```
[1,2,3,4]
```

Descending order

```python
print(sorted(numbers, reverse=True))
```

---

## Sorting Strings

```python
names = ["Charlie","Alice","Bob"]

print(sorted(names))
```

Output

```
['Alice','Bob','Charlie']
```

---

## reversed()

Returns elements in reverse order.

```python
numbers = [1,2,3]

for n in reversed(numbers):
    print(n)
```

Output

```
3
2
1
```