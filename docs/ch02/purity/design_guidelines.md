
# Designing Predictable Functions

Knowing the difference between pure functions and side effects is the theory. This page is about the practice: concrete guidelines for structuring code so that functions are as predictable as possible and side effects are controlled rather than scattered.

## The Mental Model

Think of a well-designed program as a factory with two zones. The **clean room** is where precise calculations happen---no dust, no distractions, no surprises. The **loading dock** is where messy real-world interactions occur---receiving shipments, sending packages, talking to suppliers. You want the clean room to be as large as possible and the loading dock to be as small and well-defined as possible.

In code, the clean room is your pure functions. The loading dock is the thin layer that handles I/O, user interaction, and state changes. This separation is sometimes called the **functional core / imperative shell** pattern.

## Guideline 1 -- Prefer Pure Functions

Whenever you write a function, start by asking: can this be pure? If the function's job is to compute, transform, or decide something, it almost certainly can be.

```python
# Impure: reads from global state and prints
config = {"tax_rate": 0.08}

def calculate_total(price, quantity):
    subtotal = price * quantity
    tax = subtotal * config["tax_rate"]
    total = subtotal + tax
    print(f"Total: ${total:.2f}")
    return total
```

This function has three problems: it depends on a global dictionary, it performs I/O, and it mixes computation with presentation. Refactored:

```python
# Pure: all inputs are parameters, output is the return value
def calculate_total(price, quantity, tax_rate):
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

# I/O happens outside, at the boundary
total = calculate_total(19.99, 3, 0.08)
print(f"Total: ${total:.2f}")
```

The pure version is easier to test, easier to reuse with different tax rates, and easier to understand in isolation.

## Guideline 2 -- Use Return Values Instead of Mutation

When a function needs to produce a result, prefer returning a new value over modifying an argument in place. This makes the data flow visible at the call site.

```python
# Mutation: caller must know that the list is modified
def add_tax(prices, rate):
    for i in range(len(prices)):
        prices[i] *= (1 + rate)

# Return: caller sees the new value explicitly
def add_tax(prices, rate):
    return [p * (1 + rate) for p in prices]
```

With the return-based version, the call site makes the data flow obvious:

```python
original_prices = [10.0, 20.0, 30.0]
taxed_prices = add_tax(original_prices, 0.08)
```

You can see that `original_prices` goes in and `taxed_prices` comes out. With the mutation-based version, the call `add_tax(original_prices, 0.08)` gives no visual indication that `original_prices` has changed.

There are legitimate cases where mutation is appropriate---for example, when working with very large data structures where copying would be prohibitively expensive. But for most everyday code, returning new values is clearer.

## Guideline 3 -- Isolate Side Effects at Boundaries

The functional core / imperative shell pattern organizes code into two layers:

- **Functional core**: pure functions that contain all the business logic, data transformations, and decisions. No I/O, no mutation of shared state.
- **Imperative shell**: a thin outer layer that handles I/O (reading files, printing output, database queries) and calls into the functional core.

```python
# --- Functional core (pure) ---

def parse_scores(raw_lines):
    scores = []
    for line in raw_lines:
        name, value = line.strip().split(",")
        scores.append((name, int(value)))
    return scores

def compute_statistics(scores):
    values = [s for _, s in scores]
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values),
    }

def format_report(stats):
    lines = [
        f"Students: {stats['count']}",
        f"Average:  {stats['mean']:.1f}",
        f"Highest:  {stats['highest']}",
        f"Lowest:   {stats['lowest']}",
    ]
    return "\n".join(lines)

# --- Imperative shell (side effects) ---

def main():
    with open("scores.csv") as f:
        raw_lines = f.readlines()

    scores = parse_scores(raw_lines)
    stats = compute_statistics(scores)
    report = format_report(stats)

    print(report)
    with open("report.txt", "w") as f:
        f.write(report)

if __name__ == "__main__":
    main()
```

Notice how the three core functions are completely pure. They take data in and return data out. All file reading and writing happens in `main()`. This means:

- `parse_scores`, `compute_statistics`, and `format_report` can each be tested with simple assertions, no files needed.
- The I/O logic in `main()` is straightforward and easy to review.
- If the data source changes (say, from a file to a database), only `main()` needs to change. The core logic is untouched.

## Guideline 4 -- Document Side Effects Explicitly

When a function must have side effects, document them clearly. Python's convention is to describe side effects in the docstring.

```python
def save_results(filepath, results):
    """Write results to a JSON file.

    Side effects:
        Creates or overwrites the file at `filepath`.

    Args:
        filepath: Path to the output file.
        results: Dictionary of results to save.
    """
    import json
    with open(filepath, "w") as f:
        json.dump(results, f, indent=2)
```

This is especially important for functions that mutate their arguments:

```python
def shuffle_in_place(items):
    """Randomly reorder elements of `items` in place.

    Side effects:
        Modifies `items` directly. The original order is lost.

    Args:
        items: A mutable sequence to shuffle.

    Returns:
        None
    """
    import random
    random.shuffle(items)
```

When a function returns `None`, that is often a signal that its purpose is a side effect. Python's standard library follows this convention: `list.sort()` returns `None` because its purpose is mutation, while `sorted()` returns a new list because it is pure.

## Guideline 5 -- Separate Computation from I/O

A common mistake is to interleave computation and I/O within a single function. This makes the function impossible to test without performing real I/O.

```python
# Interleaved: computation and I/O are tangled
def process_file(filename):
    with open(filename) as f:
        total = 0
        for line in f:
            value = float(line.strip())
            if value > 0:
                total += value
    print(f"Sum of positives: {total}")
    return total
```

Separated:

```python
# Pure computation
def sum_positives(values):
    return sum(v for v in values if v > 0)

# I/O at the boundary
def process_file(filename):
    with open(filename) as f:
        values = [float(line.strip()) for line in f]
    total = sum_positives(values)
    print(f"Sum of positives: {total}")
    return total
```

Now `sum_positives` can be tested without any file:

```python
assert sum_positives([3, -1, 4, -5, 2]) == 9
assert sum_positives([]) == 0
assert sum_positives([-1, -2]) == 0
```

## Putting It All Together

The guidelines form a coherent strategy:

1. **Default to pure.** Start by writing pure functions. Only add side effects when they are genuinely required.
2. **Return, do not mutate.** Prefer creating new values over changing existing ones.
3. **Push I/O to the edges.** Keep the core logic free of file operations, printing, and user input.
4. **Document what is impure.** When side effects are necessary, make them visible in the docstring.
5. **Separate computation from I/O.** If a function is doing both, split it into two functions.

Following these guidelines does not require adopting a functional programming paradigm wholesale. It simply means being intentional about where state changes and I/O happen, so that the majority of your code remains easy to understand, test, and reuse.

---

## Exercises

**Exercise 1.**
The following function violates several of the guidelines above. Identify each violation and refactor the function into a functional core / imperative shell structure.

```python
log = []

def analyze_temperatures(filename):
    global log
    with open(filename) as f:
        temps = [float(line.strip()) for line in f]
    avg = sum(temps) / len(temps)
    hot_days = [t for t in temps if t > avg]
    log.append(f"Analyzed {filename}: avg={avg:.1f}, hot_days={len(hot_days)}")
    print(f"Average: {avg:.1f}")
    print(f"Days above average: {len(hot_days)}")
    return avg, hot_days
```

??? success "Solution to Exercise 1"
    Violations:

    1. **Reads from a file** (I/O mixed with computation).
    2. **Modifies a global list** (`log.append(...)` is a side effect on global state).
    3. **Prints inside the function** (I/O mixed with computation).
    4. The function does three jobs: reads data, computes statistics, and reports results.

    Refactored into functional core / imperative shell:

    ```python
    # --- Functional core (pure) ---

    def compute_temperature_stats(temps):
        avg = sum(temps) / len(temps)
        hot_days = [t for t in temps if t > avg]
        return avg, hot_days

    def format_temperature_report(avg, hot_days):
        return (
            f"Average: {avg:.1f}\n"
            f"Days above average: {len(hot_days)}"
        )

    # --- Imperative shell ---

    def analyze_temperatures(filename, log):
        with open(filename) as f:
            temps = [float(line.strip()) for line in f]

        avg, hot_days = compute_temperature_stats(temps)
        report = format_temperature_report(avg, hot_days)

        log.append(f"Analyzed {filename}: avg={avg:.1f}, hot_days={len(hot_days)}")
        print(report)

        return avg, hot_days
    ```

    Now `compute_temperature_stats` and `format_temperature_report` are pure and testable without files or global state. The shell function `analyze_temperatures` handles all I/O and receives `log` as an explicit parameter instead of using a global.

---

**Exercise 2.**
A colleague writes a data pipeline where every function mutates a shared dictionary:

```python
def load_data(context):
    context["data"] = [1, 2, 3, 4, 5]

def filter_data(context):
    context["data"] = [x for x in context["data"] if x > 2]

def summarize(context):
    context["summary"] = sum(context["data"])

def run_pipeline():
    context = {}
    load_data(context)
    filter_data(context)
    summarize(context)
    print(context["summary"])

run_pipeline()
```

Rewrite this pipeline using pure functions that pass data through return values. Keep the `print` call only in `run_pipeline`.

??? success "Solution to Exercise 2"
    ```python
    def load_data():
        return [1, 2, 3, 4, 5]

    def filter_data(data):
        return [x for x in data if x > 2]

    def summarize(data):
        return sum(data)

    def run_pipeline():
        data = load_data()
        filtered = filter_data(data)
        total = summarize(filtered)
        print(total)

    run_pipeline()
    ```

    Output:

    ```text
    12
    ```

    Each function now takes explicit input and returns explicit output. There is no shared mutable dictionary. The data flow is visible in `run_pipeline`: `load_data` produces data, `filter_data` transforms it, `summarize` reduces it to a single value. If any step fails, you know exactly where to look because each step is independent.

---

**Exercise 3.**
You are building a small application that reads a list of student names from a file, removes duplicates, sorts the names alphabetically, and writes the result to a new file. Design the solution using the functional core / imperative shell pattern. Write out the complete code with at least two pure functions and one shell function.

??? success "Solution to Exercise 3"
    ```python
    # --- Functional core (pure) ---

    def remove_duplicates(names):
        """Return a list of unique names, preserving first occurrence order."""
        seen = set()
        result = []
        for name in names:
            if name not in seen:
                seen.add(name)
                result.append(name)
        return result

    def sort_names(names):
        """Return a new list of names sorted alphabetically (case-insensitive)."""
        return sorted(names, key=str.lower)

    # --- Imperative shell ---

    def process_student_file(input_path, output_path):
        """Read names, deduplicate, sort, and write to output file.

        Side effects:
            Reads from input_path.
            Creates or overwrites output_path.
            Prints a summary to stdout.
        """
        with open(input_path) as f:
            raw_names = [line.strip() for line in f if line.strip()]

        unique_names = remove_duplicates(raw_names)
        sorted_names = sort_names(unique_names)

        with open(output_path, "w") as f:
            for name in sorted_names:
                f.write(name + "\n")

        print(f"Wrote {len(sorted_names)} unique names to {output_path}")

    if __name__ == "__main__":
        process_student_file("students.txt", "students_sorted.txt")
    ```

    The two pure functions (`remove_duplicates` and `sort_names`) can be tested without any files:

    ```python
    assert remove_duplicates(["Alice", "Bob", "Alice"]) == ["Alice", "Bob"]
    assert sort_names(["Charlie", "alice", "Bob"]) == ["alice", "Bob", "Charlie"]
    ```

    All I/O is confined to `process_student_file`, making the core logic reusable and independently verifiable.
