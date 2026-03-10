# break and continue


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The `break` and `continue` statements give you precise control over loop execution. They let you exit loops early or skip iterations based on conditions.

---

## break Statement

`break` **immediately exits** the innermost loop, skipping any remaining iterations.

### Basic Syntax

```python
for item in sequence:
    if condition:
        break  # Exit loop immediately
    # This code runs until break
# Code here runs after loop exits
```

### Example: Finding an Item

```python
numbers = [1, 5, 8, 3, 9, 2]

for num in numbers:
    print(f"Checking {num}")
    if num == 8:
        print("Found 8!")
        break

print("Search complete")
```

Output:
```
Checking 1
Checking 5
Checking 8
Found 8!
Search complete
```

### Example: User Input Validation

```python
while True:
    password = input("Enter password: ")
    if password == "secret123":
        print("Access granted!")
        break
    print("Wrong password, try again.")
```

### Example: Early Exit on Error

```python
files = ["data1.txt", "data2.txt", "missing.txt", "data3.txt"]

for filename in files:
    try:
        with open(filename) as f:
            process(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Stopping.")
        break
```

---

## continue Statement

`continue` **skips the rest of the current iteration** and moves to the next one.

### Basic Syntax

```python
for item in sequence:
    if condition:
        continue  # Skip to next iteration
    # This code only runs if continue wasn't triggered
```

### Example: Skip Certain Values

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print only odd numbers
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)
```

Output:
```
1
3
5
7
9
```

### Example: Skip Empty Strings

```python
names = ["Alice", "", "Bob", "", "", "Charlie"]

for name in names:
    if not name:  # Empty string is falsy
        continue
    print(f"Hello, {name}!")
```

Output:
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### Example: Skip Invalid Data

```python
data = ["10", "20", "invalid", "30", "error", "40"]

total = 0
for item in data:
    try:
        value = int(item)
    except ValueError:
        print(f"Skipping invalid: {item}")
        continue
    total += value

print(f"Total: {total}")  # 100
```

---

## break vs continue

| Statement | Effect | Loop Continues? |
|-----------|--------|-----------------|
| `break` | Exit loop entirely | No |
| `continue` | Skip current iteration | Yes, next iteration |

### Visual Comparison

```python
# break stops the loop
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2

# continue skips one iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4
```

---

## Nested Loops

`break` and `continue` only affect the **innermost loop**.

### break in Nested Loop

```python
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            break  # Only exits inner loop
        print(f"  Inner loop: {j}")
```

Output:
```
Outer loop: 0
  Inner loop: 0
Outer loop: 1
  Inner loop: 0
Outer loop: 2
  Inner loop: 0
```

### Breaking Out of Multiple Loops

Python doesn't have labeled breaks, but you can use these patterns:

**Pattern 1: Flag Variable**

```python
found = False
for i in range(10):
    for j in range(10):
        if matrix[i][j] == target:
            found = True
            break
    if found:
        break
```

**Pattern 2: Function with Return**

```python
def find_target(matrix, target):
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                return (i, j)
    return None

result = find_target(matrix, target)
```

**Pattern 3: Exception (for complex cases)**

```python
class FoundIt(Exception):
    pass

try:
    for i in range(10):
        for j in range(10):
            if condition:
                raise FoundIt()
except FoundIt:
    print(f"Found at {i}, {j}")
```

---

## while Loops with break and continue

### break with while

```python
count = 0
while True:  # Infinite loop
    count += 1
    print(count)
    if count >= 5:
        break  # Exit condition

# Output: 1, 2, 3, 4, 5
```

### continue with while

```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

# Output: 1, 3, 5, 7, 9
```

**Warning**: Be careful with `continue` in `while` loops—ensure the loop variable is updated before `continue`, or you may create an infinite loop:

```python
# INFINITE LOOP - DON'T DO THIS!
num = 0
while num < 10:
    if num == 5:
        continue  # num never increments past 5!
    print(num)
    num += 1

# CORRECT VERSION
num = 0
while num < 10:
    num += 1  # Increment BEFORE continue
    if num == 5:
        continue
    print(num)
```

---

## Loop else Clause

Python loops have an optional `else` clause that executes only if the loop completes **without hitting break**.

### for-else

```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num == 4:
        print("Found 4!")
        break
else:
    print("4 not found in list")

# Output: 4 not found in list
```

### while-else

```python
count = 0
while count < 5:
    if count == 10:  # Never true
        break
    count += 1
else:
    print("Loop completed normally")

# Output: Loop completed normally
```

### Practical Example: Search with Feedback

```python
def find_prime_factor(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"Found factor: {i}")
            break
    else:
        print(f"{n} is prime!")

find_prime_factor(17)  # 17 is prime!
find_prime_factor(18)  # Found factor: 2
```

---

## Common Patterns

### Pattern 1: Search and Exit

```python
def find_first_negative(numbers):
    for num in numbers:
        if num < 0:
            return num
    return None  # Not found
```

### Pattern 2: Process Until Condition

```python
# Read lines until empty line
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)
```

### Pattern 3: Skip Invalid, Process Valid

```python
for record in records:
    if not is_valid(record):
        continue
    process(record)
```

### Pattern 4: Retry with Limit

```python
max_retries = 3
for attempt in range(max_retries):
    try:
        result = risky_operation()
        break  # Success, exit loop
    except OperationError:
        print(f"Attempt {attempt + 1} failed")
else:
    print("All attempts failed")
    result = None
```

---

## Best Practices

### 1. Use break for Early Exit

```python
# Good: exit as soon as found
for item in large_list:
    if matches(item):
        result = item
        break
```

### 2. Use continue to Reduce Nesting

```python
# Without continue (deep nesting)
for item in items:
    if is_valid(item):
        if has_permission(item):
            if is_active(item):
                process(item)

# With continue (flat structure)
for item in items:
    if not is_valid(item):
        continue
    if not has_permission(item):
        continue
    if not is_active(item):
        continue
    process(item)
```

### 3. Avoid Overusing break/continue

```python
# Too many breaks make code hard to follow
for x in data:
    if cond1:
        break
    if cond2:
        continue
    if cond3:
        break
    # ... confusing!

# Better: extract to function with clear returns
def process_data(data):
    for x in data:
        if cond1:
            return result1
        if cond2:
            continue
        return process(x)
```

### 4. Document Complex Loop Logic

```python
for record in records:
    # Skip incomplete records
    if not record.is_complete():
        continue
    
    # Stop if we hit an error marker
    if record.is_error():
        break
    
    process(record)
```

---

## Summary

| Statement | Action | Use When |
|-----------|--------|----------|
| `break` | Exit loop immediately | Found what you need, error occurred |
| `continue` | Skip to next iteration | Current item invalid, skip processing |
| `else` (on loop) | Run if no `break` | Need to know if search failed |

**Key Points:**
- `break` exits the **innermost** loop only
- `continue` skips the **current iteration** only
- `else` on loops runs only if loop completes **without** `break`
- Use functions with `return` to break out of nested loops
- `continue` in `while` loops requires careful placement of increment
