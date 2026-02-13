# Ternary Expressions

Ternary expressions (conditional expressions) provide a concise way to assign one of two values based on a condition. The syntax is `value_if_true if condition else value_if_false`, making code more readable than nested if/else statements.

---

## Basic Ternary Syntax

### Simple Value Selection

```python
age = 25
status = "adult" if age >= 18 else "minor"
print(status)
```

Output:
```
adult
```

### Numeric Calculation

```python
x = 10
y = 20
max_value = x if x > y else y
print(f"Maximum: {max_value}")
```

Output:
```
Maximum: 20
```

## Nested Ternary Expressions

### Multiple Conditions

```python
score = 85

grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")
```

Output:
```
Grade: B
```

### Function Return Values

```python
def classify_number(n):
    return "positive" if n > 0 else "negative" if n < 0 else "zero"

print(classify_number(5))
print(classify_number(-3))
print(classify_number(0))
```

Output:
```
positive
negative
zero
```

## Advanced Patterns

### With Function Calls

```python
def get_value():
    return 42

def get_default():
    return 0

result = get_value() if True else get_default()
print(result)
```

Output:
```
42
```

### List Comprehension Integration

```python
numbers = [1, 2, 3, 4, 5, 6]
even_odd = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(even_odd)
```

Output:
```
['odd', 'even', 'odd', 'even', 'odd', 'even']
```

### Practical Example

```python
user_input = ""
username = user_input if user_input.strip() else "guest"
print(f"Username: {username}")
```

Output:
```
Username: guest
```
