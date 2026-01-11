# Exercises

## Exercise 1: Counter

Implement a counter using closures:

```python
def make_counter():
    # Your code here
    pass

inc, dec, get = make_counter()
assert inc() == 1
assert inc() == 2
assert dec() == 1
assert get() == 1
```

## Exercise 2: Memoization

Create a memoization decorator:

```python
def memoize(func):
    # Your code here
    pass

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Should be fast
fibonacci(100)
```

## Exercise 3: Registry

Implement a plugin registry:

```python
def create_registry():
    # Your code here
    pass

registry = create_registry()

@registry.register('csv')
def process_csv(data):
    pass

handler = registry.get('csv')
```

## Exercise 4: Fix Bugs

Fix these bugs:

```python
# Bug 1
def append(item, lst=[]):
    lst.append(item)
    return lst

# Bug 2
funcs = []
for i in range(3):
    funcs.append(lambda: i)

# Bug 3
def outer():
    count = 0
    def inc():
        count += 1
        return count
    return inc
```

## Summary

Practice:
- Closures
- Decorators
- Registries
- Bug fixes
