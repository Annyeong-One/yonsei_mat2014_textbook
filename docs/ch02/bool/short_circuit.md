# Short-Circuit Evaluation


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python's and and or operators use short-circuit evaluation, stopping evaluation as soon as the result is determined. This behavior is crucial for writing efficient code and preventing errors from evaluating unnecessary expressions.

---

## and Short-Circuiting

### Early Termination with and

```python
def test_value(x):
    print(f"Testing {x}")
    return x > 5

result = False and test_value(10)
print(f"Result: {result}")
```

Output:
```
Result: False
```

Notice that test_value was never called because the first operand is False.

### Practical Usage

```python
user = {"name": "Alice", "age": 30}

if user and user.get("name") and len(user.get("name")) > 0:
    print(f"Valid user: {user['name']}")
```

Output:
```
Valid user: Alice
```

## or Short-Circuiting

### Early Termination with or

```python
def get_default():
    print("Getting default")
    return "default"

result = "custom" or get_default()
print(f"Result: {result}")
```

Output:
```
custom
```

The get_default function is never called because "custom" is truthy.

### Default Value Pattern

```python
username = None
fallback = "guest"

displayed_name = username or fallback
print(f"Username: {displayed_name}")
```

Output:
```
Username: guest
```

## Efficiency Implications

### Avoiding Expensive Operations

```python
import time

def expensive_check():
    time.sleep(0.1)
    return True

# Short-circuits immediately
result = False and expensive_check()
print(f"Instant result: {result}")

# This would wait for expensive_check
result2 = True and expensive_check()
print(f"Takes time: {result2}")
```

Output:
```
Instant result: False
Takes time: True
```

## Complex Expressions

### Order Matters

```python
def check_condition(n, label):
    print(f"Checking {label}")
    return n > 5

# Only first is checked
result = check_condition(3, "A") and check_condition(10, "B")
print(f"Result: {result}\n")

# Both are checked
result = check_condition(10, "A") and check_condition(3, "B")
print(f"Result: {result}")
```

Output:
```
Checking A
Result: False

Checking A
Checking B
Result: False
```
