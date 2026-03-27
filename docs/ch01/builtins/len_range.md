# len() and range()

## len()

`len()` returns the number of elements in a container.

```python
numbers = [1, 2, 3, 4]
print(len(numbers))   # 4

text = "Python"
print(len(text))      # 6
```

Works with any sized container: lists, tuples, strings, dictionaries, and sets.

## range()

`range()` generates a sequence of integers. It is lazy — the numbers are produced on demand rather than stored all at once.

Three forms:

```python
range(stop)             # 0 up to (not including) stop
range(start, stop)      # start up to (not including) stop
range(start, stop, step)# start up to stop, stepping by step
```

```python
for i in range(5):
    print(i)   # 0 1 2 3 4
```

```python
for i in range(2, 10, 2):
    print(i)   # 2 4 6 8
```

`range()` produces integers only. To iterate over a list by index, combine it with `len()`:

```python
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])
```

Output:

```text
0 apple
1 banana
2 cherry
```

In practice this pattern is rare — `enumerate()` is almost always clearer. See [enumerate() and zip()](enumerate_zip.md).

## Key Ideas

`len()` measures a container; `range()` generates integers for iteration.
`range()` is lazy and memory-efficient — `range(1_000_000)` uses no more memory than `range(5)`.
Avoid `range(len(seq))` when you need both index and value — use `enumerate()` instead.
