# match / case (Structural Pattern Matching)


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python 3.10+ introduced match/case statements for structural pattern matching, providing a more powerful alternative to if/elif chains. Match statements enable pattern-based dispatch and destructuring of complex data structures.

---

## Basic match/case Syntax

### Simple Value Matching

```python
def check_value(x):
    match x:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case _:
            return "other"

print(check_value(2))
print(check_value(5))
```

Output:
```
two
other
```

### Pattern with OR

```python
def classify_number(n):
    match n:
        case 0:
            return "zero"
        case 1 | 3 | 5 | 7 | 9:
            return "odd"
        case 2 | 4 | 6 | 8:
            return "even"
        case _:
            return "unknown"

print(classify_number(3))
print(classify_number(4))
```

Output:
```
odd
even
```

## Sequence Patterns

### List/Tuple Destructuring

```python
def process_sequence(seq):
    match seq:
        case []:
            return "empty"
        case [x]:
            return f"single: {x}"
        case [x, y]:
            return f"pair: {x}, {y}"
        case [x, *rest]:
            return f"first: {x}, rest: {rest}"

print(process_sequence([]))
print(process_sequence([1]))
print(process_sequence([1, 2, 3]))
```

Output:
```
empty
single: 1
first: 1, rest: [2, 3]
```

## Mapping Patterns

### Dictionary Matching

```python
def handle_command(command):
    match command:
        case {"action": "create", "name": name}:
            return f"Creating {name}"
        case {"action": "delete", "id": id}:
            return f"Deleting id {id}"
        case {"action": action}:
            return f"Unknown action: {action}"
        case _:
            return "Invalid command"

print(handle_command({"action": "create", "name": "file.txt"}))
print(handle_command({"action": "delete", "id": 42}))
```

Output:
```
Creating file.txt
Deleting id 42
```

## Guard Clauses

### Conditional Matching

```python
def analyze_number(n):
    match n:
        case int(x) if x < 0:
            return "negative"
        case int(x) if x > 0:
            return "positive"
        case _:
            return "zero"

print(analyze_number(-5))
print(analyze_number(10))
print(analyze_number(0))
```

Output:
```
negative
positive
zero
```
