# Essential Built-ins

Python provides a set of **built-in functions** that operate directly on values, collections, and programs.

These functions are not random utilities---they form a small, powerful set of **primitive operations** that appear throughout almost all Python code.

---

## Mental Model

Built-in functions can be understood by the role they play in computation. Many return *lazy* objects---values produced on demand instead of being stored all at once in memory. This concept applies to `range`, `map`, `filter`, `zip`, and `reversed`.

1. **Values** --- transforming individual data
2. **Collections** --- measuring, ordering, or accessing groups of data
3. **Iteration** --- defining and restructuring how programs loop
4. **Selection** --- choosing elements based on conditions (e.g., `filter`, comprehensions)
5. **Aggregation** --- reducing collections to a single result
6. **Interaction** --- communicating with the outside world
7. **Introspection** --- inspecting objects and the runtime environment

---

## Categories of Built-ins

| Category | Purpose | Examples | Covered in |
|---|---|---|---|
| Value operations | transform individual values | `abs`, `round`, type conversions | [abs / round](abs_round.md), [Type Conversions](type_conversion_functions.md) |
| Collection operations | work on groups of data | `len`, `sorted`, `reversed` | [len / range](len_range.md), [sorted / reversed](sorted_reversed.md) |
| Iteration tools | define or reshape iteration | `range`, `enumerate`, `zip`, `map`, `filter` | [enumerate / zip](enumerate_zip.md), [map / filter](map_filter.md) |
| Aggregation | reduce data to a single value | `sum`, `min`, `max`, `any`, `all` | [min / max / sum](min_max_sum.md), [any / all](any_all.md) |
| Interaction | input/output with environment | `print`, `input` | [print / input](print_input.md), [I/O Functions](io_functions.md) |
| Introspection | inspect objects and environment | `help`, `dir` | [help / dir](help_dir.md) |

---

## Quick Examples

Each category in action:

```python
# Value operation
abs(-7)             # 7

# Collection operation
len([10, 20, 30])   # 3

# Iteration tool
list(enumerate(["a", "b"]))   # [(0, 'a'), (1, 'b')]

# Aggregation
sum([1, 2, 3, 4])  # 10

# Interaction
print("hello")     # hello

# Introspection
dir([])             # list of list methods
```

---

## Design Principle

Well-written Python code uses built-ins to express intent clearly:

- use `sum()` instead of manual loops
- use `any()` / `all()` for logical checks
- use `zip()` to combine sequences
- use `enumerate()` instead of tracking indices manually

This leads to code that is shorter, clearer, and less error-prone.

---

## Key Insight

Built-ins are the **building blocks of everyday Python code**.

- Control flow defines how execution proceeds
- Data types define how data is structured
- Functions define how behavior is organized
- **Built-ins define the core operations applied to data**
- Functions compose these operations into reusable behavior

Built-ins are functions that either **return values** (pure transformations like `abs`, `sorted`, `sum`) or **produce side effects** (interaction like `print`, `input`). Understanding them is not about memorizing functions, but about recognizing **what kind of operation your problem requires** and selecting the appropriate tool.

---

## Practical Example

```python
# Combining built-ins: analyze student scores
scores = [55, 70, 85, 40, 90]

passing = [s for s in scores if s >= 60]
average = sum(scores) / len(scores)

print(f"Passing: {passing}")     # [70, 85, 90]
print(f"Average: {average:.1f}") # 68.0
```

## Exercises

**Exercise 1.** Summarize the key concepts introduced in this overview in your own words. Identify which concept you find most important and explain why.

??? success "Solution to Exercise 1"
    Answers will vary. A strong response should demonstrate understanding of the main ideas and articulate a clear reason for prioritizing one concept, connecting it to practical programming tasks.

---

**Exercise 2.** For each concept introduced in this overview, write a short code snippet (2-5 lines) that demonstrates it in action.

??? success "Solution to Exercise 2"
    Answers will vary based on the specific overview content. Each snippet should be self-contained and clearly illustrate the concept it targets.

