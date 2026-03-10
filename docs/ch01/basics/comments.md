# Comments

Comments are annotations in source code that the Python interpreter ignores. Writing effective comments is a core skill because code is read far more often than it is written.

## Definition

A **comment** is text in a Python source file that is ignored during execution. Single-line comments start with `#`. **Docstrings** are triple-quoted strings placed immediately after a function, class, or module definition that serve as documentation accessible at runtime via `__doc__`.

## Explanation

Python has no multi-line comment syntax like C's `/* */`. For multi-line comments, use consecutive `#` lines. Triple-quoted strings can serve as comments if unassigned, but they are technically string literals -- prefer `#` for true comments.

The most important rule: **comment why, not what**. Code already says what it does. Comments should explain intent, constraints, workarounds, or non-obvious design decisions. Stale comments that contradict the code are worse than no comments.

Standard markers help teams track work: `TODO`, `FIXME`, `HACK`, `NOTE`.

## Examples

```python
# Good: explains WHY, not what
x = 5  # server requires minimum timeout of 5 seconds

# Bad: restates the obvious
x = x + 1  # increment x by 1
```

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length: The length in meters.
        width: The width in meters.

    Returns:
        The area as a float.
    """
    return length * width

# Docstrings are accessible at runtime
print(calculate_area.__doc__)
help(calculate_area)
```

```python
# TODO: Optimize for large datasets
# FIXME: Handle edge case when list is empty
# HACK: Workaround for bug in library v2.3 (see issue #123)
result = data.copy()
```
