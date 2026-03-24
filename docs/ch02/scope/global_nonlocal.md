
# Global and Nonlocal

By default, assignment inside a function creates a local variable. The `global` and `nonlocal` keywords let a function explicitly modify a variable defined in an outer scope — `global` targets the module-level scope, while `nonlocal` targets the nearest enclosing function scope.

## global Keyword

### Modifying a Global Variable

```python
x = 10

def function():
    global x
    x = 20

function()
print(x)  # 20
```

## nonlocal Keyword

### Modifying an Enclosing Variable

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)  # 20
```

## Summary

- `global`: modifies a variable at module level
- `nonlocal`: modifies a variable in the enclosing function scope
- Both allow a function to modify variables defined in an outer scope
