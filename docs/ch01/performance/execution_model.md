# Python Execution

Python’s execution model explains why some operations are fast and others are slow, and how to reason about performance.

---

## Interpreted

Python code is:
1. parsed into bytecode,
2. executed by the Python virtual machine (VM),
3. evaluated instruction by instruction.

This introduces overhead compared to compiled languages.

---

## Bytecode and the VM

```python
import dis

def f(x):
    return x + 1

dis.dis(f)
```

This reveals low-level operations executed by the VM.

---

## Where Python is slow

Python is slow when:
- looping in pure Python,
- creating many small objects,
- calling functions repeatedly in tight loops.

---

## Where Python is fast

Python is fast when:
- delegating work to C extensions (NumPy, pandas),
- using built-in functions,
- minimizing Python-level loops.

---

## Mental model for

Think in terms of:
- reducing Python-level operations,
- pushing work into optimized libraries,
- clarity before optimization.

---

## Key takeaways

- Python runs on a VM with per-instruction overhead.
- Built-ins and libraries hide C-level speed.
- Performance comes from algorithmic thinking.
