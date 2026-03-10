# Python Comprehensions - Quick Reference


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Basic Syntax Comparison

| Type | Syntax | Returns | Memory |
|------|--------|---------|--------|
| **List** | `[expr for x in iter]` | List | Stores all |
| **Dict** | `{k: v for x in iter}` | Dictionary | Stores all |
| **Set** | `{expr for x in iter}` | Set | Stores unique |
| **Generator** | `(expr for x in iter)` | Generator | Lazy eval |

## List Comprehensions `[ ]`

### Basic
```python
[x for x in range(5)]                    # [0, 1, 2, 3, 4]
[x**2 for x in range(5)]                 # [0, 1, 4, 9, 16]
[x.upper() for x in ['a', 'b']]          # ['A', 'B']
```

### With Filter (if)
```python
[x for x in range(10) if x % 2 == 0]     # [0, 2, 4, 6, 8]
[x for x in range(10) if x > 5]          # [6, 7, 8, 9]
```

### With Transform (if-else)
```python
[x if x > 0 else 0 for x in [-1, 2, -3]] # [0, 2, 0]
['even' if x%2==0 else 'odd' for x in [1,2,3]]
```

### Multiple Conditions
```python
[x for x in range(20) if x % 2 == 0 if x % 3 == 0]  # AND
[x for x in range(20) if x % 2 == 0 or x % 3 == 0]  # OR
```

### Nested (Flatten)
```python
[num for row in matrix for num in row]   # Flatten 2D list
```

### With zip()
```python
[a+b for a, b in zip([1,2], [3,4])]      # [4, 6]
```

## Dictionary Comprehensions `{ : }`

### Basic
```python
{x: x**2 for x in range(5)}              # {0:0, 1:1, 2:4, 3:9, 4:16}
{word: len(word) for word in ['cat', 'dog']}
```

### From Two Lists
```python
dict(zip(keys, values))                   # Traditional
{k: v for k, v in zip(keys, values)}     # Comprehension
```

### Filter Dictionary
```python
{k: v for k, v in d.items() if v > 10}   # Filter by value
{k: v for k, v in d.items() if k.startswith('a')}  # By key
```

### Transform Values
```python
{k: v*2 for k, v in d.items()}           # Double all values
{k: v.upper() for k, v in d.items()}     # Uppercase strings
```

### Swap Keys/Values
```python
{v: k for k, v in d.items()}
```

### Conditional Values
```python
{k: 'high' if v>50 else 'low' for k,v in d.items()}
```

### Nested Dictionary
```python
{k1: {k2: 0 for k2 in list2} for k1 in list1}
```

## Set Comprehensions `{ }`

### Basic
```python
{x**2 for x in range(5)}                 # {0, 1, 4, 9, 16}
{len(word) for word in ['cat', 'dog']}   # {3}
```

### Remove Duplicates + Transform
```python
{x.lower() for x in ['A', 'B', 'a']}     # {'a', 'b'}
```

### With Filter
```python
{x for x in range(10) if x % 2 == 0}     # {0, 2, 4, 6, 8}
```

### From String
```python
{char for char in 'hello'}               # {'h', 'e', 'l', 'o'}
{char for char in text if char.isalpha()}
```

## Generator Expressions `( )`

### Basic
```python
(x**2 for x in range(5))                 # <generator object>
list((x**2 for x in range(5)))           # [0, 1, 4, 9, 16]
```

### With Functions
```python
sum(x**2 for x in range(100))            # Direct use
max(x for x in numbers if x > 0)
any(x < 0 for x in numbers)
all(x > 0 for x in numbers)
```

### Memory Efficient
```python
# Instead of
big_list = [x**2 for x in range(1000000)]
total = sum(big_list)

# Use
total = sum(x**2 for x in range(1000000))
```

### Chain Generators
```python
gen1 = (x for x in range(10))
gen2 = (x**2 for x in gen1)
```

## Common Patterns

### Filter & Transform
```python
[x.upper() for x in words if len(x) > 5]
```

### Multiple Iterables (Cartesian Product)
```python
[(x, y) for x in [1,2] for y in ['a','b']]
# [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
```

### Enumerate in Comprehension
```python
{i: val for i, val in enumerate(['a','b','c'])}
# {0: 'a', 1: 'b', 2: 'c'}
```

### Flatten Nested Lists
```python
[item for sublist in nested for item in sublist]
```

### Transpose Matrix
```python
[[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Or simpler with zip
[list(row) for row in zip(*matrix)]
```

### Count Occurrences
```python
{x: items.count(x) for x in set(items)}
```

### Group by Condition
```python
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
```

### Create Ranges
```python
[list(range(i)) for i in range(5)]
# [[], [0], [0,1], [0,1,2], [0,1,2,3]]
```

## Comparison: Loop vs Comprehension

### Traditional Loop
```python
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)
```

### List Comprehension
```python
result = [x**2 for x in range(10) if x % 2 == 0]
```

## When to Use What

### Use List Comprehension When:
- ✅ Creating a new list
- ✅ Need to iterate multiple times
- ✅ Need indexing/slicing
- ✅ Simple transformation/filtering

### Use Dictionary Comprehension When:
- ✅ Creating key-value mappings
- ✅ Transforming existing dictionary
- ✅ Filtering dictionary items

### Use Set Comprehension When:
- ✅ Need unique values
- ✅ Order doesn't matter
- ✅ Testing membership

### Use Generator Expression When:
- ✅ Large datasets
- ✅ Only iterating once
- ✅ Using with sum/max/min/any/all
- ✅ Memory is a concern

### Use Regular Loop When:
- ❌ Complex logic (multiple statements)
- ❌ Exception handling needed
- ❌ Side effects (printing, modifying external state)
- ❌ More than 2 nested levels

## Performance Tips

### Fast
```python
# Generator for single-use
sum(x**2 for x in range(1000000))

# Built-in functions
sum(numbers)
max(numbers)
```

### Slow
```python
# Creating then summing
squares = [x**2 for x in range(1000000)]
total = sum(squares)

# Using lambda in comprehension
[lambda x: x**2 for x in range(10)]  # Don't do this!
```

## Common Mistakes

### ❌ Wrong: Parentheses for Dictionary
```python
{(x, x**2) for x in range(5)}  # This is a SET of tuples!
```
### ✅ Correct:
```python
{x: x**2 for x in range(5)}    # Dictionary
```

### ❌ Wrong: Trying to Modify in Comprehension
```python
[items.remove(x) for x in items]  # Don't use for side effects!
```
### ✅ Correct:
```python
for x in items:
    items.remove(x)  # Use regular loop
```

### ❌ Wrong: Too Complex
```python
[do_something(x) if condition1(x) else do_other(x) if condition2(x) else default(x) for x in items if x > 0 if x < 100]
```
### ✅ Correct:
```python
result = []
for x in items:
    if 0 < x < 100:
        if condition1(x):
            result.append(do_something(x))
        elif condition2(x):
            result.append(do_other(x))
        else:
            result.append(default(x))
```

### ❌ Wrong: Reusing Exhausted Generator
```python
gen = (x**2 for x in range(5))
list1 = list(gen)  # [0, 1, 4, 9, 16]
list2 = list(gen)  # [] - Empty! Generator exhausted
```
### ✅ Correct:
```python
numbers = [x**2 for x in range(5)]  # Use list
list1 = numbers  # Can reuse
list2 = numbers
```

## Syntax Cheat Sheet

```python
# BASIC FORMS
[x for x in iterable]                    # List
{x for x in iterable}                    # Set
{k: v for k, v in iterable}              # Dict
(x for x in iterable)                    # Generator

# WITH CONDITION (filter)
[x for x in iterable if condition]

# WITH IF-ELSE (transform)
[x if condition else y for x in iterable]

# NESTED (two loops)
[x for sublist in lists for x in sublist]

# MULTIPLE CONDITIONS (both must be true)
[x for x in iterable if cond1 if cond2]
# Same as: if cond1 and cond2

# WITH ZIP
[f(a,b) for a,b in zip(list1, list2)]

# WITH ENUMERATE
{i: x for i, x in enumerate(list)}
```

## Real-World Examples

### Data Cleaning
```python
# Remove empty strings and lowercase
clean = [s.lower().strip() for s in data if s.strip()]
```

### CSV Processing
```python
# Parse CSV lines
rows = [line.split(',') for line in csv_data]
```

### URL Parameters
```python
# params = {'name': 'Alice', 'age': 25}
query = '&'.join(f"{k}={v}" for k, v in params.items())
# "name=Alice&age=25"
```

### File Filtering
```python
# Get .py files
py_files = [f for f in files if f.endswith('.py')]
```

### Grade Conversion
```python
# Numeric to letter
letters = ['A' if s>=90 else 'B' if s>=80 else 'C' for s in scores]
```

### Data Aggregation
```python
# Sum by category
totals = {cat: sum(v for k,v in data.items() if k==cat) 
          for cat in categories}
```

## Practice Exercises (One-Liners)

```python
# 1. Squares of evens from 1-10
[x**2 for x in range(1,11) if x%2==0]

# 2. Lengths of words
{word: len(word) for word in ['cat','dog','bird']}

# 3. Unique first letters
{word[0] for word in words}

# 4. Sum of squares
sum(x**2 for x in range(100))

# 5. Flatten and filter
[x for row in matrix for x in row if x > 0]

# 6. Invert dictionary
{v: k for k, v in original.items()}

# 7. Cartesian product
[(x,y) for x in range(3) for y in range(3)]

# 8. Filter dict by value
{k: v for k,v in d.items() if v > threshold}
```

Remember: **Readability counts!** Use comprehensions for simple cases, loops for complex logic.
