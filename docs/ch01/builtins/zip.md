
# zip()

The `zip()` function combines elements from multiple sequences.

```mermaid
flowchart LR
    A[List A] --> C[zip()]
    B[List B] --> C
    C --> D[Pairs]
````

---

## Basic Example

```python
names = ["Alice","Bob","Charlie"]
ages = [25,30,35]

for name, age in zip(names, ages):
    print(name, age)
```

Output

```
Alice 25
Bob 30
Charlie 35
```

---

## Three Sequences

```python
names = ["A","B","C"]
ages = [10,20,30]
scores = [80,90,85]

for n,a,s in zip(names,ages,scores):
    print(n,a,s)
```

---

## Converting zip Output

```python
pairs = list(zip(names,ages))
print(pairs)
```

Output

```
[('Alice',25), ('Bob',30), ('Charlie',35)]
```