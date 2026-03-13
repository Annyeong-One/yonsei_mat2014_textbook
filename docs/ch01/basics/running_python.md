

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

```mermaid2
flowchart TD
    A[Python source code] --> B[Interpreter]
    B --> C[Bytecode compilation]
    C --> D[Python Virtual Machine]
    D --> E[Program output]
```

The interpreter translates Python code into **bytecode**, which is executed by the **Python Virtual Machine (PVM)**.

---


