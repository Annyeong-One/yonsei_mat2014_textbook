# and/or Return Values


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The and and or operators don't return boolean values—they return one of their operands. This behavior is powerful for default value patterns and conditional value selection, but differs from other languages' boolean operators.

---

## and Return Values

### Returns First Falsy or Last Value

```python
print(5 and 10)
print(0 and 10)
print(False and 20)
```

Output:
```
10
0
False
```

### Understanding the Pattern

```python
# Returns first falsy operand
print([] and "value")
print("" and "value")

# Returns last operand if all truthy
print("a" and "b" and "c")
```

Output:
```
[]

c
```

## or Return Values

### Returns First Truthy or Last Value

```python
print(5 or 10)
print(0 or 10)
print(False or None or "default")
```

Output:
```
5
10
default
```

### Default Value Pattern

```python
config = {"port": None}
port = config["port"] or 8000
print(f"Port: {port}")

config["port"] = 5000
port = config["port"] or 8000
print(f"Port: {port}")
```

Output:
```
Port: 8000
Port: 5000
```

## Practical Applications

### Chained Defaults

```python
user_preference = None
system_setting = None
fallback = "light"

theme = user_preference or system_setting or fallback
print(f"Theme: {theme}")
```

Output:
```
Theme: light
```

### Value Selection

```python
scores = [85, 92, 78, 88]
passing_scores = [s for s in scores if s >= 80]

best = passing_scores and max(passing_scores) or 0
print(f"Best passing score: {best}")
```

Output:
```
Best passing score: 92
```

### Configuration Resolution

```python
def get_config(env_var, config_dict, default):
    return env_var or config_dict.get("setting") or default

result1 = get_config(None, {}, "fallback")
result2 = get_config("custom", {}, "fallback")

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
```

Output:
```
Result 1: fallback
Result 2: custom
```

## Edge Cases

### Empty Collections Are Falsy

```python
items = []
result = items or ["default"]
print(result)

items = [1, 2, 3]
result = items or ["default"]
print(result)
```

Output:
```
['default']
[1, 2, 3]
```
