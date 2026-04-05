# Generator Expressions

## Syntax

### 1. Like Comprehension

```python
# List comprehension
squares_list = [x**2 for x in range(1000)]

# Generator expression
squares_gen = (x**2 for x in range(1000))
```

## Lazy Evaluation

### 1. Memory Efficient

```python
# Consumes memory
large_list = [x**2 for x in range(1000000)]

# Memory efficient
large_gen = (x**2 for x in range(1000000))

# Use one at a time
for value in large_gen:
    process(value)
```

## Use Cases

### 1. Pipeline

```python
# Chained generators
numbers = range(1000)
squares = (x**2 for x in numbers)
evens = (x for x in squares if x % 2 == 0)
result = sum(evens)
```

## Reimplementing map and filter

Generators can recreate the behavior of `map()` and `filter()`.

### 1. Custom map

```python
def my_map(func, iterable):
    for item in iterable:
        yield func(item)

squares = my_map(lambda x: x * x, [1, 2, 3, 4])
print(list(squares))  # [1, 4, 9, 16]
```

### 2. Custom filter

```python
def my_filter(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item

evens = my_filter(lambda x: x % 2 == 0, range(10))
print(list(evens))  # [0, 2, 4, 6, 8]
```

### 3. Comparison

| Operation | Built-in | Custom Generator | Generator Expression |
|-----------|----------|------------------|----------------------|
| map | `map(f, xs)` | `my_map(f, xs)` | `(f(x) for x in xs)` |
| filter | `filter(p, xs)` | `my_filter(p, xs)` | `(x for x in xs if p(x))` |

All three approaches are **lazy** — values computed on demand.


## Summary

- Lazy evaluation
- Memory efficient
- Single iteration
- Good for pipelines


## Exercises

**Exercise 1.**
A generator can only be iterated once. Predict the output:

```python
gen = (x**2 for x in range(5))
print(sum(gen))
print(sum(gen))
```

Why does the second `sum()` return `0`? How does this differ from a list comprehension? What is the underlying mechanism (the iterator protocol) that causes this behavior?

??? success "Solution to Exercise 1"
    Output:

    ```text
    30
    0
    ```

    A generator is a **single-use iterator**. The first `sum(gen)` iterates through all values (0, 1, 4, 9, 16), consuming the generator. After exhaustion, the generator is empty -- it has no way to "rewind." The second `sum(gen)` iterates over an already-exhausted generator, finding no values, and returns `0`.

    A list comprehension creates a **reusable list in memory**. You can iterate over it multiple times because all values are stored.

    The underlying mechanism is the **iterator protocol**: a generator object has a `__next__()` method that produces values one at a time and raises `StopIteration` when exhausted. Once `StopIteration` has been raised, subsequent calls to `__next__()` continue to raise `StopIteration` -- the generator cannot restart.

---

**Exercise 2.**
A generator expression uses parentheses `()`, but so does a tuple. Explain how Python distinguishes between these two:

```python
a = (1, 2, 3)
b = (x for x in range(3))
print(type(a))
print(type(b))
```

What syntactic clue tells Python that `b` is a generator, not a tuple? How do you create a tuple from a generator expression?

??? success "Solution to Exercise 2"
    Output:

    ```text
    <class 'tuple'>
    <class 'generator'>
    ```

    Python distinguishes them by the `for` keyword inside the parentheses. `(1, 2, 3)` contains literal expressions separated by commas -- it is a tuple. `(x for x in range(3))` contains a `for` clause -- it is a generator expression.

    To create a tuple from a generator expression:

    ```python
    t = tuple(x for x in range(3))  # (0, 1, 2)
    ```

    Note: `tuple()` accepts any iterable, including generators. The parentheses around the generator expression are optional when it is the sole argument to a function: `tuple(x for x in range(3))` and `tuple((x for x in range(3)))` are equivalent.

---

**Exercise 3.**
A programmer processes a 10 GB log file:

```python
# Approach A: list comprehension
errors = [line for line in open("huge.log") if "ERROR" in line]
count = len(errors)

# Approach B: generator expression
count = sum(1 for line in open("huge.log") if "ERROR" in line)
```

Explain the memory difference between the two approaches. Why does Approach B use constant memory while Approach A uses memory proportional to the number of matching lines? Why can you use `len()` with Approach A but not with Approach B?

??? success "Solution to Exercise 3"
    **Approach A** reads every matching line into a list stored in memory. If there are 1 million error lines averaging 200 bytes each, the list consumes ~200 MB. If the entire file matches, memory usage equals the file size (10 GB).

    **Approach B** processes one line at a time. At any moment, only one line is in memory. Each line is read, checked for "ERROR", and either counted (`+1`) or discarded. Memory usage is constant regardless of file size or number of matches.

    You can use `len()` with Approach A because a list knows its length (it stores all elements). You cannot use `len()` on a generator because a generator does not know how many elements it will produce -- values are computed lazily, one at a time. The only way to count generator elements is to iterate through them (which is what `sum(1 for ...)` does).

    Note: both approaches should use `with open(...)` for proper file handling. The examples omit this for brevity.
