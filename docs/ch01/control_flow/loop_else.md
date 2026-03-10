# for...else and while...else


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python's loop-else construct allows execution of a code block when a loop completes normally (without hitting a break statement). This unique feature is powerful for search patterns and validation logic.

---

## The for...else Pattern

The else block executes only if the loop completes without a break:

### Basic Example

```python
# Search for a number in a list
numbers = [1, 2, 3, 4, 5]
search_value = 6

for num in numbers:
    if num == search_value:
        print(f"Found {search_value}")
        break
else:
    print(f"{search_value} not found in list")
```

Output:
```
6 not found in list
```

### When Break Occurs

```python
numbers = [1, 2, 3, 4, 5]
search_value = 3

for num in numbers:
    if num == search_value:
        print(f"Found {search_value}")
        break
else:
    print(f"{search_value} not found in list")
```

Output:
```
Found 3
```

## The while...else Pattern

The while...else works identically to for...else:

### Validation with while...else

```python
# Validate user input simulation
user_attempts = [None, None, "password"]
attempt = 0

while attempt < len(user_attempts):
    if user_attempts[attempt] == "password":
        print("Access granted!")
        break
    attempt += 1
else:
    print("Access denied - no valid password provided")
```

Output:
```
Access granted!
```

## Practical Use Cases

### Checking for Primality

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

print(is_prime(17))
print(is_prime(18))
```

Output:
```
True
False
```

### Processing Lists

```python
# Find first matching item and process it
items = ['apple', 'banana', 'cherry']
target = 'date'

for item in items:
    if item == target:
        print(f"Processing {item}")
        break
else:
    print(f"{target} not found - creating new entry")
```

Output:
```
date not found - creating new entry
```
