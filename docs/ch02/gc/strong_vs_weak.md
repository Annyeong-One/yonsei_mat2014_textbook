# Strong vs Weak

## Strong References

### 1. Normal References

```python
x = [1, 2, 3]
y = x
# Strong refs prevent GC
```

## Weak References

### 1. Allow GC

```python
import weakref

obj = [1, 2, 3]
weak = weakref.ref(obj)

del obj
# Can be collected
```

## Summary

- Strong: prevent GC
- Weak: allow GC
- Choose based on need
