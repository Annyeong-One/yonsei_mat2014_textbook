# Control Flow: if, for, while

## Introduction

Control flow statements determine the order in which your program executes code. Instead of running line by line from top to bottom, control flow lets you:
- Make decisions (`if` statements)
- Repeat actions (`for` and `while` loops)
- Skip or exit code blocks (`break`, `continue`, `pass`)

This chapter covers Python's core control flow constructs with comprehensive examples and best practices.

## Conditional Statements: if, elif, else

### Basic if Statement

Execute code only when a condition is true:

```python
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

# Output: You are an adult
#         You can vote
```

**Syntax**:
```python
if condition:
    # code block executed if condition is True
    statement1
    statement2
```

### if-else Statement

Execute one block if condition is true, another if false:

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Output: You are a minor
```

### if-elif-else Statement

Handle multiple conditions:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
# Output: Your grade is: B
```

**Important**: 
- Python checks conditions in order from top to bottom
- Only the first matching condition's block executes
- `else` is optional and executes if no condition matches

### Nested if Statements

Put if statements inside other if statements:

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")

# Output: You can drive
```

### One-Line if Statements

For simple cases, put everything on one line:

```python
age = 20
if age >= 18: print("Adult")

# Or use ternary operator (conditional expression)
status = "Adult" if age >= 18 else "Minor"
```

### Conditions and Truth Values

Python treats many values as True or False:

```python
# Falsy values (evaluate to False)
if 0:              # False - zero
    pass
if "":             # False - empty string
    pass
if []:             # False - empty list
    pass
if {}:             # False - empty dict
    pass
if None:           # False - None
    pass
if False:          # False - boolean False
    pass

# Truthy values (evaluate to True)
if 42:             # True - non-zero number
    print("Number is truthy")
if "hello":        # True - non-empty string
    print("String is truthy")
if [1, 2]:         # True - non-empty list
    print("List is truthy")
```

### Comparison Operators in Conditions

```python
x = 10

# Equality
if x == 10:         # Equal to
    pass
if x != 5:          # Not equal to
    pass

# Relational
if x > 5:           # Greater than
    pass
if x < 20:          # Less than
    pass
if x >= 10:         # Greater than or equal
    pass
if x <= 15:         # Less than or equal
    pass

# Chained comparisons (very Pythonic!)
if 0 < x < 20:      # x is between 0 and 20
    pass
if 0 <= x <= 100:   # x is between 0 and 100 inclusive
    pass

# Identity
if x is None:       # Check if x is None
    pass
if x is not None:   # Check if x is not None
    pass

# Membership
if x in [10, 20, 30]:  # Check if x is in list
    pass
if 'a' in 'abc':       # Check if character in string
    pass
```

### Logical Operators

Combine multiple conditions:

```python
age = 25
has_license = True
has_car = False

# AND - all conditions must be True
if age >= 18 and has_license:
    print("Can drive legally")

# OR - at least one condition must be True
if has_license or has_car:
    print("Has some transportation option")

# NOT - inverts the condition
if not has_car:
    print("Needs to buy a car")

# Complex combinations
if (age >= 18 and has_license) or has_car:
    print("Can drive somehow")
```

### Short-Circuit Evaluation

Logical operators stop evaluating as soon as the result is determined:

```python
# AND stops at first False
False and expensive_function()  # expensive_function() is NOT called

# OR stops at first True
True or expensive_function()    # expensive_function() is NOT called

# Practical example
x = None
if x and x.some_method():  # Won't call some_method() if x is None
    pass

# Another practical use
name = input_name or "Guest"  # Use "Guest" if input_name is empty
```

## For Loops

### Basic for Loop

Iterate over sequences (lists, strings, ranges, etc.):

```python
# Iterate over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

**Syntax**:
```python
for variable in sequence:
    # code block
    statement1
    statement2
```

### Iterating Over Different Types

```python
# String
for char in "Python":
    print(char)  # P, y, t, h, o, n

# List
for number in [1, 2, 3, 4, 5]:
    print(number)

# Tuple
for item in (1, 2, 3):
    print(item)

# Dictionary (iterates over keys by default)
person = {"name": "Alice", "age": 25}
for key in person:
    print(f"{key}: {person[key]}")

# Dictionary items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")

# Set
for item in {1, 2, 3}:
    print(item)
```

### The range() Function

Generate sequences of numbers:

```python
# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - from start to stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Negative step (counting down)
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1

# Even numbers
for i in range(0, 20, 2):
    print(i)
```

### Nested Loops

Loops inside loops:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line after each row

# Matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
```

### enumerate() Function

Get both index and value:

```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (better!)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start indexing from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry
```

### zip() Function

Iterate over multiple sequences simultaneously:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old

# Multiple sequences
scores = [85, 90, 78]
for name, age, score in zip(names, ages, scores):
    print(f"{name} ({age}) scored {score}")
```

### reversed() Function

Iterate in reverse:

```python
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)  # 5, 4, 3, 2, 1

# Also works with strings
for char in reversed("Python"):
    print(char)  # n, o, h, t, y, P
```

### sorted() Function

Iterate in sorted order:

```python
numbers = [3, 1, 4, 1, 5, 9]

for num in sorted(numbers):
    print(num)  # 1, 1, 3, 4, 5, 9

# Reverse sort
for num in sorted(numbers, reverse=True):
    print(num)  # 9, 5, 4, 3, 1, 1

# Sort strings
names = ["Charlie", "Alice", "Bob"]
for name in sorted(names):
    print(name)  # Alice, Bob, Charlie
```

## While Loops

### Basic while Loop

Repeat while a condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Output: 0, 1, 2, 3, 4
```

**Syntax**:
```python
while condition:
    # code block
    statement1
    statement2
```

**Warning**: Make sure the condition eventually becomes False, or you'll have an infinite loop!

### While Loop Examples

```python
# Countdown
n = 10
while n > 0:
    print(n)
    n -= 1
print("Blast off!")

# User input validation
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    print("Invalid input. Please enter a positive number.")

# Sum until negative
total = 0
num = int(input("Enter a number (negative to stop): "))
while num >= 0:
    total += num
    num = int(input("Enter a number (negative to stop): "))
print(f"Total: {total}")
```

### While vs For

```python
# Same result, different approaches

# For loop (when you know the count)
for i in range(5):
    print(i)

# While loop (when you check a condition)
i = 0
while i < 5:
    print(i)
    i += 1
```

**Use `for`** when:
- Iterating over a sequence
- You know the number of iterations

**Use `while`** when:
- You don't know how many iterations needed
- Waiting for a condition to change
- Processing user input until they quit

## Loop Control Statements

### break Statement

Exit the loop immediately:

```python
# Stop when found
numbers = [1, 3, 5, 7, 9, 2, 4]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
    print(num)

# Output: 1, 3, 5, 7, 9, Found even number: 2

# Infinite loop with break
while True:
    response = input("Continue? (y/n): ")
    if response.lower() == 'n':
        break
    print("Continuing...")
```

### continue Statement

Skip the rest of the current iteration:

```python
# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output: 1, 3, 5, 7, 9

# Skip empty strings
names = ["Alice", "", "Bob", "", "Charlie"]
for name in names:
    if not name:
        continue
    print(f"Hello, {name}")
```

### pass Statement

Do nothing (placeholder):

```python
# Placeholder for future code
for i in range(10):
    if i == 5:
        pass  # TODO: implement special handling
    print(i)

# Empty loop (useful during development)
while condition:
    pass  # Will implement later

# Minimal class definition
class MyClass:
    pass  # Will add methods later
```

### else Clause with Loops

Execute code when loop completes normally (not via `break`):

```python
# With for loop
for num in [1, 3, 5, 7]:
    if num == 10:
        print("Found 10!")
        break
else:
    print("10 not found in list")
# Output: 10 not found in list

# With while loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed normally")
# Output: 0, 1, 2, 3, 4, Loop completed normally

# Practical example: search
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")

find_item([1, 2, 3, 4], 3)  # Found 3
find_item([1, 2, 3, 4], 5)  # 5 not found
```

## Common Patterns and Idioms

### Counting Pattern

```python
# Count occurrences
numbers = [1, 2, 3, 2, 1, 2, 4]
count = 0
for num in numbers:
    if num == 2:
        count += 1
print(f"2 appears {count} times")

# Or use count() method
count = numbers.count(2)
```

### Accumulation Pattern

```python
# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# Or use sum()
total = sum(numbers)
```

### Finding Maximum/Minimum

```python
# Find maximum
numbers = [3, 7, 2, 9, 1]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)  # 9

# Or use max()
maximum = max(numbers)
```

### Filtering Pattern

```python
# Collect even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)  # [2, 4, 6]

# Or use list comprehension
evens = [num for num in numbers if num % 2 == 0]
```

### Transformation Pattern

```python
# Square all numbers
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Or use list comprehension
squares = [num ** 2 for num in numbers]

# Or use map()
squares = list(map(lambda x: x ** 2, numbers))
```

### Early Exit Pattern

```python
# Find first match and exit
def find_user(users, user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None  # Not found
```

### Flag Pattern

```python
# Set flag when condition is met
found = False
for item in collection:
    if item == target:
        found = True
        break

if found:
    print("Target found")
else:
    print("Target not found")
```

## Best Practices

### 1. Use for Loops for Sequences

```python
# Poor (C-style iteration)
i = 0
while i < len(items):
    print(items[i])
    i += 1

# Good (Pythonic iteration)
for item in items:
    print(item)
```

### 2. Use enumerate() for Index and Value

```python
# Poor
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# Good
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

### 3. Avoid Modifying List While Iterating

```python
# Dangerous!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can skip elements or raise errors

# Safe - iterate over a copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # [:] creates a copy
    if num % 2 == 0:
        numbers.remove(num)

# Better - use list comprehension
numbers = [num for num in numbers if num % 2 != 0]
```

### 4. Use List Comprehensions When Appropriate

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (more concise)
squares = [x ** 2 for x in range(10)]

# But don't overuse - readability matters
# Too complex
result = [x**2 for x in range(100) if x%2==0 and x>10 and x<90]

# Better - break it down
evens = [x for x in range(100) if x % 2 == 0]
in_range = [x for x in evens if 10 < x < 90]
result = [x ** 2 for x in in_range]
```

### 5. Avoid Infinite Loops

```python
# Dangerous - no way to exit
while True:
    print("This will run forever!")

# Better - have an exit condition
count = 0
while count < 10:
    print(count)
    count += 1

# Or use break
while True:
    response = input("Continue? (y/n): ")
    if response.lower() == 'n':
        break
```

### 6. Keep Loop Bodies Simple

```python
# Poor - complex loop body
for item in items:
    if condition1:
        if condition2:
            if condition3:
                # deeply nested code
                pass

# Better - extract to function
def process_item(item):
    if not condition1:
        return
    if not condition2:
        return
    if not condition3:
        return
    # flat code
    pass

for item in items:
    process_item(item)
```

## Common Pitfalls

### 1. Off-by-One Errors

```python
# Common mistake
for i in range(1, 10):  # Goes from 1 to 9, not 10
    print(i)

# Remember: range(start, stop) excludes stop
# To include 10:
for i in range(1, 11):
    print(i)
```

### 2. Modifying Dictionary While Iterating

```python
# Dangerous!
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    if d[key] == 2:
        del d[key]  # RuntimeError!

# Safe - iterate over a copy of keys
for key in list(d.keys()):
    if d[key] == 2:
        del d[key]
```

### 3. Forgetting to Update Loop Variable

```python
# Infinite loop!
i = 0
while i < 10:
    print(i)
    # Forgot: i += 1
```

### 4. Using Wrong Comparison Operator

```python
# Wrong - always True (single =)
if x = 10:  # SyntaxError in Python
    pass

# Correct
if x == 10:
    pass
```

## Quick Reference

### if Statement
```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

### for Loop
```python
for item in sequence:
    # code

for i in range(start, stop, step):
    # code

for i, item in enumerate(sequence):
    # code

for key, value in dictionary.items():
    # code
```

### while Loop
```python
while condition:
    # code

while True:
    # code
    if exit_condition:
        break
```

### Loop Control
```python
break      # Exit loop immediately
continue   # Skip to next iteration
pass       # Do nothing (placeholder)
```

### Loop with else
```python
for item in sequence:
    if found:
        break
else:
    # Executed if loop completed without break
    pass
```

## Summary

- **if statements** let you make decisions and execute code conditionally
- **elif** and **else** handle multiple conditions and alternatives
- **for loops** iterate over sequences (lists, strings, ranges, etc.)
- **while loops** repeat while a condition is true
- **break** exits a loop early
- **continue** skips to the next iteration
- **pass** is a placeholder that does nothing
- **else** clause on loops executes if loop completes normally (no break)
- Use **enumerate()** for index and value
- Use **zip()** to iterate multiple sequences together
- Choose **for** when iterating sequences, **while** when checking conditions
- Keep loop bodies simple and readable
- Avoid modifying collections while iterating over them

Mastering control flow is essential for writing effective Python programs. Practice these patterns and you'll develop an intuition for when to use each construct.
