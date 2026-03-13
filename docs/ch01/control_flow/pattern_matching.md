

# Pattern Matching

Python 3.10 introduced **structural pattern matching** using the `match` statement.

Pattern matching allows programs to dispatch behavior based on the **structure of data**.

---

## Basic Syntax

```python
match value:

    case pattern:
        action
````

---

## Example

```python
def http_status(code):

    match code:

        case 200:
            return "OK"

        case 404:
            return "Not Found"

        case _:
            return "Unknown"
```

The underscore `_` acts as a wildcard.

---

## Multiple Patterns

```python
match day:

    case "Saturday" | "Sunday":
        print("Weekend")

    case _:
        print("Weekday")
```

---

## Guards

Guards allow conditional checks.

```python
match number:

    case int(x) if x > 0:
        print("positive")

    case int(x) if x < 0:
        print("negative")
```

Pattern matching provides a more expressive alternative to long `if-elif` chains.

