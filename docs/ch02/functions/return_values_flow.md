
# Return Values and Data Flow

## The Mental Model

A function is a data transformation machine. Data flows **in** through arguments and flows **out** through the return value. The `return` statement is not just "producing output"---it is the mechanism by which data **leaves** a function and enters the caller's world.

Think of a function as a workshop behind a closed door. You slide materials in through a slot (arguments). The workshop does its work. Then it slides the finished product back out through another slot (return value). Everything that happens inside the workshop is invisible to you---all you see is what comes out.

This mental model has an important implication: if a function does not return anything, no data flows out. The caller receives `None`, which is Python's way of saying "nothing was handed back."

## Return as Data Movement

Every `return` statement does two things:

1. **Terminates** the function's execution.
2. **Passes an object** back to the caller.

```python
def square(n):
    return n * n

result = square(5)
print(result)  # 25
```

The object `25` is created inside the function, then **moved** to the caller via `return`. The caller can bind it to a name, pass it to another function, or use it in an expression:

```python
# Bind to a name
area = square(5)

# Pass directly to another function
print(square(5))

# Use in an expression
total = square(3) + square(4)
```

The return value is the function's **sole official output channel**. Anything else the function does (printing, modifying arguments, writing files) is a side effect.

## Returning New Objects vs Returning Modified Objects

There are two common patterns for functions that transform data.

### Pattern 1: Return a New Object

The function creates and returns a new object. The original input is unchanged.

```python
def sorted_copy(items):
    return sorted(items)  # sorted() creates a new list

original = [3, 1, 4, 1, 5]
result = sorted_copy(original)
print(original)  # [3, 1, 4, 1, 5] -- unchanged
print(result)    # [1, 1, 3, 4, 5] -- new list
```

This pattern is **predictable**: the caller knows that `original` is safe, and the return value contains the result. Data flows cleanly from input to output.

### Pattern 2: Modify and Return the Same Object

The function modifies the input in place and returns a reference to it.

```python
def sort_in_place(items):
    items.sort()
    return items

original = [3, 1, 4, 1, 5]
result = sort_in_place(original)
print(original)  # [1, 1, 3, 4, 5] -- modified!
print(result)    # [1, 1, 3, 4, 5] -- same object
print(original is result)  # True
```

This pattern is common but can be confusing: the return value and the original are the same object.

### Pattern 3: Modify in Place, Return None

Many of Python's built-in methods follow this convention: methods that modify an object in place return `None`.

```python
original = [3, 1, 4, 1, 5]
result = original.sort()  # sort() modifies in place, returns None
print(original)  # [1, 1, 3, 4, 5]
print(result)    # None
```

This is a deliberate design choice. By returning `None`, Python signals that the operation modified the existing object rather than creating a new one. You are not supposed to use the return value---the effect is on the object itself.

| Function/Method | Creates new object? | Returns |
| --- | --- | --- |
| `sorted(lst)` | Yes | New sorted list |
| `lst.sort()` | No (in-place) | `None` |
| `reversed(lst)` | Yes (iterator) | Iterator |
| `lst.reverse()` | No (in-place) | `None` |
| `lst + [x]` | Yes | New list |
| `lst.append(x)` | No (in-place) | `None` |

## Explicit Return vs Implicit Return

### Explicit Return

A function that explicitly uses `return` with a value:

```python
def add(a, b):
    return a + b
```

### Explicit Return of None

A function can explicitly return `None` to signal "no meaningful result":

```python
def validate(data):
    if not isinstance(data, list):
        return None  # explicit: no valid result
    if len(data) == 0:
        return None  # explicit: no valid result
    return sum(data) / len(data)
```

### Implicit Return of None

If a function ends without a `return` statement, or reaches a `return` with no value, Python implicitly returns `None`:

```python
def greet(name):
    print(f"Hello, {name}")
    # no return statement -- implicitly returns None

result = greet("Alice")
print(result)  # None
```

```python
def check(value):
    if value < 0:
        return  # returns None (no value given)
    print(f"Value is {value}")

result = check(-1)
print(result)  # None
```

### When Each Pattern is Appropriate

| Pattern | Use when |
| --- | --- |
| `return value` | The function computes a result that the caller needs |
| `return None` (explicit) | The function might not have a meaningful result in some cases |
| No return / `return` | The function is called for its side effects (printing, modifying state) |

## Data Flow Chains

Return values enable **chaining**: the output of one function becomes the input of the next.

```python
def read_words(text):
    return text.split()

def filter_long(words, min_length):
    return [w for w in words if len(w) >= min_length]

def capitalize_all(words):
    return [w.upper() for w in words]

# Data flows through a chain of transformations
text = "the quick brown fox jumps over the lazy dog"
words = read_words(text)
long_words = filter_long(words, 4)
result = capitalize_all(long_words)
print(result)  # ['QUICK', 'BROWN', 'JUMPS', 'OVER', 'LAZY']
```

Each function receives data, transforms it, and passes the result forward. This is clean data flow: no side effects, no hidden state, each step is independently testable.

You can also write this as a single expression:

```python
result = capitalize_all(filter_long(read_words(text), 4))
```

This is equivalent but harder to read. The intermediate variable version makes the data flow explicit.

## The Return Value as a Contract

A function's return value is part of its **contract** with the caller. The caller depends on what the function returns. Changing the return type or meaning can break code far from the function definition.

```python
def find_user(users, name):
    for user in users:
        if user["name"] == name:
            return user
    return None  # explicit: user not found

# Caller relies on the contract
user = find_user(database, "Alice")
if user is not None:
    print(user["email"])
```

If `find_user` suddenly returned an empty dictionary `{}` instead of `None` when the user is not found, the caller's `if user is not None` check would pass incorrectly because `{}` is not `None`.

## Common Mistakes

### Forgetting to Return

```python
def compute_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    # forgot to return average!

result = compute_average([1, 2, 3])
print(result)  # None -- oops
```

### Unreachable Return

```python
def classify(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    # what if value == 0? Implicitly returns None

print(classify(0))  # None -- unintended
```

Fix:

```python
def classify(value):
    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "zero"
```

### Using the Return Value of an In-Place Method

```python
numbers = [3, 1, 4]
sorted_numbers = numbers.sort()  # sort() returns None!
print(sorted_numbers)  # None

# Correct:
sorted_numbers = sorted(numbers)  # sorted() returns a new list
```

---

## Exercises

**Exercise 1.**
Consider the following function:

```python
def process(items):
    items.append("processed")
    return items
```

A caller writes:

```python
data = [1, 2, 3]
result = process(data)
print(data is result)
print(data)
print(result)
```

Predict the output. Then answer: is this function using return to communicate data flow, or is the return value redundant because the data was already communicated via a side effect? What would be a cleaner design?

??? success "Solution to Exercise 1"
    Output:

    ```text
    True
    [1, 2, 3, 'processed']
    [1, 2, 3, 'processed']
    ```

    `data is result` is `True` because the function returns the same list object it received. The `return items` is **redundant** -- the caller's `data` was already modified by `items.append("processed")`. The return value and the side effect communicate the same information through two different channels.

    This is a confusing design because it is ambiguous: does the caller use the return value or the side effect? Cleaner alternatives:

    **Option A: Pure function (return new data, no side effect)**

    ```python
    def process(items):
        return items + ["processed"]

    data = [1, 2, 3]
    result = process(data)
    # data is unchanged, result is the new version
    ```

    **Option B: Side effect only (modify in place, return None)**

    ```python
    def process(items):
        items.append("processed")
        # no return -- signals "I modified your data in place"

    data = [1, 2, 3]
    process(data)
    # data is modified, no return value to capture
    ```

    Choose one channel, not both.

---

**Exercise 2.**
Write a function `safe_divide(a, b)` that returns the result of `a / b` if `b` is not zero, and returns `None` if `b` is zero. Then write caller code that uses the return value correctly, handling the `None` case.

Explain: why is returning `None` for the error case both useful and potentially dangerous? What could go wrong if the caller forgets to check for `None`?

??? success "Solution to Exercise 2"
    ```python
    def safe_divide(a, b):
        if b == 0:
            return None
        return a / b

    # Correct caller code
    result = safe_divide(10, 3)
    if result is not None:
        print(f"Result: {result:.2f}")
    else:
        print("Cannot divide by zero")

    result = safe_divide(10, 0)
    if result is not None:
        print(f"Result: {result:.2f}")
    else:
        print("Cannot divide by zero")
    ```

    Output:

    ```text
    Result: 3.33
    Cannot divide by zero
    ```

    **Why returning `None` is useful**: It allows the function to signal "no valid result" without raising an exception. The caller can check for `None` and handle the case gracefully.

    **Why it is dangerous**: If the caller forgets to check for `None`, they might use it in arithmetic or other operations, causing a `TypeError` far from the source of the problem:

    ```python
    result = safe_divide(10, 0)
    final = result + 5  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    ```

    The error message does not mention division by zero -- it complains about adding `None` and `int`, which is confusing. This is sometimes called the "billion-dollar mistake" (Tony Hoare's term for null references). An alternative approach is to raise a `ValueError`:

    ```python
    def safe_divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

    This forces the caller to handle the error case explicitly with `try/except`, making it harder to accidentally ignore.

---

**Exercise 3.**
Trace the data flow through the following program. For each function call, identify what data flows in (arguments) and what data flows out (return value). Does any function rely on side effects to communicate results?

```python
def extract_numbers(text):
    return [int(word) for word in text.split() if word.isdigit()]

def compute_stats(numbers):
    if not numbers:
        return {"count": 0, "total": 0, "average": 0}
    total = sum(numbers)
    return {
        "count": len(numbers),
        "total": total,
        "average": total / len(numbers),
    }

def format_report(stats):
    lines = []
    lines.append(f"Count:   {stats['count']}")
    lines.append(f"Total:   {stats['total']}")
    lines.append(f"Average: {stats['average']:.1f}")
    return "\n".join(lines)

raw = "There are 10 apples and 20 oranges and 5 bananas"
numbers = extract_numbers(raw)
stats = compute_stats(numbers)
report = format_report(stats)
print(report)
```

??? success "Solution to Exercise 3"
    Output:

    ```text
    Count:   3
    Total:   35
    Average: 11.7
    ```

    Data flow analysis:

    | Step | Function | Data In (arguments) | Data Out (return value) |
    | --- | --- | --- | --- |
    | 1 | `extract_numbers` | `"There are 10 apples and 20 oranges and 5 bananas"` (str) | `[10, 20, 5]` (new list of ints) |
    | 2 | `compute_stats` | `[10, 20, 5]` (list) | `{"count": 3, "total": 35, "average": 11.666...}` (new dict) |
    | 3 | `format_report` | `{"count": 3, "total": 35, "average": 11.666...}` (dict) | `"Count:   3\nTotal:   35\nAverage: 11.7"` (new str) |
    | 4 | `print` | `"Count:   3\n..."` (str) | `None` (side effect: writes to stdout) |

    No function relies on side effects to communicate results. Each function receives data through its arguments, creates a new object, and returns it. The caller captures the return value and passes it to the next function.

    The only side effect in the entire program is `print(report)`, which writes to the console. This is the boundary between pure computation and observable output---a natural and necessary place for a side effect.

    This is an example of clean data flow: data enters from the left and transforms step by step, with each function receiving the previous function's output as input.
