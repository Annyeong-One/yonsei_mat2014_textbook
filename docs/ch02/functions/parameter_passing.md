# Parameter Passing

This document provides practical guidance on how arguments flow from caller to function in Python, building on the concepts from call-by-object-reference.


## The Assignment Model

When you call a function, Python performs implicit assignments:

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")
```

This call is equivalent to:

```python
# Implicit assignments when function is called
name = "Alice"
greeting = "Hello"
# Then execute function body
print(f"{greeting}, {name}!")
```

Parameters are local variables that get assigned the argument values.


## Passing Immutable Objects

When you pass immutable objects (int, str, tuple, frozenset), the function receives a reference to the same object but cannot modify it.

```python
def try_modify(text):
    text = text.upper()  # Creates new string, rebinds local variable
    return text

original = "hello"
result = try_modify(original)

print(original)  # "hello" (unchanged)
print(result)    # "HELLO" (new string)
```

**Why unchanged?** `text.upper()` creates a new string. The assignment `text = ...` rebinds the local variable `text`, not the caller's `original`.


## Passing Mutable Objects

When you pass mutable objects (list, dict, set), the function can modify the original.

```python
def add_item(collection, item):
    collection.append(item)  # Modifies the original object

my_list = [1, 2, 3]
add_item(my_list, 4)

print(my_list)  # [1, 2, 3, 4] (modified!)
```

**Why modified?** `collection` and `my_list` reference the same list object. `append()` mutates that object.


## Common Patterns

### Pattern 1: Modify and Return

Functions that modify in-place often also return the object for convenience:

```python
def append_and_sort(lst, item):
    lst.append(item)
    lst.sort()
    return lst  # Return for chaining, though lst is modified

data = [3, 1, 4]
result = append_and_sort(data, 2)

print(data)    # [1, 2, 3, 4]
print(result)  # [1, 2, 3, 4]
print(data is result)  # True (same object)
```


### Pattern 2: Create and Return (Non-Mutating)

Functions that shouldn't modify the input create copies:

```python
def sorted_with_item(lst, item):
    new_list = lst.copy()  # Work on a copy
    new_list.append(item)
    new_list.sort()
    return new_list

data = [3, 1, 4]
result = sorted_with_item(data, 2)

print(data)    # [3, 1, 4] (unchanged)
print(result)  # [1, 2, 3, 4]
```


### Pattern 3: Optional Output Parameter

Allow caller to provide a container, or create one:

```python
def get_even_numbers(numbers, output=None):
    if output is None:
        output = []
    for n in numbers:
        if n % 2 == 0:
            output.append(n)
    return output

# Create new list
result = get_even_numbers([1, 2, 3, 4, 5])
print(result)  # [2, 4]

# Append to existing list
existing = [0]
get_even_numbers([1, 2, 3, 4, 5], existing)
print(existing)  # [0, 2, 4]
```


## Swapping Values

A classic example showing that assignment doesn't affect the caller:

```python
def swap(a, b):
    a, b = b, a  # Only swaps local variables
    return a, b

x, y = 1, 2
swap(x, y)
print(x, y)  # 1, 2 (unchanged!)

# To actually swap, reassign from return value
x, y = swap(x, y)
print(x, y)  # 2, 1
```


## Passing Different Types

### Strings (Immutable)

```python
def process(s):
    s += " world"  # Creates new string
    return s

text = "hello"
result = process(text)
print(text)    # "hello"
print(result)  # "hello world"
```

### Lists (Mutable)

```python
def process(lst):
    lst += [4, 5]  # Mutates in place (list.__iadd__)
    return lst

data = [1, 2, 3]
result = process(data)
print(data)    # [1, 2, 3, 4, 5] (modified!)
print(result)  # [1, 2, 3, 4, 5]
```

**Note**: `+=` behaves differently for lists vs strings!


### Dictionaries (Mutable)

```python
def add_defaults(config):
    config.setdefault('timeout', 30)
    config.setdefault('retries', 3)

settings = {'timeout': 60}
add_defaults(settings)
print(settings)  # {'timeout': 60, 'retries': 3}
```


## Nested Structures

With nested structures, the rules apply at each level:

```python
def modify_nested(data):
    data['users'].append('Charlie')  # Modifies nested list
    data['count'] = 100              # Modifies dict

info = {
    'users': ['Alice', 'Bob'],
    'count': 2
}

modify_nested(info)
print(info)  # {'users': ['Alice', 'Bob', 'Charlie'], 'count': 100}
```


## Defensive Copying

When you don't want modifications to propagate:

### Shallow Copy

```python
def process(data):
    data = data.copy()  # Shallow copy
    data.append(100)
    return data

original = [1, 2, 3]
result = process(original)
print(original)  # [1, 2, 3] (protected)
```

### Deep Copy (for nested structures)

```python
import copy

def process(data):
    data = copy.deepcopy(data)  # Deep copy
    data['items'].append(100)
    return data

original = {'items': [1, 2, 3]}
result = process(original)
print(original)  # {'items': [1, 2, 3]} (protected)
```


## Function Signatures and Intent

Use type hints and docstrings to communicate intent:

```python
from typing import List

def sort_in_place(items: List[int]) -> None:
    """Sort the list in place. Modifies the original."""
    items.sort()

def sorted_copy(items: List[int]) -> List[int]:
    """Return a sorted copy. Original unchanged."""
    return sorted(items)
```


## Common Mistakes

### Mistake 1: Expecting immutable modification

```python
def increment(n):
    n += 1  # Creates new int, doesn't affect caller

x = 5
increment(x)
print(x)  # 5 (unchanged)

# Fix: return and reassign
def increment(n):
    return n + 1

x = increment(x)  # x = 6
```

### Mistake 2: Unintended mutation

```python
def calculate_stats(numbers):
    numbers.sort()  # Accidentally modifies input!
    return numbers[0], numbers[-1]

data = [3, 1, 4, 1, 5]
min_val, max_val = calculate_stats(data)
print(data)  # [1, 1, 3, 4, 5] (sorted, not original order!)

# Fix: work on a copy
def calculate_stats(numbers):
    sorted_nums = sorted(numbers)  # Creates new list
    return sorted_nums[0], sorted_nums[-1]
```

### Mistake 3: Aliasing confusion

```python
def process(a, b):
    a.append(1)
    b.append(2)

x = [0]
process(x, x)  # Both parameters reference same list!
print(x)  # [0, 1, 2]
```


## Summary Table

| Argument Type | Can Function Modify Original? | How to Prevent Modification |
|---------------|-------------------------------|----------------------------|
| `int`, `float`, `bool` | No (immutable) | N/A |
| `str` | No (immutable) | N/A |
| `tuple`, `frozenset` | No (immutable) | N/A |
| `list` | Yes | Pass `lst.copy()` or `lst[:]` |
| `dict` | Yes | Pass `dict.copy()` or `{**d}` |
| `set` | Yes | Pass `set.copy()` |
| Nested structures | Yes | Pass `copy.deepcopy(obj)` |


## Best Practices

1. **Document mutation** - Make it clear if a function modifies its arguments
2. **Prefer returning new values** - Easier to reason about
3. **Copy if unsure** - When in doubt, copy the input
4. **Use type hints** - `-> None` suggests in-place modification
5. **Name functions clearly** - `sort_in_place()` vs `sorted_copy()`
