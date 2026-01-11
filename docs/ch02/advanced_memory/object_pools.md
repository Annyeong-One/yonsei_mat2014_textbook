# Object Pools

## Concept

### 1. Reuse Objects

```python
class ObjectPool:
    def __init__(self, cls, size=10):
        self.cls = cls
        self.pool = [cls() for _ in range(size)]
        self.available = list(self.pool)
    
    def acquire(self):
        if self.available:
            return self.available.pop()
        return self.cls()
    
    def release(self, obj):
        self.available.append(obj)
```

### 2. Usage

```python
pool = ObjectPool(ExpensiveObject)

obj = pool.acquire()
try:
    use(obj)
finally:
    pool.release(obj)
```

## Benefits

### 1. Reduce Allocations

```python
# Without pool: many allocations
for i in range(1000):
    obj = ExpensiveObject()
    use(obj)

# With pool: reuse objects
for i in range(1000):
    obj = pool.acquire()
    use(obj)
    pool.release(obj)
```

## Summary

- Reuse expensive objects
- Reduce allocations
- Better performance
- Manual management
