# Python Execution Model

Is Python compiled or interpreted? The answer is **both** — Python compiles source code to bytecode, then interprets the bytecode. Understanding this model explains why some operations are fast and others are slow.

---

## Compiled vs Interpreted Languages

### Compiled Languages (C, C++, Rust)

```
Source Code (.c) → Compiler → Machine Code (.exe) → CPU
```

- Compiled once, runs directly on hardware
- Fast execution
- Platform-specific binaries
- Errors caught at compile time

### Interpreted Languages (Old BASIC)

```
Source Code → Interpreter → Execute line by line
```

- No compilation step
- Slower execution
- Cross-platform source code
- Errors found at runtime

### Python: Hybrid Approach

```
Source Code (.py) → Compiler → Bytecode (.pyc) → Interpreter (PVM) → CPU
```

Python compiles to **bytecode**, then the Python Virtual Machine (PVM) interprets it.

---

## Python's Execution Steps

### Step 1: Compilation to Bytecode

```python
# hello.py
print("Hello, World!")
```

When you run this, Python:
1. Parses the source code
2. Compiles it to bytecode
3. Stores bytecode in `.pyc` files (in `__pycache__/`)

### Step 2: Bytecode Interpretation

The Python Virtual Machine (PVM) reads bytecode instructions and executes them one by one. This per-instruction overhead is what makes Python slower than compiled languages.

---

## Viewing Bytecode

Use the `dis` module to disassemble Python code:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output:
```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

This reveals the low-level operations executed by the VM.

---

## The `__pycache__` Directory

Python caches compiled bytecode:

```
my_project/
├── main.py
├── utils.py
└── __pycache__/
    ├── main.cpython-311.pyc
    └── utils.cpython-311.pyc
```

- `.pyc` files contain bytecode
- `cpython-311` indicates Python version
- Speeds up subsequent imports
- Automatically regenerated when source changes

### Creating `.pyc` Files Manually

```python
import py_compile

py_compile.compile('my_script.py')
```

Or compile entire directory:

```bash
python -m compileall .
```

---

## Why This Matters: Order of Definition

Because Python interprets line by line, **order matters**:

### Bug: Using Before Defining

```python
# This will fail!
ops = (add, subtract)  # NameError: name 'add' is not defined

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

### Fix: Define Before Using

```python
# Define first
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Then use
ops = (add, subtract)  # Works!
```

Python executes top-to-bottom. When it sees `add` in the tuple, the function hasn't been defined yet.

---

## Running Python Scripts

### From Command Line

```bash
python script.py
```

### What Happens

1. Python reads `script.py`
2. Compiles to bytecode (in memory or `.pyc`)
3. PVM executes bytecode
4. Program runs

### The `if __name__ == "__main__":` Guard

```python
# my_module.py
def main():
    print("Running as script")

if __name__ == "__main__":
    main()
```

- When run directly: `__name__` is `"__main__"` → `main()` executes
- When imported: `__name__` is `"my_module"` → `main()` doesn't execute

---

## Performance: Where Python is Slow

Python is slow when:

- **Looping in pure Python**: Each iteration has VM overhead
- **Creating many small objects**: Memory allocation cost
- **Calling functions repeatedly in tight loops**: Function call overhead

```python
# Slow: Pure Python loop
total = 0
for i in range(1_000_000):
    total += i
```

### Why Python is "Slow"

1. **Dynamic typing**: Type checks at runtime
2. **Interpretation**: Bytecode interpreted, not native machine code
3. **GIL**: Global Interpreter Lock limits multi-threading

---

## Performance: Where Python is Fast

Python is fast when:

- **Delegating to C extensions**: NumPy, pandas, etc.
- **Using built-in functions**: Implemented in C
- **Minimizing Python-level loops**: Vectorized operations

```python
# Fast: NumPy vectorized (C extension)
import numpy as np
total = np.arange(1_000_000).sum()
```

### Mental Model for Performance

Think in terms of:
- Reducing Python-level operations
- Pushing work into optimized libraries
- Clarity before optimization (profile first!)

---

## Python Implementations

### CPython (Standard)

- Reference implementation
- Written in C
- Compiles to bytecode, interprets with PVM
- What you get from python.org

### PyPy

- JIT (Just-In-Time) compiler
- Much faster for long-running programs
- Compatible with most Python code

### Jython

- Python on the Java Virtual Machine
- Compiles to Java bytecode

### IronPython

- Python on .NET
- Compiles to .NET bytecode

---

## Python 2 vs Python 3

Python 2 reached end-of-life in 2020. Key differences:

| Feature | Python 2 | Python 3 |
|---------|----------|----------|
| Print | `print "hello"` | `print("hello")` |
| Division | `5/2 = 2` (int) | `5/2 = 2.5` (float) |
| Strings | ASCII default | Unicode default |
| `range()` | Returns list | Returns iterator |
| `input()` | Evaluates input | Returns string |

### Always Use Python 3

```bash
python --version    # Should be 3.x
python3 --version   # Explicitly Python 3
```

---

## Summary

| Aspect | Details |
|--------|---------|
| Compilation | Source → Bytecode → PVM execution |
| Bytecode cache | `__pycache__/*.pyc` files |
| Order | Define before using (top-to-bottom execution) |
| Slow operations | Pure Python loops, many small objects, tight function calls |
| Fast operations | C extensions, built-ins, vectorized operations |
| Standard implementation | CPython (from python.org) |
| Faster alternative | PyPy (JIT compilation) |

**Key Takeaways**:

- Python is **compiled to bytecode**, then **interpreted** by the PVM
- The VM executes instruction by instruction, introducing overhead
- **Order matters**: Define before using
- Use `dis` module to inspect bytecode
- Use `if __name__ == "__main__":` for script entry points
- **Performance** comes from pushing work to C extensions and built-ins
- **Always use Python 3** (Python 2 is EOL)
