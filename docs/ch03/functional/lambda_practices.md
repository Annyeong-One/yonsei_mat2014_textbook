# Lambda Practices

## When to Use

### 1. Simple Operations

```python
# Good: simple
sorted(data, key=lambda x: x[1])

# Good: short-lived
map(lambda x: x * 2, numbers)
```

## When Not to Use

### 1. Complex Logic

```python
# Bad: too complex
process = lambda x: x * 2 if x > 0 else -x if x < 0 else 0

# Better: def
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return -x
    else:
        return 0
```

## Limitations

### 1. Single Expression

```python
# Can't do
# lambda x: x += 1  # Syntax error

# Can do
lambda x: x + 1  # Expression only
```

## Best Practices

### 1. Keep Simple

```python
# Good
sorted(users, key=lambda u: u.name)

# Bad (use def)
lambda x: do_complex_thing(x, with_many_params)
```

## Summary

- Simple operations only
- Avoid complex logic
- Single expression
- Consider def for clarity
