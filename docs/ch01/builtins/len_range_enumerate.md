

# len(), range(), and enumerate()

Python provides several built-in functions for working with sequences.

These utilities allow programs to measure, generate, and iterate through data efficiently.

```mermaid2
flowchart LR
    A[Sequence] --> B[len()]
    A --> C[range()]
    A --> D[enumerate()]
````

---

## len()

The `len()` function returns the number of elements in a container.

```python
numbers = [1,2,3,4]
print(len(numbers))
```

Output

```
4
```

Works with:

* lists
* tuples
* strings
* dictionaries
* sets

Example

```python
text = "Python"
print(len(text))
```

Output

```
6
```

---

## range()

`range()` generates sequences of integers.

Common uses include loop iteration.

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

Forms:

```
range(stop)
range(start, stop)
range(start, stop, step)
```

Example

```python
for i in range(2,10,2):
    print(i)
```

Output

```
2 4 6 8
```

---

## enumerate()

`enumerate()` returns both the index and value of elements during iteration.

```python
fruits = ["apple","banana","cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output

```
0 apple
1 banana
2 cherry
```

This is preferred over using `range(len(sequence))`.



