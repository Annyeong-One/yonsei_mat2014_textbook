# Weakref Best Practices

## Check Before Access

### 1. Always Check

```python
ref = weakref.ref(obj)

# Always check
target = ref()
if target is not None:
    use(target)
```

## Callbacks

### 1. Cleanup Callback

```python
def cleanup(ref):
    print("Object collected")

ref = weakref.ref(obj, cleanup)
```

## Summary

- Always check ref()
- Use callbacks for cleanup
- Document weak ref usage
