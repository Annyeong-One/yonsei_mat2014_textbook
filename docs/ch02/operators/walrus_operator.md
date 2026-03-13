# Walrus Operator (:=)

The walrus operator (assignment expression) assigns a value and returns it in a single expression. Introduced in Python 3.8 (PEP 572), it enables more concise code in loops, conditions, and comprehensions.

---

## Basic Usage

### Assignment in Condition

```python
if (n := len("hello")) > 3:
    print(f"String length {n} is greater than 3")
```

Output:
```
String length 5 is greater than 3
```

### Assignment in while Loop

```python
data = iter([1, 2, 3, None, 4])

while (value := next(data, None)) is not None:
    print(f"Value: {value}")
```

Output:
```
Value: 1
Value: 2
Value: 3
```

## List Comprehension Usage

### Filtering with Walrus

```python
numbers = range(10)
squared = [y for x in numbers if (y := x**2) > 20]
print(squared)
```

Output:
```
[25, 36, 49, 64, 81]
```

### Reusing Computation

```python
import re

text = "Hello123World"
pattern = re.compile(r'\d+')

if (match := pattern.search(text)):
    print(f"Found: {match.group()}")
```

Output:
```
Found: 123
```

## Practical Examples

### While Loop with Input

```python
import io

user_input = iter(["valid", "another", "quit"])

while (command := next(user_input)) != "quit":
    print(f"Processing: {command}")
```

Output:
```
Processing: valid
Processing: another
```

### Dictionary Comprehension

```python
data = ["apple", "pie", "a", "banana"]
lengths = {word: length for word in data if (length := len(word)) > 2}
print(lengths)
```

Output:
```
{'apple': 5, 'banana': 6}
```

## Advantages

### Cleaner Code

```python
def some_expensive_computation():
    return [1, 2, 3]

def process(x):
    pass

if (data := some_expensive_computation()):
    process(data)
```

Output:
```
```
