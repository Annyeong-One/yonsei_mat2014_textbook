# Comprehensions

Comprehensions provide concise syntax for creating lists, dictionaries, and sets from iterables. They combine iteration and optional filtering into a single expression.

## List Comprehensions

List comprehensions create new lists by applying an expression to each item in an iterable.

### 1. Basic Syntax

The syntax is `[expression for item in iterable]`.

```python
# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

### 2. With Filtering

Add `if` clause to filter items: `[expr for item in iterable if condition]`.

```python
# Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Filter and transform
words = ["hello", "WORLD", "Python"]
lower_long = [w.lower() for w in words if len(w) > 5]
print(lower_long)  # ['python']
```

### 3. Conditional Expression

Use ternary operator for if-else in the expression part.

```python
# Classify numbers
nums = [1, -2, 3, -4, 5]
signs = ["pos" if n > 0 else "neg" for n in nums]
print(signs)  # ['pos', 'neg', 'pos', 'neg', 'pos']

# Transform based on condition
abs_vals = [n if n >= 0 else -n for n in nums]
print(abs_vals)  # [1, 2, 3, 4, 5]
```

### 4. Performance

List comprehensions are faster than equivalent for loops due to internal optimizations:

```python
# For loop (slower)
squares = []
for x in range(1000):
    squares.append(x ** 2)

# List comprehension (faster)
squares = [x ** 2 for x in range(1000)]
```

The comprehension avoids method lookup overhead (`append`) and uses optimized bytecode.

## Dict Comprehensions

Dictionary comprehensions create dictionaries using `{key: value for item in iterable}`.

### 1. Basic Syntax

Create key-value pairs from an iterable.

```python
# Square mapping
squares = {x: x ** 2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = {k: v for k, v in zip(keys, vals)}
print(d)  # {'a': 1, 'b': 2, 'c': 3}
```

### 2. Transforming Dicts

Transform existing dictionaries.

```python
prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}

# Apply discount
sale = {k: v * 0.9 for k, v in prices.items()}
print(sale)  # {'apple': 1.35, 'banana': 0.675, 'orange': 1.8}

# Swap keys and values
flipped = {v: k for k, v in prices.items()}
print(flipped)  # {1.5: 'apple', 0.75: 'banana', 2.0: 'orange'}
```

### 3. Filtering Entries

Filter dictionary entries with conditions.

```python
scores = {"Alice": 85, "Bob": 92, "Carol": 78, "Dave": 95}

# High scores only
high = {k: v for k, v in scores.items() if v >= 90}
print(high)  # {'Bob': 92, 'Dave': 95}

# Filter by key
selected = {k: v for k, v in scores.items() if k.startswith("C")}
print(selected)  # {'Carol': 78}
```

## Set Comprehensions

Set comprehensions create sets using `{expression for item in iterable}`.

### 1. Basic Syntax

Create sets with automatic deduplication.

```python
# Unique squares
squares = {x ** 2 for x in range(-3, 4)}
print(squares)  # {0, 1, 4, 9}

# Unique first letters
words = ["apple", "banana", "apricot", "cherry"]
initials = {w[0] for w in words}
print(initials)  # {'a', 'b', 'c'}
```

### 2. With Filtering

Filter elements during set creation.

```python
# Unique even squares
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
even_unique = {n for n in nums if n % 2 == 0}
print(even_unique)  # {2, 4}

# Vowels in text
text = "Hello World"
vowels = {c.lower() for c in text if c.lower() in "aeiou"}
print(vowels)  # {'e', 'o'}
```

### 3. Set Operations

Combine comprehensions with set operations.

```python
a = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
b = {x for x in range(10) if x % 3 == 0}  # {0, 3, 6, 9}

print(a & b)  # {0, 6} - intersection
print(a | b)  # {0, 2, 3, 4, 6, 8, 9} - union
print(a - b)  # {8, 2, 4} - difference
```

## Nested Loops

Comprehensions can contain multiple `for` clauses for nested iteration.

### 1. Cartesian Product

Generate all combinations of items.

```python
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

# All combinations
combos = [(c, s) for c in colors for s in sizes]
print(combos)
# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

### 2. Flattening Lists

Convert nested lists to flat lists.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# With condition
evens = [x for row in matrix for x in row if x % 2 == 0]
print(evens)  # [2, 4, 6, 8]
```

### 3. Nested Structure

Create nested structures with nested comprehensions.

```python
# Multiplication table
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)
# [[1, 4], [2, 5], [3, 6]]
```

## Generator Expressions

Generator expressions use parentheses and produce items lazily.

### 1. Basic Syntax

Replace brackets with parentheses for memory efficiency.

```python
# List comprehension (eager, stores all)
squares_list = [x ** 2 for x in range(1000000)]

# Generator expression (lazy, computes on demand)
squares_gen = (x ** 2 for x in range(1000000))

print(type(squares_gen))  # <class 'generator'>
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
```

### 2. With Functions

Pass directly to functions that accept iterables.

```python
# Sum without intermediate list
total = sum(x ** 2 for x in range(100))
print(total)  # 328350

# Any/all with generators
nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))  # True
print(any(n > 9 for n in nums))       # True
```

### 3. Memory Efficiency

Generators avoid storing large intermediate results.

```python
import sys

# List: stores all items
list_comp = [x for x in range(10000)]
print(sys.getsizeof(list_comp))  # ~87624 bytes

# Generator: stores only state
gen_exp = (x for x in range(10000))
print(sys.getsizeof(gen_exp))    # ~200 bytes
```

## Tuple from Comprehension

Python has no native tuple comprehension. Use `tuple()` with a generator:

```python
# This is a generator, not a tuple
gen = (x ** 2 for x in range(5))

# Wrap in tuple() to create tuple
t = tuple(x ** 2 for x in range(5))
print(t)  # (0, 1, 4, 9, 16)
```


## Performance Summary

| Type | Syntax | Lazy | Memory |
|------|--------|------|--------|
| List | `[x for x in iter]` | No | O(n) |
| Set | `{x for x in iter}` | No | O(n) |
| Dict | `{k: v for ...}` | No | O(n) |
| Generator | `(x for x in iter)` | Yes | O(1) |
| Tuple | `tuple(x for ...)` | No | O(n) |


## Best Practices

Guidelines for readable and efficient comprehensions.

### 1. Readability First

Keep comprehensions simple; use loops for complex logic.

```python
# Good: simple and clear
squares = [x ** 2 for x in range(10)]

# Bad: too complex, hard to read
# result = [x if x > 0 else -x for x in [y ** 2 - z for y, z in pairs] if x != 0]

# Better: break into steps
intermediate = [y ** 2 - z for y, z in pairs]
result = [x if x > 0 else -x for x in intermediate if x != 0]
```

### 2. Avoid Side Effects

Comprehensions should create data, not perform actions.

```python
# Bad: side effect in comprehension
results = []
[results.append(x ** 2) for x in range(5)]  # Don't do this

# Good: direct assignment
results = [x ** 2 for x in range(5)]
```

### 3. Choose Right Type

Select comprehension type based on need.

```python
data = [1, 2, 2, 3, 3, 3]

# Need ordered sequence? List
ordered = [x ** 2 for x in data]

# Need unique values? Set
unique = {x ** 2 for x in data}

# Need key-value mapping? Dict
counted = {x: data.count(x) for x in set(data)}

# Need lazy evaluation? Generator
lazy = (x ** 2 for x in data)
```
