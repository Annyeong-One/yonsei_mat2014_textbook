# Closure Fundamentals

클로저는 자신이 정의된 스코프의 변수를 캡처하는 함수입니다.

## What is a Closure?

### Definition

```python
def outer():
    x = 10  # Enclosing variable
    
    def inner():
        return x  # Captures x
    
    return inner

f = outer()
print(f())  # 10 — x is still accessible
```

`outer()`가 반환된 후에도 `inner`는 `x`에 접근할 수 있습니다. 이것이 클로저입니다.

### Key Terms

| Term | Definition |
|------|------------|
| **Closure** | Function with captured variables from enclosing scope |
| **Free Variable** | Variable used in function but defined in enclosing scope |
| **Cell** | CPython object that stores captured variable |
| **Enclosing Scope** | Parent function's local scope |

---

## Free Variables and Cells

### Free Variables

변수가 함수 내에서 사용되지만 로컬에서 정의되지 않은 경우:

```python
def outer():
    x = 10
    
    def inner():
        return x  # x is "free" in inner
    
    return inner

f = outer()
print(f.__code__.co_freevars)  # ('x',)
```

### Cell Objects

CPython은 캡처된 변수를 cell 객체에 저장합니다:

```python
def outer():
    x = 10
    
    def inner():
        return x
    
    return inner

f = outer()
print(f.__closure__)  # (<cell at 0x...>,)
print(f.__closure__[0].cell_contents)  # 10
```

---

## Cellvars vs Freevars

같은 변수가 두 가지 관점에서 보입니다:

```python
def outer():
    x = 10  # cellvar in outer
    
    def inner():
        return x  # freevar in inner
    
    return inner

# In outer: x is a cellvar (being captured)
print(outer.__code__.co_cellvars)  # ('x',)

# In inner: x is a freevar (captured from outside)
f = outer()
print(f.__code__.co_freevars)  # ('x',)
```

| Perspective | Variable Type | Meaning |
|-------------|--------------|---------|
| Enclosing function | `cellvar` | "I'm being captured" |
| Inner function | `freevar` | "I captured this" |

---

## Multi-Level Nesting

### Three-Level Example

```python
def level1():
    x = "L1"
    
    def level2():
        y = "L2"
        
        def level3():
            return x, y  # Both are free variables
        
        return level3
    
    return level2()

f = level1()
print(f())  # ('L1', 'L2')
print(f.__code__.co_freevars)  # ('x', 'y')
```

### Only Used Variables Are Captured

```python
def outer():
    x = "used"
    y = "unused"
    
    def inner():
        return x  # Only x is captured
    
    return inner

f = outer()
print(f.__code__.co_freevars)  # ('x',) — y not captured
```

### Variable Shadowing

```python
def outer():
    x = "outer"
    
    def middle():
        x = "middle"  # Shadows outer's x
        
        def inner():
            return x  # Gets nearest x
        
        return inner
    
    return middle()

f = outer()
print(f())  # 'middle'
```

Python은 **안쪽에서 바깥쪽으로** 변수를 찾습니다.

---

## Scope Chain (LEGB)

변수 조회 순서:

```
Local → Enclosing → Global → Builtin
```

```python
x = "global"

def level1():
    x = "level1"
    
    def level2():
        x = "level2"
        
        def level3():
            print(x)  # "level2" (nearest enclosing)
        
        level3()
    
    level2()

level1()
```

### Skipping Levels

```python
def outer():
    x = 10
    
    def middle():
        # No x defined here
        
        def inner():
            return x  # Skips middle, uses outer's x
        
        return inner
    
    return middle()

f = outer()
print(f())  # 10
```

---

## Closure Inspection

### Complete Inspection Example

```python
def make_counter(start=0):
    count = start
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

counter = make_counter(10)

# Inspect
print(counter.__closure__)  # (<cell ...>,)
print(counter.__code__.co_freevars)  # ('count',)

for var, cell in zip(counter.__code__.co_freevars, counter.__closure__):
    print(f"{var} = {cell.cell_contents}")
# count = 10
```

---

## Summary

| Concept | Description |
|---------|-------------|
| Closure | Function + captured environment |
| Free variable | Referenced but not locally defined |
| Cell | CPython's storage for captured variables |
| Cellvar | Variable being captured (in outer function) |
| Freevar | Captured variable (in inner function) |
| LEGB | Local → Enclosing → Global → Builtin |
