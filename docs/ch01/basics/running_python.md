

# Running Python

Before writing programs, we must understand how Python code is executed.

Python code can be run in several ways:

| Method                                    | Description                      |
| ----------------------------------------- | -------------------------------- |
| Interactive interpreter                   | run commands one line at a time  |
| Script execution                          | run `.py` files                  |
| Jupyter notebooks                         | interactive code + documentation |
| Integrated development environments (IDE) | full programming environment     |

---

## 1. Interactive Interpreter

The Python interpreter allows immediate evaluation of expressions.

Example session:

```python
>>> 2 + 3
5
>>> "hello".upper()
'HELLO'
```

Each line entered into the interpreter is evaluated immediately.

---

## 2. Running a Script

Python programs are commonly stored in `.py` files.

Example file:

```python
print("Hello, Python!")
```

Run it from the command line:

```bash
python hello.py
```

Output:

```
Hello, Python!
```

---

## 3. Program Execution Model

When Python runs a script, it performs the following steps:

```mermaid
flowchart TD
    A[Python source code] --> B[Interpreter]
    B --> C[Bytecode compilation]
    C --> D[Python Virtual Machine]
    D --> E[Program output]
```

The interpreter translates Python code into **bytecode**, which is executed by the **Python Virtual Machine (PVM)**.

---

## Exercises

**Exercise 1.**
Open the Python interpreter and evaluate the following expressions one at a time. Write down the output of each before running them, then verify your predictions.

```python
>>> 10 + 20
>>> "hello" * 3
>>> type(3.14)
```

??? success "Solution to Exercise 1"
    ```python
    >>> 10 + 20
    30
    >>> "hello" * 3
    'hellohellohello'
    >>> type(3.14)
    <class 'float'>
    ```

    The interpreter evaluates each expression and prints the result immediately. `10 + 20` performs integer addition. `"hello" * 3` repeats the string three times. `type(3.14)` returns the type of the float literal.

---

**Exercise 2.**
Create a file called `greet.py` with the following content:

```python
name = "World"
print("Hello, " + name + "!")
```

Run the file from the command line. What command do you use? What is the output?

??? success "Solution to Exercise 2"
    Run from the terminal:

    ```bash
    python greet.py
    ```

    Output:

    ```
    Hello, World!
    ```

    On some systems you may need to use `python3 greet.py` instead. The interpreter reads the entire file, executes it top to bottom, and prints the result of the `print` call.

---

**Exercise 3.**
Explain the three stages that occur when Python runs a `.py` script. Describe the role of each stage.

??? success "Solution to Exercise 3"
    When Python runs a script, three stages occur:

    1. **Source code reading** -- The interpreter reads the `.py` file as text.
    2. **Bytecode compilation** -- The source code is compiled into bytecode, an intermediate, platform-independent representation.
    3. **Execution by the Python Virtual Machine (PVM)** -- The PVM executes the bytecode instructions and produces the program's output.

    This process happens automatically every time a script is run. The bytecode step is why Python is sometimes called a "compiled interpreted" language.

---

**Exercise 4.**
A student types `print("Hello")` in the interactive interpreter and sees `Hello` as output. They then type `"Hello"` (without `print`) and also see `'Hello'`. Explain why both produce visible output and describe the difference between the two results.

??? success "Solution to Exercise 4"
    In the interactive interpreter, any expression that evaluates to a non-`None` value is automatically displayed using its `repr` form. So typing `"Hello"` displays `'Hello'` (with quotes), because the interpreter shows the representation of the string object.

    When `print("Hello")` is used, the `print` function writes the string's **content** to standard output (without quotes), producing `Hello`. The `print` call itself returns `None`, which the interpreter does not display.

    Key difference: the bare expression shows the `repr` (with quotes), while `print` shows the `str` form (without quotes).

---

**Exercise 5.**
Write a Python script called `calculator.py` that defines two variables `a = 7` and `b = 3`, then prints their sum, difference, product, and quotient on separate lines. Run the script and verify the output.

??? success "Solution to Exercise 5"
    File `calculator.py`:

    ```python
    a = 7
    b = 3

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    ```

    Run:

    ```bash
    python calculator.py
    ```

    Output:

    ```
    10
    4
    21
    2.3333333333333335
    ```

    Note that `/` performs true division and returns a `float`, even when both operands are integers.
