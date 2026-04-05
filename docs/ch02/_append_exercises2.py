#!/usr/bin/env python3
"""Append exercises batch 2: exceptions, functions_params, io, iteration, naming."""

import os

BASE = os.path.dirname(os.path.abspath(__file__))
EXERCISES = {}

# ============================================================================
# exceptions
# ============================================================================

EXERCISES["exceptions/assert.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `calculate_average(numbers)` that uses `assert` to ensure the input list is not empty before computing the average. Test it with both a valid list and an empty list.

---

**Exercise 2.**
Explain why `assert` should not be used for input validation in production code. What happens when Python is run with the `-O` (optimize) flag?

---

**Exercise 3.**
Write a function `validate_age(age)` that uses `assert` with a custom error message to check that `age` is between 0 and 150. Then rewrite it using a proper `if`/`raise` pattern that works even with optimization enabled.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def calculate_average(numbers):
            assert len(numbers) > 0, "Cannot compute average of empty list"
            return sum(numbers) / len(numbers)

        print(calculate_average([10, 20, 30]))  # 20.0

        try:
            calculate_average([])
        except AssertionError as e:
            print(f"Error: {e}")  # Cannot compute average of empty list
        ```

    The `assert` statement raises `AssertionError` with the custom message when the condition is `False`.

??? success "Solution to Exercise 2"

    `assert` statements are removed entirely when Python is run with `-O` (optimize) flag:

        ```bash
        python -O script.py
        ```

    This means any validation done via `assert` will be silently skipped in optimized mode. For input validation, always use explicit `if`/`raise`:

        ```python
        # Bad: silently skipped with -O
        assert user_input > 0

        # Good: always runs
        if user_input <= 0:
            raise ValueError("Input must be positive")
        ```

    Use `assert` only for internal consistency checks during development, not for validating external input.

??? success "Solution to Exercise 3"

        ```python
        # Using assert (development only)
        def validate_age_assert(age):
            assert 0 <= age <= 150, f"Invalid age: {age}"
            return age

        # Using if/raise (production safe)
        def validate_age(age):
            if not (0 <= age <= 150):
                raise ValueError(f"Invalid age: {age}")
            return age

        print(validate_age(25))  # 25

        try:
            validate_age(-5)
        except ValueError as e:
            print(f"Error: {e}")  # Invalid age: -5
        ```

    The `if`/`raise` version works regardless of optimization flags and raises a more appropriate `ValueError` instead of `AssertionError`.
"""

EXERCISES["exceptions/compile_vs_runtime.md"] = r"""
---

## Exercises

**Exercise 1.**
Classify each of the following errors as compile-time (syntax) or runtime. Verify by writing code that triggers each.

- Missing colon after `if`
- Dividing by zero
- Using an undefined variable
- Invalid indentation

---

**Exercise 2.**
Write a function that contains a syntax error and show that importing the module fails immediately. Then fix the error and show that the function works.

---

**Exercise 3.**
Write code that passes syntax checking but raises a `TypeError` at runtime. Explain why Python cannot catch this error at compile time.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # Compile-time (SyntaxError):
        # if True      # Missing colon -> SyntaxError
        # def f():
        #  x = 1       # Invalid indentation -> IndentationError

        # Runtime errors:
        try:
            result = 1 / 0
        except ZeroDivisionError as e:
            print(f"Runtime: {e}")

        try:
            print(undefined_variable)
        except NameError as e:
            print(f"Runtime: {e}")
        ```

    Syntax errors are caught during parsing, before any code executes. Runtime errors occur during execution.

??? success "Solution to Exercise 2"

        ```python
        # File with syntax error (cannot be imported):
        # def broken(:     # SyntaxError: invalid syntax

        # Fixed version:
        def fixed():
            return "It works!"

        print(fixed())  # It works!
        ```

    Python compiles the entire module before executing any code. A syntax error anywhere in the file prevents the entire module from loading.

??? success "Solution to Exercise 3"

        ```python
        def add(a, b):
            return a + b

        # This is valid syntax but fails at runtime
        try:
            result = add("hello", 42)
        except TypeError as e:
            print(f"Runtime error: {e}")
            # unsupported operand type(s) for +: 'str' and 'int'
        ```

    Python is dynamically typed, so the types of `a` and `b` are not known until runtime. The syntax `a + b` is valid for many type combinations, so Python cannot determine at compile time that this particular call will fail.
"""

EXERCISES["exceptions/custom_exceptions.md"] = r"""
---

## Exercises

**Exercise 1.**
Create a custom exception hierarchy for a banking application: `BankError` (base), `InsufficientFundsError`, and `AccountNotFoundError`. Each should accept a meaningful message.

---

**Exercise 2.**
Write a class `BankAccount` with methods `deposit(amount)` and `withdraw(amount)`. The `withdraw` method should raise `InsufficientFundsError` (from Exercise 1) if the balance would go negative. Include the current balance and requested amount in the error message.

---

**Exercise 3.**
Write a `try`/`except` block that catches `InsufficientFundsError` specifically, then a broader `BankError`, demonstrating that exception hierarchy ordering matters in `except` clauses.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        class BankError(Exception):
            pass

        class InsufficientFundsError(BankError):
            def __init__(self, balance, amount):
                self.balance = balance
                self.amount = amount
                super().__init__(
                    f"Cannot withdraw ${amount}: only ${balance} available"
                )

        class AccountNotFoundError(BankError):
            def __init__(self, account_id):
                self.account_id = account_id
                super().__init__(f"Account {account_id} not found")
        ```

    Custom exceptions inherit from a common base class, enabling both specific and broad catching.

??? success "Solution to Exercise 2"

        ```python
        class BankAccount:
            def __init__(self, balance=0):
                self.balance = balance

            def deposit(self, amount):
                self.balance += amount

            def withdraw(self, amount):
                if amount > self.balance:
                    raise InsufficientFundsError(self.balance, amount)
                self.balance -= amount

        account = BankAccount(100)
        account.deposit(50)
        print(account.balance)  # 150

        try:
            account.withdraw(200)
        except InsufficientFundsError as e:
            print(e)  # Cannot withdraw $200: only $150 available
        ```

    The exception carries context (balance and amount) that helps with debugging and user feedback.

??? success "Solution to Exercise 3"

        ```python
        account = BankAccount(50)

        try:
            account.withdraw(100)
        except InsufficientFundsError as e:
            print(f"Specific: {e}")
        except BankError as e:
            print(f"General: {e}")
        ```

    The more specific exception must come first. If `BankError` were listed first, it would catch `InsufficientFundsError` (since it is a subclass), and the specific handler would never execute.
"""

# ============================================================================
# functions_params
# ============================================================================

EXERCISES["functions_params/best_practices.md"] = r"""
---

## Exercises

**Exercise 1.**
Rewrite the following function to follow best practices: use keyword-only arguments for configuration parameters and provide sensible defaults.

```python
def send_email(to, subject, body, cc, bcc, html, priority):
    pass
```

---

**Exercise 2.**
Write a function `create_user(name, *, email=None, role="viewer", active=True)` that returns a dictionary. The `*` forces `email`, `role`, and `active` to be keyword-only. Demonstrate calling it correctly and incorrectly.

---

**Exercise 3.**
Explain why using `*args` and `**kwargs` together can make APIs harder to understand. Write an example where explicit parameters are better than `**kwargs`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def send_email(to, subject, body, *, cc=None, bcc=None,
                       html=False, priority="normal"):
            print(f"To: {to}, Subject: {subject}")
            print(f"CC: {cc}, BCC: {bcc}, HTML: {html}, Priority: {priority}")

        send_email("alice@example.com", "Hello", "Body text")
        send_email("bob@example.com", "Urgent", "Body", priority="high", html=True)
        ```

    The `*` separator forces configuration parameters to be keyword-only, making calls self-documenting.

??? success "Solution to Exercise 2"

        ```python
        def create_user(name, *, email=None, role="viewer", active=True):
            return {"name": name, "email": email, "role": role, "active": active}

        # Correct usage
        user = create_user("Alice", email="alice@example.com", role="admin")
        print(user)

        # Incorrect usage
        try:
            create_user("Bob", "bob@example.com")  # Positional not allowed
        except TypeError as e:
            print(f"Error: {e}")
        ```

    Keyword-only arguments prevent positional mistakes and make the call site explicit.

??? success "Solution to Exercise 3"

        ```python
        # Hard to understand: what kwargs are valid?
        def configure(**kwargs):
            host = kwargs.get("host", "localhost")
            port = kwargs.get("port", 8080)
            debug = kwargs.get("debug", False)
            # Typos like "debugg=True" silently ignored!

        # Better: explicit parameters with defaults
        def configure(host="localhost", port=8080, debug=False):
            pass  # IDE can autocomplete, typos caught immediately

        # configure(debugg=True)  # TypeError: unexpected keyword argument
        ```

    Explicit parameters provide documentation, IDE support, and error checking for typos. Use `**kwargs` only when the set of valid keys is truly dynamic.
"""

EXERCISES["functions_params/call_by_object_reference.md"] = r"""
---

## Exercises

**Exercise 1.**
Predict the output without running the code. Then verify.

```python
def modify(lst, num):
    lst.append(4)
    num += 10

my_list = [1, 2, 3]
my_num = 5
modify(my_list, my_num)
print(my_list, my_num)
```

---

**Exercise 2.**
Write a function `double_values(d)` that takes a dictionary and doubles all its values in place. Demonstrate that the original dictionary is modified after the function call.

---

**Exercise 3.**
Explain the difference between rebinding and mutating inside a function. Write two functions: one that mutates a list (caller sees the change) and one that rebinds it (caller does not see the change).

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def modify(lst, num):
            lst.append(4)
            num += 10

        my_list = [1, 2, 3]
        my_num = 5
        modify(my_list, my_num)
        print(my_list, my_num)  # [1, 2, 3, 4] 5
        ```

    `lst.append(4)` mutates the original list (mutable object). `num += 10` rebinds the local name `num` to a new integer object (immutable), leaving `my_num` unchanged.

??? success "Solution to Exercise 2"

        ```python
        def double_values(d):
            for key in d:
                d[key] *= 2

        data = {"a": 1, "b": 2, "c": 3}
        double_values(data)
        print(data)  # {'a': 2, 'b': 4, 'c': 6}
        ```

    Dictionaries are mutable, so modifying values through the reference changes the original object.

??? success "Solution to Exercise 3"

        ```python
        def mutate(lst):
            lst.append(99)  # Mutates the object

        def rebind(lst):
            lst = [99]       # Rebinds local name only

        a = [1, 2, 3]
        mutate(a)
        print(a)  # [1, 2, 3, 99] (changed)

        b = [1, 2, 3]
        rebind(b)
        print(b)  # [1, 2, 3] (unchanged)
        ```

    Mutation changes the object itself (all references see the change). Rebinding creates a new local variable, leaving the original unaffected.
"""

EXERCISES["functions_params/default_parameter_gotcha.md"] = r"""
---

## Exercises

**Exercise 1.**
Explain why the following function has a bug. What happens when you call `add_item("a")` twice? Fix the function.

```python
def add_item(item, lst=[]):
    lst.append(item)
    return lst
```

---

**Exercise 2.**
Write a function `make_record(name, tags=None)` that creates a dictionary `{"name": name, "tags": tags}` where `tags` defaults to an empty list. Ensure that each call gets its own list.

---

**Exercise 3.**
Show that the default mutable argument is shared by examining the function's `__defaults__` attribute before and after calling the buggy function from Exercise 1.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # Buggy version
        def add_item_buggy(item, lst=[]):
            lst.append(item)
            return lst

        print(add_item_buggy("a"))  # ['a']
        print(add_item_buggy("b"))  # ['a', 'b'] (unexpected!)

        # Fixed version
        def add_item(item, lst=None):
            if lst is None:
                lst = []
            lst.append(item)
            return lst

        print(add_item("a"))  # ['a']
        print(add_item("b"))  # ['b']
        ```

    Default mutable arguments are created once when the function is defined, not on each call. Use `None` as the default and create the mutable object inside the function.

??? success "Solution to Exercise 2"

        ```python
        def make_record(name, tags=None):
            if tags is None:
                tags = []
            return {"name": name, "tags": tags}

        r1 = make_record("Alice")
        r2 = make_record("Bob")
        r1["tags"].append("admin")

        print(r1)  # {'name': 'Alice', 'tags': ['admin']}
        print(r2)  # {'name': 'Bob', 'tags': []} (independent)
        ```

    Each call creates a new empty list, so records do not share the same tags list.

??? success "Solution to Exercise 3"

        ```python
        def add_item(item, lst=[]):
            lst.append(item)
            return lst

        print(add_item.__defaults__)  # ([],)

        add_item("a")
        print(add_item.__defaults__)  # (['a'],)

        add_item("b")
        print(add_item.__defaults__)  # (['a', 'b'],)
        ```

    `__defaults__` reveals that the default list is a single object that accumulates changes across calls.
"""

EXERCISES["functions_params/parameter_mechanisms.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function that accepts positional-only parameters, keyword-only parameters, and a mix of both. Use the `/` and `*` separators. Demonstrate valid and invalid ways to call it.

---

**Exercise 2.**
Write a function `tag(name, /, *children, **attrs)` that builds an HTML-like tag string. For example, `tag("div", "hello", "world", id="main")` should return `'<div id="main">helloworld</div>'`.

---

**Exercise 3.**
Explain the difference between `*args` and `**kwargs`. Write a function `debug_call(func, *args, **kwargs)` that prints the function name, positional arguments, and keyword arguments, then calls the function.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def example(a, b, /, c, *, d, e=10):
            print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

        example(1, 2, 3, d=4)         # Valid
        example(1, 2, c=3, d=4, e=5)  # Valid

        # example(a=1, b=2, c=3, d=4)  # TypeError: positional-only
        # example(1, 2, 3, 4)           # TypeError: d is keyword-only
        ```

    `a` and `b` are positional-only (before `/`). `d` and `e` are keyword-only (after `*`). `c` can be either.

??? success "Solution to Exercise 2"

        ```python
        def tag(name, /, *children, **attrs):
            attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
            opening = f"<{name} {attr_str}>" if attrs else f"<{name}>"
            content = "".join(str(c) for c in children)
            return f"{opening}{content}</{name}>"

        print(tag("div", "hello", "world", id="main"))
        # <div id="main">helloworld</div>

        print(tag("br"))
        # <br></br>
        ```

    `name` is positional-only, `*children` collects content, and `**attrs` collects HTML attributes.

??? success "Solution to Exercise 3"

        ```python
        def debug_call(func, *args, **kwargs):
            print(f"Calling: {func.__name__}")
            print(f"  args: {args}")
            print(f"  kwargs: {kwargs}")
            return func(*args, **kwargs)

        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        result = debug_call(greet, "Alice", greeting="Hi")
        print(f"  result: {result}")
        ```

    `*args` captures extra positional arguments as a tuple. `**kwargs` captures extra keyword arguments as a dictionary.
"""

EXERCISES["functions_params/parameter_passing.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `swap(a, b)` that attempts to swap two integers. Explain why the swap is not visible to the caller. Then write a version using a list to achieve a visible swap.

---

**Exercise 2.**
Write a function `extend_and_return(lst, items)` that extends `lst` with `items` and returns the modified list. Show that the caller's list is also modified. Then write a version that does not modify the original.

---

**Exercise 3.**
Given `def f(x): x = x + [4]` and `def g(x): x += [4]`, explain why `f` and `g` behave differently when passed a list. Demonstrate with code.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def swap(a, b):
            a, b = b, a  # Only swaps local names

        x, y = 1, 2
        swap(x, y)
        print(x, y)  # 1 2 (unchanged)

        # Visible swap using a list
        def swap_list(pair):
            pair[0], pair[1] = pair[1], pair[0]

        pair = [1, 2]
        swap_list(pair)
        print(pair)  # [2, 1]
        ```

    Integers are immutable. `swap` only rebinds local names. The list version works because it mutates the mutable container.

??? success "Solution to Exercise 2"

        ```python
        # Modifies original
        def extend_and_return(lst, items):
            lst.extend(items)
            return lst

        a = [1, 2]
        b = extend_and_return(a, [3, 4])
        print(a)  # [1, 2, 3, 4] (modified)

        # Does not modify original
        def extend_copy(lst, items):
            return lst + items

        c = [1, 2]
        d = extend_copy(c, [3, 4])
        print(c)  # [1, 2] (unchanged)
        print(d)  # [1, 2, 3, 4]
        ```

    `lst.extend(items)` mutates the list. `lst + items` creates a new list.

??? success "Solution to Exercise 3"

        ```python
        def f(x):
            x = x + [4]  # Rebinds x to new list

        def g(x):
            x += [4]     # Calls x.__iadd__([4]) -> mutates in place

        a = [1, 2, 3]
        f(a)
        print(a)  # [1, 2, 3] (unchanged)

        b = [1, 2, 3]
        g(b)
        print(b)  # [1, 2, 3, 4] (modified)
        ```

    `x = x + [4]` creates a new list and rebinds the local `x`. `x += [4]` calls `list.__iadd__`, which extends the list in place.
"""

EXERCISES["functions_params/review.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a function `describe(name, /, *, age, city="Unknown")` and show examples of valid and invalid calls.

---

**Exercise 2.**
Write a function `merge_defaults(user_config, **defaults)` that returns a dictionary with `defaults` overridden by `user_config`. The function should not modify either input.

---

**Exercise 3.**
What is the output of the following code? Explain each step.

```python
def f(a, b=[], c=None):
    if c is None:
        c = []
    b.append(a)
    c.append(a)
    return b, c

print(f(1))
print(f(2))
print(f(3))
```

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def describe(name, /, *, age, city="Unknown"):
            return f"{name}, age {age}, from {city}"

        print(describe("Alice", age=30))              # Valid
        print(describe("Bob", age=25, city="Seoul"))   # Valid

        # describe(name="Alice", age=30)  # TypeError: positional-only
        # describe("Alice", 30)           # TypeError: keyword-only
        ```

    `name` is positional-only (before `/`). `age` and `city` are keyword-only (after `*`).

??? success "Solution to Exercise 2"

        ```python
        def merge_defaults(user_config, **defaults):
            result = dict(defaults)
            result.update(user_config)
            return result

        config = merge_defaults(
            {"debug": True},
            host="localhost", port=8080, debug=False
        )
        print(config)  # {'host': 'localhost', 'port': 8080, 'debug': True}
        ```

    Starting with `defaults` and updating with `user_config` ensures user values take priority.

??? success "Solution to Exercise 3"

        ```python
        print(f(1))  # ([1], [1])
        print(f(2))  # ([1, 2], [2])
        print(f(3))  # ([1, 2, 3], [3])
        ```

    `b` is a mutable default that persists across calls, accumulating values. `c` defaults to `None` and gets a fresh list each call, so it only contains the current value. This is the classic mutable default argument gotcha.
"""

# ============================================================================
# io
# ============================================================================

EXERCISES["io/binary_files.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a script that creates a binary file containing the bytes `b'\x00\x01\x02\x03'`, then reads it back and prints each byte as a hexadecimal value.

---

**Exercise 2.**
Write a function `copy_file(src, dst)` that copies a binary file from `src` to `dst` by reading and writing in 4096-byte chunks. Use `"rb"` and `"wb"` modes.

---

**Exercise 3.**
Use the `struct` module to write two integers (42 and 100) to a binary file in little-endian format, then read them back and print them.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # Write binary file
        with open("/tmp/test.bin", "wb") as f:
            f.write(b'\x00\x01\x02\x03')

        # Read and print hex values
        with open("/tmp/test.bin", "rb") as f:
            data = f.read()
            for byte in data:
                print(f"0x{byte:02x}", end=" ")
        # 0x00 0x01 0x02 0x03
        ```

    Binary mode (`"rb"`, `"wb"`) reads/writes raw bytes without text encoding.

??? success "Solution to Exercise 2"

        ```python
        def copy_file(src, dst, chunk_size=4096):
            with open(src, "rb") as fin, open(dst, "wb") as fout:
                while True:
                    chunk = fin.read(chunk_size)
                    if not chunk:
                        break
                    fout.write(chunk)
        ```

    Reading in chunks avoids loading the entire file into memory, making this suitable for large files.

??? success "Solution to Exercise 3"

        ```python
        import struct

        # Write
        with open("/tmp/ints.bin", "wb") as f:
            f.write(struct.pack("<ii", 42, 100))

        # Read
        with open("/tmp/ints.bin", "rb") as f:
            data = f.read()
            a, b = struct.unpack("<ii", data)
            print(a, b)  # 42 100
        ```

    `"<ii"` means little-endian (`<`) with two signed integers (`i`). `struct.pack` converts to bytes and `struct.unpack` converts back.
"""

EXERCISES["io/encoding_issues.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a script that writes the string `"Hello, world!"` to a file using UTF-8 encoding, then tries to read it back using ASCII encoding. What happens? Handle the error gracefully.

---

**Exercise 2.**
Write a function `detect_encoding(filepath)` that reads the first 100 bytes of a file and returns `"utf-8"` if they decode successfully as UTF-8, or `"unknown"` otherwise.

---

**Exercise 3.**
Demonstrate the difference between `errors="ignore"`, `errors="replace"`, and `errors="strict"` when decoding bytes that contain invalid UTF-8 sequences.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        with open("/tmp/test.txt", "w", encoding="utf-8") as f:
            f.write("Hello, \u4e16\u754c!")  # Hello, 世界!

        try:
            with open("/tmp/test.txt", "r", encoding="ascii") as f:
                content = f.read()
        except UnicodeDecodeError as e:
            print(f"Error: {e}")

        # Read correctly with UTF-8
        with open("/tmp/test.txt", "r", encoding="utf-8") as f:
            print(f.read())  # Hello, 世界!
        ```

    ASCII cannot decode multi-byte UTF-8 characters, raising `UnicodeDecodeError`.

??? success "Solution to Exercise 2"

        ```python
        def detect_encoding(filepath):
            with open(filepath, "rb") as f:
                raw = f.read(100)
            try:
                raw.decode("utf-8")
                return "utf-8"
            except UnicodeDecodeError:
                return "unknown"
        ```

    This is a simple heuristic. For production use, consider the `chardet` library for more reliable detection.

??? success "Solution to Exercise 3"

        ```python
        data = b"Hello \xff\xfe World"

        print(data.decode("utf-8", errors="ignore"))   # Hello  World
        print(data.decode("utf-8", errors="replace"))  # Hello �� World
        try:
            data.decode("utf-8", errors="strict")
        except UnicodeDecodeError as e:
            print(f"strict: {e}")
        ```

    `"ignore"` silently skips invalid bytes. `"replace"` inserts replacement characters. `"strict"` (the default) raises an exception.
"""

EXERCISES["io/pickle.md"] = r"""
---

## Exercises

**Exercise 1.**
Use `pickle` to serialize and deserialize a Python dictionary containing a list, a tuple, and a nested dictionary. Verify that the deserialized object equals the original.

---

**Exercise 2.**
Explain why unpickling data from an untrusted source is a security risk. Write a short example showing how `pickle.loads` can execute arbitrary code.

---

**Exercise 3.**
Compare `pickle` with `json` for serializing `{"name": "Alice", "scores": [95, 87, 92]}`. What are the advantages of each format?

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import pickle

        data = {
            "list": [1, 2, 3],
            "tuple": (4, 5, 6),
            "nested": {"a": 1, "b": 2}
        }

        serialized = pickle.dumps(data)
        restored = pickle.loads(serialized)

        print(restored == data)  # True
        print(type(restored["tuple"]))  # <class 'tuple'>
        ```

    Pickle preserves Python types exactly, including tuples (which JSON would convert to lists).

??? success "Solution to Exercise 2"

    Never unpickle untrusted data. A malicious pickle can execute arbitrary code:

        ```python
        import pickle
        import os

        # This is DANGEROUS - for educational purposes only
        class Exploit:
            def __reduce__(self):
                return (os.system, ("echo 'compromised'",))

        payload = pickle.dumps(Exploit())
        # pickle.loads(payload)  # Would execute os.system("echo 'compromised'")
        ```

    The `__reduce__` method tells pickle how to reconstruct the object. A malicious implementation can specify any callable, including `os.system`. Always use `json` for untrusted data.

??? success "Solution to Exercise 3"

        ```python
        import pickle
        import json

        data = {"name": "Alice", "scores": [95, 87, 92]}

        # Pickle
        p = pickle.dumps(data)
        print(f"Pickle size: {len(p)} bytes")

        # JSON
        j = json.dumps(data)
        print(f"JSON size: {len(j)} bytes")
        print(f"JSON: {j}")
        ```

    **Pickle advantages**: preserves all Python types, handles circular references.
    **JSON advantages**: human-readable, language-agnostic, safe to load from untrusted sources.
"""

EXERCISES["io/shelve.md"] = r"""
---

## Exercises

**Exercise 1.**
Use `shelve` to create a persistent key-value store. Store three records with string keys and dictionary values. Close the shelf, reopen it, and verify the data persists.

---

**Exercise 2.**
Demonstrate the writeback problem: open a shelf without `writeback=True`, modify a mutable value, and show that the change is lost. Then fix it using `writeback=True`.

---

**Exercise 3.**
Write a simple address book using `shelve` with functions `add_contact(name, phone)`, `get_contact(name)`, and `list_contacts()`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import shelve

        with shelve.open("/tmp/mydata") as db:
            db["alice"] = {"age": 30, "city": "Seoul"}
            db["bob"] = {"age": 25, "city": "Tokyo"}
            db["carol"] = {"age": 35, "city": "NYC"}

        with shelve.open("/tmp/mydata") as db:
            print(db["alice"])  # {'age': 30, 'city': 'Seoul'}
            print(list(db.keys()))  # ['alice', 'bob', 'carol']
        ```

    `shelve` provides a dictionary-like interface to persistent storage. Data survives between program runs.

??? success "Solution to Exercise 2"

        ```python
        import shelve

        # Without writeback - changes lost
        with shelve.open("/tmp/test_shelf") as db:
            db["data"] = [1, 2, 3]

        with shelve.open("/tmp/test_shelf") as db:
            db["data"].append(4)  # Modifies a temporary copy

        with shelve.open("/tmp/test_shelf") as db:
            print(db["data"])  # [1, 2, 3] - append was lost!

        # With writeback - changes preserved
        with shelve.open("/tmp/test_shelf", writeback=True) as db:
            db["data"].append(4)

        with shelve.open("/tmp/test_shelf") as db:
            print(db["data"])  # [1, 2, 3, 4]
        ```

    Without `writeback=True`, accessing `db["data"]` returns a deserialized copy. Mutations to this copy are not automatically saved back.

??? success "Solution to Exercise 3"

        ```python
        import shelve

        DB_PATH = "/tmp/addressbook"

        def add_contact(name, phone):
            with shelve.open(DB_PATH) as db:
                db[name] = phone

        def get_contact(name):
            with shelve.open(DB_PATH) as db:
                return db.get(name, "Not found")

        def list_contacts():
            with shelve.open(DB_PATH) as db:
                return dict(db)

        add_contact("Alice", "555-1234")
        add_contact("Bob", "555-5678")
        print(get_contact("Alice"))   # 555-1234
        print(list_contacts())        # {'Alice': '555-1234', 'Bob': '555-5678'}
        ```
"""

EXERCISES["io/string_bytes_io.md"] = r"""
---

## Exercises

**Exercise 1.**
Use `io.StringIO` to capture the output of multiple `print()` calls into a single string. Print the combined result.

---

**Exercise 2.**
Write a function that takes a CSV string (e.g., `"name,age\nAlice,30\nBob,25"`) and uses `io.StringIO` with the `csv` module to parse it into a list of dictionaries.

---

**Exercise 3.**
Demonstrate the difference between `io.StringIO` (works with `str`) and `io.BytesIO` (works with `bytes`). Show that writing bytes to `StringIO` raises an error and vice versa.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import io

        buffer = io.StringIO()
        print("Hello", file=buffer)
        print("World", file=buffer)
        print("Python", file=buffer)

        result = buffer.getvalue()
        print(result)
        # Hello
        # World
        # Python
        ```

    `io.StringIO` acts as an in-memory text file. `print()` with `file=buffer` writes to it instead of stdout.

??? success "Solution to Exercise 2"

        ```python
        import io
        import csv

        def parse_csv(csv_string):
            reader = csv.DictReader(io.StringIO(csv_string))
            return list(reader)

        data = "name,age\nAlice,30\nBob,25"
        records = parse_csv(data)
        print(records)
        # [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
        ```

    `io.StringIO` wraps the string as a file-like object that `csv.DictReader` can consume.

??? success "Solution to Exercise 3"

        ```python
        import io

        # StringIO works with str
        s = io.StringIO()
        s.write("hello")
        try:
            s.write(b"bytes")
        except TypeError as e:
            print(f"StringIO error: {e}")

        # BytesIO works with bytes
        b = io.BytesIO()
        b.write(b"hello")
        try:
            b.write("text")
        except TypeError as e:
            print(f"BytesIO error: {e}")
        ```

    `StringIO` accepts only `str`, and `BytesIO` accepts only `bytes`. Mixing them raises `TypeError`.
"""

EXERCISES["io/tempfile.md"] = r"""
---

## Exercises

**Exercise 1.**
Use `tempfile.NamedTemporaryFile` to create a temporary file, write some data to it, read it back, and print the temporary file's path. Show that the file is deleted after the `with` block.

---

**Exercise 2.**
Use `tempfile.mkdtemp()` to create a temporary directory, create a file inside it, and then clean up using `shutil.rmtree()`.

---

**Exercise 3.**
Explain the difference between `tempfile.TemporaryFile` and `tempfile.NamedTemporaryFile`. When would you use each?

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=True) as f:
            f.write("temporary data")
            f.flush()
            print(f"Temp file: {f.name}")
            print(f"Exists: {os.path.exists(f.name)}")  # True

        print(f"Exists after: {os.path.exists(f.name)}")  # False
        ```

    `NamedTemporaryFile` provides a visible file path and automatic cleanup when the context manager exits.

??? success "Solution to Exercise 2"

        ```python
        import tempfile
        import shutil
        import os

        tmpdir = tempfile.mkdtemp()
        filepath = os.path.join(tmpdir, "data.txt")

        with open(filepath, "w") as f:
            f.write("hello")

        print(os.listdir(tmpdir))  # ['data.txt']

        shutil.rmtree(tmpdir)
        print(os.path.exists(tmpdir))  # False
        ```

    `mkdtemp()` creates the directory but does not clean it up automatically. Use `shutil.rmtree()` for cleanup.

??? success "Solution to Exercise 3"

    `TemporaryFile` creates an anonymous temporary file with no visible name in the filesystem (on Unix). It cannot be accessed by other processes. `NamedTemporaryFile` creates a file with a visible name that can be passed to other processes.

        ```python
        import tempfile

        # No visible name (Unix)
        with tempfile.TemporaryFile(mode="w") as f:
            f.write("anonymous")
            # f.name exists but may not be accessible on disk

        # Visible name
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            print(f.name)  # /tmp/tmpXXXXXX
        ```

    Use `TemporaryFile` when no other process needs to access the file. Use `NamedTemporaryFile` when you need to pass the path to external tools.
"""

# ============================================================================
# iteration
# ============================================================================

EXERCISES["iteration/generators.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a generator function `fibonacci(n)` that yields the first `n` Fibonacci numbers. Test it by printing the first 10.

---

**Exercise 2.**
Write a generator function `chunks(lst, size)` that yields successive chunks of `size` elements from `lst`. For example, `list(chunks([1,2,3,4,5], 2))` should return `[[1,2], [3,4], [5]]`.

---

**Exercise 3.**
Explain the memory advantage of generators over lists. Write a comparison that shows `sum(range(10_000_000))` uses much less memory than `sum(list(range(10_000_000)))` using `sys.getsizeof`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def fibonacci(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b

        print(list(fibonacci(10)))
        # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        ```

    The generator yields one value at a time, keeping only `a` and `b` in memory regardless of `n`.

??? success "Solution to Exercise 2"

        ```python
        def chunks(lst, size):
            for i in range(0, len(lst), size):
                yield lst[i:i + size]

        print(list(chunks([1, 2, 3, 4, 5], 2)))
        # [[1, 2], [3, 4], [5]]
        ```

    `range(0, len(lst), size)` steps through the list in increments of `size`.

??? success "Solution to Exercise 3"

        ```python
        import sys

        r = range(10_000_000)
        l = list(range(10_000_000))

        print(f"range size: {sys.getsizeof(r)} bytes")     # ~48 bytes
        print(f"list size: {sys.getsizeof(l)} bytes")       # ~80,000,000 bytes

        # Both produce the same sum
        print(sum(range(10_000_000)) == sum(list(range(10_000_000))))  # True
        ```

    `range` (like a generator) produces values on demand, using constant memory. The list materializes all 10 million integers in memory.
"""

EXERCISES["iteration/iterables.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a class `Countdown` that implements the iterator protocol (`__iter__` and `__next__`). It should count down from a given number to 1.

---

**Exercise 2.**
Show that a list is iterable but not an iterator. Demonstrate by calling `iter()` on it to get an iterator, then calling `next()` on the iterator.

---

**Exercise 3.**
Write a function `is_iterable(obj)` that returns `True` if `obj` is iterable and `False` otherwise. Test it with a list, an integer, a string, and a generator.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        class Countdown:
            def __init__(self, start):
                self.current = start

            def __iter__(self):
                return self

            def __next__(self):
                if self.current < 1:
                    raise StopIteration
                value = self.current
                self.current -= 1
                return value

        for n in Countdown(5):
            print(n, end=" ")
        # 5 4 3 2 1
        ```

    `__iter__` returns the iterator (itself), and `__next__` returns the next value or raises `StopIteration`.

??? success "Solution to Exercise 2"

        ```python
        lst = [1, 2, 3]

        # List is iterable but not an iterator
        print(hasattr(lst, "__iter__"))    # True
        print(hasattr(lst, "__next__"))    # False

        # Get an iterator from the list
        it = iter(lst)
        print(hasattr(it, "__next__"))     # True
        print(next(it))  # 1
        print(next(it))  # 2
        print(next(it))  # 3
        ```

    An iterable has `__iter__`. An iterator has both `__iter__` and `__next__`. `iter()` converts an iterable to an iterator.

??? success "Solution to Exercise 3"

        ```python
        def is_iterable(obj):
            try:
                iter(obj)
                return True
            except TypeError:
                return False

        print(is_iterable([1, 2]))       # True
        print(is_iterable(42))           # False
        print(is_iterable("hello"))      # True
        print(is_iterable(x for x in []))  # True
        ```

    Using `try`/`except` with `iter()` is the most reliable way to check iterability, following the EAFP (Easier to Ask Forgiveness than Permission) principle.
"""

EXERCISES["iteration/iterator_chaining.md"] = r"""
---

## Exercises

**Exercise 1.**
Use `itertools.chain` to combine three lists `[1, 2]`, `[3, 4]`, `[5, 6]` into a single iterable and print all elements.

---

**Exercise 2.**
Use `itertools.islice` to get elements 5 through 10 from an infinite counter created with `itertools.count`.

---

**Exercise 3.**
Write a pipeline using `map`, `filter`, and `itertools.chain` that takes multiple lists of numbers, combines them, filters out negatives, and squares the remaining values.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        from itertools import chain

        result = list(chain([1, 2], [3, 4], [5, 6]))
        print(result)  # [1, 2, 3, 4, 5, 6]
        ```

    `chain` lazily concatenates iterables without creating intermediate lists.

??? success "Solution to Exercise 2"

        ```python
        from itertools import count, islice

        result = list(islice(count(0), 5, 11))
        print(result)  # [5, 6, 7, 8, 9, 10]
        ```

    `count(0)` generates 0, 1, 2, ... infinitely. `islice` selects a range without materializing the entire sequence.

??? success "Solution to Exercise 3"

        ```python
        from itertools import chain

        lists = [[-1, 2, 3], [4, -5, 6], [-7, 8]]

        result = list(
            map(lambda x: x ** 2,
                filter(lambda x: x >= 0,
                       chain(*lists)))
        )
        print(result)  # [4, 9, 16, 36, 64]
        ```

    The pipeline processes lazily: `chain` combines, `filter` removes negatives, `map` squares -- all without intermediate lists.
"""

EXERCISES["iteration/lazy_evaluation.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a generator `infinite_squares()` that yields 1, 4, 9, 16, ... (squares of natural numbers) indefinitely. Use `itertools.islice` to get the first 10 squares.

---

**Exercise 2.**
Demonstrate lazy evaluation by writing a generator that prints a message each time it yields a value. Show that values are produced one at a time, not all at once.

---

**Exercise 3.**
Write a function `first_match(predicate, iterable)` that returns the first element for which `predicate` returns `True`, or `None` if no match is found. Use lazy evaluation to avoid processing the entire iterable.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        from itertools import islice

        def infinite_squares():
            n = 1
            while True:
                yield n * n
                n += 1

        print(list(islice(infinite_squares(), 10)))
        # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        ```

    The generator produces squares indefinitely. `islice` takes only the first 10 without running forever.

??? success "Solution to Exercise 2"

        ```python
        def verbose_range(n):
            for i in range(n):
                print(f"  Yielding {i}")
                yield i

        print("Creating generator:")
        gen = verbose_range(5)
        print("No output yet -- lazy!")

        print("Taking first 3:")
        for i, val in enumerate(gen):
            if i >= 3:
                break
            print(f"  Got {val}")
        ```

    Messages appear only when values are consumed, proving that the generator does not execute ahead of time.

??? success "Solution to Exercise 3"

        ```python
        def first_match(predicate, iterable):
            for item in iterable:
                if predicate(item):
                    return item
            return None

        result = first_match(lambda x: x > 100, range(1_000_000))
        print(result)  # 101
        ```

    The function returns immediately upon finding a match. It does not process the remaining 999,898 elements.
"""

EXERCISES["iteration/stopiteration.md"] = r"""
---

## Exercises

**Exercise 1.**
Write an iterator class `RepeatN` that yields a given value exactly `n` times, then raises `StopIteration`.

---

**Exercise 2.**
Show what happens when you call `next()` on an exhausted iterator. Demonstrate using both an explicit `next()` call and a `for` loop (which handles `StopIteration` automatically).

---

**Exercise 3.**
Write a function `take(n, iterable)` that returns a list of the first `n` elements from an iterable. Handle the case where the iterable has fewer than `n` elements.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        class RepeatN:
            def __init__(self, value, n):
                self.value = value
                self.n = n
                self.count = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.count >= self.n:
                    raise StopIteration
                self.count += 1
                return self.value

        print(list(RepeatN("hello", 3)))  # ['hello', 'hello', 'hello']
        ```

    `StopIteration` signals that the iterator has no more values. The `for` loop and `list()` catch it automatically.

??? success "Solution to Exercise 2"

        ```python
        it = iter([1, 2])

        print(next(it))  # 1
        print(next(it))  # 2

        try:
            next(it)  # StopIteration
        except StopIteration:
            print("Iterator exhausted")

        # for loop handles it silently
        for val in iter([1, 2]):
            print(val)
        # 1
        # 2
        # (no error)
        ```

    `next()` raises `StopIteration` on an exhausted iterator. `for` loops catch it internally as the signal to stop.

??? success "Solution to Exercise 3"

        ```python
        def take(n, iterable):
            result = []
            for i, item in enumerate(iterable):
                if i >= n:
                    break
                result.append(item)
            return result

        print(take(3, range(10)))      # [0, 1, 2]
        print(take(5, [1, 2]))         # [1, 2] (fewer than 5)
        print(take(3, (x*x for x in range(100))))  # [0, 1, 4]
        ```

    The function stops at `n` elements or when the iterable is exhausted, whichever comes first.
"""

EXERCISES["iteration/yield_from.md"] = r"""
---

## Exercises

**Exercise 1.**
Write a generator `flatten(nested)` that uses `yield from` to flatten a list of lists. For example, `list(flatten([[1,2],[3,4],[5]]))` should return `[1,2,3,4,5]`.

---

**Exercise 2.**
Write two generators: `evens(n)` yields even numbers up to `n`, and `odds(n)` yields odd numbers up to `n`. Then write a generator `all_numbers(n)` that uses `yield from` to combine both.

---

**Exercise 3.**
Explain the difference between `yield from iterable` and looping with `for item in iterable: yield item`. Are they always equivalent?

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        def flatten(nested):
            for sublist in nested:
                yield from sublist

        print(list(flatten([[1, 2], [3, 4], [5]])))
        # [1, 2, 3, 4, 5]
        ```

    `yield from sublist` delegates iteration to the sublist, yielding each element directly.

??? success "Solution to Exercise 2"

        ```python
        def evens(n):
            for i in range(0, n + 1, 2):
                yield i

        def odds(n):
            for i in range(1, n + 1, 2):
                yield i

        def all_numbers(n):
            yield from evens(n)
            yield from odds(n)

        print(list(all_numbers(6)))
        # [0, 2, 4, 6, 1, 3, 5]
        ```

    `yield from` delegates to each sub-generator in sequence.

??? success "Solution to Exercise 3"

    For simple iteration, they are equivalent:

        ```python
        # These produce identical output
        def gen1(iterable):
            yield from iterable

        def gen2(iterable):
            for item in iterable:
                yield item
        ```

    However, `yield from` also handles `.send()`, `.throw()`, and `.close()` by forwarding them to the sub-generator. The `for` loop version does not propagate these methods. For coroutine-style generators, `yield from` is essential.
"""

# ============================================================================
# naming
# ============================================================================

EXERCISES["naming/bad_practices.md"] = r"""
---

## Exercises

**Exercise 1.**
Identify three naming problems in the following code and fix them.

```python
l = [1, 2, 3]
str = "hello"
def f(x):
    O = x + 1
    return O
```

---

**Exercise 2.**
Explain why using `list`, `dict`, `str`, `type`, or `id` as variable names is dangerous. Write a code example that breaks because of shadowing a built-in.

---

**Exercise 3.**
Rewrite the following code with descriptive variable names.

```python
def p(d, r, t):
    return d * (1 + r) ** t
```

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # Fixed version
        numbers = [1, 2, 3]           # 'l' looks like '1'
        greeting = "hello"             # 'str' shadows built-in
        def increment(value):          # 'f' is not descriptive
            result = value + 1         # 'O' looks like '0'
            return result
        ```

    Avoid single-letter names that look like digits (`l`, `O`), shadowing built-ins (`str`), and non-descriptive function names (`f`).

??? success "Solution to Exercise 2"

        ```python
        list = [1, 2, 3]

        try:
            new_list = list("hello")
        except TypeError as e:
            print(f"Error: {e}")  # 'list' object is not callable

        del list  # Restore built-in
        print(list("hello"))  # ['h', 'e', 'l', 'l', 'o']
        ```

    Shadowing built-ins makes them inaccessible in the current scope, causing confusing errors.

??? success "Solution to Exercise 3"

        ```python
        def compound_interest(principal, annual_rate, years):
            return principal * (1 + annual_rate) ** years

        print(compound_interest(1000, 0.05, 10))  # 1628.89...
        ```

    Descriptive names make the formula self-documenting without needing comments.
"""

EXERCISES["naming/builtins.md"] = r"""
---

## Exercises

**Exercise 1.**
List five commonly shadowed built-in names. For each, suggest a better alternative variable name.

---

**Exercise 2.**
Write a function that accidentally shadows `input` inside its body. Show the resulting error, then fix it.

---

**Exercise 3.**
Use `dir(builtins)` to count how many built-in names there are in Python. Filter to show only the ones that are commonly used as variable names by beginners.

---

## Solutions

??? success "Solution to Exercise 1"

    | Built-in | Common misuse | Better name |
    |----------|---------------|-------------|
    | `list` | `list = [...]` | `items`, `values`, `data` |
    | `dict` | `dict = {...}` | `mapping`, `config`, `record` |
    | `str` | `str = "..."` | `text`, `name`, `message` |
    | `type` | `type = "admin"` | `kind`, `category`, `role` |
    | `id` | `id = 42` | `user_id`, `item_id`, `identifier` |

??? success "Solution to Exercise 2"

        ```python
        # Buggy version
        def get_name():
            input = "default"       # Shadows built-in input()
            name = input("Name: ")  # TypeError!
            return name

        # Fixed version
        def get_name():
            default_name = "default"
            name = input("Name: ")
            return name or default_name
        ```

    Once `input` is reassigned to a string, calling `input()` tries to call the string, raising `TypeError`.

??? success "Solution to Exercise 3"

        ```python
        import builtins

        all_builtins = dir(builtins)
        print(f"Total built-in names: {len(all_builtins)}")

        # Commonly misused as variable names
        common = {"list", "dict", "str", "int", "float", "type", "id",
                  "input", "print", "len", "max", "min", "sum", "set",
                  "map", "filter", "range", "open", "format", "hash"}

        found = [name for name in all_builtins if name in common]
        print(f"Commonly shadowed: {sorted(found)}")
        ```
"""

EXERCISES["naming/keywords.md"] = r"""
---

## Exercises

**Exercise 1.**
Write code that lists all Python keywords using the `keyword` module. How many are there in your Python version?

---

**Exercise 2.**
What happens when you try to use `class`, `return`, or `for` as a variable name? Demonstrate the error.

---

**Exercise 3.**
Some words that look like keywords are actually built-in names (e.g., `True`, `False`, `None`). Verify which of these are keywords using `keyword.iskeyword()` and which are just built-in constants.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        import keyword

        print(keyword.kwlist)
        print(f"Total keywords: {len(keyword.kwlist)}")
        ```

    Python 3.12 has 35 keywords. The exact number may vary by version.

??? success "Solution to Exercise 2"

        ```python
        # All of these cause SyntaxError:
        # class = 5
        # return = 10
        # for = "hello"

        # SyntaxError: invalid syntax
        ```

    Keywords are reserved by the parser. Using them as identifiers causes `SyntaxError` at compile time.

??? success "Solution to Exercise 3"

        ```python
        import keyword

        for name in ["True", "False", "None", "print", "len"]:
            is_kw = keyword.iskeyword(name)
            print(f"{name:>6}: keyword={is_kw}")
        ```

    `True`, `False`, and `None` are keywords (since Python 3). `print` and `len` are built-in names, not keywords -- they can be reassigned (though doing so is not recommended).
"""

EXERCISES["naming/naming_constraints.md"] = r"""
---

## Exercises

**Exercise 1.**
Which of the following are valid Python identifiers? Test each with `str.isidentifier()`.

```python
names = ["my_var", "2things", "_private", "__dunder__", "class", "my-var", "café"]
```

---

**Exercise 2.**
Explain the rules for valid Python identifiers: what characters can they start with, and what characters can follow?

---

**Exercise 3.**
Write a function `sanitize_name(s)` that converts an arbitrary string into a valid Python identifier by replacing invalid characters with underscores and prepending `_` if it starts with a digit.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        names = ["my_var", "2things", "_private", "__dunder__", "class", "my-var", "café"]

        for name in names:
            print(f"{name:>12}: {name.isidentifier()}")
        ```

    `my_var`, `_private`, `__dunder__`, `class`, and `café` are valid identifiers. `2things` (starts with digit) and `my-var` (contains hyphen) are not. Note that `class` is a valid identifier but is a reserved keyword.

??? success "Solution to Exercise 2"

    Python identifiers must:

    - Start with a letter (a-z, A-Z) or underscore (`_`)
    - Followed by zero or more letters, digits (0-9), or underscores
    - Not be a keyword (though `isidentifier()` returns `True` for keywords)
    - Unicode letters are allowed (e.g., `café`, `变量`)

??? success "Solution to Exercise 3"

        ```python
        import keyword

        def sanitize_name(s):
            result = ""
            for i, ch in enumerate(s):
                if i == 0 and ch.isdigit():
                    result += "_" + ch
                elif ch.isalnum() or ch == "_":
                    result += ch
                else:
                    result += "_"
            if not result:
                result = "_"
            if keyword.iskeyword(result):
                result += "_"
            return result

        print(sanitize_name("2things"))    # _2things
        print(sanitize_name("my-var"))     # my_var
        print(sanitize_name("class"))      # class_
        ```
"""

EXERCISES["naming/underscore_convention.md"] = r"""
---

## Exercises

**Exercise 1.**
Explain the meaning of each underscore convention: `_var`, `var_`, `__var`, `__var__`, and `_`. Give an example use case for each.

---

**Exercise 2.**
Demonstrate Python's name mangling for `__var` inside a class. Create a class with a `__secret` attribute and show how to access it from outside the class.

---

**Exercise 3.**
Write a loop that uses `_` as a throwaway variable and a function that uses `_` in the interactive interpreter convention.

---

## Solutions

??? success "Solution to Exercise 1"

    | Convention | Meaning | Example |
    |-----------|---------|---------|
    | `_var` | Internal/private by convention | `_helper_function()` |
    | `var_` | Avoids conflict with keyword | `class_`, `type_` |
    | `__var` | Name mangling in classes | `self.__balance` |
    | `__var__` | Dunder/magic methods | `__init__`, `__str__` |
    | `_` | Throwaway variable | `for _ in range(5)` |

??? success "Solution to Exercise 2"

        ```python
        class BankAccount:
            def __init__(self, balance):
                self.__balance = balance  # Name-mangled

            def get_balance(self):
                return self.__balance

        acc = BankAccount(100)
        # print(acc.__balance)           # AttributeError
        print(acc._BankAccount__balance)  # 100 (mangled name)
        print(acc.get_balance())          # 100
        ```

    Python mangles `__balance` to `_BankAccount__balance` to avoid accidental overrides in subclasses.

??? success "Solution to Exercise 3"

        ```python
        # Throwaway variable in loop
        for _ in range(3):
            print("Hello")

        # Ignoring values in unpacking
        name, _, age = ("Alice", "ignored", 30)
        print(f"{name}, {age}")  # Alice, 30
        ```

    `_` signals to readers that the value is intentionally unused.
"""

EXERCISES["naming/unicode_identifiers.md"] = r"""
---

## Exercises

**Exercise 1.**
Create variables using non-ASCII Unicode names (e.g., Greek letters, CJK characters). Verify they work as expected.

---

**Exercise 2.**
Explain why using Unicode identifiers can be both useful and problematic. Give one good use case and one potential pitfall.

---

**Exercise 3.**
Test whether emoji characters are valid Python identifiers using `str.isidentifier()`.

---

## Solutions

??? success "Solution to Exercise 1"

        ```python
        # Greek letters for math
        pi = 3.14159

        # CJK characters
        name = "Python"

        print(pi)
        print(name)
        ```

    Python 3 supports Unicode identifiers, allowing mathematical notation and localized variable names.

??? success "Solution to Exercise 2"

    **Good use case**: Mathematical code where Greek letters match the formulas:

        ```python
        delta = x1 - x0
        ```

    **Pitfall**: Team members may not be able to type the characters, and visually similar characters (e.g., Latin `a` vs Cyrillic `a`) can create confusing bugs.

??? success "Solution to Exercise 3"

        ```python
        print("hello".isidentifier())  # True
        print("变量".isidentifier())    # True

        # Most emoji are NOT valid identifiers
        print("\U0001F600".isidentifier())  # False (😀)
        ```

    Emoji are classified as symbols, not letters, so they cannot be used as identifiers.
"""

def append_exercises():
    for rel_path, content in EXERCISES.items():
        full_path = os.path.join(BASE, rel_path)
        if not os.path.exists(full_path):
            print(f"SKIP (not found): {full_path}")
            continue
        with open(full_path, 'r') as f:
            existing = f.read()
        if "## Exercises" in existing:
            print(f"SKIP (already has exercises): {rel_path}")
            continue
        with open(full_path, 'a') as f:
            f.write(content)
        print(f"DONE: {rel_path}")

if __name__ == "__main__":
    append_exercises()
