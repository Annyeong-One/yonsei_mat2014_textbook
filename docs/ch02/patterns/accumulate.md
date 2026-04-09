
# The Accumulation Pattern

Picture a snowball rolling downhill. It starts small, and with each rotation it picks up more snow, growing larger and larger. The **accumulation pattern** works the same way: you walk through a collection, and at each step you combine the current element with a running result. When you reach the end, that running result is your answer. Unlike transform (which produces a collection) or filter (which produces a shorter collection), accumulation reduces an entire collection down to a single value.

## Mental Model

Every accumulation has three parts: an initial value, a combining operation, and the collection to process. The combining operation takes the running result and the next element and produces a new running result.

```
data:    [a,  b,  c,  d ]

step 0:  init
step 1:  init + a        = r1
step 2:  r1   + b        = r2
step 3:  r2   + c        = r3
step 4:  r3   + d        = final
```

The "+" here is any combining operation---addition, multiplication, string concatenation, list appending, or any custom logic.

## Summing with a Loop

The most basic accumulation is summing numbers.

```python
numbers = [10, 20, 30, 40, 50]

total = 0
for n in numbers:
    total += n

print(total)  # 150
```

The variable `total` is the accumulator. It starts at `0` and grows with each iteration.

## Counting with a Loop

Counting elements that satisfy a condition is another form of accumulation.

```python
words = ["apple", "banana", "avocado", "cherry", "apricot"]

count = 0
for w in words:
    if w.startswith("a"):
        count += 1

print(count)  # 3
```

The accumulator is an integer that increments by 1 each time the condition is met.

## Built-in Accumulation Functions

Python provides several built-in functions that encapsulate common accumulation patterns.

```python
numbers = [10, 20, 30, 40, 50]

print(sum(numbers))   # 150
print(min(numbers))   # 10
print(max(numbers))   # 50
print(len(numbers))   # 5
```

Each of these walks through the collection and reduces it to a single value. `sum()` accumulates with addition, `min()` keeps the smallest value seen so far, `max()` keeps the largest, and `len()` counts elements.

### sum() with a Start Value

`sum()` accepts an optional start value, which defaults to `0`.

```python
numbers = [1, 2, 3]
print(sum(numbers, 100))  # 106
```

This is equivalent to starting the accumulator at `100` instead of `0`.

## Building Strings

String concatenation is a form of accumulation. You start with an empty string and add pieces.

```python
words = ["Python", "is", "powerful"]

sentence = ""
for w in words:
    if sentence:
        sentence += " "
    sentence += w

print(sentence)  # "Python is powerful"
```

However, the idiomatic way to do this in Python is `str.join()`, which is both cleaner and faster.

```python
words = ["Python", "is", "powerful"]
sentence = " ".join(words)
print(sentence)  # "Python is powerful"
```

`join()` is preferred because string concatenation in a loop creates a new string object at each step, which is inefficient for large collections.

## Running Totals

Sometimes you need not just the final accumulated value but every intermediate result. This produces a list of partial accumulations.

```python
transactions = [100, -20, 50, -10, 30]

balance = 0
running = []
for t in transactions:
    balance += t
    running.append(balance)

print(running)  # [100, 80, 130, 120, 150]
```

Each entry in `running` is the balance after processing that transaction.

## Counting Occurrences

Accumulating into a dictionary lets you count how often each value appears.

```python
colors = ["red", "blue", "red", "green", "blue", "red"]

counts = {}
for color in colors:
    counts[color] = counts.get(color, 0) + 1

print(counts)  # {'red': 3, 'blue': 2, 'green': 1}
```

The dictionary is the accumulator. `dict.get(key, 0)` returns `0` for keys not yet seen, avoiding a `KeyError`.

## Flattening Nested Lists

Accumulation can combine sub-collections into one flat collection.

```python
nested = [[1, 2], [3, 4], [5, 6]]

flat = []
for sublist in nested:
    flat.extend(sublist)

print(flat)  # [1, 2, 3, 4, 5, 6]
```

You can also do this with a nested comprehension:

```python
flat = [x for sublist in nested for x in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

## functools.reduce()

The `functools.reduce()` function is the general-purpose accumulation tool. It takes a two-argument function, an iterable, and an optional initial value.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120
```

`reduce()` applies the lambda cumulatively: `((((1 * 2) * 3) * 4) * 5)`.

### reduce() with an Initial Value

```python
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda acc, x: acc + x, numbers, 100)
print(result)  # 106
```

The third argument `100` is the initial accumulator value. Without it, the first element of the iterable is used as the initial value.

### When to Use reduce()

`reduce()` is powerful but can be hard to read. Prefer built-in functions (`sum`, `min`, `max`) or explicit loops when they express your intent more clearly. Reserve `reduce()` for cases where the combining operation does not have a dedicated built-in.

---

## Exercises

**Exercise 1.**
Predict the output of this code that builds a running maximum.

```python
values = [3, 1, 4, 1, 5, 9, 2, 6]

current_max = float("-inf")
running_max = []
for v in values:
    if v > current_max:
        current_max = v
    running_max.append(current_max)

print(running_max)
print(current_max)
```

Why is `float("-inf")` used as the initial value instead of `0`? In what scenario would starting with `0` give a wrong result?

??? success "Solution to Exercise 1"
    Output:

    ```text
    [3, 3, 4, 4, 5, 9, 9, 9]
    9
    ```

    Each entry in `running_max` is the largest value seen up to and including that position. The accumulator `current_max` only increases when a new value exceeds it.

    `float("-inf")` is used because it is smaller than every possible number. If you started with `0` and all values were negative (e.g., `[-5, -3, -8]`), the running maximum would incorrectly stay at `0` for the entire list---no negative value would ever exceed `0`. Starting with negative infinity guarantees that the first element always becomes the initial maximum.

---

**Exercise 2.**
Write a function `word_lengths` that takes a string, splits it into words, and returns a dictionary mapping each word to its length.

```python
def word_lengths(text):
    # your code here
    pass

result = word_lengths("the quick brown fox jumps over the lazy dog")
print(result)
```

What happens with repeated words like `"the"`? Does the function handle that correctly?

??? success "Solution to Exercise 2"
    ```python
    def word_lengths(text):
        lengths = {}
        for word in text.split():
            lengths[word] = len(word)
        return lengths

    result = word_lengths("the quick brown fox jumps over the lazy dog")
    print(result)
    ```

    Output:

    ```text
    {'the': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumps': 5, 'over': 4, 'lazy': 4, 'dog': 3}
    ```

    Repeated words like `"the"` simply overwrite the same key with the same value, so the result is correct. Since every occurrence of the same word has the same length, the duplication is harmless.

    A dictionary comprehension version is also possible:

    ```python
    def word_lengths(text):
        return {word: len(word) for word in text.split()}
    ```

    This is a combined transform-and-accumulate pattern: transform each word into a `(word, length)` pair, and accumulate the pairs into a dictionary.

---

**Exercise 3.**
Predict the output of this `reduce()` call and then rewrite it as an explicit loop.

```python
from functools import reduce

data = ["h", "e", "l", "l", "o"]
result = reduce(lambda acc, ch: acc + ch.upper(), data, ">>")
print(result)
```

What role does the third argument `">>"` play? What would happen without it?

??? success "Solution to Exercise 3"
    Output:

    ```text
    >>HELLO
    ```

    The third argument `">>"` is the initial accumulator value. `reduce()` processes each character, uppercases it, and appends it to the accumulator:

    - Start: `">>"`
    - Step 1: `">>" + "H"` = `">>H"`
    - Step 2: `">>H" + "E"` = `">>HE"`
    - Step 3: `">>HE" + "L"` = `">>HEL"`
    - Step 4: `">>HEL" + "L"` = `">>HELL"`
    - Step 5: `">>HELL" + "O"` = `">>HELLO"`

    Without the third argument, `reduce()` uses the first element `"h"` as the initial accumulator. The lambda would then process starting from the second element, and the first character would not be uppercased:

    ```python
    result = reduce(lambda acc, ch: acc + ch.upper(), data)
    print(result)  # hELLO
    ```

    Rewritten as an explicit loop:

    ```python
    data = ["h", "e", "l", "l", "o"]
    result = ">>"
    for ch in data:
        result = result + ch.upper()
    print(result)  # >>HELLO
    ```
