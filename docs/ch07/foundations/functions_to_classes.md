# Functions to Classes

Understanding the evolution from functions → closures → classes reveals Python's design philosophy.

---

## The Evolution

$$\begin{array}{ccccccccccccccc}
\text{Function}&\Rightarrow&\text{Closure}&\Rightarrow&\text{Class}\\
&&\uparrow&&\uparrow&\\
&&\text{Free Variables}&&\text{Attributes}\\
&&&&\text{Methods}\\
\end{array}$$

---

## Functions

### 1. First-Class Objects

Functions can be assigned, passed, and returned.

```python
def square(x):
    return x * x

f = square
print(f(4))  # 16
```

### 2. Stateless

Functions don't retain state between calls.

```python
def add_ten(x):
    return x + 10

result = add_ten(5)  # 15
# No memory of previous calls
```

### 3. Limitations

Cannot encapsulate data with behavior.

---

## Closures

### 1. Capturing Variables

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor  # factor is captured
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### 2. Free Variables

`factor` is a **free variable** in `multiply`:
- Used inside the function
- Not defined locally
- Captured from enclosing scope

### 3. State Retention

```python
times3 = make_multiplier(3)
del make_multiplier  # Can delete outer function

print(times3(10))  # 30 - still works!
```

---

## Free Variables

### 1. Definition

A variable that is:
- Referenced in a function
- Not bound (defined) in that function
- Comes from an enclosing scope

### 2. Example

```python
x = 10  # global

def my_function(y):
    return x + y  # x is FREE, y is BOUND
```

### 3. Where They Live

Free variables are stored in **cell objects** attached to the function via `__closure__` — not in `__dict__` or `__globals__`. This is how closures retain state after the enclosing function returns.

```python
def outer(x):
    def inner(y):
        return x + y  # x is FREE in inner
    return inner

f = outer(10)
print(f.__code__.co_freevars)          # ('x',)
print(f.__closure__[0].cell_contents)  # 10
```

??? note "Function Object Structure"

    `__code__` stores names; runtime structures hold values.

    ```text
    function object (static)
    ├── __code__
    │   ├── co_varnames   → local variable names
    │   ├── co_freevars   → enclosing variable names
    │   └── co_names      → global variable names
    ├── __globals__       → global namespace (name → value)
    └── __closure__       → enclosing values (cell objects)

    execution frame (dynamic, per call)
    └── locals            → local variable values
    ```

    This maps directly to LEGB lookup:

    - **L** ocals → names in `co_varnames`, values in frame
    - **E** nclosing → names in `co_freevars`, values in `__closure__`
    - **G** lobals → names in `co_names`, values in `__globals__`
    - **B** uiltins → fallback from `__globals__["__builtins__"]`

---

## From Closure to Class

### 1. Closure Version

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

times3 = make_multiplier(3)
print(times3(10))  # 30
```

### 2. Class Version

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # attribute instead of free variable
    
    def multiply(self, x):
        return x * self.factor
    
    def __call__(self, x):
        return self.multiply(x)

times3 = Multiplier(3)
print(times3(10))  # 30
```

### 3. Key Differences

- Closure: captures free variables
- Class: stores attributes explicitly

!!! tip "Key Insight"
    A class is a named, reusable closure with multiple behaviors. Closures store state in hidden cell objects (`__closure__`), while classes store state explicitly in instance attributes (`__dict__`). This is the fundamental difference: implicit vs explicit state.

---

## Class Advantages

### 1. Multiple Methods

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
    
    def decrement(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
```

### 2. Named State

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width   # explicit names
        self.height = height
```

### 3. Special Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
```

---

## Closure Limitations

### 1. Single Function

Closures typically return one function.

### 2. Implicit State

State is captured implicitly through free variables.

### 3. Hidden Introspection

Closure state can be inspected via `__closure__`, but it is obscure compared to class attributes.

```python
times3 = make_multiplier(3)
print(times3.__closure__[0].cell_contents)  # 3 — accessible but buried
print(vars(Multiplier(3)))                  # {'factor': 3} — explicit
```

---

??? note "Advanced: Class After Deletion"

    Instances survive even if the class itself is deleted — but class-level
    features become inaccessible.

    ```python
    class Multiplier:
        class_var = "I exist"

        def __init__(self, factor):
            self.factor = factor

    times3 = Multiplier(3)
    del Multiplier  # Delete class

    print(times3.factor)     # ✅ Works: 3
    print(times3.class_var)  # ❌ AttributeError
    # new_obj = Multiplier(5)  # ❌ NameError
    ```

    This is an implementation detail of Python's reference model, not a
    pattern you should rely on in practice.

---

## When to Use Each

### 1. Use Functions

Simple, stateless operations.

### 2. Use Closures

Encapsulate simple state with single behavior.

### 3. Use Classes

- Multiple methods needed
- Complex state
- Need inheritance
- Need special methods

---

## Key Takeaways

- Functions → Closures → Classes progression.
- Closures capture free variables.
- Classes provide explicit attributes.
- Classes offer more features (methods, inheritance).
- Choose based on complexity needs.

---

## Exercises

**Exercise 1.**
Start with a function `make_counter()` that returns a closure tracking a count. Then refactor it into a `Counter` class with `increment()`, `decrement()`, and `value()` methods. Show both implementations and discuss when the class version is preferable.

??? success "Solution to Exercise 1"

        # Closure version
        def make_counter():
            count = 0
            def increment():
                nonlocal count
                count += 1
                return count
            def decrement():
                nonlocal count
                count -= 1
                return count
            def value():
                return count
            return increment, decrement, value

        inc, dec, val = make_counter()
        print(inc())  # 1
        print(inc())  # 2
        print(dec())  # 1

        # Class version
        class Counter:
            def __init__(self):
                self._count = 0

            def increment(self):
                self._count += 1
                return self._count

            def decrement(self):
                self._count -= 1
                return self._count

            def value(self):
                return self._count

        c = Counter()
        print(c.increment())  # 1
        print(c.increment())  # 2
        print(c.decrement())  # 1
        # Class is better: easier to extend, inspect, and test

---

**Exercise 2.**
Write a function `create_greeter(greeting)` that returns a closure: a function accepting `name` and returning `f"{greeting}, {name}!"`. Then convert this into a `Greeter` class with `__init__` (accepts greeting) and `__call__` (accepts name). Show both produce the same results.

??? success "Solution to Exercise 2"

        # Closure version
        def create_greeter(greeting):
            def greet(name):
                return f"{greeting}, {name}!"
            return greet

        hello = create_greeter("Hello")
        print(hello("Alice"))  # Hello, Alice!

        # Class version
        class Greeter:
            def __init__(self, greeting):
                self.greeting = greeting

            def __call__(self, name):
                return f"{self.greeting}, {name}!"

        hi = Greeter("Hi")
        print(hi("Bob"))  # Hi, Bob!

        # Both produce same results
        assert hello("Alice") == create_greeter("Hello")("Alice")

---

**Exercise 3.**
Create three implementations of a simple accumulator (stores and sums numbers): (1) a function using a global variable, (2) a closure with `nonlocal`, and (3) a class with `add(n)` and `total()` methods. Compare the three approaches and explain why the class version is most maintainable.

??? success "Solution to Exercise 3"

        # 1. Global variable (worst)
        _total = 0
        def add_global(n):
            global _total
            _total += n
        def get_total():
            return _total

        # 2. Closure (better)
        def make_accumulator():
            total = 0
            def add(n):
                nonlocal total
                total += n
                return total
            return add

        acc = make_accumulator()
        print(acc(10))  # 10
        print(acc(20))  # 30

        # 3. Class (best)
        class Accumulator:
            def __init__(self):
                self._total = 0

            def add(self, n):
                self._total += n
                return self._total

            def total(self):
                return self._total

        a = Accumulator()
        print(a.add(10))  # 10
        print(a.add(20))  # 30
        print(a.total())  # 30
        # Class: inspectable, testable, extensible, multiple instances
