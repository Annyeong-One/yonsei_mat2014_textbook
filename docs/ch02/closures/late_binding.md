# Late Binding

클로저에서 가장 흔한 실수: 변수는 **호출 시점**에 조회됩니다.

## The Problem

### Classic Loop Bug

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

print([f() for f in funcs])  # [2, 2, 2] — NOT [0, 1, 2]!
```

**왜?** 모든 람다가 같은 변수 `i`를 참조하고, 호출 시점에 `i`는 2입니다.

### Visualizing the Problem

```
Loop iteration 0: lambda captures reference to i (i=0)
Loop iteration 1: lambda captures reference to i (i=1)
Loop iteration 2: lambda captures reference to i (i=2)

After loop: i = 2

Call all lambdas: all look up i → all get 2
```

### List Comprehension Version

```python
# Same problem
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]
```

---

## Solutions

### 1. Default Parameter (Most Common)

값을 **정의 시점**에 캡처합니다:

```python
funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)  # x=i evaluated NOW

print([f() for f in funcs])  # [0, 1, 2] ✓
```

```python
# List comprehension version
funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2] ✓
```

### 2. Factory Function

각 반복에서 새로운 스코프를 생성합니다:

```python
def make_func(val):
    return lambda: val  # val is local to each call

funcs = [make_func(i) for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2] ✓
```

### 3. functools.partial

```python
from functools import partial

def return_val(x):
    return x

funcs = [partial(return_val, i) for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2] ✓
```

### 4. Closure Factory (Explicit)

```python
funcs = [(lambda x: lambda: x)(i) for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2] ✓
```

---

## Comparison

| Method | Pros | Cons |
|--------|------|------|
| Default parameter `x=i` | Simple, idiomatic | Changes function signature |
| Factory function | Clear intent | More verbose |
| `functools.partial` | No signature change | Import required |
| IIFE `(lambda x: ...)(i)` | Inline | Less readable |

### When to Use Each

- **Simple cases**: Default parameter `x=i`
- **Complex logic**: Factory function
- **Existing functions**: `functools.partial`

---

## Common Pitfalls

### Pitfall 1: Event Handlers

```python
# Bug
buttons = []
for i in range(3):
    btn = Button(command=lambda: print(i))
    buttons.append(btn)
# All buttons print 2

# Fix
for i in range(3):
    btn = Button(command=lambda x=i: print(x))
    buttons.append(btn)
```

### Pitfall 2: Callbacks

```python
# Bug
callbacks = {}
for name in ['a', 'b', 'c']:
    callbacks[name] = lambda: print(name)

callbacks['a']()  # Prints 'c'!

# Fix
for name in ['a', 'b', 'c']:
    callbacks[name] = lambda n=name: print(n)
```

### Pitfall 3: Threading

```python
import threading

# Bug
for i in range(3):
    threading.Thread(target=lambda: print(i)).start()
# Output unpredictable, likely all same value

# Fix
for i in range(3):
    threading.Thread(target=lambda x=i: print(x)).start()
```

---

## Memory Consideration

Default parameter는 값을 복사하지 않고 참조합니다:

```python
# Mutable object caution
data = [1, 2, 3]
f = lambda x=data: x

data.append(4)
print(f())  # [1, 2, 3, 4] — reference, not copy!

# If you need a copy:
f = lambda x=data.copy(): x
# or
f = lambda x=list(data): x
```

---

## Summary

| Issue | Cause | Solution |
|-------|-------|----------|
| All closures return same value | Late binding — variable looked up at call time | Capture value at definition time |
| Loop variable captured | Same variable `i` shared | Use `x=i` default parameter |
| Callback returns wrong value | Reference to final loop value | Factory function or partial |

**Golden Rule**: 루프에서 클로저를 만들 때는 항상 **값을 캡처**하세요.
