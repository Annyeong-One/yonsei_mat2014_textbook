# Bytecode Analysis

## Inspect Bytecode

### 1. Using dis

```python
import dis

def outer():
    x = 10
    def inner():
        return x
    return inner

dis.dis(outer)
```

## Closure Instructions

### 1. LOAD_DEREF

```python
# Inner function uses LOAD_DEREF
# To load from cell
```

## Summary

- Use dis module
- LOAD_DEREF for closures
- Inspect bytecode for understanding
