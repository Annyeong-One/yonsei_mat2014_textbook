# min(), max(), sum()


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

These fundamental aggregate functions compute the minimum, maximum, and sum of iterables. They're essential for data analysis and provide convenient alternatives to loops or sorting.

---

## min() Function

### Basic Usage

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Minimum: {min(numbers)}")
```

Output:
```
Minimum: 1
```

### With Key Function

```python
words = ["apple", "pie", "a", "banana"]
shortest = min(words, key=len)
print(f"Shortest: {shortest}")
```

Output:
```
Shortest: a
```

## max() Function

### Finding Maximum

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Maximum: {max(numbers)}")
```

Output:
```
Maximum: 9
```

### Custom Comparison

```python
students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 87},
    {"name": "Charlie", "score": 92}
]

top_student = max(students, key=lambda s: s["score"])
print(f"Top: {top_student['name']} ({top_student['score']})")
```

Output:
```
Top: Alice (95)
```

## sum() Function

### Basic Summation

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum: {total}")
```

Output:
```
Sum: 15
```

### With Start Value

```python
numbers = [10, 20, 30]
total = sum(numbers, 100)  # Start from 100
print(f"Total: {total}")
```

Output:
```
Total: 160
```

## Combined Examples

### Statistics Computation

```python
scores = [92, 87, 95, 88, 91, 89]

print(f"Min: {min(scores)}")
print(f"Max: {max(scores)}")
print(f"Sum: {sum(scores)}")
print(f"Average: {sum(scores) / len(scores):.1f}")
```

Output:
```
Min: 87
Max: 95
Sum: 542
Average: 90.3
```

### Finding Extreme Values

```python
temperatures = [72, 68, 75, 70, 73, 69, 76]

coldest = min(temperatures)
hottest = max(temperatures)
average = sum(temperatures) / len(temperatures)

print(f"Coldest: {coldest}°F")
print(f"Hottest: {hottest}°F")
print(f"Average: {average:.1f}°F")
```

Output:
```
Coldest: 68°F
Hottest: 76°F
Average: 71.6°F
```
