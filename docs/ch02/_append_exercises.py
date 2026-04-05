#!/usr/bin/env python3
"""Append exercises and solutions to ch02 .md files."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# Map: relative path -> exercises text (without leading \n---\n)
EXERCISES = {}

# ============================================================================
# advanced_builtins
# ============================================================================

EXERCISES["advanced_builtins/builtins_namespace.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `count_builtins_by_type()` that returns a dictionary with three keys: `"functions"`, `"exceptions"`, and `"other"`. Iterate over all names in the `builtins` module, look up each attribute with `getattr`, and classify each as an exception class (subclass of `BaseException`), a callable (function or type), or other. Return the counts for each category.

---

**Exercise 2.**
Without running the code, predict the output of the following snippet. Then verify your prediction.

```python
list = [1, 2, 3]
try:
    result = list("hello")
except TypeError as e:
    print(f"Error: {e}")

del list
result = list("hello")
print(result)
```

---

**Exercise 3.**
Write a function `safe_builtin(name)` that takes a string and returns the corresponding built-in object if it exists, or `None` otherwise. Use the `builtins` module and `getattr` with a default value. Test it with `"len"`, `"print"`, and `"foobar"`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import builtins

        def count_builtins_by_type():
            counts = {"functions": 0, "exceptions": 0, "other": 0}
            for name in dir(builtins):
                obj = getattr(builtins, name)
                if isinstance(obj, type) and issubclass(obj, BaseException):
                    counts["exceptions"] += 1
                elif callable(obj):
                    counts["functions"] += 1
                else:
                    counts["other"] += 1
            return counts

        print(count_builtins_by_type())
        ```

    The function checks for exception classes first using `issubclass(obj, BaseException)`, then classifies remaining callables as functions. Everything else (constants like `True`, `None`) goes into "other".

??? success "Solution to Exercise 2"

    The output is:

        ```
        Error: 'list' object is not callable
        ['h', 'e', 'l', 'l', 'o']
        ```

    Assigning `list = [1, 2, 3]` shadows the built-in `list` class. Calling `list("hello")` tries to call the list *object*, which raises `TypeError`. After `del list`, the local name is removed and the built-in `list` becomes accessible again.

??? success "Solution to Exercise 3"

        ```python
        import builtins

        def safe_builtin(name):
            return getattr(builtins, name, None)

        print(safe_builtin("len"))      # <built-in function len>
        print(safe_builtin("print"))    # <built-in function print>
        print(safe_builtin("foobar"))   # None
        ```

    Using `getattr` with a default of `None` avoids raising `AttributeError` when the name does not exist in the `builtins` module.
"""

EXERCISES["advanced_builtins/introspection.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `list_methods(obj)` that takes any object and returns a sorted list of its public method names (names that do not start with `_` and are callable). Test it with a list and a string.

---

**Exercise 2.**
Given the class below, use `type()`, `isinstance()`, and `hasattr()` to answer the following questions in code: What is the type of `d`? Is `d` an instance of `Animal`? Does `d` have an attribute called `speak`?

```python
class Animal:
    pass

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog()
```

---

**Exercise 3.**
Write a function `inspect_object(obj)` that prints the object's type, its `id`, the number of attributes returned by `dir()`, and whether it is callable. Test it with an integer, a string, and a lambda function.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def list_methods(obj):
            return sorted(
                name for name in dir(obj)
                if not name.startswith("_") and callable(getattr(obj, name))
            )

        print(list_methods([]))    # ['append', 'clear', 'copy', ...]
        print(list_methods(""))    # ['capitalize', 'casefold', 'center', ...]
        ```

    `dir(obj)` returns all attribute names. Filtering out names starting with `_` removes dunder methods and private attributes. Checking `callable(getattr(obj, name))` ensures only methods are included.

??? success "Solution to Exercise 2"

        ```python
        class Animal:
            pass

        class Dog(Animal):
            def speak(self):
                return "Woof"

        d = Dog()

        print(type(d))                  # <class '__main__.Dog'>
        print(isinstance(d, Animal))    # True
        print(hasattr(d, "speak"))      # True
        ```

    `type(d)` returns `Dog`, but `isinstance(d, Animal)` returns `True` because `Dog` inherits from `Animal`. `hasattr` checks whether the attribute exists on the object or its class hierarchy.

??? success "Solution to Exercise 3"

        ```python
        def inspect_object(obj):
            print(f"Type: {type(obj)}")
            print(f"ID: {id(obj)}")
            print(f"Attributes: {len(dir(obj))}")
            print(f"Callable: {callable(obj)}")
            print()

        inspect_object(42)
        inspect_object("hello")
        inspect_object(lambda x: x)
        ```

    Integers and strings are not callable, so `callable` returns `False` for them. Lambda functions are callable, so it returns `True`.
"""

EXERCISES["advanced_builtins/sorted.md"] = r"""
---

## Exercises

**Exercise 1.**
Given a list of tuples representing students and their scores, sort them by score in descending order. If two students have the same score, sort them alphabetically by name.

```python
students = [("Alice", 88), ("Bob", 95), ("Carol", 88), ("Dave", 95)]
```

---

**Exercise 2.**
Write a function `sort_by_last_word(sentences)` that takes a list of strings and returns them sorted by their last word (case-insensitive). For example, `["Hello World", "Foo Bar", "Python Alpha"]` should be sorted by `"World"`, `"Bar"`, `"Alpha"`.

---

**Exercise 3.**
Explain the difference between `sorted()` and `list.sort()`. Write a code example that demonstrates that `sorted()` returns a new list while `list.sort()` modifies the list in place and returns `None`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        students = [("Alice", 88), ("Bob", 95), ("Carol", 88), ("Dave", 95)]

        result = sorted(students, key=lambda s: (-s[1], s[0]))
        print(result)
        # [('Bob', 95), ('Dave', 95), ('Alice', 88), ('Carol', 88)]
        ```

    Negating the score (`-s[1]`) sorts scores in descending order. The name `s[0]` serves as the tiebreaker and sorts alphabetically in ascending order.

??? success "Solution to Exercise 2"

        ```python
        def sort_by_last_word(sentences):
            return sorted(sentences, key=lambda s: s.split()[-1].lower())

        result = sort_by_last_word(["Hello World", "Foo Bar", "Python Alpha"])
        print(result)
        # ['Python Alpha', 'Foo Bar', 'Hello World']
        ```

    `s.split()[-1]` extracts the last word, and `.lower()` makes the comparison case-insensitive.

??? success "Solution to Exercise 3"

        ```python
        original = [3, 1, 2]

        # sorted() returns a new list
        new_list = sorted(original)
        print(new_list)    # [1, 2, 3]
        print(original)    # [3, 1, 2] (unchanged)

        # list.sort() modifies in place and returns None
        result = original.sort()
        print(result)      # None
        print(original)    # [1, 2, 3] (modified)
        ```

    `sorted()` creates and returns a new list, leaving the original unchanged. `list.sort()` sorts the list in place and returns `None` -- a common source of bugs when developers write `x = my_list.sort()` expecting to get the sorted list.
"""

# ============================================================================
# bool
# ============================================================================

EXERCISES["bool/and_or_return_values.md"] = r"""
---

## Exercises

**Exercise 1.**
Without running the code, predict the value of each expression. Then verify.

```python
a = 0 or "" or [] or "hello" or 42
b = 1 and "yes" and [] and "no"
c = None or 0 or False or "found"
```

---

**Exercise 2.**
Write a function `first_truthy(*args)` that returns the first truthy value from its arguments, or `None` if all are falsy. Use `or` chaining or a loop with short-circuit logic.

---

**Exercise 3.**
Explain why `x = a or b` is not the same as `x = a if a else b` in all cases. Provide a concrete example where they produce different results, or explain why they are always equivalent.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        a = 0 or "" or [] or "hello" or 42
        print(a)  # "hello"

        b = 1 and "yes" and [] and "no"
        print(b)  # []

        c = None or 0 or False or "found"
        print(c)  # "found"
        ```

    `or` returns the first truthy operand (or the last if all are falsy). `and` returns the first falsy operand (or the last if all are truthy). In `b`, the empty list `[]` is falsy, so `and` stops and returns it.

??? success "Solution to Exercise 2"

        ```python
        def first_truthy(*args):
            for arg in args:
                if arg:
                    return arg
            return None

        print(first_truthy(0, "", [], "hello", 42))  # "hello"
        print(first_truthy(0, "", [], None))          # None
        ```

    The loop returns the first truthy value immediately. If none are found, `None` is returned. This is equivalent to chaining `or` but works with any number of arguments.

??? success "Solution to Exercise 3"

    They are always equivalent for the purpose of choosing between `a` and `b`. Both expressions evaluate `a` for truthiness: if truthy, `a` is the result; otherwise `b` is the result.

        ```python
        a = 0
        b = 42

        x1 = a or b
        x2 = a if a else b

        print(x1)  # 42
        print(x2)  # 42
        print(x1 == x2)  # True
        ```

    The expressions `a or b` and `a if a else b` always produce the same result because `or` returns the first truthy value or the last value, which is exactly the behavior of the conditional expression.
"""

EXERCISES["bool/bool_applications.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `all_positive(numbers)` that returns `True` if every number in the list is positive, without using the built-in `all()`. Use boolean logic and early return.

---

**Exercise 2.**
Write a one-liner using `sum()` and a generator expression to count how many strings in a list have length greater than 5. For example, `["hi", "hello", "wonderful", "ok", "python"]` should return `2`.

---

**Exercise 3.**
Write a function `classify_value(x)` that returns `"falsy"` if `x` is falsy and `"truthy"` otherwise. Test it with `0`, `""`, `[]`, `None`, `1`, `"hello"`, and `[1, 2]`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def all_positive(numbers):
            for n in numbers:
                if n <= 0:
                    return False
            return True

        print(all_positive([1, 2, 3]))     # True
        print(all_positive([1, -2, 3]))    # False
        print(all_positive([]))            # True
        ```

    The function returns `False` as soon as a non-positive number is found. If the loop completes, all numbers are positive.

??? success "Solution to Exercise 2"

        ```python
        words = ["hi", "hello", "wonderful", "ok", "python"]
        count = sum(len(s) > 5 for s in words)
        print(count)  # 2
        ```

    `len(s) > 5` produces `True` or `False`, and `sum()` treats `True` as `1` and `False` as `0`, effectively counting matches.

??? success "Solution to Exercise 3"

        ```python
        def classify_value(x):
            return "falsy" if not x else "truthy"

        for val in [0, "", [], None, 1, "hello", [1, 2]]:
            print(f"{str(val):>10} -> {classify_value(val)}")
        ```

    Output:

        ```
                 0 -> falsy
                   -> falsy
                [] -> falsy
              None -> falsy
                 1 -> truthy
             hello -> truthy
            [1, 2] -> truthy
        ```
"""

EXERCISES["bool/bool_subclass_int.md"] = r"""
---

## Exercises

**Exercise 1.**
Without running the code, predict the output. Then verify.

```python
print(True + True + True)
print(True * 10)
print(False * 100)
print(isinstance(True, int))
```

---

**Exercise 2.**
Write a function `count_true(values)` that takes a list of booleans and returns the count of `True` values. Do this in two ways: once using `sum()`, and once without using `sum()`.

---

**Exercise 3.**
Explain why `True == 1` and `True is not 1` can both be true at the same time. Write code demonstrating both.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        print(True + True + True)    # 3
        print(True * 10)             # 10
        print(False * 100)           # 0
        print(isinstance(True, int)) # True
        ```

    Since `bool` is a subclass of `int`, `True` behaves as `1` and `False` as `0` in arithmetic operations. `isinstance(True, int)` returns `True` because of the inheritance relationship.

??? success "Solution to Exercise 2"

        ```python
        def count_true_sum(values):
            return sum(values)

        def count_true_loop(values):
            count = 0
            for v in values:
                if v:
                    count += 1
            return count

        data = [True, False, True, True, False]
        print(count_true_sum(data))   # 3
        print(count_true_loop(data))  # 3
        ```

    `sum()` works because `True` is `1` and `False` is `0`. The loop version explicitly checks each value.

??? success "Solution to Exercise 3"

        ```python
        print(True == 1)       # True  (value equality)
        print(True is 1)       # False (different objects in CPython 3.12+)
        print(type(True))      # <class 'bool'>
        print(type(1))         # <class 'int'>
        ```

    `==` compares values: `True` and `1` have the same value. `is` compares object identity: `True` is a `bool` singleton and `1` is an `int` object. They are equal in value but may be different objects in memory. Note that in some CPython versions, `True is 1` may return `True` due to integer caching, but this behavior should not be relied upon.
"""

EXERCISES["bool/short_circuit.md"] = r"""
---

## Exercises

**Exercise 1.**
Without running the code, predict which functions get called and what the final output is.

```python
def a():
    print("a called")
    return True

def b():
    print("b called")
    return False

def c():
    print("c called")
    return True

result = a() or b() or c()
print(f"Result: {result}")
```

---

**Exercise 2.**
Write a function `safe_divide(a, b)` that returns `a / b` if `b` is not zero, or `"undefined"` otherwise. Use short-circuit evaluation with `and`/`or` in a single expression (no `if` statement).

---

**Exercise 3.**
Explain why the following code does not raise a `ZeroDivisionError` even though `b` is 0.

```python
b = 0
result = b != 0 and 10 / b > 2
print(result)
```

---

## Solutions

??? success "Solution to Exercise 1"

        ```
        a called
        Result: True
        ```

    `a()` returns `True`. Since `or` short-circuits on the first truthy value, `b()` and `c()` are never called. The result is `True` (the return value of `a()`).

??? success "Solution to Exercise 2"

        ```python
        def safe_divide(a, b):
            return b and a / b or "undefined"

        # Caution: this fails if a/b is 0 (falsy). A safer version:
        def safe_divide(a, b):
            return a / b if b else "undefined"

        print(safe_divide(10, 2))   # 5.0
        print(safe_divide(10, 0))   # "undefined"
        ```

    The `and`/`or` approach works for most cases but has an edge case: if `a / b` evaluates to `0` or `0.0` (falsy), it would incorrectly return `"undefined"`. The conditional expression version is safer and more readable.

??? success "Solution to Exercise 3"

    Short-circuit evaluation prevents the division from executing. `b != 0` evaluates to `False`, so `and` immediately returns `False` without evaluating the right operand `10 / b > 2`.

        ```python
        b = 0
        result = b != 0 and 10 / b > 2
        print(result)  # False
        ```

    `and` stops at the first falsy operand. Since `b != 0` is `False`, Python never evaluates `10 / b`, avoiding the `ZeroDivisionError`.
"""

# ============================================================================
# closures
# ============================================================================

EXERCISES["closures/closure_fundamentals.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `make_greeting(greeting)` that returns a closure. The closure should take a `name` parameter and return the string `f"{greeting}, {name}!"`. For example, `hello = make_greeting("Hello")` followed by `hello("Alice")` should return `"Hello, Alice!"`.

---

**Exercise 2.**
Write a function `make_accumulator(initial=0)` that returns a closure. Each time the closure is called with a number, it adds that number to a running total and returns the new total. Use the `nonlocal` keyword.

---

**Exercise 3.**
Inspect the closure created by `make_greeting("Hi")` from Exercise 1. Print the `__closure__` attribute and access the captured value using `cell_contents`. Verify that it holds the string `"Hi"`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def make_greeting(greeting):
            def greet(name):
                return f"{greeting}, {name}!"
            return greet

        hello = make_greeting("Hello")
        print(hello("Alice"))  # Hello, Alice!
        print(hello("Bob"))    # Hello, Bob!

        hi = make_greeting("Hi")
        print(hi("Carol"))     # Hi, Carol!
        ```

    The inner function `greet` captures `greeting` from the enclosing scope. Each call to `make_greeting` creates a new closure with its own captured value.

??? success "Solution to Exercise 2"

        ```python
        def make_accumulator(initial=0):
            total = initial
            def add(n):
                nonlocal total
                total += n
                return total
            return add

        acc = make_accumulator()
        print(acc(5))    # 5
        print(acc(10))   # 15
        print(acc(3))    # 18

        acc2 = make_accumulator(100)
        print(acc2(1))   # 101
        ```

    `nonlocal total` allows the inner function to modify `total` in the enclosing scope. Each accumulator maintains its own independent total.

??? success "Solution to Exercise 3"

        ```python
        def make_greeting(greeting):
            def greet(name):
                return f"{greeting}, {name}!"
            return greet

        hi = make_greeting("Hi")

        print(hi.__closure__)                     # (<cell at 0x...>,)
        print(hi.__closure__[0].cell_contents)    # Hi
        ```

    The `__closure__` attribute is a tuple of cell objects, one for each captured variable. `cell_contents` reveals the actual captured value.
"""

EXERCISES["closures/closures_cheat_sheet.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a closure `make_filter(threshold)` that returns a function. The returned function takes a list of numbers and returns only those greater than `threshold`.

---

**Exercise 2.**
Write a closure `make_logger(prefix)` that returns a function. The returned function takes a message and prints `f"[{prefix}] {message}"`. Also include a counter using `nonlocal` that tracks how many messages have been logged.

---

**Exercise 3.**
Identify the bug in the following code. Fix it so that each function in the list returns its index (0, 1, 2, 3).

```python
funcs = []
for i in range(4):
    funcs.append(lambda: i)

print([f() for f in funcs])  # Expected: [0, 1, 2, 3]
```

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def make_filter(threshold):
            def filter_func(numbers):
                return [n for n in numbers if n > threshold]
            return filter_func

        above_10 = make_filter(10)
        print(above_10([5, 15, 8, 20, 3]))  # [15, 20]
        ```

    The closure captures `threshold` and uses it in the list comprehension filter.

??? success "Solution to Exercise 2"

        ```python
        def make_logger(prefix):
            count = 0
            def log(message):
                nonlocal count
                count += 1
                print(f"[{prefix}] ({count}) {message}")
            return log

        info = make_logger("INFO")
        info("Server started")    # [INFO] (1) Server started
        info("Request received")  # [INFO] (2) Request received
        ```

    The closure captures both `prefix` (read-only) and `count` (modified via `nonlocal`).

??? success "Solution to Exercise 3"

    The bug is late binding: all lambdas capture the variable `i` by reference, and by the time they are called, `i` is `3`. Fix it by using a default argument to capture the current value:

        ```python
        funcs = []
        for i in range(4):
            funcs.append(lambda i=i: i)

        print([f() for f in funcs])  # [0, 1, 2, 3]
        ```

    The default argument `i=i` captures the value of `i` at the time each lambda is created, rather than referencing the loop variable.
"""

EXERCISES["closures/late_binding.md"] = r"""
---

## Exercises

**Exercise 1.**
Without running the code, predict the output. Then verify.

```python
funcs = [lambda x: x + i for i in range(3)]
print([f(10) for f in funcs])
```

---

**Exercise 2.**
Rewrite the list comprehension from Exercise 1 so that each lambda correctly captures its own value of `i`, producing `[10, 11, 12]`.

---

**Exercise 3.**
Explain why using `functools.partial` can also solve the late-binding problem. Rewrite the list comprehension from Exercise 1 using `functools.partial`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        funcs = [lambda x: x + i for i in range(3)]
        print([f(10) for f in funcs])  # [12, 12, 12]
        ```

    All lambdas share the same `i` variable. By the time they are called, the loop has finished and `i` is `2`, so each returns `10 + 2 = 12`.

??? success "Solution to Exercise 2"

        ```python
        funcs = [lambda x, i=i: x + i for i in range(3)]
        print([f(10) for f in funcs])  # [10, 11, 12]
        ```

    The default argument `i=i` captures the current value of `i` at each iteration.

??? success "Solution to Exercise 3"

        ```python
        from functools import partial

        def add(x, i):
            return x + i

        funcs = [partial(add, i=i) for i in range(3)]
        print([f(10) for f in funcs])  # [10, 11, 12]
        ```

    `functools.partial` creates a new function with `i` bound to a specific value. Unlike closures, `partial` stores the value directly rather than referencing a variable, so late binding is not an issue.
"""

EXERCISES["closures/nonlocal_mutation.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a closure `make_counter()` that returns three functions: `increment`, `decrement`, and `get_value`. The counter should start at 0. Use `nonlocal` to modify the shared state.

---

**Exercise 2.**
Explain why the following code raises `UnboundLocalError`. Fix it using `nonlocal`.

```python
def outer():
    count = 0
    def inner():
        count += 1
        return count
    return inner
```

---

**Exercise 3.**
Write a closure `make_toggle()` that returns a function. Each call toggles between `True` and `False`, starting with `True` on the first call.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def make_counter():
            value = 0
            def increment():
                nonlocal value
                value += 1
            def decrement():
                nonlocal value
                value -= 1
            def get_value():
                return value
            return increment, decrement, get_value

        inc, dec, get = make_counter()
        inc(); inc(); inc()
        print(get())  # 3
        dec()
        print(get())  # 2
        ```

    All three functions share the same `value` variable from the enclosing scope, modified via `nonlocal`.

??? success "Solution to Exercise 2"

    The assignment `count += 1` makes `count` a local variable in `inner`. Python detects this at compile time, so reading `count` before assignment raises `UnboundLocalError`.

        ```python
        def outer():
            count = 0
            def inner():
                nonlocal count
                count += 1
                return count
            return inner

        f = outer()
        print(f())  # 1
        print(f())  # 2
        ```

    `nonlocal count` tells Python that `count` refers to the variable in the enclosing scope, not a new local variable.

??? success "Solution to Exercise 3"

        ```python
        def make_toggle():
            state = False
            def toggle():
                nonlocal state
                state = not state
                return state
            return toggle

        t = make_toggle()
        print(t())  # True
        print(t())  # False
        print(t())  # True
        ```

    The state starts as `False` and flips on each call. The first call returns `True`.
"""

EXERCISES["closures/practical_patterns.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a memoization closure `make_memoized(func)` that caches results of a single-argument function. The closure should store results in a dictionary and return cached values for repeated arguments.

---

**Exercise 2.**
Write a closure `make_rate_limiter(max_calls, period)` that returns a function wrapper. The wrapper should allow at most `max_calls` calls within `period` seconds, raising a `RuntimeError` if the limit is exceeded. Use `time.time()` and a list to track call timestamps.

---

**Exercise 3.**
Write a closure `make_validator(min_val, max_val)` that returns a function. The returned function takes a value and returns `True` if it is between `min_val` and `max_val` (inclusive), `False` otherwise.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def make_memoized(func):
            cache = {}
            def wrapper(arg):
                if arg not in cache:
                    cache[arg] = func(arg)
                return cache[arg]
            return wrapper

        @make_memoized
        def square(x):
            print(f"Computing {x}^2")
            return x ** 2

        print(square(4))  # Computing 4^2 -> 16
        print(square(4))  # 16 (cached, no print)
        print(square(5))  # Computing 5^2 -> 25
        ```

    The closure captures `cache` (a dict) and `func`. Results are stored on first call and returned from cache on subsequent calls.

??? success "Solution to Exercise 2"

        ```python
        import time

        def make_rate_limiter(max_calls, period):
            timestamps = []
            def wrapper(func):
                def limited(*args, **kwargs):
                    now = time.time()
                    timestamps[:] = [t for t in timestamps if now - t < period]
                    if len(timestamps) >= max_calls:
                        raise RuntimeError("Rate limit exceeded")
                    timestamps.append(now)
                    return func(*args, **kwargs)
                return limited
            return wrapper

        @make_rate_limiter(3, 1.0)
        def api_call():
            return "success"

        print(api_call())  # success
        print(api_call())  # success
        print(api_call())  # success
        # api_call()       # RuntimeError: Rate limit exceeded
        ```

    The closure maintains a list of timestamps. Old timestamps outside the period are removed before each check.

??? success "Solution to Exercise 3"

        ```python
        def make_validator(min_val, max_val):
            def validate(value):
                return min_val <= value <= max_val
            return validate

        is_valid_age = make_validator(0, 120)
        print(is_valid_age(25))   # True
        print(is_valid_age(-5))   # False
        print(is_valid_age(150))  # False
        ```

    The closure captures `min_val` and `max_val` and uses Python's chained comparison.
"""

EXERCISES["closures/scoping_rules.md"] = r"""
---

## Exercises

**Exercise 1.**
Without running the code, predict the output. Then verify.

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()

outer()
print(x)
```

---

**Exercise 2.**
Write a function `outer()` that defines a variable `data = []` and returns two closures: `add(item)` (which appends to `data`) and `get()` (which returns a copy of `data`). Demonstrate that both closures share the same `data`.

---

**Exercise 3.**
Explain what happens when you read a global variable inside a function versus when you assign to it. Why does assignment create a local variable?

---

## Solutions

??? success "Solution to Exercise 1"

        ```
        enclosing
        global
        ```

    `inner()` finds `x` in the enclosing scope (`"enclosing"`). The global `x` remains `"global"` because neither function modifies it.

??? success "Solution to Exercise 2"

        ```python
        def outer():
            data = []
            def add(item):
                data.append(item)
            def get():
                return data.copy()
            return add, get

        add, get = outer()
        add("a")
        add("b")
        print(get())  # ['a', 'b']
        add("c")
        print(get())  # ['a', 'b', 'c']
        ```

    Both closures capture the same `data` list. `add` mutates it (no `nonlocal` needed for mutation), and `get` returns a copy for safety.

??? success "Solution to Exercise 3"

    When Python compiles a function, it scans for all assignment targets. If a variable name appears on the left side of an assignment (e.g., `x = ...`), Python treats it as a local variable for the entire function. This means even reading `x` before the assignment raises `UnboundLocalError`.

        ```python
        x = 10

        def read_only():
            print(x)       # Works: reads global x

        def assigns():
            print(x)       # UnboundLocalError!
            x = 20         # This makes x local for entire function

        read_only()        # 10
        # assigns()        # UnboundLocalError
        ```

    To modify a global variable, use `global x`. To modify an enclosing variable, use `nonlocal x`.
"""

# Due to the massive size, I'll continue building the rest of the exercises dict and then apply them all.
# For brevity in this script, I'll include all remaining files.

# ============================================================================
# composites
# ============================================================================

EXERCISES["composites/dict_internals.md"] = r"""
---

## Exercises

**Exercise 1.**
Create a dictionary with keys `1`, `1.0`, and `True`. How many entries does the dictionary have? Explain why.

---

**Exercise 2.**
Write a function `find_hash_collision()` that finds two different strings (among the first 100000 integers converted to strings) that have the same hash modulo 1000. Print both strings and their hash values.

---

**Exercise 3.**
Demonstrate that looking up a key in a dictionary is O(1) by timing lookups in dictionaries of size 1000 and 1000000 and showing that the times are approximately equal.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        d = {1: "int", 1.0: "float", True: "bool"}
        print(d)       # {1: 'bool'}
        print(len(d))  # 1
        ```

    The dictionary has only 1 entry because `1 == 1.0 == True` and `hash(1) == hash(1.0) == hash(True)`. Python treats them as the same key, and each subsequent assignment overwrites the value.

??? success "Solution to Exercise 2"

        ```python
        def find_hash_collision():
            seen = {}
            for i in range(100000):
                s = str(i)
                h = hash(s) % 1000
                if h in seen:
                    print(f"'{seen[h]}' and '{s}' both hash to {h}")
                    return
                seen[h] = s

        find_hash_collision()
        ```

    Hash collisions are common when mapping to a small range. The function finds two strings whose hashes collide modulo 1000.

??? success "Solution to Exercise 3"

        ```python
        import timeit

        setup_small = "d = {i: i for i in range(1_000)}"
        setup_large = "d = {i: i for i in range(1_000_000)}"

        t_small = timeit.timeit("999 in d", setup=setup_small, number=100000)
        t_large = timeit.timeit("999999 in d", setup=setup_large, number=100000)

        print(f"Small dict: {t_small:.4f}s")
        print(f"Large dict: {t_large:.4f}s")
        ```

    Both times should be approximately equal because dictionary lookup is O(1) regardless of size.
"""

EXERCISES["composites/dict_merge_operators.md"] = r"""
---

## Exercises

**Exercise 1.**
Given two dictionaries `defaults = {"color": "red", "size": 10}` and `custom = {"size": 20, "font": "Arial"}`, merge them so that `custom` values take priority. Show two approaches: one using `|` and one using `{**d1, **d2}`.

---

**Exercise 2.**
Write a function `deep_merge(d1, d2)` that merges two dictionaries recursively. If both values for a key are dictionaries, merge them recursively. Otherwise, `d2`'s value wins.

---

**Exercise 3.**
Demonstrate the difference between `d1 | d2` (creates new dict) and `d1 |= d2` (updates in place) by showing that one changes the original dictionary and the other does not.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        defaults = {"color": "red", "size": 10}
        custom = {"size": 20, "font": "Arial"}

        # Using | (Python 3.9+)
        merged1 = defaults | custom
        print(merged1)  # {'color': 'red', 'size': 20, 'font': 'Arial'}

        # Using ** unpacking
        merged2 = {**defaults, **custom}
        print(merged2)  # {'color': 'red', 'size': 20, 'font': 'Arial'}
        ```

    Both approaches give `custom` priority. The rightmost dictionary's values win for duplicate keys.

??? success "Solution to Exercise 2"

        ```python
        def deep_merge(d1, d2):
            result = d1.copy()
            for key, value in d2.items():
                if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                    result[key] = deep_merge(result[key], value)
                else:
                    result[key] = value
            return result

        a = {"db": {"host": "localhost", "port": 5432}, "debug": True}
        b = {"db": {"port": 3306, "user": "admin"}, "debug": False}

        print(deep_merge(a, b))
        # {'db': {'host': 'localhost', 'port': 3306, 'user': 'admin'}, 'debug': False}
        ```

    The recursive approach preserves nested keys from both dictionaries while letting `d2` values take priority.

??? success "Solution to Exercise 3"

        ```python
        d1 = {"a": 1, "b": 2}
        d2 = {"b": 3, "c": 4}

        # | creates a new dict
        d3 = d1 | d2
        print(d1)  # {'a': 1, 'b': 2} (unchanged)
        print(d3)  # {'a': 1, 'b': 3, 'c': 4}

        # |= updates in place
        original_id = id(d1)
        d1 |= d2
        print(d1)  # {'a': 1, 'b': 3, 'c': 4} (modified)
        print(id(d1) == original_id)  # True (same object)
        ```

    `|` returns a new dictionary, leaving originals intact. `|=` modifies the left-hand dictionary in place.
"""

EXERCISES["composites/dict_ordering.md"] = r"""
---

## Exercises

**Exercise 1.**
Create a dictionary with keys inserted in the order `"z"`, `"a"`, `"m"`. Verify that iterating over the dictionary yields the keys in insertion order. Then delete `"a"` and re-insert it. What order do the keys appear in now?

---

**Exercise 2.**
Write a function `move_to_front(d, key)` that takes a dictionary and a key, and returns a new dictionary with that key moved to the front (first position), preserving the relative order of all other keys.

---

**Exercise 3.**
Using `next(iter(d))` and `next(reversed(d))`, write a function `first_and_last(d)` that returns a tuple of the first and last key-value pairs of a dictionary.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        d = {}
        d["z"] = 1
        d["a"] = 2
        d["m"] = 3
        print(list(d.keys()))  # ['z', 'a', 'm']

        del d["a"]
        d["a"] = 2
        print(list(d.keys()))  # ['z', 'm', 'a']
        ```

    Deleting and re-inserting a key places it at the end. Updating an existing key's value does not change its position.

??? success "Solution to Exercise 2"

        ```python
        def move_to_front(d, key):
            if key not in d:
                return dict(d)
            return {key: d[key], **{k: v for k, v in d.items() if k != key}}

        d = {"a": 1, "b": 2, "c": 3}
        print(move_to_front(d, "c"))  # {'c': 3, 'a': 1, 'b': 2}
        ```

    The function creates a new dict with `key` first, followed by all other items in their original order.

??? success "Solution to Exercise 3"

        ```python
        def first_and_last(d):
            first_key = next(iter(d))
            last_key = next(reversed(d))
            return (first_key, d[first_key]), (last_key, d[last_key])

        d = {"x": 10, "y": 20, "z": 30}
        first, last = first_and_last(d)
        print(f"First: {first}")  # First: ('x', 10)
        print(f"Last: {last}")    # Last: ('z', 30)
        ```

    `iter(d)` starts from the first key, `reversed(d)` starts from the last. Both are O(1) operations.
"""

EXERCISES["composites/hashing_deep_dive.md"] = r"""
---

## Exercises

**Exercise 1.**
Verify the hash consistency rule: if `a == b`, then `hash(a) == hash(b)`. Test this with `1` and `1.0`, with `True` and `1`, and with two identical tuples.

---

**Exercise 2.**
Write a class `Color` with attributes `r`, `g`, `b` that is both hashable and supports equality comparison. Two `Color` objects should be equal if their RGB values match. Use it as a dictionary key.

---

**Exercise 3.**
Explain why lists are not hashable. Demonstrate the error that occurs when you try to use a list as a dictionary key, and show how converting it to a tuple solves the problem.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # int and float
        print(1 == 1.0)                # True
        print(hash(1) == hash(1.0))    # True

        # bool and int
        print(True == 1)               # True
        print(hash(True) == hash(1))   # True

        # identical tuples
        t1 = (1, 2, 3)
        t2 = (1, 2, 3)
        print(t1 == t2)               # True
        print(hash(t1) == hash(t2))   # True
        ```

    The hash consistency rule is fundamental: equal objects must have equal hashes. This is required for correct behavior in sets and dictionaries.

??? success "Solution to Exercise 2"

        ```python
        class Color:
            def __init__(self, r, g, b):
                self.r = r
                self.g = g
                self.b = b

            def __eq__(self, other):
                return (self.r, self.g, self.b) == (other.r, other.g, other.b)

            def __hash__(self):
                return hash((self.r, self.g, self.b))

        palette = {Color(255, 0, 0): "red", Color(0, 255, 0): "green"}
        print(palette[Color(255, 0, 0)])  # red
        ```

    Both `__eq__` and `__hash__` must be implemented. The hash is based on the same fields used for equality.

??? success "Solution to Exercise 3"

        ```python
        try:
            d = {[1, 2]: "value"}
        except TypeError as e:
            print(f"Error: {e}")  # unhashable type: 'list'

        # Convert to tuple
        d = {(1, 2): "value"}
        print(d[(1, 2)])  # value
        ```

    Lists are mutable, so their contents can change after insertion into a set or dict, which would break the hash consistency rule. Tuples are immutable and therefore hashable.
"""

EXERCISES["composites/list_copying.md"] = r"""
---

## Exercises

**Exercise 1.**
Demonstrate the aliasing problem by creating a list `a`, assigning `b = a`, appending to `b`, and showing that `a` is also affected. Then fix it using a shallow copy.

---

**Exercise 2.**
Given the nested list `matrix = [[1, 2], [3, 4]]`, create both a shallow copy and a deep copy. Modify `matrix[0][0] = 99` and show which copy is affected and which is not.

---

**Exercise 3.**
Write a function `safe_remove_evens(lst)` that returns a new list with all even numbers removed, without modifying the original list. Demonstrate that the original list is unchanged.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        a = [1, 2, 3]
        b = a
        b.append(4)
        print(a)  # [1, 2, 3, 4] (affected!)

        # Fix with shallow copy
        a = [1, 2, 3]
        b = a.copy()
        b.append(4)
        print(a)  # [1, 2, 3] (unchanged)
        print(b)  # [1, 2, 3, 4]
        ```

    `b = a` creates an alias. `b = a.copy()` creates an independent shallow copy.

??? success "Solution to Exercise 2"

        ```python
        import copy

        matrix = [[1, 2], [3, 4]]
        shallow = matrix.copy()
        deep = copy.deepcopy(matrix)

        matrix[0][0] = 99

        print(matrix)  # [[99, 2], [3, 4]]
        print(shallow) # [[99, 2], [3, 4]] (affected!)
        print(deep)    # [[1, 2], [3, 4]]  (unchanged)
        ```

    Shallow copy shares nested objects. Deep copy recursively copies everything, creating fully independent structures.

??? success "Solution to Exercise 3"

        ```python
        def safe_remove_evens(lst):
            return [x for x in lst if x % 2 != 0]

        original = [1, 2, 3, 4, 5, 6]
        filtered = safe_remove_evens(original)

        print(original)  # [1, 2, 3, 4, 5, 6] (unchanged)
        print(filtered)  # [1, 3, 5]
        ```

    List comprehension creates a new list, leaving the original intact.
"""

EXERCISES["composites/nested_structures.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `flatten(nested)` that takes an arbitrarily nested list and returns a flat list of all non-list elements. For example, `flatten([1, [2, [3, 4]], 5])` should return `[1, 2, 3, 4, 5]`.

---

**Exercise 2.**
Given the nested dictionary below, write a function `safe_get(d, *keys, default=None)` that navigates the nested structure safely. It should return the value if all keys exist, or `default` otherwise.

```python
data = {"user": {"address": {"city": "Seoul"}}}
```

---

**Exercise 3.**
Explain the common pitfall of `grid = [[0] * 3] * 3`. What happens when you set `grid[0][0] = 1`? Write the correct way to create a 3x3 grid of zeros.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def flatten(nested):
            result = []
            for item in nested:
                if isinstance(item, list):
                    result.extend(flatten(item))
                else:
                    result.append(item)
            return result

        print(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
        print(flatten([[1, 2], [3, [4, [5]]]]))  # [1, 2, 3, 4, 5]
        ```

    The function uses recursion to handle arbitrary nesting depth.

??? success "Solution to Exercise 2"

        ```python
        def safe_get(d, *keys, default=None):
            for key in keys:
                if isinstance(d, dict):
                    d = d.get(key, default)
                else:
                    return default
            return d

        data = {"user": {"address": {"city": "Seoul"}}}

        print(safe_get(data, "user", "address", "city"))     # Seoul
        print(safe_get(data, "user", "phone"))                # None
        print(safe_get(data, "missing", "key", default="N/A"))  # N/A
        ```

    The function chains `.get()` calls, returning the default if any key is missing.

??? success "Solution to Exercise 3"

    `[[0] * 3] * 3` creates three references to the same inner list. Modifying one row affects all rows:

        ```python
        bad_grid = [[0] * 3] * 3
        bad_grid[0][0] = 1
        print(bad_grid)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

        # Correct way
        good_grid = [[0] * 3 for _ in range(3)]
        good_grid[0][0] = 1
        print(good_grid)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
        ```

    The list comprehension creates independent inner lists for each row.
"""

EXERCISES["composites/set_internals.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `find_duplicates(lst)` that uses a set to find and return all duplicate elements in a list. For example, `find_duplicates([1, 2, 2, 3, 3, 3, 4])` should return `{2, 3}`.

---

**Exercise 2.**
Demonstrate that set elements must be hashable by attempting to add a list to a set. Then show how to add the same data by converting it to a tuple.

---

**Exercise 3.**
Given two sets `a = {1, 2, 3, 4, 5}` and `b = {4, 5, 6, 7, 8}`, compute and print the union, intersection, difference (a - b), and symmetric difference using both operator syntax and method syntax.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def find_duplicates(lst):
            seen = set()
            duplicates = set()
            for item in lst:
                if item in seen:
                    duplicates.add(item)
                seen.add(item)
            return duplicates

        print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))  # {2, 3}
        ```

    Using two sets gives O(n) performance. `seen` tracks all encountered elements and `duplicates` collects those seen more than once.

??? success "Solution to Exercise 2"

        ```python
        s = set()

        try:
            s.add([1, 2, 3])
        except TypeError as e:
            print(f"Error: {e}")  # unhashable type: 'list'

        s.add((1, 2, 3))
        print(s)  # {(1, 2, 3)}
        ```

    Lists are mutable and unhashable. Tuples are immutable and hashable, making them valid set elements.

??? success "Solution to Exercise 3"

        ```python
        a = {1, 2, 3, 4, 5}
        b = {4, 5, 6, 7, 8}

        # Operator syntax
        print(a | b)   # {1, 2, 3, 4, 5, 6, 7, 8}
        print(a & b)   # {4, 5}
        print(a - b)   # {1, 2, 3}
        print(a ^ b)   # {1, 2, 3, 6, 7, 8}

        # Method syntax
        print(a.union(b))                # {1, 2, 3, 4, 5, 6, 7, 8}
        print(a.intersection(b))         # {4, 5}
        print(a.difference(b))           # {1, 2, 3}
        print(a.symmetric_difference(b)) # {1, 2, 3, 6, 7, 8}
        ```

    Both syntaxes produce identical results. The method syntax is more explicit and can accept any iterable, while operators require both operands to be sets.
"""

EXERCISES["composites/time_complexity.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a benchmark that compares the time to check membership (`x in collection`) for a list, set, and dictionary, each with 100000 elements. Which is fastest and why?

---

**Exercise 2.**
Explain why `list.insert(0, x)` is O(n) while `list.append(x)` is O(1). Write a timing experiment that demonstrates this difference with a list of 100000 elements.

---

**Exercise 3.**
A developer has written the following code. Identify the performance problem and suggest a fix that improves the time complexity.

```python
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
```

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import timeit

        n = 100_000
        setup_list = f"c = list(range({n}))"
        setup_set = f"c = set(range({n}))"
        setup_dict = f"c = {{i: None for i in range({n})}}"

        t_list = timeit.timeit(f"{n-1} in c", setup=setup_list, number=1000)
        t_set = timeit.timeit(f"{n-1} in c", setup=setup_set, number=1000)
        t_dict = timeit.timeit(f"{n-1} in c", setup=setup_dict, number=1000)

        print(f"List: {t_list:.4f}s")
        print(f"Set:  {t_set:.6f}s")
        print(f"Dict: {t_dict:.6f}s")
        ```

    Sets and dicts use hash-based lookup (O(1) average), while lists require linear scan (O(n)). Sets and dicts are orders of magnitude faster for membership testing.

??? success "Solution to Exercise 2"

        ```python
        import timeit

        n = 100_000
        t_append = timeit.timeit(
            "lst.append(0)",
            setup=f"lst = list(range({n}))",
            number=1000
        )
        t_insert = timeit.timeit(
            "lst.insert(0, 0)",
            setup=f"lst = list(range({n}))",
            number=1000
        )

        print(f"append: {t_append:.4f}s")
        print(f"insert(0): {t_insert:.4f}s")
        ```

    `append` adds to the end in O(1) amortized time. `insert(0, x)` must shift all existing elements one position to the right, requiring O(n) time.

??? success "Solution to Exercise 3"

    The problem is that `item not in result` performs a linear scan of `result` for each element, giving O(n^2) overall complexity. Fix by using a set for fast membership testing:

        ```python
        def remove_duplicates(lst):
            seen = set()
            result = []
            for item in lst:
                if item not in seen:
                    seen.add(item)
                    result.append(item)
            return result
        ```

    The improved version is O(n) because set membership testing is O(1).
"""

EXERCISES["composites/tuple_optimization.md"] = r"""
---

## Exercises

**Exercise 1.**
Compare the memory usage of a tuple and a list containing the same 1000 integers using `sys.getsizeof()`. Which uses less memory and why?

---

**Exercise 2.**
Demonstrate that tuples are hashable (and can be used as dictionary keys) while lists are not. Create a dictionary that maps (x, y) coordinate tuples to city names.

---

**Exercise 3.**
Explain what tuple packing and unpacking are. Write an example that uses both in a function that returns multiple values.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import sys

        data = list(range(1000))
        t = tuple(data)
        l = list(data)

        print(f"Tuple: {sys.getsizeof(t)} bytes")
        print(f"List:  {sys.getsizeof(l)} bytes")
        ```

    Tuples use less memory because they are fixed-size and do not need to store extra capacity for potential growth. Lists allocate extra space to support efficient appending.

??? success "Solution to Exercise 2"

        ```python
        cities = {
            (37.5665, 126.9780): "Seoul",
            (35.6762, 139.6503): "Tokyo",
            (40.7128, -74.0060): "New York",
        }

        print(cities[(37.5665, 126.9780)])  # Seoul

        try:
            bad = {[37.5665, 126.9780]: "Seoul"}
        except TypeError as e:
            print(f"Error: {e}")  # unhashable type: 'list'
        ```

    Tuples are immutable and hashable, making them valid dictionary keys. Lists are mutable and unhashable.

??? success "Solution to Exercise 3"

        ```python
        # Tuple packing: multiple values packed into a tuple
        coordinates = 37.5665, 126.9780  # packing
        print(type(coordinates))  # <class 'tuple'>

        # Tuple unpacking: extracting values from a tuple
        lat, lon = coordinates  # unpacking
        print(f"Latitude: {lat}, Longitude: {lon}")

        # Common pattern: function returning multiple values
        def min_max(numbers):
            return min(numbers), max(numbers)  # packing

        lo, hi = min_max([3, 1, 4, 1, 5, 9])  # unpacking
        print(f"Min: {lo}, Max: {hi}")  # Min: 1, Max: 9
        ```

    Packing creates a tuple from comma-separated values. Unpacking assigns tuple elements to individual variables.
"""

# I need to continue with all remaining sections. Due to the extremely large number of files,
# I'll write the rest to a separate continuation script.

# For now, write the current batch
def append_exercises():
    for rel_path, content in EXERCISES.items():
        full_path = os.path.join(BASE, rel_path)
        if not os.path.exists(full_path):
            print(f"SKIP (not found): {full_path}")
            continue

        with open(full_path, 'r') as f:
            existing = f.read()

        # Check if exercises already appended
        if "## Exercises" in existing:
            print(f"SKIP (already has exercises): {rel_path}")
            continue

        with open(full_path, 'a') as f:
            f.write(content)

        print(f"DONE: {rel_path}")

if __name__ == "__main__":
    append_exercises()
