# map() and filter()

`map()` applies a function to every element of an iterable. `filter()` keeps only the elements for which a function returns `True`. Both return lazy iterators — wrap with `list()` to materialise the result.

## map()

```python
def square(x: int) -> int:
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

With a lambda instead of a named function:

```python
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

`map()` can take multiple iterables — the function receives one element from each:

```python
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)   # [11, 22, 33]
```

Passing a named method works too:

```python
words = ["hello", "world", "python"]
upper = list(map(str.upper, words))
print(upper)   # ['HELLO', 'WORLD', 'PYTHON']
```

## filter()

```python
def is_even(x: int) -> bool:
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(is_even, numbers))
print(evens)   # [2, 4, 6, 8, 10]
```

With a lambda:

```python
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

Filtering strings:

```python
words = ["apple", "banana", "apricot", "cherry", "avocado"]
a_words = list(filter(lambda w: w.startswith("a"), words))
print(a_words)   # ['apple', 'apricot', 'avocado']
```

Passing `None` as the function keeps all truthy values:

```python
values = [0, 1, False, True, "", "hello", None, [], [1, 2]]
truthy = list(filter(None, values))
print(truthy)   # [1, True, 'hello', [1, 2]]
```

## Combining map() and filter()

Chain them by passing one as the input to the other:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of even numbers only
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)   # [4, 16, 36, 64, 100]
```

## map() and filter() vs List Comprehensions

Both approaches produce identical results. Choose based on readability:

```python
numbers = [1, 2, 3, 4, 5]

# Transform
list(map(lambda x: x ** 2, numbers))   # map
[x ** 2 for x in numbers]              # comprehension

# Filter
list(filter(lambda x: x % 2 == 0, numbers))   # filter
[x for x in numbers if x % 2 == 0]            # comprehension

# Combined
list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))  # map + filter
[x**2 for x in numbers if x % 2 == 0]                              # comprehension
```

List comprehensions are generally preferred in modern Python — they read left to right and require no lambda. Reach for `map()` or `filter()` when you already have a named function to pass:

```python
words = ["  alice  ", "BOB", "  Charlie"]
cleaned = list(map(str.strip, words))   # cleaner than a lambda here
```

## Practical Examples

**Clean and format names:**

```python
names = ["  alice  ", "BOB", "  Charlie"]
cleaned = list(map(lambda s: s.strip().title(), names))
print(cleaned)   # ['Alice', 'Bob', 'Charlie']
```

**Temperature conversion:**

```python
celsius = [0, 10, 20, 30, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
print(fahrenheit)   # [32.0, 50.0, 68.0, 86.0, 212.0]
```

**Filter passing grades:**

```python
grades = [45, 78, 92, 55, 67, 88, 34, 91]
passing = list(filter(lambda g: g >= 60, grades))
print(passing)                                      # [78, 92, 67, 88, 91]
print(f"Pass rate: {len(passing)/len(grades)*100:.1f}%")   # 62.5%
```

**Validate email addresses:**

```python
emails = ["user@example.com", "invalid", "test@test.org", "no-at-sign"]
valid = list(filter(lambda e: "@" in e and "." in e, emails))
print(valid)   # ['user@example.com', 'test@test.org']
```

## Key Ideas

`map()` transforms every element; `filter()` selects elements. Both are lazy — they produce one result at a time without building the full list in memory. List comprehensions are usually clearer for simple cases; `map()` and `filter()` shine when a named function is already available to pass directly.

We return to `map()` and `filter()` as functional programming tools — alongside `reduce()` and function composition — in [map(), filter(), reduce()](../../ch05/functional/map_filter_reduce.md).
