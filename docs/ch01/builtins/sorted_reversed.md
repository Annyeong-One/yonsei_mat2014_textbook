# sorted() and reversed()


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The sorted() function returns a new sorted list from any iterable, while reversed() returns an iterator over elements in reverse order. Both are essential for data organization and iteration.

---

## sorted() Function

### Basic Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(numbers)
print(sorted_nums)
```

Output:
```
[1, 1, 2, 3, 4, 5, 6, 9]
```

### Reverse Sorting

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
descending = sorted(numbers, reverse=True)
print(descending)
```

Output:
```
[9, 6, 5, 4, 3, 2, 1, 1]
```

### Sorting with Key

```python
words = ["python", "go", "rust", "c"]
by_length = sorted(words, key=len)
print(by_length)
```

Output:
```
['go', 'c', 'rust', 'python']
```

### Sorting Complex Objects

```python
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
for s in by_grade:
    print(f"{s['name']}: {s['grade']}")
```

Output:
```
Bob: 92
Alice: 85
Charlie: 78
```

## reversed() Function

### Basic Reversal

```python
numbers = [1, 2, 3, 4, 5]
rev = list(reversed(numbers))
print(rev)
```

Output:
```
[5, 4, 3, 2, 1]
```

### Iterating in Reverse

```python
items = ["apple", "banana", "cherry"]
for item in reversed(items):
    print(item)
```

Output:
```
cherry
banana
apple
```

### Reversing Strings

```python
text = "hello"
backwards = ''.join(reversed(text))
print(backwards)
```

Output:
```
olleh
```

## Comparison and Patterns

### sorted() vs reverse()

```python
original = [3, 1, 4, 1, 5]
print(f"Original: {original}")
print(f"sorted(): {sorted(original)}")
print(f"reversed(): {list(reversed(original))}")
```

Output:
```
Original: [3, 1, 4, 1, 5]
sorted(): [1, 1, 3, 4, 5]
reversed(): [5, 1, 4, 1, 3]
```

### Multi-Key Sorting

```python
data = [
    ("Alice", 25),
    ("Bob", 23),
    ("Charlie", 25)
]

sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
for name, age in sorted_data:
    print(f"{name}: {age}")
```

Output:
```
Bob: 23
Alice: 25
Charlie: 25
```
