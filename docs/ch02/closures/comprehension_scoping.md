# Comprehension Scoping

## List Comprehension Scope

### 1. Own Namespace

```python
x = "outer"
result = [x for x in range(3)]

print(x)  # "outer" (unchanged)
print(result)  # [0, 1, 2]
```

## Dict/Set Comprehensions

### 1. Same Behavior

```python
x = 10
d = {x: x**2 for x in range(3)}

print(x)  # 10 (unchanged)
print(d)  # {0: 0, 1: 1, 2: 4}
```

## Summary

- Comprehensions have own scope (Python 3+)
- Loop variable doesn't leak
- Prevents name pollution
