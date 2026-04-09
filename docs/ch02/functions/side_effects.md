
# Side Effects

## The Mental Model

A function takes inputs and produces an output. That is the idealized view. In practice, many functions do more than just compute a return value---they change things in the world outside themselves. These external changes are called **side effects**.

A **side effect** is any observable change that a function causes beyond returning a value. If you could replace a function call with its return value and the program would behave differently, the function has side effects.

Think of a function as a worker in a factory. The "return value" is the product they hand back to you. A "side effect" is anything else they do: rearranging the factory floor, writing a note on the whiteboard, opening a window. These actions may be intentional and useful, but they are not part of the product itself.

## What Counts as a Side Effect

Side effects include:

1. **Modifying a mutable argument**
2. **Printing to the console**
3. **Writing to or reading from a file**
4. **Modifying global or nonlocal variables**
5. **Modifying class or instance attributes**
6. **Raising exceptions** (in some analyses)
7. **Making network requests**

### Modifying a Mutable Argument

```python
def sort_and_return_first(items):
    items.sort()      # side effect: modifies the caller's list
    return items[0]

data = [3, 1, 4, 1, 5]
smallest = sort_and_return_first(data)
print(smallest)  # 1
print(data)      # [1, 1, 3, 4, 5] -- the caller's list was sorted!
```

The function returns the smallest element, but it also rearranges the caller's list. That rearrangement is a side effect.

### Printing to the Console

```python
def compute_area(width, height):
    area = width * height
    print(f"Computing area: {width} x {height} = {area}")  # side effect
    return area
```

Printing is a side effect because it changes the state of the console output. You cannot replace `compute_area(3, 4)` with `12` without losing the printed message.

### Writing to a File

```python
def log_result(filename, result):
    with open(filename, "a") as f:
        f.write(f"{result}\n")  # side effect: modifies the filesystem
    return result
```

### Modifying Global State

```python
call_count = 0

def tracked_add(a, b):
    global call_count
    call_count += 1  # side effect: modifies global variable
    return a + b

tracked_add(1, 2)
tracked_add(3, 4)
print(call_count)  # 2
```

## Pure Functions vs Functions with Side Effects

A **pure function** has two properties:

1. Its return value depends **only** on its arguments (same inputs always produce the same output).
2. It has **no side effects**.

```python
# Pure function
def add(a, b):
    return a + b

# Impure: depends on external state
current_bonus = 10
def add_with_bonus(a, b):
    return a + b + current_bonus  # depends on global variable

# Impure: has a side effect
def add_and_print(a, b):
    result = a + b
    print(result)  # side effect
    return result
```

Pure functions are easier to reason about because you only need to look at the inputs and the output. You do not need to consider what state might have changed elsewhere.

## Why Side Effects Matter

### Reasoning About Code

Consider debugging a program where a list unexpectedly changes:

```python
data = [1, 2, 3, 4, 5]
result = process(data)        # does this modify data?
summary = summarize(data)     # what about this?
output = format_report(data)  # or this?
```

If any of these functions modifies `data` as a side effect, you must read each function's implementation to understand what `data` contains at each step. With pure functions, you would know that `data` is always `[1, 2, 3, 4, 5]`.

### Testing

Functions with side effects are harder to test because you must set up and verify external state:

```python
# Hard to test: depends on and modifies external state
def process_and_save(data, filename):
    result = [x * 2 for x in data]
    with open(filename, "w") as f:
        f.write(str(result))
    return result

# Easier to test: pure computation
def process(data):
    return [x * 2 for x in data]
```

### Composition

Pure functions compose predictably. Functions with side effects can interact in unexpected ways:

```python
def add_tax(prices):
    for i in range(len(prices)):
        prices[i] *= 1.1  # side effect: modifies the list
    return prices

def add_discount(prices):
    for i in range(len(prices)):
        prices[i] *= 0.9  # side effect: modifies the list
    return prices

items = [100, 200, 300]
add_tax(items)
add_discount(items)
print(items)  # [99.0, 198.0, 297.0] -- both functions modified the same list
```

The order of calls matters, and the original data is lost.

## Identifying Side Effects

To identify side effects in a function, ask these questions:

1. Does the function modify any of its arguments?
2. Does the function use `print()`, `input()`, or any I/O?
3. Does the function use `global` or `nonlocal`?
4. Does the function modify any object accessible from outside its scope?
5. Does the function interact with the filesystem, network, or database?

```python
def analyze_function(items, config, threshold):
    # Mutation of argument -- side effect
    items.sort()

    # Reading from global -- not a side effect, but makes function impure
    # Writing to global -- side effect
    global total_calls
    total_calls += 1

    # Print -- side effect
    print(f"Processing {len(items)} items")

    # Pure computation -- no side effect
    filtered = [x for x in items if x > threshold]
    average = sum(filtered) / len(filtered) if filtered else 0

    return average
```

This function has **three** side effects: sorting `items`, incrementing `total_calls`, and printing.

## Managing Side Effects

Side effects are not inherently bad---programs need to print output, write files, and update state. The goal is to **control** them, not eliminate them.

### Separate Pure Logic from Side Effects

```python
# Instead of one function with mixed concerns:
def process_and_save(data, filename):
    result = sorted(data)  # computation
    with open(filename, "w") as f:  # I/O
        for item in result:
            f.write(f"{item}\n")

# Separate into pure computation and I/O:
def process(data):
    return sorted(data)  # pure: no side effects

def save(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(f"{item}\n")  # side effect is explicit and isolated

result = process(data)
save(result, "output.txt")
```

### Document Side Effects

When a function has side effects, document them clearly:

```python
def register_user(users, name, email):
    """Add a new user to the users dictionary.

    Modifies `users` in place by adding a new entry.
    Prints a confirmation message to stdout.

    Args:
        users: Dictionary of existing users. Modified in place.
        name: The new user's name.
        email: The new user's email.
    """
    users[name] = email
    print(f"Registered: {name}")
```

### Return New Objects Instead of Modifying Arguments

```python
# Side effect version
def normalize(data):
    for i in range(len(data)):
        data[i] = data[i].strip().lower()

# Pure version -- returns a new list
def normalize(data):
    return [item.strip().lower() for item in data]
```

---

## Exercises

**Exercise 1.**
Identify all side effects in the following function. For each side effect, explain what external state is being changed and suggest how to refactor the function to separate pure computation from side effects.

```python
results_log = []

def calculate_statistics(numbers):
    numbers.sort()
    mean = sum(numbers) / len(numbers)
    median = numbers[len(numbers) // 2]
    results_log.append({"mean": mean, "median": median})
    print(f"Mean: {mean}, Median: {median}")
    return mean, median
```

??? success "Solution to Exercise 1"
    Three side effects:

    1. **`numbers.sort()`**: Modifies the caller's list. The caller's data is rearranged after the function returns.
    2. **`results_log.append(...)`**: Modifies a global list. This changes state outside the function.
    3. **`print(...)`**: Writes to stdout. This is an I/O side effect.

    Refactored version separating pure computation from side effects:

    ```python
    # Pure computation -- no side effects
    def calculate_statistics(numbers):
        sorted_nums = sorted(numbers)  # creates a new list, does not modify input
        mean = sum(sorted_nums) / len(sorted_nums)
        median = sorted_nums[len(sorted_nums) // 2]
        return mean, median

    # Side effects isolated and explicit
    def log_and_display(stats, results_log):
        mean, median = stats
        results_log.append({"mean": mean, "median": median})
        print(f"Mean: {mean}, Median: {median}")

    # Usage
    results_log = []
    data = [3, 1, 4, 1, 5]
    stats = calculate_statistics(data)
    log_and_display(stats, results_log)
    print(data)  # [3, 1, 4, 1, 5] -- preserved
    ```

    The pure function is now easy to test (give it inputs, check outputs) and does not surprise callers by reordering their data.

---

**Exercise 2.**
The following two functions produce the same final list, but one has a side effect and the other does not. Write a short test scenario that demonstrates a practical difference between them---a situation where using the side-effect version causes a problem that the pure version avoids.

```python
# Version A: side effect
def add_header_a(lines):
    lines.insert(0, "=== REPORT ===")

# Version B: pure
def add_header_b(lines):
    return ["=== REPORT ==="] + lines
```

??? success "Solution to Exercise 2"
    A practical scenario where the side-effect version causes a problem:

    ```python
    original_data = ["Line 1", "Line 2", "Line 3"]

    # You want to create two reports with different headers
    # but keep the original data intact for reuse.

    # Using Version A (side effect):
    add_header_a(original_data)
    report_1 = original_data
    # Now original_data is ["=== REPORT ===", "Line 1", "Line 2", "Line 3"]

    # Trying to use original_data again for a second purpose:
    print(original_data)
    # ['=== REPORT ===', 'Line 1', 'Line 2', 'Line 3'] -- corrupted!
    ```

    The original data has been permanently modified. You cannot reuse it.

    ```python
    # Using Version B (pure):
    original_data = ["Line 1", "Line 2", "Line 3"]

    report_1 = add_header_b(original_data)
    report_2 = add_header_b(original_data)  # safe -- original_data is unchanged

    print(original_data)  # ['Line 1', 'Line 2', 'Line 3'] -- preserved
    print(report_1)       # ['=== REPORT ===', 'Line 1', 'Line 2', 'Line 3']
    print(report_2)       # ['=== REPORT ===', 'Line 1', 'Line 2', 'Line 3']
    ```

    The pure version lets you reuse `original_data` freely because it is never modified. This is especially important in loops or when multiple parts of the program share the same data.

---

**Exercise 3.**
Consider the following function:

```python
def apply_operations(data, operations):
    for op in operations:
        data = op(data)
    return data
```

Is `apply_operations` itself a pure function? It depends on what `operations` contains. Given the following two sets of operations, determine whether the overall pipeline has side effects:

```python
# Pipeline A
def double_all(lst):
    return [x * 2 for x in lst]

def keep_positive(lst):
    return [x for x in lst if x > 0]

# Pipeline B
def double_in_place(lst):
    for i in range(len(lst)):
        lst[i] *= 2
    return lst

def remove_negatives(lst):
    lst[:] = [x for x in lst if x > 0]
    return lst

numbers = [-1, 2, -3, 4]
result_a = apply_operations(numbers[:], [double_all, keep_positive])
result_b = apply_operations(numbers, [double_in_place, remove_negatives])
print(numbers)
```

Predict the output and explain the difference.

??? success "Solution to Exercise 3"
    Output:

    ```text
    [-2, 4, -6, 8]
    ```

    **Pipeline A** uses pure operations. `double_all` and `keep_positive` each return new lists without modifying their inputs. Note that we passed `numbers[:]` (a copy), so even if there were side effects, `numbers` would be safe. But the purity of the operations means no side effects occur at all.

    **Pipeline B** uses impure operations. `double_in_place` modifies the list in place (each element is doubled), and `remove_negatives` modifies the list in place (keeping only positive elements). Since we passed `numbers` directly (no copy), these side effects modify the caller's list.

    After `double_in_place`: `numbers` becomes `[-2, 4, -6, 8]`.

    After `remove_negatives`: `numbers` becomes `[4, 8]`.

    But wait---`apply_operations` contains `data = op(data)`, which rebinds `data` to the return value of each operation. Since both Pipeline B functions return the same list they modified, `data` still refers to the same object as `numbers` throughout.

    The final value of `numbers` is `[4, 8]`.

    Actually, let us trace more carefully:

    - `data` starts as `numbers` (same object: `[-1, 2, -3, 4]`).
    - `double_in_place(data)` modifies the list to `[-2, 4, -6, 8]` and returns it. `data = op(data)` rebinds `data` to the same list. `numbers` is now `[-2, 4, -6, 8]`.
    - `remove_negatives(data)` modifies the list via `lst[:] = ...` to `[4, 8]` and returns it. `numbers` is now `[4, 8]`.

    The output of `print(numbers)` is `[4, 8]`.

    The key lesson: `apply_operations` is only as pure as the operations you pass to it. Pure operations make the pipeline safe and predictable; impure operations introduce side effects that propagate to the caller.
