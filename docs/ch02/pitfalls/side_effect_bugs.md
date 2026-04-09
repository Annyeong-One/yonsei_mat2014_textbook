
# Unexpected Side Effects

## The Mental Model

A **side effect** is any observable change a function makes beyond returning a value. This includes modifying an argument, changing a global variable, writing to a file, or printing to the screen. Side effects are not inherently bad---a program that never writes output is useless. The bugs arise when side effects are **unexpected**: the caller does not realize that calling a function will modify its data, alter shared state, or change behavior on subsequent calls.

The core principle is: a function's observable effects should match the caller's expectations. When they diverge, you get bugs that are difficult to reproduce and painful to trace.

## Modifying the Caller's Data

The most common side-effect bug occurs when a function mutates an argument that the caller assumed would remain unchanged:

```python
def get_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]

all_scores = [72, 95, 88, 64, 91, 83]
top = get_top_three(all_scores)

print(top)         # [95, 91, 88]
print(all_scores)  # [95, 91, 88, 83, 72, 64]  -- original order destroyed
```

The caller wanted the top three scores but did not expect `get_top_three` to permanently reorder its data. The function name suggests a read-only query, but the implementation mutates the input.

The fix is to avoid modifying the argument:

```python
def get_top_three(scores):
    return sorted(scores, reverse=True)[:3]

all_scores = [72, 95, 88, 64, 91, 83]
top = get_top_three(all_scores)

print(top)         # [95, 91, 88]
print(all_scores)  # [72, 95, 88, 64, 91, 83]  -- unchanged
```

`sorted()` returns a new list, leaving the original intact. Alternatively, the function could sort a copy: `working = scores.copy(); working.sort(...)`.

## Global State Changes Between Calls

When functions read or write global variables, their behavior depends on the order of calls. This creates bugs that appear and disappear depending on execution context:

```python
_counter = 0

def generate_id():
    global _counter
    _counter += 1
    return f"item-{_counter}"

def reset_ids():
    global _counter
    _counter = 0
```

The function `generate_id` produces different results depending on how many times it has been called before:

```python
print(generate_id())  # item-1
print(generate_id())  # item-2
reset_ids()
print(generate_id())  # item-1  -- same as the first call
```

In a testing environment, tests that call `generate_id` will produce different results depending on test execution order. A test that passes in isolation may fail when run after other tests.

The fix is to make state explicit by passing it as an argument or encapsulating it in an object:

```python
def generate_id(counter):
    return f"item-{counter + 1}", counter + 1

counter = 0
label, counter = generate_id(counter)  # ('item-1', 1)
label, counter = generate_id(counter)  # ('item-2', 2)
```

Now the state is visible and controlled by the caller. There is no hidden dependency on global state.

## Modifying a Collection While Iterating

Modifying a list, dictionary, or set while iterating over it produces unpredictable results. Python may skip elements, process elements twice, or raise an error:

### List Mutation During Iteration

```python
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # [1, 3, 5, 6]  -- 6 was skipped
```

When `2` is removed, every subsequent element shifts left. The iterator's internal index advances past the shifted `3`, and later `6` is never checked because the list shrank. The result is silently wrong.

### Dictionary Mutation During Iteration

```python
data = {"a": 1, "b": 2, "c": 3}

for key in data:
    if data[key] < 3:
        del data[key]  # RuntimeError: dictionary changed size during iteration
```

Python raises a `RuntimeError` for dictionaries (and sets), making the bug immediately visible---unlike lists, where the bug is silent.

### The Fix: Iterate Over a Copy or Build a New Collection

For lists, iterate over a copy:

```python
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers.copy():  # or numbers[:]
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # [1, 3, 5]  -- correct
```

Or build a new list (often cleaner):

```python
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)  # [1, 3, 5]
```

For dictionaries, collect keys first:

```python
data = {"a": 1, "b": 2, "c": 3}

keys_to_delete = [key for key in data if data[key] < 3]
for key in keys_to_delete:
    del data[key]

print(data)  # {'c': 3}
```

## Real-World Debugging Scenario

Consider a data pipeline that processes records, filters invalid ones, and then passes the data to a reporting function:

```python
def validate_records(records):
    """Remove records with missing 'name' field."""
    for r in records:
        if "name" not in r:
            records.remove(r)
    return records

def generate_report(records):
    """Create summary from valid records."""
    return [f"Report for {r['name']}" for r in records]

raw_data = [
    {"name": "Alice", "score": 85},
    {"score": 0},
    {"score": 0},
    {"name": "Bob", "score": 92},
]

clean = validate_records(raw_data)
report = generate_report(clean)
print(report)
```

This code has **two** bugs. First, `validate_records` modifies the caller's `raw_data` list---after the call, `raw_data` has lost elements. Second, removing elements during iteration causes the loop to skip the second invalid record.

A correct version avoids both problems:

```python
def validate_records(records):
    """Return only records with a 'name' field. Does not modify input."""
    return [r for r in records if "name" in r]

raw_data = [
    {"name": "Alice", "score": 85},
    {"score": 0},
    {"score": 0},
    {"name": "Bob", "score": 92},
]

clean = validate_records(raw_data)
report = generate_report(clean)
print(report)   # ['Report for Alice', 'Report for Bob']
print(raw_data) # all four original records still present
```

## Defensive Programming Strategies

| Strategy | When to use |
|---|---|
| Return new objects instead of mutating arguments | Default approach for functions that transform data |
| Copy arguments at function entry | When mutation is needed internally but the caller's data must be preserved |
| Avoid global mutable state | Always; pass state explicitly or encapsulate in objects |
| Never modify a collection during iteration | Always; iterate over a copy or build a new collection |
| Name functions to signal intent | Use verbs like `sort_` or `remove_` for mutating functions; use noun-like names for functions that return new values |

A useful rule of thumb: **a function should either return a value or produce a side effect, but not both**. Functions that return a computed result should not also modify their inputs. Functions that modify state (like `list.sort()`) conventionally return `None` to signal that the operation happened in place.

## Exercises

**Exercise 1.**
The following function is supposed to return a cleaned copy of a dictionary, removing keys with `None` values. But it has a bug.

```python
def clean_data(d):
    for key in d:
        if d[key] is None:
            del d[key]
    return d

config = {"host": "localhost", "port": None, "debug": True, "timeout": None}
cleaned = clean_data(config)
```

(a) What error does this code raise, and why?

(b) Identify a second problem: even if it did not raise an error, what would happen to `config`?

(c) Rewrite `clean_data` so that it returns a new dictionary without `None` values and does not modify the original.

??? success "Solution to Exercise 1"
    **(a)** It raises `RuntimeError: dictionary changed size during iteration`. Python does not allow deleting keys from a dictionary while iterating over it. When `del d[key]` executes during the loop, the dictionary's internal structure changes, and Python detects the modification.

    **(b)** Even if the error were somehow avoided, the function modifies the caller's dictionary `config` directly (since `d` is an alias for `config`). After the call, `config` would be missing its `None`-valued keys. The caller might not expect that.

    **(c)** A correct version that returns a new dictionary:

    ```python
    def clean_data(d):
        return {key: value for key, value in d.items() if value is not None}

    config = {"host": "localhost", "port": None, "debug": True, "timeout": None}
    cleaned = clean_data(config)

    print(cleaned)  # {'host': 'localhost', 'debug': True}
    print(config)   # {'host': 'localhost', 'port': None, 'debug': True, 'timeout': None}
    ```

    The dictionary comprehension builds a new dictionary. The original `config` is never modified.

---

**Exercise 2.**
A programmer writes a function that should return the list with its largest element removed. However, the function has an unexpected side effect.

```python
def without_max(values):
    values.remove(max(values))
    return values

grades = [88, 95, 72, 95, 91]
adjusted = without_max(grades)

print(adjusted)
print(grades)
```

(a) What does `adjusted` contain? What does `grades` contain? Are they the same object?

(b) Rewrite the function so that `grades` is not modified.

??? success "Solution to Exercise 2"
    **(a)** Output:

    ```text
    [88, 72, 95, 91]
    [88, 72, 95, 91]
    ```

    `values.remove(max(values))` finds the maximum (`95`) and removes its **first occurrence**. The second `95` remains. Because `values` is an alias for `grades`, the original list is mutated. `adjusted` and `grades` are the same object (`adjusted is grades` is `True`).

    **(b)** A version that does not modify the original:

    ```python
    def without_max(values):
        result = values.copy()
        result.remove(max(result))
        return result

    grades = [88, 95, 72, 95, 91]
    adjusted = without_max(grades)

    print(adjusted)  # [88, 72, 95, 91]
    print(grades)    # [88, 95, 72, 95, 91]  -- unchanged
    ```

    By copying first, the `remove` call mutates only the local copy. The caller's data is preserved.

---

**Exercise 3.**
The following code attempts to remove all occurrences of a target value from a list. It runs without error but produces the wrong result.

```python
def remove_all(items, target):
    for item in items:
        if item == target:
            items.remove(item)

data = [1, 2, 2, 2, 3, 4, 2]
remove_all(data, 2)
print(data)
```

(a) What does `data` contain after the call? Why are some `2`s left?

(b) Provide two different correct implementations: one that modifies the list in place and one that returns a new list.

??? success "Solution to Exercise 3"
    **(a)** Output:

    ```text
    [1, 2, 3, 4, 2]
    ```

    Two `2`s remain. When the first `2` at index 1 is removed, the elements shift left: the second `2` (originally at index 2) moves to index 1, but the iterator has already advanced past index 1. It checks index 2 next, which now holds the third `2`. That one is removed, but the `2` that slid into index 1 was never checked. The same skip happens later, leaving two `2`s in the list.

    **(b)** In-place modification (iterate backward to avoid index shifting):

    ```python
    def remove_all(items, target):
        i = len(items) - 1
        while i >= 0:
            if items[i] == target:
                items.pop(i)
            i -= 1

    data = [1, 2, 2, 2, 3, 4, 2]
    remove_all(data, 2)
    print(data)  # [1, 3, 4]
    ```

    Return a new list (functional approach):

    ```python
    def remove_all(items, target):
        return [item for item in items if item != target]

    data = [1, 2, 2, 2, 3, 4, 2]
    result = remove_all(data, 2)
    print(result)  # [1, 3, 4]
    print(data)    # [1, 2, 2, 2, 3, 4, 2]  -- original unchanged
    ```

    The list comprehension approach is generally preferred because it is clearer, avoids mutation pitfalls, and communicates that a new collection is being created.
