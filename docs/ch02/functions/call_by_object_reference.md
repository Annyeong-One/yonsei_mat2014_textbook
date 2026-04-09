
# Call by Object Reference

## The Mental Model

When you call a function in Python and pass an argument, what exactly happens to the data? This question is fundamental to understanding how functions interact with the rest of your program.

Many programmers coming from other languages try to classify Python as either "call-by-value" or "call-by-reference." Python is neither. Python uses a mechanism called **call-by-object-reference** (sometimes called **call-by-sharing**).

The core idea: **when you pass an argument to a function, the parameter name inside the function is bound to the same object as the argument outside the function.** No copy is made. No pointer is passed. The function receives another name for the same object.

Think of it this way: if you and a colleague both have a sticky note labeled with different names, but both sticky notes are stuck to the same physical box, you are both looking at the same box. What happens when one of you tries to change the box depends on whether the box *can* be changed.

## What Happens at the Call Site

```python
def greet(name):
    print(f"Hello, {name}")

message = "Alice"
greet(message)
```

When `greet(message)` executes:

1. Python evaluates the argument `message`, which refers to the string object `"Alice"`.
2. The parameter `name` is bound to that **same** string object.
3. Inside the function, `name` and `message` (in the caller's scope) both point to the same object.

We can verify this with `id()`:

```python
def show_id(x):
    print(f"Inside function: id = {id(x)}")

value = [1, 2, 3]
print(f"Before call:     id = {id(value)}")
show_id(value)
```

Output:

```
Before call:     id = 140234567890
Inside function: id = 140234567890
```

The ids match. There is one object, and two names referring to it.

## Comparison with C and C++

Understanding Python's calling convention is easier when contrasted with the two classical approaches.

### Call by Value (C)

In C, passing a variable to a function **copies** the value into the parameter. Modifications inside the function affect only the local copy.

```c
void increment(int x) {
    x = x + 1;  // modifies local copy only
}

int main() {
    int a = 5;
    increment(a);
    // a is still 5
}
```

**Python is not call-by-value.** No copy of the object is made when you pass an argument. The function receives a reference to the original object, not a duplicate.

### Call by Reference (C++)

In C++, you can declare a reference parameter that becomes an alias for the caller's variable. Reassigning the parameter reassigns the caller's variable.

```cpp
void increment(int &x) {
    x = x + 1;  // modifies the caller's variable directly
}

int main() {
    int a = 5;
    increment(a);
    // a is now 6
}
```

**Python is not call-by-reference.** Rebinding the parameter name inside the function (e.g., `x = new_value`) does **not** affect the caller's variable. It only changes what the local name points to.

### Call by Object Reference (Python)

Python sits between the two. The parameter shares the same object as the argument, but reassigning the parameter does not reassign the argument:

```python
def try_reassign(x):
    x = 99  # rebinds the local name x; does NOT affect the caller

a = 5
try_reassign(a)
print(a)  # 5 -- unchanged
```

However, if the shared object is **mutable**, the function can modify it through the shared reference:

```python
def append_item(lst):
    lst.append(42)  # mutates the shared object

my_list = [1, 2, 3]
append_item(my_list)
print(my_list)  # [1, 2, 3, 42] -- changed!
```

| Convention | Copy made? | Reassignment affects caller? | Mutation affects caller? |
| --- | --- | --- | --- |
| Call by value (C) | Yes | No | N/A (copy) |
| Call by reference (C++) | No | Yes | Yes |
| Call by object reference (Python) | No | No | Yes (if mutable) |

## Mutable vs Immutable: The Deciding Factor

The practical consequence of call-by-object-reference depends entirely on whether the object is mutable or immutable.

**Immutable objects** (int, float, str, tuple, frozenset): any operation that "changes" the value actually creates a new object and rebinds the name. The caller's binding is unaffected.

```python
def add_exclamation(text):
    text = text + "!"  # creates a new string, rebinds local name
    print(f"Inside: {text}")

greeting = "Hello"
add_exclamation(greeting)
print(f"Outside: {greeting}")
```

Output:

```
Inside: Hello!
Outside: Hello
```

**Mutable objects** (list, dict, set): operations that modify the object in place are visible to the caller, because both names still refer to the same object.

```python
def add_key(d):
    d["new_key"] = "new_value"  # modifies the shared dict

config = {"host": "localhost"}
add_key(config)
print(config)  # {'host': 'localhost', 'new_key': 'new_value'}
```

## Rebinding vs Mutating

The critical distinction is between **rebinding** a name and **mutating** an object.

- **Rebinding**: `x = something_new` makes the local name `x` point to a different object. The caller is unaffected.
- **Mutating**: `x.append(item)` or `x["key"] = val` changes the object that `x` points to. Since the caller's name points to the same object, the caller sees the change.

```python
def rebind(lst):
    lst = [10, 20, 30]  # rebinding -- no effect on caller
    print(f"Inside (rebind): {lst}")

def mutate(lst):
    lst.append(99)  # mutating -- caller sees this
    print(f"Inside (mutate): {lst}")

original = [1, 2, 3]

rebind(original)
print(f"After rebind: {original}")  # [1, 2, 3]

mutate(original)
print(f"After mutate: {original}")  # [1, 2, 3, 99]
```

Output:

```
Inside (rebind): [10, 20, 30]
After rebind: [1, 2, 3]
Inside (mutate): [1, 2, 3, 99]
After mutate: [1, 2, 3, 99]
```

## Summary

| Concept | Description |
| --- | --- |
| Call by object reference | Parameter is bound to the same object as the argument |
| No copy | The object itself is shared, not duplicated |
| Rebinding is local | Assigning to the parameter name does not affect the caller |
| Mutation is shared | Modifying a mutable object is visible to the caller |
| Immutable safety | Immutable objects cannot be mutated, so callers are always safe |

---

## Exercises

**Exercise 1.**
Consider the following code:

```python
def mystery(a, b):
    a = a + b
    b.append(a)

x = 10
y = [1, 2, 3]
mystery(x, y)
print(x)
print(y)
```

Predict the output. For each parameter (`a` and `b`), explain whether the function rebinds or mutates the object, and why `x` and `y` are or are not affected.

??? success "Solution to Exercise 1"
    Output:

    ```text
    10
    [1, 2, 3, 13]
    ```

    - `a = a + b`: This is rebinding. `a` starts bound to the int `10`. The expression `a + b` is not valid for int + list, so let us re-examine. Actually, `a + b` would raise a `TypeError` because you cannot add an `int` and a `list`.

    Let us correct the analysis. The expression `a + b` with `a = 10` (int) and `b = [1, 2, 3]` (list) raises `TypeError: unsupported operand type(s) for +: 'int' and 'list'`.

    **Corrected version** -- suppose the code were:

    ```python
    def mystery(a, b):
        a = a + 1
        b.append(a)

    x = 10
    y = [1, 2, 3]
    mystery(x, y)
    print(x)  # 10
    print(y)  # [1, 2, 3, 11]
    ```

    - `a = a + 1`: Rebinding. `a` is rebound to a new int `11`. Since `int` is immutable, `x` in the caller remains `10`.
    - `b.append(a)`: Mutation. `b` still refers to the same list as `y`. Appending `11` modifies that shared list. The caller sees `[1, 2, 3, 11]`.

    The key insight: `=` is always rebinding (local only), while `.append()` is mutation (shared).

---

**Exercise 2.**
Write a function `swap(a, b)` that attempts to swap two variables. Explain why this cannot work in Python:

```python
def swap(a, b):
    a, b = b, a

x = "hello"
y = "world"
swap(x, y)
print(x, y)
```

What does this tell you about the difference between Python's calling convention and C++ call-by-reference? How would you achieve a swap effect in Python?

??? success "Solution to Exercise 2"
    Output:

    ```text
    hello world
    ```

    The swap does not work. Inside `swap`, the local names `a` and `b` are rebound to each other's objects. But rebinding local names has no effect on the caller's names `x` and `y`. After the function returns, `x` still refers to `"hello"` and `y` still refers to `"world"`.

    In C++ with call-by-reference (`void swap(int &a, int &b)`), the parameters are true aliases for the caller's variables. Reassigning them reassigns the caller's variables. Python's call-by-object-reference does not provide this capability.

    To achieve a swap in Python, you simply do it at the call site:

    ```python
    x, y = y, x
    ```

    Alternatively, if the values are stored in a mutable container, the function can mutate the container:

    ```python
    def swap_in_list(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    data = ["hello", "world"]
    swap_in_list(data, 0, 1)
    print(data)  # ['world', 'hello']
    ```

---

**Exercise 3.**
A colleague claims: "Python is call-by-value because reassigning a parameter inside a function never affects the caller." Another colleague counters: "Python is call-by-reference because modifying a list inside a function affects the caller." Both are partially right but ultimately wrong. Explain why, using the following code as evidence:

```python
def test(data):
    data.append(4)       # line A
    data = [10, 20, 30]  # line B
    data.append(40)      # line C

original = [1, 2, 3]
test(original)
print(original)
```

Predict the output and explain what happens at each labeled line.

??? success "Solution to Exercise 3"
    Output:

    ```text
    [1, 2, 3, 4]
    ```

    Line-by-line analysis:

    - **Line A** (`data.append(4)`): `data` is bound to the same list as `original`. This mutates the shared object. `original` is now `[1, 2, 3, 4]`.
    - **Line B** (`data = [10, 20, 30]`): This **rebinds** the local name `data` to a brand-new list. `original` is unaffected and still refers to `[1, 2, 3, 4]`. From this point on, `data` and `original` refer to different objects.
    - **Line C** (`data.append(40)`): This mutates the new list `[10, 20, 30]` to become `[10, 20, 30, 40]`. Since this is a different object from `original`, the caller sees no effect.

    Why neither "call-by-value" nor "call-by-reference" is correct:

    - If Python were call-by-value, line A would not affect `original` (a copy would have been made). But it does affect `original`. So Python is not call-by-value.
    - If Python were call-by-reference, line B would reassign `original` to `[10, 20, 30]`. But it does not. So Python is not call-by-reference.

    Python is call-by-object-reference: the parameter shares the object (so mutation is visible), but the parameter is an independent name (so rebinding is local).
