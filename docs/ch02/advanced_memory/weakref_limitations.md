# Weakref Limitations

## Cannot Weakref

### 1. Some Types

```python
import weakref

# Cannot weakref
# x = 42
# ref = weakref.ref(x)  # TypeError

# Can weakref
obj = [1, 2, 3]
ref = weakref.ref(obj)  # OK
```

## Types Supporting Weakref

- list, dict, set
- User-defined classes
- Most objects

## Types Not Supporting

- int, str, tuple
- None, True, False

## Summary

- Not all types supported
- Most user objects OK
- Built-in primitives no
