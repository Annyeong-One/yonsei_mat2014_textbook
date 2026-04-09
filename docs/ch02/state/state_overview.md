
# State and Program Execution

## What is State?

At any point during a program's execution, there exists a collection of names and the objects they refer to. This collection is the program's **state**.

State is not a single variable or a single value. It is the complete snapshot of all name-to-object bindings that exist at a given moment. When you read a line of code and ask "what would `x` be right now?"---you are reasoning about state.

---

## State as Snapshot

Consider the following program:

```python
x = 10
y = x + 5
x = 20
```

The state changes at each line:

| After line | State |
|-----------|-------|
| `x = 10` | `x` -> `10` |
| `y = x + 5` | `x` -> `10`, `y` -> `15` |
| `x = 20` | `x` -> `20`, `y` -> `15` |

Notice that reassigning `x` does not affect `y`. The value of `y` was computed from the object that `x` referred to *at the time of the assignment*, not from the name `x` itself. There is no ongoing link between `y` and `x`.

This is a direct consequence of the name-binding model: `y = x + 5` evaluates `x + 5` to produce the object `15`, then binds `y` to that object. Once bound, `y` has no memory of how it was computed.

---

## Assignments Change State

Every assignment statement changes the program's state by creating or updating a name binding.

```python
count = 0          # state: {count: 0}
count = count + 1  # state: {count: 1}
count = count + 1  # state: {count: 2}
```

The right-hand side is evaluated first using the *current* state. Then the result is bound to the left-hand name, producing a *new* state. Program execution is, at its core, a sequence of state transitions driven by assignments and expressions.

This perspective clarifies what a program does: it transforms state step by step until it reaches a result.

---

## Function Calls Create Local State

When a function is called, Python creates a **new namespace** for that call. The function's parameters and local variables live in this namespace, separate from the caller's state.

```python
def double(n):
    result = n * 2
    return result

x = 5
y = double(x)
```

During the call `double(x)`, the following local state exists inside the function:

| Name | Object |
|------|--------|
| `n` | `5` |
| `result` | `10` |

This local state is created when the function is called and destroyed when it returns. The caller's state (`x`, `y`) and the function's state (`n`, `result`) are separate namespaces.

The returned value `10` flows back to the caller and is bound to `y`, updating the caller's state. This is the primary mechanism by which data moves between functions: arguments flow in through parameter binding, and results flow out through return values.

---

## The Big Picture

Understanding state gives you a mental framework for reasoning about any program:

1. **Read the code line by line.** At each assignment, update the state snapshot.
2. **Evaluate expressions using the current state.** Names resolve to whatever objects they are currently bound to.
3. **Function calls create temporary local states.** These are isolated from the caller but connected through arguments and return values.

This model---state as a sequence of snapshots, transformed by assignments and function calls---is the foundation for everything else in this chapter. The sections that follow explore how assignment works in detail, what happens when objects are shared between names, and how data flows through function boundaries.
