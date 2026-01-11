# Namespace Manipulation

## Direct Access

### 1. globals()

```python
# Add to global namespace
globals()['new_var'] = 42
print(new_var)  # 42
```

### 2. locals()

```python
def function():
    # View locals
    print(locals())
```

## Warning

### 1. Modifying locals()

```python
# Doesn't work!
def function():
    locals()['x'] = 10
    # print(x)  # NameError
```

## Summary

- Can access namespaces
- globals() modifiable
- locals() read-only
