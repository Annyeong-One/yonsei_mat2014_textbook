
# Functions and Call Stack

A **function** is a named block of code that performs a specific task.

Functions allow programs to:

- organize logic
- reuse code
- avoid repetition
- divide large problems into smaller parts

In Python, functions are defined with the `def` keyword.

```python
def greet():
    print("Hello")
````

A function does not run when it is defined. It runs only when it is **called**.

```python
greet()
```

```mermaid2
flowchart TD
    A[Function definition] --> B[Function call]
    B --> C[Execute function body]
    C --> D[Return to caller]
```

---

## 1. Defining a Function

A basic function definition looks like this:

```python
def greet():
    print("Hello")
```

This creates a function named `greet`.

To execute it, call it with parentheses:

```python
greet()
```

Output:

```text
Hello
```

---

## 2. Functions as Reusable Units

Functions allow the same logic to be reused many times.

```python
def show_line():
    print("=" * 10)

show_line()
show_line()
```

Output:

```text
==========
==========
```

Without functions, repeated code would need to be written over and over.

---

## 3. Calling Functions

A function call transfers control to the function body.

```python
def say_hi():
    print("Hi")

print("Before")
say_hi()
print("After")
```

Output:

```text
Before
Hi
After
```

This shows that the program temporarily moves into the function and then returns to the original flow.

---

## 4. Local Scope

Variables created inside a function are usually **local** to that function.

```python
def demo():
    x = 10
    print(x)

demo()
```

The variable `x` exists inside the function body and is not normally accessible outside it.

This helps functions remain self-contained and reduces accidental interference between parts of a program.

---

## 5. The Call Stack

When one function calls another, Python keeps track of the sequence of calls using the **call stack**.

A simplified view:

```mermaid2
flowchart TD
    A[main program] --> B[call f()]
    B --> C[call g()]
    C --> D[return from g()]
    D --> E[return from f()]
```

Example:

```python
def g():
    print("inside g")

def f():
    print("inside f")
    g()
    print("back in f")

f()
```

Output:

```text
inside f
inside g
back in f
```

The program enters `f`, then enters `g`, then returns from `g`, then finishes `f`.

---

## 6. Why the Call Stack Matters

The call stack helps explain:

* nested function calls
* recursion
* where execution resumes after a call
* why local variables belong to particular function calls

Each function call gets its own execution context.

This is why two calls to the same function do not normally interfere with each other’s local variables.

---

## 7. Functions That Do Not Return Explicitly

If a function does not explicitly use `return`, it returns `None`.

```python
def hello():
    print("Hello")

result = hello()
print(result)
```

Output:

```text
Hello
None
```

This is part of Python’s function model and is important to remember.

---

## 8. Worked Examples

### Example 1: simple reusable function

```python
def banner():
    print("Welcome")

banner()
banner()
```

Output:

```text
Welcome
Welcome
```

### Example 2: call order

```python
def first():
    print("first")

def second():
    print("second")

first()
second()
```

### Example 3: nested call

```python
def square(x):
    return x * x

def show_square(n):
    print(square(n))

show_square(5)
```

Output:

```text
25
```

---

## 9. Common Pitfalls

### Forgetting parentheses when calling

```python
greet
```

This refers to the function object, but does not call it.

### Confusing definition with execution

Defining a function does not automatically run it.

### Assuming printed output is a return value

A function may print something without returning that value.

---

## 10. Summary

Key ideas:

* a function is a reusable named block of code
* `def` defines a function
* calling a function transfers control to its body
* local variables belong to the function call
* Python tracks nested calls with the call stack
* functions without explicit `return` return `None`

Functions are one of the most important tools for structuring Python programs.