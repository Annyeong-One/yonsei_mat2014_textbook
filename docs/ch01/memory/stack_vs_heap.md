# Stack vs Heap (Conceptual Model)

Understanding Python’s **memory model** starts with the conceptual distinction between the *stack* and the *heap*. This distinction explains variable lifetimes, performance, and reference behavior.

---

## 1. The stack (conceptually)

The stack stores:
- function call frames,
- local variable *names*,
- return addresses.

Characteristics:
- managed automatically,
- fast allocation/deallocation,
- scoped to function execution.

In Python, stack frames hold **references**, not actual objects.

---

## 2. The heap

The heap stores:
- all Python objects,
- dynamically allocated data,
- objects with arbitrary lifetimes.

Characteristics:
- managed by the interpreter,
- objects persist beyond function scope,
- reclaimed by garbage collection.

---

## 3. Python’s abstraction

Python hides low-level memory details:
- you never allocate or free memory manually,
- variables are *names bound to objects*,
- objects always live on the heap.

---

## Key takeaways

- Stack holds references and call frames.
- Heap holds all Python objects.
- Python abstracts away manual memory management.
