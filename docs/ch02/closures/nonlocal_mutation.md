# nonlocal and Mutation

클로저에서 외부 변수를 수정하는 방법입니다.

## Rebinding vs Mutation

### The Core Difference

```python
def outer():
    x = [1, 2, 3]
    
    def rebind():
        x = [4, 5, 6]  # Creates NEW local variable!
    
    def mutate():
        x.append(4)  # Modifies SAME object
    
    rebind()
    print(x)  # [1, 2, 3] — unchanged
    
    mutate()
    print(x)  # [1, 2, 3, 4] — modified

outer()
```

| Operation | What Happens | Works Without nonlocal? |
|-----------|--------------|------------------------|
| `x = value` | Creates new binding | ❌ No |
| `x.method()` | Mutates existing object | ✅ Yes |
| `x[i] = v` | Mutates existing object | ✅ Yes |

### Why?

- **Assignment** (`=`) creates a new local variable
- **Method calls** operate on the looked-up object

---

## The nonlocal Keyword

`nonlocal`은 내부 함수가 외부 변수를 **재바인딩**할 수 있게 합니다:

```python
def outer():
    count = 0
    
    def increment():
        nonlocal count  # Required for rebinding
        count += 1
        return count
    
    return increment

counter = increment()
print(counter())  # 1
print(counter())  # 2
```

### Without nonlocal — Error

```python
def outer():
    count = 0
    
    def increment():
        count += 1  # UnboundLocalError!
        return count
    
    return increment
```

`count += 1`은 `count = count + 1`이므로, assignment가 `count`를 로컬로 만들어버립니다.

---

## nonlocal Resolution

`nonlocal`은 가장 가까운 enclosing scope의 변수를 찾습니다:

```python
def level1():
    x = 1
    
    def level2():
        x = 2
        
        def level3():
            nonlocal x  # Modifies level2's x (closest)
            x = 3
        
        level3()
        print(f"level2: {x}")  # 3
    
    level2()
    print(f"level1: {x}")  # 1 (unchanged)

level1()
```

---

## Augmented Assignment Operators

### With Mutable Objects (Works)

```python
def outer():
    items = [1, 2, 3]
    
    def extend():
        items += [4, 5]  # Calls __iadd__, mutates in place
    
    extend()
    print(items)  # [1, 2, 3, 4, 5]

outer()
```

### With Immutable Objects (Fails)

```python
def outer():
    count = 0
    
    def increment():
        count += 1  # Rebinding! Error without nonlocal
    
    # increment()  # UnboundLocalError

outer()
```

---

## Cell Sharing

여러 내부 함수가 같은 cell을 공유합니다:

```python
def outer():
    x = 0
    
    def inc():
        nonlocal x
        x += 1
        return x
    
    def dec():
        nonlocal x
        x -= 1
        return x
    
    def get():
        return x
    
    return inc, dec, get

inc, dec, get = outer()

print(inc())  # 1
print(inc())  # 2
print(dec())  # 1
print(get())  # 1
```

### Verify Same Cell

```python
def outer():
    x = 10
    f1 = lambda: x
    f2 = lambda: x
    return f1, f2

a, b = outer()
print(a.__closure__[0] is b.__closure__[0])  # True — same cell
```

---

## Workarounds Without nonlocal

### Using Mutable Container

```python
def outer():
    count = [0]  # Mutable container
    
    def increment():
        count[0] += 1  # Mutation, not rebinding
        return count[0]
    
    return increment

counter = outer()
print(counter())  # 1
print(counter())  # 2
```

### Using Object Attribute

```python
def outer():
    class State:
        count = 0
    
    def increment():
        State.count += 1
        return State.count
    
    return increment
```

### Using Function Attribute

```python
def counter():
    def inner():
        inner.count += 1
        return inner.count
    inner.count = 0
    return inner

c = counter()
print(c())  # 1
print(c())  # 2
```

---

## Best Practices

### When to Use nonlocal

✅ Simple state management in closures:

```python
def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
```

### When to Avoid nonlocal

❌ Complex state → Use a class instead:

```python
# Instead of multiple nonlocal variables
class Counter:
    def __init__(self, start=0):
        self.count = start
    
    def increment(self):
        self.count += 1
        return self.count
```

---

## Summary

| Concept | Description |
|---------|-------------|
| Rebinding | `x = value` creates new variable; needs `nonlocal` |
| Mutation | `x.method()` modifies object; works without `nonlocal` |
| `nonlocal` | Allows rebinding of enclosing scope variable |
| Cell sharing | Multiple closures from same function share cells |
| Workaround | Use mutable container `[value]` if avoiding `nonlocal` |
