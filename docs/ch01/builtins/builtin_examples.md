

# Built-in Usage Examples

This section demonstrates how multiple built-ins combine in real programs.

---

## Example: Average Calculator

```python
numbers = [10,20,30]

avg = sum(numbers)/len(numbers)

print(avg)
````

---

## Example: Zipping Data

```python
names = ["Alice","Bob"]
scores = [90,85]

for name,score in zip(names,scores):
    print(name,score)
```

---

## Example: Filtering Data

```python
values = [0,1,2,3]

print(any(values))
print(all(values))
```

---

## Example: Sorting

```python
numbers = [3,1,4,2]

print(sorted(numbers))
```

