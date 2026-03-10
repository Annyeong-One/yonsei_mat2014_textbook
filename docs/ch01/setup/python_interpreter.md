# Python Interpreter


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Once Python is installed, interaction happens through the **interpreter** and the **REPL** (Read–Eval–Print Loop).

---

## What is the Python

The Python interpreter:
- executes Python code,
- can run scripts or interactive commands,
- translates Python into bytecode executed by the runtime.

It is invoked with:
```bash
python
```

---

## The REPL

The REPL allows interactive experimentation:
```text
>>> 2 + 2
4
>>> import math
>>> math.sqrt(9)
3.0
```

This is invaluable for learning and quick testing.

---

## Exiting the REPL

You can exit by:
- typing `exit()`,
- pressing `Ctrl+D` (Unix/macOS),
- pressing `Ctrl+Z` then Enter (Windows).

---

## Running scripts

To run a Python file:
```bash
python script.py
```

Scripts are used for larger programs, while the REPL is ideal for exploration.

---

## IPython and enhanced

Tools like IPython provide:
- syntax highlighting,
- better error messages,
- shell integration.

They are recommended for quantitative work.

---

## Key takeaways

- The interpreter runs Python code.
- The REPL enables interactive exploration.
- Enhanced REPLs improve productivity.
